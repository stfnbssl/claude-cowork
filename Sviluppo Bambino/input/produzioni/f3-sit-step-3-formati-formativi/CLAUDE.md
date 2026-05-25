# F3-SIT STEP 3 — Trasformazione formativa e narrativa

---

## A. Ruolo e contesto

Sei un agente che opera nel **modulo F3-SIT** della pipeline HCAIRE (specifica: `webapp-hcaire/specifiche/D9-pipeline-f3-sit.md`). Questo è il terzo dei quattro step del modulo.

In questo step trasformi le micro-mediazioni prodotte da `f3_sit_step_2` in **materiali comunicativi e formativi** per le famiglie narrative selezionate in `f3_sit_step_1`: vignette formative (F3-SIT-6), storyboard per fumetto/video (F3-SIT-7), linee guida narrative non prescrittive (F3-SIT-8), prompt per AI generativa (F3-SIT-9).

> **Principio guida**
>
> Il tratto HCAIRE di ogni materiale narrativo è il contrasto tra **lettura ingenua** e **lettura configurazionale** della stessa scena. La vignetta, lo storyboard, la linea guida non insegnano "cosa fare": mostrano la differenza tra moralizzare il campo e riconfigurarlo.
>
> Il materiale resta tracciabile a nodo, funzione e dispositivo: la forma diventa comunicativa, l'ancoraggio resta strutturale.

> **Skip dello step**
>
> Questo step si esegue **solo se** `f3_sit_step_1` ha impostato `narrative_families_selected: true` (almeno una famiglia tra F3-SIT-6, 7, 8, 9 selezionata). Se nessuna famiglia narrativa è selezionata, lo step è **saltato**: lo skip va registrato con motivazione in `revisioni.md` e in `steps_skipped`, e la pipeline passa direttamente a `f3_sit_step_4`.

---

## B. Input

### INPUT PRIMARIO — Micro-mediazioni (F3-SIT step 2)

`...\output\produzioni\temi\[nome-tema]\sit\sit-micro-mediazioni-v1.json`

Gli item situazionali da cui derivano i materiali narrativi. Ogni materiale narrativo dovrebbe collegarsi a uno o più item tramite `source_sit_id`.

### INPUT SECONDARIO — Selezione delle famiglie (F3-SIT step 1)

`sit-famiglie-v1.json` — per sapere quali famiglie narrative produrre (`selected_families` con `family_id` ∈ F3-SIT-6…9) e con quale priorità.

### INPUT FACOLTATIVO — Stress test (F3 step 3)

`stress-test-v1.json` — i casi tipologici possono alimentare scene di vignette e storyboard.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Produrre formati per famiglie narrative non selezionate in step 1 | Lo step 1 ha già deciso cosa serve |
| Produrre un materiale privo di `configurational_reading` | Senza la lettura configurazionale il materiale è un racconto morale, non F3-SIT |
| Trasformare l'adulto in "salvatore onnipotente" o il bambino in "caso" | Il materiale riconfigura il campo, non eroicizza né etichetta |
| Ridicolizzare terzi (compagni, gruppo) per fare contrasto | Il contrasto è tra letture, non tra personaggi buoni e cattivi |
| Produrre prompt AI senza vincoli di tono ed elementi da evitare | Un prompt senza vincoli riproduce gli stereotipi che il metodo vuole evitare |
| Perdere il legame con nodo, funzione e dispositivo | La forma diventa comunicativa, l'ancoraggio resta strutturale |

---

## D. Operazioni da svolgere

### D.1 Per ogni famiglia narrativa selezionata, produrre i `training_outputs`

Ogni elemento di `training_outputs` ha:

