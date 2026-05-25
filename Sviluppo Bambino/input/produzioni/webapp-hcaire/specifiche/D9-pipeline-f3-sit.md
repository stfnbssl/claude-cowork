# D9 — Modulo F3-SIT — specifica architetturale

> **Scopo del documento.** Definire in modo esplicito e machine-readable il **modulo F3-SIT** (Repertorio Situazionale di Micro-mediazioni): statuto, collocazione nella pipeline, grafo dei 4 step, input/output, tassonomia, verifiche, innesto in `pipeline-step-config.json`. È la sorgente di verità per la costruzione degli step (Fase 2 del piano) e per l'integrazione webapp (Fase 5).
>
> **Destinatario**: l'esecutore della pipeline (costruzione dei `CLAUDE.md` degli step) e Claude Code (orchestrazione e config). Leggere prima `D1` (grafo step), `D7`+`D8` (pipeline F3 corrente), `Storage dati e schemi pipeline.md` (persistenza e schemi).
>
> **Data**: 2026-05-23 · **Stato**: specifica iniziale (v1) · **Decisioni di riferimento**: `Piano di attuazione F3-SIT.md` §3, decisioni D-a … D-g approvate dal ricercatore.
>
> **Riferimenti**: `Brainstorming chatGPT per estensione output pipeline.md` (Q&A 2–4) · `pipeline-produzioni-documentazione-cowork.md` · `Storage dati e schemi pipeline.md` · `D1`, `D7`, `D8`.

---

## 1. Cosa è F3-SIT e perché

F3-SIT — **Repertorio Situazionale di Micro-mediazioni** — è il ramo della Fase 3 dedicato alla produzione di materiali situazionali, esemplificativi e formativi derivati dalla lettura configurazionale del campo: casistiche, frasi per operatori e caregiver, schede di atteggiamento, micro-scenari, vignette, storyboard, linee guida narrative, prompt per AI generativa.

F3-SIT **non sostituisce** la Configurazione Evolutiva, l'output-tipo contestualizzato o il micro-dispositivo. Li rende *visibili, comunicabili e trasferibili* attraverso forme situate e narrative. Dove F3 produce la grammatica del metodo (cosa *fare* al campo, come *leggere* il campo), F3-SIT la rende mostrabile: una scena, una frase, un atteggiamento, una micro-azione.

**Il rischio strutturale** del modulo è la deriva verso la manualistica educativa ("cosa dire / cosa fare"). La difesa è architetturale, non solo redazionale: F3-SIT parte sempre da un **dispositivo F3 validato**, mai dal solo tema; ogni item prodotto porta i **campi di tracciabilità** (§5); la **checklist C1–C8** (§6) rigetta gli item prescrittivi.

### 1.1 Statuto

F3-SIT è una **sotto-articolazione opzionale di Fase 3**, non una nuova fase e non un allungamento della sequenza lineare F3. È un **modulo derivato**: si attiva *dopo* il completamento di F3, solo quando il dominio richiede materiali comunicativi. Non tutti i dispositivi F3 lo richiedono (un dominio "supervisione professionale" o "politiche" può non attivare alcuna famiglia narrativa) — perciò il modulo non è obbligatorio e non blocca la pipeline F3.

---

## 2. Collocazione nella pipeline e abilitazione

```
F2 (7 step) → [decisione umana: tema × dominio] → F3 (5 step)
                                                      ↓
                                          f3_step_5 completato
                                                      ↓
                                          ┌─── modulo F3-SIT (opzionale) ───┐
                                          │  f3_sit_step_1                  │
                                          │      ↓ (verifica umana)         │
                                          │  f3_sit_step_2                  │
                                          │      ↓                          │
                                          │  f3_sit_step_3  (saltabile)     │
                                          │      ↓                          │
                                          │  f3_sit_step_4                  │
                                          └─────────────────────────────────┘
```

