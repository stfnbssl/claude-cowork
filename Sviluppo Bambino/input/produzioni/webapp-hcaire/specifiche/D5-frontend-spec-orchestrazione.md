# D5 — Frontend spec — Pannello admin, form input, polling

> **Scopo del documento**: specifica completa dei componenti React da aggiungere al client per l'orchestrazione della pipeline. Definisce componenti, props, comportamento, gestione dello stato, polling/SSE, e flussi utente principali.
>
> **Destinatario**: Claude Code — da implementare in `client/src/`. Dipende da D1, D2, D3, D4.
>
> **Principio guida**: i componenti di orchestrazione si aggiungono come **layer admin** sopra l'interfaccia read-only esistente. Gli utenti non autenticati vedono esattamente la stessa esperienza di prima. Gli admin vedono i controlli in overlay. Nessun componente esistente viene riscritto.

---

## 1. Principi di integrazione

### 1.1 Dove appaiono i controlli admin

| Pagina esistente | Integrazione orchestrazione |
|---|---|
| `SviluppoBambinoPipelineMap` | Banner "Modalità orchestrazione" + pulsante "Nuova ricerca" + per ogni tema: indicatore stato step con quick-launch |
| `SviluppoBambinoPipelineDeviceOverview` | Tab aggiuntiva **"Esegui"** (visibile solo admin) con `OrchestrationPanel` completo |
| Qualsiasi pagina pipeline | `PendingDecisionBanner` globale se c'è una decisione pendente |

### 1.2 Rilevamento ruolo admin

Usare il context Clerk già presente (`useAuth` / `useUser`). Il check è:

```typescript
// client/src/hooks/useIsAdmin.ts  (nuovo file, poche righe)
import { useUser } from '@clerk/clerk-react';

export function useIsAdmin(): boolean {
  const { user } = useUser();
  return user?.publicMetadata?.role === 'admin' ?? false;
}
```

Tutto il layer orchestrazione è condizionato a `useIsAdmin()`. Se false: nessun componente admin viene montato, nessuna chiamata alle API admin viene fatta.

### 1.3 Struttura file nuovi

```
client/src/
├── hooks/
│   ├── useIsAdmin.ts                      ← nuovo
│   ├── usePipelineOrchestration.ts        ← nuovo (hook principale)
│   └── useExecutionLogs.ts                ← nuovo (SSE)
├── components/pipeline/orchestration/
│   ├── OrchestrationPanel.tsx             ← contenitore principale
│   ├── StepList.tsx                       ← lista step con controlli
│   ├── StepRow.tsx                        ← riga singolo step
│   ├── StepStatusBadge.tsx               ← badge stato (riuso anche in read-only)
│   ├── ExternalInputForm.tsx              ← form input esterni
│   ├── HumanDecisionDialog.tsx            ← modal decisioni umane
│   ├── ExecutionLogViewer.tsx             ← drawer log SSE
│   ├── VerificationPanel.tsx              ← pannello verifica output
│   └── PendingDecisionBanner.tsx          ← banner globale decisione pendente
└── services/
    └── pipelineOrchestratorService.ts     ← nuovo: wrappa le API admin (D4)
```

---

## 2. Hook principale: `usePipelineOrchestration`

È il data layer di tutto il sistema di orchestrazione. Va montato una sola volta nel componente di pagina (`SviluppoBambinoPipelineDeviceOverview`), non in ogni StepRow.

