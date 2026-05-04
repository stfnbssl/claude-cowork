# STEP 5 — Generazione della famiglia di output

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali. Questo è lo **STEP 5** di una pipeline.

Il tuo compito è trasformare la micro-matrice strutturale validata (STEP 4) in una **famiglia di possibili direzioni di utilizzo del modello**: non ancora strumenti operativi, ma tipi di uso strutturato che la configurazione rende possibili.

> **Principio guida**
>
> STEP 5 non dice cosa fare.
> STEP 5 dice cosa diventa possibile vedere e pensare.
> Non strumenti. Non teoria. Possibilità strutturate di uso.

---

## B. Input

### STEP 1 — Definizione del tema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-discovery-v2.json`

### STEP 3 — Configurazione strutturale verificata
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-verification-v2.json`

### STEP 4 — Micro-matrice
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-matrix-v2.json`

### JSON precompilati dei sei assi
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\`

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Produrre checklist, protocolli, linee guida | Non è ancora Fase 3 |
| Prescrivere comportamenti ("fare X", "evitare Y") | La famiglia di output descrive, non prescrive |
| Banalizzare ("fa bene a…", "è importante per…") | Perdita della struttura |
| Introdurre domini non presenti in `translation_potential` di STEP 4 | I domini devono emergere dalla configurazione già validata |
| Produrre output non collegati esplicitamente alla micro-matrice | Ogni output deriva da assi, nodi e tensioni specifici |
| Trasformare `output_type` in istruzione o consiglio | Il tipo di output è una funzione, non un'azione |
| Riformulare o derivare i nodi in `structural_basis.nodes` | I nodi devono corrispondere esattamente ai `node_id` confermati in STEP 3: la tracciabilità del sistema dipende da questo vincolo |

---

## D. Operazioni da svolgere

### D.1 Ricognizione dei domini di traducibilità

Parti da `translation_potential` in STEP 4: i domini sono già identificati e motivati dalla configurazione strutturale. Non reinventarli.

Per ogni dominio confermato in STEP 4:
- recupera la motivazione strutturale già prodotta (`reason`)
- verificane la tenuta rispetto all'intera micro-matrice (assi, nodi, tensioni)
- determina se è possibile aggiungere un dominio inter-dominio (che combina due o più domini già presenti) — solo se la configurazione lo giustifica

**Target: 3–5 famiglie di output**, corrispondenti ai domini di `translation_potential` con eventuale aggiunta inter-dominio.

---

### D.2 Definizione del tipo di output per ogni dominio

Per ogni dominio, definisci il **tipo di uso possibile del modello**: non uno strumento, ma una funzione strutturata.

**Forme ammesse:**
- `"lettura configurazionale di…"` — uso del modello per leggere una situazione
- `"analisi della struttura di…"` — uso del modello per analizzare una configurazione
- `"orientamento alla qualità di…"` — uso del modello per valutare la qualità strutturale
- `"interrogazione strutturale su…"` — uso del modello per aprire domande strutturali

**Forme vietate:**
- `"come fare…"` / `"strategie per…"` / `"consigli per…"`

---

### D.3 Collegamento esplicito alla struttura

Per ogni output, specifica quali elementi della micro-matrice attiva:

- **assi** — sottoinsieme degli assi confermati in STEP 3
- **nodi** — `node_id` esatti dei nodi confermati in `theme-verification-v2.json` per il tema in questione; nessuna riformulazione o derivazione
- **tensioni** — etichette esatte delle tensioni strutturali di STEP 4 che questo output rende visibili

> **Regola sui nodi (critica per la tracciabilità)**
>
> `structural_basis.nodes` deve contenere solo i `node_id` presenti in `confirmed_nodes` di STEP 3.
> Non sono ammesse riformulazioni leggibili (es. "co-presenza" al posto di "co-regolazione-esperienziale").
>
> Se un nodo ha bisogno di contestualizzazione per chiarire come entra nell'output, usare il campo opzionale `node_interpretation` — una breve frase che spiega la lettura specifica del nodo in questo dominio, senza sostituirne l'identificatore.

> **Principio: le tensioni sono il cuore della traducibilità**
>
> Le tensioni non sono un elemento accessorio o decorativo del collegamento strutturale.
> Sono il motore interpretativo dell'output: rendono visibile perché la configurazione è rilevante per quel dominio, e perché non è riducibile a una soluzione semplice.
> Un output che non attiva almeno una tensione è strutturalmente debole.

Senza questo collegamento l'output non può essere verificato rispetto alla struttura e perde il suo valore epistemologico.

---

### D.4 Identificazione del valore aggiunto

Per ogni output: cosa permette di vedere o pensare che prima non era accessibile?

Il valore aggiunto non è "questo strumento è utile" — è il contributo specifico della configurazione strutturale rispetto a letture non strutturali del tema. Cosa vede chi usa questo output che non vede chi non lo usa?

> **Principio: ogni output produce uno spostamento di sguardo, non un miglioramento di pratica**
>
> Il valore aggiunto non è rendere una pratica più efficace, ma rendere visibile qualcosa che prima non era accessibile come livello di interrogazione. Se il `value_added` descrive un miglioramento operativo, l'output ha già scivolato verso il prescrittivo.

---

### D.5 Identificazione del rischio di riduzione

Per ogni output: come potrebbe essere banalizzato o distorto nell'uso pratico?

Identifica la forma più probabile di scivolamento verso il prescrittivo o il banale. Questo non è una nota di cautela generica: è un elemento strutturale dell'output, utile per orientare la costruzione degli strumenti in Fase 3.

---

### D.6 Note meta sulla famiglia

Dopo aver prodotto tutte le famiglie di output per un tema, produci le `meta_notes`:

- **coherence_with_structure** — valutazione della coerenza complessiva della famiglia con la micro-matrice: quanto le famiglie restano fedeli alla configurazione senza scivolare nel prescrittivo
- **limitations** — quali domini o aspetti della micro-matrice non sono stati tradotti in output e perché
- **next_step_orientation** — quali output families sono più mature per lo sviluppo di strumenti operativi in Fase 3, quali richiedono ulteriore elaborazione

---

## E. Output

### Schema
Lo schema completo è in:
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f2-step-5-output-family\output-family-schema.json`

