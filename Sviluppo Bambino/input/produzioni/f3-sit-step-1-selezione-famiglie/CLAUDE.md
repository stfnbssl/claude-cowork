# F3-SIT STEP 1 — Selezione delle famiglie situazionali

---

## A. Ruolo e contesto

Sei un agente analitico che opera nel **modulo F3-SIT** della pipeline HCAIRE. Questo è il primo dei quattro step del modulo.

F3-SIT — *Repertorio Situazionale di Micro-mediazioni* — è un **modulo derivato opzionale di Fase 3**: si attiva dopo il completamento di F3 (`f3_step_5`) e produce materiali situazionali, esemplificativi e formativi (casistiche, frasi, atteggiamenti, micro-scenari, vignette, storyboard, linee guida, prompt per AI) derivati dal dispositivo F3 già validato. Specifica completa del modulo: `webapp-hcaire/specifiche/D9-pipeline-f3-sit.md`.

In questo step **non produci ancora materiale**. Compi un solo atto: **decidere quali famiglie F3-SIT sono pertinenti** per il tema × dominio, con quale priorità e per quali destinatari. Lo step produce la *mappa* di ciò che gli step successivi dovranno produrre.

> **Principio guida**
>
> Non tutti i dispositivi richiedono tutte le famiglie. Per un dominio clinico può essere centrale il repertorio di frasi per operatori; per un dominio scuola la vignetta formativa; per un dominio genitoriale le frasi per caregiver. Selezionare una famiglia che il dominio non richiede produce materiale generico, non strumento HCAIRE.
>
> La selezione parte dal **dispositivo validato**, non dal tema. F3-SIT incarna una configurazione già letta, non genera consigli a partire da un argomento.

---

## B. Input

### INPUT PRIMARIO — Output-tipo contestualizzato (F3 step 5)

`...\output\produzioni\temi\[nome-tema]\output-tipo-{dominio}-v1.json`

Il prodotto finale di F3: la struttura triadica letta nel contesto del dominio scelto. È il riferimento per capire quale forma comunicativa serve.

### INPUT SECONDARI — F3 step 1 e step 2

- `nodo-funzione-v1.json` (F3 step 1) — nodo dominante, funzione, campo bersaglio. Sono i campi di tracciabilità che ogni item F3-SIT dovrà ereditare.
- `micro-dispositivo-v1.json` (F3 step 2) — il dispositivo, con la classificazione universale U1–U6.

### INPUT FACOLTATIVO — Stress test (F3 step 3)

`stress-test-v1.json` — usato per stimare la pertinenza della famiglia "casistiche situazionali" (F3-SIT-1), che si nutre dei 5 casi tipologici.

### INPUT STRUTTURALE — Tassonomia delle famiglie

`...\input\produzioni\f3-sit-famiglie.json` — le 9 famiglie F3-SIT con `family_id`, uso principale, destinatari tipici e flag `narrative`.

### INPUT ESTERNO — FACOLTATIVO

**Destinazione d'uso** (`destinazione_uso`): indicazione del ricercatore su destinatari e uso previsto del materiale. Campi possibili:

- `intended_use`: es. formazione operatori | orientamento genitori | sito HCAIRE | schede pratiche | supervisione
- `priority_target_users`: elenco di destinatari prioritari
- `notes`: note libere

Se assente, la selezione si basa solo sugli input pipeline. Lo schema di questo input non è materializzato come file: è descritto qui e validato alla ricezione.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Selezionare famiglie non presenti in `f3-sit-famiglie.json` | La tassonomia delle 9 famiglie è chiusa |
| Produrre già frasi, scene o materiale | Questo step seleziona, non genera: il materiale è degli step 2 e 3 |
| Selezionare una famiglia senza motivarne la pertinenza al dominio | Una famiglia senza ragione strutturale è materiale generico |
| Far derivare la selezione dal tema anziché dal dispositivo validato | F3-SIT parte dalla configurazione letta, non dall'argomento |
| Selezionare tutte e 9 le famiglie "per completezza" | La selezione è una scelta: includere tutto equivale a non scegliere |

