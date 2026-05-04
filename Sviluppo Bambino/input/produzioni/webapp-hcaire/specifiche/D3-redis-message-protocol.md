# D3 — Message protocol Redis — Orchestrazione pipeline

> **Scopo del documento**: specificare il protocollo di messaggistica Redis tra il backend Express della webapp e il server locale che interfaccia Cowork. Definisce canali, struttura dei messaggi, tipi di evento, gestione dello streaming dei log, timeout e recovery.
>
> **Destinatario**: Claude Code — da leggere prima di implementare i route handler di orchestrazione (D4) e prima di estendere il server locale Cowork. Dipende da D1 e D2.
>
> **Prerequisito**: il server locale Telegram/Redis/Cowork è già funzionante per altri flussi. Il protocollo qui definito si aggiunge a quelli esistenti senza modificarli — usa un namespace di canali dedicato (`hcaire:pipeline:*`).

---

## 1. Panoramica dell'architettura di comunicazione

```
┌─────────────────────────────────┐         ┌──────────────────────────────────┐
│         hcaire-blog             │         │       server locale              │
│  (Express backend, porta 3018)  │         │  (Cowork + Redis client)         │
│                                 │         │                                  │
│  PipelineOrchestrator           │         │  PipelineCommandHandler          │
│    │                            │         │    │                             │
│    ├─ LPUSH ──────────────────────────────────▶ BRPOP                       │
│    │    hcaire:pipeline:commands │         │    │                            │
│    │                            │         │    ▼                            │
│    │                            │         │  esegue step in Cowork          │
│    │                            │         │    │                            │
│    ◀─ SUBSCRIBE ────────────────────────────── PUBLISH                      │
│         hcaire:pipeline:events  │         │    hcaire:pipeline:events        │
│                                 │         │                                  │
└─────────────────────────────────┘         └──────────────────────────────────┘
              │
              ▼
         MongoDB Atlas
    (pipeline_step_executions)
              │
              ▼
     SSE / polling → Frontend
```

**Due canali Redis, ruoli distinti:**

| Canale | Tipo Redis | Direzione | Scopo |
|---|---|---|---|
| `hcaire:pipeline:commands` | List (queue) | backend → server locale | Comandi di esecuzione e controllo |
| `hcaire:pipeline:events` | Pub/Sub | server locale → backend | Log in streaming, notifiche di stato |

**Perché List per i comandi e Pub/Sub per gli eventi:**
- La List garantisce che ogni comando venga processato **esattamente una volta** anche se il server locale si riavvia (BRPOP è bloccante e atomico).
- Il Pub/Sub per gli eventi consente al backend di ricevere log in streaming senza polling, e in futuro potrebbe essere ascoltato anche da altri subscriber (es. un pannello di monitoring separato).

---

## 2. Envelope comune

Tutti i messaggi — sia comandi che eventi — condividono la stessa struttura di envelope.

```typescript
interface PipelineMessage {
  // Identificazione
  type: CommandType | EventType;    // tipo del messaggio (vedi §3 e §4)
  message_id: string;               // UUID v4 generato dal mittente
  timestamp: string;                // ISO 8601 UTC

  // Correlazione
  execution_id: string;             // MongoDB ObjectId di pipeline_step_executions
  context_id: string;               // tema_id o ricerca_id
  step_id: string;                  // es. "f3_step_3"
  run_number: number;               // numero della run (per naming del file output)

  // Payload specifico per tipo (vedi sotto)
  payload: Record<string, unknown>;
}
```

Il campo `execution_id` è il cardine della correlazione: è l'`_id` del documento `pipeline_step_executions` creato dal backend prima di pubblicare il comando. Il server locale lo include in ogni evento, permettendo al backend di aggiornare il documento corretto senza ambiguità.

---

## 3. Comandi (backend → server locale)

Il backend pubblica comandi con `LPUSH hcaire:pipeline:commands <json>`. Il server locale li consuma con `BRPOP hcaire:pipeline:commands 0` (blocking pop, timeout infinito).

