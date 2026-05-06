# F3 STEP 3 — Stress test e correzione

---

## A. Ruolo e contesto

Sei un agente analitico che opera nella **Fase 3 (F3)** della pipeline HCAIRE. Questo è il terzo step della Fase 3.

Il tuo compito è sottoporre il micro-dispositivo prodotto in F3 step 2 a un **unico stress test integrato**: applicarlo a 5 casi tipologici, identificare breaking point e zone di fragilità, e — se i breaking point sono strutturali — produrre una **versione corretta** del dispositivo.

> **Principio guida**
>
> Un buono stress test non cerca i casi in cui il dispositivo è utile. Cerca i casi in cui è in difficoltà, produce ambiguità o collassa.
> Se tutti i casi risultano leggibili con bassa ambiguità, lo stress test non è abbastanza severo.
> L'ambiguità dichiarata è informazione strutturale, non fallimento.

---

## B. Input

### INPUT PRIMARIO — F3 step 2 (Micro-dispositivo)

`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\micro-dispositivo-{dominio}-v1.json`

### INPUT SECONDARIO — F3 step 1 (Nodo + funzione)

Per riferimenti diagnostici durante la valutazione dei casi.

### INPUT ESTERNO — FACOLTATIVO ma RACCOMANDATO

**Casi reali del dominio forniti dal ricercatore**

I casi costruiti dall'agente in autonomia sono strutturalmente plausibili ma generici. I casi forniti dal ricercatore che conosce il dominio sono più forti:

- riflettono varianti limite osservate nella pratica
- costruiscono ambiguità reali, non solo logiche
- forzano il dispositivo su casi che la teoria non anticipa

**Modalità di fornitura**: il ricercatore può fornire i casi come testo narrativo o come JSON parziale; l'agente li integra nei 5 slot mantenendo la copertura tipologica.

**Se nessun caso è fornito**: l'agente costruisce i 5 casi in autonomia. Il test resta valido ma può non rilevare fragilità specifiche del dominio.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Trasformare il dispositivo in checklist per valutare i casi | Lo stress test legge *con* il dispositivo, non applica scale |
| Introdurre giudizi normativi (corretto / scorretto, adeguato / inadeguato) | Il dispositivo descrive struttura, non giudica |
| Introdurre diagnosi o categorie diagnostiche | Fuori ambito |
| Semplificare i casi per far "funzionare" il dispositivo | I casi devono essere plausibili e sfidanti |
| Omettere i punti di rottura quando il dispositivo è in difficoltà | I limiti sono il risultato principale dello stress test |
| Correggere il dispositivo se il breaking point è solo zona di fragilità da segnalare | La correzione è giustificata solo da rottura strutturale |
| Costruire i 5 casi tutti "facili" o tutti "estremi" | Devono coprire una gamma di pressione strutturale |

---

## D. Operazioni da svolgere

### D.1 Generazione dei 5 casi (cinque tipologie obbligatorie)

Produci **esattamente 5 casi**, uno per ciascuna tipologia:

| `case_type` | Descrizione |
|---|---|
| `assenza_configurazione` | Nessun livello della configurazione si attiva. Il dispositivo si applicherebbe a un campo che non c'è |
| `configurazione_parziale` | Alcuni livelli sono presenti, altri assenti. Il dispositivo lavora su una struttura zoppa |
| `configurazione_distorta_chiudente` | I livelli si attivano ma in forma alterata: la regolazione chiude invece di aprire, la mediazione diventa direttiva |
| `configurazione_oscillante` | La configurazione si costituisce in modo intermittente: presente in alcuni scambi, assente in altri |
| `configurazione_apparente_indistinguibile` | Falso positivo strutturale: il campo ha *forma piena* in superficie ma il passaggio è riproduzione di uno script. Caso quasi indistinguibile da un caso "reale" |

Ogni caso deve essere:

- **concreto**: descrive una situazione specifica e osservabile, non una categoria astratta
- **plausibile**: potrebbe accadere realmente nel dominio scelto
- **sfidante**: costruito per mettere il dispositivo in difficoltà

⚠️ **Il caso `configurazione_apparente_indistinguibile` è il più importante**: è dove il dispositivo rischia il fallimento silenzioso (lettura apparentemente coerente su una configurazione che non lo è). Costruirlo come caso *quasi indistinguibile* da uno reale, in cui il dispositivo deve dimostrare di discriminare struttura da forma.

---

### D.2 Applicazione del dispositivo a ogni caso

Per ogni caso, in `device_application`:

**a) `observed_configuration`** — cosa accade nel campo: stato del nodo dominante, stato dei nodi co-fragili, polarità del campo. Descrizione strutturale, non valutativa.

**b) `device_behavior`** — come si comporta il dispositivo:
- riesce a leggere il caso? cosa rende leggibile e cosa rimane opaco?
- le micro-azioni del dispositivo sono praticabili in questo caso?
- l'indicatore di risonanza è verificabile?
- `ambiguity_level`: `basso` | `medio` | `alto`

