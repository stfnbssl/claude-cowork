#!/usr/bin/env python3
"""
Self-Improving Skill — Observation Layer

Registratore generico original → final. Adatto a qualsiasi ciclo "generato dall'IA → modificato dall'utente".

Utilizzo:
    python3 observe.py record-original article.md [--text "..."] [--account X] [--content-type article]
    python3 observe.py record-final article.md [--match <hash>] [--text "..."]
    python3 observe.py pending
    python3 observe.py stats

Variabili d'ambiente:
    SKILL_LOG_DIR  — directory dei log (default: ~/clawd/memory/skill-runs/default/)
"""

import sys
import json
import os
import argparse
from pathlib import Path
from datetime import datetime, timedelta
import hashlib

# Directory dei log — rileva automaticamente OpenClaw / Claude Code / standalone
def _detect_base():
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

DEFAULT_LOG_DIR = _detect_base() / "skill-runs" / "default"


def get_log_dir(args=None):
    """Determina la directory dei log per priorità: --log-dir > SKILL_LOG_DIR > default"""
    if args and hasattr(args, 'log_dir') and args.log_dir:
        d = Path(args.log_dir)
    elif os.environ.get("SKILL_LOG_DIR"):
        d = Path(os.environ["SKILL_LOG_DIR"])
    elif args and hasattr(args, 'skill') and args.skill:
        skill_name = Path(args.skill).name
        d = Path.home() / "clawd" / "memory" / "skill-runs" / skill_name
    else:
        d = DEFAULT_LOG_DIR
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_log_file(log_dir, date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    return log_dir / f"{date_str}.jsonl"


def compute_hash(content):
    return hashlib.md5(content.encode()).hexdigest()[:8]


def get_content(args):
    if hasattr(args, 'text') and args.text:
        return args.text
    if hasattr(args, 'stdin') and args.stdin:
        return sys.stdin.read()
    if hasattr(args, 'file') and args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"❌ File non trovato: {args.file}")
            sys.exit(1)
        return p.read_text()
    return None


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


def find_unmatched(log_dir, days=14):
    """Trova i record con original ma senza final (compatibile con i tipi edited/no-change precedenti)"""
    all_originals = {}
    all_matched = set()

    for i in range(days):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        entries = read_log_entries(get_log_file(log_dir, date))
        for e in entries:
            if e["type"] == "original":
                e["_date"] = date
                all_originals[e["content_hash"]] = e
            elif e["type"] in ("final", "edited", "no-change"):
                all_matched.add(e["content_hash"])

    return {h: o for h, o in all_originals.items() if h not in all_matched}


def record_original(args):
    content = get_content(args)
    if not content:
        print("❌ È necessario fornire il contenuto (percorso file, --text o --stdin)")
        sys.exit(1)

    log_dir = get_log_dir(args)
    content_hash = compute_hash(content)

    context = {}
    if hasattr(args, 'account') and args.account:
        context["account"] = args.account
    if hasattr(args, 'content_type') and args.content_type:
        context["content_type"] = args.content_type

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "type": "original",
        "content_hash": content_hash,
        "file": str(args.file) if hasattr(args, 'file') and args.file else None,
        "content": content,
        "context": context,
        "char_count": len(content),
    }

    log_file = get_log_file(log_dir)
    with log_file.open("a") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    print(f"✅ Bozza registrata: {content_hash}")
    print(f"📝 Caratteri: {len(content)}")
    print(f"📁 Log: {log_file}")
    return content_hash


def record_final(args):
    content = get_content(args)
    if not content:
        print("❌ È necessario fornire il contenuto della versione finale")
        sys.exit(1)

    log_dir = get_log_dir(args)
    target_hash = getattr(args, 'match', None)

    if target_hash:
        # Hash specificato, ricerca su più giorni
        original = None
        for i in range(14):
            date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            entries = read_log_entries(get_log_file(log_dir, date))
            for e in entries:
                if e["type"] == "original" and e["content_hash"] == target_hash:
                    original = e
                    break
            if original:
                break
        if not original:
            print(f"❌ Nessuna bozza trovata con hash {target_hash}")
            sys.exit(1)
    else:
        # Abbinamento automatico all'original non accoppiato più recente
        unmatched = find_unmatched(log_dir, 14)
        if not unmatched:
            print("❌ Nessuna bozza in attesa di abbinamento")
            sys.exit(1)
        target_hash = list(unmatched.keys())[-1]
        original = unmatched[target_hash]

    is_same = content.strip() == original["content"].strip()

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "type": "final",
        "content_hash": target_hash,
        "original_content": original["content"],
        "final_content": content,
        "original_char_count": len(original["content"]),
        "final_char_count": len(content),
        "context": original.get("context", {}),
        "no_change": is_same,
    }

    log_file = get_log_file(log_dir)
    with log_file.open("a") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    if is_same:
        print(f"✅ Versione finale registrata: {target_hash} (nessuna modifica — feedback positivo)")
    else:
        diff_pct = ((len(content) - len(original["content"])) / max(len(original["content"]), 1)) * 100
        print(f"✅ Versione finale registrata: {target_hash}")
        print(f"📝 Bozza: {len(original['content'])} caratteri → Finale: {len(content)} caratteri ({diff_pct:+.1f}%)")
    print(f"📁 Log: {log_file}")


