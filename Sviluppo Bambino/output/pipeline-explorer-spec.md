# Pipeline Explorer — Specifica di implementazione

## Scopo

Sezione della webapp HCAIRE per visualizzare e analizzare gli output JSON della pipeline F2 (ricerca tematica) e F3 (costruzione dispositivi configurazionali). Destinatari: ricercatori del laboratorio che lavorano sulla pipeline o che vogliono consultare i dispositivi prodotti.

---

## Struttura dei dati

### F2 — batch di ricerca

Ogni ricerca è una cartella in `output/produzioni/ricerche/[nome-ricerca]/` con 5 file JSON:

```
theme-discovery-vN.json     → { research_scope, candidate_themes: [...], global_notes }
theme-relevance-vN.json     → { step, results: [{ theme_id, candidate_axes, candidate_nodes, candidate_bridge_concepts, theme_structure_assessment }] }
theme-verification-vN.json  → { step, results: [{ theme_id, confirmed_axes, confirmed_nodes, confirmed_bridge_concepts, rejected_axes, rejected_nodes, structural_configuration, synthetic_formulation }] }
theme-matrix-vN.json        → { step, results: [{ theme_id, core_configuration, axis_articulation, bridge_integration, structural_tensions, structural_questions, translation_potential, configuration_summary }] }
output-family-vN.json       → { step, results: [{ theme_id, output_families: [{ domain, output_type, structural_basis, value_added, reduction_risk }], meta_notes }] }
```

I valori ammessi chiave:
- `relevance_level` degli assi: `"forte"` | `"plausibile"` | `"da_verificare"`
- `structural_configuration.type`: `"asse_dominante"` | `"multi_assiale"` | `"soglia_tra_assi"`
- `bridge_integration.type`: `"connettivo"` | `"organizzativo"`

### F3 — dispositivo per tema

Ogni tema è una cartella in `output/produzioni/temi/[nome-tema]/` con file corrispondenti agli step completati:

```
lettura-configurazionale-*-vN.json   → step 1: { step, device: { device_id, function, structural_reference, reading_focus: [...], access_points: [...], structural_questions: [...], operative_proxy, observability_requirements: [...], non_classifiability_rules: [...], interpretive_warnings: [...], non_permitted_transformations: [...], validation_structural_check } }

stress-test-*-vN.json                → step 2: { step, cases: [{ case_id, case_type, case_description, observed_configuration, classification, verdict }] }

correzione-strutturale-*-vN.json     → step 3: { step, corrected_device: { ...come step 1, più observability_requirements, non_classifiability_rules, operative_proxies } }

indistinguibility-test-*-vN.json     → step 4: { step, case_pairs: [{ pair_id, case_A, case_B, proxy_discrimination, verdict }] }

audit-*-vN.json                      → step 5: { step, audit_results: { circularity_check, normativity_check, inference_check, ... } }

stabilizzazione-proxy-*-vN.json      → step 6: { step, proxy_diagnosis, new_proxy_proposal, non_reversibility_test }
stabilizzazione-proxy-*-vNb.json     → step 6-B: { step, operative_proxy: { proxy_name, what_it_measures, required_observations, decision_logic, allowed_outputs, epistemic_limit } }

trasferibilità-*-vN.json             → step 7: { step, transferability_assessment: { verdict, transferable_elements, non_transferable_elements, new_risks, recommendation } }

adattamento-strutturale-*-vN.json    → step 8: { step, new_corporeity, new_bridge, new_proxy, observability_requirements, non_classifiability_rules }

dispositivo-*-vN.json                → step 9 (dispositivo completo): struttura identica a step 1/3 ma per il nuovo tema

stress-test-dispositivo-*-vN.json    → step 10: { step, device_id, stress_test_results: [{ case_id, case_type, case_description, observed_configuration, proxy_application, device_performance, breaking_point, false_positive_risk, test_verdict }], global_assessment }
```

---

## Architettura della sezione

