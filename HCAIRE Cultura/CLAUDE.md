# HCAIRE Cultura — Progetto di lettura critica degli artefatti culturali

## Descrizione del progetto

Questo progetto sviluppa una **pipeline per la generazione di documenti di interpretazione critica** di prodotti della cultura: romanzi, film, opere teatrali, racconti, saggi narrativi e altri artefatti culturali.

La lettura critica prodotta dalla pipeline non è una recensione né un'analisi tematica generica. È una **lettura ragionata e metodologicamente controllata** che applica un sistema di assi strutturali di orientamento fenomenologico allo studio della configurazione umana di un'opera.

Il modello interroga l'opera chiedendo: *quale esperienza umana questa opera mette in forma? Con quale configurazione strutturale? Con quale dinamica?*

---

## Gli assi strutturali

Il cuore metodologico del progetto è un sistema di **6 assi strutturali**, sviluppati nell'ambito di un progetto sulla fenomenologia dello sviluppo umano. Gli assi sono pre-compilati in file JSON nel seguente percorso:

```
C:/my/claude/claude-cowork\Sviluppo Bambino\output\assi-strutturali\precompiled\
```

I 6 assi sono:

| File | Nome | Funzione strutturale |
|------|------|----------------------|
| `asse_1.json` | **Ontologico–fenomenologico** | Strutture di base dell'essere-soggetto: corporeità, temporalità vissuta, regolazione, campo intenzionale |
| `asse_2.json` | **Affettivo–morale** | Genesi del vincolo affettivo verso l'altro: interiorizzazione, colpa, riparazione, responsabilità pre-normativa |
| `asse_3.json` | **Normativo–educativo** | Condizioni del giudizio normativo: norma/normatività/giudizio, autorità educativa, limiti del giudizio |
| `asse_4.json` | **Separazione e Limite** | Incontro del soggetto con il reale: eccedenza, perdita, separazione dall'onnipotenza, condizione del desiderio |
| `asse_5.json` | **Desiderio** | Struttura del rapporto del soggetto con il possibile: orientamento pre-riflessivo, soggettivazione, relazione desiderio/norma |
| `asse_6.json` | **Storico–culturale** | Mediazione storica dell'esperienza: istituzioni, dispositivi tecnici, deformazioni strutturali contemporanee |

Ogni file JSON contiene: `structural_function`, `core_processes`, `bridge_concepts`, `structural_nodes`, `reduction_risks`, `methodological_constraints`. **Prima di applicare un asse, leggere sempre il suo file JSON completo.**

---

## Struttura del progetto

```
HCAIRE Cultura/
├── CLAUDE.md                          ← questo file
├── pipeline-0/                        ← pipeline analitica operativa per Cowork (Step 1–4)
│   ├── step-1-dossier-contenutistico/
│   │   ├── CLAUDE.md                ← istruzioni operative per Cowork
│   │   └── schema.json                ← JSON schema dell'output
│   ├── step-2-lettura-libera-orientata/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   ├── step-3-lettura-strutturata-per-assi/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   └── step-4-saggio-critico-revisione/
│       ├── CLAUDE.md
│       └── schema.json
├── pipeline-1/                        ← pipeline editoriale operativa per Cowork (Step 5A–5F)
│   ├── starter.md                     ← documento di specifica originale della pipeline editoriale
│   ├── stile-editoriale.md            ← norme di stile trasversali a tutti i testi prodotti
│   ├── step-5a-selezione-editoriale/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   ├── step-5b-scaletta/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   ├── step-5c-stesura/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   ├── step-5d-revisione-finale/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   ├── step-5e-resoconto-processo/
│   │   ├── CLAUDE.md
│   │   └── schema.json
│   └── step-5f-saggio-integrato/
│       ├── CLAUDE.md
│       └── schema.json
└── letture/                           ← output delle pipeline, una cartella per opera
    └── {slug}/                        ← es. lampedusa_il-gattopardo
        ├── step-1-dossier-contenutistico.json
        ├── step-2-lettura-libera-orientata.json
        ├── step-3-lettura-strutturata-per-assi.json
        ├── step-4-saggio-critico-revisione.json
        └── editorial/                 ← output della pipeline editoriale
            ├── step-5a-selezione-editoriale.json
            ├── step-5b-scaletta.json
            ├── step-5c-stesura.json
            ├── step-5d-revisione-finale.json
            ├── articolo-finale.md         ← testo dell'articolo in Markdown
            ├── step-5e-resoconto-processo.json
            ├── resoconto-processo.md      ← dietro le quinte del processo analitico
            ├── step-5f-saggio-integrato.json
            └── saggio-integrato.md        ← saggio critico lungo per pubblicazione specialistica
```

---

## Convenzione dello slug

Ogni opera è identificata da uno **slug** generato allo Step 1, che determina il nome della sua cartella sotto `letture/`.

