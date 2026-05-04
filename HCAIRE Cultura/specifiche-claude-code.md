# Specifiche — Sezione "Letture" del sito HCAIRE

## Contesto

Nuova sezione del sito HCAIRE esistente. Titolo pubblico: **Letture** — sottotitolo interno: *Letture critiche di opere culturali*. Si integra nell'infrastruttura già operativa del sito: MongoDB Atlas, autenticazione admin, bus Redis per la comunicazione con Cowork, sistema di pipeline con lo stesso schema già in uso per altre sezioni (cartelle step con `CLAUDE.md` + `schema.json`).

**Fonte di verità**: MongoDB Atlas. Il filesystem locale è scratch — Cowork scrive i file di output durante l'esecuzione, il server li legge e li persiste su MongoDB, dopodiché i file locali non sono la fonte autoritativa.

**Admin**: utente admin unico già presente nel sito. Nessun RBAC aggiuntivo.

---

## Redis — canali dedicati

Per la sezione Letture si usano canali Redis dedicati, separati da quelli delle altre sezioni:

```
hcaire:letture:commands
hcaire:letture:events
```

Il `step_id` segue la convenzione: `lett_step_1` … `lett_step_5f`.

---

## MongoDB — Collection `opere`

### Schema documento

```js
{
  _id: ObjectId,

  // Dati bibliografici
  slug: String,             // univoco, es. "werfel_i-quaranta-giorni-del-mussa-dagh"
  titolo: String,
  autore: String,
  anno: Number,             // facoltativo
  tipologia: String,        // "romanzo" | "racconto" | "film" | "opera teatrale" | "saggio narrativo" | "altro"
  lingua_originale: String, // facoltativo

  // Gestione coda
  stato: String,            // "in_attesa" | "in_corso" | "completata" | "sospesa"
  priorita: Number,         // 1 (massima) – 5 (minima) | null
  note_di_ingresso: String,

  // Timestamp
  created_at: Date,
  updated_at: Date,

  // Pipeline — ogni step ha la stessa struttura base:
  //   stato:          "non_avviato" | "in_coda" | "in_esecuzione" | "completato" | "errore"
  //   completato_il:  Date | null
  //   output:         Object | null  (il JSON prodotto dallo step)
  //   errore:         String | null  (messaggio di errore se stato = "errore")
  //
  // Gli step che producono Markdown (5d, 5e, 5f) hanno in aggiunta:
  //   testo:          String | null  (contenuto del file .md corrispondente)

  pipeline: {
    step_1:  { stato, completato_il, output, errore },
    step_2:  { stato, completato_il, output, errore },
    step_3:  { stato, completato_il, output, errore },
    step_4:  { stato, completato_il, output, errore },
    step_5a: { stato, completato_il, output, errore },
    step_5b: { stato, completato_il, output, errore },
    step_5c: { stato, completato_il, output, errore },
    step_5d: { stato, completato_il, output, errore, testo },  // articolo-finale.md
    step_5e: { stato, completato_il, output, errore, testo },  // resoconto-processo.md
    step_5f: { stato, completato_il, output, errore, testo }   // saggio-integrato.md
  }
}
```

### Indici

```js
{ slug: 1 }                             // unique: true
{ stato: 1, priorita: 1 }              // ordinamento coda
{ "pipeline.step_5d.stato": 1 }        // filtro opere pubbliche
```

### Convenzione slug

Formato: `{cognome-autore}_{titolo-opera}` — tutto minuscolo, spazi → trattini, accenti rimossi, punteggiatura eliminata, titoli lunghi troncati alle prime 4–5 parole significative.

---

## Mappa completa degli step

### Costanti da aggiungere a `constants.ts`

```ts
export const LETTURE_STEP_FOLDER_MAP: Record<string, string> = {
  lett_step_1:  'pipeline-0/step-1-dossier-contenutistico',
  lett_step_2:  'pipeline-0/step-2-lettura-libera-orientata',
  lett_step_3:  'pipeline-0/step-3-lettura-strutturata-per-assi',
  lett_step_4:  'pipeline-0/step-4-saggio-critico-revisione',
  lett_step_5a: 'pipeline-1/step-5a-selezione-editoriale',
  lett_step_5b: 'pipeline-1/step-5b-scaletta',
  lett_step_5c: 'pipeline-1/step-5c-stesura',
  lett_step_5d: 'pipeline-1/step-5d-revisione-finale',
  lett_step_5e: 'pipeline-1/step-5e-resoconto-processo',
  lett_step_5f: 'pipeline-1/step-5f-saggio-integrato',
}

// Il file di istruzioni in ogni cartella step si chiama CLAUDE.md
// (stessa convenzione delle altre pipeline del sito)
export const LETTURE_STEP_CLAUDE_FILE = 'CLAUDE.md'
```