```typescript
// client/src/hooks/usePipelineOrchestration.ts

interface UsePipelineOrchestrationOptions {
  temaId: string;
  pollingIntervalMs?: number;   // default: 5000
}

interface UsePipelineOrchestrationResult {
  // Dati
  context: PipelineContext | null;
  stepConfig: StepConfig[];
  externalInputs: PipelineExternalInput[];
  isLoading: boolean;
  error: string | null;

  // Stato derivato per ogni step (calcolato da context + stepConfig)
  stepStates: Record<string, EnrichedStepState>;

  // Azioni (chiamano pipelineOrchestratorService + aggiornano ottimisticamente)
  runStep: (stepId: string, extraParams?: Record<string, unknown>) => Promise<RunStepResult>;
  cancelExecution: (executionId: string) => Promise<void>;
  verifyExecution: (executionId: string, outcome: VerificaOutcome, notes?: string, feedback?: string) => Promise<VerifyResult>;
  skipStep: (stepId: string, reason: string) => Promise<void>;
  submitExternalInput: (stepId: string, inputId: string, data: Record<string, unknown>) => Promise<void>;
  submitDecision: (decision: HumanDecisionPayload) => Promise<void>;

  // Refresh manuale
  refresh: () => void;
}

interface EnrichedStepState extends StepState {
  // Da stepConfig (D1)
  label: string;
  verifica_required: boolean;
  can_skip: boolean;
  missing_pipeline_deps: { step_id: string; required_status: string; current_status: string }[];
  missing_external_inputs: { input_id: string; label: string }[];
  is_launchable: boolean;     // true se tutte le condizioni sono soddisfatte
  action: StepAction;         // azione primaria disponibile (vedi §4.2)
}

type StepAction =
  | 'launch'            // step pronto per essere lanciato
  | 'provide_input'     // mancano input esterni (ma dipendenze pipeline ok)
  | 'awaiting_deps'     // dipendenze pipeline non ancora soddisfatte
  | 'cancel'            // step in_coda o in_esecuzione
  | 'view_logs'         // step in_esecuzione: può aprire il log viewer
  | 'verify'            // step in_verifica
  | 'relaunch'          // step fallito o richiede_correzione
  | 'decide'            // step bloccato da pending_decision
  | 'none'              // step completato, verificato, saltato — nessuna azione primaria
```

### Logica di polling

```typescript
// Dentro usePipelineOrchestration

const hasActiveSteps = useMemo(() =>
  Object.values(context?.step_states ?? {}).some(s =>
    ['in_coda', 'in_esecuzione'].includes(s.status)
  ), [context]);

// Polling attivo solo quando ci sono step in esecuzione
useEffect(() => {
  if (!hasActiveSteps) return;
  const interval = setInterval(refresh, pollingIntervalMs ?? 5000);
  return () => clearInterval(interval);
}, [hasActiveSteps, pollingIntervalMs]);
```

Il polling si autospegne quando non ci sono step attivi. Si riaccende non appena un'azione (run, relaunch) porta uno step in `in_coda`.

---

## 3. Integrazione in `SviluppoBambinoPipelineDeviceOverview`

L'unica modifica alla pagina esistente è aggiungere la tab "Esegui" condizionalmente all'utente admin:

```tsx
// Dentro SviluppoBambinoPipelineDeviceOverview.tsx
// AGGIUNGERE, non riscrivere

const isAdmin = useIsAdmin();
const orchestration = usePipelineOrchestration({ temaId });  // solo se admin

// Nelle tabs esistenti (Panoramica, Provenienza, Correzioni, Storia):
// AGGIUNGERE tab "Esegui" alla fine, visibile solo se isAdmin

{isAdmin && (
  <Tab label="Esegui" value="esegui" />
)}

// Nel contenuto della tab:
{isAdmin && activeTab === 'esegui' && (
  <OrchestrationPanel
    temaId={temaId}
    orchestration={orchestration}
  />
)}
```

`SviluppoBambinoPipelineMap` riceve un'integrazione analoga ma più leggera: solo indicatori di stato e pulsante quick-launch per ogni tema nella card.

---

## 4. `OrchestrationPanel` e `StepList`

### 4.1 `OrchestrationPanel`

Contenitore principale della tab "Esegui". Mostra:

1. **Header**: stato generale del tema (badge robustezza, n. step completati su totale, correzioni residue).
2. **System status indicator**: pill "Server Cowork: attivo / non raggiungibile" — caricato una volta al mount con `GET /api/pipeline/system/status`.
3. **`PendingDecisionBanner`** (se `context.pending_decision !== null`).
4. **`StepList`**: lista completa degli step F3 (o F2 se contesto ricerca).
5. **Drawer `ExecutionLogViewer`** (se `activeExecutionId !== null`).
6. **Modal `VerificationPanel`** (se `verifyingExecutionId !== null`).
7. **Modal `ExternalInputForm`** (se `inputFormStep !== null`).
8. **Modal `HumanDecisionDialog`** (se `context.pending_decision !== null` e admin apre la dialog).

```tsx
interface OrchestrationPanelProps {
  temaId: string;
  orchestration: UsePipelineOrchestrationResult;
}
```

