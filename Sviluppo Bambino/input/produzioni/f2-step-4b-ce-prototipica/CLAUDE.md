# F2 STEP 4b — Configurazione Evolutiva Prototipica (CE Prototipica)

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali e sette Nodi Trasversali canonici (N1–N7). Questo è lo **STEP 4b** della pipeline F2 — si esegue subito dopo lo STEP 4 (Micro-matrice) e prima di STEP 5 (Famiglia di output).

Il tuo compito è tradurre la micro-matrice strutturale del tema nella sua **Configurazione Evolutiva Prototipica (CE Prototipica)**: la rappresentazione formale del tema nella Grammatica delle Configurazioni del modello HCAIRE.

La CE Prototipica non descrive un caso reale. Descrive la **forma strutturale tipica** del tema — la configurazione che lo rende riconoscibile come fenomeno distinto all'interno del modello.

> **Principio guida**
>
> La Grammatica delle Configurazioni è il linguaggio formale del modello HCAIRE.
> La CE Prototipica è la firma strutturale del tema: il modo in cui il tema si scrive in questo linguaggio.
> Non è la descrizione di un bambino, non è una diagnosi, non è una media statistica.
> È la struttura concettuale che rende il tema interrogabile in ogni contesto.

---

## La Grammatica delle Configurazioni (CE)

Una Configurazione Evolutiva è la forma temporaneamente stabile assunta dalla dinamica tra Nodi Trasversali in un determinato campo relazionale.

### Le cinque dimensioni grammaticali

**S — Stato dei nodi** (solo nodi canonici N1–N7 attivati nel tema):

| Codice | Significato |
|---|---|
| ↑ | espansivo |
| ~ | stabile |
| ↓ | ristretto |
| ! | disorganizzato |
| ? | non leggibile / indeterminato |

**R — Relazioni dominanti tra nodi:**

| Codice | Significato |
|---|---|
| CPL | sostegno (coupling): un nodo rende possibile l'attivazione di un altro |
| VIN | vincolo: un nodo limita fisiologicamente un altro |
| MED | mediazione: un nodo coordina due domini diversi |
| CMP | compensazione: un nodo sostiene parzialmente un deficit altrove |

**D — Direzione dinamica:**
- `↗` espansione
- `→` stabilizzazione
- `↘` restringimento

**T — Stabilità temporale:**
- `T1` situazionale (episodico)
- `T2` ricorrente (ma non stabilizzato)
- `T3` stabilizzata (strutturale)

**A — Abitabilità esperienziale:**

| Codice | Significato |
|---|---|
| A+ | esperienza abitabile |
| A± | fragile ma recuperabile |
| A− | rischio di collasso |

### Regola fondamentale

> La configurazione descrive il **campo**, non attribuisce proprietà al bambino.

---

## B. Input

### STEP 4 — Micro-matrice
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-matrix-v2.json`

### STEP 2a — Verifica Nodi Trasversali (se disponibile)
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\node-verification-v1.json`

Usa le mappature canoniche (N1–N7 attivati) per costruire la dimensione S della CE. Se STEP 2a non è disponibile, ricava i Nodi canonici attivati direttamente dagli assi e dalla `core_configuration` di STEP 4.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Usare nodi tematici (non canonici) nella dimensione S | S usa solo N1–N7; i nodi derivati non entrano nella grammatica CE |
| Assegnare valori S a Nodi canonici non attivati nel tema | Solo i Nodi presenti nel tema ricevono stato |
| Usare punteggi o scale numeriche | La grammatica CE usa solo simboli qualitativi |
| Descrivere il bambino o attribuire caratteristiche | La CE descrive il campo, non il soggetto |
| Produrre più di una CE per tema | La CE Prototipica è una sola: rappresenta la forma tipica del tema |
| Forzare la direzione D verso espansione se non supportata dalla matrice | D deve derivare dalla tensione strutturale dominante in STEP 4 |
| Trattare A come scala di qualità | A+ non è "buono", A− non è "cattivo": sono zone di abitabilità strutturale |

---

## D. Operazioni da svolgere

### D.1 Costruzione della dimensione S

Per ogni Nodo canonico attivato nel tema (da STEP 2a o inferito da STEP 4):

Determina lo stato strutturale prototipico (`↑`, `~`, `↓`, `!`, `?`) ragionando sulla **funzione del Nodo nel tema specifico**:
- Il tema richiede che questo Nodo sia espansivo, stabile, o in tensione?
- La struttura del tema implica un Nodo in stato critico?
- L'indeterminatezza strutturale del tema rende un Nodo non leggibile?

**Regola**: lo stato `?` è ammesso solo se la micro-matrice esplicita una genuina indeterminatezza strutturale per quel nodo (non come scorciatoia per evitare la classificazione).

---

### D.2 Identificazione delle relazioni R

Determina le 1–3 relazioni dominanti tra Nodi canonici che caratterizzano il tema.

