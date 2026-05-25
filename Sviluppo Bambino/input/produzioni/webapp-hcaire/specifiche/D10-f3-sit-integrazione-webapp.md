# D10 — Modulo F3-SIT — integrazione webapp — istruzioni per Claude Code

> **Destinatario**: Claude Code. Questo documento istruisce l'**integrazione nell'orchestrazione webapp** del modulo opzionale **F3-SIT** (Repertorio Situazionale di Micro-mediazioni), 4 step derivati da F3.
>
> **Leggere prima**: `D9-pipeline-f3-sit.md` — è la **specifica autoritativa** del modulo (statuto, grafo dei 4 step, tassonomia, schemi, wrapper, checklist). D10 non duplica D9: lo presuppone e lo traduce in istruzioni di codice. Per il contesto: `D1` (grafo, con la nota di revisione in testa), `D2` (macchina a stati/persistenza), `D7` (precedente: redesign F3 r3), `Storage dati e schemi pipeline.md` (persistenza).
>
> **Cosa modifica/aggiunge**:
> - aggiunge a `pipeline-step-config.json` 4 step `f3_sit_step_1…4` (fase `f3_sit`)
> - aggiorna `STEP_CLAUDE_FILE_MAP` del `PromptComposer` (4 nuovi path)
> - estende `evaluateStepEnablement` per la logica di **modulo opzionale** e per lo **skip** di `f3_sit_step_3`
> - estende `buildExecutionPlan` per il path template della sottocartella `sit/`
> - aggiunge (opzionale) un campo `sit_status` a `PipelineContext`
> - tocca `D5b` (timeline, form di verifica, viewer del repertorio)
>
> **Cosa NON modifica**: la pipeline F2; la pipeline F3 step 1–5; lo schema strutturale delle collezioni MongoDB; il protocollo Redis (`D3`); hook/service/polling/SSE del data layer (`D5`); l'output-tipo vuoto.
>
> **Migrazione dati esistenti**: nessuna. F3-SIT è puramente additivo. Nessuna esecuzione precedente da convertire.
>
> **Stato di preparazione (lato Cowork, già fatto)**:
> - ✅ Le 4 cartelle step `input/produzioni/f3-sit-step-1…4-*/` esistono con `CLAUDE.md` + `*-schema.json`; `f3-sit-step-1-…/verifica.md` presente.
> - ✅ Il file strutturale `input/produzioni/f3-sit-famiglie.json` (tassonomia 9 famiglie) esiste.
> - ✅ Un pilota manuale del modulo è stato eseguito e validato — vedi §9.5: utilizzabile come fixture di smoke test.
> - ❌ `pipeline-step-config.json` **non** contiene ancora gli step F3-SIT: è l'oggetto principale di questo documento.

---

## 1. Sintesi della modifica

### 1.1 Cosa è F3-SIT

F3-SIT è un **modulo derivato opzionale di Fase 3**. Si attiva *dopo* il completamento di `f3_step_5` (Output-tipo contestualizzato) e produce materiali situazionali e formativi (casistiche, frasi, schede di atteggiamento, vignette, linee guida, ecc.) derivati dal dispositivo F3 validato. Non tutti i dispositivi lo richiedono: per questo il modulo è **opzionale** e non prolunga la sequenza lineare obbligatoria di F3.

Statuto, motivazioni e dettaglio metodologico: `D9` §1–§2.

### 1.2 I 4 step del modulo

| ID | Label | Verifica umana | Skip | `output_prefix` |
|---|---|---|---|---|
| `f3_sit_step_1` | Selezione delle famiglie situazionali | **sì** | no | `sit-famiglie` |
| `f3_sit_step_2` | Generazione delle micro-mediazioni | no | no | `sit-micro-mediazioni` |
| `f3_sit_step_3` | Trasformazione formativa e narrativa | no | **sì** ¹ | `sit-formati` |
| `f3_sit_step_4` | Verifica e pacchetto repertorio | no ² | no | `sit-repertorio` |