- `format_id` — `vignetta` | `storyboard` | `linea_guida` | `prompt_ai`
- `family_id` — la famiglia narrativa corrispondente (F3-SIT-6 → vignetta, F3-SIT-7 → storyboard, F3-SIT-8 → linea_guida, F3-SIT-9 → prompt_ai)
- `title` — titolo del materiale
- `source_sit_id` — `sit_id` dell'item di step 2 da cui deriva (`null` se deriva direttamente dal dispositivo)
- `configurational_basis` — campi di tracciabilità (`dominant_node`, `function`, `target_field`, `universal_device_type`, `source_device_id`)
- `naive_reading` — la lettura ingenua / immediata della scena (`null` per `linea_guida` e `prompt_ai` se non pertinente)
- `configurational_reading` — la lettura configurazionale: quali nodi sono attivi, quali si restringono, quale direzione dinamica — **obbligatoria per ogni materiale**
- `content` — descrizione del materiale: scena e intervento adulto per la vignetta; principio e orientamento per la linea guida; obiettivo e configurazione da rappresentare per il prompt AI
- `panels` — solo per `storyboard`: sequenza di pannelli, ciascuno con `panel` (numero), `visual_description`, `dialogue`, `field_function` (la funzione di campo della scena)
- `discussion_questions` — domande per la discussione formativa (utili soprattutto per vignette; elenco, può essere vuoto)
- `ai_generation_prompt` — solo per `prompt_ai` (e opzionalmente storyboard): il prompt vero e proprio, con vincoli di tono ed elementi da evitare (`null` se non pertinente)
- `non_prescriptive_note` — perché il materiale orienta senza prescrivere
- `methodological_warnings` — eventuali cautele (elenco, può essere vuoto)

### D.2 Struttura della vignetta (F3-SIT-6)

Scena → lettura ingenua → lettura configurazionale → intervento adulto non prescrittivo → effetto sul campo → domanda per discussione.

### D.3 Struttura dello storyboard (F3-SIT-7)

Cinque pannelli tipici: (1) configurazione iniziale del campo; (2) restringimento / collasso / ritiro; (3) intervento adulto non prescrittivo; (4) micro-riapertura del campo; (5) chiusura formativa. Per ogni pannello: descrizione visiva, dialogo, funzione di campo.

### D.4 Struttura della linea guida (F3-SIT-8)

Quando accade → principio di lettura → orientamento operativo → cosa evitare → esempio. Testo sintetico, non protocollo.

### D.5 Struttura del prompt AI (F3-SIT-9)

Obiettivo → pubblico → configurazione da rappresentare → vincoli di tono → scene richieste → elementi da evitare → output desiderato.

---

## E. Output

### Schema

`...\input\produzioni\f3-sit-step-3-formati-formativi\sit-formati-schema.json`

### Wrapper

```json
{
  "step": "f3_sit_step_3",
  "tema_id": "...",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio

- **Nome file**: `sit-formati-v1.json`
- **Cartella**: `...\output\produzioni\temi\[nome-tema]\sit\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `training_outputs[].format_id`
`"vignetta"` | `"storyboard"` | `"linea_guida"` | `"prompt_ai"`

### `training_outputs[].family_id`
`"F3-SIT-6"` | `"F3-SIT-7"` | `"F3-SIT-8"` | `"F3-SIT-9"`

### `training_outputs[].configurational_basis.function`
`"stabilizzare"` | `"ampliare"` | `"mediare"` | `"proteggere"`

---

## G. Verifica

Verifica umana **facoltativa** — raccomandata se il materiale è destinato al sito HCAIRE o alla formazione. Lo step può procedere direttamente a `f3_sit_step_4`.

---

## H. Posizione nella pipeline

1. **Dopo**: `f3_sit_step_2` (micro-mediazioni). Eseguito solo se `narrative_families_selected: true`.
2. **Prima**: `f3_sit_step_4` (verifica e pacchetto repertorio).
3. **Funzione metodologica**: rendere il metodo *mostrabile*. Trasforma le micro-mediazioni in materiali che possono essere usati per formazione, orientamento dei genitori, pagine del sito, fumetti e video — senza perdere il legame con la configurazione di campo.
