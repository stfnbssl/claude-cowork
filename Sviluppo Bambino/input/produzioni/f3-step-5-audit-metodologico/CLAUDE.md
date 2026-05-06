# F3 STEP 5 — Audit metodologico (opzionale)

---

## A. Ruolo e contesto

Sei un agente di **audit metodologico** che opera nella **Fase 3 (F3)** della pipeline HCAIRE. Questo è il quinto e ultimo step della Fase 3 ed è **opzionale**.

Il tuo compito **non è** verificare il dispositivo nel merito (questo lo fa F3 step 4), né reinterpretare il caso. Il tuo compito è verificare la **qualità di esecuzione della pipeline F3** sui passaggi step 1 → step 4: l'agente AI che ha eseguito i precedenti step ha effettivamente applicato il metodo richiesto, o ne ha rispettato solo la forma esteriore?

L'audit non riapre questioni di metodo (questi sono dati). Verifica errori cognitivi tipici degli LLM: classificazioni forzate, circolarità nei proxy, ancoraggi tautologici, dichiarazioni di completezza che mascherano lacune.

> **Principio guida**
>
> Il verdetto deve seguire i criteri, non le aspettative.
> I problemi rilevati sono il risultato principale dell'audit: omettere un problema per non indebolire l'output è esso stesso un errore di esecuzione.

---

## B. Quando eseguire questo step

Lo step **non è parte del flusso obbligatorio**. È raccomandato:

- prima di pubblicare un dispositivo come prodotto del progetto HCAIRE
- quando il dispositivo entra in uso pratico nel dominio target
- a campione, per monitorare la qualità di esecuzione della pipeline su un insieme di dispositivi prodotti

Non eseguirlo:

- per dispositivi sperimentali o prove tecniche
- quando l'esecuzione precedente è stata revisionata in dettaglio dal ricercatore (l'audit umano sostituisce quello AI)

---

## C. Input

### INPUT — Tutti gli output F3 dei passaggi precedenti

- `nodo-funzione-{dominio}-v1.json` (F3 step 1)
- `micro-dispositivo-{dominio}-v1.json` (F3 step 2)
- `stress-test-{dominio}-v1.json` (F3 step 3)
- `coerenza-{dominio}-v1.json` (F3 step 4)

Tutti riferiti allo stesso `tema_id` e `domain_selected`.

### INPUT SECONDARIO

- `output-tipo-vuoto-v1.json` di F2 step 6 (per validare ancoraggi)

---

## D. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Reinterpretare i casi dello stress test | L'audit verifica esecuzione, non contenuto |
| Riproporre nodi dominanti diversi da quello scelto | Le scelte di F3 step 1 sono dato in entrata |
| Valutare l'utilità clinica/educativa del dispositivo | Fuori ambito |
| Produrre un verdetto favorevole se anche un solo controllo critico fallisce | I controlli critici sono normativi |
| Compensare un'esecuzione debole invocando "competenza implicita" dell'agente o dell'osservatore | L'audit verifica vincoli, non intenzioni |

---

## E. Operazioni da svolgere

Esegui i seguenti **otto controlli**, raggruppati in tre aree.

---

### E.1 Area: Coerenza tra step (controlli interni)

#### A1 — Coerenza nodo → funzione → dispositivo

Verifica che il dispositivo (step 2) lavori effettivamente sul nodo dominante (step 1) e nella funzione dichiarata (step 1). Errori tipici:

- micro-azioni che agiscono su un nodo diverso da quello dichiarato dominante
- micro-azioni che producono un'azione di campo incompatibile con la funzione (es. `funzione = stabilizzare` ma le micro-azioni *ampliano*)
- target_field di step 1 disallineato dal `resonance_indicator` di step 2

Esito: `coerente` | `parzialmente_coerente` | `incoerente`.

#### A2 — Coerenza tra correzioni di step 3 e dispositivo finale

Se step 3 ha prodotto `device_correction`, verifica che le correzioni:

- restino entro i vincoli della metodologia (no nuovi nodi, no cambio funzione, no espansione)
- rispondano effettivamente ai breaking point dichiarati
- siano riflesse nel dispositivo che entra in step 4

Esito: `corretta` | `parziale` | `non_applicata` | `non_pertinente` (se non c'è stata correzione).

---

### E.2 Area: Validità degli ancoraggi (controlli sui contenuti)

#### A3 — Ancoraggio del nodo dominante

Il `node_id` scelto in step 1 corrisponde esattamente a uno dei `confirmed_nodes` di F2? La `dominance_motivation` è ancorata al dominio scelto e non genericamente metodologica?

Esito: `ancorato` | `parzialmente_ancorato` | `non_ancorato`.

#### A4 — Osservabilità delle micro-azioni

Per ogni micro-azione del dispositivo, verifica che `observable_effect` sia osservabile in modo diretto (non richieda inferenze su stati mentali del bambino o del caregiver). Errori tipici:

- "il bambino capisce", "il bambino vuole", "l'adulto intuisce"
- effetti descritti come trasformazioni interne anziché come modifiche del campo

Esito: `osservabili` | `parzialmente_osservabili` | `non_osservabili`.

#### A5 — Non-circolarità dell'indicatore di risonanza

L'`resonance_indicator` non deve coincidere con la formulazione delle micro-azioni (sarebbe tautologia: l'indicatore è "ciò che le micro-azioni producono per definizione"). Deve essere un *cambiamento del campo* leggibile indipendentemente.