**Formato**: `{cognome-autore}_{titolo-opera}`

**Regole**:
- Tutto in minuscolo
- Spazi sostituiti da trattini (`-`)
- Caratteri accentati sostituiti dalla versione base (è → e, à → a, ecc.)
- Punteggiatura e caratteri speciali rimossi
- Titoli lunghi: prime 4-5 parole significative

**Esempi**:
- *Il Gattopardo* di Tomasi di Lampedusa → `lampedusa_il-gattopardo`
- *La cognizione del dolore* di Carlo Emilio Gadda → `gadda_la-cognizione-del-dolore`
- *Apocalypse Now* di Francis Ford Coppola → `coppola_apocalypse-now`
- *Aspettando Godot* di Samuel Beckett → `beckett_aspettando-godot`

---

## Le due pipeline

Il progetto è composto da due pipeline in sequenza:

- **Pipeline analitica** (`pipeline-0`): 4 step di lettura critica metodologicamente controllata (Step 1–4)
- **Pipeline editoriale** (`pipeline-1`): 6 step di curazione editoriale e produzione testuale (Step 5A–5F)

Le due pipeline sono indipendenti: la pipeline editoriale richiede come input gli output completi della pipeline analitica.

---

## La pipeline analitica (Step 1–4)

### Step 1 — Dossier contenutistico
**Obiettivo**: raccogliere informazioni affidabili sull'opera senza interpretarla.  
**Input**: titolo, autore, macrotipologia, materiali disponibili.  
**Output**: dati essenziali, sintesi neutra, struttura formale, personaggi/figure, scene chiave, temi espliciti, tensioni emergenti, contesto storico-culturale, avvertenze anti-confabulazione.  
**Regola**: nessuna applicazione degli assi, nessuna critica compiuta.

### Step 2 — Prima lettura libera orientata
**Obiettivo**: individuare la configurazione umana dominante dell'opera.  
**Input**: dossier Step 1.  
**Output**: nucleo tematico centrale, ipotesi critica provvisoria, tensioni principali, domande critiche aperte, prime aree di rilevanza (antropologica, esistenziale, storica, simbolica).  
**Regola**: gli assi possono restare sullo sfondo come sensibilità, non come griglia rigida.

### Step 3 — Lettura strutturata per assi e nodi
**Obiettivo**: tradurre l'intuizione critica in scheda metodologicamente controllata.  
**Input**: dossier Step 1 + lettura Step 2.  
**Output**: assi implicati con gradi e motivazioni, nodi trasversali attivati, evidenze testuali/visive/narrative, nodi assenti (dato critico), configurazione strutturale dominante, dinamica dell'opera, rischi di forzatura.  
**Regola**: non diagnosticare personaggi; leggere configurazioni dell'opera. Leggere sempre i file JSON degli assi prima di applicarli.

### Step 4 — Saggio critico e revisione
**Obiettivo**: produrre una lettura finale, leggibile e criticamente difendibile.  
**Input**: materiali degli Step 1, 2 e 3.  
**Output**: tesi interpretativa centrale, saggio breve in Markdown, analisi dei momenti più forti, integrazione narrativa degli assi, contro-lettura, limiti della lettura, valore aggiunto del modello.  
**Regola**: la conclusione non dice "il modello spiega l'opera", ma "questa lente permette di vedere alcuni aspetti dell'opera, lasciandone aperti altri".

---

## La pipeline editoriale (Step 5A–5F)

La pipeline editoriale prende in input i quattro JSON prodotti dalla pipeline analitica e produce tre prodotti editoriali distinti: un **articolo critico** destinato a un lettore colto ma non specialista (Step 5A–5D), un **resoconto del processo analitico** per un lettore curioso del metodo (Step 5E), e un **saggio integrato** per una pubblicazione specialistica che fonde i due precedenti in un testo organico (Step 5F).

L'agente editoriale non aggiunge interpretazione: **coordina, seleziona e trasforma** i materiali analitici in testi leggibili. Tutti i testi prodotti seguono le norme dello `stile-editoriale.md` in questa cartella.

L'agente editoriale non aggiunge interpretazione: **coordina, seleziona e trasforma** i materiali analitici in un testo leggibile. Il suo compito è aumentare la qualità editoriale, non la quantità interpretativa.

### Step 5A — Selezione editoriale
**Obiettivo**: produrre una mappa editoriale senza ancora scrivere il testo.
**Input**: Step 1 + 2 + 3 + 4.
**Output**: tesi editoriale riformulata, elementi da includere/escludere, scene da valorizzare, assi selezionati con formula linguistica, rischi residui, proposta di titolo e struttura.
**Regola**: non aumentare l'interpretazione — selezionare e organizzare ciò che è già stato prodotto.