### Input/output per step

`{slug_path}` = `letture/{slug}` — `{ed_path}` = `letture/{slug}/editorial`

| step_id | input_files (role → path) | output_json | output_md |
|---------|--------------------------|-------------|-----------|
| `lett_step_1` | *(nessuno — titolo/autore/tipologia passati nel prompt dal server)* | `{slug_path}/step-1-dossier-contenutistico.json` | — |
| `lett_step_2` | `step_1` → `{slug_path}/step-1-dossier-contenutistico.json` | `{slug_path}/step-2-lettura-libera-orientata.json` | — |
| `lett_step_3` | `step_1` → `…step-1….json`<br>`step_2` → `…step-2….json`<br>+ 6 assi (vedi sotto) | `{slug_path}/step-3-lettura-strutturata-per-assi.json` | — |
| `lett_step_4` | `step_1` `step_2` `step_3` → rispettivi JSON in `{slug_path}/` | `{slug_path}/step-4-saggio-critico-revisione.json` | — |
| `lett_step_5a` | `step_1` `step_2` `step_3` `step_4` → rispettivi JSON in `{slug_path}/` | `{ed_path}/step-5a-selezione-editoriale.json` | — |
| `lett_step_5b` | `step_5a` → `{ed_path}/step-5a….json`<br>`step_1…4` → `{slug_path}/` | `{ed_path}/step-5b-scaletta.json` | — |
| `lett_step_5c` | `step_5b` → `{ed_path}/step-5b….json`<br>`step_5a` → `{ed_path}/step-5a….json`<br>`step_1…4` → `{slug_path}/` | `{ed_path}/step-5c-stesura.json` | — |
| `lett_step_5d` | `step_5c` → `{ed_path}/step-5c….json`<br>`step_5b` → `{ed_path}/step-5b….json`<br>`step_5a` → `{ed_path}/step-5a….json`<br>`step_4` → `{slug_path}/step-4….json` | `{ed_path}/step-5d-revisione-finale.json` | `{ed_path}/articolo-finale.md` |
| `lett_step_5e` | `step_5d` → `{ed_path}/step-5d….json`<br>`step_1…4` → `{slug_path}/` | `{ed_path}/step-5e-resoconto-processo.json` | `{ed_path}/resoconto-processo.md` |
| `lett_step_5f` | `articolo` → `{ed_path}/articolo-finale.md`<br>`resoconto` → `{ed_path}/resoconto-processo.md`<br>`step_1…4` → `{slug_path}/` *(consultazione)* | `{ed_path}/step-5f-saggio-integrato.json` | `{ed_path}/saggio-integrato.md` |

### Assi strutturali per `lett_step_3`

Tutti e sei i file vanno inclusi nel contesto, con i role seguenti:

```
role "asse_1" → config/assi/asse_1.json
role "asse_2" → config/assi/asse_2.json
role "asse_3" → config/assi/asse_3.json
role "asse_4" → config/assi/asse_4.json
role "asse_5" → config/assi/asse_5.json
role "asse_6" → config/assi/asse_6.json
```

Path di origine sul desktop di sviluppo:
```
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\
```
In produzione: copiati in `server/schemas/letture/assi/` al deploy (vedi sezione Schema.json).

### Estrazione campo `testo` per step 5D / 5E / 5F

Quando il server riceve l'evento `completed` per uno di questi step, legge il file `.md` scritto da Cowork nella stessa cartella del JSON e lo salva come `pipeline.step_Nx.testo` su MongoDB:

| step | file .md letto | campo MongoDB |
|------|---------------|---------------|
| `lett_step_5d` | `articolo-finale.md` | `pipeline.step_5d.testo` |
| `lett_step_5e` | `resoconto-processo.md` | `pipeline.step_5e.testo` |
| `lett_step_5f` | `saggio-integrato.md` | `pipeline.step_5f.testo` |

Il `CoworkRunner` attuale legge un solo file JSON: nessuna modifica al runner. Il server legge il file `.md` in modo autonomo dopo aver ricevuto l'evento, usando il path derivato da `OUTPUT_ROOT_LETTURE` e dallo slug.

---

## Schema.json — deployment

I file `schema.json` di validazione vengono copiati nel repository del server al deploy:

