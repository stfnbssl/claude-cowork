# F3 STEP 2 — Costruzione del micro-dispositivo di campo

---

## A. Ruolo e contesto

Sei un agente che opera nella **Fase 3 (F3)** della pipeline HCAIRE. Questo è il secondo step della Fase 3.

Il tuo compito è costruire un **micro-dispositivo di campo** per il tema e il dominio scelti, partendo dal nodo dominante e dalla funzione decisi in F3 step 1.

Un micro-dispositivo di campo, secondo la metodologia, è una **modifica locale delle condizioni di sviluppo**: breve, integrabile nel contesto reale, non specialistico, reversibile, osservabile nei suoi effetti. Non è un intervento terapeutico, non è una tecnica educativa, non è un protocollo clinico.

> **Principio guida**
>
> Il dispositivo *non corregge il bambino*: modifica il campo relazionale di esperienza.
> Lo strumento non è una soluzione: è un *regolatore di campo*.
> Tempo reale: 5–10 minuti.

---

## B. Input

### INPUT PRIMARIO — F3 step 1 (Nodo dominante + funzione)

`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\nodo-funzione-{dominio}-v1.json`

Contiene il nodo dominante, la funzione, il campo bersaglio e l'auto-verifica di coerenza.

### INPUT SECONDARIO — Output-Tipo Vuoto (F2 step 6)

`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\output-tipo-vuoto-v1.json`

Per accedere alla CE complessiva e alla classificazione U1–U6 già attivata.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Produrre protocolli, linee guida, checklist, scoring | Il dispositivo non è uno strumento di valutazione né di applicazione standardizzata |
| Prescrivere comportamenti del bambino o del caregiver | Lo strumento agisce sul *campo*, non sulla persona |
| Più di 5 micro-azioni | Un micro-dispositivo è breve. Oltre 5 azioni si entra nel protocollo |
| Micro-azioni non osservabili (azioni mentali, intenzioni) | L'osservabilità è criterio di esistenza |
| Micro-azioni non reversibili | Un dispositivo F3 deve poter essere interrotto senza danno |
| Etichettare il bambino, diagnosticare, valutare ("adeguato/inadeguato") | Fuori metodo (sez. 2.7) |
| Introdurre nodi o assi non presenti nella CE | Il dispositivo lavora sulla configurazione confermata |
| Confondere il *campo bersaglio* con un comportamento del bambino | Il dispositivo agisce sulle condizioni del campo, non sui comportamenti |

---

## D. Operazioni da svolgere

Costruisci il dispositivo nel formato del **template a sette campi** della metodologia (sez. 2.5), più la classificazione U1–U6 e le condizioni di non-applicabilità.

---

### D.1 Configurazione di origine (CE)

In `ce_origin` riporta una **sintesi grammaticale** della CE in entrata: nodi attivi, loro stato, polarità del campo. Una frase, due al massimo.

Esempio di forma (non contenuto): *"Accesso condiviso presente / regolazione fragile / esplorazione ridotta / A±"*.

---

### D.2 Riferimento al nodo dominante e alla funzione

Riporta in `dominant_node_ref` e `function_ref` i valori prodotti in F3 step 1. Non riformulare.

---

### D.3 Campo bersaglio specifico

Riprendi `target_field` da F3 step 1.

---

### D.4 Micro-azioni (3–5)

In `micro_actions` produci **da 3 a 5** azioni. Ogni micro-azione deve essere:

- **osservabile**: descrivibile come azione fenomenicamente leggibile
- **reversibile**: interrompibile senza creare dipendenza o vincolo
- **integrabile**: praticabile nel contesto reale del dominio (ambulatorio, nido, colloquio, ecc.) senza richiedere setting speciali
- **non specialistica**: eseguibile da un professionista del dominio senza training tecnico aggiuntivo
- **agente sul campo**, non sul bambino: l'azione è del professionista o del caregiver, *modifica le condizioni* del campo, non corregge il bambino

Per ogni micro-azione:

- `id`
- `description` — formulata come azione del professionista/caregiver
- `observable_effect` — cosa diventa visibile quando l'azione è in atto
- `reversibility_note` — come si interrompe l'azione senza danno

> **Principio**: una micro-azione non è una raccomandazione né una tecnica. È una *forma del campo*.