def show_pending(args):
    log_dir = get_log_dir(args)
    unmatched = find_unmatched(log_dir, 14)

    if not unmatched:
        print("✅ Tutti abbinati")
        return

    print(f"\n⏳ {len(unmatched)} in attesa di abbinamento:\n")
    for h, entry in unmatched.items():
        preview = entry["content"][:80].replace("\n", " ")
        ctx = entry.get("context", {})
        account = ctx.get("account", "?")
        date = entry.get("_date", "?")
        print(f"  📄 {h} | {date} | {account}")
        print(f"     {preview}...")
        print()


def show_stats(args):
    log_dir = get_log_dir(args)
    all_files = sorted(log_dir.glob("*.jsonl"))

    total_originals = 0
    total_finals = 0
    total_no_change = 0
    total_changed = 0

    for log_file in all_files:
        entries = read_log_entries(log_file)
        total_originals += sum(1 for e in entries if e["type"] == "original")
        finals = [e for e in entries if e["type"] in ("final", "edited")]
        total_finals += len(finals)
        total_no_change += sum(1 for e in finals if e.get("no_change"))
        total_changed += sum(1 for e in finals if not e.get("no_change"))

    pending = find_unmatched(log_dir, 14)

    print(f"\n📊 Self-Improving Skill — Statistiche di osservazione")
    print(f"{'='*40}")
    print(f"📁 Giorni di log: {len(all_files)}")
    print(f"📝 Bozze: {total_originals}")
    print(f"✅ Abbinate: {total_finals}")
    print(f"   ├ Con modifiche: {total_changed}")
    print(f"   └ Senza modifiche: {total_no_change}")
    print(f"⏳ In attesa: {len(pending)}")
    if total_finals > 0:
        print(f"📈 Tasso di modifica: {total_changed}/{total_finals} = {total_changed/total_finals*100:.0f}%")


def add_common_args(parser):
    """Aggiunge gli argomenti comuni"""
    parser.add_argument("--skill", help="Nome della directory della skill di destinazione (per individuare la directory dei log)")
    parser.add_argument("--log-dir", help="Directory dei log personalizzata")


def main():
    parser = argparse.ArgumentParser(description="Self-Improving Skill — Observation Layer")
    subparsers = parser.add_subparsers(dest="action")

    # record-original
    p_orig = subparsers.add_parser("record-original", help="Registra la bozza dell'IA")
    p_orig.add_argument("file", nargs="?", help="Percorso del file")
    p_orig.add_argument("--text", help="Passa il testo direttamente")
    p_orig.add_argument("--stdin", action="store_true", help="Leggi da stdin")
    p_orig.add_argument("--account", help="Account di pubblicazione")
    p_orig.add_argument("--content-type", help="Tipo di contenuto")
    add_common_args(p_orig)

    # record-final
    p_final = subparsers.add_parser("record-final", help="Registra la versione finale")
    p_final.add_argument("file", nargs="?", help="Percorso del file")
    p_final.add_argument("--text", help="Passa il testo direttamente")
    p_final.add_argument("--stdin", action="store_true", help="Leggi da stdin")
    p_final.add_argument("--match", help="Hash della bozza da abbinare")
    add_common_args(p_final)

    # pending
    p_pending = subparsers.add_parser("pending", help="Visualizza le bozze in attesa di abbinamento")
    add_common_args(p_pending)

    # stats
    p_stats = subparsers.add_parser("stats", help="Statistiche generali")
    add_common_args(p_stats)

    args = parser.parse_args()
    if not args.action:
        parser.print_help()
        sys.exit(1)

    actions = {
        "record-original": record_original,
        "record-final": record_final,
        "pending": show_pending,
        "stats": show_stats,
    }
    actions[args.action](args)


if __name__ == "__main__":
    main()
