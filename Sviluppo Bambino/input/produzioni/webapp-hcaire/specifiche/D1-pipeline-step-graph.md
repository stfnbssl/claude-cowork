# D1 — Grafo dichiarativo degli step della pipeline

> **Scopo del documento**: definire in modo esplicito e machine-readable la struttura di dipendenze della pipeline F2/F3. Sostituisce l'euristica `inferPipelineInputs` in `DeviceLineage.tsx` e diventa la sorgente di verità per il motore di esecuzione (D2–D5).
>
> **Destinatario**: Claude Code — da leggere prima di implementare qualsiasi logica di orchestrazione, form di input, o stato di esecuzione.

---

## 1. Concetti fondamentali

### Tipi di input

| Tipo | Codice | Descrizione |
|---|---|---|
| Input pipeline | `pipeline` | File JSON prodotto da uno step precedente della stessa run |
| Input strutturale fisso | `strutturale` | File di configurazione sempre disponibile, non prodotto dalla pipeline (es. assi strutturali, schema del dispositivo). Letto dal filesystem del progetto, non versionato per run. |
| Input esterno obbligatorio | `esterno_obbligatorio` | Dato fornito dal ricercatore prima dell'esecuzione dello step. Senza di esso lo step non può partire. Richiede una UI di compilazione/upload. |
| Input esterno facoltativo | `esterno_facoltativo` | Parametro opzionale fornito dal ricercatore. Se assente lo step usa il comportamento di default. |
| Dispositivo sorgente | `dispositivo_sorgente` | Dispositivo validato di un **altro tema** usato come base (rilevante per step 7, 8, 9 di temi derivati). |

### Tipi di output

Ogni step produce esattamente **un file JSON** (eccetto 6b che produce una variante del file di step 6). Il file viene salvato in `temi/<tema_id>/` o `ricerche/<ricerca_id>/` secondo la fase.

### Verifica

Alcuni step hanno un `verifica.md` che produce una **diagnosi** — non un'approvazione automatica. La verifica richiede valutazione umana. Nel motore di esecuzione, uno step con `verifica: true` va in stato `in_verifica` dopo il completamento, e passa a `verificato` solo dopo conferma esplicita dell'operatore.

### Step saltabili

`f3_step_8` può essere saltato quando il tema è una specializzazione di dominio di un tema esistente (non un tema nuovo). Lo skip va registrato esplicitamente con motivazione in `revisioni.md` e in `pipeline-index.json` → `steps_skipped`.

### Variante 6b e integrazione 6c

`f3_step_6b` è una **variante operativa** di `f3_step_6` e ne sovrascrive il proxy nel dispositivo finale (step 9). Il risultato di step 6b può richiedere un passo di integrazione `f3_step_6c` (non standardizzato) il cui output va trattato come una versione aggiornata del dispositivo corretto (equivalente funzionale di step 3).

---

## 2. Step F2 — Ricerca tematica

### f2_step_1 — Ricerca temi (Discovery)

**Funzione**: ricerca e formulazione di temi candidati strutturalmente significativi.

**Input**:
- `strutturale`: file JSON degli assi strutturali del progetto
- `esterno_facoltativo` `fonti_web`: fonti esterne (web, letteratura) da cui estrarre i temi candidati

**Output**: `ricerche/{ricerca_id}/theme-discovery-v{N}.json`

Schema root: `{ research_scope, candidate_themes: [...], global_notes }`

**Verifica**: ❌ (la selezione dei temi è validata direttamente dal ricercatore)

**Dipende da**: nessuno — è il primo step F2

---

### f2_step_2 — Rilevanza strutturale

**Funzione**: prima mappa esplorativa di assi, nodi e concetti-ponte per ciascun tema.

**Input**:
- `pipeline` `theme-discovery`: `ricerche/{ricerca_id}/theme-discovery-v{N}.json`
- `strutturale`: file JSON degli assi strutturali
- `esterno_obbligatorio` `scelta_tema`: scelta del tema (atto/fenomeno) da analizzare — definisce l'oggetto ontologico della pipeline. Senza questa scelta lo step non può essere eseguito.

**Output**: `ricerche/{ricerca_id}/theme-relevance-v{N}.json`

Schema root: `{ step, results: [{ theme_id, candidate_axes, candidate_nodes, candidate_bridge_concepts, theme_structure_assessment }] }`

**Verifica**: ✅ — applicare prima di procedere a f2_step_3

**Dipende da**: `f2_step_1`

---

### f2_step_3 — Verifica strutturale

**Funzione**: riduzione e selezione della configurazione strutturale (da ipotesi a vincolo).

