# STEP 5D — Revisione finale

## Obiettivo
Produrre la **versione finale del prodotto editoriale**: revisionare la prima stesura dello Step 5C attraverso un controllo sistematico editoriale e metodologico, poi consegnare il testo definitivo accompagnato da un log delle modifiche effettuate.

Questo è l'ultimo step della pipeline. Il suo output è il prodotto editoriale pubblicabile.

---

## Input atteso

- Il documento JSON dello **Step 5C** (prima stesura)
- Il documento JSON dello **Step 5B** (scaletta, per verificare la coerenza strutturale)
- Il documento JSON dello **Step 5A** (selezione editoriale, per verificare il rispetto delle scelte)
- I documenti JSON degli **Step 1–4** (per verificare le evidenze se necessario)

---

## Stile editoriale

Prima di procedere con la revisione, rileggi il file:
```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\pipeline-1\stile-editoriale.md
```
Le norme lì contenute si applicano anche alla versione finale — la revisione è il momento in cui verificarle sistematicamente, non solo la checklist interna.

---

## Istruzioni operative per Cowork

### 1. Leggi la prima stesura e le note per la revisione

Prima di procedere con la revisione, leggi per intero la prima stesura dello Step 5C e le `note_per_revisione` che l'agente ha lasciato. Queste note indicano i punti più critici su cui concentrare l'attenzione.

### 2. Applica la checklist di controllo

Per ogni domanda della checklist, valuta il testo e intervieni se necessario:

**Comprensibilità**
- Il testo è comprensibile per chi non conosce l'opera?
- Il sunto dell'opera è sufficientemente chiaro senza essere eccessivo?
- I termini del modello sono spiegati nel contesto?

**Metodo**
- Il metodo è presente ma non invasivo? Non deve sembrare un verbale tecnico
- Gli assi sono usati come lenti, non come etichette? Verifica che non compaia mai la formula "l'Asse X spiega che..."
- I limiti della lettura sono dichiarati esplicitamente?
- La contro-lettura è presente e onesta?

**Tesi e argomentazione**
- La tesi emerge con forza e chiarezza?
- Le evidenze sono sufficienti e riconducibili ai materiali degli step analitici?
- Lo sviluppo argomentativo è coeso? Le transizioni funzionano?

**Qualità editoriale**
- Il tono è saggistico e non da referto?
- Il testo ha coesione: le sezioni si tengono?
- La lunghezza è adeguata (1500–2500 parole totali)?
- La nota sul metodo è sobria e non autopromozionale?

**Controllo metodologico anti-forzatura**
- Non ci sono dati inventati o scene non documentate?
- Non ci sono intenzioni attribuite all'autore senza base?
- La distinzione tra contenuto dell'opera, interpretazione e cautela metodologica è mantenuta?
- I personaggi non vengono diagnosticati?

### 3. Rivedi il testo

Apporta le modifiche necessarie. Per ogni modifica significativa, registra nel log:
- la sezione coinvolta
- la natura della modifica
- la motivazione

Non riscrivere da zero se non strettamente necessario. La revisione è un affinamento, non una riscrittura.

### 4. Verifica la nota sul metodo

La nota sul metodo deve:
- spiegare in 8–10 righe il processo di analisi (pipeline in quattro step)
- chiarire che gli assi sono una lente, non uno schema dimostrativo
- concludere con la formula o una sua variante: "questo testo propone una prospettiva di lettura controllata, non una spiegazione dell'opera"

### 5. Produce il documento JSON finale

Il documento JSON di output contiene:
- la versione finale del testo (titolo, sottotitolo, corpo, nota sul metodo)
- la checklist di controllo compilata
- il log delle modifiche effettuate

### 6. Esporta il testo finale in Markdown

Dopo aver salvato il JSON, estrai il testo finale dal campo `testo_finale` e scrivilo come file Markdown autonomo nella stessa cartella. Questo file è destinato alla lettura, alla condivisione e alla visualizzazione diretta — senza necessità di aprire il JSON.

Il file Markdown deve contenere:
- titolo (come `# Titolo`)
- sottotitolo (come testo in corsivo o come paragrafo introduttivo)
- corpo del testo completo
- nota sul metodo (come sezione finale separata da `---`)

Il file deve essere scritto in Markdown pulito, senza metadati tecnici né riferimenti alla pipeline.

---

## Regola fondamentale

> **La conclusione non deve dire che il modello "spiega" l'opera.**
> **Deve dire che questa lettura apre una possibilità interpretativa controllata.**

Il prodotto editoriale è criticamente onesto quando riconosce sia ciò che ha illuminato sia ciò che ha lasciato nell'ombra.

---

## Percorso di input

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\step-5c-stesura.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\step-5b-scaletta.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\step-5a-selezione-editoriale.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-4-saggio-critico-revisione.json
```

Lo slug è quello generato durante lo Step 1.

---

## Percorso di output

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\step-5d-revisione-finale.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\articolo-finale.md
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella, e un file Markdown con il testo finale dell'articolo.
