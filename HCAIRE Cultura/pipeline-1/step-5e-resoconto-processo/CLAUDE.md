# STEP 5E — Resoconto del processo

## Obiettivo
Produrre un **resoconto discorsivo del processo analitico**: un testo in forma di articolo che racconta come, partendo dai materiali dell'opera, si è arrivati alla proposta interpretativa dell'articolo finale.

Non è un riassunto dei quattro step analitici. Non è una replica dell'articolo. È il racconto del percorso: le scelte fatte, le scoperte inattese, i momenti in cui l'analisi ha trovato resistenza, le assenze significative, le tensioni irrisolte. Un **dietro le quinte** scritto per un lettore che ha letto l'articolo e vuole capire come è stato costruito.

---

## Input atteso

- I documenti JSON degli **Step 1–4** (pipeline analitica)
- Il documento JSON dello **Step 5D** (articolo finale, per consultazione)

---

## Stile editoriale

Prima di scrivere, leggi il file:
```
C:\my\claude\claude-cowork\HCAIRE Cultura\pipeline-1\stile-editoriale.md
```
Le norme lì contenute si applicano anche al resoconto del processo. In particolare: non citare i nomi degli step ("Step 1", ecc.), non usare il termine "pipeline", e non formulare frasi che presentino il metodo come condizione necessaria dei risultati critici.

---

## Istruzioni operative per Cowork

### 1. Rileggi il percorso analitico completo

Prima di scrivere, rileggi i quattro step analitici come se fossero un unico processo in evoluzione. Nota:
- Come l'ipotesi critica si trasforma dal Step 2 al Step 4
- Quali assi sono stati selezionati e con quale motivazione
- Quali nodi erano attesi e non si sono trovati (dato critico)
- Dove l'analisi ha trovato resistenza o ambiguità

### 2. Identifica i momenti salienti del processo

Seleziona 3–5 momenti in cui l'analisi ha compiuto uno scarto significativo — un'intuizione, una scoperta inattesa, un problema che ha richiesto una scelta interpretativa. Questi momenti sono il materiale narrativo del resoconto.

### 3. Scrivi il resoconto in forma discorsiva

Il testo deve:
- **Aprire** con il problema che la lettura si è posta: la domanda critica di partenza
- **Raccontare** il percorso in modo narrativo, non come lista di step
- **Nominare** le scelte decisive: quali assi, quali nodi, e perché
- **Dare risalto** alle scoperte inattese — in particolare alle assenze significative
- **Spiegare** come la tesi si è formata: il percorso dall'ipotesi provvisoria alla formulazione finale
- **Riconoscere** le tensioni irrisolte: dove l'analisi ha trovato resistenza o ambiguità
- **Concludere** con una riflessione su cosa questa metodologia permette di vedere e cosa lascia fuori

### 4. Tono e destinatario

Il testo è rivolto a un **lettore curioso del metodo**, che ha letto l'articolo finale e vuole capire come è stato prodotto. Non presuppone familiarità con la fenomenologia o con il sistema degli assi strutturali. Il tono è saggistico-divulgativo: rigoroso ma accessibile.

Il resoconto può — anzi deve — usare la nomenclatura degli assi (asse_1, asse_4, nodo 'riparazione', ecc.) perché il suo obiettivo è proprio rendere visibile il lavoro metodologico. Ma ogni volta che usa un termine tecnico deve spiegarlo brevemente nel contesto.

### 5. Lunghezza

Tra **1000 e 1800 parole**. Più breve dell'articolo: è un testo di accompagnamento, non un'opera autonoma.

---

## Regola fondamentale

> **Il resoconto racconta il processo, non ribatte l'interpretazione.**
>
> Non deve ripetere le tesi dell'articolo come se le stesse dimostrando di nuovo. Deve spiegare come quelle tesi sono nate: attraverso quali scelte, quali scoperte, quali resistenze.

---

## Percorso di input

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-2-lettura-libera-orientata.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-3-lettura-strutturata-per-assi.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-4-saggio-critico-revisione.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5d-revisione-finale.json
```

Lo slug è quello generato durante lo Step 1.

---

## Percorso di output

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\step-5e-resoconto-processo.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\editorial\resoconto-processo.md
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella, e un file Markdown con il testo del resoconto.