¹ `f3_sit_step_3` è saltabile quando `f3_sit_step_1` produce `narrative_families_selected: false` (nessuna famiglia tra F3-SIT-6…9 selezionata). Vedi §3.5.
² La verifica di `f3_sit_step_4` *è* lo step (checklist C1–C8): nessun layer di verifica aggiuntivo.

Output di tutti gli step: in `output/produzioni/temi/<context_id>/sit/`. Naming **senza** suffisso `{dominio}` (`sit-famiglie-v{N}.json`, ecc.) — convenzione post-bridge confermata, coerente con F3 step 1–4.

---

## 2. `pipeline-step-config.json` — le 4 entry

Aggiungere 4 step al config. La forma di riferimento è in `D9` §8; qui la tabella sintetica e le regole vincolanti. **I nomi di campo esatti vanno verificati sul config v3.1 reale**: dove D9/D10 propongono un nome (`phase`, `optional_module`) che non esiste già, Claude Code valuti come rappresentare la stessa semantica con i campi disponibili.

| `step_id` | `depends_on` | `blocks` | `verifica` | `can_skip` | `output_prefix` |
|---|---|---|---|---|---|
| `f3_sit_step_1` | `f3_step_5` | `f3_sit_step_2` | true | false | `sit-famiglie` |
| `f3_sit_step_2` | `f3_sit_step_1` | `f3_sit_step_3`, `f3_sit_step_4` | false | false | `sit-micro-mediazioni` |
| `f3_sit_step_3` | `f3_sit_step_2` | `f3_sit_step_4` | false | true | `sit-formati` |
| `f3_sit_step_4` | `f3_sit_step_2`, `f3_sit_step_3` | — | false | false | `sit-repertorio` |

Regole vincolanti:

1. **Fase logica distinta.** I 4 step appartengono a una fase `f3_sit`, separata da `f2` e `f3`. Serve a tenerli isolati nella UI e nella macchina a stati. Se `pipeline-step-config.json` non ha un campo `phase`, introdurlo o usare l'equivalente già presente (prefisso `step_id`).
2. **Modulo opzionale — regola critica.** `f3_step_5` **non** deve elencare `f3_sit_step_1` nei propri `blocks`. `f3_sit_step_1` *dipende da* `f3_step_5` completato ma non ne è la prosecuzione dovuta: l'attivazione del modulo è un atto esplicito (vedi §3.1 e §4). Marcare i 4 step con un flag `optional_module: true` (o equivalente) così che il calcolo di "pipeline F3 completa" non li includa.
3. **`inputs_pipeline`** per ogni step: vedi tabella §5 di `D9`. Il backend risolve i path da `step_states[<dep>].output_file` come per ogni altro step (`Storage dati e schemi` §1.4). `f3_sit_step_4` dichiara `f3_step_4` (coerenza) tra gli input come **opzionale**: nel pilota `coerenza-v1.json` poteva mancare (vedi §9, domanda 5).
4. **`inputs_strutturali`** per ogni step: il proprio `*-schema.json` + `f3-sit-famiglie.json` (almeno per `f3_sit_step_1`).
5. **`inputs_esterni`**: solo `f3_sit_step_1` ne ha uno, `destinazione_uso`, di tipo `esterno_facoltativo` (vedi §3.3).
6. **`output_path_template`**: `temi/{context_id}/sit/{output_prefix}-v{N}.json` (vedi §3.2).
7. **`_version`**: bump del config quando si aggiungono gli step.

Skeleton della prima entry (le altre 3 per analogia — dettaglio in `D9` §8):