---

## D. Operazioni da svolgere

### D.1 Lettura del dispositivo validato

Dagli input pipeline estrai e fissa i **campi di tracciabilità** che orienteranno tutta la selezione:

- nodo dominante (`dominant_node.node_id` da F3 step 1)
- funzione (`function.function_type`)
- campo bersaglio (`target_field.field_label`)
- forme universali del dispositivo (`universal_form.forms[]` da F3 step 2)

### D.2 Valutazione delle 9 famiglie

Per ciascuna delle 9 famiglie di `f3-sit-famiglie.json`, valuta se è pertinente per *questo* tema × dominio. Criteri:

- la famiglia ha un destinatario reale nel dominio scelto?
- la forma comunicativa della famiglia aiuta a rendere abitabile il campo letto dal dispositivo?
- la famiglia è coerente con la funzione del dispositivo (stabilizzare / ampliare / mediare / proteggere)?

### D.3 Costruzione di `selected_families`

Per ogni famiglia selezionata produci un elemento di `selected_families` con:

- `family_id` — uno dei 9 `family_id` della tassonomia
- `family_name` — nome leggibile
- `priority` — `alta` | `media` | `bassa`
- `target_user` — destinatario principale (tra i `target_user_values` della tassonomia)
- `reason` — perché questa famiglia è pertinente *in questo dominio* (non in astratto)
- `expected_items` — numero indicativo di item attesi (intero, 2–8)

### D.4 Costruzione di `excluded_families`

Per ogni famiglia non selezionata produci un elemento di `excluded_families` con `family_id` e `reason` (perché non è pertinente). Le famiglie escluse non scompaiono: restano tracciabili con motivazione.

### D.5 Flag delle famiglie narrative

Imposta `narrative_families_selected` a `true` se almeno una famiglia selezionata ha `narrative: true` nella tassonomia (F3-SIT-6, 7, 8, 9), altrimenti `false`. Questo flag determina se `f3_sit_step_3` verrà eseguito o saltato.

---

## E. Output

### Schema

`...\input\produzioni\f3-sit-step-1-selezione-famiglie\sit-famiglie-schema.json`

### Wrapper

```json
{
  "step": "f3_sit_step_1",
  "tema_id": "...",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio

- **Nome file**: `sit-famiglie-v1.json`
- **Cartella**: `...\output\produzioni\temi\[nome-tema]\sit\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `selected_families[].priority`
`"alta"` | `"media"` | `"bassa"`

### `selected_families[].target_user`
`"pediatra"` | `"educatore"` | `"insegnante"` | `"bibliotecario"` | `"genitore"` | `"caregiver"` | `"formatore"`

### `narrative_families_selected`
`true` | `false` — `true` se è selezionata almeno una tra F3-SIT-6, F3-SIT-7, F3-SIT-8, F3-SIT-9.

---

## G. Verifica

Questo step ha **verifica umana obbligatoria** (`verifica.md` presente nella cartella). È il punto in cui il ricercatore decide la destinazione comunicativa del materiale: una selezione sbagliata qui propaga su tutto il modulo. Applicare `verifica.md` prima di procedere a `f3_sit_step_2`.

---

## H. Posizione nella pipeline

1. **Dopo**: F3 step 5 completato (`output-tipo-{dominio}-v1.json` esistente per il tema × dominio).
2. **Prima**: `f3_sit_step_2` (generazione delle micro-mediazioni).
3. **Funzione metodologica**: trasformare F3-SIT da raccolta libera di esempi a ramo controllato. La selezione delle famiglie àncora la produzione situazionale alla configurazione letta e alla destinazione d'uso reale, evitando che il modulo generi materiale comunicativo non richiesto dal dominio.
