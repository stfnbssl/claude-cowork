# STEP 4 — Costruzione della micro-matrice del tema

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali. Questo è lo **STEP 4** di una pipeline.

Il tuo compito è trasformare la configurazione strutturale selezionata (STEP 3) in una **configurazione leggibile e interrogabile**: la micro-matrice.

La micro-matrice non dice cosa fare. Dice cosa sta succedendo strutturalmente.

> **Principio guida**
>
> STEP 4 è lo spazio tra teoria e applicazione.
> Non ancora strumenti. Non più teoria pura.
> Una struttura che genera domande, non risposte.

---

## B. Input

### STEP 1 — Definizione del tema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-discovery-v2.json`

### STEP 3 — Configurazione strutturale selezionata
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-verification-v2.json`

### JSON precompilati dei sei assi
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\`

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Creare checklist, protocolli, indicazioni pratiche | Non è ancora Fase 3 |
| Riscrivere gli assi o fare filosofia generale | Stare tra teoria e applicazione |
| Introdurre nuovi nodi, assi o concetti | Lavorare solo con ciò che è confermato in STEP 3 |
| Usare esempi concreti | Ancora presto |
| Usare linguaggio tecnico settoriale | Mantenere apertura interdisciplinare |
| Trasformare la matrice in linee guida | La matrice descrive, non prescrive |

---

## D. Operazioni da svolgere

### D.1 Configurazione centrale

Descrivi come i nodi confermati interagiscono tra loro — non in modo descrittivo ma strutturale:

- chi organizza cosa
- cosa dipende da cosa
- cosa trasforma cosa

Il risultato va in `core_configuration`: un `description` (la logica della configurazione) e uno `structure_logic` (la formula sintetica del funzionamento).

---

### D.2 Articolazione per assi

Per ciascun asse confermato (da STEP 3):

- qual è la sua funzione specifica nel tema (`function_in_theme`)
- come entra nella configurazione
- cosa aggiunge che gli altri assi confermati non fanno (`specific_contribution`)

---

### D.3 Integrazione dei concetti-ponte

Per ogni concetto-ponte confermato (da STEP 3), determina:

**a) Come connette gli assi** — descrivi la relazione che produce tra i due livelli

**b) Che tipo di funzione svolge** — classifica in uno di questi due tipi:

- `"connettivo"` — il concetto crea un passaggio tra assi senza modificare la struttura degli elementi che collega; gli assi restano riconoscibili come separati
- `"organizzativo"` — il concetto non solo collega ma struttura la configurazione intera: gli altri elementi si dispongono attorno ad esso e la sua rimozione cambierebbe la logica della micro-matrice

Indica anche quali nodi confermati sono coinvolti nel ponte (`linked_nodes`).

---

### D.4 Tensioni strutturali

**Target: 2–4 tensioni.**

Identifica le tensioni interne alla configurazione: coppie di forze strutturalmente opposte che coesistono nel tema senza risolversi in una sintesi.

Le tensioni non sono problemi da risolvere — sono ciò che rende la micro-matrice utile come strumento di lettura professionale.

Ogni tensione ha:
- un'etichetta sintetica (`tension`): due poli separati da "vs." (es. "regolazione vs. apertura")
- una descrizione strutturale (`description`): perché i due poli coesistono e non si annullano

---

### D.5 Domande strutturali

**Target: 5–8 domande.**

Produci domande che:
- derivano direttamente dalla struttura della micro-matrice
- sono leggibili da professionisti di ambiti diversi
- non sono prescrittive (non iniziano con "come fare", "quando applicare")
- aprono interrogazioni strutturali, non procedure

---

### D.6 Potenziale di traducibilità

Indica in quali ambiti professionali la configurazione è traducibile (es. clinico, educativo, della formazione, delle politiche). Per ognuno specifica perché la struttura del tema è pertinente a quell'ambito — non cosa fare, ma quale domanda la configurazione porta in quell'ambito.

**Target: 2–4 ambiti.**

---

### D.7 Sintesi della configurazione

Produci in `configuration_summary` una frase o un breve paragrafo (max 3 frasi) che descriva la micro-matrice nella sua interezza: la logica che connette configurazione centrale, assi, ponti e tensioni. Deve essere leggibile autonomamente, senza i JSON degli assi.

---

## E. Output

### Schema
Lo schema completo è in:
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f2-step-4-micro-matrice\theme-matrix-schema.json`

### Wrapper per input multi-tema
```json
{
  "step": "step_4",
  "results": [ { ... }, { ... }, ... ]
}
```

### Salvataggio
- **Nome file**: `theme-matrix-v2.json`
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `bridge_integration.type`
- `"connettivo"` — crea un passaggio tra assi senza ristrutturare la configurazione
- `"organizzativo"` — struttura la configurazione intera; la sua rimozione cambierebbe la logica della micro-matrice

---

## G. Differenza chiave con STEP 3

| STEP 3 | STEP 4 |
|---|---|
| seleziona | organizza |
| elimina | articola |
| decide | rende leggibile |
| vincola | genera domande |

---

## H. Posizione nella pipeline

1. **Dopo**: STEP 3 approvato (`theme-verification-v2.json`)
2. **Prima**: costruzione degli strumenti operativi (Fase 3)
3. **Iterativo**: può essere revisionato prima di passare a Fase 3