```jsonc
{
  "step_id": "f3_sit_step_1",
  "phase": "f3_sit",
  "label": "Selezione delle famiglie situazionali",
  "optional_module": true,
  "depends_on": ["f3_step_5"],
  "blocks": ["f3_sit_step_2"],
  "inputs_pipeline": [
    { "role": "output-tipo-contestualizzato", "from_step": "f3_step_5" },
    { "role": "nodo-funzione",  "from_step": "f3_step_1" },
    { "role": "micro-dispositivo", "from_step": "f3_step_2" },
    { "role": "stress-test", "from_step": "f3_step_3", "optional": true }
  ],
  "inputs_strutturali": [
    "f3-sit-step-1-selezione-famiglie/sit-famiglie-schema.json",
    "f3-sit-famiglie.json"
  ],
  "inputs_esterni": [
    { "input_id": "destinazione_uso", "type": "esterno_facoltativo" }
  ],
  "output_prefix": "sit-famiglie",
  "output_path_template": "temi/{context_id}/sit/sit-famiglie-v{N}.json",
  "verifica": true,
  "can_skip": false
}
```

---

## 3. Modifiche al backend di orchestrazione

### 3.1 `evaluateStepEnablement` — logica di modulo opzionale

`f3_sit_step_1` va abilitato (`enabled`) quando `f3_step_5` è in stato `completato`/`verificato`, ma **non** auto-avviato e **non** conteggiato nel completamento della pipeline F3. Concretamente:

- gli step `f3_sit_*` entrano nel calcolo di enablement solo se il modulo è stato attivato (campo `sit_status.enabled` — §4 — oppure presenza di almeno una `PipelineStepExecution` con `step_id` `f3_sit_*`);
- il completamento di `f3_step_5` **non** rende la pipeline "incompleta" per il fatto che gli `f3_sit_*` non siano stati eseguiti;
- una volta attivato il modulo, gli `f3_sit_*` seguono l'enablement lineare ordinario sui propri `depends_on`.

Diversamente da `D7` §4.2, qui non c'è biforcazione del grafo: solo un ramo opzionale che pende da `f3_step_5`.

### 3.2 `buildExecutionPlan` — path della sottocartella `sit/`

Gli output F3-SIT vanno in `temi/<context_id>/sit/`. Verificare in `pipelineController.buildExecutionPlan` come è risolta oggi la variabile di cartella del tema (per F3 è `temi/{tema_id|context_id}/`) e replicare il meccanismo aggiungendo il livello `sit/`. Il worker deve creare la sottocartella `sit/` se assente. **Non** è richiesta la risoluzione della variabile `{dominio}` nel path (a differenza di `f3_step_5`): la convenzione F3-SIT non usa `{dominio}` nel filename.

### 3.3 Input esterno `destinazione_uso` (`f3_sit_step_1`)

`f3_sit_step_1` ha un input esterno **facoltativo** `destinazione_uso` (destinatari e uso previsto del materiale). Coerentemente con `f3_step_1.contesto_ambito` e con `Storage dati e schemi` §3.1, **non materializzare** un file `external-input-schemas/*.json`: lo schema del payload `data` è descritto nel `CLAUDE.md` di `f3_sit_step_1` (sez. B) e va validato lato server alla ricezione via `postStepInput`. Se assente, lo step procede sui soli input pipeline.

### 3.4 `PromptComposer` — `STEP_CLAUDE_FILE_MAP`

Aggiungere alla mappa (server locale Cowork, `D6` §1) i 4 path:

| Step ID | Path (relativo a `input/produzioni/`) |
|---|---|
| `f3_sit_step_1` | `f3-sit-step-1-selezione-famiglie/CLAUDE.md` |
| `f3_sit_step_2` | `f3-sit-step-2-micro-mediazioni/CLAUDE.md` |
| `f3_sit_step_3` | `f3-sit-step-3-formati-formativi/CLAUDE.md` |
| `f3_sit_step_4` | `f3-sit-step-4-repertorio/CLAUDE.md` |

Nessuna gestione speciale: gli step F3-SIT non hanno `CLAUDE-B.md` né blocchi tipo `MICRO CASI`. L'input esterno `destinazione_uso`, quando presente, va passato come blocco di input strutturato uniforme agli altri input esterni.

### 3.5 Skip di `f3_sit_step_3`

