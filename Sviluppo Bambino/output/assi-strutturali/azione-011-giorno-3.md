---
id: azione-011-giorno-3
azione: 011
giorno: 3 di 5
stato: completato
autori_da_trattare: 8
libri_da_trattare: 15
---

# Azione 011 — Giorno 3: Asse 3 — Normatività, educazione, giudizio (8 autori, 15 libri)

## Contesto dell'azione

Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** del progetto Sviluppo Bambino (HCAIRE).

**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione degli assi strutturali, produrre un testo che spiega perché quel pensatore / quel testo è rilevante per il progetto Sviluppo Bambino.

**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-3.json` nel formato descritto nelle linee guida sotto. Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà i file JSON giornalieri in `autori.json` e `bibliografia.json`.

---

## Focus di oggi

**Asse 3 — Normativo-educativo**

I pensatori della norma, dell'educazione e del giudizio. Arendt è centrale per la distinzione tra autorità e potere; MacIntyre e Taylor fondano l'etica delle virtù e del sé narrativo; Stiegler porta la critica della tecnica come dispositivo educativo; Agostino e Tommaso rappresentano la tradizione della normatività orientata al bene.

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

## Autori da trattare oggi (8)

### Hannah Arendt
- **ID**: `hannah-arendt`
- **Disciplina**: Filosofia politica
- **Periodo**: 1906–1975
- **Nazionalità**: Tedesca / statunitense
- **Assi**: Asse 3, Asse 5, Asse 6
- **Note**: Filosofa politica. Citata per i concetti di autorità educativa, natalità, distinzione tra obbedienza e giudizio, e responsabilità del mondo.

### Alasdair MacIntyre
- **ID**: `alasdair-macintyre`
- **Disciplina**: Filosofia morale
- **Periodo**: 1929–
- **Nazionalità**: Scozzese
- **Assi**: Asse 3, Asse 5
- **Note**: Filosofo morale comunitarista. Citato come diagnosi del collasso del linguaggio normativo nella modernità.

### Charles Taylor
- **ID**: `charles-taylor`
- **Disciplina**: Filosofia morale e politica
- **Periodo**: 1931–
- **Nazionalità**: Canadese
- **Assi**: Asse 3, Asse 4, Asse 5, Asse 6
- **Note**: Filosofo comunitarista. Teorico degli «orizzonti di senso» come condizione dell'identità e della «strong evaluation».

### Bernard Stiegler
- **ID**: `bernard-stiegler`
- **Disciplina**: Filosofia della tecnica
- **Periodo**: 1952–2020
- **Nazionalità**: Francese
- **Assi**: Asse 3, Asse 6
- **Note**: Filosofo della tecnica. Teorico della tecnica come memoria esternalizzata che forma l'attenzione e il desiderio.

### Agostino d'Ippona
- **ID**: `agostino-d-ippona`
- **Disciplina**: Teologia, filosofia
- **Periodo**: 354–430
- **Nazionalità**: Nordafricana / romana
- **Assi**: Asse 3, Asse 5
- **Note**: Padre della chiesa e filosofo. Contribuisce al progetto tramite il concetto di desiderio come inquietudine strutturale e l'«ordine degli amori» (ordo amoris).

### Tommaso d'Aquino
- **ID**: `tommaso-d-aquino`
- **Disciplina**: Teologia, filosofia scolastica
- **Periodo**: 1225–1274
- **Nazionalità**: Italiana
- **Assi**: Asse 3, Asse 5
- **Note**: Teologo e filosofo. Citato per la distinzione tra atto materiale e atto formale della volontà e la riflessione sulla norma.

### Helmuth Plessner
- **ID**: `helmuth-plessner`
- **Disciplina**: Antropologia filosofica
- **Periodo**: 1892–1985
- **Nazionalità**: Tedesca
- **Assi**: Asse 4
- **Note**: Antropologo filosofico. Teorico della «posizionalità eccentrica» dell'essere umano come condizione di apertura e distanza da sé.

### George Herbert Mead
- **ID**: `george-herbert-mead`
- **Disciplina**: Filosofia sociale, psicologia sociale
- **Periodo**: 1863–1931
- **Nazionalità**: Statunitense
- **Assi**: Asse 4
- **Note**: Filosofo del pragmatismo. Teorico delle trasformazioni del sé nei contesti sociali e dell'interazionismo simbolico.

---

## Libri da trattare oggi (15)

### Sé come un altro
- **ID**: `ricoeur-se-come-un-altro`
- **Autore**: Paul Ricoeur
- **Anno**: 1990
- **Genere**: Fenomenologia, filosofia morale
- **Assi**: Asse 3, Asse 6
- **Titolo originale**: Soi-même comme un autre
- **Contesto citazione**: Imputazione a sé, responsabilità, identità narrativa come soggetto costituito ma non dissolto nella narrazione.

### Le fonti del sé
- **ID**: `taylor-fonti-del-se`
- **Autore**: Charles Taylor
- **Anno**: 1989
- **Genere**: Filosofia morale
- **Assi**: Asse 3, Asse 5, Asse 6
- **Titolo originale**: Sources of the Self
- **Contesto citazione**: Gli orizzonti di senso come condizione della valutazione; l'identità si forma in orizzonti di valore.

### Dopo la virtù
- **ID**: `macintyre-dopo-la-virtu`
- **Autore**: Alasdair MacIntyre
- **Anno**: 1981
- **Genere**: Filosofia morale
- **Assi**: Asse 3, Asse 5
- **Titolo originale**: After Virtue
- **Contesto citazione**: La frammentazione moderna dei concetti morali è un esito storico, non una necessità.

### Prendersi cura. Della gioventù e delle generazioni
- **ID**: `stiegler-prendersi-cura`
- **Autore**: Bernard Stiegler
- **Anno**: 2008
- **Genere**: Filosofia della tecnica
- **Assi**: Asse 3
- **Titolo originale**: Prendre soin. De la jeunesse et des générations
- **Contesto citazione**: La prestazione come sostituto funzionale della normatività.

### La crisi dell'educazione
- **ID**: `arendt-crisi-dell-educazione`
- **Autore**: Hannah Arendt
- **Anno**: 1958
- **Genere**: Filosofia politica, filosofia dell'educazione
- **Assi**: Asse 3, Asse 6
- **Titolo originale**: Between Past and Future (saggio: The Crisis in Education)
- **Contesto citazione**: Autorità educativa come responsabilità del mondo; educare significa assumere la responsabilità del mondo davanti ai nuovi nati.

### Sulla violenza
- **ID**: `arendt-sulla-violenza`
- **Autore**: Hannah Arendt
- **Anno**: 1970
- **Genere**: Filosofia politica
- **Assi**: Asse 3
- **Titolo originale**: On Violence
- **Contesto citazione**: Autorità ed esercizio del potere; usato per la riflessione sull'autorità educativa.

### Responsabilità e giudizio
- **ID**: `arendt-responsabilita-e-giudizio`
- **Autore**: Hannah Arendt
- **Anno**: 2003
- **Genere**: Filosofia politica
- **Assi**: Asse 3
- **Titolo originale**: Responsibility and Judgment
- **Contesto citazione**: Il giudizio in condizioni di irresolubilità.

### Confessioni
- **ID**: `agostino-confessiones`
- **Autore**: Agostino d'Ippona
- **Anno**: 397–400
- **Genere**: Teologia, autobiografia filosofica
- **Assi**: Asse 5
- **Titolo originale**: Confessiones
- **Contesto citazione**: L'inquietudine come motore strutturale, non come patologia. «Pondus meum amor meus».

### De magistro
- **ID**: `agostino-de-magistro`
- **Autore**: Agostino d'Ippona
- **Anno**: 389
- **Genere**: Filosofia dell'educazione
- **Assi**: Asse 3
- **Contesto citazione**: La verità non viene trasmessa dall'esterno, ma riconosciuta interiormente nel giudizio del soggetto.

### Summa Theologiae
- **ID**: `tommaso-summa-theologiae`
- **Autore**: Tommaso d'Aquino
- **Anno**: 1265–1274
- **Genere**: Teologia, filosofia scolastica
- **Assi**: Asse 3
- **Contesto citazione**: Riflessione sulla norma: I-II, q. 90 e De veritate q. 14.

### Essays on Moral Development
- **ID**: `kohlberg-essays-on-moral-development`
- **Autore**: Lawrence Kohlberg
- **Anno**: 1981–1984
- **Genere**: Psicologia morale
- **Assi**: Asse 3
- **Contesto citazione**: Riduzione del giudizio a schema cognitivo; usato come termine di confronto critico.

### Il giudizio morale nel bambino
- **ID**: `piaget-giudizio-morale-nel-bambino`
- **Autore**: Jean Piaget
- **Anno**: 1932
- **Genere**: Psicologia dello sviluppo
- **Assi**: Asse 3
- **Titolo originale**: Le jugement moral chez l'enfant
- **Contesto citazione**: Usato in funzione delimitativa: capire una regola non equivale all'esercizio del giudizio normativo.

### Verità e metodo
- **ID**: `gadamer-verita-e-metodo`
- **Autore**: Hans-Georg Gadamer
- **Anno**: 1960
- **Genere**: Ermeneutica
- **Assi**: Asse 4, Asse 6
- **Titolo originale**: Wahrheit und Methode
- **Contesto citazione**: L'esperienza autentica smentisce l'aspettativa; la comprensione è fusione di orizzonti (Horizontverschmelzung).

### I gradi dell'organico e l'uomo
- **ID**: `plessner-gradi-dellorganico`
- **Autore**: Helmuth Plessner
- **Anno**: 1928
- **Genere**: Antropologia filosofica
- **Assi**: Asse 4
- **Titolo originale**: Die Stufen des Organischen und der Mensch
- **Contesto citazione**: L'eccedenza come struttura dell'esistenza umana.

### Mente, sé e società
- **ID**: `mead-mind-self-and-society`
- **Autore**: George Herbert Mead
- **Anno**: 1934
- **Genere**: Filosofia sociale, psicologia sociale
- **Assi**: Asse 4
- **Titolo originale**: Mind, Self, and Society
- **Contesto citazione**: Le trasformazioni del sé nei contesti sociali; il sé come struttura dialogica che emerge nell'interazione.
- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)

---

## Output del giorno — da compilare

Al termine, salvare il file `rilevanza-giorno-3.json` in `output/assi-strutturali/` con questa struttura:

```json
{
  "giorno": 3,
  "autori": [
    { "id": "hannah-arendt", "nome": "Hannah Arendt", "rilevanza": "..." },
    { "id": "alasdair-macintyre", "nome": "Alasdair MacIntyre", "rilevanza": "..." },
    { "id": "charles-taylor", "nome": "Charles Taylor", "rilevanza": "..." },
    { "id": "bernard-stiegler", "nome": "Bernard Stiegler", "rilevanza": "..." },
    { "id": "agostino-d-ippona", "nome": "Agostino d'Ippona", "rilevanza": "..." },
    { "id": "tommaso-d-aquino", "nome": "Tommaso d'Aquino", "rilevanza": "..." },
    { "id": "helmuth-plessner", "nome": "Helmuth Plessner", "rilevanza": "..." },
    { "id": "george-herbert-mead", "nome": "George Herbert Mead", "rilevanza": "..." },
  ],
  "libri": [
    { "id": "ricoeur-se-come-un-altro", "titolo": "Sé come un altro", "rilevanza": "..." },
    { "id": "taylor-fonti-del-se", "titolo": "Le fonti del sé", "rilevanza": "..." },
    { "id": "macintyre-dopo-la-virtu", "titolo": "Dopo la virtù", "rilevanza": "..." },
    { "id": "stiegler-prendersi-cura", "titolo": "Prendersi cura. Della gioventù e delle generazioni", "rilevanza": "..." },
    { "id": "arendt-crisi-dell-educazione", "titolo": "La crisi dell'educazione", "rilevanza": "..." },
    { "id": "arendt-sulla-violenza", "titolo": "Sulla violenza", "rilevanza": "..." },
    { "id": "arendt-responsabilita-e-giudizio", "titolo": "Responsabilità e giudizio", "rilevanza": "..." },
    { "id": "agostino-confessiones", "titolo": "Confessioni", "rilevanza": "..." },
    { "id": "agostino-de-magistro", "titolo": "De magistro", "rilevanza": "..." },
    { "id": "tommaso-summa-theologiae", "titolo": "Summa Theologiae", "rilevanza": "..." },
    { "id": "kohlberg-essays-on-moral-development", "titolo": "Essays on Moral Development", "rilevanza": "..." },
    { "id": "piaget-giudizio-morale-nel-bambino", "titolo": "Il giudizio morale nel bambino", "rilevanza": "..." },
    { "id": "gadamer-verita-e-metodo", "titolo": "Verità e metodo", "rilevanza": "..." },
    { "id": "plessner-gradi-dellorganico", "titolo": "I gradi dell'organico e l'uomo", "rilevanza": "..." },
    { "id": "mead-mind-self-and-society", "titolo": "Mente, sé e società", "rilevanza": "..." },
  ]
}
```