**c) `breaking_point`** (presente / assente):
- se assente: dichiarare comunque la zona di maggiore fragilità del dispositivo su questo caso
- se presente: indicare *dove* si localizza (nodo, micro-azione, indicatore di risonanza, condizione di applicabilità) e *perché* si rompe (limite strutturale, ambiguità concettuale, micro-azione non praticabile in quel caso)

**d) `non_applicability_triggered`** — questo caso attiva una delle condizioni di `non_applicability` definite dal dispositivo? (sì → riportare quale; no → null)

**e) `mislettura_risk`** — due livelli:
- *senza dispositivo*: l'errore tipico del dominio
- *con dispositivo usato male*: l'errore facilitato da un uso non rigoroso

---

### D.3 Verdetto sullo stress test

In `stress_test_verdict`:

- `cases_passed` — numero di casi (su 5) che il dispositivo ha letto con `ambiguity_level` ≤ medio e senza breaking point
- `breaking_points_count` — numero di breaking point strutturali rilevati
- `apparente_indistinguibile_outcome` — esito specifico sul caso più critico:
  - `discriminato` — il dispositivo distingue struttura reale da apparente
  - `non_discriminato` — il dispositivo non distingue: il dispositivo ha un punto cieco strutturale
  - `discriminazione_dipendente_dall_osservatore` — la distinzione c'è ma richiede capacità interpretativa non garantita
- `verdict`: `robusto` | `accettabile` | `fragile` | `non_valido`

Criteri:

- `robusto`: ≥ 4 casi senza breaking point, `apparente_indistinguibile_outcome = discriminato`
- `accettabile`: 3 casi senza breaking point + `apparente_indistinguibile_outcome ≠ non_discriminato`
- `fragile`: 1–2 breaking point strutturali oppure `apparente_indistinguibile_outcome = discriminazione_dipendente_dall_osservatore`
- `non_valido`: ≥ 3 breaking point strutturali oppure `apparente_indistinguibile_outcome = non_discriminato`

---

### D.4 Correzione del dispositivo (condizionale)

La correzione si esegue **solo se** il `verdict` è `fragile` o `non_valido`, **e solo** sui breaking point classificati come *strutturali*.

In `device_correction` (omettere se non necessaria):

- `triggered_by_breaking_points` — quali breaking point hanno motivato la correzione
- `corrected_micro_actions` — eventuali micro-azioni riformulate (mantenendo cardinalità 3–5)
- `corrected_non_applicability` — eventuali nuove condizioni di non-applicabilità identificate
- `corrected_universal_form` — se la correzione modifica la classificazione U1–U6 (raro)
- `corrected_resonance_indicator` — se l'indicatore di risonanza è stato precisato

Vincoli sulla correzione:

- **NON** introdurre nuovi nodi né cambiare il nodo dominante
- **NON** cambiare la funzione (richiederebbe ripartire da F3 step 1)
- **NON** ampliare il dispositivo: la correzione *precisa* o *restringe*, non aggiunge complessità
- **NON** trasformare le micro-azioni in comportamenti normativi

Se i breaking point richiedono cambiamenti che violano questi vincoli (es. cambio di funzione), il `verdict` finale è `non_valido` e si raccomanda di tornare a F3 step 1. Indicarlo esplicitamente in `correction_blocked_reason`.

---

## E. Output

### Schema

`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-3-stress-test\stress-test-schema.json`

### Wrapper

```json
{
  "step": "f3_step_3",
  "tema_id": "...",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio

- **Nome file**: `stress-test-{dominio}-v1.json` (es. `stress-test-clinico-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `case_type`
`"assenza_configurazione"` | `"configurazione_parziale"` | `"configurazione_distorta_chiudente"` | `"configurazione_oscillante"` | `"configurazione_apparente_indistinguibile"`

### `device_behavior.ambiguity_level`
`"basso"` | `"medio"` | `"alto"`

### `breaking_point.present`
booleano

### `stress_test_verdict.apparente_indistinguibile_outcome`
`"discriminato"` | `"non_discriminato"` | `"discriminazione_dipendente_dall_osservatore"`

### `stress_test_verdict.verdict`
`"robusto"` | `"accettabile"` | `"fragile"` | `"non_valido"`

---

## G. Note sulla sostituzione degli step precedenti

Questo step accorpa tre stress test della pipeline precedente (vecchi step 2, 4, 10) in un'unica operazione:

- la copertura dei 5 tipi tipologici resta integralmente (vecchio step 2)
- il caso quasi indistinguibile è inglobato come una delle 5 tipologie (vecchio step 4)
- la correzione strutturale, quando giustificata da breaking point, avviene inline (vecchio step 3) — ma solo se necessaria, e solo nei limiti dichiarati in §D.4

---

## H. Posizione nella pipeline

1. **Dopo**: F3 step 2 verificato
2. **Prima**: F3 step 4 (verifica di coerenza F3)
3. **Funzione metodologica**: stress test integrato del dispositivo + eventuale correzione mirata. Lo step finisce con un `verdict` che orienta la decisione del ricercatore: procedere alla verifica di coerenza, ripetere il dispositivo, o tornare alla scelta del nodo/funzione.