**Input**:
- `pipeline` `theme-discovery`: `ricerche/{ricerca_id}/theme-discovery-v{N}.json`
- `pipeline` `theme-relevance`: `ricerche/{ricerca_id}/theme-relevance-v{N}.json`
- `strutturale`: file JSON degli assi strutturali

**Output**: `ricerche/{ricerca_id}/theme-verification-v{N}.json`

Schema root: `{ step, results: [{ theme_id, confirmed_axes, confirmed_nodes, confirmed_bridge_concepts, rejected_axes, rejected_nodes, structural_configuration, synthetic_formulation }] }`

**Verifica**: ❌ (la verifica è incorporata nello step stesso)

**Dipende da**: `f2_step_1`, `f2_step_2` (dopo verifica)

---

### f2_step_4 — Micro-matrice

**Funzione**: articolazione della configurazione strutturale in micro-matrice interrogabile.

**Input**:
- `pipeline` `theme-discovery`: `ricerche/{ricerca_id}/theme-discovery-v{N}.json`
- `pipeline` `theme-verification`: `ricerche/{ricerca_id}/theme-verification-v{N}.json`
- `strutturale`: file JSON degli assi strutturali

**Output**: `ricerche/{ricerca_id}/theme-matrix-v{N}.json`

Schema root: `{ step, results: [{ theme_id, core_configuration, axis_articulation, bridge_integration, structural_tensions, structural_questions, translation_potential, configuration_summary }] }`

**Verifica**: ❌

**Dipende da**: `f2_step_1`, `f2_step_3`

---

### f2_step_5 — Famiglia di output

**Funzione**: identificazione delle possibilità strutturate di uso del modello per dominio.

**Input**:
- `pipeline` `theme-discovery`: `ricerche/{ricerca_id}/theme-discovery-v{N}.json`
- `pipeline` `theme-verification`: `ricerche/{ricerca_id}/theme-verification-v{N}.json`
- `pipeline` `theme-matrix`: `ricerche/{ricerca_id}/theme-matrix-v{N}.json`
- `strutturale`: file JSON degli assi strutturali

**Output**: `ricerche/{ricerca_id}/output-family-v{N}.json`

Schema root: `{ step, results: [{ theme_id, output_families: [{ domain, output_type, structural_basis, value_added, reduction_risk }], meta_notes }] }`

**Verifica**: ✅ — applicare prima di passare a F3

**Dipende da**: `f2_step_1`, `f2_step_3`, `f2_step_4`

---

## 3. Step F3 — Costruzione del dispositivo

F3 lavora su **un tema per volta**. Il passaggio da F2 a F3 (quale tema portare in F3) è una **decisione umana**.

---

### f3_step_1 — Lettura configurazionale (Dispositivo di lettura)

**Funzione**: costruzione del dispositivo di lettura configurazionale per il tema.

**Input**:
- `pipeline` `output-family`: `ricerche/{ricerca_id}/output-family-v{N}.json` (tema selezionato)
- `strutturale`: `f3-step-1/reading-device-schema.json` — schema del dispositivo
- `esterno_obbligatorio` `tema_selezionato`: il tema specifico scelto dall'output family F2 — la selezione è una decisione umana esplicita, non automatica

**Output**: `temi/{tema_id}/lettura-configurazionale-v{N}.json`

Schema root: `{ step, device: { device_id, function, structural_reference, reading_focus, access_points, structural_questions, operative_proxy, observability_requirements, non_classifiability_rules, interpretive_warnings, non_permitted_transformations, validation_structural_check } }`

**Verifica**: ✅

**Dipende da**: `f2_step_5` (dopo verifica)

---

### f3_step_2 — Stress test

**Funzione**: test di tenuta del dispositivo su casi critici (configurazioni assenti, parziali, ambigue).

**Input**:
- `pipeline` `lettura-configurazionale`: `temi/{tema_id}/lettura-configurazionale-v{N}.json`
- `strutturale`: `f3-step-2/stress-test-schema.json`

**Output**: `temi/{tema_id}/stress-test-v{N}.json`

Schema root: `{ step, cases: [{ case_id, case_type, case_description, observed_configuration, classification, verdict }] }`

**Verifica**: ❌

**Dipende da**: `f3_step_1` (dopo verifica)

---

### f3_step_3 — Correzione strutturale

**Funzione**: correzione del dispositivo sulla base delle fratture emerse nello stress test.

**Input**:
- `pipeline` `lettura-configurazionale`: `temi/{tema_id}/lettura-configurazionale-v{N}.json`
- `pipeline` `stress-test`: `temi/{tema_id}/stress-test-v{N}.json`
- `strutturale`: `f3-step-3/structural-correction-schema.json`

**Output**: `temi/{tema_id}/correzione-strutturale-v{N}.json`

Schema root: `{ step, corrected_device: { ...struttura identica a step 1, più observability_requirements, non_classifiability_rules, operative_proxies }, corrections_log: [...] }`

