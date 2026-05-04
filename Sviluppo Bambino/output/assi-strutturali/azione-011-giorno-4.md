---
id: azione-011-giorno-4
azione: 011
giorno: 4 di 5
stato: completato
autori_da_trattare: 9
libri_da_trattare: 13
---

# Azione 011 — Giorno 4: Assi 4 e 5 — Limite, perdita, desiderio (9 autori, 13 libri)

## Contesto dell'azione

Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** del progetto Sviluppo Bambino (HCAIRE).

**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione degli assi strutturali, produrre un testo che spiega perché quel pensatore / quel testo è rilevante per il progetto Sviluppo Bambino.

**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-4.json` nel formato descritto nelle linee guida sotto. Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà i file JSON giornalieri in `autori.json` e `bibliografia.json`.

---

## Focus di oggi

**Assi 4 e 5 — Separazione/Limite e Desiderio**

Asse 4: pensatori dell'incontro con il reale, la perdita, la separazione — Basaglia sulla crisi dell'istituzione, Han sulla società performativa, Plessner e Mead sull'eccentricità del soggetto. Asse 5: i filosofi del desiderio — Platone e Aristotele fondano la tradizione; Kant introduce il dovere; Sen, Bourdieu e Jonas completano il quadro della soggettività orientata.

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

### Franco Basaglia
- **ID**: `franco-basaglia`
- **Disciplina**: Psichiatria critica
- **Periodo**: 1924–1980
- **Nazionalità**: Italiana
- **Assi**: Asse 4
- **Note**: Psichiatra e riformatore. Citato per la critica alla patologizzazione e alla medicalizzazione dell'esperienza umana.

### Byung-Chul Han
- **ID**: `byung-chul-han`
- **Disciplina**: Filosofia
- **Periodo**: 1959–
- **Nazionalità**: Coreana / tedesca
- **Assi**: Asse 4, Asse 5, Asse 6
- **Note**: Filosofo contemporaneo. Critico della «società della prestazione» e dell'auto-ottimizzazione come sostituto della normatività.

### Axel Honneth
- **ID**: `axel-honneth`
- **Disciplina**: Filosofia sociale
- **Periodo**: 1949–
- **Nazionalità**: Tedesca
- **Assi**: Asse 6
- **Note**: Filosofo della Scuola di Francoforte. Teorico del riconoscimento come dinamica strutturale del conflitto sociale.

### Platone
- **ID**: `platone`
- **Disciplina**: Filosofia
- **Periodo**: 427–347 a.C.
- **Nazionalità**: Greca
- **Assi**: Asse 5
- **Note**: Filosofo greco. Citato per il concetto di érōs come desiderio strutturale della mancanza (Simposio) e per la filosofia politica (Repubblica).

### Aristotele
- **ID**: `aristotele`
- **Disciplina**: Filosofia
- **Periodo**: 384–322 a.C.
- **Nazionalità**: Greca
- **Assi**: Asse 5
- **Note**: Filosofo greco. Citato per il concetto di phronesis (saggezza pratica) e la deliberazione orientata dal fine desiderato.

### Immanuel Kant
- **ID**: `immanuel-kant`
- **Disciplina**: Filosofia
- **Periodo**: 1724–1804
- **Nazionalità**: Tedesca / prussiana
- **Assi**: Asse 5
- **Note**: Filosofo critico. Citato come contro-modello: una normatività fondata sull'autonomia della ragione, non sul desiderio.

### Amartya Sen
- **ID**: `amartya-sen`
- **Disciplina**: Economia, filosofia politica
- **Periodo**: 1933–
- **Nazionalità**: Indiana
- **Assi**: Asse 5
- **Note**: Premio Nobel per l'economia. Citato per il concetto di «capabilities» (capacità fondamentali).

### Pierre Bourdieu
- **ID**: `pierre-bourdieu`
- **Disciplina**: Sociologia
- **Periodo**: 1930–2002
- **Nazionalità**: Francese
- **Assi**: Asse 5
- **Note**: Sociologo. Citato per i concetti di habitus e campo come strutture sociali dell'esperienza.

### Edward Tronick
- **ID**: `edward-tronick`
- **Disciplina**: Psicologia dello sviluppo
- **Periodo**: 1942–
- **Nazionalità**: Statunitense
- **Assi**: Asse 5
- **Note**: Psicologo dello sviluppo. Teorico del paradigma «Still Face» e delle rotture e riparazioni nella co-regolazione.

---

## Libri da trattare oggi (13)

### Lutto e melanconia
- **ID**: `freud-lutto-e-melanconia`
- **Autore**: Sigmund Freud
- **Anno**: 1917
- **Genere**: Psicoanalisi
- **Assi**: Asse 4
- **Titolo originale**: Trauer und Melancholie
- **Contesto citazione**: Il reale non è riducibile a dinamica regolativa; il lutto come lavoro non immediato.

### L'istituzione negata
- **ID**: `basaglia-l-istituzione-negata`
- **Autore**: Franco Basaglia
- **Anno**: 1968
- **Genere**: Psichiatria critica
- **Assi**: Asse 4
- **Contesto citazione**: La critica alla patologizzazione dell'esperienza umana e alla medicalizzazione del non simbolizzato.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### La società della stanchezza
- **ID**: `han-societa-della-stanchezza`
- **Autore**: Byung-Chul Han
- **Anno**: 2010
- **Genere**: Filosofia contemporanea
- **Assi**: Asse 6
- **Titolo originale**: Müdigkeitsgesellschaft
- **Contesto citazione**: La società della performance sostituisce il dovere con l'auto-ottimizzazione.

### Simposio
- **ID**: `platone-simposio`
- **Autore**: Platone
- **Anno**: 385–370 a.C.
- **Genere**: Filosofia classica
- **Assi**: Asse 5
- **Titolo originale**: Συμπόσιον
- **Contesto citazione**: Érōs come desiderio di ciò che non si possiede; desiderio come mancanza strutturale.

### Repubblica
- **ID**: `platone-repubblica`
- **Autore**: Platone
- **Anno**: 380 a.C.
- **Genere**: Filosofia classica
- **Assi**: Asse 5
- **Titolo originale**: Πολιτεία
- **Contesto citazione**: Citato insieme al Simposio per il concetto di desiderio.

### Etica Nicomachea
- **ID**: `aristotele-etica-nicomachea`
- **Autore**: Aristotele
- **Anno**: 350 a.C.
- **Genere**: Filosofia morale
- **Assi**: Asse 5
- **Titolo originale**: Ἠθικὰ Νικομάχεια
- **Contesto citazione**: La deliberazione che nasce dal desiderio razionale (orexis logiké); la phronesis.

### Critica della ragion pratica
- **ID**: `kant-critica-della-ragion-pratica`
- **Autore**: Immanuel Kant
- **Anno**: 1788
- **Genere**: Filosofia morale
- **Assi**: Asse 5
- **Titolo originale**: Kritik der praktischen Vernunft
- **Contesto citazione**: Usato come contro-modello: una normatività fondata sull'autonomia della ragione pura, non sul desiderio.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Fondazione della metafisica dei costumi
- **ID**: `kant-fondazione-metafisica-costumi`
- **Autore**: Immanuel Kant
- **Anno**: 1785
- **Genere**: Filosofia morale
- **Assi**: Asse 5
- **Titolo originale**: Grundlegung zur Metaphysik der Sitten
- **Contesto citazione**: L'imperativo categorico come archetipo di normatività razionale: punto di distanza esplicita del modello degli assi.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Ideen II
- **ID**: `husserl-ideen-ii`
- **Autore**: Edmund Husserl
- **Anno**: 1952
- **Genere**: Fenomenologia
- **Assi**: Asse 5
- **Titolo originale**: Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie, Zweites Buch
- **Contesto citazione**: Ogni coscienza è sempre coscienza di qualcosa (principio dell'intenzionalità).

### Lo sviluppo è libertà
- **ID**: `sen-lo-sviluppo-e-liberta`
- **Autore**: Amartya Sen
- **Anno**: 1999
- **Genere**: Economia, filosofia politica
- **Assi**: Asse 5
- **Titolo originale**: Development as Freedom
- **Contesto citazione**: Il concetto di capabilities (capacità fondamentali) come misura della libertà reale.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Il senso pratico
- **ID**: `bourdieu-il-senso-pratico`
- **Autore**: Pierre Bourdieu
- **Anno**: 1980
- **Genere**: Sociologia
- **Assi**: Asse 5
- **Titolo originale**: Le sens pratique
- **Contesto citazione**: Il concetto di habitus come struttura incorporata che orienta le pratiche senza essere esplicitamente cosciente.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Ragioni pratiche
- **ID**: `bourdieu-ragioni-pratiche`
- **Autore**: Pierre Bourdieu
- **Anno**: 1994
- **Genere**: Sociologia
- **Assi**: Asse 5
- **Titolo originale**: Raisons pratiques
- **Contesto citazione**: Il campo come struttura di posizioni relative che organizza l'esperienza sociale.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

### Il principio responsabilità
- **ID**: `jonas-il-principio-responsabilita`
- **Autore**: Hans Jonas
- **Anno**: 1979
- **Genere**: Etica della responsabilità
- **Assi**: Asse 5, Asse 6
- **Titolo originale**: Das Prinzip Verantwortung
- **Contesto citazione**: L'apertura dell'organismo al futuro; la tecnica promette dominio ma genera vulnerabilità.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

---

## Output del giorno — da compilare

Al termine, salvare il file `rilevanza-giorno-4.json` in `output/assi-strutturali/` con questa struttura:

```json
{
  "giorno": 4,
  "autori": [
    { "id": "franco-basaglia", "nome": "Franco Basaglia", "rilevanza": "..." },
    { "id": "byung-chul-han", "nome": "Byung-Chul Han", "rilevanza": "..." },
    { "id": "axel-honneth", "nome": "Axel Honneth", "rilevanza": "..." },
    { "id": "platone", "nome": "Platone", "rilevanza": "..." },
    { "id": "aristotele", "nome": "Aristotele", "rilevanza": "..." },
    { "id": "immanuel-kant", "nome": "Immanuel Kant", "rilevanza": "..." },
    { "id": "amartya-sen", "nome": "Amartya Sen", "rilevanza": "..." },
    { "id": "pierre-bourdieu", "nome": "Pierre Bourdieu", "rilevanza": "..." },
    { "id": "edward-tronick", "nome": "Edward Tronick", "rilevanza": "..." },
  ],
  "libri": [
    { "id": "freud-lutto-e-melanconia", "titolo": "Lutto e melanconia", "rilevanza": "..." },
    { "id": "basaglia-l-istituzione-negata", "titolo": "L'istituzione negata", "rilevanza": "..." },
    { "id": "han-societa-della-stanchezza", "titolo": "La società della stanchezza", "rilevanza": "..." },
    { "id": "platone-simposio", "titolo": "Simposio", "rilevanza": "..." },
    { "id": "platone-repubblica", "titolo": "Repubblica", "rilevanza": "..." },
    { "id": "aristotele-etica-nicomachea", "titolo": "Etica Nicomachea", "rilevanza": "..." },
    { "id": "kant-critica-della-ragion-pratica", "titolo": "Critica della ragion pratica", "rilevanza": "..." },
    { "id": "kant-fondazione-metafisica-costumi", "titolo": "Fondazione della metafisica dei costumi", "rilevanza": "..." },
    { "id": "husserl-ideen-ii", "titolo": "Ideen II", "rilevanza": "..." },
    { "id": "sen-lo-sviluppo-e-liberta", "titolo": "Lo sviluppo è libertà", "rilevanza": "..." },
    { "id": "bourdieu-il-senso-pratico", "titolo": "Il senso pratico", "rilevanza": "..." },
    { "id": "bourdieu-ragioni-pratiche", "titolo": "Ragioni pratiche", "rilevanza": "..." },
    { "id": "jonas-il-principio-responsabilita", "titolo": "Il principio responsabilità", "rilevanza": "..." },
  ]
}
```
