# STEP 3 — Lettura strutturata per assi e nodi

## Obiettivo
Tradurre l'intuizione critica dello Step 2 in una scheda metodologicamente controllata, attraverso l'applicazione esplicita degli assi strutturali. Lo step produce una mappa interpretativa rigorosa che prepara il materiale per il saggio finale.

---

## Input atteso

- Il documento JSON dello **Step 1** (dossier contenutistico)
- Il documento JSON dello **Step 2** (lettura libera orientata)

---

## Gli assi strutturali di riferimento

Questo step applica il sistema degli **assi strutturali** sviluppato a partire dalla fenomenologia di Edmund Husserl e Maurice Merleau-Ponty. I 6 assi sono pre-compilati e si trovano in:

`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\`

Prima di procedere con l'analisi, **leggi i file JSON degli assi** per verificare i nodi strutturali, i concetti-ponte e i rischi di riduzione di ciascuno. I 6 assi sono:

| ID | Nome |
|----|------|
| `asse_1` | Ontologico–fenomenologico |
| `asse_2` | Affettivo–morale |
| `asse_3` | Normativo–educativo |
| `asse_4` | Separazione e Limite |
| `asse_5` | Desiderio |
| `asse_6` | Storico–culturale |

---

## Istruzioni operative per Cowork

### 1. Selezione degli assi implicati

Leggi i 6 file JSON degli assi. Per ciascuno, valuta il suo grado di implicazione nell'opera:
- **alto**: l'asse è direttamente e profondamente implicato dalla configurazione dell'opera
- **medio**: l'asse è presente ma non è il cuore della lettura
- **basso/assente**: l'asse non sembra rilevante per questa opera

Descrivi per ogni asse implicato (grado alto o medio) **in che modo specifico** è attivato dall'opera. Usa i nodi strutturali e i concetti-ponte dei file JSON degli assi come vocabolario tecnico.

### 2. Nodi trasversali attivati

Identifica i nodi strutturali — presenti nei file degli assi — che l'opera sembra mettere in gioco con maggiore intensità. Un nodo è "attivato" quando le evidenze dell'opera lo richiamano in modo non forzato.

Per ogni nodo attivato, indica:
- L'asse di appartenenza
- La definizione breve (dal file JSON)
- L'evidenza nell'opera che lo attiva

### 3. Evidenze testuali, visive o narrative

Per ogni asse e nodo attivati, indica le evidenze concrete nell'opera: scene specifiche, dialoghi, immagini, momenti formali, strutture narrative. Le evidenze devono essere tratte dal dossier dello Step 1.

> **Regola critica**: se non hai un'evidenza concreta nell'opera per un nodo o un asse, non applicarlo. La mancanza di evidenza è un'informazione critica: registrala come "nodo assente" o "asse non implicato".

### 4. Configurazione strutturale dominante

Sulla base dell'analisi per assi, descrivi la **configurazione strutturale dominante** dell'opera: non la somma degli assi attivati, ma la forma d'insieme che emerge dalla loro interazione. È il pattern interpretativo che organizza la lettura.

### 5. Dinamica dell'opera

Descrivi la dinamica dell'opera come movimento complessivo. Scegli la forma più adeguata tra:
- **espansione**: l'opera allarga progressivamente il campo del possibile
- **resistenza**: l'opera mostra un soggetto (o una configurazione) che resiste a una pressione
- **restringimento**: il campo si chiude progressivamente
- **collasso**: la configurazione non regge e si dissolve
- **trasformazione**: avviene un cambiamento qualitativo della configurazione
- **sospensione**: la dinamica rimane aperta, irrisolta

Puoi indicare più di una dinamica se l'opera le combina in fasi.

### 6. Rischi di forzatura

Segnala esplicitamente i rischi di forzatura interpretativa: dove l'analisi per assi rischia di imporre una griglia che non corrisponde all'opera, dove si potrebbe stare proiettando un quadro invece di leggere una configurazione. Consulta la sezione `reduction_risks` di ogni asse per identificare i rischi specifici.

---

## Regola fondamentale

> **Non diagnosticare personaggi. Leggere configurazioni dell'opera. Gli assi sono una lente, non una gabbia. Se un'interpretazione è troppo pulita, probabilmente è forzata.**

---

## Percorso di input

Leggi i documenti prodotti dagli step precedenti da:

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-2-lettura-libera-orientata.json
```

Leggi i file degli assi strutturali da:

```
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_1.json
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_2.json
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_3.json
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_4.json
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_5.json
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled\asse_6.json
```

Lo slug è quello generato durante lo Step 1. Se non lo conosci, chiedilo all'utente prima di procedere.

---

## Percorso di output

Salva il file di output nel percorso:

```
C:\Users\nnmrd\Documents\Claude\Projects\HCAIRE Cultura\letture\{slug}\step-3-lettura-strutturata-per-assi.json
```

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella.
