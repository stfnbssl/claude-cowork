# STEP 4 — Saggio critico e revisione

## Obiettivo
Produrre una lettura finale: leggibile, criticamente difendibile, che integri organicamente tutto il lavoro dei tre step precedenti in un testo unitario. Il saggio non è la somma degli step: è la loro sintesi, in cui la complessità dell'analisi diventa comprensibile senza perdere rigore.

---

## Input atteso

- Il documento JSON dello **Step 1** (dossier contenutistico)
- Il documento JSON dello **Step 2** (lettura libera orientata)
- Il documento JSON dello **Step 3** (lettura strutturata per assi)

---

## Istruzioni operative per Cowork

### 1. Elabora la tesi interpretativa centrale

Partendo dall'ipotesi critica dello Step 2 e dalla configurazione strutturale dello Step 3, formula la **tesi interpretativa centrale**: un'affermazione chiara, specifica e difendibile su che cosa fa questa opera — su quale esperienza umana mette in forma, con quale configurazione, con quale dinamica.

La tesi deve:
- essere enunciabile in 2-3 frasi
- essere radicata negli elementi del dossier (Step 1)
- non coincidere semplicemente con il tema esplicito dell'opera
- lasciare aperta la possibilità di una contro-lettura

### 2. Scrivi il saggio breve o la scheda critica

Produci un testo scritto (non un elenco di punti) di lunghezza adeguata all'opera e alla complessità dell'analisi. Il testo deve:

- **Aprire** con un'entrata nell'opera: una scena, un momento, un'immagine che radica la lettura nel concreto
- **Sviluppare** la tesi attraverso l'analisi dei momenti più forti dell'opera, con riferimento agli assi e ai nodi emersi nello Step 3
- **Integrare** gli assi strutturali in modo narrativo: non come lista ("l'asse 1 mostra che..., l'asse 2 mostra che...") ma come elementi del ragionamento interpretativo
- **Proporre** la contro-lettura
- **Riconoscere** i limiti della lettura
- **Concludere** con una valutazione del valore aggiunto del modello

### 3. Analizza le scene/momenti più forti

Identifica 2-4 momenti dell'opera particolarmente ricchi dal punto di vista della configurazione strutturale. Per ciascuno, svolgi un'analisi ravvicinata che mostri come la tesi si radica nelle evidenze. Questi momenti sono il cuore del saggio.

### 4. Integrazione narrativa degli assi

Gli assi strutturali non devono comparire nel saggio come elenco scolastico ("si evidenziano l'asse 1, l'asse 2 e l'asse 4"). Devono emergere come strumenti di comprensione: il loro nome tecnico può essere usato, ma inserito nel flusso del ragionamento. Chiedi: "Se tolgo il nome di questo asse, il ragionamento regge ugualmente?"

### 5. Scrivi la contro-lettura

Elabora la prospettiva critica più seria che si potrebbe opporre alla tua tesi. Deve essere onesta e non di comodo: una lettura alternativa realmente possibile, che l'opera supporta almeno parzialmente. La contro-lettura non confuta il saggio: lo arricchisce mostrando che l'opera è più complessa di qualsiasi griglia.

### 6. Indica i limiti della lettura

Segnala esplicitamente:
- Cosa questa lente non vede o vede con distorsione
- Elementi dell'opera che restano irriducibili all'analisi svolta
- Aspetti che richiederebbero uno studio più approfondito o materiali diversi

### 7. Valuta il valore aggiunto del modello

Concludi con una valutazione critica: cosa permette di vedere questo approccio fenomenologico che altri approcci avrebbero trascurato? Quali aspetti dell'opera diventano visibili attraverso gli assi strutturali?

---

## Regola fondamentale sulla conclusione

> **La conclusione non deve dire: "il modello spiega l'opera".**
> **Deve dire: "questa lente permette di vedere alcuni aspetti dell'opera, lasciandone aperti altri".**

Il saggio è criticamente onesto quando riconosce sia ciò che ha illuminato sia ciò che ha lasciato nell'ombra.

---

## Tono e stile

- Scrittura in prima persona critica o in terza persona saggistica: scegli in coerenza con lo stile che meglio serve l'opera analizzata
- Linguaggio tecnico degli assi ammesso, ma sempre al servizio della comprensione, non della dimostrazione
- Evitare il tono da referto clinico: si interpreta un'opera d'arte, non si compila una cartella
- Ammessa la presa di posizione critica: il saggio non è neutro, è difendibile

---

## Percorso di input

Leggi tutti i documenti prodotti dagli step precedenti da:

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-2-lettura-libera-orientata.json
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-3-lettura-strutturata-per-assi.json
```

Lo slug è quello generato durante lo Step 1. Se non lo conosci, chiedilo all'utente prima di procedere.

---

## Percorso di output

Salva il file di output nel percorso:

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-4-saggio-critico-revisione.json
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella. Il campo `testo_saggio` conterrà il testo completo in formato Markdown.