### Route structure
```
/pipeline                          → Pipeline Map (landing)
/pipeline/ricerche/:ricercaId      → Theme Explorer F2 (lista temi della ricerca)
/pipeline/ricerche/:ricercaId/:temaId  → Theme Detail F2 (step 1-5 del tema)
/pipeline/temi                     → Lista temi F3
/pipeline/temi/:temaId             → Device Overview (step F3 completati)
/pipeline/temi/:temaId/dispositivo → Device Viewer (step 9 completo)
/pipeline/temi/:temaId/stress-test → Stress Test Dashboard (step 10)
/pipeline/temi/:temaId/proxy       → Proxy Evolution (storia versioni)
/pipeline/temi/:temaId/compare     → Comparative View (se più dispositivi)
```

### Data loading
Caricare i JSON staticamente. Creare un index file `pipeline-index.json` che mappa:
```json
{
  "ricerche": [
    { "id": "ricerca-01-comunicazione-precoce", "label": "Comunicazione precoce", "n_temi": 10, "steps_completed": ["f2-step-1","f2-step-2","f2-step-3","f2-step-4","f2-step-5"] }
  ],
  "temi": [
    { "id": "pointing", "ricerca_origine": "ricerca-02-pointing-precoce", "steps_completed": ["f3-step-1","f3-step-2","f3-step-3","f3-step-4","f3-step-5","f3-step-6","f3-step-6b"] },
    { "id": "richiesta-aiuto-clinico", "ricerca_origine": "ricerca-02-pointing-precoce", "steps_completed": ["f3-step-7","f3-step-8","f3-step-9","f3-step-10"] }
  ]
}
```

---

## Componenti — specifiche dettagliate

---

### 1. PipelineMap

**Layout**: due colonne affiancate — sinistra F2, destra F3.

**Colonna F2**:
- Header "Ricerche tematiche"
- Per ogni ricerca: card con nome, data/versione, numero di temi
- Clic → Theme Explorer

**Colonna F3**:
- Header "Dispositivi"
- Per ogni tema F3: card con nome tema, dominio, indicatore di completamento degli step F3 (barra orizzontale con 10 segmenti, colorati per stato: completato / con_riserva / non_eseguito)
- Sotto la barra: link al dispositivo sorgente se il tema è derivato
- Clic → Device Overview

**Nessuna logica di filtro necessaria** a questo livello — la lista è corta per design.

---

### 2. ThemeExplorer F2

**Layout**: sidebar sinistra con lista temi della ricerca, area principale con dettaglio tema selezionato.

**Theme card** nella sidebar:
- Label provvisoria del tema
- Badge con tipo struttura (`asse_dominante` / `multi_assiale` / `soglia_tra_assi`)
- N. assi confermati

**Area principale — navigazione a tab** tra gli step F2:

**Tab Discovery**:
- `what_it_is`: testo in card
- `what_it_is_not`: testo in card con sfondo leggermente diverso
- `why_it_matters`: testo
- `theme_reduction_risks`: lista con icona ⚠️

**Tab Rilevanza**:
- Assi: tabella con nome asse, livello (badge colorato: forte=verde, plausibile=giallo, da_verificare=grigio), motivazione in tooltip o accordion
- Nodi: lista con badge dell'asse di origine, flag `is_derived` se presente
- Concetti-ponte: lista con i due assi collegati come tag

**Tab Verifica**:
- Assi confermati: lista verde
- Assi rifiutati: lista rossa con `rejection_reason`
- Nodi confermati: lista verde
- Nodi rifiutati/secondari: lista rossa/arancio con motivazione
- `synthetic_formulation`: in evidenza (testo grande, card dedicata)

**Tab Matrice**:
- `core_configuration.description`: testo in evidenza
- Tensioni strutturali: visualizzazione a coppie di poli con freccia doppia tra i due (es. "regolazione ←→ apertura"), descrizione sotto
- Domande strutturali: lista numerata con accordion (domanda → espande per mostrare il contesto strutturale)
- `translation_potential`: chip per dominio (clinico / educativo / formazione / politiche) con tooltip sulla motivazione

