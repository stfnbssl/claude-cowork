# Specifiche architetturali — Orchestrazione pipeline HCAIRE

> **Destinatario**: Claude Code — leggere questo file prima di qualsiasi altro documento della cartella.
>
> **Progetto**: estensione della webapp `hcaire-blog` per rendere la pipeline F2/F3 eseguibile dall'interfaccia web, oltre che consultabile.
>
> **Contesto di partenza**: la webapp esiste già ed è descritta in `hcaire-blog/docs/produzioni-architettura.md`. Prima di leggere le specifiche qui sotto, leggere quel documento per capire lo stato attuale.

---

## Mappa dei documenti

```
D1  →  D2  →  D3  →  D4  →  D5
│       │       │       │       │
│       │       │       └───────┴── implementazione (backend poi frontend)
│       │       │
│       │       ├── D3: protocollo Redis (non implementare senza D1 e D2)
│       │       └── D6: server locale Cowork (lato opposto del canale Redis — progetto separato)
│       └── D2: MongoDB schema (non implementare senza D1)
└── D1: fondazione (leggere sempre per primo)
```

| File | Cosa definisce | Implementato in |
|---|---|---|
| `D1-pipeline-step-graph.md` | Grafo dichiarativo degli step: input, output, dipendenze, input esterni per ogni step F2/F3 | `client/public/pipeline/pipeline-step-config.json` (file di config da creare) |
| `D2-execution-state-model.md` | Schema MongoDB: 3 collection, stati lifecycle, indici, query chiave | `server/src/models/Pipeline*.ts` |
| `D3-redis-message-protocol.md` | Protocollo Redis tra backend Express e server locale Cowork: canali, messaggi, flow completo, composizione prompt (§12) | `server/src/services/messageBus.ts` |
| `D4-api-spec-express.md` | 19 endpoint Express: metodo, path, auth, request/response, status code, side effect | `server/src/routes/pipeline.ts` + `controllers/pipelineController.ts` |
| `D5-frontend-spec-orchestrazione.md` | Componenti React admin: StepList, ExternalInputForm, LogViewer SSE, VerificationPanel, hook polling | `client/src/components/pipeline/orchestration/` |
| `D6-server-locale-cowork.md` | Implementazione lato server locale: `PipelineCommandHandler` (BRPOP loop), `PromptComposer` (composizione tre blocchi), `CoworkRunner` (spawn + timeout + cancellazione) | `[server-locale]/pipeline/` — **progetto separato da `hcaire-blog`** |

---

## Ordine di lettura obbligatorio

Leggere i documenti **nell'ordine numerico D1 → D6**. Ogni documento dipende da quelli precedenti e li dà per noti. Non implementare D3 senza aver letto D1 e D2, non implementare D5 senza aver letto D4, non implementare D6 senza aver letto D3 (specialmente §12 sulla composizione del prompt).

**Nota su D6**: riguarda il server locale Cowork, che è un progetto separato da `hcaire-blog`. Leggere D6 dopo D3, ma implementarlo in parallelo con la Fase 3 di `hcaire-blog`, coordinando i due lati del canale Redis.

---

## Ordine di implementazione consigliato

### Fase 1 — Fondamenta (prerequisiti di tutto)

1. **Creare `pipeline-step-config.json`** (D1 §7) in `client/public/pipeline/`. È il file di config machine-readable che contiene il grafo degli step. Usato sia dal frontend che dal backend per valutare le condizioni di abilitazione.

2. **Creare i modelli Mongoose** (D2 §3, §4, §5): `PipelineContext`, `PipelineStepExecution`, `PipelineExternalInput`. Aggiungere gli indici definiti in D2.

3. **Seeding da file esistenti** (D2 §7): estendere `scripts/sync-pipeline.mjs` con una fase di seed MongoDB. Idempotente — non sovrascrive documenti già presenti.

### Fase 2 — Backend read-only

4. **Registrare le route** `server/src/routes/pipeline.ts` + `app.use('/api/pipeline', ...)` in `index.ts`.

5. **Implementare gli endpoint GET** (D4 §2): `/api/pipeline/index`, `/api/pipeline/temi/:id`, `/api/pipeline/ricerche/:id`, `/api/pipeline/step-config`. Questi sostituiscono il fetch del file statico.

