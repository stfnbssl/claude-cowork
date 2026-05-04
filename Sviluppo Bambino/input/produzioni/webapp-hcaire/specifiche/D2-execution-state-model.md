# D2 — Execution state model — Schema MongoDB

> **Scopo del documento**: definire le collection MongoDB e i tipi TypeScript per il tracking dello stato di esecuzione della pipeline. Questo layer permette alla webapp di sapere in ogni momento cosa è stato eseguito, cosa è in corso, cosa attende input umano, e cosa ha fallito.
>
> **Destinatario**: Claude Code — da leggere prima di implementare qualsiasi endpoint API (D4) o componente UI di orchestrazione (D5). Dipende da D1.
>
> **Database**: `hcaire_db` su MongoDB Atlas (connessione già configurata in `server/.env`).

---

## 1. Panoramica delle collection

| Collection | Ruolo | Cardinalità |
|---|---|---|
| `pipeline_contexts` | Stato aggregato corrente di un tema o di una ricerca | 1 documento per tema/ricerca |
| `pipeline_step_executions` | Record atomico di ogni singola esecuzione di uno step | N documenti per step (una per run) |
| `pipeline_external_inputs` | Input esterni forniti dal ricercatore, persistiti prima del lancio | 1+ per step, per context |

Le tre collection sono progettate per usi distinti: `pipeline_contexts` serve la UI (lettura veloce dello stato complessivo), `pipeline_step_executions` serve il motore (scrittura durante l'esecuzione, audit completo), `pipeline_external_inputs` separa la gestione degli input dal record di esecuzione.

---

## 2. Stato lifecycle di un'esecuzione

### Stati possibili (`ExecutionStatus`)

```typescript
type ExecutionStatus =
  | 'non_avviato'         // step non ancora toccato
  | 'attende_input'       // step abilitato ma mancano input esterni obbligatori
  | 'attende_decisione'   // punto di decisione umana non automatizzabile (vedi §2.2)
  | 'in_coda'             // step in attesa di essere preso in carico dal server Cowork
  | 'in_esecuzione'       // Cowork sta elaborando lo step
  | 'completato'          // output prodotto, nessuna verifica richiesta
  | 'in_verifica'         // output prodotto, in attesa di approvazione umana
  | 'verificato'          // approvato dal ricercatore, sblocca gli step dipendenti
  | 'richiede_correzione' // verifica ha restituito esito negativo, step da ri-eseguire
  | 'saltato'             // skip esplicito registrato con motivazione
  | 'fallito'             // errore durante l'esecuzione (Cowork o sistema)
```

### Macchina a stati

```
non_avviato
    │
    ├─ (dipendenze soddisfatte, input esterni mancanti) ──→ attende_input
    │                                                              │
    │                                                    (input forniti)
    │                                                              │
    ├─ (dipendenze soddisfatte, input forniti) ────────────→ in_coda
    │                                                              │
    │                                                    (Cowork avvia)
    │                                                              │
    │                                                       in_esecuzione
    │                                                         │       │
    │                                                    (successo) (errore)
    │                                                         │       │
    │                                              (verifica?) │       └──→ fallito
    │                                              sì ↙    no ↘
    │                                        in_verifica   completato
    │                                             │
    │                                   (approvato) (non approvato)
    │                                         │           │
    │                                     verificato  richiede_correzione
    │                                                      │
    │                                               (ri-esecuzione) ──→ in_coda
    │
    └─ (skip esplicito) ────────────────────────────────→ saltato
```

### 2.2 Stato `attende_decisione`

Usato esclusivamente nei due punti di transizione non automatizzabile della pipeline (vedi D1 §8, punto 6):

1. **Transizione F2 → F3**: dopo che `f2_step_5` è `verificato`, il sistema entra in `attende_decisione` sul context della ricerca. L'operatore sceglie quale tema portare in F3 → viene creato un nuovo `pipeline_context` di tipo `tema`.

2. **Passaggio contesto step 7**: `f3_step_7` non può partire senza il campo `contesto_ambito`. Questo input è strutturalmente diverso dagli altri `esterno_obbligatorio`: non è solo un file da compilare, ma la scelta che definisce l'intera direzione del dispositivo. Il sistema entra in `attende_decisione` per richiamare l'attenzione esplicita del ricercatore, non in `attende_input`.

La differenza tra `attende_input` e `attende_decisione`:
- `attende_input` → l'operatore compila un form e il sistema procede automaticamente
- `attende_decisione` → l'operatore deve prendere una decisione che ha conseguenze strutturali; il sistema notifica e attende conferma esplicita

---

## 3. Collection: `pipeline_contexts`

Un documento per ogni tema o ricerca. Fornisce una vista denormalizzata e aggiornata in tempo reale dello stato di tutti gli step — è la sorgente di verità per la UI di orchestrazione.

### Schema TypeScript

```typescript
interface PipelineContext {
  _id: ObjectId;

  // Identificazione
  context_type: 'ricerca' | 'tema';
  context_id: string;           // es. "ricerca-02-pointing-precoce" | "pointing"
  label: string;                // label leggibile

  // Solo per temi F3
  ricerca_origine: string | null;         // context_id della ricerca F2 di origine
  dispositivo_sorgente: {                 // se il tema deriva da un altro tema
    tema_id: string;
    file: string;
    device_id: string;
  } | null;

  // Stato per ogni step
  // chiave: step_id (es. "f3_step_3")
  step_states: Record<string, StepState>;

  // Punto di decisione umana corrente (se presente)
  pending_decision: HumanDecision | null;

  // Metadati derivati (mantenuti in sync con le executions)
  steps_completed: string[];       // step_id[] con status 'completato' | 'verificato' | 'saltato'
  steps_in_progress: string[];     // step_id[] con status 'in_coda' | 'in_esecuzione'
  steps_failed: string[];          // step_id[] con status 'fallito' | 'richiede_correzione'
  robustezza: 'alta' | 'media' | 'bassa' | null;  // da step 10 global_assessment
  correzioni_residue: number;      // somma correzioni non applicate (step 3/6/8)
  has_revisioni: boolean;

  created_at: Date;
  updated_at: Date;
}

interface StepState {
  status: ExecutionStatus;
  current_run: number;                  // numero della run più recente (1-based)
  last_execution_id: ObjectId | null;   // riferimento a pipeline_step_executions
  output_file: string | null;           // path relativo in pipeline/ (quando completato)
  verifica_outcome: VerificaOutcome | null;
  updated_at: Date;
}

type VerificaOutcome =
  | 'approvato'
  | 'richiede_correzione'
  | 'richiede_6c';              // specifico per step 6b: richiede integrazione strutturale

interface HumanDecision {
  type: 'f2_to_f3_tema_selection' | 'step7_context_selection';
  step_from: string;            // es. "f2_step_5"
  step_to: string;              // es. "f3_step_1" | "f3_step_7"
  description: string;          // testo da mostrare in UI
  // Opzioni pre-popolate (es. temi candidati dall'output-family F2)
  options: Record<string, unknown>[] | null;
  created_at: Date;
  decided_at: Date | null;
  decided_by: string | null;    // Clerk user id
  decision: Record<string, unknown> | null;
}
```

### Esempio documento (tema F3 in lavorazione)

```json
{
  "_id": "...",
  "context_type": "tema",
  "context_id": "pointing",
  "label": "Pointing precoce",
  "ricerca_origine": "ricerca-02-pointing-precoce",
  "dispositivo_sorgente": null,
  "step_states": {
    "f3_step_1": {
      "status": "verificato",
      "current_run": 1,
      "last_execution_id": "...",
      "output_file": "temi/pointing/lettura-configurazionale-v1.json",
      "verifica_outcome": "approvato",
      "updated_at": "2026-04-20T10:30:00Z"
    },
    "f3_step_2": {
      "status": "completato",
      "current_run": 1,
      "last_execution_id": "...",
      "output_file": "temi/pointing/stress-test-v1.json",
      "verifica_outcome": null,
      "updated_at": "2026-04-20T11:00:00Z"
    },
    "f3_step_3": {
      "status": "in_esecuzione",
      "current_run": 1,
      "last_execution_id": "...",
      "output_file": null,
      "verifica_outcome": null,
      "updated_at": "2026-04-20T11:15:00Z"
    },
    "f3_step_4": { "status": "non_avviato", "current_run": 0, "last_execution_id": null, "output_file": null, "verifica_outcome": null, "updated_at": "2026-04-20T09:00:00Z" }
  },
  "pending_decision": null,
  "steps_completed": ["f3_step_1", "f3_step_2"],
  "steps_in_progress": ["f3_step_3"],
  "steps_failed": [],
  "robustezza": null,
  "correzioni_residue": 0,
  "has_revisioni": false,
  "created_at": "2026-04-20T09:00:00Z",
  "updated_at": "2026-04-20T11:15:00Z"
}
```

### Indici

```javascript
// Lookup per context_id (il più frequente)
db.pipeline_contexts.createIndex({ context_id: 1 }, { unique: true });

// Lookup per tipo (per listare tutte le ricerche o tutti i temi)
db.pipeline_contexts.createIndex({ context_type: 1 });

// Temi per ricerca di origine
db.pipeline_contexts.createIndex({ ricerca_origine: 1 });
```

---

## 4. Collection: `pipeline_step_executions`

Un documento per ogni singola esecuzione di uno step. Non viene mai aggiornato retroattivamente — ogni ri-esecuzione crea un nuovo documento con `run_number` incrementato. Questo garantisce un audit trail completo.

### Schema TypeScript

```typescript
interface PipelineStepExecution {
  _id: ObjectId;

  // Contesto
  context_type: 'ricerca' | 'tema';
  context_id: string;
  step_id: string;              // es. "f3_step_3"
  run_number: number;           // 1, 2, 3... auto-incrementato per (context_id, step_id)

  // Stato
  status: ExecutionStatus;
  created_at: Date;
  started_at: Date | null;
  completed_at: Date | null;
  verified_at: Date | null;
  verified_by: string | null;   // Clerk user id

  // Input utilizzati
  inputs: ExecutionInputs;

  // Output
  output_file: string | null;   // path relativo a pipeline/ dopo completamento

  // Comunicazione con Cowork
  cowork_message_id: string | null;   // ID del messaggio Redis inviato
  cowork_session_id: string | null;   // ID della sessione Cowork (se disponibile)

  // Log
  log_lines: LogLine[];

  // Errore (se status === 'fallito')
  error: {
    message: string;
    source: 'cowork' | 'sistema' | 'timeout';
    detail: string | null;
  } | null;

  // Verifica
  verifica_required: boolean;
  verifica_notes: string | null;          // note libere del ricercatore
  verifica_outcome: VerificaOutcome | null;
  verifica_feedback: string | null;       // motivazione se richiede_correzione o richiede_6c

  // Skip
  is_skipped: boolean;
  skip_reason: string | null;
}

interface ExecutionInputs {
  // File prodotti da step precedenti della stessa pipeline
  pipeline: {
    step_id: string;
    run_number: number;
    file: string;               // path relativo a pipeline/
  }[];

  // Input esterni forniti dal ricercatore
  esterni: {
    input_id: string;           // es. "contesto_ambito"
    external_input_doc_id: ObjectId;   // ref a pipeline_external_inputs
    file: string | null;        // path relativo a pipeline/inputs/ se salvato su disco
  }[];

  // File strutturali fissi (config del metodo)
  strutturali: string[];

  // Dispositivo sorgente (step 7, 8, 9 di temi derivati)
  dispositivo_sorgente: {
    tema_id: string;
    file: string;
  } | null;
}

interface LogLine {
  ts: Date;
  text: string;
  level: 'info' | 'warn' | 'error';
}
```

### Esempio documento

```json
{
  "_id": "...",
  "context_type": "tema",
  "context_id": "pointing",
  "step_id": "f3_step_3",
  "run_number": 1,
  "status": "in_verifica",
  "created_at": "2026-04-20T11:00:00Z",
  "started_at": "2026-04-20T11:01:00Z",
  "completed_at": "2026-04-20T11:14:32Z",
  "verified_at": null,
  "verified_by": null,
  "inputs": {
    "pipeline": [
      { "step_id": "f3_step_1", "run_number": 1, "file": "temi/pointing/lettura-configurazionale-v1.json" },
      { "step_id": "f3_step_2", "run_number": 1, "file": "temi/pointing/stress-test-v1.json" }
    ],
    "esterni": [],
    "strutturali": ["f3-step-3/structural-correction-schema.json"],
    "dispositivo_sorgente": null
  },
  "output_file": "temi/pointing/correzione-strutturale-v1.json",
  "cowork_message_id": "msg-20260420-110100-abc123",
  "cowork_session_id": null,
  "log_lines": [
    { "ts": "2026-04-20T11:01:05Z", "text": "Avvio step f3_step_3 per tema pointing", "level": "info" },
    { "ts": "2026-04-20T11:14:30Z", "text": "Output scritto: correzione-strutturale-v1.json", "level": "info" }
  ],
  "error": null,
  "verifica_required": false,
  "verifica_notes": null,
  "verifica_outcome": null,
  "verifica_feedback": null,
  "is_skipped": false,
  "skip_reason": null
}
```

### Note sui run_number e versionamento

Il `run_number` di un'esecuzione corrisponde direttamente al suffisso `-vN` del file di output. La relazione è:

```
run_number: 1  →  output: correzione-strutturale-v1.json
run_number: 2  →  output: correzione-strutturale-v2.json
```

Per step 6b il file ha suffisso `b` (es. `stabilizzazione-proxy-v1b.json`): il `run_number` rimane numerico, il suffisso `b` è una proprietà del naming convention dello step, non del run.

Per step 6c, che produce una **nuova versione** del file di step 3, il `run_number` riprende la sequenza di step 3:

```
step_3, run_1  →  correzione-strutturale-v1.json
step_6c, run_1 →  correzione-strutturale-v2.json   (equivalente funzionale di step 3, versione 2)
```

Il `pipeline_contexts.step_states["f3_step_3"].output_file` viene aggiornato per puntare al file più recente (v2) quando step 6c completa.

### Indici

```javascript
// Lookup primario: tutte le esecuzioni di uno step per un context
db.pipeline_step_executions.createIndex(
  { context_id: 1, step_id: 1, run_number: -1 }
);

// Esecuzioni attive (per monitoring)
db.pipeline_step_executions.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: { $in: ['in_coda', 'in_esecuzione'] } } }
);

// Lookup per cowork_message_id (per ricevere le risposte dal server locale)
db.pipeline_step_executions.createIndex(
  { cowork_message_id: 1 },
  { sparse: true }
);

// Tutte le esecuzioni di un context (per audit trail)
db.pipeline_step_executions.createIndex({ context_id: 1, created_at: -1 });
```

---

## 5. Collection: `pipeline_external_inputs`

Archivia gli input esterni forniti dal ricercatore, separatamente dalle esecuzioni. Un input esterno può essere fornito una volta sola e riutilizzato in più run dello stesso step (o in step diversi se il tipo lo consente).

### Schema TypeScript

```typescript
interface PipelineExternalInput {
  _id: ObjectId;

  // Contesto
  context_type: 'ricerca' | 'tema';
  context_id: string;
  step_id: string;              // lo step per cui è stato fornito
  input_id: string;             // es. "contesto_ambito", "casi_stress_test"
  label: string;                // label leggibile

  // Provenienza
  provided_by: string;          // Clerk user id
  provided_at: Date;

  // Dati
  data: Record<string, unknown>;        // il contenuto dell'input (compilato via form)
  file_path: string | null;            // path relativo in pipeline/inputs/ se anche salvato su disco

  // Validità
  is_superseded: boolean;               // true se è stata fornita una versione più recente
  superseded_by: ObjectId | null;
}
```

### Esempio documento (contesto step 7)

```json
{
  "_id": "...",
  "context_type": "tema",
  "context_id": "pointing",
  "step_id": "f3_step_7",
  "input_id": "contesto_ambito",
  "label": "Contesto/ambito target",
  "provided_by": "user_clerk_abc",
  "provided_at": "2026-04-21T09:30:00Z",
  "data": {
    "target_domain": "clinico",
    "target_subdomain": "neuropsviluppo",
    "age_range": "9-24 mesi",
    "setting": "ambulatorio, setting semi-strutturato",
    "observer_profile": "logopedista, neuropsichiatra infantile",
    "notes": ""
  },
  "file_path": "inputs/temi/pointing/f3-step-7-contesto-clinico.json",
  "is_superseded": false,
  "superseded_by": null
}
```

### Indici

```javascript
// Lookup per context + step (il più frequente: "ho già un input per questo step?")
db.pipeline_external_inputs.createIndex(
  { context_id: 1, step_id: 1, input_id: 1, is_superseded: 1 }
);

// Tutti gli input di un context (per DeviceLineage — sezione External Inputs)
db.pipeline_external_inputs.createIndex({ context_id: 1 });
```

---

## 6. Relazione con `pipeline-index.json`

### Stato attuale

`pipeline-index.json` è un file statico generato da `sync-pipeline.mjs` a partire dal filesystem. È la sorgente di verità per la webapp read-only attuale.

### Stato target

MongoDB diventa la sorgente di verità per lo stato di esecuzione. Il file `pipeline-index.json` può continuare a esistere come cache statica per la parte read-only, ma viene **generato da MongoDB** invece che dal filesystem.

La strategia di coesistenza proposta:

```
MongoDB (pipeline_contexts)
        │
        ├──→ API GET /api/pipeline/index        ← sostituisce il file statico
        │    (risponde con la stessa struttura di pipeline-index.json)
        │
        └──→ script: genera pipeline-index.json  ← compatibilità con sync esistente
             (opzionale, per deployments senza API)
```

In pratica: il `pipelineService.ts` del frontend viene modificato per chiamare l'API invece di leggere il file statico. L'API ricostruisce la struttura di `PipelineIndex` dalla collection `pipeline_contexts`. I file JSON degli artefatti rimangono su disco in `client/public/pipeline/` (o in futuro su object storage), MongoDB traccia solo lo stato e i metadati.

### Schema di mapping `PipelineContext` → `TemaIndexEntry`

```typescript
// Come ricostruire TemaIndexEntry da PipelineContext
function contextToIndexEntry(ctx: PipelineContext): TemaIndexEntry {
  return {
    id: ctx.context_id,
    label: ctx.label,
    steps_completed: ctx.steps_completed,
    files: Object.fromEntries(
      Object.entries(ctx.step_states)
        .filter(([, s]) => s.output_file !== null)
        .map(([stepId, s]) => [stepId, s.output_file!])
    ),
    canonical_device: deriveCanonicalDevice(ctx.step_states),
    theme_id: null,
    ricerca_origine: ctx.ricerca_origine,
    dispositivo_sorgente: ctx.dispositivo_sorgente,
    steps_skipped: Object.entries(ctx.step_states)
      .filter(([, s]) => s.status === 'saltato')
      .map(([stepId, s]) => ({ step: stepId as PipelineStepId, reason: '...' })),
    external_inputs: [],   // da pipeline_external_inputs
    robustezza: ctx.robustezza,
    correzioni_residue: ctx.correzioni_residue,
    has_revisioni: ctx.has_revisioni,
  };
}
```

---

## 7. Seeding da file esistenti (migrazione)

Il `sync-pipeline.mjs` attuale sa già leggere e classificare tutti i file prodotti. Va esteso con una fase di **seeding MongoDB** che:

1. Per ogni cartella ricerca trovata → crea o aggiorna un `PipelineContext` di tipo `ricerca` con tutti gli step completati come `status: 'verificato'` (assunzione conservativa: se il file esiste, lo step è passato).
2. Per ogni cartella tema trovata → crea o aggiorna un `PipelineContext` di tipo `tema`.
3. Per ogni file trovato → crea un `PipelineStepExecution` con `run_number: 1`, `status: 'verificato'`, `started_at/completed_at/verified_at` impostati alla data di modifica del file (best-effort).
4. Non sovrascrive documenti già esistenti in MongoDB (seeding idempotente).

Comando da aggiungere in `package.json`:

```json
"seed-pipeline-db": "node scripts/seed-pipeline-db.mjs"
```

Il seeding è una tantum (o rieseguibile con `--force` per reset). Dopo il seeding, il ciclo di vita degli artefatti passa interamente attraverso MongoDB.

---

## 8. Query chiave per il backend

Di seguito le query MongoDB più frequenti che il backend (Express) dovrà eseguire. Servono come riferimento per D4 (API spec).

### Stato corrente di un tema

```javascript
// GET /api/pipeline/temi/:temaId
db.pipeline_contexts.findOne({ context_id: temaId, context_type: 'tema' });
```

### Ultima esecuzione di uno step

```javascript
// Usata internamente per determinare le dipendenze soddisfatte
db.pipeline_step_executions.findOne(
  { context_id, step_id },
  { sort: { run_number: -1 } }
);
```

### Step abilitati (condizioni di lancio soddisfatte)

La logica di abilitazione usa D1 (`pipeline-step-config.json`) + lo stato di `pipeline_contexts`. Non è una query MongoDB diretta ma una funzione che:

1. Legge il `step_states` del context.
2. Per ogni step non ancora avviato, verifica che tutti i `inputs_pipeline` required abbiano status `completato` o `verificato` (e `verificato` se `requires_verifica: true`).
3. Restituisce la lista di step avviabili.

### Input esterni già forniti per uno step

```javascript
// Usata per pre-popolare il form e verificare se lo step è pronto
db.pipeline_external_inputs.find(
  { context_id, step_id, is_superseded: false }
);
```

### Esecuzioni attive (per il server di orchestrazione)

```javascript
// Polling del server locale per sapere cosa è in coda
db.pipeline_step_executions.find(
  { status: { $in: ['in_coda', 'in_esecuzione'] } },
  { sort: { created_at: 1 } }
);
```

### Audit trail di uno step

```javascript
// GET /api/pipeline/temi/:temaId/steps/:stepId/history
db.pipeline_step_executions.find(
  { context_id: temaId, step_id },
  { sort: { run_number: -1 } }
);
```

---

## 9. Aggiornamento atomico di `pipeline_contexts`

Ogni volta che lo stato di una `pipeline_step_execution` cambia, `pipeline_contexts` va aggiornato in modo atomico per mantenere la consistenza. Il pattern raccomandato è una funzione `updateContextStepState(contextId, stepId, newState)` che usa `findOneAndUpdate` con `$set` su `step_states.<stepId>` e ricalcola `steps_completed`, `steps_in_progress`, `steps_failed`.

```javascript
// Esempio: step completato
await db.pipeline_contexts.findOneAndUpdate(
  { context_id: contextId },
  {
    $set: {
      [`step_states.${stepId}.status`]: 'completato',
      [`step_states.${stepId}.output_file`]: outputFile,
      [`step_states.${stepId}.updated_at`]: new Date(),
      'updated_at': new Date(),
    },
    $addToSet: { steps_completed: stepId },
    $pull: { steps_in_progress: stepId, steps_failed: stepId },
  }
);
```

Questa funzione sarà il punto centrale di aggiornamento stato — usata sia dall'API (quando il ricercatore verifica manualmente) sia dal message handler (quando arriva la risposta da Cowork via Redis).

---

## 10. Implicazioni per i deliverable successivi

- **D3 (Message protocol Redis)**: i messaggi di comando devono includere `execution_id` (ObjectId della `pipeline_step_execution`) per permettere al server locale di aggiornare il documento corretto quando riceve la risposta.
- **D4 (API spec Express)**: gli endpoint di lettura (`GET /api/pipeline/temi/:id`) possono rispondere direttamente da `pipeline_contexts`. Gli endpoint di scrittura (`POST .../run`, `POST .../verify`) devono aggiornare sia `pipeline_step_executions` che `pipeline_contexts` in sequenza.
- **D5 (Frontend spec)**: il componente di orchestrazione può usare polling su `GET /api/pipeline/temi/:id` (aggiornato atomicamente) oppure WebSocket/SSE per aggiornamenti in tempo reale dei log durante `in_esecuzione`.
