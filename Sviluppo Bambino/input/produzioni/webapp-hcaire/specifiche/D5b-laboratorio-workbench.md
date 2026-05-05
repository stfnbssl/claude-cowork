# D5b — Frontend spec — Laboratorio Workbench (redesign UX)

> **Destinatario**: Claude Code — leggere D1, D2, D3, D4 prima di questo documento. Conoscere le sezioni di D5 ancora valide (§1.2, §1.3, §2, §10, §11, §13).
>
> **Cosa sostituisce**: questo documento **rimpiazza integralmente** D5 §3 (integrazione tab "Esegui"), §4 (`StepList`/`StepRow`), §5 (`ExternalInputForm` come modal), §6 (`HumanDecisionDialog` come modal), §7 (`ExecutionLogViewer` come drawer), §8 (`VerificationPanel` come modal), §9 (`PendingDecisionBanner`).
>
> **Cosa preserva**: il data layer di D5 resta invariato. Nello specifico:
>
> - D5 §1.2 — `useIsAdmin`
> - D5 §2 — `usePipelineOrchestration` (hook + `EnrichedStepState` + `StepAction`)
> - D5 §10 — strategia di polling + SSE
> - D5 §11 — `pipelineOrchestratorService`
> - D5 §13 — tipi `StepConfig`, ecc.
>
> La proposta cambia la composizione visuale e l'ergonomia interattiva, e introduce un **modello a entità** che rispecchia la natura della pipeline (vedi §1.4). Le API e gli schemi MongoDB di D2/D4 vanno rivisti per riflettere il nuovo modello (vedi note in §1.4).

---

## Storia delle revisioni

- **r1** — Workbench focalizzato + timeline + tre zone INPUT/ESEC/OUTPUT (sostituisce le modali sparpagliate di D5).
- **r2** (corrente) — Modello a tre entità: **Archivio Temi** (esterno alla pipeline), **Tema/RicercaF2** (entità unica con stati di vita, 1-1), **DispositivoF3 contestualizzato** (relazione 1-N con il tema). L'attuale `f2_step_1` esce dalla pipeline e diventa attività dell'archivio. La pipeline F2 inizia da `f2_step_2`. La pipeline F3 viene eseguita una volta per ogni contestualizzazione.

---

## 0. Sintesi esecutiva

L'attuale specifica frontend tratta l'orchestrazione come una **lista di righe con popup**: ogni interazione (fornire input, vedere log, verificare, decidere) apre un componente diverso (modal, drawer, banner). L'utente è costretto a un continuo "apri / chiudi / cerca dove sono finito". Il risultato è frammentazione cognitiva — esattamente l'opposto di ciò che serve a guidare un ricercatore in una pipeline metodologicamente densa come F2/F3 di HCAIRE.

Questa spec sostituisce la lista-con-modali con un **Laboratorio**: due viste dedicate (per il **Tema** in elaborazione F2, e per il singolo **Dispositivo** F3 contestualizzato) che condividono lo stesso **Workbench focalizzato sullo step corrente**. Il workbench mostra **simultaneamente e sempre nella stessa pagina**:

1. **Cosa entra** nello step (dipendenze pipeline, input strutturali, input esterni del ricercatore)
2. **Lo stato di esecuzione** (lancia, log live, annulla)
3. **Cosa esce** dallo step (output renderizzato, verifica, eventuale decisione)

Una **timeline verticale** sulla sinistra mostra la pipeline corrente (F2 nella vista Tema, F3 nella vista Dispositivo) come percorso lineare, con badge di stato per ciascun tappo, e funge da navigatore persistente. La timeline non è un elenco di azioni: è la mappa del viaggio. L'azione è sempre nel workbench.

Il principio guida è: **una sola pagina, una sola nozione di "dove sono", tre zone visibili in parallelo.** Niente modali per il flusso normale. Le modali sopravvivono solo per atti rari e fortemente intenzionali (conferma skip, conferma decisione strutturale, creazione di una nuova contestualizzazione F3).

Sopra al Laboratorio sta l'**Archivio dei temi**: un'entità separata, alimentata dal ricercatore (eventualmente con assistenza Cowork — fuori scope di questo documento), da cui un tema può essere **promosso** a oggetto di RicercaF2. Il Laboratorio assume l'archivio come *dato esistente*: ne consuma i metadati, ne mostra il riferimento, ma non ne specifica la gestione interna.

---

## 1. Principi di design

### 1.1 Quattro principi non-negoziabili

**P1 — Coabitazione di input, esecuzione, output.** In ogni momento il ricercatore deve poter ispezionare i dati che alimentano lo step e l'output prodotto, senza navigare via dalla schermata. La pipeline HCAIRE è un metodo che produce dispositivi epistemici: l'unica cosa che conta è la trasparenza tra ciò che entra e ciò che esce.

**P2 — Linearità con libertà.** Il default è seguire la pipeline in ordine. Ma il ricercatore deve poter saltare a qualsiasi step già completato per ispezionarlo, e tornare al "fronte" attivo con un click solo. Il sistema **suggerisce sempre il prossimo passo**; non lo impone.

**P3 — Niente modali nel flusso normale.** Lanciare uno step, leggere log, verificare un output, fornire input esterni: tutte queste azioni avvengono **in pagina**, nel workbench. Le modali compaiono solo per: (a) conferma di skip con motivazione, (b) decisione umana strutturale (variante 1: selezione tema F2→F3; variante 2: conferma contesto F3 step 7).

**P4 — Stato persistente leggibile.** Il workbench non è una shell che si svuota tra step: il pannello di output di uno step verificato resta accessibile (in modalità "consultazione") quando l'utente ci ritorna dalla timeline. Tutto è ispezionabile a posteriori.

### 1.2 Cosa cambia rispetto a D5

| Aspetto | D5 originale | D5b |
|---|---|---|
| Modello entità | Implicito: tema F3 monolitico con riferimento a ricerca F2 | Esplicito a tre entità: Archivio temi → Tema/RicercaF2 → N DispositiviF3 (vedi §1.4) |
| Forma della tab "Esegui" | Lista di righe (`StepList` di `StepRow`) | Vista "Laboratorio" con timeline + workbench |
| Form input esterni | Modal aperta da `StepRow` | Pannello inline nella zona INPUT del workbench |
| Log di esecuzione | Drawer laterale | Pannello inline nella zona ESECUZIONE del workbench |
| Verifica output | Modal pieno schermo | Pannello inline nella zona OUTPUT del workbench |
| Decisione umana strutturale | Modal `HumanDecisionDialog` | Modal (preservata: è atto deliberato, raro) |
| Banner decisione pendente | Banner sticky in cima | Banner sticky in cima al Laboratorio (preservato) |
| Skip step | Voce nel menu `▾` | Pulsante secondario nello header dello step + dialog di conferma |
| Step `f2_step_1` (ricerca temi) | Primo step della pipeline F2 | **Rimosso dalla pipeline** — confluisce nell'archivio temi (vedi §1.4) |
| Pipeline F3 | Una per tema | Una **per contestualizzazione** del tema (relazione 1-N) |

### 1.3 Layout del Laboratorio

Una sola pagina, tre regioni:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  [Top Bar — sempre visibile]                                                 │
│  HCAIRE Laboratorio · Tema "pointing-clinico" · F3 (3 verificati / 10)       │
│  ● Cowork: attivo  ·  Polling: on  ·  [Vai al fronte attivo →]               │
├──────────────────────────────────────────────────────────────────────────────┤
│ [Banner decisione pendente — solo se presente]                               │
├──────────────────┬───────────────────────────────────────────────────────────┤
│                  │                                                           │
│   TIMELINE       │                  WORKBENCH                                │
│   (verticale)    │                  (focus su uno step)                      │
│                  │                                                           │
│   F2                                                                         │
│   ✓ Discovery    │   [Header step + azione primaria]                         │
│   ✓ Rilevanza    │   ─────────────────────────────────────────────────       │
│   ✓ Nodi tras.   │                                                           │
│   ✓ Verifica     │   ┌── INPUT ─────┬── ESEC. ─────┬── OUTPUT ────────┐     │
│   ✓ Matrice      │   │              │              │                  │     │
│   ✓ CE proto.    │   │ Dipendenze   │ Stato + Log  │ JSON renderizzato│     │
│   ✓ Out family   │   │ Strutturali  │ Lancia/      │ + verifica       │     │
│   ✓ Output-tipo  │   │ Esterni      │ Annulla/     │                  │     │
│                  │   │              │ Scaric.      │                  │     │
│   ?? F2→F3       │   └──────────────┴──────────────┴──────────────────┘     │
│                  │                                                           │
│   F3                                                                         │
│   ✓ Lettura      │   [Footer step]                                           │
│   ✓ Stress       │   [← step precedente]              [step successivo →]   │
│   ▶ Correzione   │                                                           │
│   · Indistin.    │                                                           │
│   · Audit        │                                                           │
│   · Stab. proxy  │                                                           │
│   · Proxy oper.  │                                                           │
│   · Trasferib.   │                                                           │
│   · Adattamento  │                                                           │
│   · Disp. comp.  │                                                           │
│   · Stress disp. │                                                           │
└──────────────────┴───────────────────────────────────────────────────────────┘
```

- **Larghezza timeline**: ~280px desktop, collassabile a icone (~64px) per dare più spazio al workbench.
- **Workbench**: occupa il resto della pagina. Scroll interno indipendente dalla timeline.
- **Tre colonne INPUT/ESEC./OUTPUT**: in desktop sono affiancate; sotto la breakpoint `lg` collassano in tre **tab orizzontali** ma con la stessa identità (`Input`, `Esecuzione`, `Output`).
- **Top Bar e Banner**: sticky in cima alla viewport. Il resto scrolla.

### 1.4 Modello a entità del Laboratorio

La pipeline HCAIRE non è un singolo tubo lineare F2→F3. È un grafo di **tre entità distinte** legate da relazioni precise:

```
┌─────────────────────────────┐
│   ARCHIVIO TEMI             │   (gestito fuori dal Laboratorio)
│   collezione di candidati   │
│   in evoluzione libera      │
└─────────────┬───────────────┘
              │ promozione (atto deliberato)
              │ relazione 1-1
              ▼
┌─────────────────────────────┐
│   TEMA / RICERCA F2         │   (vista "Tema" del Laboratorio)
│   pipeline F2 strutturale   │   stati di vita: vedi §1.4.2
│   = ricerca di un tema      │
└─────────────┬───────────────┘
              │ contestualizzazione (atto deliberato, ripetibile)
              │ relazione 1-N
              ▼
┌─────────────────────────────┐    ┌─────────────────────────────┐
│   DISPOSITIVO F3            │    │   DISPOSITIVO F3            │   ...
│   pipeline F3 contesto X    │    │   pipeline F3 contesto Y    │
└─────────────────────────────┘    └─────────────────────────────┘
   (vista "Dispositivo")              (vista "Dispositivo")
```

#### 1.4.1 Tre entità

**1. Tema candidato (Archivio).** Un'entità anagrafica gestita fuori dal Laboratorio. Contiene metadati di evoluzione libera: titolo, descrizione, fonti, note del ricercatore, asse dominante presunto. La gestione interna dell'archivio (ricerca, scoperta-Cowork, indicizzazione) è fuori dallo scope di questo documento e sarà specificata separatamente. Questo documento assume che l'archivio esista e che ogni Tema/RicercaF2 nel Laboratorio abbia un riferimento al candidato di archivio da cui è stato promosso (`tema_candidato_id`).

**2. Tema (= RicercaF2).** Identità unica con un singolo `tema_id` (= slug del tema candidato promosso). Non sono due entità: sono due **stati di vita** della stessa cosa. Quando un tema viene promosso dall'archivio, *il tema candidato diventa il soggetto* di una pipeline F2. Lo stato attraversa il ciclo:

```
[bozza] → [maturo] → [promosso] → [f2_in_corso] → [f2_verificata] → [f3_in_corso (1+ contesti)]
                                                          │
                                                          └→ [parcheggiato] / [abbandonato] / [archiviato]
