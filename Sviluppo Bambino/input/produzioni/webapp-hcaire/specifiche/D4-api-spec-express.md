# D4 — API spec Express — Endpoint orchestrazione pipeline

> **Scopo del documento**: specifica completa di tutti gli endpoint Express da aggiungere al backend `server/` per supportare la pipeline. Definisce metodo, path, autenticazione, request/response body, status code, e side effect per ogni endpoint.
>
> **Destinatario**: Claude Code — da implementare in `server/src/routes/pipeline.ts` e `server/src/controllers/pipelineController.ts`. Dipende da D1, D2, D3.
>
> **Namespace**: tutti gli endpoint vivono sotto `/api/pipeline/`. I file statici degli artefatti JSON continuano a essere serviti da `client/public/pipeline/` — non sostituiti da API.

---

## 1. Principi generali

### 1.1 Autenticazione

Tutti gli endpoint si dividono in due livelli:

| Livello | Chi può accedere | Come verificare |
|---|---|---|
| `public` | Chiunque (anche non autenticato) | Nessun middleware |
| `admin` | Solo utenti con ruolo `admin` (Clerk) | Middleware `requireAdmin` (già presente in `middleware/auth.ts`) |

Gli endpoint di **lettura** (`GET`) sono `public` — le produzioni sono contenuti del sito, visibili a tutti. Gli endpoint di **scrittura** (esecuzione, verifica, input, decisioni) sono `admin`.

### 1.2 Envelope di risposta

Tutte le risposte seguono questa struttura:

```typescript
// Successo
{
  "ok": true,
  "data": { ... }       // payload specifico dell'endpoint
}

// Errore
{
  "ok": false,
  "error": {
    "code": "STEP_NOT_FOUND",          // codice macchina
    "message": "Step f3_step_99 non trovato nella configurazione",  // messaggio leggibile
    "detail": null | { ... }           // dettaglio opzionale (es. validation errors)
  }
}
```

### 1.3 Codici HTTP

| Situazione | Codice |
|---|---|
| Lettura riuscita | 200 |
| Creazione riuscita | 201 |
| Comando accettato (asincrono) | 202 |
| Richiesta malformata | 400 |
| Non autenticato | 401 |
| Non autorizzato (autenticato ma non admin) | 403 |
| Risorsa non trovata | 404 |
| Conflitto di stato (es. step già in esecuzione) | 409 |
| Condizioni non soddisfatte (dipendenze mancanti) | 422 |
| Errore interno | 500 |
| Server Cowork non raggiungibile | 503 |

### 1.4 Codici errore applicativi

```
CONTEXT_NOT_FOUND          context_id non esiste in pipeline_contexts
STEP_NOT_FOUND             step_id non valido (non in pipeline-step-config.json)
STEP_ALREADY_RUNNING       step con status in_coda o in_esecuzione
STEP_DEPENDENCIES_UNMET    dipendenze pipeline non soddisfatte (D1 §4)
STEP_INPUTS_MISSING        input esterni obbligatori non ancora forniti
EXECUTION_NOT_FOUND        execution_id non esiste
EXECUTION_NOT_IN_VERIFICA  tentativo di verify su step non in stato in_verifica
COWORK_UNAVAILABLE         ping al server locale fallito
DECISION_NOT_PENDING       tentativo di submit decision su context senza pending_decision
INPUT_SCHEMA_INVALID       i dati dell'input esterno non rispettano lo schema atteso
```

---

## 2. Endpoint di lettura (public)

Sostituiscono il fetch diretto di `pipeline-index.json`. Rispondono con dati da MongoDB, garantendo che lo stato di esecuzione sia sempre aggiornato.

---

### `GET /api/pipeline/index`

Restituisce l'indice globale della pipeline — equivalente del `pipeline-index.json` statico, generato live da MongoDB. Usato da `pipelineService.fetchPipelineIndex()` (da modificare per puntare qui invece del file statico).

