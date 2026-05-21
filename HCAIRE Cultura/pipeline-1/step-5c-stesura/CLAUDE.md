# STEP 5C — Prima stesura

## Obiettivo
Scrivere la **prima versione completa del testo editoriale**, seguendo la scaletta dello Step 5B. Il testo deve essere già leggibile, saggistico e coerente — non una bozza approssimativa, ma una stesura di lavoro controllata che lo Step 5D potrà migliorare senza dover riscrivere da zero.

---

## Input atteso

- Il documento JSON dello **Step 5B** (scaletta editoriale)
- Il documento JSON dello **Step 5A** (selezione editoriale, per consultazione)
- I documenti JSON degli **Step 1–4** (per verificare le evidenze durante la stesura)

---

## Stile editoriale

Prima di iniziare a scrivere, leggi il file:
```
C:\my\claude\claude-cowork\HCAIRE Cultura\pipeline-1\stile-editoriale.md
```
Le norme lì contenute si applicano a tutto il testo prodotto in questo step.

---

## Istruzioni operative per Cowork

### 1. Segui la scaletta — non deviare senza motivo

Scrivi sezione per sezione seguendo la scaletta dello Step 5B. Se durante la stesura emerge una necessità di deviare dalla scaletta (aggiungere una sezione, cambiare ordine, modificare una transizione), registrala nelle `note_per_revisione` invece di modificare la struttura senza segnalarlo.

### 2. Tono e registro

- **Chiaro ed elegante**: non accademico in senso pesante, non giornalistico in senso superficiale
- **Saggistico**: ragiona, non cataloga; argomenta, non enumera
- **Non tecnico, ma preciso**: quando usi termini del modello (asse, nodo, configurazione), spiegali brevemente nel contesto, senza mai fermarti a definirli come in un manuale
- **Non diagnostico**: non diagnosticare personaggi, non moralizzare l'opera

### 3. Regole di controllo durante la stesura

- Non inventare dati non presenti negli step analitici
- Non introdurre nuove scene o informazioni non documentate
- Non attribuire intenzioni all'autore se non emerse da fonti affidabili
- Non trasformare il testo in una recensione generica
- Non trasformare il testo in una dimostrazione del modello
- Non usare gli assi come etichette: "l'Asse 4 spiega questo" è una formula da evitare
- Mantieni la distinzione tra contenuto dell'opera, interpretazione e cautela metodologica

### 4. Usa le formule suggerite per gli assi

Nello Step 5A sono state indicate formule linguistiche per ciascun asse o nodo selezionato. Usale come punto di partenza, non come formula rigida. Esempi di registro appropriato:
- "la lente del limite reale permette di leggere..."
- "il nodo della temporalità vissuta aiuta a cogliere..."
- "questa configurazione rende visibile..."
- "il modello consente di nominare quello che altrimenti resterebbe implicito..."

### 5. Scrivi la nota sul metodo

In fondo al testo, aggiungi una breve nota redazionale intitolata **"Nota sul metodo"** di 8–10 righe che spieghi:
- che la lettura deriva da una pipeline in quattro passaggi (dossier, prima lettura, lettura strutturata per assi, saggio critico)
- che il modello degli assi strutturali è usato come lente interpretativa, non come schema dimostrativo
- che l'obiettivo non è "spiegare" l'opera ma aprire una prospettiva di lettura controllata

La nota deve essere sobria, non autopromozionale.

### 6. Registra le note per la revisione

Durante la stesura, segnala nella sezione `note_per_revisione` del JSON di output:
- punti del testo che senti come deboli o non ancora risolti
- deviazioni dalla scaletta e relativa motivazione
- formule che potrebbero essere migliorate
- rischi di forzatura che hai percepito durante la scrittura

---

## Regola fondamentale

> **Scrivi per il lettore, non per il modello.**
>
> Il testo finale deve essere comprensibile e coinvolgente anche per chi non conosce il progetto HCAIRE, il sistema degli assi strutturali o l'opera analizzata. Se per capire una frase bisogna aver letto i quattro step precedenti, quella frase va riscritta.

---

## Percorso di input

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5b-scaletta.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5a-selezione-editoriale.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-2-lettura-libera-orientata.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-3-lettura-strutturata-per-assi.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-4-saggio-critico-revisione.json
```

Lo slug è quello generato durante lo Step 1.

---

## Percorso di output

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5c-stesura.json
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella.