**Condizione di abilitazione**: il modulo F3-SIT diventa eseguibile quando `f3_step_5` è `completato`. Poiché il modulo è opzionale, `f3_step_5` **non** elenca `f3_sit_step_1` tra i propri `blocks`: l'abilitazione è una *possibilità*, non un passaggio dovuto. L'attivazione del modulo è un atto esplicito del ricercatore.

**Una pipeline F3-SIT = un tema × un dominio.** Come F3, F3-SIT lavora su un solo `context_id` (`<theme_id>--<ambito_id>`). Il dominio è quello già scelto in F3 step 1; F3-SIT non lo ridefinisce.

> **Decisione D-c.** La modalità DRAFT (innesto anticipato dopo F3 step 2) è **rimandata a una v2** del modulo. La v1 qui specificata prevede solo l'innesto FINAL dopo `f3_step_5`.

---

## 3. Grafo dei 4 step

Convenzioni di tipo input ereditate da `D1`: `pipeline` (file prodotto da uno step precedente), `strutturale` (file di metodo statico), `esterno_obbligatorio` / `esterno_facoltativo` (dato del ricercatore).

Per gli input `pipeline` il path concreto **non va hard-codato**: il backend lo deriva da `step_states[<dep>].output_file` del `PipelineContext` (cfr. `Storage dati e schemi pipeline.md` §1.4). D9 dichiara quindi le dipendenze per `step_id`, non per nome di file.

### f3_sit_step_1 — Selezione delle famiglie situazionali

**Funzione**: decidere quali delle 9 famiglie F3-SIT (§4) sono pertinenti per il tema × dominio, con priorità e destinatario di ciascuna. Non tutti i dispositivi generano tutte le famiglie: per un dominio clinico può essere centrale il repertorio di frasi per operatori; per un dominio scuola la vignetta formativa; per un dominio genitoriale le frasi caregiver e i micro-scenari. Lo step **non produce ancora materiale**: produce la mappa di ciò che va prodotto.

**Input**:
- `pipeline` `output-tipo-contestualizzato` ← `f3_step_5`
- `pipeline` `nodo-funzione` ← `f3_step_1`
- `pipeline` `micro-dispositivo` ← `f3_step_2`
- `pipeline` `stress-test` ← `f3_step_3` *(facoltativo: usato per stimare la pertinenza della famiglia "casistiche")*
- `strutturale` `f3-sit-famiglie` ← `f3-sit-famiglie.json` (tassonomia delle 9 famiglie)
- `esterno_facoltativo` `destinazione_uso`: indicazione del ricercatore su destinatari e uso previsto (formazione operatori, orientamento genitori, sito, schede pratiche). Schema **descritto nel `CLAUDE.md`**, non materializzato (decisione D-g).

**Output**: `sit-famiglie-v{N}.json`

**Verifica umana**: ✅ **obbligatoria**. È il punto in cui il ricercatore decide la destinazione comunicativa del materiale; una scelta sbagliata qui propaga su tutto il modulo.

**Skip**: no.

### f3_sit_step_2 — Generazione delle micro-mediazioni

**Funzione**: produrre gli item delle **famiglie 1–5** selezionate (casistiche situazionali, frasi per operatori, frasi per caregiver, schede di atteggiamento, micro-scenari). Ogni item è ancorato a nodo dominante, funzione e tipo universale del dispositivo.

**Input**:
- `pipeline` `sit-famiglie` ← `f3_sit_step_1`
- `pipeline` `micro-dispositivo` ← `f3_step_2`
- `pipeline` `stress-test` ← `f3_step_3`

**Output**: `sit-micro-mediazioni-v{N}.json`

**Verifica umana**: facoltativa (raccomandata se il materiale è destinato a pubblicazione).

**Skip**: no (se il modulo è attivo, almeno una famiglia 1–5 è quasi sempre selezionata; se nessuna lo fosse, lo step produce un `items` vuoto e lo registra).