### 3.1 `pipeline.step.run` — Avvia esecuzione

Ordina al server locale di avviare l'esecuzione di uno step in Cowork.

```typescript
interface StepRunCommand extends PipelineMessage {
  type: 'pipeline.step.run';
  payload: {
    // Istruzioni per Cowork
    prompt_file: string;            // path al file CLAUDE.md dello step
                                    // es. "f3-step-3-correzione-strutturale/CLAUDE.md"

    // Input files da passare a Cowork (path assoluti sul filesystem del server locale)
    input_files: {
      role: string;                 // es. "lettura-configurazionale", "stress-test"
      path: string;                 // path assoluto al file JSON di input
    }[];

    // Dove scrivere l'output
    output_dir: string;             // cartella in cui Cowork deve salvare l'output
    output_filename: string;        // nome file atteso (es. "correzione-strutturale-v1.json")

    // Parametri opzionali per step con input esterni facoltativi
    extra_params: Record<string, unknown>;   // es. { severita_test: "forte" }

    // Timeout
    timeout_ms: number;             // quanto aspettare prima di dichiarare fallimento
                                    // default: 300000 (5 minuti)
  };
}
```

**Esempio:**

```json
{
  "type": "pipeline.step.run",
  "message_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-04-20T11:01:00Z",
  "execution_id": "6627a1b2c3d4e5f600000001",
  "context_id": "pointing",
  "step_id": "f3_step_3",
  "run_number": 1,
  "payload": {
    "prompt_file": "f3-step-3-correzione-strutturale/CLAUDE.md",
    "input_files": [
      { "role": "lettura-configurazionale", "path": "/data/pipeline/temi/pointing/lettura-configurazionale-v1.json" },
      { "role": "stress-test", "path": "/data/pipeline/temi/pointing/stress-test-v1.json" }
    ],
    "output_dir": "/data/pipeline/temi/pointing/",
    "output_filename": "correzione-strutturale-v1.json",
    "extra_params": {},
    "timeout_ms": 300000
  }
}
```

---

### 3.2 `pipeline.step.cancel` — Cancella esecuzione

Ordina al server locale di interrompere un'esecuzione in corso.

```typescript
interface StepCancelCommand extends PipelineMessage {
  type: 'pipeline.step.cancel';
  payload: {
    reason: string;   // es. "richiesta operatore", "timeout esterno"
  };
}
```

Il server locale deve:
1. Terminare il processo Cowork associato all'`execution_id` (se ancora in esecuzione).
2. Pubblicare un evento `pipeline.step.cancelled`.
3. Non pubblicare `pipeline.step.failed` — sono semanticamente distinti.

---

### 3.3 `pipeline.step.ping` — Health check

Usato dal backend per verificare che il server locale sia attivo e in ascolto.

```typescript
interface StepPingCommand extends PipelineMessage {
  type: 'pipeline.step.ping';
  payload: {
    reply_expected: true;
  };
}
```

Il server locale risponde con `pipeline.step.pong` (vedi §4.5). Non ha `execution_id` significativo — usare un UUID fisso o `"ping"`.

---

## 4. Eventi (server locale → backend)

Il server locale pubblica eventi con `PUBLISH hcaire:pipeline:events <json>`. Il backend è in ascolto con `SUBSCRIBE hcaire:pipeline:events`.

### 4.1 `pipeline.step.started` — Esecuzione avviata

Pubblicato quando Cowork ha preso in carico il task e sta elaborando.

```typescript
interface StepStartedEvent extends PipelineMessage {
  type: 'pipeline.step.started';
  payload: {
    cowork_session_id: string | null;   // ID sessione Cowork, se disponibile
  };
}
```

**Azione backend**: aggiorna `pipeline_step_executions.started_at` e `status → 'in_esecuzione'`; aggiorna `pipeline_contexts.step_states[stepId].status`.

---

### 4.2 `pipeline.step.log` — Riga di log

