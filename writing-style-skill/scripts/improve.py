#!/usr/bin/env python3
"""
Self-Improving Skill — Improver

Estrae regole dalle modifiche umane e aggiorna il SKILL.md di destinazione.

Utilizzo:
    python3 improve.py extract [--days 7] [--date 2026-03-17]
    python3 improve.py auto                  # estrai + applica automaticamente P0 (per cron)
    python3 improve.py show                  # visualizza tutte le proposte
    python3 improve.py apply <proposal_id>   # applica una proposta specifica
    python3 improve.py rollback              # ripristina l'ultima applicazione

Variabili d'ambiente:
    SKILL_LOG_DIR      — directory dei log
    SKILL_TARGET_PATH  — percorso del SKILL.md di destinazione
    SKILL_PROPOSAL_DIR — directory delle proposte
    SKILL_BACKUP_DIR   — directory dei backup
"""

import sys
import json
import os
import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime, timedelta

# Percorsi predefiniti — rileva automaticamente OpenClaw (~/.openclaw) o Claude Code (~/.claude)
def _detect_base():
    """Rileva la directory base per l'archiviazione dei dati"""
    # Priorità: variabile d'ambiente > ~/clawd > ~/.openclaw > ~/.claude > ~/.self-improving
    if os.environ.get("SKILL_BASE_DIR"):
        return Path(os.environ["SKILL_BASE_DIR"])
    candidates = [
        Path.home() / "clawd" / "memory",
        Path.home() / ".openclaw" / "memory",
        Path.home() / ".claude" / "memory",
    ]
    for c in candidates:
        if c.parent.exists():
            return c
    return Path.home() / ".self-improving" / "memory"

_BASE = _detect_base()
DEFAULT_LOG_DIR = _BASE / "skill-runs" / "default"
DEFAULT_PROPOSAL_DIR = _BASE / "skill-proposals" / "default"
DEFAULT_BACKUP_DIR = _BASE / "skill-backups" / "default"


def get_paths(args=None):
    """Risolve la configurazione di tutti i percorsi"""
    skill_name = "default"
    if args and hasattr(args, 'skill') and args.skill:
        skill_name = Path(args.skill).name

    base = Path.home() / "clawd" / "memory"

    log_dir = Path(os.environ.get("SKILL_LOG_DIR",
                   getattr(args, 'log_dir', None) or
                   str(base / "skill-runs" / skill_name)))

    proposal_dir = Path(os.environ.get("SKILL_PROPOSAL_DIR",
                        getattr(args, 'proposal_dir', None) or
                        str(base / "skill-proposals" / skill_name)))

    backup_dir = Path(os.environ.get("SKILL_BACKUP_DIR",
                      getattr(args, 'backup_dir', None) or
                      str(base / "skill-backups" / skill_name)))

    # SKILL.md di destinazione
    if os.environ.get("SKILL_TARGET_PATH"):
        target = Path(os.environ["SKILL_TARGET_PATH"])
    elif args and hasattr(args, 'target') and args.target:
        target = Path(args.target)
    elif args and hasattr(args, 'skill') and args.skill:
        target = Path(args.skill) / "SKILL.md"
    else:
        target = None

    for d in (log_dir, proposal_dir, backup_dir):
        d.mkdir(parents=True, exist_ok=True)

    return log_dir, proposal_dir, backup_dir, target