---

### D.5 Tempo reale

In `real_time` indica la durata operativa attesa del dispositivo. Default: `"5-10 minuti"`. Se diversa, motivare in `time_motivation` perché il dominio richiede una durata diversa.

---

### D.6 Indicatore di risonanza

In `resonance_indicator` indica **cosa dovrebbe cambiare nel campo** quando il dispositivo è in atto. Non è un esito misurabile, è una *trasformazione qualitativa del campo*. Una frase.

> Esempio di forma corretta: *"Il bambino entra nello scambio con propri tempi e l'adulto rallenta verso quei tempi."*
> Esempio di forma sbagliata: *"Il bambino aumenta del 30% le iniziative comunicative."* (è metrica, non risonanza).

---

### D.7 Classificazione U1–U6 (tipologia universale)

In `universal_form` indica la classificazione del dispositivo secondo la tipologia universale del metodo (sez. 4):

| ID | Forma | Funzione |
|---|---|---|
| U1 | Regolazione | stabilizzare l'esperienza quando tende al collasso |
| U2 | Sintonizzazione | rendere l'esperienza condivisibile |
| U3 | Apertura | ampliare il campo delle possibilità |
| U4 | Mediazione simbolica | trasformare esperienza in significato condiviso |
| U5 | Limite generativo | integrare il reale senza disorganizzare |
| U6 | Riattivazione del desiderio | ripristinare direzione evolutiva |

Un dispositivo può essere classificato come **combinazione** (es. `U2+U4` per dialogic book sharing). Indica:

- `forms` — array di codici U1–U6 (1 o più)
- `combination_motivation` — se più di una forma, motivazione strutturale della combinazione

---

### D.8 Condizioni di non-applicabilità (auto-limitazione)

In `non_applicability` indica le condizioni in cui il dispositivo **non deve essere applicato** o produrre l'esito `non_classificabile`. La metodologia (sez. 5.6) richiede questa proprietà come **costitutiva** del dispositivo: deve "smettere di funzionare quando i dati non ci sono".

Per ogni condizione:

- `trigger` — la condizione che invalida l'applicabilità (assenza di dati osservabili minimi, presenza di rischio prescrittivo, ecc.)
- `required_outcome` — uno tra `non_classificabile` | `ambiguo` | `sospendere`
- `rationale` — perché in questa condizione il dispositivo *non deve* funzionare

---

### D.9 Sintesi narrativa (frase finale)

In `synthesis` riporta una **frase sintetica** che dichiari, in linguaggio condivisibile tra operatori del dominio, cosa il dispositivo *fa al campo*. Una frase, max 30 parole. Non descrive il bambino. Non descrive azioni operative. Descrive la trasformazione di campo.

---

## E. Output

### Schema

`C:/my/claude/claude-cowork\Sviluppo Bambino\input\produzioni\f3-step-2-micro-dispositivo\micro-dispositivo-schema.json`

### Wrapper

```json
{
  "step": "f3_step_2",
  "tema_id": "...",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio

- **Nome file**: `micro-dispositivo-{dominio}-v1.json` (es. `micro-dispositivo-clinico-v1.json`)
- **Cartella**: `C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `universal_form.forms[]`
`"U1"` | `"U2"` | `"U3"` | `"U4"` | `"U5"` | `"U6"`

### `non_applicability[].required_outcome`
`"non_classificabile"` | `"ambiguo"` | `"sospendere"`

### `micro_actions` — cardinalità
3 ≤ |`micro_actions`| ≤ 5

---

## G. Differenza chiave con F3 step 1

| F3 step 1 | F3 step 2 |
|---|---|
| Sceglie nodo dominante e funzione | Costruisce il dispositivo |
| Atto decisionale | Atto costruttivo |
| Output: piccolo JSON di orientamento | Output: dispositivo completo applicabile |

---

## H. Posizione nella pipeline

1. **Dopo**: F3 step 1 verificato
2. **Prima**: F3 step 3 (stress test e correzione)
3. **Funzione metodologica**: produrre il *micro-dispositivo di campo* nel template della metodologia (sez. 2.5), classificato secondo le forme universali (sez. 4) e dotato di auto-limitazione (sez. 5.6).