6. **Aggiornare `pipelineService.ts`** nel client (D4 §10): cambiare `fetchPipelineIndex()` per puntare a `/api/pipeline/index`. Nessuna altra modifica al frontend esistente.

7. **Verificare** che le pagine esistenti (`PipelineMap`, `DeviceOverview`, ecc.) continuino a funzionare identicamente — i dati ora vengono da MongoDB ma la struttura è la stessa.

### Fase 3 — Backend orchestrazione (`hcaire-blog`)

8. **Implementare `PipelineMessageBus`** (D3 §9) in `server/src/services/messageBus.ts`. Usare `ioredis`. Testare `ping()` contro il server locale Cowork.

9. **Implementare `evaluateStepEnablement`** (D4 §9) in `server/src/services/pipelineService.ts`. È la funzione critica — testarla in isolamento con casi da D1.

10. **Implementare gli endpoint di orchestrazione** (D4 §3): `POST .../run`, `DELETE .../executions/:id`, `POST .../executions/:id/verify`, `POST .../steps/:id/skip`.

11. **Implementare gli endpoint input esterni** (D4 §4) e **decisioni umane** (D4 §5).

12. **Implementare SSE `/api/pipeline/executions/:id/logs`** (D4 §6).

### Fase 3 (parallela) — Server locale Cowork

13. **Leggere D6 integralmente** prima di toccare qualsiasi file del server locale.

14. **Creare `pipeline/pipeline-constants.js`** (D6 §1): `STEP_FOLDER_MAP` e `STEP_CLAUDE_FILE_MAP`. Verificare che i path dei CLAUDE.md corrispondano a quelli reali sul filesystem.

15. **Creare `pipeline/PromptComposer.js`** (D6 §3): composizione tre blocchi, pulizia CLAUDE.md, gestione `f3_step_10` MICRO CASI. Testare con lo script isolato in D6 §7 prima di integrare.

16. **Creare `pipeline/CoworkRunner.js`** (D6 §4): spawn Cowork, readline capture, timeout, cancellazione. **Adattare `_buildCoworkArgs()`** (D6 §4.5) ai pattern già usati dal server locale per altri flussi — questo è il punto da verificare con il codice esistente.

17. **Creare `pipeline/PipelineCommandHandler.js`** (D6 §2): BRPOP loop, deduplicazione via `activeExecutions`, dispatch. Registrarlo nell'entry point del server locale senza modificare i handler esistenti.

18. **Eseguire la pre-flight checklist** (D6 §6): verificare Redis raggiungibile, canali corretti, path CLAUDE.md esistenti, output dir scrivibile, `ping` funzionante end-to-end.

### Fase 4 — Frontend orchestrazione

13. **`useIsAdmin`** + **`pipelineOrchestratorService`** (D5 §1.2, §11).

14. **`usePipelineOrchestration`** (D5 §2) — hook principale con polling.

15. **`StepStatusBadge`** + **`StepRow`** (D5 §4) — visualizzazione stato, poi azioni.

16. **`StepList`** + **`OrchestrationPanel`** + integrazione tab "Esegui" in `DeviceOverview` (D5 §3, §4.1).

17. **`ExecutionLogViewer`** con `useExecutionLogs` SSE (D5 §7).

18. **`VerificationPanel`** (D5 §8).

19. **`ExternalInputForm`** (D5 §5).

20. **`HumanDecisionDialog`** + **`PendingDecisionBanner`** (D5 §6, §9).

---

## Decisioni architetturali già prese — non ridiscutere

