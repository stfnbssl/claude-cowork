# STEP 5F — Saggio integrato

## Obiettivo
Produrre un **saggio critico lungo**, destinato a una pubblicazione specialistica, che fonde l'articolo finale (Step 5D) e il resoconto del processo (Step 5E) in un testo organico e nuovo. Non è una somma né una giustapposizione: è una riscrittura che usa entrambi i testi come materiale, organizzandosi attorno ai nuclei tematici più forti dell'analisi.

Il risultato appartiene al genere del **saggio critico riflessivo**: un testo in cui l'argomentazione interpretativa e la consapevolezza metodologica si tengono insieme nello stesso movimento, rivolto a un lettore che ha familiarità con il discorso critico e con le questioni di metodo.

---

## Input atteso

- Il file Markdown dello **Step 5D** (`articolo-finale.md`)
- Il file Markdown dello **Step 5E** (`resoconto-processo.md`)
- I documenti JSON degli **Step 1–4** (per eventuali verifiche puntuali)

---

## Stile editoriale

Prima di scrivere, leggi il file:
```
C:\my\claude\claude-cowork\HCAIRE Cultura\pipeline-1\stile-editoriale.md
```
Le norme lì contenute si applicano integralmente. In particolare: nessun riferimento agli step numerati, nessuna formula che presenti il metodo come condizione necessaria dei risultati, citazione di HCAIRE con nome proprio quando il progetto è nominato.

---

## Istruzioni operative per Cowork

### 1. Leggi i due testi sorgente

Leggi per intero `articolo-finale.md` e `resoconto-processo.md`. Prima di scrivere qualsiasi cosa, identifica:
- Le affermazioni interpretative più forti dell'articolo
- I momenti di processo più significativi del resoconto
- I punti in cui le due dimensioni si corrispondono: dove un'affermazione critica e la storia di come è nata sono inscindibili

### 2. Identifica i nuclei tematici (3–5)

I nuclei tematici sono i punti in cui l'interpretazione e il processo si toccano con maggiore intensità — dove capire *cosa* si è trovato richiede capire *come* lo si è cercato, e viceversa. Non sono sezioni dell'articolo originale: sono le articolazioni interne dell'analisi attorno a cui il saggio si organizza.

Per ciascun nucleo, verifica che abbia:
- una dimensione interpretativa: cosa dice sull'opera
- una dimensione di processo: come è emerso, quale resistenza ha incontrato, quale scoperta ha richiesto

### 3. Scrivi una struttura nuova

Il saggio non segue né la struttura dell'articolo né quella del resoconto. Costruisce una struttura propria, organizzata attorno ai nuclei identificati. La sequenza dei nuclei deve avere una logica: può essere quella della complessità crescente, dell'ordine in cui le scoperte si sono accumulate, o di un'argomentazione che si dipana.

Il saggio ha:
- un'**apertura** che introduce il testo, il problema e il genere del saggio (senza presentare la struttura come un indice)
- le **sezioni tematiche** (una per nucleo), ciascuna delle quali tesse insieme argomento critico e racconto analitico
- una **chiusura** che raccoglie il senso del percorso senza ripetere le tesi

### 4. Come intrecciare le due dimensioni

La tecnica dell'intreccio non è rigida: si adatta al nucleo. Alcune possibilità:

- **Partire dall'opera, arrivare al processo**: si enuncia un'affermazione sull'opera, poi si mostra come quella affermazione ha preso forma — la domanda iniziale, la resistenza, la scoperta
- **Partire dal processo, arrivare all'opera**: si racconta un momento del percorso analitico (una domanda, una sorpresa, un nodo assente), e si mostra cosa rivela del romanzo
- **Tenere le due dimensioni in parallelo**: l'analisi del testo e il racconto del come procedono nello stesso paragrafo, senza separazione netta

La scelta dipende da quale dimensione è più produttiva per quel nucleo. Non uniformare: varietà interna rende il saggio più vivo.

### 5. Tono e destinatario

Il lettore di riferimento è un ricercatore o un critico con familiarità con il discorso interpretativo, aperto alle questioni di metodo, non necessariamente specialista di Werfel né della fenomenologia. Il tono è saggistico: argomentativo, non didattico; riflessivo, non autoreferenziale.

Il saggio può nominare esplicitamente gli assi strutturali e i nodi, spiegandoli brevemente nel contesto — come farebbe qualsiasi saggio critico che usa un quadro teorico senza farne il soggetto esclusivo.

### 6. Lunghezza

Tra **3500 e 5000 parole**. Più lungo dell'articolo, più lungo del resoconto: il saggio integrato ha una densità propria che giustifica la lunghezza. Se la fusione è riuscita, non deve sembrare gonfio — deve sembrare necessario.

### 7. Eliminare i doppioni

I due testi sorgente hanno inevitabilmente sovrapposizioni: alcune affermazioni compaiono in entrambi. Nel saggio integrato, ogni affermazione appare una volta sola, nel posto in cui è più efficace. Non si tratta di tagliare: si tratta di scegliere il registro giusto per ogni affermazione (critico o riflessivo) e tenerlo.

---

## Regola fondamentale

> **Il saggio integrato non è una somma. È una riscrittura.**
>
> I due testi sorgente sono materiale, non struttura. Il risultato deve poter essere letto da chi non ha letto né l'articolo né il resoconto, e deve avere una sua coerenza interna che non dipende dalla conoscenza dei testi di origine.

---

## Percorso di input

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\articolo-finale.md
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\resoconto-processo.md
```

---

## Percorso di output

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5f-saggio-integrato.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\saggio-integrato.md
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella, e un file Markdown con il testo del saggio.