**Verifica**: ❌

**Dipende da**: `f3_step_1`, `f3_step_2`

> **Nota**: questo step produce `corrections_log[]` — la struttura che alimenta `CorrectionsLog.tsx`. Il log deve essere sempre presente anche se vuoto.

---

### f3_step_4 — Test di indistinguibilità

**Funzione**: costruzione di coppie di casi quasi indistinguibili per verificare la tenuta del proxy.

**Input**:
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json`
- `strutturale`: `f3-step-4/indistinguibility-test-schema.json`

**Output**: `temi/{tema_id}/indistinguibility-test-v{N}.json`

Schema root: `{ step, case_pairs: [{ pair_id, case_A, case_B, proxy_discrimination, verdict }] }`

**Verifica**: ✅

**Dipende da**: `f3_step_3`

---

### f3_step_5 — Audit

**Funzione**: audit epistemico completo del dispositivo (inferenze, circolarità, normatività).

**Input**:
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json`
- `pipeline` `indistinguibility-test`: `temi/{tema_id}/indistinguibility-test-v{N}.json`
- `strutturale`: `f3-step-5/audit-schema.json`

**Output**: `temi/{tema_id}/audit-v{N}.json`

Schema root: `{ step, audit_results: { circularity_check, normativity_check, inference_check, ... } }`

**Verifica**: ✅

**Dipende da**: `f3_step_3`, `f3_step_4` (dopo verifica)

---

### f3_step_6 — Stabilizzazione proxy

**Funzione**: stabilizzazione del proxy (sostituzione di proxy fragili con proxy strutturalmente non reversibili).

**Input**:
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json`
- `pipeline` `indistinguibility-test`: `temi/{tema_id}/indistinguibility-test-v{N}.json`
- `pipeline` `audit`: `temi/{tema_id}/audit-v{N}.json`
- `esterno_facoltativo` `severita_test`: livello di severità del test di non-reversibilità (`standard` | `forte`). Default: `standard`.

**Output**: `temi/{tema_id}/stabilizzazione-proxy-v{N}.json`

Schema root: `{ step, proxy_diagnosis, new_proxy_proposal, non_reversibility_test }`

**Verifica**: ❌ (la verifica si applica dopo aver completato anche 6b)

**Dipende da**: `f3_step_3`, `f3_step_4` (dopo verifica), `f3_step_5` (dopo verifica)

---

### f3_step_6b — Stabilizzazione proxy — forma operativa

**Funzione**: forma operativa completa del proxy (condizioni di applicabilità, regole di non classificabilità). Da eseguire dopo step 6, prima della verifica.

**Input**:
- `pipeline` `stabilizzazione-proxy`: `temi/{tema_id}/stabilizzazione-proxy-v{N}.json`

**Output**: `temi/{tema_id}/stabilizzazione-proxy-v{N}b.json`

Schema root: `{ step, operative_proxy: { proxy_name, what_it_measures, required_observations, decision_logic, allowed_outputs, epistemic_limit } }`

**Verifica**: ✅ — la verifica copre sia step 6 che step 6b insieme

**Dipende da**: `f3_step_6`

> **Nota override**: l'output di 6b **sovrascrive** `operative_proxies` nel dispositivo finale (step 9) e — se presenti nel file — anche `observability_requirements` e `non_classifiability_rules`. Il campo `supersedes` in `OperativeProxy` traccia questa relazione.

---

### f3_step_6c — Integrazione proxy stabilizzato (variante non standard)

**Funzione**: integrazione del proxy stabilizzato nel dispositivo corretto, quando la verifica di 6b richiede un aggiornamento strutturale del dispositivo (non solo del proxy).

**Input**:
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json`
- `pipeline` `stabilizzazione-proxy-6b`: `temi/{tema_id}/stabilizzazione-proxy-v{N}b.json`

**Output**: `temi/{tema_id}/correzione-strutturale-v{N+1}.json` (nuova versione del dispositivo corretto, equivalente funzionale di step 3)

**Verifica**: ❌

**Dipende da**: `f3_step_6b` (dopo verifica, solo se richiesta dalla verifica)

> **Nota**: step 6c non è sempre presente. Se eseguito, il file prodotto diventa il nuovo `canonical_device` per gli step successivi al posto della versione precedente di step 3.

---

### f3_step_7 — Trasferibilità del dispositivo

**Funzione**: valutazione della trasferibilità del dispositivo validato a un nuovo ambito/dominio.