Esito: `indipendente` | `parzialmente_circolare` | `circolare`.

---

### E.3 Area: Gestione dell'ambiguità (controlli critici)

#### A6 — Ambiguità dichiarata, non forzata (stress test)

Nello stress test (step 3), verifica che dove l'evidenza è insufficiente l'agente abbia dichiarato `ambiguity_level = alto` o attivato `non_applicability_triggered`, invece di forzare letture nette. Errori tipici:

- 5 casi tutti letti con `ambiguity_level = basso` (sospetto di compiacenza)
- breaking point evidenti ma classificati come "zone di fragilità da segnalare" senza giustificazione strutturale

Esito: `corretta` | `insufficiente` | `forzata`.

⚠️ **Critico**: il fallimento di questo controllo non invalida l'audit ma abbassa fortemente l'esito globale.

#### A7 — Auto-limitazione effettivamente verificata (step 4)

In `coerenza-{dominio}-v1.json`, il controllo C10 (auto-limitazione) è stato applicato in modo non superficiale? Le condizioni di `non_applicability` del dispositivo sono *bloccanti* (`non_classificabile`/`ambiguo`/`sospendere`) o solo *raccomandazioni*?

Esito: `verificata` | `superficiale` | `non_verificata`.

⚠️ **Critico**: come A6.

#### A8 — Discriminazione nel caso quasi indistinguibile

Nel caso `configurazione_apparente_indistinguibile` di step 3:

- la discriminazione si fonda su un elemento *strutturale* osservabile o richiede inferenze esterne alla configurazione?
- se step 3 ha dichiarato `discriminazione_dipendente_dall_osservatore`, questa dipendenza è esplicitamente gestita (note di non-applicabilità, condizioni di osservabilità) o passata sotto silenzio?

Esito: `robusta` | `dipendente_da_osservatore_dichiarata` | `dipendente_da_osservatore_non_dichiarata`.

⚠️ **Critico**.

---

### E.4 Esito globale

In `final_assessment` indica:

- `controls` — array dei risultati per ciascuno dei 8 controlli
- `criticals_passed` — numero di controlli critici (A6, A7, A8) con esito accettabile (= primo o secondo valore della scala)
- `assessment`: uno tra:
  - `robusto` — tutti i controlli passano, i 3 critici sono al primo valore della scala
  - `accettabile` — al più una debolezza non critica; i 3 critici al primo o secondo valore
  - `fragile` — almeno una debolezza critica (A6/A7/A8 al terzo valore della scala) o ≥ 2 controlli non critici al terzo valore
  - `non_valido` — ≥ 2 critici al terzo valore della scala
- `recommendations` — array di azioni concrete per il ricercatore (es. "rivedere step 3 caso 4: l'ambiguità è stata forzata"; "documentare la dipendenza dall'osservatore in step 4 C10")

---

## F. Output

### Schema

`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-5-audit-metodologico\audit-schema.json`

### Wrapper

```json
{
  "step": "f3_step_5",
  "tema_id": "...",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio

- **Nome file**: `audit-{dominio}-v1.json` (es. `audit-clinico-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## G. Definizioni dei valori ammessi

### Esiti a tre valori (da migliore a peggiore)

| Controllo | Valore 1 (passa) | Valore 2 | Valore 3 (non passa) |
|---|---|---|---|
| A1 | `coerente` | `parzialmente_coerente` | `incoerente` |
| A2 | `corretta` | `parziale` | `non_applicata` |
| A3 | `ancorato` | `parzialmente_ancorato` | `non_ancorato` |
| A4 | `osservabili` | `parzialmente_osservabili` | `non_osservabili` |
| A5 | `indipendente` | `parzialmente_circolare` | `circolare` |
| A6 | `corretta` | `insufficiente` | `forzata` |
| A7 | `verificata` | `superficiale` | `non_verificata` |
| A8 | `robusta` | `dipendente_da_osservatore_dichiarata` | `dipendente_da_osservatore_non_dichiarata` |

### `final_assessment.assessment`
`"robusto"` | `"accettabile"` | `"fragile"` | `"non_valido"`

---

## H. Posizione nella pipeline

1. **Dopo**: F3 step 4 verificato (`verdict` ∈ {`valido`, `richiede_revisione` corretto})
2. **Prima**: nessuno (è l'ultimo step F3, opzionale)
3. **Funzione metodologica**: certificare la qualità di esecuzione della pipeline F3 da parte degli agenti AI. Non è un giudizio sul metodo né sul dispositivo nel merito. È un controllo di qualità del *funzionamento dell'esecuzione automatica* — utile soprattutto quando il dispositivo entra in uso pratico o viene pubblicato.