**Auth**: public

**Response 200**:

```typescript
{
  ok: true,
  data: {
    generated_at: string;     // ISO8601
    ricerche: RicercaIndexEntry[];
    temi: TemaIndexEntry[];
  }
}
```

La struttura di `RicercaIndexEntry` e `TemaIndexEntry` è identica a quella attuale di `pipeline-index.json` (tipi in `client/src/types/pipeline.ts`) — nessuna breaking change per il frontend.

---

### `GET /api/pipeline/temi/:temaId`

Stato completo di un tema: step states, esecuzione corrente, input esterni noti, decisione pending.

**Auth**: public

**Response 200**:

```typescript
{
  ok: true,
  data: {
    context: PipelineContext;          // documento da pipeline_contexts
    step_config: StepConfig[];         // subset da pipeline-step-config.json relativo ai soli step F3
    external_inputs: PipelineExternalInput[];  // input già forniti (is_superseded: false)
  }
}
```

**Response 404**: `CONTEXT_NOT_FOUND`

---

### `GET /api/pipeline/ricerche/:ricercaId`

Stato completo di una ricerca.

**Auth**: public

**Response 200**: struttura analoga a `GET /api/pipeline/temi/:temaId` ma per contesto ricerca.

---

### `GET /api/pipeline/temi/:temaId/steps/:stepId/history`

Storico di tutte le run di uno step per un tema (audit trail).

**Auth**: public

**Response 200**:

```typescript
{
  ok: true,
  data: {
    executions: PipelineStepExecution[];   // ordinate run_number DESC
  }
}
```

---

### `GET /api/pipeline/step-config`

Restituisce il contenuto completo di `pipeline-step-config.json`. Usato dal frontend per costruire form di input e valutare le condizioni di abilitazione degli step.

**Auth**: public

**Response 200**:

```typescript
{
  ok: true,
  data: {
    steps: StepConfig[];    // array completo da D1 §7
  }
}
```

---

## 3. Endpoint di orchestrazione (admin)

### `POST /api/pipeline/temi/:temaId/steps/:stepId/run`

Avvia l'esecuzione di uno step. È il punto di ingresso principale dell'orchestrazione.

**Auth**: admin

**Request body**:

```typescript
{
  // Parametri facoltativi per step con inputs_esterni facoltativi
  extra_params?: {
    severita_test?: 'standard' | 'forte';          // f3_step_6
    specificita_dispositivo?: 'standard' | 'alta'; // f3_step_8
  };

  // Timeout personalizzato (opzionale, default da env)
  timeout_ms?: number;
}
```

**Logica server** (in sequenza, sincrona prima del 202):

1. Verifica che `temaId` esista in `pipeline_contexts` → 404 se no.
2. Verifica che `stepId` sia valido in `pipeline-step-config.json` → 404 se no.
3. Verifica che lo step non sia già `in_coda` o `in_esecuzione` → 409 `STEP_ALREADY_RUNNING`.
4. Verifica che tutte le dipendenze pipeline siano soddisfatte (D1 adjacency list + status da `pipeline_contexts`) → 422 `STEP_DEPENDENCIES_UNMET` con dettaglio dei blocchi mancanti.
5. Verifica che tutti gli `inputs_esterni` obbligatori siano presenti in `pipeline_external_inputs` → 422 `STEP_INPUTS_MISSING` con lista degli input mancanti.
6. Calcola `run_number` = ultima run + 1 (query su `pipeline_step_executions`).
7. Costruisce il documento `PipelineStepExecution` con status `in_coda` e lo inserisce in MongoDB.
8. Aggiorna `pipeline_contexts.step_states[stepId].status → 'in_coda'`.
9. Risolve i path assoluti degli input files (da output_file dei step precedenti).
10. Chiama `messageBus.sendStepRun(...)` → LPUSH su Redis.
11. Risponde `202 Accepted`.

**Response 202**:

