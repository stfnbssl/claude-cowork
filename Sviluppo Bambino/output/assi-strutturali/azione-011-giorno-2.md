---
id: azione-011-giorno-2
azione: 011
giorno: 2 di 5
stato: completato
autori_da_trattare: 9
libri_da_trattare: 12
---

# Azione 011 — Giorno 2: Asse 2 — Psicoanalisi e genesi della vita morale (9 autori, 12 libri)

## Contesto dell'azione

Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** del progetto Sviluppo Bambino (HCAIRE).

**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione degli assi strutturali, produrre un testo che spiega perché quel pensatore / quel testo è rilevante per il progetto Sviluppo Bambino.

**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-2.json` nel formato descritto nelle linee guida sotto. Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà i file JSON giornalieri in `autori.json` e `bibliografia.json`.

---

## Focus di oggi

**Asse 2 — Affettivo-morale**

I pensatori della psicoanalisi e della genesi morale. Klein, Freud e Bion costruiscono la teoria dell'interiorizzazione dell'altro; Levinas fornisce il fondamento etico del volto; Trevarthen e Stern portano la ricerca empirica sull'intersoggettività precoce; Piaget e Kohlberg aprono sul versante dello sviluppo morale.

---

## Linee guida per la scrittura

**Obiettivo di ogni testo**: spiegare perché questo autore / questo libro è importante *per il progetto Sviluppo Bambino*, non fornire una biografia o una recensione generale.

**Prospettiva**: il lettore del sito HCAIRE (educatore, clinico, ricercatore) vuole capire il legame specifico tra questo pensatore e il modello degli assi strutturali.

**Per gli autori** (150–200 parole):
1. Chi è, in una frase (disciplina, epoca, tradizione)
2. Qual è il contributo specifico al modello degli assi strutturali
3. In quali assi il suo pensiero è presente e come
4. Una frase finale sul perché vale la pena conoscerlo per questo progetto

**Per i libri** (100–150 parole):
1. Di cosa tratta il libro, in una frase
2. Quale problema del modello aiuta a rispondere
3. In quali assi viene usato e come

**Tono**: accessibile ma non divulgativo, preciso ma non accademico. Evitare riassunti enciclopedici.

**Output JSON** (al termine del giorno di lavoro, aggiungere al file `rilevanza-GIORNO-N.json`):
```json
{
  "autori": [
    { "id": "edmund-husserl", "rilevanza": "..." },
    ...
  ],
  "libri": [
    { "id": "husserl-lezioni-sulla-coscienza-interna-del-tempo", "rilevanza": "..." },
    ...
  ]
}
```


---

## Autori da trattare oggi (9)

### Melanie Klein
- **ID**: `melanie-klein`
- **Disciplina**: Psicoanalisi
- **Periodo**: 1882–1960
- **Nazionalità**: Austriaca / britannica
- **Assi**: Asse 2
- **Note**: Psicoanalista. Teorica delle relazioni oggettuali. Citata per il concetto di colpa come segnale di integrazione dell'oggetto e la posizione depressiva.

### Sigmund Freud
- **ID**: `sigmund-freud`
- **Disciplina**: Psicoanalisi
- **Periodo**: 1856–1939
- **Nazionalità**: Austriaca
- **Assi**: Asse 2, Asse 4, Asse 5
- **Note**: Fondatore della psicoanalisi. Citato per il Super-io, il lavoro del lutto, l'onnipotenza infantile e la distinzione tra colpa e giudizio responsabile.

### Wilfred R. Bion
- **ID**: `wilfred-bion`
- **Disciplina**: Psicoanalisi
- **Periodo**: 1897–1979
- **Nazionalità**: Britannica / indiana
- **Assi**: Asse 4
- **Note**: Psicoanalista. Teorico del «contenitore-contenuto», della tolleranza della frustrazione e del «Learning from Experience». Citato per esperienze non trasformabili in pensiero.

### Paul Ricoeur
- **ID**: `paul-ricoeur`
- **Disciplina**: Fenomenologia, ermeneutica, filosofia morale
- **Periodo**: 1913–2005
- **Nazionalità**: Francese
- **Assi**: Asse 1, Asse 3, Asse 4, Asse 5, Asse 6
- **Note**: Filosofo ermeneutico. Citato per l'identità narrativa, la responsabilità come risposta, il simbolo, la narrazione e il legame tra temporalità e racconto.

### Emmanuel Levinas
- **ID**: `emmanuel-levinas`
- **Disciplina**: Fenomenologia, filosofia etica
- **Periodo**: 1906–1995
- **Nazionalità**: Francese / lituano-ebraica
- **Assi**: Asse 1, Asse 2, Asse 4
- **Note**: Filosofo dell'alterità. Citato per la responsabilità come risposta all'altro prima della norma e per l'idea che l'altro «interrompe e obbliga».

### Jean Piaget
- **ID**: `jean-piaget`
- **Disciplina**: Psicologia dello sviluppo, epistemologia genetica
- **Periodo**: 1896–1980
- **Nazionalità**: Svizzera
- **Assi**: Asse 2, Asse 3
- **Note**: Psicologo dello sviluppo. Citato come termine di confronto e delimitazione: capire una regola non equivale all'esercizio del giudizio normativo.

### Lawrence Kohlberg
- **ID**: `lawrence-kohlberg`
- **Disciplina**: Psicologia morale
- **Periodo**: 1927–1987
- **Nazionalità**: Statunitense
- **Assi**: Asse 2, Asse 3
- **Note**: Psicologo morale. Citato come termine di confronto critico: il modello stadiale riduce il giudizio a schema cognitivo.

### Colwyn Trevarthen
- **ID**: `colwyn-trevarthen`
- **Disciplina**: Psicologia dello sviluppo
- **Periodo**: 1931–
- **Nazionalità**: Scozzese
- **Assi**: Asse 4
- **Note**: Psicologo dello sviluppo. Teorico dell'intersoggettività primaria e delle «sintonie» come base della comunicazione pre-verbale.

### Daniel Stern
- **ID**: `daniel-stern`
- **Disciplina**: Psicologia dello sviluppo, psichiatria infantile
- **Periodo**: 1934–2012
- **Nazionalità**: Statunitense
- **Assi**: Asse 4, Asse 5
- **Note**: Psichiatra infantile. Teorico delle «sintonizzazioni affettive» e del sé emergente nel bambino piccolo.

---

## Libri da trattare oggi (12)

### The Maturational Processes and the Facilitating Environment
- **ID**: `winnicott-maturational-processes`
- **Autore**: Donald W. Winnicott
- **Anno**: 1965
- **Genere**: Psicoanalisi dello sviluppo
- **Assi**: Asse 2
- **Contesto citazione**: Capacity for concern, sopravvivenza dell'oggetto, responsabilità pre-normativa.

### The Capacity for Concern
- **ID**: `winnicott-capacity-for-concern`
- **Autore**: Donald W. Winnicott
- **Anno**: 1965
- **Genere**: Psicoanalisi dello sviluppo
- **Assi**: Asse 2
- **Titolo originale**: The Capacity for Concern (in: The Maturational Processes)
- **Contesto citazione**: La colpa diventa feconda solo se può trasformarsi in gesto di riparazione.

### The Use of an Object
- **ID**: `winnicott-use-of-an-object`
- **Autore**: Donald W. Winnicott
- **Anno**: 1969
- **Genere**: Psicoanalisi dello sviluppo
- **Assi**: Asse 2
- **Titolo originale**: The Use of an Object and Relating through Identifications
- **Contesto citazione**: «The object survives the subject's destructiveness».

### Envy and Gratitude
- **ID**: `klein-envy-and-gratitude`
- **Autore**: Melanie Klein
- **Anno**: 1957
- **Genere**: Psicoanalisi
- **Assi**: Asse 2
- **Contesto citazione**: La colpa nasce quando l'aggressività riguarda un oggetto che è anche amato; integrazione oggetto buono e cattivo.

### L'Io e l'Es
- **ID**: `freud-io-e-es`
- **Autore**: Sigmund Freud
- **Anno**: 1923
- **Genere**: Psicoanalisi
- **Assi**: Asse 2
- **Titolo originale**: Das Ich und das Es
- **Contesto citazione**: Il Super-io può diventare tanto più severo quanto più il soggetto è virtuoso.

### Learning from Experience
- **ID**: `bion-learning-from-experience`
- **Autore**: Wilfred R. Bion
- **Anno**: 1962
- **Genere**: Psicoanalisi
- **Assi**: Asse 4
- **Contesto citazione**: Esperienze non immediatamente trasformabili in pensiero; tolleranza della frustrazione.

### Il visibile e l'invisibile
- **ID**: `merleau-ponty-il-visibile-e-linvisibile`
- **Autore**: Maurice Merleau-Ponty
- **Anno**: 1968
- **Genere**: Fenomenologia
- **Assi**: Asse 2, Asse 3
- **Titolo originale**: Le visible et l'invisible
- **Contesto citazione**: La presenza che continua a operare in assenza; il reale eccede ogni tematizzazione compiuta del senso.

### Totalità e infinito
- **ID**: `levinas-totalita-e-infinito`
- **Autore**: Emmanuel Levinas
- **Anno**: 1961
- **Genere**: Fenomenologia, filosofia etica
- **Assi**: Asse 1, Asse 2, Asse 4
- **Titolo originale**: Totalité et Infini
- **Contesto citazione**: L'altro come infinito che interrompe e obbliga; la responsabilità come risposta all'altro prima di ogni norma.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Altrimenti che essere, o al di là dell'essenza
- **ID**: `levinas-altrimenti-che-essere`
- **Autore**: Emmanuel Levinas
- **Anno**: 1974
- **Genere**: Fenomenologia, filosofia etica
- **Assi**: Asse 4
- **Titolo originale**: Autrement qu'être ou au-delà de l'essence
- **Contesto citazione**: La responsabilità non fondata su sovranità; la presenza dell'altro senza appropriazione.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Communication and Cooperation in Early Infancy
- **ID**: `trevarthen-communication-cooperation`
- **Autore**: Colwyn Trevarthen
- **Anno**: 1979
- **Genere**: Psicologia dello sviluppo
- **Assi**: Asse 4
- **Titolo originale**: Communication and Cooperation in Early Infancy: A Description of Primary Intersubjectivity
- **Contesto citazione**: L'intersoggettività primaria come struttura della relazione pre-verbale; le sintonie come base della comunicazione.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Il mondo interpersonale del bambino
- **ID**: `stern-mondo-interpersonale-del-bambino`
- **Autore**: Daniel Stern
- **Anno**: 1985
- **Genere**: Psicologia dello sviluppo, psichiatria infantile
- **Assi**: Asse 4, Asse 5
- **Titolo originale**: The Interpersonal World of the Infant
- **Contesto citazione**: Le sintonizzazioni affettive e il sé emergente; le rotture delle aspettative di coerenza nello sviluppo.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### The Neurobehavioral and Social-Emotional Development of Infants and Children
- **ID**: `tronick-neurobehavioral-development`
- **Autore**: Edward Tronick
- **Anno**: 2007
- **Genere**: Psicologia dello sviluppo
- **Assi**: Asse 5
- **Contesto citazione**: Le rotture non riparate nella co-regolazione; il paradigma Still Face come evidenza delle interruzioni nella sintonizzazione.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

---

## Output del giorno — da compilare

Al termine, salvare il file `rilevanza-giorno-2.json` in `output/assi-strutturali/` con questa struttura:

```json
{
  "giorno": 2,
  "autori": [
    { "id": "melanie-klein", "nome": "Melanie Klein", "rilevanza": "..." },
    { "id": "sigmund-freud", "nome": "Sigmund Freud", "rilevanza": "..." },
    { "id": "wilfred-bion", "nome": "Wilfred R. Bion", "rilevanza": "..." },
    { "id": "paul-ricoeur", "nome": "Paul Ricoeur", "rilevanza": "..." },
    { "id": "emmanuel-levinas", "nome": "Emmanuel Levinas", "rilevanza": "..." },
    { "id": "jean-piaget", "nome": "Jean Piaget", "rilevanza": "..." },
    { "id": "lawrence-kohlberg", "nome": "Lawrence Kohlberg", "rilevanza": "..." },
    { "id": "colwyn-trevarthen", "nome": "Colwyn Trevarthen", "rilevanza": "..." },
    { "id": "daniel-stern", "nome": "Daniel Stern", "rilevanza": "..." },
  ],
  "libri": [
    { "id": "winnicott-maturational-processes", "titolo": "The Maturational Processes and the Facilitating En", "rilevanza": "..." },
    { "id": "winnicott-capacity-for-concern", "titolo": "The Capacity for Concern", "rilevanza": "..." },
    { "id": "winnicott-use-of-an-object", "titolo": "The Use of an Object", "rilevanza": "..." },
    { "id": "klein-envy-and-gratitude", "titolo": "Envy and Gratitude", "rilevanza": "..." },
    { "id": "freud-io-e-es", "titolo": "L'Io e l'Es", "rilevanza": "..." },
    { "id": "bion-learning-from-experience", "titolo": "Learning from Experience", "rilevanza": "..." },
    { "id": "merleau-ponty-il-visibile-e-linvisibile", "titolo": "Il visibile e l'invisibile", "rilevanza": "..." },
    { "id": "levinas-totalita-e-infinito", "titolo": "Totalità e infinito", "rilevanza": "..." },
    { "id": "levinas-altrimenti-che-essere", "titolo": "Altrimenti che essere, o al di là dell'essenza", "rilevanza": "..." },
    { "id": "trevarthen-communication-cooperation", "titolo": "Communication and Cooperation in Early Infancy", "rilevanza": "..." },
    { "id": "stern-mondo-interpersonale-del-bambino", "titolo": "Il mondo interpersonale del bambino", "rilevanza": "..." },
    { "id": "tronick-neurobehavioral-development", "titolo": "The Neurobehavioral and Social-Emotional Developme", "rilevanza": "..." },
  ]
}
```