```

Il primo step della pipeline F2 nel Laboratorio è **`f2_step_2`** (rilevanza strutturale). L'attuale `f2_step_1` (ricerca temi) **non fa più parte della pipeline**: la sua funzione è confluita nell'archivio.

**3. Dispositivo F3 (contestualizzazione).** Una pipeline F3 completa eseguita per una specifica scelta di contesto/ambito. Identità: `(tema_id, contesto_id)`. Il `contesto_id` è uno slug derivato dal contesto target (es. `clinico-neurosviluppo-9-24-mesi`, `educativo-nido`). Ogni dispositivo è autonomo nel ciclo di vita: lanciato indipendentemente, verificato indipendentemente, conservato come oggetto distinto. Più dispositivi-fratelli possono coesistere, in stati di avanzamento diversi.

#### 1.4.2 Stati di vita del Tema

| Stato | Significato | Visibilità Archivio | Visibilità Laboratorio |
|---|---|---|---|
| `bozza` | Candidato in raccolta, metadati incompleti | sì | no |
| `maturo` | Candidato pronto per la promozione (metadati minimi presenti) | sì | no |
| `promosso` | Promosso dall'utente — pipeline F2 non ancora avviata | sì (badge "promosso") | sì (`f2_in_corso` con 0 step eseguiti) |
| `f2_in_corso` | Pipeline F2 in esecuzione | sì (badge "in elaborazione") | sì |
| `f2_verificata` | Tutti gli step F2 verificati (incluso `f2_step_6`) | sì (badge "F2 ok") | sì |
| `parcheggiato` | F2 sospesa volontariamente | sì (badge "parcheggiato") | sì (read-only) |
| `abbandonato` | F2 abbandonata | sì (badge "abbandonato") | no |
| `archiviato` | Tema concluso e archiviato | sì (filtro archivio) | sì (read-only) |

I dispositivi F3 hanno un proprio stato di vita più semplice: `non_avviato | in_corso | verificato | parcheggiato | abbandonato | archiviato`, calcolato sull'avanzamento della loro pipeline F3.

#### 1.4.3 Implicazioni sul backend

> ⚠ Questa spec frontend richiede un aggiornamento dei modelli MongoDB e degli endpoint definiti in D2 e D4. La revisione backend è fuori scope di questo documento, ma queste sono le richieste minime che la UI ha bisogno di soddisfare:

- Una collezione `temi` (al posto della collezione "tema F3" implicita di D2) con campo `stato` che attraversa il ciclo §1.4.2 e riferimento `tema_candidato_id` all'archivio.
- Una collezione `dispositivi_f3` distinta, ciascuno con `tema_id` + `contesto_id` + il proprio `step_states` per la pipeline F3.
- La collezione `pipeline_step_executions` di D2 §4 deve riferirsi a un'identità di pipeline che includa l'`entity_kind` (`tema` per gli step F2, `dispositivo` per gli step F3) e l'`entity_id` corrispondente.
- Endpoint nuovi richiesti dalla UI:
  - `GET /api/pipeline/temi/:temaId/dispositivi` → elenco dispositivi figli con stato sintetico
  - `POST /api/pipeline/temi/:temaId/dispositivi` → crea un dispositivo F3 (richiede `contesto_id` + label)
  - `GET /api/pipeline/dispositivi/:dispositivoId` → context + stepConfig (solo F3) + externalInputs del dispositivo
  - Le rotte esistenti `GET /api/pipeline/temi/:id` continuano a esistere ma ora restituiscono *solo* i dati F2 del tema; il `step_states` contiene solo step F2
- Il file `pipeline-step-config.json` (D1 §7) va rivisto per:
  - Rimuovere `f2_step_1` dall'array degli step **eseguibili dal Laboratorio**, oppure marcarlo con un flag `excluded_from_pipeline_ui: true` (mantenibile come record storico per produzioni esistenti)
  - Aggiungere alla configurazione di `f3_step_1` la nota che il `tema_id` ora è implicito (ereditato dal `dispositivoId` della pipeline F3), e che il `contesto_id` è anch'esso un'identità di pipeline, non un input esterno separato
  - L'attuale `f3_step_7` continua a richiedere un input esterno "contesto" come dato strutturato (dominio, sottodominio, fascia d'età, setting, profilo osservatore), ma il `contesto_id` slug viene fissato all'atto di creazione del dispositivo (vedi flusso F in §12.6). Il form `f3_step_7` arricchisce il contesto con i metadati strutturati.

Questo documento procede assumendo che il backend si adegui. Dove un endpoint nuovo è richiesto, lo segnaleremo con il prefisso ⚠ NEW BACKEND.

---

## 2. Routing e integrazione nella webapp

### 2.1 Nuove route

| Route | Componente di pagina | Quando |
|---|---|---|
| `/laboratorio` | `LaboratorioIndexPage` | Index dei temi e dispositivi attivi (vedi §10) |
| `/laboratorio/temi/:temaId` | `LaboratorioTemaPage` | Vista di un tema in elaborazione: pipeline F2 + sezione contestualizzazioni |
| `/laboratorio/temi/:temaId/step/:stepId` | `LaboratorioTemaPage` | Deep-link a uno step F2 specifico del tema |
| `/laboratorio/temi/:temaId/dispositivi/:contestoId` | `LaboratorioDispositivoPage` | Vista di un dispositivo F3 contestualizzato: pipeline F3 |
| `/laboratorio/temi/:temaId/dispositivi/:contestoId/step/:stepId` | `LaboratorioDispositivoPage` | Deep-link a uno step F3 specifico del dispositivo |

L'archivio dei temi avrà le proprie route (`/archivio/...`), specificate in un documento separato. Quando l'utente promuove un tema dall'archivio, la promozione redirige a `/laboratorio/temi/:temaId`.

Le route esistenti (`/sviluppo-bambino/...`, `/produzioni/...`, ecc.) rimangono **invariate** e visibili a tutti. Il Laboratorio è una vista parallela accessibile solo agli admin.

### 2.2 Punti di accesso al Laboratorio

- Da `SviluppoBambinoPipelineMap`, su ogni card: il pulsante **"Apri laboratorio"** (visibile solo se `useIsAdmin()`) porta al tema o al dispositivo corrispondente.
- Da `SviluppoBambinoPipelineDeviceOverview`: la tab "Esegui" — invece di mostrare il vecchio `OrchestrationPanel` — diventa un link diretto al Laboratorio appropriato. Se l'overview è di un dispositivo F3, linka al `LaboratorioDispositivoPage` corrispondente; se è di un tema in F2, linka al `LaboratorioTemaPage`. Una banda informativa spiega: *"Il laboratorio si apre in vista dedicata. [Apri laboratorio →]"*. Questa scelta evita di duplicare il workbench dentro una tab di un'altra pagina.
- Globalmente: voce di navigazione admin **"Laboratorio"** che porta all'index (§10).
- Dall'archivio (futuro): il pulsante "Promuovi a ricerca F2" su un tema candidato `maturo` reindirizza al `LaboratorioTemaPage` del nuovo tema promosso.

### 2.3 Sostituzione della tab "Esegui"

Il tab "Esegui" della `SviluppoBambinoPipelineDeviceOverview` non monta più componenti di orchestrazione. Diventa un placeholder con un solo CTA che linka al Laboratorio appropriato. Motivo: un tab dentro una pagina dettaglio non ha lo spazio orizzontale necessario per un workbench a tre colonne.

---

## 3. Viste del Laboratorio: `LaboratorioTemaPage` e `LaboratorioDispositivoPage`

Il Laboratorio ha due varianti di pagina, simmetriche per UX ma distinte per dominio dati:

- **`LaboratorioTemaPage`**: lavoro sulla pipeline F2 di un tema. Mostra timeline F2 + sezione contestualizzazioni F3.
- **`LaboratorioDispositivoPage`**: lavoro sulla pipeline F3 di un dispositivo contestualizzato. Mostra timeline F3 + breadcrumb al tema madre.

Le due pagine condividono i sottocomponenti (`TopBar`, `TimelineRail`, `Workbench`, ecc.), passati con prop differenti. Per evitare duplicazione, viene introdotto un componente comune `LaboratorioShell` che orchestra il layout; `LaboratorioTemaPage` e `LaboratorioDispositivoPage` lo configurano con i dati pertinenti.

### 3.1 `LaboratorioShell` (componente comune)

```typescript
// client/src/components/laboratorio/LaboratorioShell.tsx

interface LaboratorioShellProps {
  entity: LaboratorioEntity;
  orchestration: UsePipelineOrchestrationResult;
  // estensione opzionale del workbench (es. sezione contestualizzazioni nella vista Tema)
  workbenchTrailing?: React.ReactNode;
  // breadcrumb opzionale (es. nella vista Dispositivo: "← Tema: pointing-clinico")
  topBarBreadcrumb?: React.ReactNode;
}

type LaboratorioEntity =
  | { kind: 'tema'; temaId: string; label: string; stato: TemaStato; temaCandidatoId: string }
  | { kind: 'dispositivo'; temaId: string; contestoId: string; temaLabel: string; contestoLabel: string };

type TemaStato =
  | 'promosso' | 'f2_in_corso' | 'f2_verificata'
  | 'parcheggiato' | 'abbandonato' | 'archiviato';
```

Responsabilità: monta `TopBar`, eventuale `PendingDecisionBanner`, `TimelineRail`, `Workbench`. **Non** chiama `usePipelineOrchestration` direttamente — riceve l'istanza già montata dal componente di pagina.

### 3.2 `LaboratorioTemaPage`

```typescript
// client/src/pages/LaboratorioTemaPage.tsx

interface LaboratorioTemaPageRouteParams {
  temaId: string;
  stepId?: string;        // deep-link
}
```

Responsabilità:

1. Risolve `temaId` dal route.
2. Monta `usePipelineOrchestration({ temaId, scope: 'F2' })` per ottenere il context F2 e i suoi step.
3. Carica anche la lista dei dispositivi figli con `useDispositiviTema(temaId)` (⚠ NEW BACKEND: `GET /api/pipeline/temi/:temaId/dispositivi`).
4. Renderizza `LaboratorioShell` con:
   - `entity = { kind: 'tema', temaId, ... }`
   - `workbenchTrailing = <ContestualizzazioniSection dispositivi={...} onCreate={...} />` — visibile **solo** quando `tema.stato === 'f2_verificata'` (vedi §6.7).
5. Gestisce l'apertura della modal `NuovaContestualizzazioneDialog` (§9.4) per la creazione di nuovi dispositivi.

La timeline F2 mostra **solo** gli step F2 (da `f2_step_2` a `f2_step_6`, con sub-step canonici 2a e 4b). Lo step `f2_step_1` non appare.

### 3.3 `LaboratorioDispositivoPage`

```typescript
// client/src/pages/LaboratorioDispositivoPage.tsx

interface LaboratorioDispositivoPageRouteParams {
  temaId: string;
  contestoId: string;
  stepId?: string;        // deep-link
}
```

Responsabilità:

1. Risolve `temaId` + `contestoId` dal route.
2. Monta `usePipelineOrchestration({ dispositivoId: { temaId, contestoId }, scope: 'F3' })` per ottenere il context F3 di quel dispositivo (⚠ NEW BACKEND: `GET /api/pipeline/dispositivi/:dispositivoId`).
3. Carica i metadati del tema madre (`GET /api/pipeline/temi/:temaId`) per il breadcrumb e i riferimenti read-only.
4. Renderizza `LaboratorioShell` con:
   - `entity = { kind: 'dispositivo', temaId, contestoId, ... }`
   - `topBarBreadcrumb = <Breadcrumb to=tema />`
   - `workbenchTrailing = null` (i dispositivi non hanno figli)

La timeline F3 mostra **solo** gli step F3 (da `f3_step_1` a `f3_step_10`, con sub-step 6b/6c). Una sezione collassata in cima alla timeline ("Pre-requisiti F2 ✓") rinvia in sola lettura agli step F2 verificati del tema, ognuno cliccabile per ispezione (apre il workbench dello step F2 in modalità read-only, in nuova tab oppure overlay leggero).

### 3.4 Stato locale (comune a entrambe)

```typescript
interface LaboratorioShellState {
  focusedStepId: string;            // step attualmente nel workbench (F2 o F3)
  focusMode: 'auto' | 'manual';
  timelineCollapsed: boolean;       // persistito in localStorage
  workbenchActiveSection: 'input' | 'esecuzione' | 'output';  // solo layout mobile
}
```

`focusMode === 'auto'` significa che `focusedStepId` viene **ricalcolato a ogni refresh dello stato** e segue il "fronte attivo" della pipeline corrente (F2 nella vista Tema, F3 nella vista Dispositivo). Quando l'utente clicca su uno step nella timeline, `focusMode` passa a `'manual'`.

### 3.5 Algoritmo del "fronte attivo"

Dato `stepStates` (D5 §2) — limitato agli step della pipeline visualizzata —, il fronte attivo è il primo step nella seguente priorità:

1. Step in stato `attende_decisione` (decisione umana che blocca).
2. Step in stato `in_esecuzione`.
3. Step in stato `in_coda`.
4. Step in stato `in_verifica`.
5. Step in stato `attende_input` con `is_launchable === false`.
6. Step in stato `richiede_correzione` o `fallito`.
7. Primo step con `action === 'launch'` (lanciabile, in attesa di azione admin).
8. Se nessuno: ultimo step `verificato` o `completato` (la pipeline è ferma o conclusa).

Casi speciali per `LaboratorioTemaPage`:

- Se tutti gli step F2 sono `verificato` e *non esistono dispositivi figli*: il fronte è virtualmente la sezione "Contestualizzazioni" (§6.7) — la `TopBar` mostra il pulsante "+ Crea prima contestualizzazione" come azione primaria, e il workbench scorre alla sezione trailing.
- Se `tema.stato === 'parcheggiato'` o `archiviato`: pipeline read-only, nessun fronte attivo, banner "Tema in stato X" con CTA "Riprendi" (riporta a `f2_in_corso`).

### 3.6 Persistenza UX

In `localStorage`, sotto la chiave `hcaire.laboratorio.preferences.v2`:

```json
{
  "timelineCollapsed": false,
  "lastFocusedByEntity": {
    "tema:pointing-clinico": "f2_step_4",
    "dispositivo:pointing-clinico:clinico-neurosviluppo-9-24-mesi": "f3_step_3"
  }
}
```

La chiave d'entità è composta da `kind:id1[:id2]`. Versione bumped a `v2` per evitare collisioni con il vecchio storage di r1. Quando l'utente clicca "Torna al fronte attivo →", ripuliamo l'entry.

---

## 4. `TopBar`

### 4.1 Layout — vista Tema

```
┌────────────────────────────────────────────────────────────────────────────┐
│  ⚗ HCAIRE Laboratorio  ·  Tema: pointing-clinico  [stato: f2_in_corso]      │
│  F2 · 4 verificati / 7  ·  ●⚡ Cowork attivo  ·  [Torna al fronte ↩]       │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Layout — vista Dispositivo