```typescript
{
  ok: true,
  data: {
    execution_id: string;    // MongoDB ObjectId della nuova execution
    run_number: number;
    status: 'in_coda';
  }
}
```

**Response 404**: `CONTEXT_NOT_FOUND` | `STEP_NOT_FOUND`
**Response 409**: `STEP_ALREADY_RUNNING`
**Response 422**: `STEP_DEPENDENCIES_UNMET` | `STEP_INPUTS_MISSING`

```typescript
// Esempio 422 STEP_DEPENDENCIES_UNMET
{
  ok: false,
  error: {
    code: 'STEP_DEPENDENCIES_UNMET',
    message: 'Dipendenze non soddisfatte per f3_step_6',
    detail: {
      missing: [
        { step_id: 'f3_step_4', required_status: 'verificato', current_status: 'in_verifica' },
        { step_id: 'f3_step_5', required_status: 'verificato', current_status: 'non_avviato' }
      ]
    }
  }
}
```

**Response 503**: `COWORK_UNAVAILABLE` — se il ping preventivo al server locale fallisce

> **Nota**: il ping al server locale (D3 §3.3) è opzionale in questo endpoint — aggiunge latenza. Meglio farlo solo all'apertura del pannello admin, non ad ogni run.

---

### `DELETE /api/pipeline/executions/:executionId`

Cancella un'esecuzione in corso (`in_coda` o `in_esecuzione`).

**Auth**: admin

**Logica server**:
1. Verifica che l'execution esista → 404.
2. Verifica che sia in stato `in_coda` o `in_esecuzione` → 409 se già terminata.
3. Chiama `messageBus.sendStepCancel(executionId, reason)`.
4. Risponde `202 Accepted`. L'aggiornamento di stato avviene quando arriva l'evento `pipeline.step.cancelled`.

**Request body**:

```typescript
{
  reason?: string;    // motivazione della cancellazione (opzionale, per il log)
}
```

**Response 202**:

```typescript
{
  ok: true,
  data: { execution_id: string; status: 'cancellazione_inviata' }
}
```

---

### `POST /api/pipeline/executions/:executionId/verify`

Registra l'esito della verifica umana su uno step completato.

**Auth**: admin

**Request body**:

```typescript
{
  outcome: 'approvato' | 'richiede_correzione' | 'richiede_6c';
  notes?: string;        // note libere del ricercatore
  feedback?: string;     // motivazione se outcome !== 'approvato'
}
```

**Logica server**:
1. Verifica che l'execution esista → 404.
2. Verifica che sia in stato `in_verifica` → 409 `EXECUTION_NOT_IN_VERIFICA`.
3. Aggiorna `pipeline_step_executions`: `status → 'verificato'` | `'richiede_correzione'`, `verified_at`, `verified_by`, `verifica_outcome`, `verifica_notes`, `verifica_feedback`.
4. Aggiorna `pipeline_contexts` via `updateContextStepState()`.
5. Se `outcome === 'approvato'` o `'richiede_6c'`: lo step passa a `verificato` — valuta se sbloccare step dipendenti (invia notifica frontend via SSE se qualcuno è in ascolto).
6. Se `outcome === 'richiede_correzione'`: lo step passa a `richiede_correzione` — step dipendenti rimangono bloccati.
7. Se `outcome === 'richiede_6c'` (solo per `f3_step_6b`): imposta `pending_decision` sul context per guidare l'operatore verso l'esecuzione di step 6c.

**Response 200**:

```typescript
{
  ok: true,
  data: {
    execution_id: string;
    new_status: ExecutionStatus;
    unlocked_steps: string[];    // step_id[] ora abilitati grazie a questa verifica
  }
}
```

---

### `POST /api/pipeline/temi/:temaId/steps/:stepId/skip`

Registra lo skip esplicito di uno step saltabile (f3_step_8, f3_step_6c).

**Auth**: admin

**Request body**:

```typescript
{
  reason: string;    // obbligatorio — motivazione dello skip
}
```

**Logica server**:
1. Verifica che lo step sia `can_skip: true` in `pipeline-step-config.json` → 422 se no.
2. Verifica che lo step sia in stato `non_avviato` o `attende_input` → 409 se in esecuzione.
3. Crea un `PipelineStepExecution` con `status: 'saltato'`, `is_skipped: true`, `skip_reason`.
4. Aggiorna `pipeline_contexts`.
5. Aggiunge la voce a `steps_skipped` nel context.
6. Valuta se sbloccare step dipendenti.

**Response 200**:

```typescript
{
  ok: true,
  data: {
    step_id: string;
    status: 'saltato';
    unlocked_steps: string[];
  }
}
```

---

## 4. Endpoint input esterni (admin)

### `GET /api/pipeline/temi/:temaId/steps/:stepId/inputs`

Restituisce gli input esterni già forniti per uno step (non superseded).

**Auth**: public (l'operatore deve poter vedere cosa ha già caricato anche senza essere loggato nella stessa sessione)

**Response 200**:

```typescript
{
  ok: true,
  data: {
    inputs: PipelineExternalInput[];   // is_superseded: false
    step_config_inputs: ExternalInputConfig[];  // da pipeline-step-config.json
    all_required_provided: boolean;    // true se tutti gli esterno_obbligatorio sono presenti
  }
}
```

---

### `POST /api/pipeline/temi/:temaId/steps/:stepId/inputs`

Salva un input esterno per uno step. Se esiste già un input con lo stesso `input_id`, lo marca come superseded e crea il nuovo.

**Auth**: admin

**Request body**:

```typescript
{
  input_id: string;                   // es. "contesto_ambito"
  data: Record<string, unknown>;      // i dati del form (validati contro lo schema atteso)
  save_to_file?: boolean;             // default true — salva anche il JSON in pipeline/inputs/
}
```

**Logica server**:
1. Verifica che `input_id` sia valido per lo step in `pipeline-step-config.json` → 400.
2. Valida `data` contro lo schema JSON dello step (da `external-input-schemas/`) → 400 `INPUT_SCHEMA_INVALID` con dettaglio degli errori.
3. Marca come superseded il precedente input con lo stesso `input_id` (se presente).
4. Crea nuovo documento in `pipeline_external_inputs`.
5. Se `save_to_file: true`: scrive il file JSON in `pipeline/inputs/temi/{temaId}/f3-step-N-{label}.json`.
6. Aggiorna `pipeline_contexts.step_states[stepId]` se ora tutti gli input obbligatori sono presenti (status `non_avviato` → `attende_input` solo se era fermo lì per mancanza di input).

**Response 201**:

```typescript
{
  ok: true,
  data: {
    input_id: string;
    external_input_doc_id: string;
    file_path: string | null;
    all_required_provided: boolean;   // ora lo step può essere lanciato?
  }
}
```

---

### `DELETE /api/pipeline/external-inputs/:inputDocId`

Marca un input esterno come superseded (non lo elimina fisicamente — mantiene l'audit trail).

**Auth**: admin

**Response 200**:

```typescript
{
  ok: true,
  data: { input_doc_id: string; superseded: true }
}
```

---

## 5. Endpoint decisioni umane (admin)

Le decisioni umane sono i due punti non automatizzabili della pipeline (D2 §2.2).

### `GET /api/pipeline/temi/:temaId/pending-decision`

Restituisce la decisione pendente per un tema (se presente).

**Auth**: public

**Response 200**:

```typescript
{
  ok: true,
  data: {
    decision: HumanDecision | null;
  }
}
```

---

### `GET /api/pipeline/ricerche/:ricercaId/pending-decision`

Restituisce la decisione pendente per una ricerca (es. quale tema portare in F3 dopo f2_step_5).

**Auth**: public

**Response 200**: stessa struttura del precedente.

---

### `POST /api/pipeline/ricerche/:ricercaId/decisions`

Registra la decisione F2→F3: quale tema portare in F3 e crea il contesto tema.

**Auth**: admin

**Request body**:

```typescript
{
  decision_type: 'f2_to_f3_tema_selection';
  selected_theme: {
    theme_id: string;        // es. "pointing"
    label: string;
    from_step: 'f2_step_5';
    from_file: string;       // path del file output-family da cui è stato scelto
  };
  // Opzionale: tema derivato da un dispositivo sorgente
  dispositivo_sorgente?: {
    tema_id: string;
    file: string;
    device_id: string;
  };
}
```

**Logica server**:
1. Verifica che il context ricerca abbia `pending_decision.type === 'f2_to_f3_tema_selection'` → 409 `DECISION_NOT_PENDING`.
2. Crea un nuovo `PipelineContext` di tipo `tema` con tutti gli step in `non_avviato`.
3. Azzera `pending_decision` sul context ricerca.
4. Registra la decisione nell'execution history della ricerca.

**Response 201**:

```typescript
{
  ok: true,
  data: {
    created_tema_id: string;
    tema_context: PipelineContext;
  }
}
```

---

### `POST /api/pipeline/temi/:temaId/decisions`

Registra una decisione su un tema (es. conferma contesto step 7 prima del lancio).

**Auth**: admin

**Request body**:

```typescript
{
  decision_type: 'step7_context_selection';
  // La decisione in sé viene gestita come input esterno (già fornito via POST /inputs)
  // Questo endpoint serve solo a confermare che si vuole procedere
  confirmed: true;
  notes?: string;
}
```

**Logica server**:
1. Verifica `pending_decision` → 409 se assente.
2. Risolve la decisione: segna come `decided_at`, `decided_by`, `decision`.
3. Azzera `pending_decision` sul context.
4. Se l'input esterno corrispondente è già stato fornito: sblocca lo step (status → `attende_input` se mancano altri input, o direttamente avviabile).

**Response 200**:

```typescript
{
  ok: true,
  data: {
    decision_resolved: true;
    step_now_launchable: boolean;
  }
}
```

---

## 6. SSE — Log in streaming

### `GET /api/pipeline/executions/:executionId/logs`

Apre una connessione Server-Sent Events per ricevere i log di un'esecuzione in tempo reale.

**Auth**: public (i log non contengono dati sensibili)

**Headers risposta**:

```
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

**Formato eventi SSE**:

```
event: log
data: {"ts":"2026-04-20T11:05:00Z","text":"Analisi struttura dispositivo...","level":"info"}

event: log
data: {"ts":"2026-04-20T11:05:01Z","text":"Rilevata frattura in dimensione co-regolatoria","level":"warn"}

event: status
data: {"status":"completato","output_file":"temi/pointing/correzione-strutturale-v1.json"}

event: done
data: {}
```

**Logica server**:
1. Carica i log già presenti in `pipeline_step_executions.log_lines` e li invia come burst iniziale.
2. Sottoscrive a `hcaire:pipeline:events` e filtra per `execution_id`.
3. Per ogni `pipeline.step.log` → invia evento `log`.
4. Per `pipeline.step.completed` | `pipeline.step.failed` | `pipeline.step.cancelled` → invia evento `status` poi `done`, chiude la connessione.
5. Se l'esecuzione è già terminata al momento della connessione: invia tutti i log storici + evento `status` + `done` immediatamente.

**Nota**: il frontend mantiene la connessione SSE aperta solo mentre visualizza l'esecuzione. Chiuderla quando il componente viene smontato.

---

## 7. Endpoint contestuali e di sistema

### `POST /api/pipeline/ricerche`

Crea un nuovo contesto ricerca (avvia una nuova run F2).

**Auth**: admin

**Request body**:

```typescript
{
  ricerca_id: string;    // slug kebab-case, es. "ricerca-03-sguardo-condiviso"
  label: string;
}
```

**Logica**: crea `PipelineContext` tipo `ricerca` con tutti gli step F2 in `non_avviato`. Verifica che `ricerca_id` non esista già → 409.

**Response 201**:

```typescript
{
  ok: true,
  data: { context: PipelineContext }
}
```

---

### `GET /api/pipeline/system/status`

Verifica che il server locale Cowork sia attivo e raggiungibile.

**Auth**: admin

**Logica**: chiama `messageBus.ping()` con timeout 5 secondi.

**Response 200** (server attivo):

```typescript
{
  ok: true,
  data: {
    cowork_server: {
      active: true;
      active_executions: number;
      uptime_seconds: number;
      server_version: string;
    }
  }
}
```

**Response 503** (server non raggiungibile):

```typescript
{
  ok: false,
  error: {
    code: 'COWORK_UNAVAILABLE',
    message: 'Server Cowork non raggiungibile. Verificare che il server locale sia in esecuzione.',
    detail: null
  }
}
```

---

## 8. Struttura file nel backend

```
server/src/
├── routes/
│   └── pipeline.ts          ← nuovo: registra tutti i route handler
├── controllers/
│   └── pipelineController.ts ← nuovo: logica di ogni endpoint
├── services/
│   ├── pipelineService.ts    ← nuovo: logica di business (step enablement, context updates)
│   ├── messageBus.ts         ← nuovo: PipelineMessageBus (D3 §9)
│   └── stepConfigService.ts  ← nuovo: carica e interroga pipeline-step-config.json
├── models/
│   ├── PipelineContext.ts    ← nuovo: schema Mongoose per pipeline_contexts
│   ├── PipelineStepExecution.ts ← nuovo
│   └── PipelineExternalInput.ts ← nuovo
└── middleware/
    └── auth.ts              ← esistente: aggiungere requireAdmin se non presente
```

### Registrazione route in `server/src/index.ts`

```typescript
import pipelineRoutes from './routes/pipeline';
app.use('/api/pipeline', pipelineRoutes);
```

---

## 9. Funzione di valutazione abilitazione step

La funzione `evaluateStepEnablement(contextId, stepId)` è il cuore della logica di orchestrazione. Usata da `POST .../run` (§3.1) e dalla risposta di `POST .../verify` (§3.3) per calcolare `unlocked_steps`.

```typescript
async function evaluateStepEnablement(
  context: PipelineContext,
  stepId: string
): Promise<{
  enabled: boolean;
  blocking_reasons: BlockingReason[];
}> {
  const stepConfig = getStepConfig(stepId);  // da pipeline-step-config.json

  const reasons: BlockingReason[] = [];

  // 1. Controlla dipendenze pipeline
  for (const dep of stepConfig.inputs_pipeline ?? []) {
    const depState = context.step_states[dep.step];
    const requiredStatus = dep.requires_verifica ? 'verificato' : 'completato';
    const acceptableStatuses = [requiredStatus, 'verificato', 'saltato'];

    // Caso speciale: f3_step_3_or_6c — accetta f3_step_3 O f3_step_6c
    if (dep.step === 'f3_step_3_or_6c') {
      const step6cState = context.step_states['f3_step_6c'];
      const step3State = context.step_states['f3_step_3'];
      const resolved = step6cState?.status === 'verificato' || step6cState?.status === 'completato'
        ? step6cState
        : step3State;
      if (!resolved || !acceptableStatuses.includes(resolved.status)) {
        reasons.push({ type: 'dependency', step_id: dep.step, required_status: requiredStatus, current_status: resolved?.status ?? 'non_avviato' });
      }
      continue;
    }

    if (!depState || !acceptableStatuses.includes(depState.status)) {
      reasons.push({ type: 'dependency', step_id: dep.step, required_status: requiredStatus, current_status: depState?.status ?? 'non_avviato' });
    }
  }

  // 2. Controlla input esterni obbligatori
  const requiredInputs = (stepConfig.inputs_esterni ?? []).filter(i => i.type === 'esterno_obbligatorio');
  for (const inputConfig of requiredInputs) {
    const provided = await db.pipeline_external_inputs.findOne({
      context_id: context.context_id,
      step_id: stepId,
      input_id: inputConfig.id,
      is_superseded: false
    });
    if (!provided) {
      reasons.push({ type: 'missing_input', input_id: inputConfig.id, label: inputConfig.label });
    }
  }

  // 3. Controlla pending_decision bloccante
  if (context.pending_decision && DECISION_BLOCKS_STEP[context.pending_decision.type]?.includes(stepId)) {
    reasons.push({ type: 'pending_decision', decision_type: context.pending_decision.type });
  }

  return { enabled: reasons.length === 0, blocking_reasons: reasons };
}
```

---

## 10. Modifiche al frontend esistente

Per usare le nuove API, il frontend deve aggiornare solo il servizio di accesso ai dati:

### `client/src/services/pipelineService.ts`

```typescript
// PRIMA (file statico)
async function fetchPipelineIndex(): Promise<PipelineIndex> {
  const res = await fetch('/pipeline/pipeline-index.json');
  return res.json();
}

// DOPO (API)
async function fetchPipelineIndex(): Promise<PipelineIndex> {
  const res = await fetch('/api/pipeline/index');
  const body = await res.json();
  return body.data;
}
```

Le stesse signature di funzione, stesso tipo di ritorno: nessuna modifica ai componenti React esistenti.

I file statici degli artefatti (i JSON degli step) continuano a essere serviti da `client/public/pipeline/` — il frontend li carica già con path relativi, e i nuovi file prodotti dall'orchestrazione vengono copiati lì dal backend quando un'esecuzione completa (D3 §4.3, punto 1).

---

## 11. Tabella riepilogativa degli endpoint

| Metodo | Path | Auth | Scopo |
|---|---|---|---|
| GET | `/api/pipeline/index` | public | Indice globale (sostituisce file statico) |
| GET | `/api/pipeline/step-config` | public | Config dichiarativa degli step (D1) |
| GET | `/api/pipeline/temi/:id` | public | Stato completo tema |
| GET | `/api/pipeline/ricerche/:id` | public | Stato completo ricerca |
| GET | `/api/pipeline/temi/:id/steps/:stepId/history` | public | Storico esecuzioni step |
| GET | `/api/pipeline/temi/:id/steps/:stepId/inputs` | public | Input esterni forniti |
| GET | `/api/pipeline/temi/:id/pending-decision` | public | Decisione pendente tema |
| GET | `/api/pipeline/ricerche/:id/pending-decision` | public | Decisione pendente ricerca |
| GET | `/api/pipeline/executions/:id/logs` | public | SSE log streaming |
| GET | `/api/pipeline/system/status` | **admin** | Health check server Cowork |
| POST | `/api/pipeline/ricerche` | **admin** | Crea contesto ricerca |
| POST | `/api/pipeline/temi/:id/steps/:stepId/run` | **admin** | Avvia esecuzione step |
| POST | `/api/pipeline/temi/:id/steps/:stepId/inputs` | **admin** | Fornisce input esterno |
| POST | `/api/pipeline/temi/:id/steps/:stepId/skip` | **admin** | Skip step saltabile |
| POST | `/api/pipeline/executions/:id/verify` | **admin** | Verifica/approva step |
| POST | `/api/pipeline/ricerche/:id/decisions` | **admin** | Decisione F2→F3 |
| POST | `/api/pipeline/temi/:id/decisions` | **admin** | Decisione contesto step 7 |
| DELETE | `/api/pipeline/executions/:id` | **admin** | Cancella esecuzione |
| DELETE | `/api/pipeline/external-inputs/:id` | **admin** | Invalida input esterno |