### 4.2 `StepRow`

Una riga per ogni step. Mostra stato e offre l'azione primaria disponibile.

```tsx
interface StepRowProps {
  stepId: string;
  stepState: EnrichedStepState;
  onLaunch: () => void;
  onCancel: () => void;
  onVerify: () => void;
  onProvideInput: () => void;
  onViewLogs: () => void;
  onSkip: () => void;
  onDecide: () => void;
}
```

**Layout di una riga:**

```
[StatusBadge] [Step label]  [run #N]  [BlockingReason?]  [ActionButton]  [SecondaryActions▾]
```

**`StepStatusBadge`** — colori per stato:

| Status | Colore | Icona | Testo |
|---|---|---|---|
| `non_avviato` | slate | ○ | Non avviato |
| `attende_input` | blue | ✎ | Fornire input |
| `attende_decisione` | amber | ⏳ | Decisione richiesta |
| `in_coda` | blue | ⋯ | In coda |
| `in_esecuzione` | blue (pulse) | ⟳ | In esecuzione |
| `completato` | emerald | ✓ | Completato |
| `in_verifica` | amber | ◎ | In verifica |
| `verificato` | emerald | ✓✓ | Verificato |
| `richiede_correzione` | red | ✗ | Da correggere |
| `fallito` | red | ✗ | Fallito |
| `saltato` | slate | — | Saltato |

**ActionButton** — pulsante primario per `action`:

| `action` | Pulsante | Colore | Variante |
|---|---|---|---|
| `launch` | "Lancia" | emerald | filled |
| `provide_input` | "Fornisci input" | blue | outline |
| `awaiting_deps` | "In attesa" | slate | disabled, tooltip con dipendenze bloccanti |
| `cancel` | "Annulla" | red | outline |
| `view_logs` | "Vedi log" | blue | outline |
| `verify` | "Verifica output" | amber | filled |
| `relaunch` | "Rilancia" | orange | outline |
| `decide` | "Prendi decisione" | amber | filled |
| `none` | — | — | nessun pulsante |

**SecondaryActions** (menu a tendina `▾`):
- Se step saltabile e non saltato: "Salta step"
- Se step completato/verificato: "Vedi storico run"
- Se step fallito: "Vedi log errore"
- Se step in_verifica: (solo per step 6b) "Richiede integrazione (6c)"

**Blocco di motivazione** — appare sotto la riga quando `action === 'awaiting_deps'` o `action === 'provide_input'`:

```
⚠ In attesa di:
  • f3_step_4 (richiede: verificato — attuale: in_verifica)
  • f3_step_5 (richiede: verificato — attuale: non_avviato)
```

```
✎ Input richiesti prima del lancio:
  • Contesto/ambito target  [Fornisci →]
```

---

## 5. `ExternalInputForm`

Modal con form per fornire gli input esterni obbligatori prima del lancio di uno step. Compare quando l'utente clicca "Fornisci input" o "Lancia" su uno step con input mancanti.

```tsx
interface ExternalInputFormProps {
  temaId: string;
  stepId: string;
  inputConfig: ExternalInputConfig[];   // da pipeline-step-config.json
  existingInputs: PipelineExternalInput[];
  onSubmit: (inputId: string, data: Record<string, unknown>) => Promise<void>;
  onClose: () => void;
}
```

Il form è **guidato dallo schema**: ogni input esterno ha un `schema` in `pipeline-step-config.json` che definisce i campi. Il componente legge lo schema e renderizza i campi corrispondenti.

### Form per ogni step con input obbligatori

**f2_step_2 — Scelta del tema**

```
Tema selezionato *          [___________________________]  (text)
Descrizione                 [___________________________]  (textarea)
Motivazione della scelta    [___________________________]  (textarea)
```

**f3_step_7 — Contesto/ambito**

```
Dominio target *            [clinico ▾]                   (select: clinico, educativo, formazione, politiche)
Sottodominio                [___________________________]  (text, es. "neuropsviluppo")
Fascia d'età                [___________________________]  (text, es. "9-24 mesi")
Setting                     [___________________________]  (text, es. "ambulatorio")
Profilo osservatore         [___________________________]  (text, es. "logopedista")
Note                        [___________________________]  (textarea, opzionale)
```

