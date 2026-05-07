# Writing Style Skill — Guida completa

## Cos'è e a cosa serve

La writing-style-skill è uno strumento che insegna a Claude a scrivere come scrivi tu. Invece di spiegargli ogni volta il tuo stile con istruzioni vaghe ("scrivi in modo più diretto", "non essere troppo formale"), il tool costruisce automaticamente un insieme di regole precise partendo da un'osservazione semplice: cosa cambi quando correggi i testi che Claude ti produce.

L'idea di fondo è che le tue modifiche sono il dato più onesto sul tuo stile. Se Claude scrive "vale la pena notare che" e tu lo togli sistematicamente, quella è una regola. Il tool la cattura, la scrive in SKILL.md e la userà la prossima volta.

---

## Come funziona il ciclo di apprendimento

Il meccanismo centrale è questo loop:

```
Claude scrive una bozza usando SKILL.md
        ↓
Tu la correggi fino a soddisfazione
        ↓
Registri la bozza originale e la tua versione finale
        ↓
Lo script confronta le due versioni e ne estrae le differenze
        ↓
Un LLM analizza le differenze e propone nuove regole
        ↓
Le regole vengono scritte in SKILL.md
        ↓
La prossima bozza di Claude sarà già più simile a te
```

Non serve scrivere le regole a mano. Basta correggere i testi come faresti normalmente e lasciare che il sistema impari da lì.

---

## I file del progetto

```
writing-style-skill/
├── SKILL.md              ← il cuore del sistema: le tue regole di stile
├── README.md             ← istruzioni rapide
├── docs.md               ← questo file
└── scripts/
    ├── observe.py        ← registra le bozze e le versioni finali
    └── improve.py        ← estrae le regole e aggiorna SKILL.md
```

**SKILL.md** è il file che Claude legge prima di scrivere. All'inizio è quasi vuoto (un template con segnaposto), ma con il tempo si riempie di regole estratte automaticamente dalle tue correzioni. Più lo usi, più diventa preciso.

---

## Come usarlo con Cowork

### Configurazione iniziale (una sola volta)

**1. Personalizza SKILL.md**

Apri `SKILL.md` e compila le sezioni principali:

- **Voice Dimensions** — assegna un punteggio da 1 a 10 alle dimensioni del tuo stile. Per esempio: sei più formale o informale? Più sintetico o dettagliato? I numeri aiutano Claude a calibrarsi meglio di qualsiasi aggettivo.

- **Ruolo e lettori** — descrivi chi sei e per chi scrivi. Non serve essere precisi al millimetro: anche "sviluppatore indipendente che scrive per altri tecnici appassionati di AI" è più che sufficiente per iniziare.

