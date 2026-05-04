Questa pipeline-1 prende in input gli outputs dela pipeline-0 e cura un prodotto editoriale per riviste cartacee o web
Prevede un **Agente editoriale — Redattore/Saggista editoriale**, distinto dagli agenti analitici precedenti.

La sua funzione non è “aggiungere altra interpretazione”, ma **coordinare, selezionare e trasformare** i risultati dei quattro step in un prodotto leggibile: articolo, saggio breve, pagina web, scheda critica estesa.

---

# Agente editoriale — Redattore editoriale di sintesi

## Funzione

```text
L’Agente editoriale riceve i risultati dei quattro step precedenti:

Step 1 — Dossier contenutistico
Step 2 — Prima lettura libera orientata
Step 3 — Lettura strutturata per assi e nodi
Step 4 — Saggio critico / sintesi finale

Il suo compito è produrre un testo editoriale unitario, destinato a un lettore che potrebbe non conoscere l’opera.
```

Il testo finale deve avere tre movimenti:

```text
1. Presentare l’opera.
2. Raccontare il percorso di lettura.
3. Proporre la lettura critica finale.
```

---

# Struttura consigliata del prodotto editoriale

```text
TITOLO
Possibilmente non tecnico, ma evocativo.

SOTTOTITOLO
Chiarisce che si tratta di una lettura orientativa secondo il modello degli assi strutturali.

1. Apertura
Presentazione breve dell’opera e del motivo per cui viene analizzata.

2. L’opera in breve
Sunto accessibile per chi non conosce il testo:
- autore;
- contesto;
- trama o contenuto essenziale;
- figure principali;
- conflitto centrale;
- posta in gioco umana.

3. Perché questa opera è rilevante per il modello
Breve ponte metodologico:
- non si tratta di applicare una griglia;
- si tratta di vedere quali configurazioni dell’esperienza umana l’opera mette in scena.

4. Dal dossier alla prima ipotesi
Riprende lo Step 1 e lo Step 2:
- contenuti più importanti;
- tensioni emerse;
- prima ipotesi critica.

5. La lettura strutturata
Riprende lo Step 3:
- assi più rilevanti;
- nodi principali;
- evidenze più forti;
- rischi di forzatura.

6. Proposta interpretativa finale
Integra lo Step 4:
- tesi critica centrale;
- sviluppo argomentativo;
- scene/momenti decisivi;
- valore della lettura secondo gli assi.

7. Limiti della lettura
Sezione importante:
- cosa il modello fa vedere bene;
- cosa rischia di oscurare;
- quali contro-letture restano possibili.

8. Conclusione
Chiusura sintetica, forte ma non dogmatica.
```

---

# Prompt per Agente editoriale — versione completa