Il breadcrumb verso il tema madre sostituisce parte della prima riga; il contesto del dispositivo prende la seconda parte.

```
┌────────────────────────────────────────────────────────────────────────────┐
│  ⚗ HCAIRE Lab  ·  ← Tema: pointing-clinico  ·  Dispositivo: clinico-9-24m  │
│  F3 · 5 verificati / 10  ·  ●⚡ Cowork attivo  ·  [Torna al fronte ↩]     │
└────────────────────────────────────────────────────────────────────────────┘
```

Il "← Tema: ..." è un link a `/laboratorio/temi/:temaId`.

### 4.3 Props

```typescript
interface TopBarProps {
  entity: LaboratorioEntity;        // vedi §3.1
  phase: 'F2' | 'F3';                // derivata da entity.kind
  progress: { verified: number; total: number };  // sulla pipeline corrente
  systemStatus: 'attivo' | 'non_raggiungibile' | 'sconosciuto';
  pollingActive: boolean;
  focusMode: 'auto' | 'manual';
  onReturnToFront: () => void;        // visibile solo se focusMode === 'manual'
  onToggleTimeline: () => void;
  breadcrumb?: React.ReactNode;       // valorizzato solo nella vista Dispositivo
}
```

### 4.4 Comportamento

- Il pill "Cowork attivo / non raggiungibile" è cliccabile: apre un piccolo popover con last-ping, errori recenti, link a `GET /api/pipeline/system/status`.
- "Torna al fronte attivo" appare solo se `focusMode === 'manual'`. Quando l'utente lo clicca: `focusMode = 'auto'`, `focusedStepId = computeActiveFront()`, e (se la timeline è collassata) viene espansa con animazione.
- Nella vista Tema, il pill `[stato: ...]` è cliccabile per stati `f2_verificata` (mostra menu "Parcheggia tema" / "Archivia tema") e per stati terminali (mostra "Riprendi tema").
- Nella vista Dispositivo, il breadcrumb usa `<Link>` di react-router; click ordinario naviga, cmd/ctrl-click apre in nuova tab.

---

## 5. `TimelineRail`

La timeline ha due **varianti** in funzione della pagina che la ospita: F2-only nella vista Tema, F3-only nella vista Dispositivo. Il componente è lo stesso, configurato dalle prop.

### 5.1 Modello visivo — vista Tema (F2-only)

```
TEMA pointing-clinico                     stato: f2_in_corso

  ●  f2_step_2 — Rilevanza              ✓
  │
  ●  f2_step_2a — Nodi trasversali      ✓
  │
  ●  f2_step_3 — Verifica               ✓
  │
  ●  f2_step_4 — Micro-matrice          ✓
  │
  ●  f2_step_4b — CE prototipica       ▶ ⟳   ← step in focus
  │
  ○  f2_step_5 — Output family
  │
  ○  f2_step_6 — Output-tipo vuoto
  │
  ─── F2 verificata ─────────────────
  Contestualizzazioni F3:
  (nessuna ancora — disponibile dopo verifica F2)
```

Quando `f2_step_6` è `verificato`, la timeline mostra in coda un riepilogo cliccabile dei dispositivi F3 esistenti:

```
  ─── F2 verificata ✓ ───────────────
  Contestualizzazioni F3:
  ▸ clinico-9-24m              ✓ verificato
  ▸ educativo-nido            ▶ in_esecuzione
  ▸ formazione-pediatri       ○ avviato 0/10
  [+ Nuova contestualizzazione]
```

I nomi sono link a `/laboratorio/temi/:temaId/dispositivi/:contestoId`. Il pulsante "+ Nuova contestualizzazione" apre la modal `NuovaContestualizzazioneDialog` (§9.4).

### 5.2 Modello visivo — vista Dispositivo (F3-only)

```
DISPOSITIVO clinico-9-24m
← Tema: pointing-clinico (F2 ✓)

  ▸ Pre-requisiti F2 ✓ (clicca per ispezionare)

  ●  f3_step_1 — Lettura                ✓
  │
  ●  f3_step_2 — Stress test            ✓
  │
  ●  f3_step_3 — Correzione         ▶ ◎  ← step in focus
  │
  ○  f3_step_4 — Indistinguibilità
  │
  ○  f3_step_5 — Audit
  │
  ●  f3_step_6 — Stabilizzazione
  │  ●  f3_step_6b — Forma operativa
  │  ●  f3_step_6c — Integrazione        (compare solo se rilevante)
  │
  ○  f3_step_7 — Trasferibilità          ✎ (input richiesto)
  │
  ○  f3_step_8 — Adattamento
  │
  ○  f3_step_9 — Dispositivo completo
  │
  ○  f3_step_10 — Stress test disp.      ✎
```

Il blocco "Pre-requisiti F2 ✓" è una sezione collassabile (di default chiusa). Click → si espande mostrando l'elenco degli step F2 verificati (read-only); click su uno step F2 apre l'output di quello step in un overlay leggero (non naviga via dalla pagina del dispositivo). Per l'edit/relancio di uno step F2, l'utente deve tornare al `LaboratorioTemaPage`.

### 5.3 Caratteristiche comuni

- **Glifo di stato a sinistra del nome**: cerchio pieno (●) per step toccato, vuoto (○) per non avviato, rombo (◇) per decisione umana, ◌ per saltato.
- **Marcatore di stato a destra**: badge testuale identico a `StepStatusBadge` (vedi §5.5).
- **Indicatore di focus**: la riga dello step in focus ha sfondo accentato e prefisso `▶`.
- **Sub-step annidati (2a, 4b in F2; 6b, 6c in F3)**: indentazione di un livello, con tratto di connessione che torna sulla colonna principale.
- **Step `f2_step_1`**: **non appare**. Nel `pipeline-step-config.json`, il rendering filtra gli step con `excluded_from_pipeline_ui === true` o equivalente flag.

### 5.4 Comportamento di interazione

