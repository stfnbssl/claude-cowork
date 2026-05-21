# STEP 3 — Verifica strutturale e selezione

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali. Questo è lo **STEP 3** di una pipeline.

Il tuo compito è trasformare un'**ipotesi plausibile (STEP 2)** in una **configurazione strutturalmente fondata**: ridurre, raffinare, selezionare.

> **Principio guida**
>
> STEP 2 apre possibilità. STEP 3 crea vincoli.
> Se tutto resta possibile → STEP 3 è fallito.
> Se tutto è ridotto a uno → STEP 3 è eccessivo.

---

## B. Input

### STEP 1 — Definizione dei temi
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-discovery-v2.json`

### STEP 2 — Ipotesi strutturale (assi, nodi, concetti-ponte)
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-relevance-v2.json`

### JSON precompilati dei sei assi
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\assi-strutturali\precompiled\`

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Aggiungere nuovi elementi non presenti in STEP 2 | Il lavoro è ridurre, non espandere |
| Costruire la micro-matrice | Riservato a STEP 4 |
| Produrre output applicativi o operativi | Nessuna applicazione |
| Mantenere tutto per prudenza | La selezione è il compito |
| Usare linguaggio descrittivo al posto di strutturale | |

---

## D. Operazioni da svolgere

### D.1 Verifica degli assi

Per ogni asse candidato (da STEP 2), determina:

- **confermato** — il tema non è pensabile senza di esso; ha più di un nodo rilevante; ha funzione strutturale non accessoria
- **secondario** — contribuisce al tema ma non è indispensabile; va in `rejected_axes` con `rejection_reason: "secondario"` e una nota
- **non necessario** — non regge alla verifica; va in `rejected_axes` con `rejection_reason` esplicita

**Vincolo**: mantieni massimo **2–3 assi confermati**.

---

### D.2 Verifica dei nodi

Per ogni nodo (da STEP 2), applica i tre test:

```
TEST 1 — Necessità:       il tema può essere pensato senza questo nodo?
TEST 2 — Specificità:     questo nodo distingue questo tema da altri temi?
TEST 3 — Non ridondanza:  è già coperto da un altro nodo?
```

Classifica ogni nodo come:

- **confermato** — supera tutti e tre i test
- **secondario** — utile ma non strutturalmente necessario; va in `secondary_nodes` con motivazione
- **eliminato** — va in `rejected_nodes` con `rejection_reason`

**Vincolo**: mantieni **4–7 nodi confermati**.

> **Definizione di nodo secondario**: un nodo che contribuisce a descrivere il tema ma non è necessario per la configurazione essenziale. Se rimosso, il tema resta strutturalmente leggibile, anche se meno ricco. Non accumulare nodi secondari per prudenza: se superano 2, rivaluta la selezione.

---

### D.3 Verifica dei concetti-ponte

Per ogni concetto-ponte (da STEP 2), applica i tre test:

```
TEST 1 — Connessione reale:  collega davvero più assi confermati?
TEST 2 — Valore aggiunto:    aggiunge qualcosa rispetto ai soli nodi?
TEST 3 — Non ridondanza:     non è solo una riformulazione di un altro concetto-ponte?
```

- Mantieni massimo **2–3 concetti-ponte confermati**
- I concetti-ponte eliminati vanno in `rejected_bridge_concepts` con `rejection_reason`

---

### D.4 Verifica della coerenza globale

Controlla:

- Gli assi confermati sono coerenti con i nodi confermati?
- I nodi confermati sono coerenti tra loro?
- I concetti-ponte collegano effettivamente gli assi confermati?

Se no → correggi la selezione prima di procedere.

---

### D.5 Identificazione della struttura

Determina il tipo di struttura con maggiore precisione rispetto a STEP 2:

- **`asse_dominante`** — un asse è chiaramente prevalente
- **`multi_assiale`** — più assi con peso comparabile e funzioni distinte
- **`soglia_tra_assi`** — il tema si colloca al confine tra due assi specifici

In `description` specifica la **funzione** di ciascun asse confermato, non solo il nome (es. "Asse 1 → strutturazione del campo esperienziale; Asse 6 → mediazione simbolica e culturale").

---

### D.6 Formulazione sintetica

Produci in `synthetic_formulation` una frase compatta che descriva la struttura del tema (es. "configurazione triadica di mediazione simbolica e regolazione incarnata"). Deve essere leggibile senza i JSON degli assi.

---

## E. Output

### Schema
Lo schema completo è in:
`C:/my/claude/claude-cowork\Sviluppo Bambino\input\produzioni\f2-step-3-verifica-strutturale\theme-verification-schema.json`

### Wrapper output
```json
{
  "step": "step_3",
  "results": [ { ... } ]
}
```

> **F2 è single-tema**: `results` contiene sempre esattamente un elemento.

### Salvataggio
- **Nome file**: `theme-verification-v2.json`
- **Cartella**: `C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `role` (in `confirmed_axes`)
Descrivere in prosa la funzione strutturale dell'asse nel tema specifico (es. "asse esperienziale e regolativo", "asse della mediazione simbolica e culturale"). Non usare valori predefiniti: la funzione va argomentata caso per caso.

### `structural_configuration.type`
`"asse_dominante"` | `"multi_assiale"` | `"soglia_tra_assi"`

---

## G. Differenza chiave con STEP 2

| STEP 2 | STEP 3 |
|---|---|
| esplora | seleziona |
| include | esclude |
| ipotizza | vincola |
| apre | chiude |

---

## H. Posizione nella pipeline

1. **Dopo**: STEP 2 approvato (`theme-relevance-v2.json`)
2. **Prima**: costruzione della micro-matrice (STEP 4)
3. **Iterativo**: può essere revisionato in dialogo con STEP 2 se la selezione svuota il tema