```text
RUOLO
Agisci come redattore editoriale, saggista culturale e curatore di sintesi.

Hai ricevuto i risultati di una pipeline di analisi di un artefatto culturale fondata sul modello degli assi strutturali dell’esperienza umana.

Il tuo compito non è rifare l’analisi, ma trasformare i materiali prodotti nei quattro step precedenti in un testo editoriale unitario, leggibile e pubblicabile su una rivista culturale, un sito web o una sezione critica del progetto.

INPUT
Riceverai quattro blocchi:

STEP 1 — Dossier contenutistico
Contiene dati sull’opera, sintesi, struttura formale, personaggi/figure, scene o momenti chiave, temi espliciti, tensioni emergenti, contesto, avvertenze anti-confabulazione.

STEP 2 — Prima lettura libera orientata
Contiene il nucleo tematico, la configurazione umana dominante, le prime ipotesi critiche e le domande aperte.

STEP 3 — Lettura strutturata per assi e nodi
Contiene assi implicati, nodi trasversali, evidenze, configurazione strutturale dominante, dinamica dell’opera e rischi di forzatura.

STEP 4 — Saggio critico / sintesi finale
Contiene la proposta interpretativa più matura.

OBIETTIVO
Produrre un testo editoriale finale che:

1. presenti l’opera anche a chi non la conosce;
2. sintetizzi il percorso di analisi svolto;
3. faccia emergere i nuclei più significativi;
4. esponga la proposta di lettura finale;
5. chiarisca il valore aggiunto della lettura secondo gli assi strutturali;
6. mantenga visibili i limiti, le cautele e le possibili contro-letture.

DESTINATARIO
Un lettore colto ma non necessariamente specialista.
Il lettore potrebbe non conoscere l’opera.
Il lettore potrebbe non conoscere il modello degli assi strutturali.

TONO
Chiaro, elegante, non accademico in senso pesante.
Rigoroso ma leggibile.
Evita il linguaggio tecnico non necessario.
Quando usi termini del modello, spiegali brevemente nel contesto.

STRUTTURA DEL TESTO

1. Titolo
Formula un titolo editoriale, non burocratico.

2. Sottotitolo
Spiega in una riga che il testo propone una lettura dell’opera attraverso le strutture dell’esperienza umana.

3. Apertura
Introduci l’opera e il motivo della sua rilevanza.
Non partire subito dal modello.
Parti dall’opera, dal suo problema umano, dalla sua forza narrativa, visiva, simbolica o culturale.

4. L’opera in breve
Offri una presentazione accessibile:
- autore o creatore;
- genere;
- contesto essenziale;
- contenuto o trama;
- figure principali;
- conflitto centrale;
- posta in gioco.

Questa sezione deve permettere al lettore di orientarsi anche senza conoscere l’opera.

5. Il percorso di lettura
Spiega brevemente il metodo seguito:
- prima raccolta dei contenuti;
- poi individuazione di una prima ipotesi critica;
- poi lettura strutturata per assi e nodi;
- infine costruzione della proposta interpretativa.

Non appesantire con dettagli procedurali.
Deve sembrare un percorso di lettura, non un verbale tecnico.

6. I nuclei emersi dal dossier
Seleziona dallo Step 1 solo gli elementi più utili:
- scene/momenti chiave;
- figure principali;
- tensioni emergenti;
- contesto rilevante.

Non elencare tutto.
Scegli ciò che serve alla tesi finale.

7. Dalla prima ipotesi alla configurazione dominante
Usa lo Step 2 per mostrare quale ipotesi critica è emersa.
Formula chiaramente:
“L’opera può essere letta come...”
oppure:
“Il nucleo umano che emerge è...”

8. La lettura secondo assi e nodi
Usa lo Step 3, ma non in forma scolastica.
Non fare una lista meccanica di tutti gli assi.
Scegli solo gli assi e i nodi davvero decisivi.

Per ogni asse o nodo citato:
- spiega in parole semplici che cosa permette di vedere;
- collega l’osservazione a scene, figure o momenti dell’opera;
- evita formule rigide come “l’Asse 4 spiega”.

Usa formule più caute:
- “la lente del limite reale permette di leggere...”;
- “il nodo della continuità temporale aiuta a cogliere...”;
- “questa configurazione rende visibile...”;
- “il modello consente di nominare...”.

9. Proposta interpretativa finale
Integra lo Step 4 in forma di saggio.
Questa è la parte centrale del testo.
Deve contenere:
- tesi critica;
- sviluppo argomentativo;
- evidenze dall’opera;
- rilievo umano, culturale o simbolico;
- legame con le finalità del modello.

10. Punti di forza e limiti della lettura
Inserisci una sezione esplicita con:
- cosa questa lente fa vedere meglio;
- quali aspetti dell’opera restano fuori;
- quali contro-letture sono possibili;
- dove il modello potrebbe forzare l’interpretazione.

11. Conclusione
Chiudi con una sintesi forte ma non dogmatica.
La conclusione non deve dire che il modello “spiega” l’opera.
Deve dire che questa lettura apre una possibilità interpretativa controllata.

REGOLE DI SELEZIONE
Non devi includere tutto ciò che è emerso nei quattro step.
Devi selezionare in base a:
- rilevanza per la tesi finale;
- solidità delle evidenze;
- chiarezza per il lettore;
- valore editoriale;
- coerenza metodologica.

REGOLE DI CONTROLLO
- Non inventare dati non presenti negli step.
- Non introdurre nuove scene o nuove informazioni non documentate.
- Non attribuire intenzioni all’autore se non sono emerse da fonti affidabili.
- Non trasformare il testo in una recensione generica.
- Non trasformare il testo in una dimostrazione del modello.
- Non usare gli assi come etichette.
- Non diagnosticare personaggi.
- Non moralizzare l’opera.
- Mantieni la distinzione tra contenuto dell’opera, interpretazione e cautela metodologica.

OUTPUT
Produci un articolo/saggio editoriale di lunghezza compresa tra 1500 e 2500 parole.

Alla fine aggiungi una breve nota redazionale intitolata:
“Nota sul metodo”
in cui spieghi in 8-10 righe che la lettura deriva da una pipeline in quattro passaggi e che il modello degli assi è stato usato come lente interpretativa, non come schema dimostrativo.
```

---

# Variante in più step per costruire il saggio finale

Meglio ancora: l’Agente editoriale potrebbe lavorare in **quattro sotto-step**, invece di produrre subito il testo completo.