| Decisione | Motivazione | Documento |
|---|---|---|
| MongoDB (non Neo4j) per lo stato di esecuzione | Il grafo delle dipendenze è statico e piccolo — non giustifica un graph DB | D2 intro |
| Redis List per comandi, Pub/Sub per eventi | List = at-most-once processing; Pub/Sub = streaming senza polling | D3 §1 |
| File statici degli artefatti rimangono in `client/public/pipeline/` | Solo lo stato (MongoDB) cambia, non i file — zero breaking change per il frontend esistente | D4 §1.4 |
| Endpoint GET pubblici, endpoint di scrittura admin-only | Le produzioni sono contenuti del sito, non dati privati | D4 §1.1 |
| `202 Accepted` per tutte le azioni asincrone | Nessuna richiesta HTTP lunga durante esecuzioni Cowork | D4 §1.3 |
| Polling autospento quando nessun step attivo | Evita chiamate inutili; si riattiva automaticamente a ogni azione | D5 §10 |
| Layer admin come overlay, non nuove pagine | Zero rischio di rompere l'esperienza read-only esistente | D5 §1 |

---

## Punti critici — prestare attenzione speciale

**`evaluateStepEnablement`** (D4 §9): gestisce la biforcazione `f3_step_3_or_6c` — quando step 6c è presente, sostituisce step 3 come input per gli step successivi. Sbagliare questa logica blocca la pipeline.

**Override step 6b** (D1 §1, variante 6b): l'output di `f3_step_6b` sovrascrive `operative_proxies`, `observability_requirements`, `non_classifiability_rules` nel dispositivo finale. Il motore di esecuzione deve aggiornare `canonical_device` del context dopo che 6b è verificato.

**Aggiornamento atomico `pipeline_contexts`** (D2 §9): usare sempre `findOneAndUpdate` con `$set` puntuale su `step_states.<stepId>`. Non fare read-modify-write: race condition garantita durante esecuzioni parallele.

**SSE cleanup** (D5 §7): ogni `EventSource` aperto da `useExecutionLogs` deve essere chiuso nel cleanup dell'`useEffect`. Dimenticarlo causa connessioni zombie.

**Seeding idempotente** (D2 §7): il seed non deve sovrascrivere documenti già presenti in MongoDB. Usare `updateOne` con `upsert: false` o verificare l'esistenza prima dell'insert.

**`attende_decisione` vs `attende_input`** (D2 §2.2): stati semanticamente distinti. `attende_input` = form da compilare, sistema procede da solo. `attende_decisione` = scelta strutturale, richiede conferma esplicita. Non unificarli.

**`_buildCoworkArgs()` nel server locale** (D6 §4.5): il metodo che costruisce gli argomenti per lo spawn di Cowork è marcato come placeholder — il pattern dipende da come il server locale lancia già Cowork in altri flussi. Prima di implementare, ispezionare i handler esistenti e replicare lo stesso pattern. Non inventare nuovi argomenti CLI.

---

## File esistenti da modificare (e come)

| File esistente | Modifica | Dettaglio |
|---|---|---|
| `scripts/sync-pipeline.mjs` | Aggiungere fase seeding MongoDB | D2 §7 |
| `client/src/services/pipelineService.ts` | `fetchPipelineIndex()` → chiama `/api/pipeline/index` | D4 §10 |
| `server/src/index.ts` | Aggiungere `app.use('/api/pipeline', pipelineRoutes)` | D4 §8 |
| `client/src/pages/.../SviluppoBambinoPipelineDeviceOverview.tsx` | Aggiungere tab "Esegui" condizionale a `useIsAdmin()` | D5 §3 |
| `client/src/types/pipeline.ts` | Aggiungere `StepConfig`, `ExternalInputConfig`, `PipelineContext`, `PipelineStepExecution`, `PipelineExternalInput`, `ExecutionStatus` | D2 §3-5, D5 §13 |

---

## Infrastruttura esistente da non toccare

- **Server locale Telegram/Redis/Cowork**: funziona già per altri flussi. Aggiungere solo il handler `PipelineCommandHandler` (D6 §2) senza modificare i flussi esistenti. Tutta la logica pipeline va in `pipeline/` come sotto-cartella del server locale.
- **Autenticazione Clerk**: già presente con ruolo `admin`. Usare il middleware esistente in `server/src/middleware/auth.ts`.
- **Componenti di visualizzazione esistenti**: `DeviceViewer`, `StressTestDashboard`, `CorrectionsLog`, `ProcessNarrative`, `DeviceLineage` — non toccarli. Il `VerificationPanel` (D5 §8) li importa e li riusa.
- **`sync-pipeline.mjs`**: non riscriverlo, solo estenderlo con il seeding.