- Click su uno step: `focusedStepId = stepId`, `focusMode = 'manual'`. Il workbench passa a quello step.
- Hover su uno step: tooltip con (a) status, (b) ultima esecuzione (run #N, timestamp), (c) eventuali blocchi (`missing_pipeline_deps`, `missing_external_inputs`).
- Long-press / right-click: menu contestuale rapido — "Apri in workbench" / "Vedi storico run" / "Vai a output file" (per step verificati).
- Tasti freccia (`↑`/`↓`) quando la timeline ha focus: navigazione tra step.
- Nella vista Tema, click su un dispositivo nella sezione "Contestualizzazioni F3": naviga a `/laboratorio/temi/:temaId/dispositivi/:contestoId`.
- Nella vista Dispositivo, click sul blocco "Pre-requisiti F2 ✓": espande/comprime; click su uno step F2 listato dentro: apre overlay di ispezione.

### 5.5 Mapping stato → glifo + badge (riferimento)

| `status` | Glifo | Badge testo | Colore |
|---|---|---|---|
| `non_avviato` | ○ | "Non avviato" | slate-400 |
| `attende_input` | ○ ✎ | "Input richiesto" | sky-500 |
| `attende_decisione` | ◇ | "Decisione" | amber-500 |
| `in_coda` | ● ⋯ | "In coda" | sky-500 |
| `in_esecuzione` | ● ⟳ (pulse) | "In esecuzione" | sky-600 + pulse |
| `completato` | ● | "Completato" | emerald-500 |
| `in_verifica` | ● ◎ | "In verifica" | amber-500 |
| `verificato` | ● ✓ | "Verificato" | emerald-600 |
| `richiede_correzione` | ● ✗ | "Da correggere" | red-500 |
| `fallito` | ● ✗ | "Fallito" | red-600 |
| `saltato` | ◌ | "Saltato" | slate-300 |

### 5.6 Modalità collassata

Quando `timelineCollapsed === true`, la rail mostra solo i glifi (larghezza ~64px). Il nome dello step compare in tooltip al hover. Il marcatore di focus diventa una barra verticale di accento.

### 5.7 Props

```typescript
interface TimelineRailProps {
  variant: 'tema' | 'dispositivo';
  steps: StepConfig[];                    // già filtrati: solo F2 in vista tema, solo F3 in vista dispositivo
  stepStates: Record<string, EnrichedStepState>;
  focusedStepId: string;
  collapsed: boolean;

  // Vista tema (variant === 'tema')
  temaStato?: TemaStato;
  dispositiviChildren?: DispositivoSummary[];
  onCreateDispositivo?: () => void;
  onOpenDispositivo?: (contestoId: string) => void;

  // Vista dispositivo (variant === 'dispositivo')
  temaMadreLabel?: string;
  temaMadreId?: string;
  f2StepStates?: Record<string, EnrichedStepState>;   // read-only del tema madre
  onInspectF2Step?: (stepId: string) => void;          // apre overlay ispezione

  // Comuni
  onSelectStep: (stepId: string) => void;
  onToggleCollapsed: () => void;
  pendingDecision: HumanDecision | null;
  onSelectDecision: () => void;
}

interface DispositivoSummary {
  contesto_id: string;
  contesto_label: string;
  stato: 'non_avviato' | 'in_corso' | 'verificato' | 'parcheggiato' | 'abbandonato' | 'archiviato';
  steps_verified: number;
  steps_total: number;
  active_step_id: string | null;
}
```

---

## 6. `Workbench` — la zona centrale

`Workbench` è il componente di riepilogo per **uno step**. Riceve `focusedStepId` e renderizza header, tre zone, e footer di navigazione.

### 6.1 Layout completo

```
┌─ Header step ──────────────────────────────────────────────────────────┐
│ f3_step_3 · Correzione strutturale       [In esecuzione · run #2 · ⟳] │
│ Fase F3 · Verifica richiesta · Step non saltabile        [⋯ Azioni ▾] │
└────────────────────────────────────────────────────────────────────────┘

┌── INPUT ─────────────────┬── ESECUZIONE ──────────┬── OUTPUT ─────────┐
│ ◆ Dipendenze pipeline    │ Stato: ⟳ in esecuzione │ Output atteso:    │
│ ─────────────────────    │ Run: #2                │ correzione-       │
│ ✓ f3_step_1 (lettura)    │ Avviato: 11:01:05      │ strutturale-v2    │
│   [Ispeziona →]          │                        │                   │
│ ✓ f3_step_2 (stress)     │ ┌─ Live log ────────┐ │ (Output sarà      │
│   [Ispeziona →]          │ │ 11:01:05 INFO ... │ │  visibile a       │
│                          │ │ 11:01:12 INFO ... │ │  esecuzione       │
│ ◆ Input strutturali      │ │ 11:03:44 INFO ... │ │  completata)      │
│ ─────────────────────    │ │ 11:07:21 WARN ... │ │                   │
│ • structural-correction  │ │  ⏵                │ │                   │
│   -schema.json           │ │ [auto-scroll on]  │ │                   │
│   [Visualizza schema →]  │ └───────────────────┘ │                   │
│                          │ [Annulla esecuzione] │                   │
│ ◆ Input esterni          │                        │                   │
│ ─────────────────────    │                        │                   │
│ Nessuno                  │                        │                   │
└──────────────────────────┴────────────────────────┴───────────────────┘

[← f3_step_2: Stress test]                     [f3_step_4: Indistinguibilità →]
```

### 6.2 Header step — `WorkbenchHeader`

```typescript
interface WorkbenchHeaderProps {
  step: StepConfig;
  stepState: EnrichedStepState;
  primaryAction: PrimaryActionDescriptor;
  secondaryActions: SecondaryAction[];   // per il menu ⋯
  onPrimaryAction: () => void;
  onSecondaryAction: (id: SecondaryActionId) => void;
}

interface PrimaryActionDescriptor {
  label: string;            // es. "Lancia esecuzione", "Annulla", "Verifica output"
  variant: 'launch' | 'cancel' | 'verify' | 'relaunch' | 'decide' | 'view_logs' | 'none';
  disabled: boolean;
  disabledReason?: string;  // tooltip se disabled
}

type SecondaryActionId =
  | 'skip'              // step saltabili, non saltati
  | 'view_run_history'
  | 'view_error_log'
  | 'request_6c_integration'
  | 'open_output_file'  // step verificati: link al file JSON
  | 'copy_output_path'
  | 'rerun_with_extra_params';
```

L'azione primaria è **sempre un solo pulsante grosso** in alto a destra dell'header, ben visibile. Le azioni secondarie sono nascoste dietro `⋯ Azioni ▾`.

### 6.3 Zona INPUT — `WorkbenchInputPanel`

Mostra in sequenza tre gruppi (omettendo quelli vuoti):

**Dipendenze pipeline.** Lista di `inputs_pipeline` con un ✓/✗/⋯ indicatore di soddisfacimento (calcolato da `stepStates`). Ogni voce ha un pulsante secondario **"Ispeziona →"** che apre, **inline sotto la voce**, un viewer JSON dell'output del passo dipendente. Doppio click → espande in altezza piena della zona INPUT (modalità "ispezione profonda").

**Input strutturali.** Schema/json dei vincoli (file in `inputs_strutturali`). Pulsante **"Visualizza schema →"** apre lo stesso viewer inline con il file caricato da `/pipeline/...`.

**Input esterni.** Per ogni `ExternalInputConfig`:
- Se non ancora fornito: card con label + descrizione + pulsante **"Compila →"** che monta inline il form (vedi §7).
- Se già fornito: card con riepilogo dei valori chiave + pulsante **"Modifica"** + pulsante **"Vedi JSON"**.
- Se opzionale: badge "Facoltativo" e default value mostrato esplicitamente (es. `severità test = "standard"`).

```typescript
interface WorkbenchInputPanelProps {
  step: StepConfig;
  stepState: EnrichedStepState;
  pipelineInputResolutions: Record<string, PipelineInputResolution>;
  externalInputs: PipelineExternalInput[];
  onInspectPipelineInput: (stepId: string) => void;     // mostra il JSON dell'output del dep
  onInspectStructuralInput: (path: string) => void;
  onProvideExternalInput: (inputId: string) => void;    // monta il form inline
  onEditExternalInput: (inputId: string) => void;
  onShowExternalInputJson: (inputId: string) => void;
}

interface PipelineInputResolution {
  satisfied: 'yes' | 'no' | 'pending_verifica';
  source_step_id: string;
  source_output_path: string | null;
  required_status: string;
  current_status: string;
}
```

### 6.4 Zona ESECUZIONE — `WorkbenchRunPanel`

Cuore operativo. Quattro sotto-stati visivi:

**Stato A — Lanciabile.** Bottone grosso "Lancia esecuzione" centrato. Sotto: una checklist riassuntiva in verde delle pre-condizioni soddisfatte.

```
✓ Dipendenze pipeline soddisfatte
✓ Input strutturali presenti
✓ Input esterni completi
─────────────────────────────────
        [Lancia esecuzione]
```

**Stato B — Bloccato.** Bottone disabilitato + spiegazione testuale dei blocchi:

```
⚠ Non lanciabile

Mancano:
  • f3_step_4 (richiesto verificato — attualmente in_verifica)
  • f3_step_5 (richiesto verificato — attualmente non_avviato)

✎ Input richiesto:
  • Contesto/ambito target  [Compila →]
```

Il pulsante "Compila →" sposta il focus alla zona INPUT (auto-scroll) e apre il form pertinente.

**Stato C — In esecuzione.** Pannello live log con SSE attivo. Run #N. Tempo trascorso. Pulsante "Annulla esecuzione" in basso. Vedi §8 per il componente `LiveLogPanel`.

**Stato D — Conclusa.** Riassunto: durata, esito (`completato` / `fallito` / `verificato`). Lista delle ultime 3 run con badge stato. Pulsante "Vedi log run #N" e "Rilancia" se applicabile.

```typescript
interface WorkbenchRunPanelProps {
  step: StepConfig;
  stepState: EnrichedStepState;
  activeExecutionId: string | null;
  runHistory: ExecutionSummary[];   // recenti, max 5
  onLaunch: () => void;             // chiama orchestration.runStep
  onCancel: () => void;
  onRelaunch: () => void;
  onShowRunLog: (executionId: string) => void;
}

interface ExecutionSummary {
  execution_id: string;
  run_number: number;
  status: ExecutionStatus;
  started_at: string;
  ended_at: string | null;
  duration_ms: number | null;
}
```

### 6.5 Zona OUTPUT — `WorkbenchOutputPanel`

Comportamento dipendente dallo stato dello step:

**Output non disponibile** (status `non_avviato`, `attende_input`, `attende_decisione`, `in_coda`): zona vuota con illustrazione neutra e testo:

> *"L'output sarà disponibile a esecuzione completata. Atteso: `correzione-strutturale-v2.json`"*

**Output in produzione** (status `in_esecuzione`): testo neutro:

> *"Esecuzione in corso. L'output verrà mostrato non appena disponibile."*

Eventuale spinner discreto.

**Output disponibile** (status `completato`, `in_verifica`, `verificato`, `richiede_correzione`):

```
┌─ Output: correzione-strutturale-v2.json ────────────────────────────┐
│ [ Anteprima · JSON · Diff con v1 ]                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [renderizzato dal componente specifico per tipo di step]           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Status: ◎ In verifica

Note di verifica (opzionali):
[___________________________________________________________________]

Esito:
  ○ Approva (sblocca step dipendenti)
  ○ Richiedi correzione (rilancia lo step)
  ○ Richiedi integrazione 6c (solo per f3_step_6b)

Motivazione (richiesta se non approvato):
[___________________________________________________________________]

                                              [Conferma verifica →]
```

I tre tab sopra il contenuto:

- **Anteprima**: rendering dedicato per tipo di step. Mappa identica a D5 §8 (preserva il riuso di `DeviceViewer`, `StressTestDashboard`, `CorrectionsLog`).
- **JSON**: viewer JSON pretty-printed con copia-clipboard.
- **Diff con vN-1**: solo se esiste una run precedente — diff JSON side-by-side. Implementabile con `react-diff-viewer` o equivalente.

I controlli di verifica appaiono **solo** se `stepState.status === 'in_verifica'` e l'utente ha permesso di verificare. Una volta confermato, il pannello passa a stato "verificato" con badge ✓✓ e i controlli scompaiono. Le note e l'esito restano leggibili (read-only).

```typescript
interface WorkbenchOutputPanelProps {
  step: StepConfig;
  stepState: EnrichedStepState;
  outputFile: string | null;       // path relativo per fetch JSON
  previousVersionFile: string | null;  // per il diff
  canVerify: boolean;              // = (stepState.status === 'in_verifica' && isAdmin)
  onVerify: (outcome: VerificaOutcome, notes: string, feedback: string) => Promise<void>;
  onDownloadOutput: () => void;
  onOpenInExternalViewer: () => void;
}
```

### 6.6 Footer di navigazione

```
[← f3_step_2: Stress test]                     [f3_step_4: Indistinguibilità →]
```

I link `prev`/`next` sono calcolati sull'ordine di `stepConfig.steps` filtrato per la pipeline corrente (F2 nella vista Tema, F3 nella vista Dispositivo). Cliccarli passa il focus a quello step (e setta `focusMode = 'manual'`).

Edge case: per il primo step della pipeline il pulsante `prev` è disabilitato; per l'ultimo, il `next` è disabilitato. Nella vista Tema, dopo `f2_step_6` verificato, il `next` punta alla sezione Contestualizzazioni (vedi §6.7) come "ultimo passo" naturale.

### 6.7 Sezione "Contestualizzazioni F3" (solo vista Tema)

Compare **come trailing del Workbench** nella `LaboratorioTemaPage`, **solo quando `tema.stato === 'f2_verificata'`**. Prima di quella soglia non viene renderizzata.

#### 6.7.1 Layout

```
═══════════════════════════════════════════════════════════════════════════
CONTESTUALIZZAZIONI F3
Da questo tema sono stati derivati i seguenti dispositivi contestualizzati.
Ogni dispositivo è una pipeline F3 indipendente.

┌─────────────────────────────────────────────────────────────────────────┐
│ ▶ clinico-neurosviluppo-9-24-mesi                  ✓ verificato 10/10   │
│   Setting: ambulatorio · Profilo osservatore: logopedista               │
│   Ultimo aggiornamento: 2 ore fa                                        │
│                                                  [Apri laboratorio →]   │
├─────────────────────────────────────────────────────────────────────────┤
│ ▶ educativo-nido                                  ⟳ in_esecuzione 4/10  │
│   Setting: nido d'infanzia · Profilo: educatore                         │
│   f3_step_4 in esecuzione · run #1                                       │
│                                                  [Apri laboratorio →]   │
├─────────────────────────────────────────────────────────────────────────┤
│ ▶ formazione-pediatri                             ○ avviato 0/10        │
│   Setting: aula formativa · Profilo: pediatra                           │
│                                                  [Apri laboratorio →]   │
└─────────────────────────────────────────────────────────────────────────┘

[+ Nuova contestualizzazione]
═══════════════════════════════════════════════════════════════════════════
```

Ogni card mostra:

- Glifo + label del contesto (cliccabile come l'intera card).
- Riassunto strutturato del contesto (setting, profilo osservatore — letti da `f3_step_7` se eseguito, altrimenti dai metadati di creazione).
- Avanzamento pipeline: `N/10` step verificati + stato dello step attivo.
- Timestamp di ultimo aggiornamento.
- Pulsante "Apri laboratorio →" che naviga a `/laboratorio/temi/:temaId/dispositivi/:contestoId`.

Le card sono ordinate per data di ultimo aggiornamento decrescente. Il pulsante "+ Nuova contestualizzazione" apre la modal `NuovaContestualizzazioneDialog` (§9.4).

#### 6.7.2 Empty state

Quando non ci sono ancora dispositivi:

```
═══════════════════════════════════════════════════════════════════════════
CONTESTUALIZZAZIONI F3

La pipeline F2 di questo tema è verificata. Puoi ora contestualizzarlo
in uno o più ambiti per produrre dispositivi operativi.

                       [+ Crea prima contestualizzazione]
═══════════════════════════════════════════════════════════════════════════
```

#### 6.7.3 Props

```typescript
interface ContestualizzazioniSectionProps {
  temaId: string;
  temaLabel: string;
  dispositivi: DispositivoSummary[];
  onCreate: () => void;                              // apre NuovaContestualizzazioneDialog
  onOpen: (contestoId: string) => void;
}
```

I dati sono caricati al mount del `LaboratorioTemaPage` con `useDispositiviTema(temaId)`. Polling: la lista ricarica ogni 15s se almeno un dispositivo è in stato `in_corso` (granularità più larga del polling step-level perché qui basta il riassunto).

---

## 7. `ExternalInputPanel` — il form inline

Sostituisce `ExternalInputForm` (D5 §5). Non è una modal: è un pannello che si espande **dentro la zona INPUT** del workbench, sotto la card dell'input pertinente.

### 7.1 Layout (espanso sotto la card)

```
◆ Input esterni
─────────────────────
Card f3_step_7: Contesto/ambito target           [✎ Compila ▾]
┌─────────────────────────────────────────────────────────────┐
│  Dominio target *                                           │
│  ◯ clinico   ◯ educativo   ◯ formazione   ◯ politiche      │
│                                                             │
│  Sottodominio                                               │
│  [_____________________________]   es. neuropsviluppo       │
│                                                             │
│  Fascia d'età                                               │
│  [_____________________________]   es. 9-24 mesi            │
│                                                             │
│  Setting                                                    │
│  [_____________________________]   es. ambulatorio          │
│                                                             │
│  Profilo osservatore                                        │
│  [_____________________________]   es. logopedista          │
│                                                             │
│  Note (opzionale)                                           │
│  [_____________________________________________________]    │
│                                                             │
│         [Annulla]   [Salva input]                           │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Form per step

Identici alla §5 di D5, **ma renderizzati inline** invece che in modal. Mantenere le tre forme:

- `f2_step_2` — scelta tema (campi: tema_label*, descrizione, motivazione)
- `f3_step_7` — contesto (campi: dominio*, sottodominio, fascia_eta, setting, profilo_osservatore, note)
- `f3_step_10` — 5 casi stress test (5 textarea fissi: assente, parziale, chiudente, apparente_scripted, quasi_indistinguibile)

Per `f3_step_10`, ogni caso è una sezione `<details>` collassabile. La prima è aperta di default. Un contatore in alto mostra "3 / 5 casi compilati".

### 7.3 Comportamento

1. Pre-popola con `existingInputs` se presente.
2. Validazione client-side (campi obbligatori) **mentre l'utente digita** (verde/rosso sui bordi del campo, non blocca finché l'utente non clicca "Salva").
3. "Salva input" → `orchestration.submitExternalInput(stepId, inputId, data)` → al successo: il pannello si **collassa** e la card mostra il riepilogo. Toast non bloccante: *"Input salvato. Step pronto per il lancio."*
4. "Annulla" → collassa il pannello senza salvare. Se ci sono modifiche non salvate: chiede conferma.

### 7.4 Schema-driven per estendibilità

Anche se per `f3_step_7` e `f3_step_10` l'implementazione iniziale è hardcoded, definire un'interfaccia `ExternalInputRenderer` per favorire la generalizzazione:

```typescript
interface ExternalInputRendererProps {
  inputConfig: ExternalInputConfig;
  initialValue: Record<string, unknown> | null;
  onSubmit: (data: Record<string, unknown>) => Promise<void>;
  onCancel: () => void;
}

// Registry: input_id → renderer
const externalInputRenderers: Record<string, React.FC<ExternalInputRendererProps>> = {
  scelta_tema: F2Step2InputRenderer,
  contesto_ambito: F3Step7InputRenderer,
  casi_stress_test: F3Step10InputRenderer,
  // facoltativi opzionali con renderer generico:
  severita_test: GenericEnumInputRenderer,
  specificita_dispositivo: GenericEnumInputRenderer,
  fonti_web: GenericTextInputRenderer,
};
```

`ExternalInputPanel` sceglie il renderer dal registry; se non trovato → fallback a `<JsonInputRenderer>` (textarea con validazione JSON).

---

## 8. `LiveLogPanel` — log inline

Sostituisce `ExecutionLogViewer` (D5 §7). Non è un drawer: è il pannello centrale della zona ESECUZIONE quando lo step è `in_esecuzione`.

### 8.1 Layout

```
┌─ Live log · run #2 ────────────────────────────── [11:14 trascorsi] ──┐
│ 11:01:05 INFO  Avvio step f3_step_3 per tema pointing                  │
│ 11:01:12 INFO  Caricamento dispositivo di lettura...                   │
│ 11:03:44 INFO  Analisi delle fratture dallo stress test...             │
│ 11:07:21 WARN  Dimensione co-regolatoria: articolazione                │
│                insufficiente — applicazione correzione                  │
│ 11:14:30 INFO  Output scritto: correzione-strutturale-v2.json          │
│  ⏵                                                                     │
│  [auto-scroll: ●]                                                      │
├────────────────────────────────────────────────────────────────────────┤
│ [Annulla esecuzione]   [Espandi a tutta pagina ⤢]   [Copia log ↓]     │
└────────────────────────────────────────────────────────────────────────┘
```

- Sfondo scuro (slate-900), font monospace, livello-colorato (info=slate-100, warn=amber-300, error=red-400).
- Auto-scroll attivo per default; si disattiva se l'utente scrolla manualmente verso l'alto e si riattiva quando torna in fondo.
- Il pulsante "Espandi a tutta pagina ⤢" rende il log a piena viewport (overlay), utile per esecuzioni lunghe — è l'unica eccezione "modal-like" del flusso normale, e solo perché il log può essere molto verboso.
- A esecuzione conclusa: appare una banda colorata in fondo al log con esito (`✓ Completato in 13:25` / `✗ Fallito dopo 0:45 — vedi messaggio sopra`). Il pulsante "Annulla" diventa "Vai alla verifica →" (se `verifica_required`) o "Vedi output →" (altrimenti, salta alla zona OUTPUT con auto-scroll).

### 8.2 Hook

Riutilizza `useExecutionLogs` (D5 §7) **senza modifiche**.

### 8.3 Props

```typescript
interface LiveLogPanelProps {
  executionId: string;
  stepId: string;
  runNumber: number;
  isFinishing: boolean;
  onExpandFullScreen: () => void;
  onCancel: () => void;
  onJumpToVerify?: () => void;       // se verifica richiesta
  onJumpToOutput?: () => void;       // altrimenti
  onCopyLog: () => void;
}
```

---

## 9. Modali residue (atti deliberati)

Le uniche modali sopravvissute sono per atti **fortemente intenzionali**, in cui l'attenzione piena è una virtù: skip step, decisione umana strutturale, **creazione di una nuova contestualizzazione F3**.

### 9.1 `SkipStepDialog`

Apertura: dal menu `⋯ Azioni ▾` dello header step, voce "Salta step…" (visibile solo se `step.can_skip === true` e status non terminale).

```
╔══════════════════════════════════════════════════════════════════╗
║  Salta step f3_step_8 — Adattamento strutturale                  ║
╠══════════════════════════════════════════════════════════════════╣
║  Saltare uno step lo marca come non eseguito ma sblocca i suoi   ║
║  dipendenti (in questo caso: f3_step_9).                         ║
║                                                                  ║
║  Condizione di skip raccomandata:                                ║
║  "Specializzazione di dominio (non nuovo tema) — step 8 non      ║
║   necessario"                                                    ║
║                                                                  ║
║  Motivo dello skip *                                             ║
║  [_______________________________________________________]       ║
║                                                                  ║
║                                  [Annulla]  [Conferma skip →]    ║
╚══════════════════════════════════════════════════════════════════╝
```

```typescript
interface SkipStepDialogProps {
  stepId: string;
  stepLabel: string;
  recommendedReason?: string;        // da step.skip_condition
  unlockedSteps: string[];           // chi si sbloccherà
  onConfirm: (reason: string) => Promise<void>;
  onClose: () => void;
}
```

### 9.2 `HumanDecisionDialog` (preservata, una sola variante attiva)

Variante attiva nel modello r2:
- `step7_context_selection` (conferma contesto in pipeline F3)

La variante `f2_to_f3_tema_selection` di D5 §6 è **rimossa** dal grafo delle decisioni di pipeline (vedi nota in §9.3). Le sue funzioni sono assorbite, una metà dall'archivio (selezione/promozione tema) e l'altra da `NuovaContestualizzazioneDialog` (creazione dispositivo).

Motivazione del mantenimento di `step7_context_selection`: la conferma del contesto è una decisione **strutturale**, ha conseguenze metodologiche profonde (definisce il vincolo di realtà del dispositivo). La modal a piena attenzione è un freno deliberato corretto. **Non integrare nel workbench.**

L'apertura è governata da:
- Click sul pulsante "Prendi decisione" del `PendingDecisionBanner`.
- Click sull'azione primaria dello step quando `action === 'decide'`.

### 9.3 `PendingDecisionBanner` (preservato)

Banner sticky in cima al Laboratorio, sotto la TopBar. Identico a D5 §9. Apre `HumanDecisionDialog`.

```
┌──────────────────────────────────────────────────────────────────┐
│ 🔔 Decisione richiesta: Conferma contesto per il dispositivo     │
│ La pipeline è in attesa di una scelta strutturale.               │
│                                       [Prendi decisione →]       │
└──────────────────────────────────────────────────────────────────┘
```

> Nota: nel nuovo modello a tre entità, la decisione "F2 → F3 selezione tema" non esiste più come decisione di pipeline. La promozione di un tema candidato avviene nell'archivio (atto separato) e la creazione di un dispositivo F3 contestualizzato avviene in `NuovaContestualizzazioneDialog` (§9.4). Resta come decisione il **contesto step 7** (`step7_context_selection`), che continua ad apparire come pending decision durante la pipeline F3.

### 9.4 `NuovaContestualizzazioneDialog`

Modal aperta da:

- Pulsante "+ Nuova contestualizzazione" nella sezione `ContestualizzazioniSection` del `LaboratorioTemaPage` (§6.7).
- Pulsante "+ Crea prima contestualizzazione" dello stato vuoto della stessa sezione.
- Pulsante in coda alla sezione "Contestualizzazioni F3" della `TimelineRail` in vista Tema (§5.1).

Visibile solo se `tema.stato === 'f2_verificata'`.

#### 9.4.1 Layout

```
╔══════════════════════════════════════════════════════════════════╗
║  Nuova contestualizzazione del tema "pointing-clinico"           ║
╠══════════════════════════════════════════════════════════════════╣
║  Stai per avviare una pipeline F3 che porterà il tema verificato ║
║  in un ambito specifico, producendo un dispositivo operativo     ║
║  contestualizzato.                                               ║
║                                                                  ║
║  Dominio target *                                                ║
║  ◯ clinico   ◯ educativo   ◯ formazione   ◯ politiche           ║
║                                                                  ║
║  Etichetta del contesto (slug) *                                 ║
║  [clinico-neurosviluppo-9-24-mesi               ]                ║
║  Pattern kebab-case · Identifica univocamente il dispositivo     ║
║                                                                  ║
║  Etichetta leggibile                                             ║
║  [Clinico — neurosviluppo 9-24 mesi             ]                ║
║                                                                  ║
║  Note di indirizzo (opzionale)                                   ║
║  [_____________________________________________]                 ║
║  Annotazioni del ricercatore sul perché di questo contesto.      ║
║  Verranno conservate ma non condizionano la pipeline F3.         ║
║                                                                  ║
║  ⚠ Verrà creata una pipeline F3 indipendente. Il dispositivo     ║
║   risultante sarà autonomo dagli altri dispositivi-fratelli.     ║
║                                                                  ║
║                          [Annulla]  [Crea e apri laboratorio →]  ║
╚══════════════════════════════════════════════════════════════════╝
```

#### 9.4.2 Comportamento

1. Validazione client-side: `dominio` obbligatorio (radio); `slug` obbligatorio + pattern kebab-case + univoco tra i dispositivi-fratelli del tema (controllo client su `dispositivi` già caricati + verifica server al submit).
2. Lo slug è pre-suggerito a partire dal dominio scelto (es. selezione `clinico` → suggerito `clinico-...`), ma l'utente lo personalizza.
3. Submit → `POST /api/pipeline/temi/:temaId/dispositivi` (⚠ NEW BACKEND) con payload `{ contesto_id, contesto_label, dominio, note }`. Il backend crea il `PipelineContext` per il dispositivo F3.
4. Risposta 201 → toast "Dispositivo creato" + redirect a `/laboratorio/temi/:temaId/dispositivi/:contestoId`.
5. Nel nuovo `LaboratorioDispositivoPage`, il fronte attivo è `f3_step_1` (lanciabile, perché `f2_step_6` esiste e verificato).

#### 9.4.3 Differenza rispetto al form `f3_step_7`

Il dialog raccoglie **solo i metadati identitari minimi** del contesto (dominio + slug + label + note). I metadati strutturali completi del contesto (setting, profilo osservatore, fascia d'età, sottodominio) vengono raccolti **dopo**, nel form `f3_step_7` quando la pipeline F3 lo raggiunge.

Motivazione: lo slug serve subito (è l'identità del dispositivo); i metadati strutturali servono solo allo step 7 e potrebbero essere precisati man mano che il ricercatore avanza.

#### 9.4.4 Props

```typescript
interface NuovaContestualizzazioneDialogProps {
  temaId: string;
  temaLabel: string;
  existingContestiIds: string[];        // per validazione univocità slug
  onSubmit: (payload: NuovaContestualizzazionePayload) => Promise<{ contestoId: string }>;
  onClose: () => void;
}

interface NuovaContestualizzazionePayload {
  contesto_id: string;          // slug
  contesto_label: string;
  dominio: 'clinico' | 'educativo' | 'formazione' | 'politiche';
  note?: string;
}
```

---

## 10. Index del Laboratorio (vista d'ingresso)

Quando l'admin clicca sulla voce di nav "Laboratorio" senza un tema/dispositivo selezionato, vediamo un'index organizzata per tema (con i suoi dispositivi annidati):

```
LABORATORIO HCAIRE                            [Apri archivio temi →]

▸ Temi in lavorazione F2 (2)
  ┌──────────────────────────────────────────────────────────────────┐
  │ TEMA · lettura-condivisa-0-3                                     │
  │ stato: f2_in_corso · F2 4/7 verificati · ◎ in_verifica           │
  │ Aggiornato 2 ore fa                              [Apri lab →]    │
  ├──────────────────────────────────────────────────────────────────┤
  │ TEMA · regolazione-corporea                                      │
  │ stato: f2_in_corso · F2 6/7 verificati                           │
  │ Aggiornato 3 giorni fa                           [Apri lab →]    │
  └──────────────────────────────────────────────────────────────────┘

▸ Temi con F2 verificata (2 — pronti per contestualizzazione)
  ┌──────────────────────────────────────────────────────────────────┐
  │ TEMA · pointing-clinico  ✓                                       │
  │ 3 dispositivi F3:                                                │
  │   ▸ clinico-9-24m         ✓ verificato 10/10  [Apri →]          │
  │   ▸ educativo-nido        ▶ in_esecuzione 4/10 [Apri →]          │
  │   ▸ formazione-pediatri   ○ avviato 0/10      [Apri →]          │
  │ [+ Nuova contestualizzazione]                  [Apri tema →]     │
  ├──────────────────────────────────────────────────────────────────┤
  │ TEMA · pianto-modulato  ✓                                        │
  │ Nessun dispositivo F3 ancora                                     │
  │ [+ Crea prima contestualizzazione]              [Apri tema →]    │
  └──────────────────────────────────────────────────────────────────┘

▸ Temi parcheggiati / abbandonati (collassato di default — clicca per espandere)
```

Componente: `LaboratorioIndexPage` su route `/laboratorio`.

- Sorgente dati: `GET /api/pipeline/temi?include=dispositivi_summary` (⚠ NEW BACKEND — estensione dell'endpoint index esistente). Risposta: array di `TemaSummary` con `dispositivi: DispositivoSummary[]`.
- Raggruppamento per `tema.stato`: `f2_in_corso` (sezione 1), `f2_verificata` (sezione 2 — quella che mostra i figli), `parcheggiato/abbandonato/archiviato` (sezione 3 collassata).
- Le card di tema sono cliccabili: il click su corpo card naviga al `LaboratorioTemaPage`. I link interni dei dispositivi navigano al `LaboratorioDispositivoPage` corrispondente.
- Il pulsante "Apri archivio temi →" linka all'archivio (route `/archivio/temi`, fuori scope di questo doc).
- Non c'è più un pulsante "+ Nuova ricerca" nell'index del Laboratorio: la creazione di un nuovo tema-ricerca passa dall'archivio (promozione di un tema candidato).

---

## 11. Mapping dello stato sull'UI (matrice di riferimento)

Tabella di riferimento per Claude Code: per ciascun `EnrichedStepState.status`, cosa mostra ciascuna zona.

| Status | Header — azione primaria | INPUT panel | RUN panel | OUTPUT panel |
|---|---|---|---|---|
| `non_avviato` (lanciabile) | "Lancia esecuzione" | Tutto verde, tutti soddisfatti | Stato A (lanciabile) | Vuoto: "Disponibile dopo esecuzione" |
| `non_avviato` (bloccato deps) | Disabled — tooltip blocchi | Card blocchi rosse | Stato B (bloccato) | Vuoto |
| `attende_input` | "Compila input" | Form inline aperto sull'input mancante | Stato B (bloccato) | Vuoto |
| `attende_decisione` | "Prendi decisione" | Card con riepilogo input | Stato B + nota "Attende decisione umana" | Vuoto |
| `in_coda` | "Annulla" | Read-only riepilogo | "In coda — Cowork riceverà a breve" | Vuoto |
| `in_esecuzione` | "Annulla" | Read-only riepilogo | Stato C (Live log) | "Esecuzione in corso" |
| `completato` (no verifica) | "Vai allo step successivo" | Read-only riepilogo | Stato D (run history) | Output renderizzato — tab Anteprima/JSON/Diff |
| `in_verifica` | "Verifica output" → scroll alla zona OUTPUT | Read-only riepilogo | Stato D | Output renderizzato + form verifica |
| `verificato` | "Vai allo step successivo" | Read-only riepilogo | Stato D | Output renderizzato (read-only) + badge ✓✓ + note di verifica |
| `richiede_correzione` | "Rilancia esecuzione" | Read-only riepilogo + feedback verifica precedente | Stato D | Output precedente (read-only) + motivazione correzione richiesta |
| `fallito` | "Rilancia esecuzione" | Read-only riepilogo | Stato D + messaggio errore | Vuoto |
| `saltato` | "Annulla skip" (riapre lo step) | Read-only riepilogo | Banner "Step saltato — motivo: ..." | Vuoto |

**Nota su "Annulla skip"**: nuova azione conveniente. Implementabile come `POST /api/pipeline/temi/:id/steps/:id/run` con `extra_params.unskip = true` (da definire con backend) oppure rimossa se non supportata. Da decidere con D4.

---

## 12. Flussi utente (riformulati per il workbench)

### 12.1 Flusso A — Lancio diretto (nessun input esterno)

```
1. Admin apre /laboratorio/temi/pointing-clinico
2. Auto-focus calcola fronte attivo: f3_step_3
3. Workbench mostra:
     INPUT     — tutto verde
     ESEC.     — Stato A: pulsante "Lancia esecuzione"
     OUTPUT    — vuoto
4. Admin clicca "Lancia esecuzione"
5. Aggiornamento ottimistico → status: in_coda
6. ESEC. cambia in "In coda" con spinner
7. Polling raccoglie status: in_esecuzione → ESEC. passa a Stato C (Live log)
8. SSE collegato, righe scorrono in tempo reale
9. Evento done → banda verde "✓ Completato in 13:25" + bottone "Vai alla verifica →"
10. Admin clicca "Vai alla verifica →" — auto-scroll alla zona OUTPUT
11. OUTPUT mostra il dispositivo prodotto (tab Anteprima/JSON/Diff) + form verifica
12. Admin seleziona "Approvato", aggiunge nota, clicca "Conferma verifica"
13. Status → verificato → focus auto avanza a f3_step_4
```

### 12.2 Flusso B — Step con input esterno (f3_step_7)

```
1. Auto-focus → f3_step_7 (status attende_input)
2. Workbench:
     INPUT  — card "Contesto/ambito target" con badge ✎ "Da compilare"
              + pulsante "Compila →"
     ESEC.  — Stato B: "Compila l'input prima di lanciare"
     OUTPUT — vuoto
3. Admin clicca "Compila →"
4. Sotto la card si espande il form (renderer F3Step7)
5. Admin compila i campi, clicca "Salva input"
6. Form si collassa; card mostra riepilogo + pulsanti "Modifica" e "Vedi JSON"
7. status → attende_decisione (è uno step con conferma strutturale)
8. PendingDecisionBanner appare in cima
9. Admin clicca "Prendi decisione"
10. HumanDecisionDialog (variante step7) → conferma
11. status → non_avviato lanciabile → ESEC. passa a Stato A
12. Da qui: flusso A
```

### 12.3 Flusso C — Verifica con richiesta di correzione

```
1. f3_step_3 in stato in_verifica
2. Workbench mostra OUTPUT con dispositivo + form verifica
3. Admin esamina il dispositivo, ritiene insufficiente la dimensione co-regolatoria
4. Seleziona "Richiedi correzione"
5. Compila motivazione (obbligatoria): "La dimensione co-regolatoria non distingue
   tra Fase 0 di pre-attenzione e Fase 1 di engagement diadico"
6. Clicca "Conferma verifica"
7. status → richiede_correzione
8. Header step: azione primaria diventa "Rilancia esecuzione"
9. INPUT mostra la motivazione della correzione richiesta come "feedback per l'agente"
10. Admin clicca "Rilancia"
11. status → in_coda → in_esecuzione → flusso A da step 7
```

### 12.4 Flusso D — Promozione di un tema dall'archivio (richiamato per completezza)

Sequenza pre-Laboratorio (sarà specificata in dettaglio nel documento sull'archivio):

```
1. Admin in /archivio/temi vede il tema candidato "pointing-precoce" in stato maturo
2. Clicca "Promuovi a ricerca F2" → dialog di conferma (slug, label, controllo metadati minimi)
3. Submit → backend crea il record in collezione `temi` con stato 'promosso'
4. Redirect → /laboratorio/temi/pointing-clinico
5. LaboratorioTemaPage si apre, auto-focus su f2_step_2 (primo step della pipeline F2)
6. Da qui: flusso A
```

### 12.5 Flusso E — Skip step 8

```
1. Auto-focus → f3_step_8 (status non_avviato, lanciabile)
2. Admin sa che il dispositivo è una specializzazione di dominio: vuole saltare 8
3. Header step → menu ⋯ → "Salta step…"
4. SkipStepDialog si apre con motivo raccomandato pre-popolato
5. Admin lo accetta o personalizza, clicca "Conferma skip"
6. status → saltato
7. Focus auto avanza a f3_step_9 (sbloccato)
8. Nella timeline, f3_step_8 ha glifo ◌ con badge "Saltato"
9. Cliccando f3_step_8 nella timeline: workbench mostra il pannello "Step saltato — motivo: …"
   con possibilità (se implementata) di riaprirlo
```

### 12.6 Flusso F — Nuova contestualizzazione F3

```
 1. Tema "pointing-clinico" ha F2 verificata (stato: f2_verificata)
 2. Admin apre /laboratorio/temi/pointing-clinico
 3. Workbench in modalità "F2 conclusa": l'azione primaria della TopBar è
    "+ Nuova contestualizzazione". Sotto la timeline F2 appare la
    ContestualizzazioniSection (§6.7) con eventuali dispositivi esistenti
 4. Admin clicca "+ Nuova contestualizzazione"
 5. Si apre NuovaContestualizzazioneDialog
 6. Admin sceglie dominio "clinico", inserisce slug "clinico-neurosviluppo-9-24m",
    label leggibile, opzionalmente note
 7. Validazione client: slug univoco tra dispositivi-fratelli ✓, kebab-case ✓
 8. Click "Crea e apri laboratorio →"
 9. POST /api/pipeline/temi/pointing-clinico/dispositivi → 201 con contesto_id
10. Redirect a /laboratorio/temi/pointing-clinico/dispositivi/clinico-neurosviluppo-9-24m
11. LaboratorioDispositivoPage si apre. La TimelineRail mostra solo F3.
    Il blocco "Pre-requisiti F2 ✓" è disponibile (collassato).
12. Auto-focus → f3_step_1, action: 'launch' (output-tipo-vuoto-v1 del tema esiste già)
13. Da qui: flusso A
```

### 12.7 Flusso G — Apertura di un dispositivo esistente

```
1. Admin apre /laboratorio/temi/pointing-clinico
2. Sotto la TimelineRail F2 vede 3 dispositivi nella sezione Contestualizzazioni
3. Clicca su "educativo-nido" (in stato in_esecuzione, f3_step_4 attivo)
4. Naviga a /laboratorio/temi/pointing-clinico/dispositivi/educativo-nido
5. LaboratorioDispositivoPage carica il context F3 del dispositivo
6. Auto-focus → f3_step_4 (in esecuzione)
7. Workbench mostra Stato C (live log SSE) — flusso A in corso, ripreso al volo
```

---

## 13. Struttura file da creare

```
client/src/
├── pages/
│   ├── LaboratorioIndexPage.tsx                  ← /laboratorio
│   ├── LaboratorioTemaPage.tsx                   ← /laboratorio/temi/:temaId
│   └── LaboratorioDispositivoPage.tsx            ← /laboratorio/temi/:temaId/dispositivi/:contestoId
├── components/laboratorio/
│   ├── LaboratorioShell.tsx                      ← layout comune alle due pagine
│   ├── TopBar.tsx
│   ├── TimelineRail.tsx
│   ├── TimelineRailItem.tsx
│   ├── ContestualizzazioniSection.tsx            ← solo vista Tema
│   ├── DispositivoCard.tsx                       ← riga di ContestualizzazioniSection
│   ├── PrerequisitiF2Block.tsx                   ← solo vista Dispositivo (top della timeline)
│   ├── Workbench.tsx
│   ├── WorkbenchHeader.tsx
│   ├── WorkbenchInputPanel.tsx
│   ├── WorkbenchRunPanel.tsx
│   ├── WorkbenchOutputPanel.tsx
│   ├── LiveLogPanel.tsx
│   ├── LiveLogPanelFullScreen.tsx
│   ├── ExternalInputPanel.tsx
│   ├── PipelineDependencyCard.tsx                ← card "✓ f3_step_1 [Ispeziona →]"
│   ├── StructuralInputCard.tsx
│   ├── ExternalInputCard.tsx
│   ├── JsonInspector.tsx                         ← viewer JSON inline (riusato)
│   ├── OutputDiffViewer.tsx                      ← diff JSON tra vN e vN-1
│   ├── VerificationForm.tsx                      ← il sotto-form della zona OUTPUT
│   ├── SkipStepDialog.tsx
│   ├── NuovaContestualizzazioneDialog.tsx        ← NEW r2 (§9.4)
│   ├── PendingDecisionBanner.tsx                 ← preservato da D5 §9
│   └── HumanDecisionDialog.tsx                   ← preservato da D5 §6 (varianti ridotte: solo step7_context_selection)
├── components/laboratorio/external-input-renderers/
│   ├── F3Step7InputRenderer.tsx                  ← contesto_ambito (step 7 della pipeline F3)
│   ├── F3Step10InputRenderer.tsx                 ← casi_stress_test
│   ├── GenericEnumInputRenderer.tsx              ← per severità/specificità
│   ├── GenericTextInputRenderer.tsx              ← fonti_web ecc.
│   └── JsonInputRenderer.tsx                     ← fallback
│   (NB: F2Step2InputRenderer eliminato — la scelta del tema avviene nell'archivio,
│    non più come input esterno della pipeline)
├── hooks/
│   ├── useIsAdmin.ts                             ← (preservato da D5 §1.2)
│   ├── usePipelineOrchestration.ts               ← (preservato da D5 §2, ma vedi nota)
│   ├── useExecutionLogs.ts                       ← (preservato da D5 §7)
│   ├── useLaboratorioFocus.ts                    ← NUOVO: gestisce focusedStepId/focusMode
│   ├── useLaboratorioPreferences.ts              ← NUOVO: persistenza localStorage
│   ├── useDispositiviTema.ts                     ← NEW r2: lista dispositivi figli + polling 15s
│   └── useTemaMadre.ts                           ← NEW r2: usato da LaboratorioDispositivoPage per il breadcrumb
├── services/
│   └── pipelineOrchestratorService.ts            ← preservato da D5 §11, esteso con metodi per
│                                                  dispositivi (createDispositivo, getDispositivo, ecc.)
└── types/
    └── pipeline.ts                               ← (esteso da D5 §13 — vedi §15 sotto)
```

**Nota su `usePipelineOrchestration`**: la firma cambia per supportare due tipi di pipeline. Da `useO({ temaId })` a:

```typescript
function usePipelineOrchestration(args:
  | { kind: 'tema'; temaId: string }
  | { kind: 'dispositivo'; temaId: string; contestoId: string }
): UsePipelineOrchestrationResult;
```

Internamente l'hook chiama `GET /api/pipeline/temi/:temaId` o `GET /api/pipeline/temi/:temaId/dispositivi/:contestoId` in base al kind. Lo `step_states` ricevuto contiene solo gli step della pipeline pertinente. Il filtraggio degli step da mostrare nella timeline usa il `phase` dello step (`'F2'` per la vista Tema, `'F3'` per la vista Dispositivo).

**Componenti di D5 da rimuovere** dal piano implementativo originale:
- `OrchestrationPanel.tsx` (sostituito da `LaboratorioShell` + `Workbench`)
- `StepList.tsx` / `StepRow.tsx` (sostituiti da `TimelineRail` + `TimelineRailItem`)
- `ExternalInputForm.tsx` come modal (sostituito da `ExternalInputPanel` inline + renderer)
- `ExecutionLogViewer.tsx` come drawer (sostituito da `LiveLogPanel` inline + `LiveLogPanelFullScreen`)
- `VerificationPanel.tsx` come modal (sostituito da `WorkbenchOutputPanel` + `VerificationForm` inline)

**Componenti di D5 preservati**:
- `useIsAdmin`, `useExecutionLogs`, `pipelineOrchestratorService` (esteso con metodi per dispositivi)
- `usePipelineOrchestration` (firma estesa — vedi nota sopra)
- `HumanDecisionDialog`, `PendingDecisionBanner` — spostati in `components/laboratorio/`. Le varianti di `HumanDecisionDialog` si riducono a `step7_context_selection` (la variante `f2_to_f3_tema_selection` viene **rimossa** dalle decisioni di pipeline — la creazione dei dispositivi avviene via `NuovaContestualizzazioneDialog`).
- `StepStatusBadge` — preservato in `components/pipeline/`, riusato dal `TimelineRail` (`TimelineRailItem` lo importa)

---

## 14. Hook nuovi

### 14.1 `useLaboratorioFocus`

```typescript
// client/src/hooks/useLaboratorioFocus.ts

interface UseLaboratorioFocusOptions {
  steps: StepConfig[];
  stepStates: Record<string, EnrichedStepState>;
  pendingDecision: HumanDecision | null;
  initialStepId?: string;     // dal route deep-link o da localStorage
}

interface UseLaboratorioFocusResult {
  focusedStepId: string;
  focusMode: 'auto' | 'manual';
  setFocusedStepId: (stepId: string) => void;   // → focusMode = 'manual'
  returnToFront: () => void;                     // → focusMode = 'auto', recompute
  computedFront: string;                         // sempre aggiornato (utile per pulsante)
}
```

Logica del fronte (vedi §3.3): pura funzione di `(steps, stepStates, pendingDecision)`. Da memoizzare con `useMemo`.

### 14.2 `useLaboratorioPreferences`

```typescript
// client/src/hooks/useLaboratorioPreferences.ts

interface LaboratorioPreferences {
  timelineCollapsed: boolean;
  lastFocusedByEntity: Record<string, string>;
}

function useLaboratorioPreferences(): {
  preferences: LaboratorioPreferences;
  setTimelineCollapsed: (v: boolean) => void;
  setLastFocused: (entityKey: string, stepId: string) => void;
  clearLastFocused: (entityKey: string) => void;
};
```

Persistenza in `localStorage` sotto la chiave `hcaire.laboratorio.preferences.v1`. Lettura sincrona al mount; scrittura debounced (300ms).

---

## 15. Estensioni di `types/pipeline.ts`

Da aggiungere a `client/src/types/pipeline.ts`:

```typescript
// Stati derivati per la presentazione del workbench

export type WorkbenchSection = 'input' | 'esecuzione' | 'output';

export interface PipelineInputResolution {
  satisfied: 'yes' | 'no' | 'pending_verifica';
  source_step_id: string;
  source_output_path: string | null;
  required_status: ExecutionStatus;
  current_status: ExecutionStatus;
}

export interface ExecutionSummary {
  execution_id: string;
  run_number: number;
  status: ExecutionStatus;
  started_at: string;
  ended_at: string | null;
  duration_ms: number | null;
}

export interface PrimaryActionDescriptor {
  label: string;
  variant: 'launch' | 'cancel' | 'verify' | 'relaunch' | 'decide' | 'view_logs' | 'compila_input' | 'goto_next' | 'goto_skipped' | 'none';
  disabled: boolean;
  disabledReason?: string;
}

export type SecondaryActionId =
  | 'skip'
  | 'view_run_history'
  | 'view_error_log'
  | 'request_6c_integration'
  | 'open_output_file'
  | 'copy_output_path'
  | 'rerun_with_extra_params'
  | 'unskip';

export interface SecondaryAction {
  id: SecondaryActionId;
  label: string;
  enabled: boolean;
}
```

---

## 16. Comportamenti trasversali

### 16.1 Selettori del fronte attivo (riepilogo)

Algoritmo da §3.3 implementato in una funzione pura testabile:

```typescript
// client/src/utils/laboratorioFront.ts

export function computeActiveFront(
  steps: StepConfig[],
  stepStates: Record<string, EnrichedStepState>,
  pendingDecision: HumanDecision | null,
): string {
  // 1. attende_decisione
  // 2. in_esecuzione
  // 3. in_coda
  // 4. in_verifica
  // 5. attende_input
  // 6. richiede_correzione | fallito
  // 7. action === 'launch'
  // 8. ultimo verificato/completato
  // (fallback: primo step)
}
```

Test unitari obbligatori per ciascuna delle 8 priorità.

### 16.2 Aggiornamento dopo un'azione

Quando `usePipelineOrchestration` esegue un'azione (`runStep`, `verifyExecution`, `submitExternalInput`, ecc.) e fa `refresh()`:

- `useLaboratorioFocus` ricalcola `computedFront`.
- Se `focusMode === 'auto'`: `focusedStepId = computedFront` (può cambiare).
- Se `focusMode === 'manual'`: `focusedStepId` resta invariato. Il pulsante "Torna al fronte attivo →" mostra un piccolo badge se `computedFront !== focusedStepId` (informa che c'è movimento altrove).

### 16.3 Auto-scroll all'interno del workbench

- Cambio di `focusedStepId`: scroll in cima al workbench.
- Click su "Vai alla verifica →" nel `LiveLogPanel`: scroll alla zona OUTPUT.
- Click su "Compila →" in INPUT/ESEC.: scroll all'input pertinente in INPUT con highlight breve.
- Cambio di `stepStates[focusedStepId].status` (es. da `in_esecuzione` a `completato`): scroll allineato sulla nuova UI prominente.

Implementare con `scrollIntoView({ behavior: 'smooth', block: 'start' })` su `ref` mirati. **Non** scrollare se l'utente è in interazione con un campo input.

### 16.4 Polling — invariato

La strategia di polling di D5 §10 resta valida: 5s quando `hasActiveSteps`, off altrimenti. SSE attivo solo quando `LiveLogPanel` è renderizzato (status `in_esecuzione` di `focusedStepId`).

### 16.5 Aggiornamento ottimistico — invariato

Le azioni eseguono prima un setStepStates ottimistico (es. `runStep` → `in_coda` immediato), poi chiamano l'API, poi `refresh()`. Identico a D5 §10.

---

## 17. Accessibilità

- **Tastiera**: tutti i controlli del workbench accessibili in tab order. Le frecce ↑/↓ navigano la timeline quando ha focus. Esc collassa pannelli inline (input form, ispettore JSON).
- **ARIA**:
  - `TimelineRail` → `role="navigation"` + `aria-label="Timeline pipeline"`.
  - Ogni `TimelineRailItem` → `role="button"` + `aria-current="step"` quando in focus.
  - `LiveLogPanel` → `role="log"` + `aria-live="polite"` (non assertivo, evitare overload screen-reader durante esecuzioni lunghe).
  - Tre zone del workbench → `role="region"` + `aria-labelledby` puntato all'header della zona.
- **Contrasto**: tutti i badge stato hanno colore + glifo + testo, mai colore-solo.
- **Modalità ridotta**: rispettare `prefers-reduced-motion` per pulse, smooth-scroll, espansioni di pannelli.

---

## 18. Responsiveness

| Breakpoint | Layout |
|---|---|
| `≥ 1280px` | Timeline 280px + Workbench 3 colonne affiancate |
| `1024–1279px` | Timeline collassabile a icone, Workbench 3 colonne strette |
| `768–1023px` | Timeline a icone (sempre), Workbench 3 tab orizzontali (`Input` / `Esecuzione` / `Output`) |
| `< 768px` | Timeline collassata in cassetto laterale (icona menu in TopBar), Workbench 3 tab |

Sotto `lg`, mostriamo un pulsante "▦ Timeline" nella TopBar che apre la timeline come `<Sheet>` (cassetto laterale).

---

## 19. Criteri di accettazione

Per dare per concluso il lavoro su questa spec, i seguenti criteri devono essere verificati. Sono raggruppati per area.

### 19.1 Routing e ingresso

- [ ] Le route `/laboratorio`, `/laboratorio/temi/:temaId`, `/laboratorio/temi/:temaId/dispositivi/:contestoId` esistono e sono raggiungibili.
- [ ] Le route deep-link a un singolo step (`.../step/:stepId`) funzionano sia per la vista Tema che per la vista Dispositivo: aprono la pagina con `focusedStepId = stepId` e `focusMode = 'manual'`.
- [ ] Utenti non admin che accedono a `/laboratorio/...` ricevono un redirect alla home (o un 403). Nessuna chiamata alle API admin viene fatta.
- [ ] La tab "Esegui" della `SviluppoBambinoPipelineDeviceOverview` non monta più `OrchestrationPanel`; mostra il CTA verso il Laboratorio appropriato (Tema o Dispositivo).
- [ ] La route `/laboratorio/temi/:temaId/dispositivi/:contestoId` con `temaId` o `contestoId` non esistente restituisce un 404 amichevole con CTA al `LaboratorioTemaPage` o all'index.

### 19.2 Timeline

- [ ] **Vista Tema**: la timeline mostra **solo** gli step F2 (`f2_step_2` → `f2_step_6` con sub-step canonici 2a, 4b). Lo step `f2_step_1` non appare.
- [ ] **Vista Dispositivo**: la timeline mostra **solo** gli step F3 (`f3_step_1` → `f3_step_10` con sub-step 6b, 6c).
- [ ] **Vista Tema**: quando `tema.stato === 'f2_verificata'`, la timeline mostra in coda la sezione "Contestualizzazioni F3" con i dispositivi figli e il pulsante "+ Nuova contestualizzazione".
- [ ] **Vista Dispositivo**: in cima alla timeline appare il blocco "Pre-requisiti F2 ✓" collassabile, che espande l'elenco read-only degli step F2 verificati con possibilità di ispezionarne l'output in overlay.
- [ ] Click su uno step la cambia di focus e setta `focusMode = 'manual'`.
- [ ] Sub-step (2a, 4b in F2; 6b, 6c in F3) sono visualmente annidati.
- [ ] La timeline è collassabile e la scelta è persistita in localStorage (chiave `hcaire.laboratorio.preferences.v2`).

### 19.3 Workbench — Header

- [ ] L'azione primaria è coerente con il `EnrichedStepState.action` (mappa di §11).
- [ ] Le azioni secondarie nel menu `⋯` sono filtrate in base al contesto (es. "Salta step…" appare solo se `step.can_skip === true`).

### 19.4 Workbench — INPUT panel

- [ ] Tutte le `inputs_pipeline` sono listate, ognuna con stato `✓` / `⋯` / `✗`.
- [ ] "Ispeziona" carica il JSON dell'output del passo dipendente e lo mostra in un viewer inline.
- [ ] Tutte le `inputs_strutturali` sono listate con link al file schema.
- [ ] Per ogni input esterno: se obbligatorio e mancante, badge ✎; se fornito, riepilogo + "Modifica"; se facoltativo non fornito, mostra default.
- [ ] Il form inline si espande sotto la card e si collassa a salvataggio o annullamento.
- [ ] Il form `f3_step_10` ha 5 sezioni con contatore "N/5 casi compilati".

### 19.5 Workbench — ESEC panel

- [ ] Stato A (lanciabile): pulsante grosso, checklist di pre-condizioni in verde.
- [ ] Stato B (bloccato): pulsante disabilitato, lista esplicita dei blocchi (deps + input).
- [ ] Stato C (in esecuzione): live log via SSE, auto-scroll, pulsante annulla.
- [ ] Stato D (concluso): banda di esito, run history (max 5), bottoni "Vedi log run #N" e "Rilancia".
- [ ] L'annullamento esecuzione fa POST corretto e aggiorna lo stato a `non_avviato` o `fallito` secondo D4.
- [ ] L'espansione full-screen del live log sovrappone la pagina ma non blocca il polling.

### 19.6 Workbench — OUTPUT panel

- [ ] Mostra "vuoto" coerente con la matrice §11 quando l'output non è disponibile.
- [ ] Per status `completato`/`in_verifica`/`verificato`: tre tab Anteprima / JSON / Diff con vN-1 (se v ≥ 2).
- [ ] Anteprima usa il componente corretto per tipo di step (vedi tabella in D5 §8).
- [ ] Il form di verifica è abilitato **solo** se `status === 'in_verifica'`.
- [ ] Submit verifica con outcome corretti; rilancio automatico in caso di "Richiede correzione" (lo step torna `richiede_correzione`, l'utente dà il "Rilancia").

### 19.7 Modali e atti deliberati

- [ ] `SkipStepDialog` chiede sempre una motivazione testuale.
- [ ] `HumanDecisionDialog` (§9.2) si apre dal banner e dall'azione primaria. Solo la variante `step7_context_selection` è attiva.
- [ ] `PendingDecisionBanner` è sticky e non dismissibile.
- [ ] `NuovaContestualizzazioneDialog` (§9.4) è raggiungibile **solo** quando `tema.stato === 'f2_verificata'`.
- [ ] `NuovaContestualizzazioneDialog` valida slug (kebab-case + univoco tra dispositivi-fratelli) prima del submit.
- [ ] Submit di `NuovaContestualizzazioneDialog` reindirizza alla `LaboratorioDispositivoPage` del nuovo dispositivo.

### 19.7-bis Sezione Contestualizzazioni (vista Tema)

- [ ] La sezione `ContestualizzazioniSection` appare nel `LaboratorioTemaPage` **solo** quando `tema.stato === 'f2_verificata'`.
- [ ] Nello stato vuoto mostra un CTA "+ Crea prima contestualizzazione".
- [ ] Le card dispositivo mostrano: contesto label, badge stato pipeline, N/10 step verificati, timestamp ultimo aggiornamento.
- [ ] Click su una card naviga al `LaboratorioDispositivoPage` del dispositivo.
- [ ] Il polling della lista dispositivi gira a 15s **solo se** almeno un dispositivo è in stato `in_corso`.

### 19.8 Comportamento auto-focus

- [ ] All'apertura del Laboratorio senza `lastFocusedByEntity`: focus su `computeActiveFront()`.
- [ ] All'apertura con `lastFocusedByEntity` valorizzato: focus su quello, `focusMode = 'manual'`.
- [ ] Cliccando "Torna al fronte attivo": `focusMode = 'auto'`, focus aggiornato, `lastFocusedByEntity` ripulito.
- [ ] Quando `focusMode === 'manual'` e il fronte cambia, il pulsante "Torna al fronte attivo" mostra un piccolo badge.

### 19.9 Test unitari minimi

- [ ] `computeActiveFront` — un test per ciascuna delle 8 priorità.
- [ ] Mapping `EnrichedStepState.action` → `PrimaryActionDescriptor.variant` — copertura completa di `StepAction`.
- [ ] `useLaboratorioPreferences` — lettura/scrittura/debouncing.
- [ ] Renderer di `WorkbenchInputPanel` per uno step con tutti i tre tipi di input.

### 19.10 No-regressioni

- [ ] Le pagine read-only esistenti (`PipelineMap`, `DeviceOverview`, ecc.) **non sono toccate** né nel layout né nei dati.
- [ ] Gli utenti non admin vedono esattamente la stessa esperienza di prima.
- [ ] Gli endpoint API esistenti non cambiano funzionalmente: dove serve (es. estensione di `GET /api/pipeline/index` con `dispositivi_summary`, nuove route per i dispositivi), i contratti sono additivi e versionati.

### 19.11 Modello a entità (r2)

- [ ] `LaboratorioTemaPage` carica `context` con **soli step F2**; nessun riferimento a step F3 nel suo `step_states`.
- [ ] `LaboratorioDispositivoPage` carica `context` con **soli step F3**; nessun riferimento a step F2 nel suo `step_states` (gli step F2 del tema madre sono caricati separatamente per il blocco read-only).
- [ ] Il vecchio flusso "decisione F2 → F3 di selezione tema" è **rimosso**: la selezione del tema avviene nell'archivio (separato), la creazione di un dispositivo F3 avviene via `NuovaContestualizzazioneDialog`.
- [ ] La firma di `usePipelineOrchestration` accetta sia `{ kind: 'tema', temaId }` sia `{ kind: 'dispositivo', temaId, contestoId }` e produce `stepStates` filtrati per la pipeline pertinente.
- [ ] La navigazione `LaboratorioTemaPage` → `LaboratorioDispositivoPage` (e viceversa via breadcrumb) preserva `focusMode = 'auto'` come default.

---

## 20. Roadmap implementativa consigliata

Sequenza in 8 tappe. Ogni tappa è completabile e dimostrabile in isolamento.

**Tappa 0 — Allineamento backend (prerequisito)**
- Migrazione del modello dati MongoDB: collezione `temi` con `stato` di vita; collezione `dispositivi_f3` con `(tema_id, contesto_id)`.
- Endpoint nuovi: `GET /api/pipeline/temi/:temaId/dispositivi`, `POST /api/pipeline/temi/:temaId/dispositivi`, `GET /api/pipeline/dispositivi/:dispositivoId`.
- Estensione di `GET /api/pipeline/index` con `dispositivi_summary` per ogni tema.
- Marcatura di `f2_step_1` come `excluded_from_pipeline_ui` in `pipeline-step-config.json` (oppure rimozione, da decidere).
- Backend deve esistere prima della Tappa 1, oppure mockare le risposte nel client durante lo sviluppo iniziale.

**Tappa 1 — Scheletro routing e index**
- Route `/laboratorio`, `/laboratorio/temi/:temaId`, `/laboratorio/temi/:temaId/dispositivi/:contestoId`. Pagine vuote, redirect anti-non-admin.
- `LaboratorioIndexPage` con il raggruppamento a tre sezioni (in F2 / F2 verificata con figli / parcheggiati).

**Tappa 2 — `LaboratorioShell` + TopBar + TimelineRail (read-only) — vista Tema**
- `LaboratorioShell` come layout container.
- `TopBar` variante Tema, `TimelineRail` variante `'tema'` (solo F2).
- `useLaboratorioFocus`, `useLaboratorioPreferences`. Persistenza minima.
- Non ancora azioni — solo navigazione e visualizzazione.

**Tappa 3 — Workbench scheletro + zona OUTPUT in lettura**
- `Workbench` con header + 3 zone vuote per MVP.
- `WorkbenchOutputPanel` per step verificati: tab Anteprima/JSON che riusa `DeviceViewer` ecc.
- Verifica end-to-end nella vista Tema: l'admin può navigare gli step F2 verificati e ispezionarne l'output.

**Tappa 4 — Zona INPUT (read-only) + ispezione**
- `WorkbenchInputPanel` con tutte le card (deps, strutturali, esterni).
- `JsonInspector` inline per "Ispeziona →" / "Visualizza schema →".
- Read-only delle external input già fornite.

**Tappa 5 — Lancio (Stato A) + Live log (Stato C) + Verifica + Skip**
- Pulsante "Lancia esecuzione" funzionante.
- `LiveLogPanel` con `useExecutionLogs` riusato. Annulla.
- `VerificationForm` nella zona OUTPUT.
- `SkipStepDialog`.
- A questo punto l'admin può eseguire end-to-end la pipeline F2 di un tema promosso.

**Tappa 6 — `ContestualizzazioniSection` + `NuovaContestualizzazioneDialog`**
- Sezione "Contestualizzazioni F3" come trailing del Workbench nella vista Tema.
- Modal di creazione dispositivo (§9.4) con validazione slug.
- Il workflow Tema → "+ Nuova contestualizzazione" → redirect a `LaboratorioDispositivoPage` è funzionante.

**Tappa 7 — `LaboratorioDispositivoPage` (vista Dispositivo)**
- Pagina `LaboratorioDispositivoPage` che monta lo stesso `LaboratorioShell` con variante Dispositivo.
- `TimelineRail` variante `'dispositivo'` (solo F3 + blocco "Pre-requisiti F2 ✓" collassabile).
- `useTemaMadre` per breadcrumb e overlay di ispezione F2.
- `HumanDecisionDialog` per `step7_context_selection`.
- `PendingDecisionBanner`.

**Tappa 8 — External input compilazione + raffinamenti**
- `ExternalInputPanel` + due renderer hardcoded (`F3Step7`, `F3Step10`) + tre generici (Enum, Text, Json).
- Diff con vN-1 nella zona OUTPUT.
- Auto-scroll mirati.
- Responsiveness < 1024px.

A ogni tappa: smoke-test manuale dei flussi A/B/C/D/E/F/G (§12) per quanto implementato. Test unitari su `computeActiveFront` e mapping stati dalla Tappa 2.

---

## 21. Note finali per Claude Code

1. **Estendere `usePipelineOrchestration` con la nuova firma a discriminator** (`{ kind: 'tema' | 'dispositivo', ... }`), ma non duplicare la logica di trasformazione `context + stepConfig + externalInputs → stepStates`. Le pagine `LaboratorioTemaPage` e `LaboratorioDispositivoPage` consumano e basta.

2. **Mantenere il riuso dei componenti di visualizzazione esistenti** (`DeviceViewer`, `StressTestDashboard`, `CorrectionsLog`, ecc.). La zona OUTPUT li importa, non li duplica.

3. **Una sola istanza di `usePipelineOrchestration` per pagina**. Mai chiamarla dentro componenti figli del workbench: passare i dati come props o via context.

4. **Context di pagina suggerito** (opzionale ma raccomandato per evitare prop drilling):

   ```typescript
   const LaboratorioContext = createContext<{
     orchestration: UsePipelineOrchestrationResult;
     focus: UseLaboratorioFocusResult;
     entity: { kind: 'tema' | 'ricerca'; id: string; label: string };
   } | null>(null);
   ```

5. **No `localStorage` dentro componenti**: solo in `useLaboratorioPreferences`. Rispetta la regola del progetto che vieta `localStorage` distribuito.

6. **Tailwind core only**: niente plugin custom. Usare design tokens esistenti del progetto.

7. **Quando in dubbio sul comportamento di un edge case**: comportarsi come la matrice §11. Se la matrice non copre il caso: aprire una issue / chiedere conferma. Non inventare comportamenti.

8. **Telemetria/logging**: non aggiungere chiamate a servizi di analytics. Eventuali log devono essere sotto `console.debug` con prefisso `[laboratorio]` e gated da `import.meta.env.DEV`.

9. **Strings literali in italiano**: nessun sistema di i18n richiesto a questo stadio. Centralizzare comunque le stringhe lunghe in un file `client/src/components/laboratorio/strings.ts` per facilitare future traduzioni.

10. **Relazione con `nuova-ricerca.md`**: la pagina di "Nuova ricerca" specificata in `webapp-hcaire/nuova-ricerca.md` veniva concepita come l'ingresso della pipeline F2 (avvio diretto di `f2_step_1`). Nel modello r2 quel ruolo è ribaltato: la "nuova ricerca" coincide con la **promozione di un tema dall'archivio**. Il documento `nuova-ricerca.md` **va aggiornato o ricondotto** all'archivio nel documento separato sull'archivio. Il `LaboratorioIndexPage` di r2 non ha un pulsante "+ Nuova ricerca" — ha un link "Apri archivio temi →".

---

## 22. Glossario

| Termine | Significato |
|---|---|
| Archivio temi | Collezione di temi candidati gestita fuori dal Laboratorio. Sorgente da cui un tema viene **promosso** a soggetto di RicercaF2. La sua UI è specificata in un documento separato. |
| Tema | Entità unica del progetto: identità del tema candidato (in archivio) + identità della RicercaF2 (in laboratorio). Cambia stato di vita ma non identità. |
| Tema (vista Laboratorio) | Stato di vita del tema in cui la pipeline F2 è in corso o completata. Pagina: `LaboratorioTemaPage`. |
| Promozione | Atto deliberato che fa transitare un tema candidato dall'archivio al Laboratorio (stato `promosso` → `f2_in_corso`). |
| Dispositivo F3 | Pipeline F3 contestualizzata di un tema in stato `f2_verificata`. Identità: `(tema_id, contesto_id)`. Pagina: `LaboratorioDispositivoPage`. |
| Contestualizzazione | Atto deliberato che crea un dispositivo F3 a partire da un tema con F2 verificata. Apre `NuovaContestualizzazioneDialog`. |
| Laboratorio | Le viste admin dedicate all'esecuzione delle pipeline F2 (vista Tema) o F3 (vista Dispositivo). |
| Workbench | Il pannello centrale del Laboratorio, focalizzato su un singolo step. Comune alle due viste. |
| Timeline (rail) | La rail verticale a sinistra. Variante `'tema'` mostra solo F2; variante `'dispositivo'` mostra solo F3 + Pre-requisiti F2. |
| Fronte attivo | Lo step calcolato dall'algoritmo §3.5 come "prossimo passo rilevante" della pipeline corrente. |
| Focus mode auto/manual | Stato della pagina che determina se il workbench segue il fronte o resta su uno step scelto dall'utente. |
| Zona INPUT/ESEC/OUTPUT | Le tre colonne fisse del Workbench. |
| Atto deliberato | Un'interazione che giustifica una modal: skip step, decisione umana strutturale (step 7), nuova contestualizzazione. |

---

**Fine documento.**

Per qualsiasi divergenza tra questo documento e D5 originale, **prevale questo documento** per le sezioni indicate al §0 ("Cosa sostituisce"). Per tutto il resto (data layer, polling, hook, service, tipi, integrazione Clerk admin), prevale D5.