Pubblicato durante l'esecuzione ogni volta che Cowork emette output. Può arrivare con alta frequenza.

```typescript
interface StepLogEvent extends PipelineMessage {
  type: 'pipeline.step.log';
  payload: {
    text: string;
    level: 'info' | 'warn' | 'error';
  };
}
```

**Azione backend**:
- Accumula in `pipeline_step_executions.log_lines[]` (con throttling — non salvare ogni riga individualmente su MongoDB per evitare write storm; fare bulk insert ogni N righe o ogni K secondi).
- Forwarda via SSE al frontend se c'è un client in ascolto su quella esecuzione.

**Throttling consigliato**: buffer di max 20 righe o 2 secondi, poi flush su MongoDB con `$push: { log_lines: { $each: buffer } }`.

---

### 4.3 `pipeline.step.completed` — Esecuzione completata con successo

```typescript
interface StepCompletedEvent extends PipelineMessage {
  type: 'pipeline.step.completed';
  payload: {
    output_file: string;            // path assoluto del file prodotto
    output_file_relative: string;   // path relativo a pipeline/ (per MongoDB e frontend)
                                    // es. "temi/pointing/correzione-strutturale-v1.json"
    verifica_required: boolean;     // da pipeline-step-config.json
    summary: string | null;         // breve sintesi dell'output (opzionale, da Cowork)
  };
}
```

**Azione backend**:
1. Copia/sposta il file dall'output_dir di produzione a `client/public/pipeline/` (o lo lascia in place se le cartelle coincidono).
2. Aggiorna `pipeline_step_executions`: `status → 'completato'` | `'in_verifica'`, `completed_at`, `output_file`.
3. Aggiorna `pipeline_contexts` via `updateContextStepState()` (vedi D2 §9).
4. Se `verifica_required: false`: valuta se sbloccare step dipendenti (controlla condizioni di abilitazione da D1).
5. Se `verifica_required: true`: entra in `in_verifica`, notifica l'operatore (Telegram opzionale).

---

### 4.4 `pipeline.step.failed` — Esecuzione fallita

```typescript
interface StepFailedEvent extends PipelineMessage {
  type: 'pipeline.step.failed';
  payload: {
    error_source: 'cowork' | 'sistema' | 'timeout';
    error_message: string;
    error_detail: string | null;    // stack trace o output Cowork se disponibile
    partial_output_file: string | null;  // se Cowork ha prodotto output parziale
  };
}
```

**Azione backend**:
1. Aggiorna `pipeline_step_executions.status → 'fallito'`, `error`.
2. Aggiorna `pipeline_contexts`.
3. Notifica operatore (Telegram opzionale).
4. Non sblocca step dipendenti.

---

### 4.5 `pipeline.step.cancelled` — Esecuzione cancellata

```typescript
interface StepCancelledEvent extends PipelineMessage {
  type: 'pipeline.step.cancelled';
  payload: {
    reason: string;
  };
}
```

**Azione backend**: aggiorna status → `'non_avviato'` (lo step torna disponibile per essere rilancato).

---

### 4.6 `pipeline.step.pong` — Risposta a ping

```typescript
interface StepPongEvent extends PipelineMessage {
  type: 'pipeline.step.pong';
  payload: {
    server_version: string;
    active_executions: number;      // quante esecuzioni sono in corso
    uptime_seconds: number;
  };
}
```

---

## 5. Flusso completo di una esecuzione