### Wrapper per input multi-tema
```json
{
  "step": "step_5",
  "results": [ { ... }, { ... }, ... ]
}
```

### Salvataggio
- **Nome file**: `output-family-v2.json`
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `output_type`
Stringa libera, ma con forma vincolata. Deve descrivere una **funzione** (cosa il modello permette di fare), non un'**azione** (cosa un professionista deve fare). Esempi validi:
- `"lettura configurazionale della qualità della co-presenza in contesti di osservazione clinica"`
- `"analisi della struttura del campo triadico in pratiche di lettura condivisa"`
- `"orientamento alla qualità del campo co-regolativo nei setting educativi 0-3"`

### `structural_basis.nodes`
Devono corrispondere esattamente ai `node_id` presenti in `confirmed_nodes` di `theme-verification-v2.json` per il tema in questione. Non sono ammesse riformulazioni leggibili né derivazioni. Se necessario, usare il campo opzionale `node_interpretation` per contestualizzare come il nodo entra nell'output specifico.

Esempio corretto:
```json
"nodes": ["co-regolazione-esperienziale"],
"node_interpretation": "nel dominio clinico: co-presenza incarnata nella situazione di osservazione"
```

Esempio errato:
```json
"nodes": ["co-presenza"]   ← non è un node_id confermato in STEP 3
```

### `structural_basis.tensions`
I valori devono corrispondere esattamente alle etichette `tension` presenti in `theme-matrix-v2.json` per il tema in questione (es. `"presenza fisica vs. presenza strutturale"`).

### `structural_basis.axes`
Sottoinsieme degli assi confermati per il tema in STEP 3. Non introdurre assi non confermati.

---

## G. Differenza chiave con STEP 4

| STEP 4 | STEP 5 |
|---|---|
| descrive la struttura | identifica possibilità di uso |
| configura | orienta |
| rende leggibile | rende utilizzabile |
| genera domande strutturali | genera direzioni di applicazione |

---

## H. Posizione nella pipeline

1. **Dopo**: STEP 4 approvato (`theme-matrix-v2.json`)
2. **Prima**: costruzione degli strumenti operativi (Fase 3)
3. **Iterativo**: può essere revisionato prima di passare a Fase 3