### Step 5B — Scaletta editoriale
**Obiettivo**: costruire la scaletta dettagliata sezione per sezione.
**Input**: Step 5A + Step 1–4 per consultazione.
**Output**: scaletta con funzione, materiali, tesi locale, lunghezza e transizione per ogni sezione; verifica di coerenza; note di stesura.
**Regola**: la scaletta è un progetto di testo, non un riassunto dei materiali.

### Step 5C — Prima stesura
**Obiettivo**: scrivere la prima versione completa seguendo la scaletta.
**Input**: Step 5B + Step 5A + Step 1–4.
**Output**: testo completo (corpo + nota sul metodo) in Markdown, note per la revisione.
**Regola**: scrivere per il lettore, non per il modello.

### Step 5D — Revisione finale
**Obiettivo**: produrre la versione finale pubblicabile.
**Input**: Step 5C + Step 5B + Step 5A + Step 4.
**Output**: testo finale revisionato, checklist di controllo compilata, log delle modifiche, file Markdown dell'articolo (`articolo-finale.md`).
**Regola**: la conclusione non dice "il modello spiega l'opera", ma "questa lettura apre una prospettiva interpretativa controllata".

### Step 5E — Resoconto del processo
**Obiettivo**: produrre un resoconto discorsivo del percorso analitico — il "dietro le quinte" che spiega come si è arrivati alla proposta interpretativa.
**Input**: Step 1–4 + Step 5D (articolo finale).
**Output**: testo in forma di articolo che racconta le scelte, le scoperte inattese, i momenti di resistenza e le assenze significative del processo. File JSON + Markdown (`resoconto-processo.md`).
**Regola**: il resoconto racconta il processo, non ribatte l'interpretazione. Usa la nomenclatura degli assi, spiegandola nel contesto, per un lettore curioso del metodo.

### Step 5F — Saggio integrato
**Obiettivo**: produrre un saggio critico lungo destinato a una pubblicazione specialistica, che fonde l'articolo finale e il resoconto del processo in un testo organico e nuovo.
**Input**: `articolo-finale.md` + `resoconto-processo.md` + Step 1–4 per eventuali verifiche.
**Output**: saggio critico (~3500–5000 parole) organizzato attorno a 3–5 nuclei tematici in cui argomento interpretativo e racconto del processo si intrecciano. File JSON + Markdown (`saggio-integrato.md`).
**Regola**: il saggio non è una somma né una giustapposizione dei due testi sorgente: è una riscrittura con struttura propria. I due testi sorgente sono materiale, non struttura.

---

## Utilizzo della pipeline in Cowork

Per avviare la **pipeline analitica** su un'opera:

1. **Leggi** il file `CLAUDE.md` dello step corrente in `pipeline-0/`
2. **Leggi** il file `schema.json` dello step corrente
3. Se sei allo **Step 3**, leggi anche i file JSON degli assi in `Sviluppo Bambino/output/assi-strutturali/precompiled/`
4. **Leggi** i file di input dalla cartella `letture\{slug}\` secondo le istruzioni del `CLAUDE.md`
5. **Produci** il JSON di output conforme allo schema
6. **Salva** il JSON in `letture\{slug}\` con il nome file previsto

Per avviare la **pipeline editoriale** su un'opera già analizzata:

1. **Verifica** che i 4 JSON della pipeline analitica siano presenti in `letture\{slug}\`
2. **Leggi** il file `CLAUDE.md` dello step corrente in `pipeline-1/`
3. **Leggi** il file `schema.json` dello step corrente
4. **Leggi** i file di input indicati nel `CLAUDE.md`
5. **Produci** il JSON di output conforme allo schema
6. **Salva** il JSON in `letture\{slug}\editorial\` con il nome file previsto

Per una nuova opera, lo slug viene generato allo **Step 1** e rimane invariato per tutti gli step successivi. Se si riprende una pipeline già avviata, lo slug è già presente come nome della cartella in `letture\`.

---

## Note metodologiche fondamentali

- Gli assi strutturali sono **strumenti di lettura**, non categorie diagnostiche. Applicarli all'analisi culturale richiede una traduzione interpretativa, non un'applicazione meccanica.
- La **mancanza di un nodo** atteso è un dato critico tanto quanto la sua presenza: va registrata e motivata.
- Il modello non spiega le opere: **apre prospettive di lettura** e lascia aperti altri aspetti.
- La **contro-lettura** è parte integrante del metodo, non un'appendice opzionale.
- Le **avvertenze anti-confabulazione** sono obbligatorie: se l'opera non è direttamente accessibile, va dichiarato.

---

## Contesto di sviluppo

Il progetto è sviluppato nell'ambito di HCAIRE (Human-Centered AI Research Environment). La pipeline è pensata per essere implementata anche come **web app** (sviluppo con Claude Code) per la gestione dell'intero ciclo di lettura critica.

Gli assi strutturali appartengono a un progetto parallelo sulla fenomenologia dello sviluppo infantile (`Sviluppo Bambino`), qui applicati per analogia all'analisi culturale.