```
Backend                         Redis                      Server locale
   │                              │                              │
   │ 1. Crea PipelineStepExecution│                              │
   │    (status: 'in_coda')       │                              │
   │                              │                              │
   │ 2. LPUSH commands ──────────▶│                              │
   │    { type: step.run, ... }   │◀── BRPOP ────────────────────│
   │                              │                              │
   │                              │                              │ 3. Avvia Cowork
   │                              │                              │    con input files
   │                              │                              │
   │◀── SUBSCRIBE events ─────────│◀── PUBLISH step.started ─────│ 4. Cowork parte
   │    Aggiorna: in_esecuzione   │                              │
   │                              │                              │
   │◀─────────────────────────────│◀── PUBLISH step.log (×N) ────│ 5. Log in streaming
   │    Buffer → MongoDB          │                              │    (durante elaborazione)
   │    Forward → SSE frontend    │                              │
   │                              │                              │
   │◀─────────────────────────────│◀── PUBLISH step.completed ───│ 6. Cowork ha finito,
   │    Aggiorna: completato      │                              │    file scritto su disco
   │    Copia output in public/   │                              │
   │    Valuta step dipendenti    │                              │
   │                              │                              │
```

**Caso con verifica:**

```
   ...step.completed (verifica_required: true)
   │
   │ 7. status → in_verifica
   │    Notifica operatore
   │
   │ [operatore accede alla webapp, legge output, approva]
   │
   │ 8. POST /api/pipeline/executions/:id/verify
   │    { outcome: "approvato", notes: "..." }
   │
   │ 9. status → verificato
   │    Sblocca step dipendenti
```

**Caso di fallimento con retry:**

```
   ...step.failed
   │
   │ 7. status → fallito
   │    Notifica operatore
   │
   │ [operatore decide di riprovare]
   │
   │ 8. POST /api/pipeline/temi/:id/steps/:stepId/run
   │    (crea nuova execution con run_number: 2)
   │
   │ 9. LPUSH commands { type: step.run, run_number: 2, ... }
   │    (il ciclo riparte da 1)
```

---

## 6. Gestione timeout

Ogni comando `step.run` include un `timeout_ms`. Il server locale è responsabile di rispettarlo:

```
server locale:
  1. Riceve step.run con timeout_ms: 300000
  2. Avvia Cowork e setta un timer locale
  3. Se il timer scade prima di step.completed:
     → Termina processo Cowork
     → PUBLISH step.failed { error_source: "timeout", error_message: "Timeout dopo 300s" }
```

Il backend ha un **timeout di sorveglianza indipendente** (`execution_watchdog`): se dopo `timeout_ms + 60000` (grace period) un'esecuzione è ancora in stato `in_esecuzione` senza aver ricevuto eventi, il backend la considera persa:

```typescript
// Eseguito da un cron job ogni 5 minuti
async function executionWatchdog() {
  const staleThreshold = new Date(Date.now() - MAX_EXECUTION_MS);
  const stale = await db.pipeline_step_executions.find({
    status: { $in: ['in_coda', 'in_esecuzione'] },
    started_at: { $lt: staleThreshold }
  });
  for (const exec of stale) {
    await updateExecutionStatus(exec._id, 'fallito', {
      error_source: 'timeout',
      error_message: 'Watchdog: nessun evento ricevuto oltre la soglia'
    });
  }
}
```

---

## 7. Gestione disconnessioni e recovery

### Server locale che si riavvia

Il server locale, all'avvio, deve:

1. Verificare se ci sono `pipeline_step_executions` con status `in_esecuzione` (query su MongoDB).
2. Per ciascuna: pubblicare `pipeline.step.failed` con `error_source: 'sistema'`, `error_message: 'Server riavviato durante esecuzione'`.
3. Svuotare la coda `hcaire:pipeline:commands` e riprocessare i messaggi rimasti (le execution con status `in_coda` sono già in MongoDB — il backend può ri-pubblicare i comandi).

### Backend che si riavvia

Il backend, all'avvio:

1. Re-subscribe a `hcaire:pipeline:events`.
2. Verifica esecuzioni con status `in_coda` o `in_esecuzione` su MongoDB.
3. Per le `in_coda`: ri-pubblica il comando (idempotente perché il server locale controlla duplicati tramite `execution_id`).
4. Per le `in_esecuzione`: il server locale sta ancora girando — gli eventi arriveranno quando il backend si ri-connette al canale.

### Deduplicazione lato server locale