**Tab Output Family**:
- Per ogni dominio: accordion con `output_type`, `value_added`, `reduction_risk` (con icona ⚠️)

---

### 3. DeviceViewer F3

**Layout**: navigation rail laterale con le 5 dimensioni + sezioni operative, area principale.

**Navigation rail**:
```
● Base corporea
● Campo intenzionale
● Co-regolazione
● Mediazione simbolica
● Passaggio trasformativo
─────────────────
● Proxy operativo
● Osservabilità
● Non classificabilità
● Warning interpretativi
● Trasformazioni vietate
─────────────────
✓ Validazione strutturale
```

**Sezione dimensione** (per ognuna delle 5):
- Titolo dimensione
- Testo descrittivo completo (reading_focus[i].description)
- Se la dimensione ha stati nominati (es. "presente / assente / distorta / oscillante"): visualizzarli come chip in una riga, ciascuno espandibile con la descrizione specifica

**Sezione Proxy operativo**:
- `proxy_name`: titolo in evidenza
- `what_it_measures`: testo in card
- `decision_logic`: visualizzare come flowchart testuale:
  ```
  SE [condizioni di applicabilità soddisfatte]
    → adulto orienta verso configurazione specifica → APERTO
    → adulto agisce direttamente → PREDETERMINATO
    → orientamento non distinguibile → AMBIGUO
  SE anche una sola condizione di non-applicabilità
    → NON_CLASSIFICABILE (senza tentativo)
  ```
  Gli output (`aperto`, `predeterminato`, `ambiguo`, `non_classificabile`) come badge colorati: verde / arancio / giallo / grigio
- `epistemic_limit`: testo in card con sfondo warning

**Sezione Osservabilità**:
- Tabella: id | label | tipo | observer_dependency | required_for_proxy
- `required_for_proxy = true` → riga evidenziata

**Sezione Non classificabilità**:
- Per ogni regola: `trigger` → `required_output` con distinzione cromatica `non_classificabile` (grigio) vs `ambiguo` (giallo)
- Nota esplicativa sulla distinzione: dato assente ≠ dato presente ma non discriminante

**Sezione Warning interpretativi**:
- Lista con icona per tipo: 🔴 comportamentismo | 🟠 normatività | 🟡 tecnicismo | 🔵 riduzione cognitiva | 🟣 tecnicismo riabilitativo
- Accordion con testo completo

**Sezione Validazione strutturale**:
- Checklist 5 criteri: `configurational_logic_preserved` / `no_psychological_inference` / `no_circularity` / `proxy_observable` / `self_limiting`
- Icona ✓/✗ per ciascuno + notes in accordion

---

### 4. StressTestDashboard

**Layout**: lista casi a sinistra (sidebar), dettaglio caso a destra.

**Sidebar casi**:
- Per ogni caso: chip tipo (assente / parziale / chiudente / apparente / quasi-indistinguibile), badge verdetto (regge=verde / regge_con_riserva=arancio / fallisce=rosso)
- Selezione → aggiorna dettaglio

**Dettaglio caso**:

*Header*: nome caso, tipo, verdetto badge

*Configurazione osservata*: 5 dimensioni in lista compatta (label + breve descrizione)

*Proxy application*:
- `applicable`: true/false con icona
- `proxy_output`: badge colorato grande
- `required_observations_present`: lista verde
- `missing_observations`: lista rossa

*Device performance*:
- `readable`: true/false
- `what_it_reads`: testo
- `what_becomes_unclear`: testo con sfondo giallo chiaro
- `ambiguity_level`: badge (basso=verde / medio=arancio / alto=rosso)

*Breaking point* (se present=true):
- Card con sfondo arancio: `where` + `why`

*Rischio falso positivo* (se risk_present=true):
- Card con sfondo rosso chiaro: `description` + `mitigation`