**Input**:
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json` (o step 6c se presente)
- `pipeline` `stabilizzazione-proxy-6b`: `temi/{tema_id}/stabilizzazione-proxy-v{N}b.json`
- `esterno_obbligatorio` `contesto_ambito`: definizione del contesto/dominio target (es. "clinico, neuropsviluppo, 9-24 mesi"). Questa scelta è **il vincolo di realtà del dispositivo** — definisce l'uso finale. File: `inputs/temi/{tema_id}/f3-step-7-contesto-{label}.json`.

**Output**: `temi/{tema_id}/trasferibilità-v{N}.json`

Schema root: `{ step, transferability_assessment: { verdict, transferable_elements, non_transferable_elements, new_risks, recommendation } }`

**Verifica**: ❌ (il verdetto di trasferibilità orienta la decisione di procedere a step 8)

**Dipende da**: `f3_step_3` (o `f3_step_6c`), `f3_step_6b` (dopo verifica)

---

### f3_step_8 — Adattamento strutturale

**Funzione**: costruzione dei quattro blocchi strutturali del nuovo dispositivo (corporeità, bridge, proxy, requisiti di osservabilità).

**Input**:
- `dispositivo_sorgente`: dispositivo corretto del tema di origine (`temi/{tema_sorgente}/correzione-strutturale-v{N}.json`)
- `pipeline` `trasferibilità`: `temi/{tema_id}/trasferibilità-v{N}.json`
- `esterno_facoltativo` `specificita_dispositivo`: livello di specificità del dispositivo finale. Raramente necessario — default: non fornito.

**Output**: `temi/{tema_id}/adattamento-strutturale-v{N}.json`

Schema root: `{ step, new_corporeity, new_bridge, new_proxy, observability_requirements, non_classifiability_rules }`

**Verifica**: ✅ — il proxy v1 può essere rifiutato dalla verifica e richiedere una versione v2 (re-esecuzione dello step con stesso input + feedback della verifica)

**Può essere saltato**: ✅ — quando il tema è una **specializzazione di dominio** di un tema esistente (non un tema nuovo). In questo caso `steps_skipped` in `pipeline-index.json` deve contenere `{ step: "f3_step_8", reason: "..." }`.

**Dipende da**: `f3_step_7`

---

### f3_step_9 — Dispositivo completo

**Funzione**: sintesi operativa del dispositivo completo per il tema. Integra tutti gli elementi stabilizzati senza innovazione libera.

**Input** (caso standard, step 8 eseguito):
- `dispositivo_sorgente`: `temi/{tema_sorgente}/correzione-strutturale-v{N}.json`
- `pipeline` `adattamento-strutturale`: `temi/{tema_id}/adattamento-strutturale-v{N}.json`
- `pipeline` `stabilizzazione-proxy-6b`: `temi/{tema_id}/stabilizzazione-proxy-v{N}b.json` (override proxy)

**Input** (caso specializzazione dominio, step 8 saltato):
- `pipeline` `correzione-strutturale`: `temi/{tema_id}/correzione-strutturale-v{N}.json` (o step 6c)
- `pipeline` `stabilizzazione-proxy-6b`: `temi/{tema_id}/stabilizzazione-proxy-v{N}b.json`
- `pipeline` `trasferibilità`: `temi/{tema_id}/trasferibilità-v{N}.json`

**Output**: `temi/{tema_id}/dispositivo-{label}-v{N}.json`

Schema root: identico a step 1 (`{ step, device: { device_id, ... } }`) ma per il tema/dominio corrente.

**Verifica**: ❌ (può essere aggiunta caso per caso)

**Dipende da**: `f3_step_6b` (dopo verifica), `f3_step_8` (dopo verifica) | `f3_step_7` (se step 8 saltato)

---

### f3_step_10 — Stress test del dispositivo

**Funzione**: stress test finale del dispositivo completo su 5 casi critici: assente, parziale, chiudente, apparente/scripted, quasi indistinguibile.

**Input**:
- `pipeline` `dispositivo`: `temi/{tema_id}/dispositivo-{label}-v{N}.json`
- `esterno_obbligatorio` `casi_stress_test`: i 5 casi critici costruiti dal ricercatore. File: `inputs/temi/{tema_id}/f3-step-10-casi-{label}.json`. **Senza questi casi lo step non può essere eseguito.**

**Output**: `temi/{tema_id}/stress-test-dispositivo-{label}-v{N}.json`

Schema root: `{ step, device_id, stress_test_results: [{ case_id, case_type, case_description, observed_configuration, proxy_application, device_performance, breaking_point, false_positive_risk, test_verdict }], global_assessment }`

**Verifica**: ❌ (il `global_assessment` orienta eventuali correzioni residue)

**Dipende da**: `f3_step_9`

---

## 4. Adjacency list delle dipendenze

```
F2:
  f2_step_1  →  f2_step_2
  f2_step_1  →  f2_step_3
  f2_step_1  →  f2_step_4
  f2_step_1  →  f2_step_5
  f2_step_2* →  f2_step_3   (* dopo verifica)
  f2_step_3  →  f2_step_4
  f2_step_3  →  f2_step_5
  f2_step_4  →  f2_step_5
  f2_step_5* →  [decisione umana: quale tema portare in F3]