- **Regole di scrittura** — se hai già in mente alcune cose che non vuoi (parole abusate dall'AI, strutture che ti danno fastidio), scrivile qui. Altrimenti lascia vuoto e lascia che l'apprendimento automatico le scopra da solo.

Non devi completare tutto subito. Bastano anche solo le Voice Dimensions per iniziare.

**2. Installa Python (se non ce l'hai)**

Gli script `observe.py` e `improve.py` richiedono Python 3. Su macOS è già installato di default. Su Windows puoi scaricarlo da python.org. `observe.py` non ha altre dipendenze. `improve.py` ha bisogno di accesso a un LLM CLI — in Cowork puoi usare Claude Code CLI (`claude`) se è installato, oppure impostare la variabile d'ambiente `IMPROVE_LLM_CMD`.

---

### Il flusso di lavoro quotidiano

#### Fase 1 — Chiedi a Claude di scrivere

In Cowork, chiedi a Claude di produrre un testo e specifica che deve usare la writing-style-skill. Per esempio:

> "Scrivi un post per il mio blog sull'argomento X seguendo le regole di stile in SKILL.md"

Claude leggerà SKILL.md e produrrà una bozza basata sulle regole che ci sono in quel momento.

#### Fase 2 — Registra la bozza originale

Prima di modificare qualsiasi cosa, salva la bozza originale di Claude in un file (per esempio `bozza.md`) e registrala:

```bash
python3 scripts/observe.py record-original bozza.md
```

Lo script stamperà un hash breve (tipo `a3f7c2b1`) che identifica questa bozza. Tienilo da parte, ti servirà al passo successivo.

#### Fase 3 — Correggi il testo

Modifica la bozza come vuoi, senza preoccuparti di niente. Puoi farlo direttamente nel file, su Google Docs, dove preferisci. Non importa quante volte ci torni sopra: il sistema confronterà solo la versione iniziale di Claude e quella finale tua.

#### Fase 4 — Registra la versione finale

Quando sei soddisfatto, salva il testo finale in un file (per esempio `finale.md`) e registralo abbinandolo alla bozza originale:

```bash
python3 scripts/observe.py record-final finale.md --match a3f7c2b1
```

Sostituisci `a3f7c2b1` con l'hash che hai ottenuto al passo 2. Se hai solo una bozza in sospeso puoi anche omettere `--match` e lo script la abbinerà automaticamente.

#### Fase 5 — Estrai le regole (periodicamente)

Dopo aver accumulato alcune correzioni (anche 2-3 sono sufficienti per iniziare), puoi estrarre le regole:

```bash
python3 scripts/improve.py auto --skill .
```

Il comando analizza le tue correzioni, propone nuove regole e applica automaticamente quelle ad alta affidabilità (P0) a SKILL.md. La prossima bozza di Claude sarà già più vicina al tuo stile.

---

## Il sistema di classificazione delle regole

Ogni regola estratta riceve un livello di priorità in base a quante volte il pattern è stato osservato:

**P0 — Alta affidabilità**: la stessa modifica è apparsa più volte in sessioni diverse. Viene applicata automaticamente a SKILL.md senza chiedere conferma.

**P1 — Media affidabilità**: il pattern è stato osservato, ma non abbastanza da essere sicuri. Viene proposta per revisione manuale.

**P2 — Bassa affidabilità**: osservata una sola volta, potrebbe essere casuale. Viene archiviata per osservazione futura.

Con `improve.py auto` si applicano solo le P0. Se vuoi applicare anche le P1, puoi farlo manualmente con `improve.py apply <id>` dopo aver visto le proposte con `improve.py show`.

---

## Comandi utili

### observe.py

| Comando | Cosa fa |
|---|---|
| `python3 scripts/observe.py record-original bozza.md` | Registra la bozza di Claude |
| `python3 scripts/observe.py record-final finale.md --match <hash>` | Registra la versione finale |
| `python3 scripts/observe.py pending` | Mostra le bozze in attesa di abbinamento |
| `python3 scripts/observe.py stats` | Statistiche generali (quante bozze, quante abbinate, tasso di modifica) |

### improve.py

| Comando | Cosa fa |
|---|---|
| `python3 scripts/improve.py auto --skill .` | Estrai regole e applica automaticamente le P0 |
| `python3 scripts/improve.py extract --days 7` | Solo estrazione, senza applicare |
| `python3 scripts/improve.py show` | Visualizza tutte le proposte in sospeso |
| `python3 scripts/improve.py apply <id>` | Applica manualmente una proposta specifica |
| `python3 scripts/improve.py rollback` | Ripristina la versione precedente di SKILL.md |

---

## Sicurezza e backup

Prima di ogni modifica a SKILL.md, `improve.py` crea automaticamente un backup nella directory `~/.claude/memory/skill-backups/` (o `~/clawd/memory/skill-backups/`). Se un aggiornamento automatico produce risultati che non ti piacciono, un solo comando ti riporta allo stato precedente:

```bash
python3 scripts/improve.py rollback --skill .
```

---

## Cosa aspettarsi nel tempo

Il sistema migliora gradualmente con l'uso. Non aspettarti grandi cambiamenti dopo una sola sessione — le regole estratte da un singolo confronto hanno affidabilità bassa (P2) e non vengono applicate automaticamente. La curva tipica è:

- **Dopo 3-5 sessioni**: compaiono le prime regole P0, il tono generale inizia ad allinearsi.
- **Dopo 10 sessioni**: le regole più importanti sono già consolidate, le bozze di Claude richiedono meno correzioni.
- **Dopo un mese di uso regolare**: SKILL.md contiene una trentina di regole precise che catturano le caratteristiche più distintive del tuo stile.

L'investimento iniziale è minimo: basta salvare la bozza prima di correggerla e la versione finale dopo. Tutto il resto è automatico.