**Footer — Global Assessment**:
- `device_robustness`: badge grande (alta=verde / media=arancio / bassa=rosso)
- `main_strengths`: lista con icona ✓
- `main_weaknesses`: lista con icona ⚠
- `required_corrections`: lista con icona → (vuota se nessuna correzione strutturale)

---

### 5. ProxyEvolution

**Layout**: timeline verticale.

Per ogni versione del proxy (in ordine cronologico):

```
[v1]  ──────────────────────────────────────
  proxy_name: "..."
  stato: parzialmente_resistente   ← badge rosso/arancio
  motivo rifiuto: "..."            ← card con sfondo arancio
      ↓ (freccia "promosso a")
[v2]  ──────────────────────────────────────
  proxy_name: "..."
  stato: resistente                ← badge verde
  elemento chiave: "obs_5 promosso da rafforzamento a discriminante centrale"
```

Se è il proxy del dispositivo completo (step 9), aggiungere badge "In uso nel dispositivo finale".

Sotto la timeline: sezione "Principio di non reversibilità" con la spiegazione di perché il proxy v2 (o vN) è strutturalmente non mimabile dallo script.

---

### 6. DeviceLineage — Tracciabilità input e derivazione

**Scopo**: mostrare *cosa ha prodotto* ogni risultato — quali file di input, quali input esterni forniti dal ricercatore, e in quale sequenza gli step si sono costruiti l'uno sull'altro. Risponde alla domanda "come si è arrivati a questo dispositivo?".

**Dove appare**: come tab aggiuntiva in Device Overview (`/pipeline/temi/:temaId`), accessibile anche come panel collassabile dentro DeviceViewer e StressTestDashboard.

---

#### 6.1 Grafo di derivazione (Input Graph)

Visualizzazione a grafo verticale (top → bottom) dove ogni nodo è uno step e gli archi indicano i flussi di input.

```
[INPUT ESTERNO: contesto clinico]          [Dispositivo sorgente: pointing-v2]
          │                                           │
          ▼                                           ▼
    ┌─────────────┐                         ┌──────────────────┐
    │  f3-step-7  │ ──────────────────────▶ │  f3-step-9       │
    │ Trasferibilità│                        │ Dispositivo      │
    │ clinica     │                         │ completo         │
    └─────────────┘                         └──────────────────┘
                                                     │
                                                     ▼
                                            ┌──────────────────┐
                                            │  f3-step-10      │
                                            │ Stress test      │
                                            └──────────────────┘
```

**Nodi del grafo**:
- **Step pipeline** (rettangolo): nome step, step_id, data di esecuzione se disponibile
- **Input esterno** (rombo, colore diverso): input forniti dal ricercatore — contesto/dominio (f3-step-7), casi di stress test (f3-step-10), scelta del tema (f2-step-2)
- **Dispositivo sorgente** (esagono): quando uno step deriva da un dispositivo validato di un altro tema

**Archi**: etichettati con il nome del file passato come input (es. `correzione-strutturale-clinico-v2.json`).

**Clic su un nodo step** → espande un pannello inline con:
- File di input (lista con link ai JSON)
- File di output prodotto (link)
- Skip se applicabile (es. "step-8 saltato: specializzazione di dominio, non nuovo tema")

---

#### 6.2 Input Provenance Panel

Pannello strutturato per ogni step, mostrato come accordion nella pagina del dispositivo.

**Per ogni step completato**, mostrare:

```
┌─ f3-step-7 — Trasferibilità ─────────────────────────────────────┐
│ INPUT PIPELINE                                                    │
│   • correzione-strutturale-clinico-v2.json  [dispositivo sorgente]│
│   • stabilizzazione-proxy-clinico-v1b.json  [proxy stabilizzato]  │
│                                                                   │
│ INPUT ESTERNO (fornito dal ricercatore)                           │
│   • f3-step-7-contesto-clinico.json  ← contesto neuropsviluppo   │
│     target_domain: "clinico (neuropsviluppo, 9-24 mesi)"         │
│     setting: "ambulatorio, setting semi-strutturato"             │
│     [espandi per dettaglio completo]                              │
│                                                                   │
│ CONDIZIONI DI ESECUZIONE                                          │
│   skip_step_8: true — "specializzazione dominio, non nuovo tema"  │
│                                                                   │
│ OUTPUT PRODOTTO                                                   │
│   • f3-step-7-trasferibilita-clinico-v1.json                     │
│   verdetto: trasferibile_con_adattamenti                         │
└───────────────────────────────────────────────────────────────────┘
```