Il server locale tiene in memoria un set di `execution_id` attivi. Se riceve un comando con un `execution_id` già presente (duplicato per retry del backend), lo scarta e pubblica immediatamente `pipeline.step.started` per notificare che è già in esecuzione.

---

## 8. Notifiche Telegram (layer opzionale)

Il server locale può inviare notifiche Telegram per eventi rilevanti, usando il canale già esistente nell'infrastruttura. Questo è **opzionale** e non fa parte del protocollo Redis core — è un side effect del server locale.

**Notifiche consigliate:**

| Evento Redis | Notifica Telegram |
|---|---|
| `step.completed` con `verifica_required: true` | "✅ Step [label] completato — richiede verifica. Apri la webapp." |
| `step.failed` | "❌ Step [label] fallito: [error_message]" |
| `attende_decisione` | "🔔 Pipeline in attesa di decisione: [description]" |

Il testo della notifica viene composto dal server locale usando i campi del messaggio Redis. Il backend non interagisce con Telegram — quella logica rimane tutta nel server locale.

---

## 9. Interfaccia TypeScript per il backend (`PipelineMessageBus`)

Il backend implementa una classe che incapsula tutta la logica Redis. Claude Code deve usare questa interfaccia nei route handler, non accedere direttamente a Redis.

```typescript
interface PipelineMessageBus {
  // Invia un comando di esecuzione
  // Ritorna dopo aver fatto LPUSH (non aspetta la risposta)
  sendStepRun(params: {
    execution_id: string;
    context_id: string;
    step_id: string;
    run_number: number;
    prompt_file: string;
    input_files: { role: string; path: string }[];
    output_dir: string;
    output_filename: string;
    extra_params?: Record<string, unknown>;
    timeout_ms?: number;
  }): Promise<void>;

  // Cancella un'esecuzione in corso
  sendStepCancel(execution_id: string, reason: string): Promise<void>;

  // Verifica che il server locale sia attivo
  ping(): Promise<{ active: boolean; active_executions: number }>;

  // Registra un handler per gli eventi in arrivo
  // Chiamato all'avvio del backend, gira per tutta la vita del processo
  onEvent(handler: (event: PipelineMessage) => Promise<void>): void;
}
```

L'implementazione usa `ioredis` (già disponibile nel progetto o da installare). Un'istanza per il LPUSH, una separata per SUBSCRIBE (Redis non permette pub/sub e comandi normali sulla stessa connessione).

---

## 10. Responsabilità del server locale Cowork

Il server locale deve implementare `PipelineCommandHandler`, che:

1. **Legge comandi** con `BRPOP hcaire:pipeline:commands 0` in un loop.
2. **Per `pipeline.step.run`**:
   a. Verifica che `execution_id` non sia già in esecuzione (deduplicazione).
   b. Costruisce il prompt da passare a Cowork: legge il `prompt_file` CLAUDE.md, prepara il contesto con i file di input, lancia Cowork.
   c. Cattura l'output di Cowork riga per riga → pubblica `pipeline.step.log`.
   d. Quando Cowork termina: pubblica `pipeline.step.completed` o `pipeline.step.failed`.
3. **Per `pipeline.step.cancel`**: termina il processo Cowork, pubblica `pipeline.step.cancelled`.
4. **Per `pipeline.step.ping`**: pubblica `pipeline.step.pong`.

La costruzione del prompt per Cowork è responsabilità del server locale: deve sapere come leggere un CLAUDE.md di step e come passare i file di input come contesto alla sessione Cowork. Il formato esatto dipende dall'implementazione Cowork esistente — il server locale usa le stesse API che già usa per gli altri flussi.

---

## 11. Configurazione

Variabili d'ambiente da aggiungere a `server/.env`:

