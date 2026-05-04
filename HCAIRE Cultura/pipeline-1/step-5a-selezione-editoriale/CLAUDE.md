# STEP 5A — Selezione editoriale

## Obiettivo
Leggere tutti i materiali prodotti nei quattro step analitici e produrre una **mappa editoriale**: una selezione ragionata di ciò che vale la pena includere nel prodotto editoriale finale, con l'identificazione della tesi più forte, delle scene da valorizzare, degli assi da usare e dei rischi da presidiare.

**Non scrivere ancora l'articolo.** Questo step produce solo la mappa, non il testo.

---

## Input atteso

- Il documento JSON dello **Step 1** (dossier contenutistico)
- Il documento JSON dello **Step 2** (lettura libera orientata)
- Il documento JSON dello **Step 3** (lettura strutturata per assi)
- Il documento JSON dello **Step 4** (saggio critico)

---

## Istruzioni operative per Cowork

### 1. Leggi tutti e quattro gli step

Leggi i file JSON degli step 1, 2, 3 e 4 prima di procedere. Non iniziare la selezione senza avere una visione d'insieme dei materiali.

### 2. Seleziona la tesi finale come bussola editoriale

Partendo dalla tesi dello Step 4, verifica se è enunciabile in modo accessibile per un lettore che non conosce né l'opera né il modello degli assi. Se necessario, riformulala — non modificandone il contenuto, ma rendendola più leggibile. Questa tesi riformulata guiderà tutte le scelte successive.

### 3. Mappa gli elementi da includere e da escludere

Per ogni step, identifica:
- Cosa è **indispensabile** per costruire il testo editoriale: le informazioni senza le quali il lettore non riesce a seguire il ragionamento
- Cosa è **tecnico o ridondante** e può essere omesso: dettagli metodologici, nodi secondari, varianti non sviluppate

Motiva le esclusioni: non si tratta di censurare, ma di scegliere in funzione del lettore e della tesi.

### 4. Identifica le scene e i momenti da valorizzare

Seleziona 2–3 scene o momenti dell'opera che possono fare da pilastri narrativi nel testo editoriale: quelli che, raccontati bene a chi non conosce l'opera, rendono immediatamente visibile la posta in gioco umana. Privilegia le scene che sono già state analizzate nello Step 4.

### 5. Seleziona gli assi e i nodi editorialmente utili

Non tutti gli assi identificati nello Step 3 vanno inclusi nel testo editoriale. Seleziona solo quelli che:
- supportano direttamente la tesi editoriale
- sono spiegabili in modo accessibile senza terminologia tecnica pesante
- arricchiscono la lettura senza appesantirla

Per ciascun asse o nodo selezionato, formula una **funzione editoriale**: come lo useresti nel testo, con quale formula linguistica, per illuminare quale aspetto.

### 6. Segnala i rischi di forzatura residui

Riprendi i rischi già identificati nello Step 3. Nel passaggio da analisi a testo editoriale alcuni rischi si attenuano (perché si semplifica) e altri si amplificano (perché si perde la cautela metodologica). Identifica quelli più critici per questo testo.

### 7. Proponi il titolo e la struttura

Proponi:
- Un **titolo editoriale principale**: evocativo, non burocratico, non tecnico
- 2–3 **titoli alternativi** per confronto
- Una **struttura proposta** dell'articolo: le sezioni, la loro funzione, i materiali da cui attingono, la lunghezza indicativa

---

## Regola fondamentale

> **Non aumentare la quantità di interpretazione. Selezionare e organizzare ciò che è già stato prodotto.**
>
> L'Agente editoriale è un curatore, non un interprete aggiuntivo. La sua consegna è aumentare la qualità editoriale e la leggibilità, non ampliare il modello.

---

## Percorso di input

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-2-lettura-libera-orientata.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-3-lettura-strutturata-per-assi.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-4-saggio-critico-revisione.json
```

Lo slug è quello generato durante lo Step 1. Se non lo conosci, chiedilo all'utente prima di procedere.

---

## Percorso di output

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\editorial\step-5a-selezione-editoriale.json
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella.
