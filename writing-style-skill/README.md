# Writing Style Skill

Modello di Writing Style Skill riutilizzabile. **Apprendimento automatico integrato** — estrae regole dalle tue modifiche, così SKILL.md diventa sempre più preciso con l'uso.

Compatibile con **Claude Code** + **OpenClaw (ClawHub)**.

## Come funziona

```
L'IA scrive la prima bozza con SKILL.md → tu la correggi → diff tra le due versioni → estrazione delle regole → aggiornamento di SKILL.md → la prossima volta il risultato è più preciso
```

Servono solo due punti di dati: **original** (prima versione dell'IA) e **final** (versione finale definitiva). Non importa quanti giri di revisione ci sono stati nel mezzo.

## Installazione

```bash
# Claude Code
git clone https://github.com/jzOcb/writing-style-skill.git
cp -r writing-style-skill ~/.claude/skills/my-writing-style

# OpenClaw / ClawHub
npx clawhub@latest install jz-writing-style-skill
```

## Avvio rapido

1. **Modifica SKILL.md** — sostituisci le regole di stile del template con le tue (o lascia vuoto e lascia che l'apprendimento automatico le popoli)
2. **Chiedi all'IA di scrivere contenuti usando questa skill**
3. **Correggi fino a soddisfazione**
4. Registra:
```bash
python3 scripts/observe.py record-original draft.md
# ... apporta le modifiche ...
python3 scripts/observe.py record-final final.md
```
5. Estrai le regole:
```bash
python3 scripts/improve.py auto --skill .
```

## Struttura dei file

```
writing-style-skill/
├── SKILL.md              # Il tuo stile di scrittura (template, personalizzalo)
├── README.md             # Questo file
└── scripts/
    ├── observe.py        # Registra original / final (zero dipendenze)
    └── improve.py        # Estrai / applica / ripristina (richiede LLM CLI)
```

## Come funziona l'apprendimento automatico

- `observe.py` registra la bozza iniziale dell'IA e la tua versione finale
- `improve.py` usa un LLM per analizzare il diff ed estrarre regole di scrittura
- Le regole vengono classificate per affidabilità in P0/P1/P2, P0 viene applicato automaticamente
- Prima di ogni aggiornamento viene creato un backup automatico, con ripristino in un clic

## Supporto LLM

`improve.py` rileva automaticamente:
- `claude` (Claude Code) — priorità massima
- `llm` (pip install llm) — generico
- Variabile d'ambiente `IMPROVE_LLM_CMD` — personalizzato

`observe.py` è puro Python senza dipendenze.

## Licenza

MIT
