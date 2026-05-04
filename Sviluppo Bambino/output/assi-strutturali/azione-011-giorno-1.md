---
id: azione-011-giorno-1
azione: 011
giorno: 1 di 5
stato: completato
autori_da_trattare: 9
libri_da_trattare: 8
---

# Azione 011 — Giorno 1: Asse 1 — Fenomenologia, corpo, conoscenza biologica (9 autori, 8 libri)

## Contesto dell'azione

Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** del progetto Sviluppo Bambino (HCAIRE).

**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione degli assi strutturali, produrre un testo che spiega perché quel pensatore / quel testo è rilevante per il progetto Sviluppo Bambino.

**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-1.json` nel formato descritto nelle linee guida sotto. Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà i file JSON giornalieri in `autori.json` e `bibliografia.json`.

---

## Focus di oggi

**Asse 1 — Ontologico-fenomenologico**

I pensatori che fondano la comprensione del soggetto come corpo vissuto, intenzionalità, temporalità. Merleau-Ponty e Husserl sono il cuore dell'asse; Heidegger e Gadamer aprono verso l'essere-nel-mondo e l'ermeneutica; Goldstein e Canguilhem forniscono il fondamento biologico-normativo; Bowlby e Winnicott portano la prospettiva dello sviluppo relazionale precoce.

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

### Edmund Husserl
- **ID**: `edmund-husserl`
- **Disciplina**: Fenomenologia
- **Periodo**: 1859–1938
- **Nazionalità**: Tedesca / moravo-ceca
- **Assi**: Asse 1, Asse 5
- **Note**: Fondatore della fenomenologia. Citato per i concetti di costituzione trascendentale, intenzionalità, mondo della vita (Lebenswelt) e sintesi passiva.

### Maurice Merleau-Ponty
- **ID**: `maurice-merleau-ponty`
- **Disciplina**: Fenomenologia
- **Periodo**: 1908–1961
- **Nazionalità**: Francese
- **Assi**: Asse 1, Asse 2, Asse 3, Asse 4, Asse 5, Asse 6
- **Note**: Filosofo fenomenologo. Autore più citato del progetto. Fondamentale per i concetti di corporeità, soggettività incarnata, campo intenzionale, temporalità vissuta e relazione come condizione strutturale.

### Martin Heidegger
- **ID**: `martin-heidegger`
- **Disciplina**: Fenomenologia, ontologia
- **Periodo**: 1889–1976
- **Nazionalità**: Tedesca
- **Assi**: Asse 1, Asse 4, Asse 5
- **Note**: Filosofo. Citato per l'ontologia come analitica dell'esistenza (Essere e tempo) e per il concetto di Stimmung (tonalità emotiva fondamentale).

### Hans-Georg Gadamer
- **ID**: `hans-georg-gadamer`
- **Disciplina**: Ermeneutica
- **Periodo**: 1900–2002
- **Nazionalità**: Tedesca
- **Assi**: Asse 1, Asse 4, Asse 5, Asse 6
- **Note**: Filosofo ermeneutico. Citato per la «fusione di orizzonti» (Horizontverschmelzung), il pregiudizio come condizione della comprensione e il posizionamento del lettore.

### Kurt Goldstein
- **ID**: `kurt-goldstein`
- **Disciplina**: Neurologia, filosofia della biologia
- **Periodo**: 1878–1965
- **Nazionalità**: Tedesco / statunitense
- **Assi**: Asse 1
- **Note**: Neurologo e filosofo. Teorico dell'organismo come totalità autoreferente; la regolazione efficace sostiene la possibilità senza disorganizzazione.

### Georges Canguilhem
- **ID**: `georges-canguilhem`
- **Disciplina**: Filosofia della scienza, epistemologia
- **Periodo**: 1904–1995
- **Nazionalità**: Francese
- **Assi**: Asse 1
- **Note**: Filosofo ed epistemologo. Citato per la distinzione tra descrizione strutturale, spiegazione causale e prescrizione normativa, e per la regolazione come principio strutturale.

### John Bowlby
- **ID**: `john-bowlby`
- **Disciplina**: Psicoanalisi, psicologia dello sviluppo
- **Periodo**: 1907–1990
- **Nazionalità**: Britannica
- **Assi**: Asse 1
- **Note**: Psichiatra e psicoanalista. Teorico dell'attaccamento. Citato per la co-regolazione come condizione ontologica originaria.

### Donald W. Winnicott
- **ID**: `donald-winnicott`
- **Disciplina**: Psicoanalisi, pediatria
- **Periodo**: 1896–1971
- **Nazionalità**: Britannica
- **Assi**: Asse 1, Asse 2, Asse 4, Asse 5
- **Note**: Pediatra e psicoanalista. Teorico dello spazio transizionale, della «capacità di preoccuparsi» (capacity for concern), dell'holding e del vero/falso sé.

### Michel Foucault
- **ID**: `michel-foucault`
- **Disciplina**: Filosofia, storia delle idee
- **Periodo**: 1926–1984
- **Nazionalità**: Francese
- **Assi**: Asse 1, Asse 3, Asse 4, Asse 6
- **Note**: Filosofo e storico delle idee. Citato per l'analisi delle istituzioni come dispositivi di potere e disciplina. Usato come contro-campo critico.

---

## Libri da trattare oggi (8)

### Fenomenologia della percezione
- **ID**: `merleau-ponty-fenomenologia-della-percezione`
- **Autore**: Maurice Merleau-Ponty
- **Anno**: 1945
- **Genere**: Fenomenologia
- **Assi**: Asse 1, Asse 3, Asse 5, Asse 6
- **Titolo originale**: Phénoménologie de la perception
- **Contesto citazione**: Fondamento principale per il concetto di corporeità, temporalità vissuta, soggetto incarnato e campo intenzionale.

### Lezioni sulla coscienza interna del tempo
- **ID**: `husserl-lezioni-sulla-coscienza-interna-del-tempo`
- **Autore**: Edmund Husserl
- **Anno**: 1928
- **Genere**: Fenomenologia
- **Assi**: Asse 1
- **Titolo originale**: Vorlesungen zur Phänomenologie des inneren Zeitbewusstseins
- **Contesto citazione**: La struttura della temporalità vissuta come unità dell'esperienza.

### Essere e tempo
- **ID**: `heidegger-essere-e-tempo`
- **Autore**: Martin Heidegger
- **Anno**: 1927
- **Genere**: Ontologia fenomenologica
- **Assi**: Asse 1, Asse 4
- **Titolo originale**: Sein und Zeit
- **Contesto citazione**: Ontologia come analitica dell'esistenza; il mondo non è mai completamente «a disposizione».

### Attaccamento e perdita
- **ID**: `bowlby-attaccamento-e-perdita`
- **Autore**: John Bowlby
- **Anno**: 1969–1980
- **Genere**: Psicoanalisi dello sviluppo
- **Assi**: Asse 1
- **Titolo originale**: Attachment and Loss
- **Contesto citazione**: Co-regolazione come condizione ontologica originaria.

### Il normale e il patologico
- **ID**: `canguilhem-normale-e-patologico`
- **Autore**: Georges Canguilhem
- **Anno**: 1966
- **Genere**: Filosofia della biologia
- **Assi**: Asse 1
- **Titolo originale**: Le normal et le pathologique
- **Contesto citazione**: La regolazione intesa come principio strutturale dell'esperienza, non come funzione psicologica isolabile.

### La struttura dell'organismo
- **ID**: `goldstein-struttura-dellorganismo`
- **Autore**: Kurt Goldstein
- **Anno**: 1934
- **Genere**: Neurologia, filosofia della biologia
- **Assi**: Asse 1
- **Titolo originale**: Der Aufbau des Organismus
- **Contesto citazione**: La regolazione efficace sostiene la possibilità senza disorganizzazione.

### Sorvegliare e punire
- **ID**: `foucault-sorvegliare-e-punire`
- **Autore**: Michel Foucault
- **Anno**: 1975
- **Genere**: Filosofia / storia delle istituzioni
- **Assi**: Asse 1, Asse 3, Asse 6
- **Titolo originale**: Surveiller et punir
- **Contesto citazione**: Distinzione tra regolazione e controllo normativo; le istituzioni disciplinari organizzano il tempo e il corpo.

### Gioco e realtà
- **ID**: `winnicott-gioco-e-realta`
- **Autore**: Donald W. Winnicott
- **Anno**: 1971
- **Genere**: Psicoanalisi dello sviluppo
- **Assi**: Asse 1
- **Titolo originale**: Playing and Reality
- **Contesto citazione**: Co-regolazione come condizione ontologica originaria.

---

## Output del giorno — da compilare

Al termine, salvare il file `rilevanza-giorno-1.json` in `output/assi-strutturali/` con questa struttura:

```json
{
  "giorno": 1,
  "autori": [
    { "id": "edmund-husserl", "nome": "Edmund Husserl", "rilevanza": "..." },
    { "id": "maurice-merleau-ponty", "nome": "Maurice Merleau-Ponty", "rilevanza": "..." },
    { "id": "martin-heidegger", "nome": "Martin Heidegger", "rilevanza": "..." },
    { "id": "hans-georg-gadamer", "nome": "Hans-Georg Gadamer", "rilevanza": "..." },
    { "id": "kurt-goldstein", "nome": "Kurt Goldstein", "rilevanza": "..." },
    { "id": "georges-canguilhem", "nome": "Georges Canguilhem", "rilevanza": "..." },
    { "id": "john-bowlby", "nome": "John Bowlby", "rilevanza": "..." },
    { "id": "donald-winnicott", "nome": "Donald W. Winnicott", "rilevanza": "..." },
    { "id": "michel-foucault", "nome": "Michel Foucault", "rilevanza": "..." },
  ],
  "libri": [
    { "id": "merleau-ponty-fenomenologia-della-percezione", "titolo": "Fenomenologia della percezione", "rilevanza": "..." },
    { "id": "husserl-lezioni-sulla-coscienza-interna-del-tempo", "titolo": "Lezioni sulla coscienza interna del tempo", "rilevanza": "..." },
    { "id": "heidegger-essere-e-tempo", "titolo": "Essere e tempo", "rilevanza": "..." },
    { "id": "bowlby-attaccamento-e-perdita", "titolo": "Attaccamento e perdita", "rilevanza": "..." },
    { "id": "canguilhem-normale-e-patologico", "titolo": "Il normale e il patologico", "rilevanza": "..." },
    { "id": "goldstein-struttura-dellorganismo", "titolo": "La struttura dell'organismo", "rilevanza": "..." },
    { "id": "foucault-sorvegliare-e-punire", "titolo": "Sorvegliare e punire", "rilevanza": "..." },
    { "id": "winnicott-gioco-e-realta", "titolo": "Gioco e realtà", "rilevanza": "..." },
  ]
}
```