`f3_sit_step_3` ha `can_skip: true`. La `skip_condition`: l'output di `f3_sit_step_1` (`sit-famiglie-v{N}.json`) ha `results[0].narrative_families_selected === false`. `evaluateStepEnablement` (o il punto in cui si valutano le skip condition) deve leggere quel campo dall'`output_data` mirrorato di `f3_sit_step_1`. Lo skip va registrato esplicitamente in `step_states` → `steps_skipped` con motivazione, come da `D1` ("Step saltabili"). Se lo step 3 è saltato, `f3_sit_step_4` procede senza l'input `sit-formati` (che dichiara quindi come opzionale).

### 3.6 Verifica umana di `f3_sit_step_1`

`f3_sit_step_1` ha `verifica: true`. Riusa il meccanismo esistente: a completamento, lo step va in `in_verifica` e passa a `verificato` solo dopo conferma esplicita dell'operatore (`VerificaOutcome` `approvato` / `richiede_correzione`). Nessun nuovo tipo di esito. La cartella dello step contiene `verifica.md` (protocollo V1–V7) che orienta la diagnosi. È l'**unica** verifica umana del modulo.

### 3.7 MongoDB — nessuna modifica strutturale

Gli step `f3_sit_*` sono normali `PipelineStepExecution` (`context_id` + `step_id` + `run_number`). L'`output_data` viene mirrorato dall'evento `completed` come per ogni altro step. Nessuna nuova collezione, nessun nuovo indice. L'unica estensione di modello è il campo facoltativo `sit_status` su `PipelineContext` (§4).

---

## 4. Macchina a stati

Il modulo va tracciato senza interferire con la sequenza lineare di F3. Due opzioni (`D9` §9):

- **Opzione A (raccomandata)** — campo dedicato `sit_status` in `PipelineContext`:
  ```jsonc
  "sit_status": { "enabled": false, "current_step": null, "publication_ready": false }
  ```
  `enabled` → `true` quando `f3_step_5` è completato *e* il ricercatore attiva il modulo; `current_step` segue l'avanzamento; `publication_ready` → `true` quando `f3_sit_step_4` produce `methodological_status = "validato"`.
- **Opzione B** — riuso di `step_states` con i nuovi `step_id`, ignorando quelli non avviati. Meno codice, ma mescola modulo opzionale e sequenza obbligatoria.

Raccomandazione: **Opzione A**, coerente con lo statuto di modulo derivato opzionale e con la separazione di fase. Decisione finale di Claude Code in base a `D2`.

---

## 5. Frontend (`D5b`)

Aggiornare `D5b-laboratorio-workbench.md` e l'implementazione:

1. **TimelineRail — ramo F3-SIT.** Dopo le 5 voci F3, aggiungere un blocco opzionale F3-SIT, visivamente distinto (collassato finché il modulo non è attivato), con le 4 voci `f3_sit_step_1…4`. Lo step 3 mostra il glifo di "saltabile"; lo step 1 il glifo di verifica umana.
2. **Attivazione del modulo.** Un'azione esplicita ("Avvia repertorio situazionale F3-SIT") disponibile quando `f3_step_5` è completato. È ciò che porta `sit_status.enabled` a `true`.
3. **Form di verifica di `f3_sit_step_1`.** Riusa il pattern di verifica umana esistente (come `f3_step_1…3`); il contenuto da verificare è la selezione delle famiglie. Non è una `HumanDecisionDialog` modale: è una verifica di step.
4. **Renderer dell'input esterno `destinazione_uso`** — facoltativo: pochi campi liberi (vedi `CLAUDE.md` di `f3_sit_step_1` sez. B). Pattern uniforme agli altri `ExternalInputPanel`.
5. **Viewer del repertorio.** Un `RepertorioViewer` per `sit-repertorio-v{N}.json` sarebbe utile (item per famiglia, stato C1–C8, raccomandazione di pubblicazione). **Per la prima implementazione il fallback "JSON pretty-printed" è sufficiente** per tutti e 4 gli step F3-SIT; i viewer specifici sono posticipabili.

---

## 6. Cosa NON cambia

