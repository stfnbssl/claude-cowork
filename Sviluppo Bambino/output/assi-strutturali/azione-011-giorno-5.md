---
id: azione-011-giorno-5
azione: 011
giorno: 5 di 5
stato: completato
autori_da_trattare: 9
libri_da_trattare: 15
---

# Azione 011 — Giorno 5: Asse 6 — Storico-culturale, linguaggio, istituzioni (9 autori, 15 libri)

## Contesto dell'azione

Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** del progetto Sviluppo Bambino (HCAIRE).

**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione degli assi strutturali, produrre un testo che spiega perché quel pensatore / quel testo è rilevante per il progetto Sviluppo Bambino.

**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-5.json` nel formato descritto nelle linee guida sotto. Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà i file JSON giornalieri in `autori.json` e `bibliografia.json`.

---

## Focus di oggi

**Asse 6 — Storico-culturale**

I pensatori della mediazione culturale, del linguaggio, delle istituzioni. Vygotskij e Bruner forniscono il fondamento psico-culturale; Dilthey e Humboldt apportano la tradizione delle scienze dello spirito e del linguaggio; Rosa, Han e Illich portano la critica della modernità; Schutz e Honneth completano il quadro sociologico-fenomenologico.

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

### Lev Semënovič Vygotskij
- **ID**: `lev-vygotskij`
- **Disciplina**: Psicologia dello sviluppo
- **Periodo**: 1896–1934
- **Nazionalità**: Russa / bielorussa
- **Assi**: Asse 5, Asse 6
- **Note**: Psicologo dello sviluppo. Teorico della mediazione simbolica come struttura antropologica e della zona di sviluppo prossimale.

### Jerome Bruner
- **ID**: `jerome-bruner`
- **Disciplina**: Psicologia culturale, psicologia dell'educazione
- **Periodo**: 1915–2016
- **Nazionalità**: Statunitense
- **Assi**: Asse 4, Asse 6
- **Note**: Psicologo culturale. Teorico della mente come culturalmente modellata attraverso narrazioni; citato per lo sviluppo come trasformazione di forme.

### Arnold Gehlen
- **ID**: `arnold-gehlen`
- **Disciplina**: Antropologia filosofica
- **Periodo**: 1904–1976
- **Nazionalità**: Tedesca
- **Assi**: Asse 6
- **Note**: Antropologo filosofico. Citato per l'idea che le istituzioni stabilizzano l'esistenza umana, riducendo l'eccesso di possibilità.

### Alfred Schutz
- **ID**: `alfred-schutz`
- **Disciplina**: Fenomenologia sociale
- **Periodo**: 1899–1959
- **Nazionalità**: Austriaca
- **Assi**: Asse 6
- **Note**: Sociologo e fenomenologo. Teorico del «mondo della vita quotidiana» come struttura già data prima di ogni atto teorico.

### Wilhelm Dilthey
- **ID**: `wilhelm-dilthey`
- **Disciplina**: Filosofia dello spirito, ermeneutica
- **Periodo**: 1833–1911
- **Nazionalità**: Tedesca
- **Assi**: Asse 6
- **Note**: Filosofo delle scienze dello spirito. Citato per l'idea che «la vita si comprende solo a partire dalla vita» e per la distinzione tra scienze naturali e scienze dello spirito.

### Wilhelm von Humboldt
- **ID**: `wilhelm-von-humboldt`
- **Disciplina**: Filosofia del linguaggio, linguistica
- **Periodo**: 1767–1835
- **Nazionalità**: Tedesca / prussiana
- **Assi**: Asse 6
- **Note**: Filosofo e linguista. Citato per l'idea che il linguaggio non è strumento ma «attività formativa del pensiero».

### Hartmut Rosa
- **ID**: `hartmut-rosa`
- **Disciplina**: Sociologia critica
- **Periodo**: 1965–
- **Nazionalità**: Tedesca
- **Assi**: Asse 6
- **Note**: Sociologo critico. Teorico dell'accelerazione sociale e della sua influenza sul rapporto con il tempo, il desiderio e l'esperienza.

### Ivan Illich
- **ID**: `ivan-illich`
- **Disciplina**: Filosofia critica dell'educazione
- **Periodo**: 1926–2002
- **Nazionalità**: Austro-croata
- **Assi**: Asse 6
- **Note**: Filosofo e critico sociale. Citato per la critica alle istituzioni educative formali.

### Hans Jonas
- **ID**: `hans-jonas`
- **Disciplina**: Filosofia, etica della responsabilità
- **Periodo**: 1903–1993
- **Nazionalità**: Tedesco / statunitense
- **Assi**: Asse 5, Asse 6
- **Note**: Filosofo della responsabilità. Citato per l'apertura dell'organismo al futuro e per l'idea che la tecnica genera vulnerabilità.

---

## Libri da trattare oggi (15)

### Pensiero e linguaggio
- **ID**: `vygotskij-pensiero-e-linguaggio`
- **Autore**: Lev Semënovič Vygotskij
- **Anno**: 1934
- **Genere**: Psicologia dello sviluppo
- **Assi**: Asse 6
- **Titolo originale**: Мышление и речь
- **Contesto citazione**: La mediazione simbolica come struttura antropologica.

### Lo sviluppo delle funzioni psichiche superiori
- **ID**: `vygotskij-sviluppo-funzioni-psichiche`
- **Autore**: Lev Semënovič Vygotskij
- **Anno**: 1931
- **Genere**: Psicologia dello sviluppo
- **Assi**: Asse 6
- **Titolo originale**: История развития высших психических функций
- **Contesto citazione**: Ogni funzione psichica superiore appare prima tra le persone, poi dentro la persona.

### Acts of Meaning
- **ID**: `bruner-acts-of-meaning`
- **Autore**: Jerome Bruner
- **Anno**: 1990
- **Genere**: Psicologia culturale
- **Assi**: Asse 6
- **Contesto citazione**: La mente è culturalmente modellata attraverso narrazioni.

### La cultura dell'educazione
- **ID**: `bruner-cultura-dell-educazione`
- **Autore**: Jerome Bruner
- **Anno**: 1996
- **Genere**: Psicologia culturale
- **Assi**: Asse 6
- **Titolo originale**: The Culture of Education
- **Contesto citazione**: Viviamo in un mondo interpretato narrativamente.

### Il problema della realtà sociale
- **ID**: `schutz-sinnhafte-aufbau`
- **Autore**: Alfred Schutz
- **Anno**: 1932
- **Genere**: Fenomenologia sociale
- **Assi**: Asse 6
- **Titolo originale**: Der sinnhafte Aufbau der sozialen Welt
- **Contesto citazione**: Il mondo della vita quotidiana è dato come già strutturato prima di ogni atto teorico.

### Lotta per il riconoscimento
- **ID**: `honneth-lotta-per-il-riconoscimento`
- **Autore**: Axel Honneth
- **Anno**: 1992
- **Genere**: Filosofia sociale
- **Assi**: Asse 6
- **Titolo originale**: Kampf um Anerkennung
- **Contesto citazione**: Il conflitto come dinamica strutturale del riconoscimento.

### Introduzione alle scienze dello spirito
- **ID**: `dilthey-introduzione-scienze-spirito`
- **Autore**: Wilhelm Dilthey
- **Anno**: 1883
- **Genere**: Filosofia dello spirito
- **Assi**: Asse 6
- **Titolo originale**: Einleitung in die Geisteswissenschaften
- **Contesto citazione**: La vita si comprende solo a partire dalla vita.

### La costruzione del mondo storico nelle scienze dello spirito
- **ID**: `dilthey-costruzione-mondo-storico`
- **Autore**: Wilhelm Dilthey
- **Anno**: 1910
- **Genere**: Filosofia dello spirito
- **Assi**: Asse 6
- **Titolo originale**: Der Aufbau der geschichtlichen Welt in den Geisteswissenschaften
- **Contesto citazione**: Il soggetto storicamente costituito.

### Accelerazione e alienazione
- **ID**: `rosa-accelerazione-e-alienazione`
- **Autore**: Hartmut Rosa
- **Anno**: 2010
- **Genere**: Sociologia critica
- **Assi**: Asse 6
- **Titolo originale**: Alienation and Acceleration
- **Contesto citazione**: L'accelerazione ristruttura l'esperienza del tempo e rischia la saturazione del desiderio.

### Descolarizzare la società
- **ID**: `illich-deschooling-society`
- **Autore**: Ivan Illich
- **Anno**: 1971
- **Genere**: Critica dell'educazione
- **Assi**: Asse 6
- **Titolo originale**: Deschooling Society
- **Contesto citazione**: Critica alle istituzioni educative formali.

### L'uomo. La sua natura e il suo posto nel mondo
- **ID**: `gehlen-l-uomo`
- **Autore**: Arnold Gehlen
- **Anno**: 1940
- **Genere**: Antropologia filosofica
- **Assi**: Asse 6
- **Titolo originale**: Der Mensch. Seine Natur und seine Stellung in der Welt
- **Contesto citazione**: L'essere umano come «essere manchevole» (Mängelwesen): le istituzioni compensano l'incompletezza biologica e stabilizzano l'esistenza.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### La diversità delle lingue
- **ID**: `humboldt-diversita-delle-lingue`
- **Autore**: Wilhelm von Humboldt
- **Anno**: 1836
- **Genere**: Filosofia del linguaggio
- **Assi**: Asse 6
- **Titolo originale**: Über die Verschiedenheit des menschlichen Sprachbaues
- **Contesto citazione**: Il linguaggio non è strumento ma «attività formativa del pensiero» (ergon vs energeia).
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Tempo e racconto
- **ID**: `ricoeur-tempo-e-racconto`
- **Autore**: Paul Ricoeur
- **Anno**: 1983–1985
- **Genere**: Ermeneutica, filosofia della narrazione
- **Assi**: Asse 6
- **Titolo originale**: Temps et récit
- **Contesto citazione**: Legame tra narrazione, temporalità e identità.

### La prosa del mondo
- **ID**: `merleau-ponty-la-prosa-del-mondo`
- **Autore**: Maurice Merleau-Ponty
- **Anno**: 1969
- **Genere**: Filosofia del linguaggio
- **Assi**: Asse 6
- **Titolo originale**: La prose du monde
- **Contesto citazione**: Il linguaggio non traduce il pensiero: lo realizza.

### Institution et passivité
- **ID**: `merleau-ponty-institution-et-passivite`
- **Autore**: Maurice Merleau-Ponty
- **Anno**: 2003
- **Genere**: Fenomenologia delle istituzioni
- **Assi**: Asse 6
- **Titolo originale**: Institution et passivité (cours au Collège de France)
- **Contesto citazione**: L'istituzione non è un apparato, ma un evento che stabilizza senso nel tempo.

---

## Output del giorno — da compilare

Al termine, salvare il file `rilevanza-giorno-5.json` in `output/assi-strutturali/` con questa struttura:

```json
{
  "giorno": 5,
  "autori": [
    { "id": "lev-vygotskij", "nome": "Lev Semënovič Vygotskij", "rilevanza": "..." },
    { "id": "jerome-bruner", "nome": "Jerome Bruner", "rilevanza": "..." },
    { "id": "arnold-gehlen", "nome": "Arnold Gehlen", "rilevanza": "..." },
    { "id": "alfred-schutz", "nome": "Alfred Schutz", "rilevanza": "..." },
    { "id": "wilhelm-dilthey", "nome": "Wilhelm Dilthey", "rilevanza": "..." },
    { "id": "wilhelm-von-humboldt", "nome": "Wilhelm von Humboldt", "rilevanza": "..." },
    { "id": "hartmut-rosa", "nome": "Hartmut Rosa", "rilevanza": "..." },
    { "id": "ivan-illich", "nome": "Ivan Illich", "rilevanza": "..." },
    { "id": "hans-jonas", "nome": "Hans Jonas", "rilevanza": "..." },
  ],
  "libri": [
    { "id": "vygotskij-pensiero-e-linguaggio", "titolo": "Pensiero e linguaggio", "rilevanza": "..." },
    { "id": "vygotskij-sviluppo-funzioni-psichiche", "titolo": "Lo sviluppo delle funzioni psichiche superiori", "rilevanza": "..." },
    { "id": "bruner-acts-of-meaning", "titolo": "Acts of Meaning", "rilevanza": "..." },
    { "id": "bruner-cultura-dell-educazione", "titolo": "La cultura dell'educazione", "rilevanza": "..." },
    { "id": "schutz-sinnhafte-aufbau", "titolo": "Il problema della realtà sociale", "rilevanza": "..." },
    { "id": "honneth-lotta-per-il-riconoscimento", "titolo": "Lotta per il riconoscimento", "rilevanza": "..." },
    { "id": "dilthey-introduzione-scienze-spirito", "titolo": "Introduzione alle scienze dello spirito", "rilevanza": "..." },
    { "id": "dilthey-costruzione-mondo-storico", "titolo": "La costruzione del mondo storico nelle scienze del", "rilevanza": "..." },
    { "id": "rosa-accelerazione-e-alienazione", "titolo": "Accelerazione e alienazione", "rilevanza": "..." },
    { "id": "illich-deschooling-society", "titolo": "Descolarizzare la società", "rilevanza": "..." },
    { "id": "gehlen-l-uomo", "titolo": "L'uomo. La sua natura e il suo posto nel mondo", "rilevanza": "..." },
    { "id": "humboldt-diversita-delle-lingue", "titolo": "La diversità delle lingue", "rilevanza": "..." },
    { "id": "ricoeur-tempo-e-racconto", "titolo": "Tempo e racconto", "rilevanza": "..." },
    { "id": "merleau-ponty-la-prosa-del-mondo", "titolo": "La prosa del mondo", "rilevanza": "..." },
    { "id": "merleau-ponty-institution-et-passivite", "titolo": "Institution et passivité", "rilevanza": "..." },
  ]
}
```