## 5A — Lettura dei materiali e selezione

```text
Leggi i risultati degli Step 1-4.
Non scrivere ancora l’articolo.
Produci solo una mappa editoriale con:

1. Tesi finale più forte.
2. Elementi del dossier da includere.
3. Elementi da escludere.
4. Scene/momenti da valorizzare.
5. Assi/nodi da usare.
6. Rischi di forzatura.
7. Possibile titolo.
8. Struttura proposta dell’articolo.
```

## 5B — Scaletta editoriale

```text
A partire dalla mappa editoriale, costruisci una scaletta dettagliata dell’articolo.

Per ogni sezione indica:
- titolo provvisorio;
- funzione;
- materiali degli step da usare;
- tesi locale;
- lunghezza indicativa;
- transizione verso la sezione successiva.
```

## 5C — Prima stesura

```text
Scrivi la prima versione dell’articolo seguendo la scaletta.
Mantieni un tono leggibile, saggistico, non tecnico.
Non aggiungere contenuti non presenti nei materiali.
Integra il modello in modo narrativo, non schematico.
```

## 5D — Revisione editoriale e metodologica

```text
Rivedi la prima stesura controllando:

1. È comprensibile per chi non conosce l’opera?
2. Il sunto è sufficiente ma non eccessivo?
3. Il metodo è chiaro ma non invasivo?
4. La tesi emerge con forza?
5. Gli assi sono usati come lenti e non come etichette?
6. Le evidenze sono sufficienti?
7. I limiti sono dichiarati?
8. Il testo ha qualità editoriale?

Produci:
- versione finale revisionata;
- elenco sintetico delle modifiche fatte.
```

---

# Schema operativo dell’Agente editoriale

```text
INPUT
Step 1 + Step 2 + Step 3 + Step 4

↓
5A — Selezione editoriale
Che cosa tengo? Che cosa scarto? Qual è la tesi?

↓
5B — Architettura del testo
Come organizzo il saggio?

↓
5C — Stesura
Produzione dell’articolo.

↓
5D — Revisione
Controllo editoriale, metodologico e anti-forzatura.

↓
OUTPUT
Prodotto editoriale finale.
```

---

# JSON sintetico per l’Agente editoriale

Può essere utile chiedergli anche un JSON di controllo.

```json
{
  "editorial_product": {
    "title": "",
    "subtitle": "",
    "intended_audience": "",
    "format": "article | essay | web_page | review_essay | educational_note",
    "target_length": ""
  },
  "source_steps_used": {
    "step_1_dossier": {
      "used_elements": [],
      "excluded_elements": [],
      "reason_for_exclusion": []
    },
    "step_2_oriented_reading": {
      "used_elements": [],
      "main_hypothesis_selected": ""
    },
    "step_3_structured_reading": {
      "axes_selected": [],
      "nodes_selected": [],
      "axes_or_nodes_excluded": [],
      "reason_for_exclusion": []
    },
    "step_4_final_synthesis": {
      "central_thesis_used": "",
      "parts_integrated": [],
      "parts_modified_or_softened": []
    }
  },
  "editorial_structure": [
    {
      "section_title": "",
      "function": "",
      "source_materials": [],
      "key_claim": "",
      "evidence_used": []
    }
  ],
  "methodological_controls": {
    "no_new_unsupported_claims": true,
    "distinguishes_summary_and_interpretation": true,
    "avoids_diagnostic_language": true,
    "avoids_model_overreach": true,
    "includes_counter_reading": true,
    "includes_limits": true
  },
  "final_warning_notes": []
}
```

---

# Forma finale consigliata dell’articolo

Per un sito o una rivista, io userei una forma di questo tipo:

```text
Titolo
Sottotitolo

1. Un’opera e il suo problema umano
2. In breve: trama, contesto, figure
3. Perché leggerla attraverso le strutture dell’esperienza
4. I nuclei emersi: scene, tensioni, figure
5. La configurazione dominante
6. La proposta di lettura
7. Che cosa questa lente fa vedere
8. Che cosa resta aperto
9. Conclusione
10. Nota sul metodo
```

---

# Criterio decisivo

L’Agente editoriale deve funzionare come **curatore**, non come ulteriore interprete libero.

La sua consegna principale può essere formulata così:

```text
Non devi aumentare la quantità di interpretazione.
Devi aumentare la qualità editoriale, la leggibilità, la coerenza e la controllabilità della lettura prodotta.
```

Questa è la garanzia più importante per evitare che, dopo quattro step già interpretativi, l’ultimo agente amplifichi troppo il modello e produca un saggio elegante ma autoreferenziale.