```
server/schemas/letture/
├── step-1-dossier-contenutistico.schema.json
├── step-2-lettura-libera-orientata.schema.json
├── step-3-lettura-strutturata-per-assi.schema.json
├── step-4-saggio-critico-revisione.schema.json
├── step-5a-selezione-editoriale.schema.json
├── step-5b-scaletta.schema.json
├── step-5c-stesura.schema.json
├── step-5d-revisione-finale.schema.json
├── step-5e-resoconto-processo.schema.json
├── step-5f-saggio-integrato.schema.json
└── assi/
    ├── asse_1.json … asse_6.json
```

Origine: `HCAIRE Cultura/pipeline-0/step-*/schema.json` e `pipeline-1/step-*/schema.json`.

---

## OUTPUT_ROOT per Letture

Variabile d'ambiente: `PIPELINE_OUTPUT_ROOT_LETTURE`

Sul desktop di sviluppo corrisponde a:
```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\
```

Il server costruisce i path dei file così:
```
{OUTPUT_ROOT_LETTURE}/{slug}/                  ← step 1–4
{OUTPUT_ROOT_LETTURE}/{slug}/editorial/        ← step 5A–5F
```

---

## Politica di ri-esecuzione e cascata

Quando l'admin ri-esegue uno step, tutti gli step che (direttamente o transitivamente) dipendono da esso vengono resettati automaticamente a `non_avviato`, con `output`, `testo`, `errore` e `completato_il` azzerati. Il campo `stato` dell'opera viene ricalcolato.

Mappa della cascata:

```ts
export const LETTURE_INVALIDATION_MAP: Record<string, string[]> = {
  lett_step_1:  ['lett_step_2','lett_step_3','lett_step_4','lett_step_5a','lett_step_5b','lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_2:  ['lett_step_3','lett_step_4','lett_step_5a','lett_step_5b','lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_3:  ['lett_step_4','lett_step_5a','lett_step_5b','lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_4:  ['lett_step_5a','lett_step_5b','lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_5a: ['lett_step_5b','lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_5b: ['lett_step_5c','lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_5c: ['lett_step_5d','lett_step_5e','lett_step_5f'],
  lett_step_5d: ['lett_step_5e','lett_step_5f'],
  lett_step_5e: ['lett_step_5f'],
  lett_step_5f: [],
}
```

---

## Calcolo automatico del campo `stato` dell'opera

Ricalcolato dal server ad ogni aggiornamento di step:

| Condizione | `stato` |
|-----------|---------|
| Tutti gli step a `non_avviato` | `in_attesa` |
| Almeno uno step `in_coda`, `in_esecuzione`, `completato` o `errore` | `in_corso` |
| Tutti e 10 gli step a `completato` | `completata` |
| Admin ha impostato manualmente | `sospesa` |

---

## API endpoints

### Pubblici (nessuna autenticazione)

```
GET  /api/letture
     → lista opere con pipeline.step_5d.stato = "completato"
     → campi restituiti: slug, titolo, autore, anno, tipologia,
       completato_il (da step_5d), testi disponibili (5e, 5f)
     → ordinamento: step_5d.completato_il desc

GET  /api/letture/:slug
     → dettaglio opera pubblica
     → campi restituiti: dati bibliografici +
       pipeline.step_5d.testo (articolo)
       pipeline.step_5e.testo (se completato)
       pipeline.step_5f.testo (se completato)
```

### Admin (autenticazione esistente)

```
GET    /api/admin/letture
       → lista completa con tutti i campi tranne output (troppo pesante)
       → supporta filtri: stato, tipologia, priorita
       → ordinamento default: priorita asc, created_at desc

POST   /api/admin/letture
       → crea opera: genera slug, inizializza tutti gli step a non_avviato
       → body: { titolo, autore, anno?, tipologia, lingua_originale?, priorita?, note_di_ingresso? }

GET    /api/admin/letture/:slug
       → dettaglio completo incluso output di ogni step

PATCH  /api/admin/letture/:slug
       → aggiorna metadati: titolo, autore, anno, tipologia, lingua_originale, priorita, note_di_ingresso, stato
       → non tocca i campi pipeline

DELETE /api/admin/letture/:slug
       → elimina opera e tutti i suoi dati

POST   /api/admin/letture/:slug/steps/:step_id/run
       → avvia step: verifica prerequisiti, imposta stato in_coda,
         invia comando su hcaire:letture:commands
       → se step già completato: applica prima la cascata di invalidazione

GET    /api/admin/letture/:slug/steps/:step_id
       → stato e log di un singolo step
```

---

## Sezione pubblica — pagina "Letture"