```env
# Redis
REDIS_URL=redis://localhost:6379      # o Redis Cloud se disponibile
REDIS_PIPELINE_COMMANDS_KEY=hcaire:pipeline:commands
REDIS_PIPELINE_EVENTS_CHANNEL=hcaire:pipeline:events

# Timeout esecuzioni
PIPELINE_DEFAULT_TIMEOUT_MS=300000   # 5 minuti
PIPELINE_WATCHDOG_GRACE_MS=60000     # 1 minuto di grace dopo timeout

# Percorsi filesystem (devono corrispondere a quelli del server locale)
PIPELINE_PUBLIC_DIR=/path/to/client/public/pipeline
PIPELINE_SOURCE_DIR=/path/to/Sviluppo Bambino/output/produzioni
```

Le stesse variabili `REDIS_*` devono essere configurate nel server locale Cowork.

---

## 12. Composizione del prompt per Cowork

> **Problema**: i file `CLAUDE.md` di ogni step sono scritti per esecuzione manuale. Citano gli input in modo generico ("Ti vengono forniti: un dispositivo prodotto in F3 Step 1..."), hanno percorsi di output hardcoded, e descrivono gli input esterni come istruzioni al ricercatore. Per l'esecuzione automatica il server locale deve costruire un prompt composito prima di passare il tutto a Cowork.

### 12.1 Struttura del prompt composito

Il server locale NON passa il CLAUDE.md grezzo a Cowork. Costruisce un prompt finale in tre blocchi concatenati:

```
╔══════════════════════════════════════════════════════════╗
║  BLOCCO 1 — CONTESTO INPUT  (iniettato dal server)       ║
╠══════════════════════════════════════════════════════════╣
║  BLOCCO 2 — ISTRUZIONI STEP  (da CLAUDE.md, adattato)    ║
╠══════════════════════════════════════════════════════════╣
║  BLOCCO 3 — DIRETTIVA OUTPUT  (iniettata dal server)     ║
╚══════════════════════════════════════════════════════════╝
```

---

### 12.2 Blocco 1 — Contesto input

Preposto al CLAUDE.md, fornisce i file di input concreti per questa esecuzione.

```
---
CONTESTO DI ESECUZIONE AUTOMATICA
Step: {step_id}  |  Tema: {context_id}  |  Run: #{run_number}

FILE DI INPUT DISPONIBILI
{per ogni input_file del comando step.run:}
• [{role}]  {path assoluto}
  Contenuto: {JSON.stringify(content, null, 2)}   ← solo se il file è < 50KB
              oppure
  Percorso per lettura diretta: {path}             ← se > 50KB

{se ci sono input esterni forniti dal ricercatore:}
INPUT FORNITI DAL RICERCATORE
{input_id}: {JSON.stringify(data, null, 2)}

---
```

**Soglia 50KB**: i file JSON degli step sono tipicamente piccoli (< 20KB). Inserire il contenuto inline evita che Cowork debba leggerli separatamente. Se un file fosse insolitamente grande, passare solo il path e lasciare che Cowork lo legga.

---

### 12.3 Blocco 2 — Istruzioni step (da CLAUDE.md)

Il contenuto del CLAUDE.md viene incluso **quasi integralmente**, con due sole modifiche:

1. **Rimozione del percorso di output hardcoded**: la sezione `### Salvataggio` (o equivalente) che specifica nome file e cartella viene rimossa — sarà sostituita dal Blocco 3.
2. **Nessun'altra modifica**: vincoli, obiettivi, formato JSON dell'output rimangono invariati.

Il server locale individua la sezione di output con una regex semplice:

```javascript
// Rimuove la sezione "### Salvataggio" o "### FORMATO DI OUTPUT > Salvataggio"
// con il suo contenuto fino alla prossima sezione o fine file
const cleanedPrompt = rawClaudeMd.replace(
  /###\s*Salvataggio[\s\S]*?(?=\n###|\n---|\n##|$)/gi,
  ''
).trim();
```

---

### 12.4 Blocco 3 — Direttiva output

Apposto al prompt, sovrascrive qualsiasi indicazione di percorso presente nel CLAUDE.md.

