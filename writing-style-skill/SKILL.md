---
name: writing-style-skill
version: 1.0.0
description: |
  Modello di Writing Style Skill riutilizzabile. Apprendimento automatico integrato:
  estrae regole automaticamente dalle tue modifiche, SKILL.md diventa sempre più preciso con l'uso.
  Fai il fork e personalizzalo con il tuo stile.
dependencies: []
allowed-tools:
  - Read
  - Write
  - Edit
  - exec
---

# Writing Style Skill (template)

**Fai il fork di questa skill e personalizzala con il tuo stile di scrittura. Apprendimento automatico integrato, migliora con l'uso.**

---

## 🎯 Come si usa

1. Fai il fork / clone di questa skill
2. Sostituisci le regole di stile qui sotto con le tue
3. Chiedi all'IA di scrivere contenuti usando questa skill
4. Correggi fino a soddisfazione → lo script impara automaticamente cosa hai cambiato
5. La prossima volta l'IA scriverà in modo più simile a te

---

## 【0】Voice Dimensions (quantifica il tuo stile)

**Definisci le dimensioni del tuo stile con un punteggio da 1 a 10. I numeri sono più facili da interpretare per l'IA rispetto a frasi come "scrivi in modo più naturale".**

| Dimensione | Punteggio | La tua descrizione |
|-----------|-------|---------|
| **formal_casual** | **?/10** | Più formale o più informale? |
| **technical_accessible** | **?/10** | Quanto tecnico? |
| **serious_playful** | **?/10** | Serio o giocoso? |
| **concise_elaborate** | **?/10** | Sintetico o dettagliato? |
| **reserved_expressive** | **?/10** | Riservato o diretto? |

> 💡 **Non sai cosa scrivere?** Fai qualche giro di scrittura IA → correzione → l'apprendimento automatico penserà a riempire i campi.

---

## 【1】Ruolo e lettori

**Chi sono:**
- (descrivi la tua identità, es.: sviluppatore indipendente, appassionato di IA alle prime armi)

**Chi sono i miei lettori:**
- (descrivi il tuo pubblico, es.: persone con competenze tecniche interessate all'IA)

**Rapporto con i lettori:**
- (es.: scambio tra colleghi, non lezioni)

---

## 【2】Regole di scrittura

### Regole di base

- (inserisci le tue regole, es.: non usare "approfondire", paragrafi brevi, includere dati concreti)
- 
- 

### Parole vietate

- (parole che l'IA usa spesso ma che non ti piacciono, es.: vale la pena notare, in conclusione, in questo articolo vedremo)
- 
- 

### Preferenze sintattiche

- (costruzioni che preferisci, es.: conclusione prima, niente introduzioni accademiche)
- 
- 

> 💡 **Non è necessario compilare tutto subito.** Le regole si accumulano automaticamente attraverso le tue modifiche.
> Dopo 10 cicli di scrittura→correzione, qui compariranno decine di regole precise.

---

## 【3】Standard di formattazione

### Adattamento per piattaforma

| Piattaforma | Requisiti di formato |
|------|---------|
| X/Twitter | Niente markdown, solo testo semplice |
| Instagram | Molte emoji, paragrafi brevi |
| Blog | Markdown standard |
| (la tua piattaforma) | (i tuoi requisiti) |

---

## 🔄 Apprendimento automatico (integrato)

**Questa skill impara automaticamente dalle tue modifiche. Non è necessario scrivere le regole a mano.**

### Come funziona

```
L'IA usa questa skill per scrivere la prima bozza
    ↓
Tu correggi fino a soddisfazione
    ↓
Lo script confronta le due versioni → estrae cosa hai cambiato
    ↓
Le nuove regole vengono scritte automaticamente in questo SKILL.md
    ↓
La prossima volta l'IA scriverà in modo più simile a te
```

### Servono solo due punti di dati

- **original**: la prima versione generata dall'IA
- **final**: la versione finale confermata da te

Non importa quanti giri di revisione ci sono stati nel mezzo. Hai modificato avanti e indietro 10 volte su Google Doc? Non fa niente, si confrontano solo inizio e fine.

### Guida operativa per l'agente

**Dopo aver scritto il contenuto:**
```bash
python3 scripts/observe.py record-original <file> --account <account> --content-type <tipo>
```

**Dopo che l'utente ha confermato la versione finale:**
```bash
python3 scripts/observe.py record-final <file> --match <hash>
```

**Estrai le regole (manualmente o automaticamente con cron):**
```bash
python3 scripts/improve.py auto --skill .
```

### Livelli delle regole

| Livello | Significato | Gestione |
|------|------|---------|
| P0 | Alta affidabilità (più occorrenze) | Applicazione automatica |
| P1 | Media affidabilità | Conferma manuale |
| P2 | Bassa affidabilità (1 sola occorrenza) | Archiviato per osservazione |

### Sicurezza

- Backup automatico di SKILL.md prima di ogni aggiornamento
- `improve.py rollback` per ripristinare in un clic
- La modalità auto applica solo P0

---

## 📊 Riferimento CLI

### observe.py (puro Python, zero dipendenze)

| Comando | Funzione |
|------|------|
| `record-original <file>` | Registra la bozza dell'IA |
| `record-final <file> --match <hash>` | Registra la versione finale |
| `pending` | Visualizza i record non ancora accoppiati |
| `stats` | Statistiche |

### improve.py (richiede LLM CLI)

| Comando | Funzione |
|------|------|
| `extract [--days 7]` | Estrai suggerimenti di miglioramento |
| `auto` | Estrai + applica automaticamente P0 |
| `show` | Visualizza le proposte |
| `apply <id>` | Applica una proposta |
| `rollback` | Ripristina la versione precedente |

LLM CLI supportati: `claude` (Claude Code) / `llm` (pip install llm) / variabile d'ambiente `IMPROVE_LLM_CMD`

---

## 📂 Archiviazione dati

```
~/clawd/memory/                    # OpenClaw
~/.claude/memory/                  # Claude Code
├── skill-runs/<skill-name>/
│   └── YYYY-MM-DD.jsonl          # Log giornaliero delle osservazioni
├── skill-proposals/<skill-name>/
│   └── YYYYMMDD-HHMMSS.md       # Proposte di miglioramento
└── skill-backups/<skill-name>/
    └── SKILL-YYYYMMDD-HHMMSS.md  # Backup automatici
```

Rileva automaticamente l'ambiente, non è necessario configurare i percorsi manualmente.

---

## 🚀 Risultati attesi in 30 giorni

| Periodo | Risultato atteso |
|------|---------|
| 1ª settimana | 3-5 modifiche accumulate, prime regole generate |
| 2ª settimana | 10+ regole, l'output dell'IA assomiglia già a te in modo evidente |
| 1° mese | 30+ regole, dimensioni di stile calibrate automaticamente |
| In corso | La libreria di regole cresce stabilmente, nuovi pattern catturati automaticamente |
