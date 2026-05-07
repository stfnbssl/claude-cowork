# Gestione dei file — Come funziona davvero

## Il principio fondamentale

Gli script `observe.py` e `improve.py` **non gestiscono i tuoi file di lavoro**. Non creano cartelle per le bozze, non spostano nulla, non ti impongono una struttura. Fanno una cosa sola: leggono il contenuto di un file che gli indichi e lo copiano dentro il proprio sistema di log interno.

Questo significa che i tuoi testi — bozze prodotte da Claude, versioni corrette — possono stare ovunque sul tuo computer. Sono fatti tuoi. Gli script li leggono al volo e poi se ne dimenticano.

---

## Dove finisce il contenuto dei tuoi testi

Quando lanci `record-original` o `record-final`, il testo del file viene salvato interamente in un file di log in formato JSONL (una riga JSON per ogni operazione). Questi log sono la vera memoria del sistema.

### Percorso dei log

Gli script rilevano automaticamente l'ambiente e scelgono la directory base in questo ordine di priorità:

1. Variabile d'ambiente `SKILL_BASE_DIR` (se impostata)
2. `~/clawd/memory/` (Cowork)
3. `~/.openclaw/memory/`
4. `~/.claude/memory/` (Claude Code standalone)
5. `~/.self-improving/memory/` (fallback)

In Cowork, la directory base sarà quasi certamente `~/clawd/memory/`.

### Struttura completa delle directory interne

```
~/clawd/memory/
├── skill-runs/
│   └── writing-style-skill/       ← log giornalieri delle osservazioni
│       ├── 2026-05-01.jsonl
│       ├── 2026-05-06.jsonl
│       └── 2026-05-07.jsonl
├── skill-proposals/
│   └── writing-style-skill/       ← proposte di miglioramento generate da improve.py
│       └── 20260507-143022.md
└── skill-backups/
    └── writing-style-skill/       ← backup automatici di SKILL.md prima di ogni modifica
        ├── SKILL-20260506-091200.md
        └── SKILL-20260507-143025.md
```

Il nome della sottocartella (`writing-style-skill`) corrisponde al nome della directory della skill. Per questo è importante usare sempre il parametro `--skill .` quando lanci gli script dall'interno della cartella della skill: così entrambi gli script concordano su dove leggere e scrivere i log.

### Cosa contiene un file di log JSONL

Ogni riga è un evento JSON. Un file di log tipico contiene sia i record `original` che i record `final`:

```json
{"timestamp": "2026-05-07T10:30:00", "type": "original", "content_hash": "a3f7c2b1", "file": "/path/to/bozza.md", "content": "testo completo della bozza...", "char_count": 1240, "context": {"account": "blog", "content_type": "articolo"}}
{"timestamp": "2026-05-07T11:45:00", "type": "final", "content_hash": "a3f7c2b1", "original_content": "testo completo della bozza...", "final_content": "testo completo della versione corretta...", "no_change": false}
```

Il testo completo è dentro il log. Il campo `file` è solo un riferimento informativo — il file originale non viene né spostato né copiato altrove.

---

## Cosa devi gestire tu

I file di lavoro — bozze e versioni corrette — sono interamente sotto il tuo controllo. Gli script non ti impongono nulla. In Cowork, il flusso naturale è questo:

**Claude produce la bozza** nella cartella di lavoro che hai selezionato (es. `writing-style-skill/`). Puoi anche chiedergli di salvarla in una sottocartella dedicata, per esempio `testi/`.

**Tu la correggi** dove preferisci: direttamente nel file, su un editor esterno, su Google Docs e poi reincolli. Non importa come — quello che conta è avere un file con la versione finale quando hai finito.

**Registri i due stati** puntando gli script ai file giusti:

```bash
# Prima di correggere
python3 scripts/observe.py record-original testi/bozza-articolo.md --skill .

# Dopo aver corretto
python3 scripts/observe.py record-final testi/finale-articolo.md --skill .
```

Dopo questi due comandi i file `bozza-articolo.md` e `finale-articolo.md` possono essere tenuti, rinominati o eliminati — il loro contenuto è già nel log.

### Suggerimento pratico per Cowork

Una struttura semplice che funziona bene:

```
writing-style-skill/
├── SKILL.md
├── docs.md
├── files-management.md
├── scripts/
│   ├── observe.py
│   └── improve.py
└── testi/                  ← cartella che crei tu per i testi di lavoro
    ├── 2026-05-07-articolo-bozza.md
    └── 2026-05-07-articolo-finale.md
```

Non è obbligatoria, ma avere una cartella `testi/` separata tiene pulita la root della skill e rende facile trovare i file da passare agli script.

---

## Il parametro `--skill` — perché è importante

Entrambi gli script accettano `--skill <percorso>`. Questo parametro serve a due cose:

1. Dice a `improve.py` dove si trova il `SKILL.md` da aggiornare.
2. Determina il nome della sottocartella usata per i log (`~/clawd/memory/skill-runs/<nome-skill>/`).

Se lanci gli script dall'interno della cartella `writing-style-skill/` usando `--skill .`, il nome ricavato è `writing-style-skill` e i log finiscono in `~/clawd/memory/skill-runs/writing-style-skill/`. Questo vale per entrambi gli script, quindi i log scritti da `observe.py` vengono letti correttamente da `improve.py`.

Se non usi `--skill`, i log finiscono in una cartella generica chiamata `default`. Va bene se hai una sola skill, ma può creare confusione se ne aggiungi altre in futuro.

---

## Riepilogo visivo

```
Testo che produci con Claude
        │
        │  (puoi tenerlo dove vuoi)
        ↓
[ bozza.md ]  →  observe.py record-original  →  ~/clawd/memory/skill-runs/writing-style-skill/2026-05-07.jsonl
                                                          (il testo è qui dentro)

[ finale.md ] →  observe.py record-final     →  stessa riga + contenuto finale aggiunto al log

                  improve.py auto             →  legge i log
                                              →  chiama il LLM
                                              →  scrive proposta in ~/clawd/memory/skill-proposals/
                                              →  fa backup in ~/clawd/memory/skill-backups/
                                              →  aggiorna SKILL.md nella cartella della skill
```

I tuoi file di testo (bozza, finale) vengono letti una sola volta e poi non sono più toccati dagli script. La memoria permanente del sistema è tutta dentro `~/clawd/memory/`.