```
---
DIRETTIVA OUTPUT (SOVRASCRIVE QUALSIASI PERCORSO NEL TESTO SOPRA)

Salva il risultato come file JSON con queste specifiche:
• Nome file: {output_filename}          (es. correzione-strutturale-v2.json)
• Cartella: {output_dir}                (es. C:\...\output\produzioni\temi\pointing\)
• Formato: JSON valido, nessun testo prima o dopo
• Non creare sottocartelle aggiuntive

Quando hai completato la scrittura del file, termina la sessione.
---
```

---

### 12.5 Iniezione degli input esterni

Gli step con `inputs_esterni` obbligatori (f2_step_2, f3_step_7, f3_step_10) hanno nel loro CLAUDE.md una sezione esplicita che descrive l'input richiesto al ricercatore (es. "⬥ INPUT ESTERNO — OBBLIGATORIO"). Nel prompt composito quella sezione diventa **ridondante** perché i dati sono già nel Blocco 1.

Il server locale NON rimuove quella sezione: Cowork la legge insieme ai dati iniettati nel Blocco 1, il che rafforza la coerenza del prompt (le istruzioni e i dati sono entrambi presenti).

**Esempio concreto per f3_step_7** con contesto clinico:

```
--- BLOCCO 1 ---
FILE DI INPUT DISPONIBILI
• [correzione-strutturale]  C:\...\correzione-strutturale-clinico-v2.json
  Contenuto: { "step": "f3_step_3", "corrected_device": { ... } }

• [stabilizzazione-proxy-b]  C:\...\stabilizzazione-proxy-v1b.json
  Contenuto: { "step": "f3_step_6b", "operative_proxy": { ... } }

INPUT FORNITI DAL RICERCATORE
contesto_ambito: {
  "target_domain": "clinico",
  "target_subdomain": "neuropsviluppo",
  "age_range": "9-24 mesi",
  "setting": "ambulatorio, setting semi-strutturato",
  "observer_profile": "logopedista, neuropsichiatra infantile"
}

--- BLOCCO 2 ---
RUOLO
Sei un agente di verifica metodologica...
[contenuto CLAUDE.md f3-step-7 completo, senza la sezione Salvataggio]

--- BLOCCO 3 ---
DIRETTIVA OUTPUT
Salva il risultato come file JSON:
• Nome file: trasferibilità-clinico-v1.json
• Cartella: C:\...\output\produzioni\temi\pointing\
...
```

---

### 12.6 Caso speciale: f3_step_10 (casi di stress test)

I casi di stress test (5 oggetti JSON) sono voluminosi. Il server locale li inietta nel Blocco 1 come array JSON completo. Il CLAUDE.md di step 10 contiene già un template `MICRO CASI` con esempi placeholder — nel prompt composito quei placeholder vengono **sostituiti** con i casi reali forniti dal ricercatore:

```javascript
// Sostituisce il template MICRO CASI con i casi reali
const withRealCases = cleanedPrompt.replace(
  /```json\s*"cases":\s*\[[\s\S]*?\]\s*```/,
  `I casi reali da usare per questo stress test sono nel Blocco 1 (contesto_ambito.cases).`
);
```

---

## 13. Implicazioni per D4 (API spec Express)

I route handler di orchestrazione useranno `PipelineMessageBus` come segue:

- `POST /api/pipeline/temi/:id/steps/:stepId/run` → crea `PipelineStepExecution` su MongoDB → chiama `messageBus.sendStepRun(...)` → risponde `202 Accepted` con `execution_id`.
- `DELETE /api/pipeline/executions/:executionId` → chiama `messageBus.sendStepCancel(...)` → risponde `202 Accepted`.
- `GET /api/pipeline/executions/:executionId/logs` → risponde con SSE: subscribe a `hcaire:pipeline:events`, filtra per `execution_id`, forwarda i `pipeline.step.log`.

Il backend **non aspetta** la risposta del server locale nella stessa richiesta HTTP. Il frontend monitora lo stato tramite polling su `GET /api/pipeline/temi/:id` (che legge da MongoDB) o tramite SSE per i log in tempo reale.
