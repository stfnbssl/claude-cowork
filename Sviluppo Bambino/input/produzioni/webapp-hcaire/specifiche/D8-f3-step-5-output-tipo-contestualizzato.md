# D8 — F3 step 5 redesign — migrazione per Claude Code

> **Destinatario**: Claude Code — leggere D7 prima di questo documento. D8 è un delta su D7: modifica esclusivamente `f3_step_5`, lasciando invariati tutti gli altri step F2 e F3.
>
> **Cosa cambia**: `f3_step_5` passa da "Audit metodologico (opzionale)" a "Output-tipo contestualizzato". Si tratta di uno step completamente nuovo nel ruolo metodologico: non verifica l'esecuzione della pipeline, produce l'**artefatto finale pubblico** della pipeline F3 — la versione del modulo triadico (sezioni A–E dell'output-tipo vuoto di F2) contestualizzata per il dominio scelto. È ciò che il sito HCAIRE presenta come "strumento operativo".
>
> **Per tutto ciò che D8 non menziona, prevale D7. Per `f3_step_5`, prevale D8.**

---

## 1. Sintesi delle modifiche

| File / sistema | Modifica |
|---|---|
| `pipeline-step-config.json` | Entry `f3_step_5`: label, output_prefix, path, schema, can_skip, inputs_pipeline, _note |
| `STEP_CLAUDE_FILE_MAP` (server locale Cowork — D6 §1) | Path CLAUDE.md di `f3_step_5` |
| `D5b` §5.2 — TimelineRail vista Dispositivo | Etichetta e glifo dell'ultimo step |
| `D5b` §6.5 — WorkbenchOutputPanel mapping preview | Componente di preview per `f3_step_5` |
| `input/produzioni/f3-step-5-output-tipo-contestualizzato/` | ✅ Già aggiornata (CLAUDE.md e schema riscritti, cartella rinominata) |

---

## 2. `pipeline-step-config.json`

### 2.1 Entry da sostituire

Sostituire integralmente l'entry `f3_step_5` con:

```json
{
  "id": "f3_step_5",
  "label": "Output-tipo contestualizzato",
  "phase": "F3",
  "_note": "r3+D8: ultimo step obbligatorio della pipeline F3. Produce la versione del modulo triadico A–E contestualizzata per il dominio scelto (§3.3 della metodologia). È l'artefatto che il sito HCAIRE presenta come strumento operativo. Non è un audit della pipeline: produce un output sostantivo.",
  "output_prefix": "output-tipo",
  "output_path_template": "temi/{tema_id}/output-tipo-{dominio}-v{N}.json",
  "inputs_pipeline": [
    { "step": "f3_step_4", "role": "coerenza", "required": true, "_note": "Verifica che il dispositivo abbia verdict valido prima di contestualizzare" },
    { "step": "f3_step_3", "role": "stress-test", "required": true, "_note": "Per accedere al dispositivo corretto se step 3 ha prodotto device_correction" },
    { "step": "f3_step_2", "role": "micro-dispositivo", "required": true, "_note": "Dispositivo base; sostituito dalla versione corretta di step 3 se presente" },
    { "step": "f2_step_6", "role": "output-tipo-vuoto", "required": true, "_note": "Struttura triadica astratta A–E da contestualizzare" },
    { "step": "f3_step_1", "role": "nodo-funzione", "required": true, "_note": "Fornisce domain_selected e context_label" }
  ],
  "inputs_strutturali": [
    "f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json"
  ],
  "inputs_esterni": [],
  "verifica": false,
  "can_skip": false,
  "blocks": []
}
```

### 2.2 Aggiornare `_version`

```json
"_version": "3.1"
```

### 2.3 Cosa cambia rispetto all'entry D7

| Campo | Valore D7 | Valore D8 |
|---|---|---|
| `label` | `"Audit metodologico (opzionale)"` | `"Output-tipo contestualizzato"` |
| `output_prefix` | `"audit"` | `"output-tipo"` |
| `output_path_template` | `"temi/{tema_id}/audit-{dominio}-v{N}.json"` | `"temi/{tema_id}/output-tipo-{dominio}-v{N}.json"` |
| `inputs_strutturali[0]` | `"f3-step-5-audit-metodologico/audit-schema.json"` | `"f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json"` |
| `inputs_pipeline` | step 1–4 | step 1–4 + `f2_step_6` (aggiunto) |
| `can_skip` | `true` | `false` |
| `skip_condition` | presente | **rimosso** |
| `_note` | descrive audit opzionale | descrive output sostantivo finale |

---

## 3. Server locale Cowork — `STEP_CLAUDE_FILE_MAP` (D6 §1)

Aggiornare il mapping di `f3_step_5`:

```javascript
// Prima (D7):
'f3_step_5': 'f3-step-5-audit-metodologico/CLAUDE.md',

// Dopo (D8):
'f3_step_5': 'f3-step-5-output-tipo-contestualizzato/CLAUDE.md',
```

### 3.1 Nota sul filesystem

La cartella `f3-step-5-output-tipo-contestualizzato/` contiene due file di schema:
- `output-tipo-schema.json` — schema attivo (D8)
- `audit-schema.json` — file legacy residuo (non eliminabile per permessi del mount) — ignorare

Il `PromptComposer` non carica i file `.json`, quindi la presenza del file legacy è inerte.

---

## 4. Frontend — D5b aggiornamenti

### 4.1 TimelineRail vista Dispositivo (D5b §5.2)

La lista degli step F3 nella timeline va aggiornata:

```
// Prima (D7):
○  f3_step_5 — Audit metodologico (opz.)

// Dopo (D8):
○  f3_step_5 — Output-tipo contestualizzato
```

Nessun glifo `✎` (nessun input esterno). Nessun tag `(opz.)` (lo step non è più skippable).

### 4.2 WorkbenchOutputPanel — mapping preview (D5b §6.5)

| Step | Componente di preview (D7) | Componente di preview (D8) |
|---|---|---|
| `f3_step_5` | `AuditViewer` (NUOVO) | `OutputTipoViewer` (NUOVO, opzionale) o JSON pretty-printed |

**Per la prima implementazione**: il fallback JSON pretty-printed è sufficiente. `OutputTipoViewer` può essere introdotto in una tappa successiva.

Quando implementato, `OutputTipoViewer` deve mostrare:
- Le 5 sezioni A–E con `section_label`, `domain_examples` (lista), `linguistic_frame`, `decisional_nodes` (lista)
- `narrative_synthesis` (paragrafo evidenziato — è la voce del ricercatore)
- `orientative_direction` (frase distinta, non confondere con prescrizione)
- `dispositivo_ref` (collassabile — rimanda al dispositivo senza duplicarlo)

---

## 5. Modifica al `pipeline-step-config.json` — istruzione operativa

Il file si trova in:

```
input/produzioni/webapp-hcaire/pipeline-step-config.json
```

Sostituire l'oggetto il cui `"id"` è `"f3_step_5"` con il JSON del §2.1. Aggiornare `_version` a `"3.1"`.

**Attenzione**: non modificare nessun'altra entry. Le entry F2 e F3 step 1–4 restano invariate rispetto a D7.

---

## 6. Filesystem `produzioni/` — stato attuale

✅ Nessuna operazione richiesta. Le cartelle e i file sono già nel corretto stato:

```
input/produzioni/f3-step-5-output-tipo-contestualizzato/
  CLAUDE.md                    ← riscritto (D8)
  output-tipo-schema.json      ← nuovo (D8)
  audit-schema.json            ← legacy residuo (ignorare)
```

---

## 7. MongoDB — nessuna modifica strutturale

Schema delle collection invariato rispetto a D7. I documenti `pipeline_step_executions` con `step_id = "f3_step_5"` prodotti prima di D8 (audit outputs) avranno struttura diversa dall'output atteso dal nuovo schema. Trattarli come prove tecniche: segnare come `cancellato` con motivazione `"migrazione D8"` oppure ignorare (non saranno più referenziati dal motore r3.1).

---

## 8. Criteri di accettazione

### 8.1 Configurazione

- [ ] `pipeline-step-config.json._version === "3.1"`
- [ ] `f3_step_5.label === "Output-tipo contestualizzato"`
- [ ] `f3_step_5.output_prefix === "output-tipo"`
- [ ] `f3_step_5.can_skip === false`
- [ ] `f3_step_5.skip_condition` assente
- [ ] `f3_step_5.inputs_strutturali[0]` punta a `f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json`
- [ ] `f3_step_5.inputs_pipeline` include `f2_step_6` come required

### 8.2 Server locale

- [ ] `STEP_CLAUDE_FILE_MAP['f3_step_5']` punta a `f3-step-5-output-tipo-contestualizzato/CLAUDE.md`
- [ ] Lanciando `f3_step_5`, il `PromptComposer` carica il nuovo CLAUDE.md

### 8.3 Esecuzione end-to-end

- [ ] `f3_step_5` si abilita automaticamente dopo che `f3_step_4` è completato con `verdict` ∈ {`valido`, `richiede_revisione`}
- [ ] L'output prodotto è validato da `output-tipo-schema.json` (sezioni A–E, `narrative_synthesis`, `orientative_direction`, `dispositivo_ref`)
- [ ] Il file di output è salvato come `output-tipo-{dominio}-v1.json` nella cartella del tema
- [ ] Lo step non ha pulsante "Salta" nell'interfaccia (can_skip = false)

### 8.4 Frontend

- [ ] La TimelineRail mostra `f3_step_5` come "Output-tipo contestualizzato" senza tag `(opz.)`
- [ ] L'avanzamento N/5 nel `ContestualizzazioniSection` funziona correttamente (lo step 5 conta come passo obbligatorio)
- [ ] Il pannello output mostra almeno il fallback JSON pretty-printed

### 8.5 No-regressioni

- [ ] Le entry F2 e F3 step 1–4 del `pipeline-step-config.json` non sono state modificate
- [ ] La pipeline F2 esegue identicamente
- [ ] Le pagine read-only esistenti non sono toccate

---

## 9. Riferimenti

- **Metodologia**: `HCAIRE Slides/context/metodo/f3-strumenti-operativi.md` — §3.3 (riempimento output-tipo in F3)
- **CLAUDE.md step**: `input/produzioni/f3-step-5-output-tipo-contestualizzato/CLAUDE.md`
- **Schema JSON step**: `input/produzioni/f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json`
- **Configurazione orchestrazione**: `input/produzioni/webapp-hcaire/pipeline-step-config.json` (target: v3.1)
- **Documento precedente**: `D7-pipeline-f3-redesign.md` (per contesto generale della migrazione F3)
- **Documenti da integrare**:
  - `D6-server-locale-cowork.md` §1 — `STEP_CLAUDE_FILE_MAP` (aggiornare path `f3_step_5`)
  - `D5b-laboratorio-workbench.md` §5.2 e §6.5 (timeline label + preview component)

---

**Fine documento.**

Per tutto ciò che riguarda `f3_step_5`, questo documento sostituisce D7. Per F2, F3 step 1–4 e il modello architetturale generale, prevale D7.