Per ogni relazione:
- indica la coppia di Nodi (es. `N2 → N3`)
- il tipo di relazione (`CPL` | `VIN` | `MED` | `CMP`)
- una frase di motivazione strutturale

Usa come guida le relazioni già emerse in `core_configuration` e `bridge_integration` di STEP 4: le relazioni R della CE devono essere coerenti con la logica strutturale della micro-matrice.

---

### D.3 Determinazione della direzione D

Determina la direzione dinamica prototipica del tema (`↗` | `→` | `↘`):

- Se le tensioni strutturali di STEP 4 indicano un tema che tende all'apertura e all'espansione → `↗`
- Se le tensioni indicano un tema in equilibrio critico, che richiede sostegno per restare stabile → `→`
- Se il tema è caratterizzato da riduzione o chiusura strutturale → `↘`

La direzione è del **campo nel momento del fenomeno**, non della traiettoria a lungo termine.

---

### D.4 Determinazione della stabilità temporale T

- `T1`: il fenomeno è episodico, circoscritto, non stabilizzato (es. un gesto puntuale)
- `T2`: il fenomeno è ricorrente ma non ancora strutturato (es. pattern emergente)
- `T3`: il fenomeno è parte di una struttura relazionale stabilizzata

Usa `translation_potential` di STEP 4 come indicatore: se il tema è leggibile in contesti multipli e longitudinali, T3 è plausibile.

---

### D.5 Determinazione dell'abitabilità A

- `A+`: la configurazione del tema è strutturalmente sostenibile senza intervento specifico
- `A±`: la configurazione è fragile; il tema si trova in una zona di transizione che richiede attenzione
- `A−`: la configurazione indica rischio di collasso; il campo non è strutturalmente abitabile senza sostegno

Usa `structural_tensions` di STEP 4: tensioni molto marcate suggeriscono `A±` o `A−`; configurazioni espansive integrate suggeriscono `A+`.

---

### D.6 Formulazione della CE in notazione formale e in traduzione naturale

**Notazione formale** (obbligatoria):

```
CE =
  S: N1[stato] N2[stato] ... (solo nodi attivati)
  R: Nx→Ny (TIPO), ...
  D: [freccia]
  T: T[1-3]
  A: A[+/±/−]
```

**Traduzione naturale** (obbligatoria, 2–4 frasi): descrizione della CE in linguaggio non tecnico, comprensibile a professionisti di domini diversi. Non deve usare i codici della grammatica; deve descrivere il campo relazionale che la CE rappresenta.

---

### D.7 Varianti strutturali della CE

Indica **2–3 varianti** della CE Prototipica: come il tema si manifesta in configurazioni strutturalmente diverse dalla prototipica.

Ogni variante ha:
- una modificazione minima della CE (quale dimensione cambia e come)
- il nome della variante (es. "CE chiudente", "CE in attesa", "CE disorganizzata")
- una frase di descrizione strutturale

Le varianti servono a F3 per costruire i casi del dispositivo di lettura (access points, stress test).

---

## E. Output

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f2-step-4b-ce-prototipica\ce-prototipica-schema.json`

### Wrapper
```json
{
  "step": "f2_step_4b",
  "results": [ { ... } ]
}
```

### Salvataggio
- **Nome file**: `ce-prototipica-v1.json`
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `node_state` (dimensione S)
`"↑"` | `"~"` | `"↓"` | `"!"` | `"?"`

### `relation_type` (dimensione R)
`"CPL"` | `"VIN"` | `"MED"` | `"CMP"`

### `direction` (dimensione D)
`"↗"` | `"→"` | `"↘"`

### `temporal_stability` (dimensione T)
`"T1"` | `"T2"` | `"T3"`

### `habitability` (dimensione A)
`"A+"` | `"A±"` | `"A-"`

---

## G. Posizione nella pipeline

1. **Dopo**: STEP 4 (`theme-matrix-v2.json`) e STEP 2a (`node-verification-v1.json`, se disponibile)
2. **Prima**: STEP 5 (Famiglia di output) — la CE Prototipica informa la costruzione delle famiglie di output
3. **Input critico per F3**: la CE Prototipica diventa il nucleo della Configurazione Evolutiva nell'output-tipo vuoto (STEP 6), che a sua volta alimenta F3 STEP 1
4. **Non iterativo**: se STEP 4 viene revisionato, rieseguire STEP 4b

---

## H. Perché questo step esiste

Senza la CE Prototipica, la pipeline produce una micro-matrice ricca ma non traducibile nella grammatica formale del modello. La Grammatica delle Configurazioni è il linguaggio che rende i dispositivi F3 comparabili, coerenti e non arbitrari. La CE Prototipica è il ponte obbligatorio tra la struttura descrittiva (assi, nodi, tensioni di STEP 4) e la struttura operativa (operatore di lettura, output-tipo vuoto, dispositivi di STEP 6 e F3).