### `/letture` — indice

Lista delle opere con `pipeline.step_5d.stato = "completato"`, ordinate per data di pubblicazione dell'articolo (discendente).

Per ogni opera: titolo, autore, anno, tipologia. Badge opzionali se disponibili anche resoconto (5E) e saggio integrato (5F).

### `/letture/:slug` — pagina opera

Visualizza i testi disponibili. Se solo 5D è completato: mostra l'articolo. Se anche 5E e/o 5F sono completati: mostra tab o sezioni aggiuntive.

Il testo Markdown viene renderizzato in HTML con la libreria già in uso nel sito.

---

## Sezione admin — interfaccia Letture

Integrata nell'area amministrativa esistente, stile e componenti UI del sito.

### Vista archivio

Tabella: titolo, autore, tipologia, stato, priorità, avanzamento (N/10 step completati), data inserimento.
Filtri: stato, tipologia, priorità. Ordinamento: priorità asc (default per in_attesa), data inserimento desc.
Azioni per riga: apri scheda, modifica priorità inline, cambia stato.
Azione globale: aggiungi opera.

### Form inserimento opera

Campi: titolo, autore, anno (opz.), tipologia (select), lingua originale (opz.), priorità (select 1–5 | nessuna), note di ingresso (textarea).
Al salvataggio: genera slug, crea documento MongoDB, crea cartelle sul filesystem locale.

### Scheda opera

**Intestazione**: dati bibliografici + slug + stato + priorità (modificabili inline).

**Pannello pipeline analitica** (Step 1–4) e **pannello pipeline editoriale** (Step 5A–5F).
Per ogni step:
- Icona stato: grigio (non_avviato) / giallo (in_coda, in_esecuzione) / verde (completato) / rosso (errore)
- Timestamp completamento se disponibile
- Pulsante **Esegui** — attivo solo se prerequisiti soddisfatti e step non in_esecuzione/in_coda
- Pulsante **Riesegui** — disponibile se completato, con modale di conferma che elenca gli step che verranno invalidati

**Anteprima testi**: tab o link per visualizzare articolo / resoconto / saggio se disponibili.

**Log step**: per ogni step, lista degli eventi con timestamp ed esito.

---

## Prerequisiti per abilitare il pulsante Esegui

| step_id | prerequisiti (tutti devono essere `completato`) |
|---------|------------------------------------------------|
| `lett_step_1` | nessuno |
| `lett_step_2` | `lett_step_1` |
| `lett_step_3` | `lett_step_1`, `lett_step_2` |
| `lett_step_4` | `lett_step_1`, `lett_step_2`, `lett_step_3` |
| `lett_step_5a` | `lett_step_1…4` |
| `lett_step_5b` | `lett_step_5a` |
| `lett_step_5c` | `lett_step_5b` |
| `lett_step_5d` | `lett_step_5c` |
| `lett_step_5e` | `lett_step_5d` |
| `lett_step_5f` | `lett_step_5d`, `lett_step_5e` |

---

## Prompt di Step 1 — costruzione lato server

Step 1 non ha file di input precedenti. Il server costruisce il messaggio utente con i metadati dell'opera prima di invocare Cowork:

```
Titolo: {titolo}
Autore: {autore}
Tipologia: {tipologia}
Anno: {anno}          (se disponibile)
Lingua originale: {lingua_originale}    (se disponibile)
Note: {note_di_ingresso}    (se presenti)
```

Questo testo viene passato come primo messaggio utente, seguito dalle istruzioni del `CLAUDE.md` dello step 1.

---

## File di pipeline — path di riferimento

```
HCAIRE Cultura/
├── pipeline-0/
│   ├── step-1-dossier-contenutistico/
│   │   ├── CLAUDE.md          ← istruzioni per Cowork
│   │   └── schema.json
│   ├── step-2-lettura-libera-orientata/   (idem)
│   ├── step-3-lettura-strutturata-per-assi/   (idem)
│   └── step-4-saggio-critico-revisione/   (idem)
└── pipeline-1/
    ├── stile-editoriale.md    ← norme di stile (letto da Cowork agli step 5C–5F)
    ├── step-5a-selezione-editoriale/   (CLAUDE.md + schema.json)
    ├── step-5b-scaletta/
    ├── step-5c-stesura/
    ├── step-5d-revisione-finale/
    ├── step-5e-resoconto-processo/
    └── step-5f-saggio-integrato/
```

Desktop di sviluppo: `C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\`
Variabile d'ambiente: `PIPELINE_SPECS_ROOT_LETTURE`