def read_log_entries(log_file):
    if not log_file.exists():
        return []
    entries = []
    with log_file.open("r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def collect_edits(log_dir, days=1, date_str=None):
    """Raccoglie i record final/edited con modifiche effettive"""
    edits = []
    if date_str:
        log_file = log_dir / f"{date_str}.jsonl"
        entries = read_log_entries(log_file)
        edits.extend([e for e in entries
                      if e["type"] in ("final", "edited") and not e.get("no_change")])
    else:
        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            log_file = log_dir / f"{date}.jsonl"
            entries = read_log_entries(log_file)
            edits.extend([e for e in entries
                          if e["type"] in ("final", "edited") and not e.get("no_change")])
    return edits


def call_llm(prompt, timeout=180):
    """Chiama il LLM — rileva automaticamente il CLI disponibile (claude / openclaw / llm)"""
    # Priorità: claude CLI → openclaw exec → llm CLI generico
    candidates = [
        ["claude", "--print", "--model", "sonnet"],  # Claude Code
        ["claude", "--print"],                         # Claude Code (modello predefinito)
        ["llm", "-m", "claude-sonnet"],               # llm CLI di Simon Willison
        ["llm"],                                       # llm CLI predefinito
    ]
    for cmd in candidates:
        try:
            result = subprocess.run(cmd, input=prompt, capture_output=True,
                                    text=True, timeout=timeout)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue

    # fallback: usa IMPROVE_LLM_CMD se la variabile d'ambiente è impostata
    custom_cmd = os.environ.get("IMPROVE_LLM_CMD")
    if custom_cmd:
        try:
            result = subprocess.run(custom_cmd.split(), input=prompt,
                                    capture_output=True, text=True, timeout=timeout)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

    print("❌ Chiamata al LLM fallita. Metodi supportati:")
    print("   - Installa Claude Code CLI (claude --print)")
    print("   - Installa llm CLI (pip install llm)")
    print("   - Imposta la variabile d'ambiente IMPROVE_LLM_CMD")
    return None


def extract_improvements(args):
    log_dir, proposal_dir, _, target = get_paths(args)
    days = getattr(args, 'days', 1) or 1
    date_str = getattr(args, 'date', None)

    edits = collect_edits(log_dir, days=days, date_str=date_str)
    if not edits:
        print("⚠️  Nessuna modifica registrata")
        return None

    print(f"📊 Trovate {len(edits)} modifiche, analisi in corso...")

    # Leggi il SKILL.md attuale
    current_skill = ""
    if target and target.exists():
        current_skill = target.read_text()

    # Costruisci i dati di confronto
    edit_summaries = []
    for i, edit in enumerate(edits):
        orig = edit.get("original_content", "")[:3000]
        final = edit.get("final_content", edit.get("edited_content", ""))[:3000]
        ctx = edit.get("context", {})
        edit_summaries.append({
            "index": i + 1,
            "account": ctx.get("account", "unknown"),
            "content_type": ctx.get("content_type", "unknown"),
            "original": orig,
            "final": final,
        })

    proposal_id = datetime.now().strftime("%Y%m%d-%H%M%S")

    prompt = f"""Sei un assistente al miglioramento della writing style skill.

Analizza le modifiche apportate dall'utente ai testi generati dall'IA ed estrai nuove regole da aggiungere a SKILL.md.

## SKILL.md attuale (ultimi 3000 caratteri, per evitare duplicati)
{current_skill[-3000:]}

## Registro delle modifiche (original vs final)
{json.dumps(edit_summaries, ensure_ascii=False, indent=2)}

## Requisiti
1. Confronta original e final e individua le modifiche sistematiche
2. Estrai solo le modifiche con un pattern ricorrente (almeno 2 volte, oppure 1 sola ma con variazione ampia e chiara)
3. Non estrarre regole già presenti in SKILL.md
4. Ogni regola deve essere concretamente applicabile

## Formato di output

---
id: {proposal_id}
date: {datetime.now().isoformat()}
source: {len(edits)} edits
status: pending
---

# Proposta di miglioramento

## Suggerimenti estratti

### 1. Nuove parole vietate
- **`parola`** → alternativa: "YYY" | motivazione: ... | priorità: **P0/P1/P2**

### 2. Nuove regole di stile
- Descrizione della regola | motivazione: ... | priorità: **P0/P1/P2**

### 3. Anti-pattern
- Descrizione | motivazione: ... | priorità: **P0/P1/P2**

P0=alta affidabilità (più occorrenze), P1=media affidabilità, P2=bassa affidabilità (1 sola occorrenza)
"""

    suggestions = call_llm(prompt)
    if not suggestions:
        return None

    proposal_file = proposal_dir / f"{proposal_id}.md"
    proposal_file.write_text(suggestions)

    print(f"✅ Suggerimenti di miglioramento salvati: {proposal_file}")
    print(f"\n{suggestions[:2000]}")
    if len(suggestions) > 2000:
        print(f"\n... (contenuto completo nel file)")
    return proposal_id


def show_proposals(args):
    _, proposal_dir, _, _ = get_paths(args)
    proposals = list(proposal_dir.glob("*.md"))

    if not proposals:
        print("⚠️  Nessuna proposta")
        return

    print(f"\n📋 {len(proposals)} proposte totali:\n")
    for p in sorted(proposals, reverse=True):
        content = p.read_text()
        status = "unknown"
        for line in content.split("\n")[:10]:
            if line.startswith("status:"):
                status = line.split(":", 1)[1].strip()
        icon = {"pending": "⏳", "applied": "✅", "rejected": "❌"}.get(
            status.split("(")[0].strip(), "❓")
        print(f"  {icon} {p.stem} — {status}")


def backup_skill(target, backup_dir):
    if not target or not target.exists():
        return None
    name = f"SKILL-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    backup_path = backup_dir / name
    shutil.copy2(target, backup_path)
    print(f"📦 Backup: {backup_path}")
    return backup_path


def apply_proposal(args):
    _, proposal_dir, backup_dir, target = get_paths(args)
    proposal_id = args.proposal_id
    proposal_file = proposal_dir / f"{proposal_id}.md"

    if not proposal_file.exists():
        print(f"❌ Proposta non trovata: {proposal_id}")
        return

    if not target or not target.exists():
        print(f"❌ SKILL.md di destinazione non trovato (usa --skill o --target per specificarlo)")
        return

    proposal_content = proposal_file.read_text()
    current_skill = target.read_text()

    auto_mode = getattr(args, 'auto', False)
    filter_level = "P0" if auto_mode else "P0 e P1"

    backup_skill(target, backup_dir)

    prompt = f"""Unisci le regole **{filter_level}** della proposta di miglioramento in SKILL.md.

Istruzioni:
1. Nuove parole vietate → aggiungile alla sezione parole vietate
2. Nuove regole di stile → aggiungile alla sezione corrispondente
3. Non eliminare le regole esistenti, non modificare la struttura del file
4. version +0.1

## Proposta
{proposal_content}

## SKILL.md attuale
{current_skill}

Restituisci il SKILL.md aggiornato completo. Senza blocchi di codice."""

    updated = call_llm(prompt, timeout=300)
    if not updated:
        print("❌ Unione fallita")
        return

    target.write_text(updated)

    new_content = proposal_content.replace(
        "status: pending",
        f"status: applied ({datetime.now().strftime('%Y-%m-%d')})")
    proposal_file.write_text(new_content)

    print(f"✅ Proposta {proposal_id} applicata")
    print(f"💡 Per ripristinare: python3 improve.py rollback")


def auto_improve(args):
    log_dir, _, _, _ = get_paths(args)
    edits = collect_edits(log_dir, days=7)

    if not edits:
        print("⚠️  Nessuna modifica negli ultimi 7 giorni, salto")
        return

    print(f"🤖 Modalità automatica: {len(edits)} modifiche")

    args.days = 7
    args.date = None
    proposal_id = extract_improvements(args)

    if not proposal_id:
        return

    _, proposal_dir, _, _ = get_paths(args)
    content = (proposal_dir / f"{proposal_id}.md").read_text()

    if "P0" not in content:
        print("ℹ️  Nessuna regola P0, salto l'applicazione automatica")
        return

    print("\n🔄 Applicazione automatica delle regole P0...")
    apply_args = argparse.Namespace(**vars(args))
    apply_args.proposal_id = proposal_id
    apply_args.auto = True
    apply_proposal(apply_args)


def rollback(args):
    _, _, backup_dir, target = get_paths(args)

    if not target:
        print("❌ SKILL.md di destinazione non specificato")
        return

    backups = sorted(backup_dir.glob("SKILL-*.md"), reverse=True)
    if not backups:
        print("❌ Nessun backup disponibile")
        return

    latest = backups[0]
    # Salva la versione attuale prima del ripristino
    if target.exists():
        emergency = backup_dir / f"SKILL-pre-rollback-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        shutil.copy2(target, emergency)

    shutil.copy2(latest, target)
    print(f"✅ Ripristinato a: {latest.name}")


def add_common_args(parser):
    parser.add_argument("--skill", help="Directory della skill di destinazione")
    parser.add_argument("--target", help="Percorso del SKILL.md di destinazione")
    parser.add_argument("--log-dir", help="Directory dei log")
    parser.add_argument("--proposal-dir", help="Directory delle proposte")


def main():
    parser = argparse.ArgumentParser(description="Self-Improving Skill — Improver")
    subparsers = parser.add_subparsers(dest="action")

    p_ext = subparsers.add_parser("extract", help="Estrai suggerimenti di miglioramento")
    p_ext.add_argument("--date", help="Specifica una data")
    p_ext.add_argument("--days", type=int, default=1)
    add_common_args(p_ext)

    p_show = subparsers.add_parser("show", help="Visualizza le proposte")
    add_common_args(p_show)

    p_apply = subparsers.add_parser("apply", help="Applica una proposta")
    p_apply.add_argument("proposal_id")
    add_common_args(p_apply)

    p_auto = subparsers.add_parser("auto", help="Estrai e applica automaticamente P0")
    add_common_args(p_auto)

    p_rb = subparsers.add_parser("rollback", help="Ripristina la versione precedente")
    add_common_args(p_rb)

    args = parser.parse_args()
    if not args.action:
        parser.print_help()
        sys.exit(1)

    actions = {
        "extract": extract_improvements,
        "show": show_proposals,
        "apply": apply_proposal,
        "auto": auto_improve,
        "rollback": rollback,
    }
    actions[args.action](args)


if __name__ == "__main__":
    main()