> **Connessione con lo stress test ("connessione B").** I 5 casi tipologici di `f3_step_3` (`assenza_configurazione`, `configurazione_parziale`, `configurazione_distorta_chiudente`, `configurazione_oscillante`, `configurazione_apparente_indistinguibile`) sono la **base privilegiata** della famiglia F3-SIT-1 (casistiche situazionali): sono già "sotto modello" e non vanno reinventati. Lo step 2 li converte in casistiche formative anziché generarne di nuove.

### f3_sit_step_3 — Trasformazione formativa e narrativa

**Funzione**: produrre gli item delle **famiglie narrative 6–9** selezionate (vignette formative, storyboard per fumetto/video, linee guida narrative, prompt per AI generativa), trasformando le micro-mediazioni dello step 2 in materiali comunicativi.

**Input**:
- `pipeline` `sit-famiglie` ← `f3_sit_step_1`
- `pipeline` `sit-micro-mediazioni` ← `f3_sit_step_2`
- `pipeline` `stress-test` ← `f3_step_3` *(facoltativo)*

**Output**: `sit-formati-v{N}.json`

**Verifica umana**: facoltativa (dipende dalla destinazione: se il materiale va sul sito o in formazione, raccomandata).

**Skip**: ✅ **saltabile**. `skip_condition`: `f3_sit_step_1` non ha selezionato alcuna famiglia tra F3-SIT-6, 7, 8, 9. Lo skip va registrato esplicitamente con motivazione in `revisioni.md` e in `step_states.steps_skipped` (sul modello dello skip già previsto in `D1`).

### f3_sit_step_4 — Verifica e pacchetto repertorio

**Funzione**: applicare la checklist di coerenza F3-SIT (§6) a tutti gli item prodotti, assegnare lo stato metodologico e produrre il **pacchetto repertorio finale** — l'output utilizzabile da sito, materiali formativi, prompt per fumetti/video, schede per operatori o genitori.