- **Pipeline F2 e F3 step 1–5**: invariate. F3-SIT è puramente additivo.
- **Output-tipo contestualizzato** (`f3_step_5`): è e resta l'input primario di F3-SIT. Nessuna modifica al suo schema.
- **Schema strutturale delle collezioni** `pipeline_contexts`, `pipeline_step_executions`, `pipeline_external_inputs`: nessuna modifica (solo l'aggiunta facoltativa del campo `sit_status` al documento di contesto).
- **Protocollo Redis (`D3`)**: invariato.
- **Hook, service, polling, SSE del data layer (`D5`)**: invariati.

---

## 7. Sequenza di rilascio consigliata

**Tappa 0 — Filesystem (già fatto)**
0. ✅ Le 4 cartelle `input/produzioni/f3-sit-step-*/` con `CLAUDE.md` + schema e il file `f3-sit-famiglie.json` esistono già. Verificare solo che siano presenti.

**Tappa 1 — Config e backend (atomica)**
1. Aggiungere i 4 step `f3_sit_*` a `pipeline-step-config.json` (§2); bump `_version`.
2. Estendere `evaluateStepEnablement` con la logica di modulo opzionale (§3.1) e la `skip_condition` di `f3_sit_step_3` (§3.5).
3. Estendere `buildExecutionPlan` per il path `temi/<context_id>/sit/` (§3.2).
4. Aggiornare `STEP_CLAUDE_FILE_MAP` del `PromptComposer` con i 4 path (§3.4).
5. Aggiungere la validazione server-side del payload `destinazione_uso` in `postStepInput` (§3.3).

**Tappa 2 — Macchina a stati**
6. Aggiungere il campo `sit_status` a `PipelineContext` (§4, opzione A) e i punti che lo aggiornano.

**Tappa 3 — Frontend D5b**
7. Aggiornare la `TimelineRail` con il ramo F3-SIT opzionale (§5.1).
8. Implementare l'azione di attivazione del modulo (§5.2) e il form di verifica di `f3_sit_step_1` (§5.3).
9. Renderer di `destinazione_uso` (§5.4); mapping output → preview con fallback JSON (§5.5).

**Tappa 4 — Smoke test end-to-end**
10. Su un tema con F3 completo, attivare il modulo ed eseguire `f3_sit_step_1 → 4`, verificando che ogni step accetti gli input e produca output validati dai 4 schemi.
11. Verificare il caso di skip: una selezione senza famiglie narrative (`narrative_families_selected: false`) deve saltare `f3_sit_step_3` e far procedere `f3_sit_step_4`.
12. Confrontare gli output con la fixture del pilota manuale (§10).

---

## 8. Criteri di accettazione

### 8.1 Config e backend

- [ ] `pipeline-step-config.json` contiene esattamente 4 step `f3_sit_step_1…4` con `phase`/prefisso `f3_sit`
- [ ] `f3_step_5.blocks` **non** contiene `f3_sit_step_1` (modulo opzionale)
- [ ] I 4 step sono marcati come modulo opzionale (`optional_module: true` o equivalente) e non entrano nel completamento della pipeline F3
- [ ] `f3_sit_step_1.verifica === true`; `f3_sit_step_3.can_skip === true` con `skip_condition` valorizzata
- [ ] `output_path_template` dei 4 step punta a `temi/{context_id}/sit/…`
- [ ] `STEP_CLAUDE_FILE_MAP` contiene i 4 path `f3-sit-step-*/CLAUDE.md`
- [ ] `evaluateStepEnablement` abilita `f3_sit_step_1` solo dopo `f3_step_5` completato e non auto-avvia il modulo

### 8.2 Esecuzione

- [ ] Lanciando `f3_sit_step_1`, l'agente riceve `f3-sit-step-1-selezione-famiglie/CLAUDE.md` e il file strutturale `f3-sit-famiglie.json`
- [ ] L'output di ogni step F3-SIT è validato dal rispettivo `*-schema.json`
- [ ] Gli output sono scritti in `output/produzioni/temi/<context_id>/sit/` e mirrorati in `PipelineStepExecution.output_data`
- [ ] `f3_sit_step_1` va in `in_verifica` e procede solo dopo `approvato`
- [ ] Se `narrative_families_selected === false`, `f3_sit_step_3` è saltato (registrato in `steps_skipped`) e `f3_sit_step_4` procede comunque
- [ ] `f3_sit_step_4` gestisce l'assenza di `coerenza-v1.json` (`f3_coherence_status: null`)

### 8.3 Stato e frontend

- [ ] `sit_status` (o equivalente) traccia attivazione, step corrente, `publication_ready`
- [ ] La `TimelineRail` mostra il ramo F3-SIT opzionale solo dopo `f3_step_5` completato
- [ ] La verifica di `f3_sit_step_1` usa il pattern di verifica di step, non una decisione modale

### 8.4 No-regressioni

- [ ] Le pipeline F2 e F3 (step 1–5) eseguono identicamente; un tema senza F3-SIT è considerato completo dopo `f3_step_5`
- [ ] Nessuna modifica al protocollo Redis né al data layer D5

---

## 9. Domande aperte da chiarire prima dell'implementazione

1. **Rappresentazione dell'opzionalità nel config.** `pipeline-step-config.json` v3.1 ha già un modo di marcare uno step come opzionale/fuori dalla sequenza (cfr. `f2_step_1.excluded_from_pipeline_ui`, `f3_step_5.can_skip` nel vecchio modello)? Se sì, riusarlo; se no, introdurre `optional_module`. Decisione di Claude Code sulla base del config reale.
2. **`sit_status` vs `step_states`** (§4): opzione A o B. Raccomandata A.
3. **Viewer specifici vs fallback JSON** (§5.5): per la prima implementazione il fallback JSON è accettabile? I viewer (`RepertorioViewer`, ecc.) sono posticipabili a una tappa successiva?
4. **Modalità DRAFT.** `D9` §11 nota 3 prevede una possibile v2 con innesto anticipato dopo `f3_step_2`. Confermare che l'integrazione v1 implementa **solo** l'innesto FINAL dopo `f3_step_5` (raccomandato).
5. **`coerenza-v1.json` assente.** Nel pilota lo `f3_step_4` (coerenza) non era presente nella cartella del tema. `f3_sit_step_4` deve trattare quell'input come **opzionale** e registrare `f3_coherence_status: null`. Va inoltre chiarito, sul piano della pipeline F3, se `coerenza-v1.json` debba sempre esistere a valle di `f3_step_4`: è una pendenza F3, non F3-SIT, ma impatta la raccomandazione di pubblicazione del repertorio.
6. **Riallineamento di `D1`.** La §3 di `D1` è ancora pre-r3 (vedi nota di revisione in testa a `D1`). Il riallineamento completo di `D1` alla pipeline r3 + modulo F3-SIT resta una pendenza tecnica separata, indipendente da questa integrazione.

---

## 10. Fixture di smoke test — pilota manuale già disponibile

Un pilota completo del modulo è stato eseguito manualmente sul tema × dominio **`gioco-libero-come-incontro-del-bambino-con-il-possibile--clinico-pediatrico`**. In `output/produzioni/temi/<context_id>/sit/` sono presenti i 4 output validati:

- `sit-famiglie-v1.json` — 5 famiglie selezionate (`narrative_families_selected: true`)
- `sit-micro-mediazioni-v1.json` — 14 item
- `sit-formati-v1.json` — 5 training_outputs
- `sit-repertorio-v1.json` — 19 item verificati, `methodological_status: validato`

Claude Code può usarli come **output attesi di riferimento** per lo smoke test della Tappa 4: rieseguendo il modulo via orchestrator sullo stesso tema, gli output prodotti devono avere la stessa struttura e validare contro i medesimi schemi. Il diario del pilota è in `temi/<context_id>/revisioni.md`.

---

*Fine documento — D10, integrazione webapp del modulo F3-SIT, 2026-05-23.*