**f3_step_10 — Casi di stress test**

Cinque sezioni, una per tipo di caso. Ogni sezione è espandibile:

```
┌─ Caso 1: Assente ────────────────────────────────── [espandi ▾] ─┐
│  Descrizione del caso *   [________________________________]      │
│                           (textarea — descrivere la situazione)   │
└──────────────────────────────────────────────────────────────────┘
┌─ Caso 2: Parziale ─────────────────────────────────────────────┐
│  ...                                                            │
└─────────────────────────────────────────────────────────────────┘
... (×5 tipi fissi: assente, parziale, chiudente, apparente_scripted, quasi_indistinguibile)
```

### Comportamento del form

1. Al mount: pre-popola i campi con `existingInputs` se presenti (l'utente può modificare).
2. Validazione client-side prima del submit (campi obbligatori non vuoti).
3. Al submit: chiama `orchestration.submitExternalInput(stepId, inputId, data)`.
4. Dopo submit riuscito: chiude il modal e aggiorna lo stato. Se ora tutti gli input sono forniti, abilita automaticamente il pulsante "Lancia" nello StepRow.

---

## 6. `HumanDecisionDialog`

Modal per i due punti di decisione non automatizzabile (D2 §2.2).

```tsx
interface HumanDecisionDialogProps {
  decision: HumanDecision;
  temaId?: string;
  ricercaId?: string;
  context: PipelineContext;
  onSubmit: (payload: HumanDecisionPayload) => Promise<void>;
  onClose: () => void;
}
```

### Variante 1: `f2_to_f3_tema_selection`

Appare dopo che `f2_step_5` è verificato in una ricerca.

```
╔══════════════════════════════════════════════════════════════════╗
║  Selezione tema da portare in F3                                 ║
╠══════════════════════════════════════════════════════════════════╣
║  Dalla ricerca "[label ricerca]" sono disponibili i seguenti     ║
║  temi candidati. Seleziona quello da portare in F3:              ║
║                                                                  ║
║  ○  Pointing precoce                                             ║
║     asse_dominante · 3 assi confermati                           ║
║                                                                  ║
║  ○  Richiesta di aiuto                                           ║
║     multi_assiale · 4 assi confermati                            ║
║                                                                  ║
║  ○  ... (altri temi dall'output-family)                          ║
║                                                                  ║
║  Tema nuovo o derivato da dispositivo esistente?                  ║
║  ○ Tema nuovo (avvia da f3_step_1)                               ║
║  ○ Derivato da: [__________________] (seleziona tema sorgente)   ║
║                                                                  ║
║  ID tema da creare: [pointing-clinico     ]  (slug, modificabile)║
║  Label:             [Pointing clinico     ]                      ║
║                                                                  ║
║                              [Annulla]  [Conferma e crea tema →] ║
╚══════════════════════════════════════════════════════════════════╝
```

La lista dei temi candidati è pre-popolata dall'`options[]` in `HumanDecision` (D2 §3), che il backend popola leggendo l'`output-family` della ricerca.

### Variante 2: `step7_context_selection`

Appare quando `f3_step_7` entra in `attende_decisione`. Mostra il form di contesto (identico a §5 `f3_step_7`) con un header esplicativo:

```
╔══════════════════════════════════════════════════════════════════╗
║  Definizione del contesto per il dispositivo                     ║
╠══════════════════════════════════════════════════════════════════╣
║  Questa scelta definisce il vincolo di realtà del dispositivo    ║
║  finale. Non è un parametro tecnico — è una decisione di         ║
║  ricerca con implicazioni strutturali.                           ║
║                                                                  ║
║  [form contesto — identico a ExternalInputForm f3_step_7]        ║
║                                                                  ║
║  Ho verificato che questo contesto è corretto per il tema        ║
║  "[label tema]".  ☐ Confermo                                     ║
║                                                                  ║
║                              [Annulla]  [Conferma e prosegui →]  ║
╚══════════════════════════════════════════════════════════════════╝
```

Il checkbox "Confermo" è obbligatorio prima di abilitare il pulsante. Questo non è un ostacolo UX — è un freno deliberato che richiama l'attenzione sul peso della decisione.

---

## 7. `ExecutionLogViewer`

Drawer laterale (o panel a scomparsa dalla parte destra) che mostra i log in tempo reale di un'esecuzione.

```tsx
interface ExecutionLogViewerProps {
  executionId: string;
  stepId: string;
  stepLabel: string;
  runNumber: number;
  onClose: () => void;
}
```

### Hook SSE: `useExecutionLogs`

```typescript
// client/src/hooks/useExecutionLogs.ts

interface UseExecutionLogsResult {
  logs: LogLine[];
  status: ExecutionStatus | null;   // aggiornato quando arriva evento 'status'
  isConnected: boolean;
  isFinished: boolean;
}

function useExecutionLogs(executionId: string): UseExecutionLogsResult {
  const [logs, setLogs] = useState<LogLine[]>([]);
  const [status, setStatus] = useState<ExecutionStatus | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const [isFinished, setIsFinished] = useState(false);

  useEffect(() => {
    const es = new EventSource(`/api/pipeline/executions/${executionId}/logs`);

    es.addEventListener('log', (e) => {
      const line: LogLine = JSON.parse(e.data);
      setLogs(prev => [...prev, line]);
    });

    es.addEventListener('status', (e) => {
      const { status } = JSON.parse(e.data);
      setStatus(status);
    });

    es.addEventListener('done', () => {
      setIsFinished(true);
      es.close();
    });

    es.onopen = () => setIsConnected(true);
    es.onerror = () => { setIsConnected(false); es.close(); };

    return () => es.close();
  }, [executionId]);

  return { logs, status, isConnected, isFinished };
}
```

### Layout del drawer

```
┌────────────────────────────────────────────────────────── ✕ ──┐
│  f3_step_3 — Correzione strutturale  [Run #1]                 │
│  ● In esecuzione                                              │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  11:01:05  INFO  Avvio step f3_step_3 per tema pointing       │
│  11:01:12  INFO  Caricamento dispositivo di lettura...        │
│  11:03:44  INFO  Analisi delle fratture dallo stress test...  │
│  11:07:21  WARN  Dimensione co-regolatoria: articolazione     │
│                  insufficiente — applicazione correzione       │
│  11:14:30  INFO  Output scritto: correzione-strutturale-v1.json│
│                                                               │
│  [auto-scroll attivo]                          [Copia log ↓]  │
└───────────────────────────────────────────────────────────────┘
```

- Sfondo nero/grigio scuro, font monospace, colori per livello: bianco (info), giallo (warn), rosso (error).
- Auto-scroll verso il basso mentre arrivano nuove righe. L'utente può scorrere su: l'auto-scroll si ferma. Riprende se l'utente torna in fondo.
- Quando lo step completa: appare un banner colorato in fondo (`✓ Completato` | `✗ Fallito`) e il drawer rimane aperto.
- Se `verifica_required` e completato con successo: appare un pulsante "Vai alla verifica →" in fondo al drawer.

---

## 8. `VerificationPanel`

Panel (modal o pagina intera, da valutare in base allo spazio disponibile) per la verifica umana dell'output di uno step.

```tsx
interface VerificationPanelProps {
  executionId: string;
  stepId: string;
  stepLabel: string;
  outputFile: string;       // path relativo per fetch del JSON da /pipeline/
  onVerify: (outcome: VerificaOutcome, notes: string, feedback: string) => Promise<void>;
  onClose: () => void;
}
```

### Layout

```
┌──────────────────────────────────────────────────────────────┐
│  Verifica output: f3_step_3 — Correzione strutturale  [Run #1]│
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  OUTPUT PRODOTTO                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  [Rendering del JSON via componente DeviceViewer       │  │
│  │   o StressTestDashboard, in base al tipo di step]      │  │
│  │                                                        │  │
│  │  Per step che producono un dispositivo: mostra         │  │
│  │  DeviceViewer con l'output file caricato.              │  │
│  │  Per stress test: StressTestDashboard.                 │  │
│  │  Per altri step: JSON pretty-printed in card.          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ESITO DELLA VERIFICA                                        │
│                                                              │
│  ○ Approvato — lo step è completato, sblocca i dipendenti   │
│  ○ Richiede correzione — rilancia lo step                   │
│  ○ Richiede integrazione (6c)  [solo per f3_step_6b]        │
│                                                              │
│  Note (opzionale):                                           │
│  [________________________________________________]          │
│                                                              │
│  Motivazione (obbligatoria se non approvato):               │
│  [________________________________________________]          │
│                                                              │
│                          [Annulla]  [Conferma verifica →]    │
└──────────────────────────────────────────────────────────────┘
```

**Rendering dell'output per tipo di step**:

| Step | Componente di preview |
|---|---|
| f3_step_1, f3_step_9 | `DeviceViewer` (read-only, layout compatto) |
| f3_step_2 | `StressTestDashboard` (read-only) |
| f3_step_3 | `DeviceViewer` (corrected_device) + `CorrectionsLog` |
| f3_step_10 | `StressTestDashboard` completo |
| altri | JSON pretty-printed in blocco scorrevole |

Il `VerificationPanel` riusa i componenti esistenti — non ridisegna la visualizzazione, la ingloba in un contesto di revisione.

---

## 9. `PendingDecisionBanner`

Banner sticky che appare in cima alla pagina quando c'è una decisione umana pendente. Non-admin non lo vede.

```tsx
interface PendingDecisionBannerProps {
  decision: HumanDecision;
  onOpenDialog: () => void;
}
```

```
┌──────────────────────────────────────────────────────────── ✕ ─┐
│  🔔 Decisione richiesta: Selezione tema da portare in F3         │
│  La pipeline è in attesa di una scelta strutturale.              │
│                              [Prendi decisione →]                │
└──────────────────────────────────────────────────────────────────┘
```

Colore: sfondo amber-50, bordo amber-300. Non è dismissibile senza prendere la decisione.

---

## 10. Polling e aggiornamenti di stato

### Strategia complessiva

```
Evento utente              →  Aggiornamento ottimistico immediato in UI
                           +  Chiamata API (fire)
                           +  Polling attivo ogni 5s (se step attivi)

Polling riceve nuovo stato →  Sovrascrive lo stato ottimistico con quello reale
```

L'aggiornamento ottimistico evita che la UI sembri "lenta" dopo un'azione admin. Il polling garantisce che lo stato sia sempre allineato con la realtà.

### Quando il polling è attivo

```typescript
// In usePipelineOrchestration

const ACTIVE_STATUSES = ['in_coda', 'in_esecuzione'];

const hasActiveSteps = Object.values(stepStates).some(s =>
  ACTIVE_STATUSES.includes(s.status)
);

// Polling ogni 5s solo se c'è qualcosa in esecuzione
// Si spegne automaticamente quando tutti gli step sono fermi
```

### Quando usare SSE vs polling

| Situazione | Meccanismo |
|---|---|
| Step in `in_esecuzione`, log viewer aperto | **SSE** su `/api/pipeline/executions/:id/logs` |
| Step in `in_coda` o `in_esecuzione`, log viewer chiuso | **Polling** su `GET /api/pipeline/temi/:id` |
| Nessun step attivo | Nessun polling — dato statico caricato al mount |
| Verifica completata, step sbloccati | Polling aggiorna la lista (`unlocked_steps` arriva dalla risposta verify) |

### Invalidazione cache dopo azioni

Dopo ogni azione che cambia lo stato (run, verify, skip, submit input), il hook deve:

1. Aggiornare ottimisticamente `stepStates` in memoria.
2. Schedulare un refresh immediato (non aspettare il prossimo ciclo di polling).

```typescript
const runStep = async (stepId: string, extraParams = {}) => {
  // Aggiornamento ottimistico
  setStepStates(prev => ({
    ...prev,
    [stepId]: { ...prev[stepId], status: 'in_coda', action: 'cancel' }
  }));

  const result = await pipelineOrchestratorService.runStep(temaId, stepId, extraParams);

  // Refresh immediato per allineare con MongoDB
  await refresh();

  return result;
};
```

---

## 11. `pipelineOrchestratorService`

Wrappa tutte le chiamate API admin (D4). Usato da `usePipelineOrchestration`, non direttamente dai componenti.

```typescript
// client/src/services/pipelineOrchestratorService.ts

const pipelineOrchestratorService = {
  // Lettura (usate anche dal hook read-only)
  getTema: (temaId: string) =>
    apiClient.get<{ context: PipelineContext; stepConfig: StepConfig[]; externalInputs: PipelineExternalInput[] }>(
      `/api/pipeline/temi/${temaId}`
    ),

  getStepConfig: () =>
    apiClient.get<{ steps: StepConfig[] }>('/api/pipeline/step-config'),

  // Orchestrazione
  runStep: (temaId: string, stepId: string, extraParams = {}) =>
    apiClient.post<{ execution_id: string; run_number: number }>( 
      `/api/pipeline/temi/${temaId}/steps/${stepId}/run`,
      { extra_params: extraParams }
    ),

  cancelExecution: (executionId: string, reason = '') =>
    apiClient.delete(`/api/pipeline/executions/${executionId}`, { reason }),

  verifyExecution: (executionId: string, outcome: VerificaOutcome, notes = '', feedback = '') =>
    apiClient.post<{ new_status: ExecutionStatus; unlocked_steps: string[] }>(
      `/api/pipeline/executions/${executionId}/verify`,
      { outcome, notes, feedback }
    ),

  skipStep: (temaId: string, stepId: string, reason: string) =>
    apiClient.post(`/api/pipeline/temi/${temaId}/steps/${stepId}/skip`, { reason }),

  // Input esterni
  submitExternalInput: (temaId: string, stepId: string, inputId: string, data: Record<string, unknown>) =>
    apiClient.post<{ all_required_provided: boolean }>(
      `/api/pipeline/temi/${temaId}/steps/${stepId}/inputs`,
      { input_id: inputId, data }
    ),

  // Decisioni umane
  submitTemaSelection: (ricercaId: string, payload: TemaSelectionPayload) =>
    apiClient.post<{ created_tema_id: string }>(
      `/api/pipeline/ricerche/${ricercaId}/decisions`,
      { decision_type: 'f2_to_f3_tema_selection', ...payload }
    ),

  submitContextDecision: (temaId: string, confirmed: boolean, notes = '') =>
    apiClient.post(
      `/api/pipeline/temi/${temaId}/decisions`,
      { decision_type: 'step7_context_selection', confirmed, notes }
    ),

  // System
  getSystemStatus: () =>
    apiClient.get<{ cowork_server: { active: boolean; active_executions: number } }>(
      '/api/pipeline/system/status'
    ),
};
```

---

## 12. Flussi utente principali

### Flusso A: lancio di uno step senza input esterni

```
1. Admin apre tab "Esegui" di un tema
2. Vede StepList — f3_step_3 ha action: "launch" (dipendenze ok, nessun input richiesto)
3. Clicca "Lancia"
4. Aggiornamento ottimistico: f3_step_3 → in_coda
5. API POST .../run → risponde 202 con execution_id
6. Polling ogni 5s — arriva status in_esecuzione
7. Pulsante diventa "Vedi log" + "Annulla"
8. Admin clicca "Vedi log" → si apre ExecutionLogViewer con SSE
9. Log scorrono in tempo reale
10. Arriva evento done: banner "✓ Completato" nel drawer
11. f3_step_3 → completato, step dipendenti sbloccati appaiono con action: "launch"
```

### Flusso B: step con input esterno obbligatorio (f3_step_7)

```
1. Admin vede f3_step_7 con action: "provide_input"
   Sotto: "✎ Input richiesti: Contesto/ambito target [Fornisci →]"
2. Clicca "Fornisci input" → si apre ExternalInputForm per f3_step_7
3. Compila i campi (domain, subdomain, age_range, setting, observer_profile)
4. Submit → API POST .../inputs → risponde 201 con all_required_provided: true
5. Modal si chiude, StepRow aggiorna: action diventa "decide" (pending_decision)
6. PendingDecisionBanner appare in cima
7. Admin clicca "Prendi decisione" → HumanDecisionDialog variante step7
8. Legge riepilogo contesto, spunta checkbox "Confermo"
9. Submit → API POST .../decisions → risponde 200 con step_now_launchable: true
10. Banner sparisce, f3_step_7 → action: "launch"
11. Admin clicca "Lancia" → flusso A
```

### Flusso C: verifica output

```
1. f3_step_1 completa → status in_verifica
2. StepRow mostra action: "verify" con pulsante "Verifica output"
3. Admin clicca → si apre VerificationPanel
4. Viene caricato l'output file e renderizzato con DeviceViewer
5. Admin legge il dispositivo prodotto
6. Seleziona "Approvato", aggiunge nota opzionale
7. Clicca "Conferma verifica →"
8. API POST .../verify → risponde 200 con unlocked_steps: ["f3_step_2"]
9. Modal si chiude, f3_step_1 → verificato, f3_step_2 → action: "launch"
```

### Flusso D: step fallito con retry

```
1. f3_step_3 → fallito
2. StepRow mostra badge rosso ✗, action: "relaunch"
3. Sotto: snippet del messaggio di errore
4. Admin clicca "Rilancia"
5. Aggiornamento ottimistico: f3_step_3 → in_coda (run_number: 2)
6. API POST .../run → risponde 202
7. Flusso A riprende da step 6
```

### Flusso E: skip di uno step (f3_step_8)

```
1. Admin vede f3_step_8 — f3_step_7 è completato (verdetto: trasferibile)
2. Il dispositivo è una specializzazione di dominio → step 8 non serve
3. Admin apre SecondaryActions ▾ → "Salta step"
4. Dialog di conferma: "Motivo dello skip: [_______________]"
5. Admin scrive "Specializzazione dominio clinico — non nuovo tema"
6. Conferma → API POST .../skip
7. f3_step_8 → saltato, f3_step_9 → unlocked (action: "launch")
```

---

## 13. Tipo `StepConfig` lato client

Da aggiungere a `client/src/types/pipeline.ts`:

```typescript
// Corrisponde alla struttura di pipeline-step-config.json (D1 §7)

interface StepConfig {
  id: string;
  label: string;
  phase: 'F2' | 'F3';
  output_prefix: string;
  output_path_template: string;
  inputs_pipeline?: PipelineInputDep[];
  inputs_pipeline_standard?: PipelineInputDep[];   // f3_step_9
  inputs_pipeline_skip_8?: PipelineInputDep[];      // f3_step_9
  inputs_strutturali?: string[];
  inputs_esterni?: ExternalInputConfig[];
  inputs_dispositivo_sorgente?: DeviceSourceInput;
  verifica: boolean;
  can_skip: boolean;
  skip_condition?: string;
  overrides?: string[];    // f3_step_6b
  blocks?: string[];
}

interface PipelineInputDep {
  step: string;
  role: string;
  required: boolean;
  requires_verifica?: boolean;
  note?: string;
}

interface ExternalInputConfig {
  id: string;
  label: string;
  type: 'esterno_obbligatorio' | 'esterno_facoltativo';
  schema?: string;
  file_template?: string;
  values?: string[];
  default?: string;
  note?: string;
}

interface DeviceSourceInput {
  required: boolean | string;
  description: string;
  path_template: string;
}
```

---

## 14. Note implementative per Claude Code

**Ordine consigliato di implementazione**:

1. `useIsAdmin` + `pipelineOrchestratorService` (fondamenta senza UI)
2. `usePipelineOrchestration` con solo lettura (polling, nessuna azione)
3. `StepStatusBadge` + `StepRow` read-only (solo visualizzazione stato)
4. `StepList` + `OrchestrationPanel` integrati nella tab "Esegui"
5. Azione "Lancia" (flusso A) — la più semplice
6. `ExecutionLogViewer` con SSE
7. Azione "Verifica" + `VerificationPanel`
8. `ExternalInputForm` + azione "Fornisci input"
9. `HumanDecisionDialog` + `PendingDecisionBanner`
10. Azione "Salta step"

**Non usare `localStorage`** per lo stato di orchestrazione — tutto in React state nel hook.

**Il `VerificationPanel` riusa i componenti esistenti** (`DeviceViewer`, `StressTestDashboard`): importarli e passare l'`outputFile` come sorgente dati invece del file statico dell'indice.

**L'`ExternalInputForm` è schema-driven** ma i form per f3_step_7 e f3_step_10 sono sufficientemente complessi da meritare implementazioni hardcoded per ora, con un commento `// TODO: schema-driven rendering`. Generalizzare in un secondo momento se necessario.

**SSE e cleanup**: assicurarsi che ogni `EventSource` aperto in `useExecutionLogs` venga chiuso nel cleanup dell'`useEffect` (già mostrato in §7). Altrimenti le connessioni rimangono aperte anche dopo che il drawer viene smontato.