F3:
  [decisione umana] → f3_step_1
  f3_step_1*  →  f3_step_2
  f3_step_2   →  f3_step_3
  f3_step_1   →  f3_step_3
  f3_step_3   →  f3_step_4
  f3_step_4*  →  f3_step_5
  f3_step_3   →  f3_step_5
  f3_step_5*  →  f3_step_6
  f3_step_4*  →  f3_step_6
  f3_step_3   →  f3_step_6
  f3_step_6   →  f3_step_6b
  f3_step_6b* →  f3_step_6c  (solo se verifica richiede integrazione)
  f3_step_6b* →  f3_step_7   (f3_step_6c se presente)
  f3_step_3   →  f3_step_7   (o f3_step_6c)
  f3_step_7   →  f3_step_8   (se non saltato)
  f3_step_8*  →  f3_step_9
  f3_step_6b  →  f3_step_9
  f3_step_9   →  f3_step_10

Legenda: * = la dipendenza si attiva solo dopo verifica positiva
```

---

## 5. Tabella riepilogativa

| Step | Fase | Label | Input pipeline | Input esterni obbligatori | Input esterni facoltativi | Verifica | Saltabile |
|---|---|---|---|---|---|---|---|
| `f2_step_1` | F2 | Discovery | — | — | fonti web | ❌ | ❌ |
| `f2_step_2` | F2 | Rilevanza | step 1 | scelta tema | — | ✅ | ❌ |
| `f2_step_3` | F2 | Verifica strutturale | step 1, 2 | — | — | ❌ | ❌ |
| `f2_step_4` | F2 | Micro-matrice | step 1, 3 | — | — | ❌ | ❌ |
| `f2_step_5` | F2 | Output family | step 1, 3, 4 | — | — | ✅ | ❌ |
| `f3_step_1` | F3 | Lettura configurazionale | output-family F2 | tema selezionato | — | ✅ | ❌ |
| `f3_step_2` | F3 | Stress test | step 1 | — | — | ❌ | ❌ |
| `f3_step_3` | F3 | Correzione strutturale | step 1, 2 | — | — | ❌ | ❌ |
| `f3_step_4` | F3 | Indistinguibilità | step 3 | — | — | ✅ | ❌ |
| `f3_step_5` | F3 | Audit | step 3, 4 | — | — | ✅ | ❌ |
| `f3_step_6` | F3 | Stabilizzazione proxy | step 3, 4, 5 | — | severità test | ❌ | ❌ |
| `f3_step_6b` | F3 | Proxy forma operativa | step 6 | — | — | ✅ | ❌ |
| `f3_step_6c` | F3 | Integrazione proxy (var.) | step 3/6c, 6b | — | — | ❌ | ✅* |
| `f3_step_7` | F3 | Trasferibilità | step 3/6c, 6b | contesto/ambito | — | ❌ | ❌ |
| `f3_step_8` | F3 | Adattamento strutturale | step 7 + sorgente | — | specificità dispositivo | ✅ | ✅ |
| `f3_step_9` | F3 | Dispositivo completo | step 6b, 8 / 7 | — | — | ❌ | ❌ |
| `f3_step_10` | F3 | Stress test dispositivo | step 9 | 5 casi critici | — | ❌ | ❌ |

`*` f3_step_6c è saltabile perché emerge solo se la verifica di 6b lo richiede.

---

## 6. Input esterni — schemi attesi

Gli input esterni obbligatori richiedono una UI di compilazione prima del lancio dello step. Di seguito la struttura minima attesa per ciascuno, utile a costruire i form.

### f2_step_2 — Scelta del tema

```json
{
  "tema_scelto": "pointing",
  "descrizione": "Il pointing come atto comunicativo precoce...",
  "motivazione_selezione": "Alta priorità esplorativa e pilota",
  "ricerca_id": "ricerca-02-pointing-precoce"
}
```

### f3_step_1 — Tema selezionato

```json
{
  "theme_id": "pointing",
  "label": "Pointing precoce",
  "provenienza_ricerca": "ricerca-02-pointing-precoce",
  "provenienza_step": "f2_step_5"
}
```

### f3_step_7 — Contesto/ambito

```json
{
  "target_domain": "clinico",
  "target_subdomain": "neuropsviluppo",
  "age_range": "9-24 mesi",
  "setting": "ambulatorio, setting semi-strutturato",
  "observer_profile": "logopedista, neuropsichiatra infantile",
  "notes": ""
}
```

### f3_step_10 — Casi di stress test

```json
{
  "tema_id": "pointing",
  "domain": "clinico",
  "cases": [
    { "case_id": "caso_01", "case_type": "assente", "case_description": "..." },
    { "case_id": "caso_02", "case_type": "parziale", "case_description": "..." },
    { "case_id": "caso_03", "case_type": "chiudente", "case_description": "..." },
    { "case_id": "caso_04", "case_type": "apparente_scripted", "case_description": "..." },
    { "case_id": "caso_05", "case_type": "quasi_indistinguibile", "case_description": "..." }
  ]
}
```

---

## 7. JSON config machine-readable (`pipeline-step-config.json`)

File da creare in `client/public/pipeline/pipeline-step-config.json` (o `server/src/config/`). Sostituisce l'euristica `inferPipelineInputs` e alimenta sia il frontend (DeviceLineage) che il motore di esecuzione backend.

```json
{
  "steps": [
    {
      "id": "f2_step_1",
      "label": "Discovery",
      "phase": "F2",
      "output_prefix": "theme-discovery",
      "output_path_template": "ricerche/{ricerca_id}/theme-discovery-v{N}.json",
      "inputs_pipeline": [],
      "inputs_strutturali": ["assi-strutturali.json"],
      "inputs_esterni": [
        { "id": "fonti_web", "label": "Fonti di ricerca esterne", "type": "esterno_facoltativo", "schema": null }
      ],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f2_step_2", "f2_step_3", "f2_step_4", "f2_step_5"]
    },
    {
      "id": "f2_step_2",
      "label": "Rilevanza strutturale",
      "phase": "F2",
      "output_prefix": "theme-relevance",
      "output_path_template": "ricerche/{ricerca_id}/theme-relevance-v{N}.json",
      "inputs_pipeline": [
        { "step": "f2_step_1", "role": "theme-discovery", "required": true }
      ],
      "inputs_strutturali": ["assi-strutturali.json"],
      "inputs_esterni": [
        { "id": "scelta_tema", "label": "Scelta del tema (atto/fenomeno)", "type": "esterno_obbligatorio", "schema": "external-input-schemas/f2-step-2-scelta-tema.json" }
      ],
      "verifica": true,
      "can_skip": false,
      "blocks": ["f2_step_3"]
    },
    {
      "id": "f2_step_3",
      "label": "Verifica strutturale",
      "phase": "F2",
      "output_prefix": "theme-verification",
      "output_path_template": "ricerche/{ricerca_id}/theme-verification-v{N}.json",
      "inputs_pipeline": [
        { "step": "f2_step_1", "role": "theme-discovery", "required": true },
        { "step": "f2_step_2", "role": "theme-relevance", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": ["assi-strutturali.json"],
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f2_step_4", "f2_step_5"]
    },
    {
      "id": "f2_step_4",
      "label": "Micro-matrice",
      "phase": "F2",
      "output_prefix": "theme-matrix",
      "output_path_template": "ricerche/{ricerca_id}/theme-matrix-v{N}.json",
      "inputs_pipeline": [
        { "step": "f2_step_1", "role": "theme-discovery", "required": true },
        { "step": "f2_step_3", "role": "theme-verification", "required": true }
      ],
      "inputs_strutturali": ["assi-strutturali.json"],
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f2_step_5"]
    },
    {
      "id": "f2_step_5",
      "label": "Output family",
      "phase": "F2",
      "output_prefix": "output-family",
      "output_path_template": "ricerche/{ricerca_id}/output-family-v{N}.json",
      "inputs_pipeline": [
        { "step": "f2_step_1", "role": "theme-discovery", "required": true },
        { "step": "f2_step_3", "role": "theme-verification", "required": true },
        { "step": "f2_step_4", "role": "theme-matrix", "required": true }
      ],
      "inputs_strutturali": ["assi-strutturali.json"],
      "inputs_esterni": [],
      "verifica": true,
      "can_skip": false,
      "blocks": ["[human_decision] → f3_step_1"]
    },
    {
      "id": "f3_step_1",
      "label": "Lettura configurazionale",
      "phase": "F3",
      "output_prefix": "lettura-configurazionale",
      "output_path_template": "temi/{tema_id}/lettura-configurazionale-v{N}.json",
      "inputs_pipeline": [
        { "step": "f2_step_5", "role": "output-family", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": ["f3-step-1/reading-device-schema.json"],
      "inputs_esterni": [
        { "id": "tema_selezionato", "label": "Tema selezionato da F2", "type": "esterno_obbligatorio", "schema": "external-input-schemas/f3-step-1-tema.json" }
      ],
      "verifica": true,
      "can_skip": false,
      "blocks": ["f3_step_2"]
    },
    {
      "id": "f3_step_2",
      "label": "Stress test",
      "phase": "F3",
      "output_prefix": "stress-test",
      "output_path_template": "temi/{tema_id}/stress-test-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_1", "role": "lettura-configurazionale", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": ["f3-step-2/stress-test-schema.json"],
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f3_step_3"]
    },
    {
      "id": "f3_step_3",
      "label": "Correzione strutturale",
      "phase": "F3",
      "output_prefix": "correzione-strutturale",
      "output_path_template": "temi/{tema_id}/correzione-strutturale-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_1", "role": "lettura-configurazionale", "required": true },
        { "step": "f3_step_2", "role": "stress-test", "required": true }
      ],
      "inputs_strutturali": ["f3-step-3/structural-correction-schema.json"],
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f3_step_4", "f3_step_5", "f3_step_6", "f3_step_7", "f3_step_9"]
    },
    {
      "id": "f3_step_4",
      "label": "Test di indistinguibilità",
      "phase": "F3",
      "output_prefix": "indistinguibility-test",
      "output_path_template": "temi/{tema_id}/indistinguibility-test-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_3", "role": "correzione-strutturale", "required": true }
      ],
      "inputs_strutturali": ["f3-step-4/indistinguibility-test-schema.json"],
      "inputs_esterni": [],
      "verifica": true,
      "can_skip": false,
      "blocks": ["f3_step_5", "f3_step_6"]
    },
    {
      "id": "f3_step_5",
      "label": "Audit",
      "phase": "F3",
      "output_prefix": "audit",
      "output_path_template": "temi/{tema_id}/audit-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_3", "role": "correzione-strutturale", "required": true },
        { "step": "f3_step_4", "role": "indistinguibility-test", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": ["f3-step-5/audit-schema.json"],
      "inputs_esterni": [],
      "verifica": true,
      "can_skip": false,
      "blocks": ["f3_step_6"]
    },
    {
      "id": "f3_step_6",
      "label": "Stabilizzazione proxy",
      "phase": "F3",
      "output_prefix": "stabilizzazione-proxy",
      "output_path_template": "temi/{tema_id}/stabilizzazione-proxy-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_3", "role": "correzione-strutturale", "required": true },
        { "step": "f3_step_4", "role": "indistinguibility-test", "required": true, "requires_verifica": true },
        { "step": "f3_step_5", "role": "audit", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": [],
      "inputs_esterni": [
        { "id": "severita_test", "label": "Severità test non-reversibilità", "type": "esterno_facoltativo", "values": ["standard", "forte"], "default": "standard" }
      ],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f3_step_6b"]
    },
    {
      "id": "f3_step_6b",
      "label": "Proxy forma operativa",
      "phase": "F3",
      "output_prefix": "stabilizzazione-proxy",
      "output_suffix": "b",
      "output_path_template": "temi/{tema_id}/stabilizzazione-proxy-v{N}b.json",
      "inputs_pipeline": [
        { "step": "f3_step_6", "role": "stabilizzazione-proxy", "required": true }
      ],
      "inputs_strutturali": [],
      "inputs_esterni": [],
      "verifica": true,
      "overrides": ["operative_proxies", "observability_requirements", "non_classifiability_rules"],
      "can_skip": false,
      "blocks": ["f3_step_6c", "f3_step_7", "f3_step_9"]
    },
    {
      "id": "f3_step_6c",
      "label": "Integrazione proxy stabilizzato",
      "phase": "F3",
      "output_prefix": "correzione-strutturale",
      "output_path_template": "temi/{tema_id}/correzione-strutturale-v{N+1}.json",
      "note": "Nuova versione del dispositivo corretto. Diventa il canonical_device per gli step successivi.",
      "inputs_pipeline": [
        { "step": "f3_step_3", "role": "correzione-strutturale", "required": true },
        { "step": "f3_step_6b", "role": "stabilizzazione-proxy-b", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": [],
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": true,
      "skip_condition": "La verifica di f3_step_6b non richiede integrazione strutturale",
      "blocks": ["f3_step_7", "f3_step_9"]
    },
    {
      "id": "f3_step_7",
      "label": "Trasferibilità",
      "phase": "F3",
      "output_prefix": "trasferibilità",
      "output_path_template": "temi/{tema_id}/trasferibilità-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_3_or_6c", "role": "correzione-strutturale", "required": true, "note": "f3_step_6c se presente, altrimenti f3_step_3" },
        { "step": "f3_step_6b", "role": "stabilizzazione-proxy-b", "required": true, "requires_verifica": true }
      ],
      "inputs_strutturali": [],
      "inputs_esterni": [
        { "id": "contesto_ambito", "label": "Contesto/ambito target", "type": "esterno_obbligatorio", "schema": "external-input-schemas/f3-step-7-contesto.json", "file_template": "inputs/temi/{tema_id}/f3-step-7-contesto-{label}.json" }
      ],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f3_step_8", "f3_step_9"]
    },
    {
      "id": "f3_step_8",
      "label": "Adattamento strutturale",
      "phase": "F3",
      "output_prefix": "adattamento-strutturale",
      "output_path_template": "temi/{tema_id}/adattamento-strutturale-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_7", "role": "trasferibilità", "required": true }
      ],
      "inputs_dispositivo_sorgente": {
        "required": true,
        "description": "Dispositivo corretto del tema di origine",
        "path_template": "temi/{tema_sorgente_id}/correzione-strutturale-v{N}.json"
      },
      "inputs_strutturali": [],
      "inputs_esterni": [
        { "id": "specificita_dispositivo", "label": "Livello di specificità del dispositivo finale", "type": "esterno_facoltativo", "values": ["standard", "alta"], "default": "standard" }
      ],
      "verifica": true,
      "can_skip": true,
      "skip_condition": "Specializzazione di dominio (non nuovo tema) — step 8 non necessario",
      "blocks": ["f3_step_9"]
    },
    {
      "id": "f3_step_9",
      "label": "Dispositivo completo",
      "phase": "F3",
      "output_prefix": "dispositivo",
      "output_path_template": "temi/{tema_id}/dispositivo-{label}-v{N}.json",
      "inputs_pipeline_standard": [
        { "step": "f3_step_6b", "role": "stabilizzazione-proxy-b", "required": true },
        { "step": "f3_step_8", "role": "adattamento-strutturale", "required": true, "requires_verifica": true }
      ],
      "inputs_pipeline_skip_8": [
        { "step": "f3_step_3_or_6c", "role": "correzione-strutturale", "required": true },
        { "step": "f3_step_6b", "role": "stabilizzazione-proxy-b", "required": true },
        { "step": "f3_step_7", "role": "trasferibilità", "required": true }
      ],
      "inputs_dispositivo_sorgente": {
        "required": "se step 8 eseguito",
        "description": "Dispositivo corretto del tema di origine",
        "path_template": "temi/{tema_sorgente_id}/correzione-strutturale-v{N}.json"
      },
      "inputs_esterni": [],
      "verifica": false,
      "can_skip": false,
      "blocks": ["f3_step_10"]
    },
    {
      "id": "f3_step_10",
      "label": "Stress test dispositivo",
      "phase": "F3",
      "output_prefix": "stress-test-dispositivo",
      "output_path_template": "temi/{tema_id}/stress-test-dispositivo-{label}-v{N}.json",
      "inputs_pipeline": [
        { "step": "f3_step_9", "role": "dispositivo", "required": true }
      ],
      "inputs_strutturali": [],
      "inputs_esterni": [
        { "id": "casi_stress_test", "label": "5 casi critici per lo stress test", "type": "esterno_obbligatorio", "schema": "external-input-schemas/f3-step-10-casi.json", "file_template": "inputs/temi/{tema_id}/f3-step-10-casi-{label}.json", "note": "Deve coprire i 5 tipi: assente, parziale, chiudente, apparente_scripted, quasi_indistinguibile" }
      ],
      "verifica": false,
      "can_skip": false,
      "blocks": []
    }
  ]
}
```

---

## 8. Implicazioni per il motore di esecuzione

Le informazioni di questo documento definiscono direttamente:

1. **Condizioni di abilitazione di uno step** — un step è lanciabile quando tutti i suoi `inputs_pipeline` con `required: true` hanno uno step con status `completato` (e `verificato` se `requires_verifica: true`), e tutti i suoi `inputs_esterni` obbligatori sono stati forniti.

2. **Form di input esterno** — la UI deve mostrare il form corrispondente all'input esterno prima di abilitare il pulsante "Lancia step". Lo schema del form è in `external-input-schemas/{file}`.

3. **Override step 6b** — dopo il completamento di f3_step_6b (verificato), il sistema deve segnalare che i campi `operative_proxies`, `observability_requirements`, `non_classifiability_rules` del dispositivo canonico sono stati sovrascritti.

4. **Step 6c condizionale** — il sistema deve esporre l'opzione "Esegui integrazione (6c)" solo dopo che la verifica di 6b è stata completata e ha prodotto una raccomandazione di integrazione.

5. **Biforcazione step 9** — il motore deve distinguere i due percorsi di input di step 9 in base alla presenza/assenza di step 8 nell'esecuzione corrente.

6. **Decisioni umane** — i due passaggi di decisione umana (`f2_step_5 → f3_step_1` e la selezione del contesto in `f3_step_7`) non sono automatizzabili: il sistema deve entrare in stato `attende_decisione` e notificare l'operatore.