**Input**:
- `pipeline` `sit-micro-mediazioni` ← `f3_sit_step_2`
- `pipeline` `sit-formati` ← `f3_sit_step_3` *(assente se lo step 3 è stato saltato)*
- `pipeline` `coerenza` ← `f3_step_4` *(per ereditare l'esito di coerenza del dispositivo sorgente)*

**Output**: `sit-repertorio-v{N}.json`

**Verifica umana**: no — la verifica *è* lo step (come `f3_step_4`).

**Verdetto** (`methodological_status`): `validato` / `richiede_revisione` / `non_pubblicabile`.

**Skip**: no.

---

## 4. Tassonomia delle 9 famiglie F3-SIT

Materializzata nel file strutturale `f3-sit-famiglie.json` (input `strutturale` di `f3_sit_step_1`). I `family_id` sono stabili e non vanno rinominati.

| `family_id` | Nome | Uso principale | Prodotta da | Famiglia narrativa |
|---|---|---|---|---|
| `F3-SIT-1` | Casistiche situazionali | Riconoscere configurazioni di campo | step 2 | no |
| `F3-SIT-2` | Frasi per operatori | Colloquio con genitori o altri adulti | step 2 | no |
| `F3-SIT-3` | Frasi per caregiver | Interazione adulto–bambino | step 2 | no |
| `F3-SIT-4` | Schede di atteggiamento adulto | Postura, tono, timing, tipo di presenza | step 2 | no |
| `F3-SIT-5` | Micro-scenari situazionali | Sequenze brevi di campo | step 2 | no |
| `F3-SIT-6` | Vignette formative | Formazione e supervisione | step 3 | **sì** |
| `F3-SIT-7` | Storyboard fumetto/video | Materiali comunicativi visivi | step 3 | **sì** |
| `F3-SIT-8` | Linee guida narrative non prescrittive | Orientamento divulgativo o professionale | step 3 | **sì** |
| `F3-SIT-9` | Prompt per AI generativa | Produzione assistita di materiali | step 3 | **sì** |

La colonna "famiglia narrativa" determina la `skip_condition` di `f3_sit_step_3`: lo step 3 si esegue solo se almeno una famiglia tra 6–9 è selezionata.

> **Statuto della tassonomia**: le 9 famiglie sono una **proposta da validare**. Vanno trattate come ipotesi finché il pilota (Fase 4 del piano, su `pointing`) non le conferma. Alcune potrebbero risultare ridondanti o mancanti: la correzione di `f3-sit-famiglie.json` dopo il pilota è prevista e legittima.

### 4.1 Relazione con le famiglie di output F2 e la tipologia U1–U6

F3-SIT non inventa nuove finalità: specifica forme concrete dentro famiglie già previste da F2 (`output-family`). Mappatura orientativa:

| Famiglia F2 (`output-family`) | Traduzione F3-SIT |
|---|---|
| Osservativa | casistiche situazionali (F3-SIT-1), vignette di lettura (F3-SIT-6) |
| Formativa | schede, storyboard, vignette, prompt AI (F3-SIT-4/6/7/9) |
| Accompagnamento | frasi per operatori/caregiver, atteggiamenti, micro-scenari (F3-SIT-2/3/4/5) |

Ogni item resta inoltre ancorato alla **Tipologia Universale U1–U6** del dispositivo sorgente (campo `universal_device_type`, §5): è ciò che impedisce a F3-SIT-2/3 di degradare in "liste di frasi belle" — ogni frase ha una funzione di dispositivo.

---

## 5. Wrapper di output e campi di tracciabilità

Gli output F3-SIT mantengono il **wrapper single-tema** della pipeline post-v3.0:

```jsonc
{
  "step": "f3_sit_step_N",
  "tema_id": "<slug>",
  "domain_selected": "clinico | educativo | formazione | politiche",
  "results": [ { /* esattamente 1 elemento */ } ]
}
```

`results` ha sempre `minItems=1, maxItems=1`. **Le famiglie multiple e i loro item non sono `results` multipli**: stanno in sotto-array dentro `results[0]` (es. `results[0].items[]`, `results[0].selected_families[]`).

**Campi di tracciabilità obbligatori per ogni item** prodotto dagli step 2, 3, 4. Un item privo di questi campi è materiale narrativo scollegato dal metodo e va rigettato dalla checklist:

```jsonc
{
  "source_device_id": "...",                  // dispositivo F3 sorgente
  "dominant_node": "N1..N7",                   // da nodo-funzione → results[0].dominant_node.node_id
  "function": "stabilizzare|ampliare|mediare|proteggere",  // da nodo-funzione → function.function_type
  "target_field": "...",                       // da nodo-funzione → target_field.field_label
  "universal_device_type": ["U1".."U6"],       // da micro-dispositivo → universal_form.forms[]
  "family_id": "F3-SIT-1..9",
  "methodological_warnings": []
}
```

`theme_id` e `domain_selected` stanno già nel wrapper e non vanno ripetuti per item. La catena di ereditarietà (`nodo-funzione` → `micro-dispositivo` → item F3-SIT) è ciò che mantiene ogni materiale **tracciabile agli assi e ai nodi** e impedisce la deriva verso le buone pratiche generiche.

---

## 6. Checklist di coerenza F3-SIT (C1–C8)

Applicata da `f3_sit_step_4` a ogni item. Derivata dalla checklist a 10 controlli di `f3_step_4`, adattata ai materiali situazionali. Esito per item: `passa` / `passa_con_riserve` / `non_passa`.

| ID | Controllo |
|---|---|
| C1 | Non etichetta il bambino (nessuna classificazione, definizione, diagnosi) |
| C2 | Non colpevolizza il genitore |
| C3 | Non moralizza il bambino né i terzi (compagni, gruppo) |
| C4 | Non prescrive rigidamente (resta micro-mediazione, non protocollo) |
| C5 | Modifica il campo relazionale, non corregge direttamente il soggetto |
| C6 | È tracciabile a nodo dominante e funzione (campi della §5 presenti e coerenti) |
| C7 | È adatto a un uso formativo senza diventare ricetta |
| C8 | Lascia aperta una nuova osservabilità del campo |

**Controlli critici**: C1, C2, C5, C6. Un `non_passa` su uno di questi rende l'item `non_pubblicabile`. Il verdetto di repertorio (`methodological_status`) è:
- `validato` — nessun `non_passa` critico, riserve ammesse;
- `richiede_revisione` — `non_passa` non critici, recuperabili;
- `non_pubblicabile` — almeno un `non_passa` critico.

---

## 7. Schemi di output

Quattro schemi JSON Schema (Draft-07), uno per step, da materializzare in Fase 2 nelle cartelle degli step. Ogni schema valida il wrapper della §5 + la struttura specifica dello step. Sono dichiarati come `inputs_strutturali` del proprio step (come gli `*-schema.json` esistenti).

| Step | File schema (sotto `input/produzioni/`) | Contenuto chiave di `results[0]` |
|---|---|---|
| `f3_sit_step_1` | `f3-sit-step-1-selezione-famiglie/sit-famiglie-schema.json` | `selected_families[]{family_id, priority, target_user, reason, expected_items}`, `excluded_families[]{family_id, reason}`, `narrative_families_selected` (bool, guida lo skip dello step 3) |
| `f3_sit_step_2` | `f3-sit-step-2-micro-mediazioni/sit-micro-mediazioni-schema.json` | `items[]{sit_id, family_id, title, context, configurational_basis, micro_mediation{adult_attitude, possible_phrase, alternative_phrase, gesture_or_timing, avoid[]}, expected_field_effect, non_prescriptive_note, + campi di tracciabilità §5}` |
| `f3_sit_step_3` | `f3-sit-step-3-formati-formativi/sit-formati-schema.json` | `training_outputs[]{format_id, source_sit_id, ...}` — vignette, storyboard (a pannelli), linee guida, prompt AI; `ai_generation_prompt` dove pertinente |
| `f3_sit_step_4` | `f3-sit-step-4-repertorio/sit-repertorio-schema.json` | `methodological_status`, `coherence_check{C1..C8}` per item, `repertoire{}` aggregato per famiglia, `publication_recommendation` |

---

## 8. Innesto in `pipeline-step-config.json`

Aggiungere 4 step. Forma proposta (allineata agli step F3 esistenti; i nomi di campo esatti vanno verificati sul config v3.1):

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

Punti chiave dell'innesto, validi per tutti e 4 gli step:

1. **`phase: "f3_sit"`** — nuova fase logica, distinta da `f2` e `f3`. Tiene il modulo separato nella UI e nella macchina a stati.
2. **`optional_module: true`** e **`f3_step_5` non elenca `f3_sit_step_1` nei propri `blocks`** — il modulo è attivabile, non dovuto.
3. **`output_path_template`** con destinazione `temi/{context_id}/sit/` (decisione D-d: nessun sottolivello `{dominio}`, il `context_id` codifica già `tema × ambito`). Verificare in `pipelineController.buildExecutionPlan` come è risolta la variabile di cartella per gli step F3 e replicare il meccanismo; **non** è richiesta la risoluzione di `{dominio}` nel path.
4. **Nessuno schema external materializzato** — l'`input_id` `destinazione_uso` è descritto nel `CLAUDE.md` di `f3_sit_step_1` e validato lato server alla ricezione (`postStepInput`), come `f3_step_1.contesto_ambito` (decisione D-g; cfr. `Storage dati e schemi pipeline.md` §3.1).
5. **`f3_sit_step_3`** porta `can_skip: true` e una `skip_condition` valorizzata (nessuna famiglia narrativa selezionata in `f3_sit_step_1`).
6. **Mirror Mongo invariato** — ogni step restituisce il JSON via `output_data` nell'evento `completed`; nessuna logica nuova nel subscriber.

Tabella sintetica dei 4 step per il config:

| `step_id` | `depends_on` | `verifica` | `can_skip` | `output_prefix` |
|---|---|---|---|---|
| `f3_sit_step_1` | `f3_step_5` | true | false | `sit-famiglie` |
| `f3_sit_step_2` | `f3_sit_step_1` | false | false | `sit-micro-mediazioni` |
| `f3_sit_step_3` | `f3_sit_step_2` | false | **true** | `sit-formati` |
| `f3_sit_step_4` | `f3_sit_step_2`, `f3_sit_step_3` | false | false | `sit-repertorio` |

---

## 9. Macchina a stati

Il modulo va tracciato senza interferire con la macchina a stati lineare di F3. Due opzioni, da decidere con Claude Code in base a `D2`:

- **Opzione A** — campo dedicato `sit_status` in `PipelineContext`: `{ enabled: bool, current_step: string, publication_ready: bool }`. Più esplicito, separa nettamente il modulo.
- **Opzione B** — riuso di `step_states` con i nuovi `step_id` `f3_sit_step_*`, ignorando quelli non avviati. Meno codice, ma mescola il modulo opzionale con la sequenza obbligatoria.

Raccomandazione: **Opzione A**, coerente con lo statuto di modulo derivato opzionale. `enabled` passa a `true` quando `f3_step_5` è `completato`; `publication_ready` a `true` quando `f3_sit_step_4` produce `methodological_status = validato`.

---

## 10. Verifiche umane

In linea con la logica delle verifiche della pipeline (un punto di verifica dove serve giudizio metodologico non delegabile all'agente):

| Step | Verifica umana | Motivo |
|---|---|---|
| `f3_sit_step_1` | **Sì, obbligatoria** | Il ricercatore decide la destinazione comunicativa: quali famiglie, per quali destinatari |
| `f3_sit_step_2` | Facoltativa | Qualità delle micro-mediazioni; raccomandata se destinate a pubblicazione |
| `f3_sit_step_3` | Facoltativa | Dipende dalla destinazione (sito/formazione → raccomandata) |
| `f3_sit_step_4` | No | La verifica metodologica *è* lo step (checklist C1–C8) |

---

## 11. Note aperte e pendenze

1. **Tassonomia da validare sul pilota.** Le 9 famiglie e gli schemi sono ipotesi finché la Fase 4 (pilota su `pointing`) non le conferma. Non costruire un set ampio di schede prima del pilota.
2. **Convenzione di naming F3 v3.0+ — risolta** *(chiarita da Claude Code, 2026-05-23)*. La sorgente di verità è `pipeline-step-config.json` v3.1: F3 step 1–4 producono file **senza** `{dominio}` (`{prefix}-v{N}.json`); solo F3 step 5 mantiene `{dominio}` nel filename per convenienza editoriale (la cartella `context_id = <theme_id>--<ambito_id>` codifica già l'ambito). I documenti `pipeline-produzioni-documentazione-cowork.md` §6 e `produzioni/CLAUDE.md` (lato Cowork) usavano la convenzione pre-bridge — `{dominio}` ovunque — e sono in corso di allineamento alla v3.0+ a cura di Claude Code. Per F3-SIT vale la convenzione post-bridge, già adottata in questo documento: file `sit-*-v{N}.json` **senza** `{dominio}`, sotto `temi/{context_id}/sit/`.
3. **Modalità DRAFT (v2).** L'innesto anticipato dopo `f3_step_2`, con un output `sit-draft-*`, resta una possibile evoluzione. Da valutare dopo il pilota.
4. **Audit metodologico.** Non è più uno step F3 (vedi nota di revisione in `D7` e `D8`). Se in futuro si volesse reintrodurre un audit di esecuzione, sarebbe un modulo separato, indipendente da F3-SIT.
5. **Componenti UI di preview** per gli output F3-SIT (viewer del repertorio, form di verifica famiglie): da specificare in coordinamento con `D5b`. Per la prima esecuzione il fallback "JSON pretty-printed" è sufficiente.

---

*Fine documento — D9, specifica del modulo F3-SIT, 2026-05-23.*