**Tipi di input** da visualizzare con badge distinti:
- `pipeline` → grigio: file prodotto da uno step precedente della stessa pipeline
- `esterno_obbligatorio` → blu: input fornito dal ricercatore (contesto, tema, casi)
- `esterno_facoltativo` → celeste: input opzionale (severità test, specificità dispositivo)
- `dispositivo_sorgente` → viola: dispositivo di un altro tema usato come base

---

#### 6.3 CorrectionsLog — Sequenza fratture → correzioni

Componente dedicato che ricostruisce il processo decisionale dagli step di correzione (f3-step-3, f3-step-6, f3-step-8 v2).

Fonte: `corrections_log[]` nei file di correzione strutturale.

**Layout**: lista verticale di episodi correzione, ciascuno con struttura:

```
┌─ FRATTURA RILEVATA (step 2, caso_03) ───────────────────────────┐
│  "Il nodo co-regolazione è descritto come unico stato           │
│   qualitativo senza articolazione interna..."                   │
│                                                                 │
│  breaking_point_ref: case_03                                    │
│  scope: reading_focus                                           │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼ CORREZIONE APPLICATA
┌─────────────────────────────────────────────────────────────────┐
│  "La dimensione 'Qualità co-regolatoria della risposta'         │
│   è riarticolata in cinque livelli strutturalmente distinti:    │
│   assente, registrativa, partecipativa, trasformativa,          │
│   chiudente..."                                                 │
│                                                                 │
│  RAZIONALE:                                                     │
│  "La versione precedente collassava risposta-assente e          │
│   risposta-che-non-sostiene in un'unica categoria..."           │
└─────────────────────────────────────────────────────────────────┘
```

**Colorazione**: frattura = sfondo rosso chiaro, correzione = sfondo verde chiaro, razionale = sfondo grigio.

Se il campo `correction_type` è `"applicata"` → mostrare la freccia. Se è `"rinviata"` o `"non_applicata"` → mostrare con badge grigio e motivazione.

---

#### 6.4 ProcessNarrative — Storia decisionale del tema

Componente narrativo costruito dal file `revisioni.md` della cartella del tema.

**Formato**: timeline verticale con sezioni corrispondenti alle sezioni di revisioni.md.

Ogni sezione mostra:
- Intestazione dello step o passaggio (es. "f3-step-6 → f3-step-6B → f3-step-6C")
- Testo narrativo della revisione (il body della sezione md)
- Tag dei concetti chiave estratti (proxy, NCR, breaking point, principio consolidato)

**Principio chiave evidenziato**: se il testo contiene una frase esplicitamente segnalata come principio consolidato (es. "**Principio consolidato**: ..."), estrarlo e mostrarlo in una card dedicata con bordo a sinistra colorato.

Questo componente risponde alla domanda "quali decisioni episodiche hanno reso questo dispositivo quello che è?" — non descrive la struttura del dispositivo ma la storia del suo diventare.

---

#### 6.5 Aggiornamento pipeline-index.json

Il file index va esteso con informazioni di derivazione per ogni tema:

```json
{
  "temi": [
    {
      "id": "pointing",
      "ricerca_origine": "ricerca-02-pointing-precoce",
      "dispositivo_sorgente": null,
      "steps_completed": ["f3-step-1","f3-step-2","f3-step-3","f3-step-4","f3-step-5","f3-step-6","f3-step-6b","f3-step-6c","f3-step-7","f3-step-9","f3-step-10"],
      "steps_skipped": [{ "step": "f3-step-8", "reason": "specializzazione dominio, non nuovo tema" }],
      "external_inputs": [
        { "step": "f3-step-7", "file": "f3-step-7-contesto-clinico.json", "type": "esterno_obbligatorio", "label": "Contesto clinico neuropsviluppo" }
      ],
      "dispositivo_file": "dispositivo-pointing-clinico-neuropsviluppo-v1.json",
      "stress_test_file": "stress-test-pointing-clinico-v1.json",
      "robustezza": "alta",
      "correzioni_residue": 2
    },
    {
      "id": "richiesta-aiuto-clinico",
      "ricerca_origine": "ricerca-02-pointing-precoce",
      "dispositivo_sorgente": "pointing/correzione-strutturale-clinico-v2.json",
      "steps_completed": ["f3-step-7","f3-step-8","f3-step-9","f3-step-10"],
      "steps_skipped": [],
      "external_inputs": [
        { "step": "f3-step-7", "file": "f3-step-7-contesto-clinico.json", "type": "esterno_obbligatorio", "label": "Contesto clinico neuropsviluppo" },
        { "step": "f3-step-10", "file": "f3-step-10-casi-clinico.json", "type": "esterno_obbligatorio", "label": "Casi stress test dominio clinico" }
      ],
      "dispositivo_file": "dispositivo-richiesta-aiuto-clinico-v1.json",
      "stress_test_file": "stress-test-richiesta-aiuto-v1.json",
      "robustezza": "alta",
      "correzioni_residue": 0
    }
  ]
}
```

---

### 7. Note di implementazione

**Non mostrare mai il JSON grezzo** all'utente. Tutta la visualizzazione deve essere una trasformazione dei dati in componenti leggibili.

**Gestione `non_classificabile`**: in tutto il sistema, questo output ha un valore epistemico positivo (è la risposta corretta a dati insufficienti, non un fallimento). Non trattarlo come errore nella UI — usare grigio neutro, non rosso.

**I testi descrittivi** (function, description, what_it_reads, ecc.) sono stringhe lunghe e ben scritte. Mostrarle per intero, senza troncamento, in blocchi di testo leggibili.

**Mobile**: la sezione è progettata per desktop (analisi densa). Su mobile mostrare solo PipelineMap e accesso alle card di riepilogo — il dettaglio richiede schermo largo.

**JSON index**: creare e mantenere `pipeline-index.json` come file di configurazione che lista le ricerche e i temi disponibili con i loro step completati. Questo permette alla webapp di sapere cosa caricare senza scandire il filesystem.

---

## Priorità di implementazione

1. **Prima**: PipelineMap + DeviceViewer (massimo valore, minima dipendenza da altri step)
2. **Seconda**: StressTestDashboard + CorrectionsLog (analitico, specifico)
3. **Terza**: DeviceLineage — Input Graph + Input Provenance Panel (tracciabilità)
4. **Quarta**: ProcessNarrative da revisioni.md (storia decisionale)
5. **Quinta**: ThemeExplorer F2 + ProxyEvolution + Comparative View

---

## Integrazioni tra componenti

Le sezioni di tracciabilità (§6) non sono componenti separati ma si integrano nei componenti principali come layer aggiuntivo:

| Componente principale | Integrazione tracciabilità |
|---|---|
| DeviceViewer | Tab "Provenienza" → Input Provenance Panel (§6.2) |
| DeviceViewer | Tab "Storia" → ProcessNarrative da revisioni.md (§6.4) |
| StressTestDashboard | Link da `breaking_point` dei casi → CorrectionsLog (§6.3) |
| StressTestDashboard | Header con Input Provenance: "Casi forniti da / costruiti autonomamente" |
| PipelineMap | Nodi cliccabili → espandono Input Graph (§6.1) |
| DeviceOverview | Pannello laterale con grafo derivazione semplificato |

**Principio**: la tracciabilità non è una sezione separata da visitare — è disponibile come layer contestuale ovunque ci sia un risultato da spiegare.
