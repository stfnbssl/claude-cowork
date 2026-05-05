# Modulo 1 — Il problema della traduzione senza riduzione
**Numero slide**: 5
**Colore accent**: `#6c63ff`
**Tipo prevalente**: narrative + comparison

---

## Dati globali del modulo

Definire in `m01.js` i dati dei criteri di validità e delle anomalie come costanti:

```javascript
const TRE_ANOMALIE = [
  {
    id: 'riduzione-psicologica',
    numero: '01',
    nome: 'Riduzione psicologica',
    descrizione: 'Un concetto ontologico — che riguarda la struttura dell\'esperienza del bambino — viene trasformato in un tratto individuale: una caratteristica della sua personalità, del suo temperamento, del suo funzionamento interno.',
    esempio_errore: 'Il bambino ha scarsa capacità di attenzione condivisa.',
    esempio_corretto: 'In questa sequenza il campo condiviso si interrompe rapidamente e richiede forte sostegno adulto per riorganizzarsi.',
    cosa_si_perde: 'Il campo relazionale sparisce. Resta solo il bambino con le sue caratteristiche.'
  },
  {
    id: 'tecnicizzazione-precoce',
    numero: '02',
    nome: 'Tecnicizzazione precoce',
    descrizione: 'Un concetto interpretativo — che serve a leggere una situazione — viene trasformato in procedura d\'intervento: cosa fare, quando, con quali passi.',
    esempio_errore: 'Occorre proporre al genitore un training sulla lettura dialogica.',
    esempio_corretto: 'La situazione suggerisce una configurazione in cui il campo relazionale sostiene l\'accesso al mondo condiviso, ma la continuità temporale dello scambio resta fragile.',
    cosa_si_perde: 'La lettura della configurazione salta. Si va direttamente all\'azione senza passare per la comprensione.'
  },
  {
    id: 'normativita-implicita',
    numero: '03',
    nome: 'Normatività implicita',
    descrizione: 'Una descrizione del funzionamento evolutivo diventa implicitamente prescrizione: suggerisce cosa è normale, cosa è adeguato, cosa dovrebbe succedere.',
    esempio_errore: 'L\'adulto deve rallentare, attendere tre secondi e poi nominare l\'immagine.',
    esempio_corretto: 'Quando l\'adulto accelera troppo la sequenza, il bambino interrompe lo scambio; quando attende, il bambino riprende a indicare e vocalizzare.',
    cosa_si_perde: 'La descrizione si trasforma in norma. Il professionista si trova a dire cosa si deve fare, non cosa si vede.'
  }
];

// I 10 criteri selezionati per le flip-card (su 15 totali)
const CRITERI_VALIDITA = [
  {
    id: 'c01',
    numero: '1',
    nome: 'Ancoraggio alla Fase 1',
    domanda: 'Il concetto fondativo è ancora riconoscibile?',
    valido: {
      testo: 'Il bambino entra, attraverso corpo, sguardo, gesto e relazione, in un campo di esperienza condivisibile con l\'adulto.',
      perche: 'Resta riconoscibile il fondamento: soggetto incarnato, relazionale, orientato al mondo.'
    },
    nonValido: {
      testo: 'Il bambino ha buona attenzione visiva.',
      perche: 'Isola una funzione, perde il campo relazionale, rischia di ridurre l\'esperienza a prestazione cognitiva.'
    }
  },
  {
    id: 'c02',
    numero: '2',
    nome: 'Osservabilità situata',
    domanda: 'Chi, dove, cosa, con quali vincoli?',
    valido: {
      testo: 'Durante un bilancio dei 18 mesi, il pediatra osserva il bambino seduto vicino al genitore mentre sfoglia un libro. Il bambino guarda alcune figure, vocalizza, indica un animale e alterna lo sguardo tra libro e adulto.',
      perche: 'Ha contesto, attori, oggetto e osservabili precisi.'
    },
    nonValido: {
      testo: 'Il bambino sviluppa il simbolico attraverso la relazione.',
      perche: 'Corretta come idea generale, ma non è ancora un esempio metodologico. Manca il campo osservativo.'
    }
  },
  {
    id: 'c03',
    numero: '3',
    nome: 'Non-diagnosticità',
    domanda: 'Evita ogni etichetta — clinica, psicologica o morale?',
    valido: {
      testo: 'Il bambino entra nel campo condiviso solo per brevi sequenze; l\'adulto sostiene l\'attenzione nominando le figure, ma il passaggio tra libro, gesto e sguardo resta discontinuo.',
      perche: 'Descrive una configurazione fragile senza classificarla né prescrivere.'
    },
    nonValido: {
      testo: 'Il bambino presenta un ritardo dell\'attenzione condivisa.',
      perche: 'Anticipa una classificazione clinica. Non appartiene alla Fase 2.'
    }
  },
  {
    id: 'c04',
    numero: '4',
    nome: 'Neutralità normativa',
    domanda: 'Descrive o prescrive?',
    valido: {
      testo: 'Quando l\'adulto accelera troppo la sequenza, il bambino interrompe lo scambio; quando l\'adulto attende, il bambino riprende a indicare e vocalizzare.',
      perche: 'Osserva una relazione tra comportamenti senza dire cosa si deve fare.'
    },
    nonValido: {
      testo: 'L\'adulto deve rallentare, attendere tre secondi e poi nominare l\'immagine.',
      perche: 'Può diventare uno strumento in F3, ma in F2 è prematura: trasforma la lettura in prescrizione.'
    }
  },
  {
    id: 'c05',
    numero: '5',
    nome: 'Multi-asseità',
    domanda: 'Mostra l\'intreccio di più assi strutturali?',
    valido: {
      testo: 'Nella lettura condivisa: il corpo è orientato verso libro e adulto; la relazione sostiene l\'attenzione; il gesto indica qualcosa di condivisibile; il desiderio appare come interesse verso alcune figure; il linguaggio adulto introduce un mondo simbolico comune.',
      perche: 'Intreccio di Asse 1 (corpo), Asse 2 (relazione), Asse 5 (desiderio), Asse 6 (mondo simbolico).'
    },
    nonValido: {
      testo: 'Il bambino indica correttamente tre figure.',
      perche: 'Dato comportamentale utile ma mono-dimensionale. Non mostra la configurazione multi-asse.'
    }
  },
  {
    id: 'c06',
    numero: '6',
    nome: 'Traducibilità interdisciplinare',
    domanda: 'Può essere letto da discipline diverse senza appartenere a nessuna in esclusiva?',
    valido: {
      testo: 'Il bambino riesce a trasformare l\'immagine del libro in un\'occasione di scambio: guarda, indica, vocalizza e cerca la risposta dell\'adulto.',
      perche: 'Può parlare alla pediatria, alla psicologia, alla pedagogia e alla relazione genitoriale.'
    },
    nonValido: {
      testo: 'Il bambino mostra competenze referenziali proto-dichiarative adeguate.',
      perche: 'Formulazione specialistica: tecnicamente utile, ma non funziona come traduzione interdisciplinare.'
    }
  },
  {
    id: 'c07',
    numero: '7',
    nome: 'Separazione leggibilità / azione',
    domanda: 'Produce maggiore capacità di vedere — non ancora una decisione?',
    valido: {
      testo: 'La situazione suggerisce una configurazione in cui il campo relazionale sostiene l\'accesso al mondo condiviso, ma la continuità temporale dello scambio resta fragile.',
      perche: 'Aumenta la comprensione. Non dice ancora cosa fare.'
    },
    nonValido: {
      testo: 'Occorre proporre al genitore un training sulla lettura dialogica.',
      perche: 'È già una decisione d\'intervento. Può venire dopo, ma non è compito della Fase 2.'
    }
  },
  {
    id: 'c08',
    numero: '8',
    nome: 'Anti-inferenza',
    domanda: 'Distingui ciò che si osserva da ciò che si interpreta?',
    valido: {
      testo: 'Il bambino allontana il libro, guarda verso la porta e non risponde alla proposta dell\'adulto. In questa sequenza il campo condiviso non si stabilizza.',
      perche: 'Descrive comportamenti osservabili e nomina la configurazione risultante — senza inferire stati interni.'
    },
    nonValido: {
      testo: 'Il bambino non è interessato alla lettura.',
      perche: 'Inferenza troppo rapida: potrebbe essere stanco, sovraccarico, distratto o attratto da altro.'
    }
  },
  {
    id: 'c09',
    numero: '9',
    nome: 'Reversibilità',
    domanda: 'Descrive una configurazione situata o un tratto stabile del bambino?',
    valido: {
      testo: 'In questa sequenza il bambino fatica a mantenere il campo condiviso, ma lo recupera quando l\'adulto rallenta e segue il suo gesto.',
      perche: 'La configurazione è situata, temporanea, modificabile. Non fissa il bambino.'
    },
    nonValido: {
      testo: 'Il bambino non sa condividere l\'attenzione.',
      perche: 'Trasforma una configurazione osservata in un tratto del bambino. Viola il principio di reversibilità.'
    }
  },
  {
    id: 'c10',
    numero: '10',
    nome: 'Protezione dal moralismo',
    domanda: 'Evita giudizi impliciti sull\'adulto, sul bambino o sulla famiglia?',
    valido: {
      testo: 'L\'adulto tende a guidare molto la sequenza; il bambino partecipa soprattutto quando può scegliere la figura da guardare.',
      perche: 'Descrive la dinamica relazionale senza valutare chi sbaglia o chi fa bene.'
    },
    nonValido: {
      testo: 'L\'adulto è troppo direttivo e non lascia spazio al bambino.',
      perche: 'Può cogliere qualcosa di reale, ma la formula è giudicante. Non appartiene alla Fase 2.'
    }
  }
];

// Tabella di validità negativa (da 1.14)
const TABELLA_RIFORMULAZIONI = [
  { riduttiva: 'Il bambino ha scarsa attenzione', valida: 'Il campo condiviso si interrompe rapidamente e richiede forte sostegno adulto' },
  { riduttiva: 'Il genitore stimola poco', valida: 'L\'adulto offre poche aperture allo scambio, ma risponde quando il bambino prende iniziativa' },
  { riduttiva: 'Il bambino non parla', valida: 'La partecipazione simbolica avviene più attraverso gesto e sguardo che attraverso parola' },
  { riduttiva: 'Il bambino è oppositivo', valida: 'Il limite produce rottura del campo e fatica di recupero relazionale' },
  { riduttiva: 'Il bambino è bravo', valida: 'La sequenza mostra buona integrazione tra orientamento corporeo, relazione e iniziativa' }
];
```

---

## SLIDE 1.1 — Ogni disciplina vede in modo diverso

**Tipo**: `narrative`
**Titolo**: Il problema di partenza
**Sottotitolo**: Più linguaggi, stessa scena

**Contenuto principale**:

Layout a colonna singola, abbondante spazio bianco. Apertura narrativa, senza elenchi.

**Sezione superiore — la scena (già nota dal M0, richiamate brevemente)**:

Card tenue (--color-primary-light, bordo sinistro colorato), testo in corsivo:

*Il bambino indica una figura del libro. Vocalizza. Guarda la madre. Lei sorride e nomina l'immagine.*

**Sezione centrale — quattro prospettive disciplinari**:

Quattro colonne (o quattro card affiancate su due righe su mobile), una per disciplina. Ogni card ha: icona/colore disciplina, nome, domanda che la disciplina pone istintivamente.

| Disciplina | Domanda spontanea |
|-----------|------------------|
| 🩺 **Pediatria** | "È nella norma per 18 mesi?" |
| 📚 **Pedagogia** | "L'ambiente è stimolante?" |
| 🧠 **NPI** | "Ci sono segnali d'allerta?" |
| 👨‍👩‍👧 **Counseling familiare** | "Il legame genitore-bambino funziona?" |

**Sezione inferiore — il problema**:

Testo in due righe, centrato, font medio-grande:

*Quattro sguardi legittimi. Quattro linguaggi diversi. Nessuno sbagliato.*

Poi, sotto, con font più piccolo e colore secondario:

*Ma se ognuno legge solo con il proprio linguaggio, il passaggio dall'uno all'altro rischia di produrre errori. La traduzione diretta tra discipline — senza un livello intermedio — genera anomalie.*

**Freccia verso il basso** (elemento grafico) che porta alla slide successiva:

*Quali anomalie?*

---

## SLIDE 1.2 — Le tre anomalie della traduzione diretta

**Tipo**: `interactive`
**Titolo**: Tre anomalie da prevenire
**Sottotitolo**: Cosa accade quando si salta la traduzione

**Contenuto principale**:

Questa slide ha un'**animazione a rivelazione progressiva**: le tre anomalie appaiono una alla volta. L'utente avanza cliccando un pulsante "Mostra prossima anomalia" (oppure la rivelazione avviene con un click sull'area). Un indicatore mostra "1 di 3", "2 di 3", "3 di 3".

Quando tutte e tre sono visibili, appare la definizione conclusiva.

**Struttura di ogni anomalia** (usa i dati da `TRE_ANOMALIE`):

Ogni anomalia è una card orizzontale con:
- Badge numerato grande (01 / 02 / 03), colore --color-accent
- Nome anomalia in grassetto
- Descrizione sintetica (2-3 righe)
- Due righe affiancate: "❌ Formulazione errata" | "✓ Formulazione valida" (dati dal campo `esempio_errore` e `esempio_corretto`)
- Riga finale in piccolo: "Cosa si perde:" + testo dal campo `cosa_si_perde`

**Card 1 — Riduzione psicologica** (appare subito):

Badge: `01` | Nome: **Riduzione psicologica**

Un concetto ontologico — che riguarda la struttura dell'esperienza del bambino — viene trasformato in un **tratto individuale**: una caratteristica della sua personalità o del suo funzionamento interno.

❌ *"Il bambino ha scarsa capacità di attenzione condivisa."*
✓ *"In questa sequenza il campo condiviso si interrompe rapidamente e richiede forte sostegno adulto per riorganizzarsi."*

Cosa si perde: *Il campo relazionale sparisce. Resta solo il bambino con le sue caratteristiche.*

**Card 2 — Tecnicizzazione precoce** (appare al secondo click):

Badge: `02` | Nome: **Tecnicizzazione precoce**

Un concetto interpretativo — che serve a leggere una situazione — viene trasformato in **procedura d'intervento**: cosa fare, quando, con quali passi.

❌ *"Occorre proporre al genitore un training sulla lettura dialogica."*
✓ *"La situazione suggerisce una configurazione in cui il campo relazionale sostiene l'accesso al mondo condiviso, ma la continuità temporale dello scambio resta fragile."*

Cosa si perde: *La lettura della configurazione salta. Si va direttamente all'azione senza passare per la comprensione.*

**Card 3 — Normatività implicita** (appare al terzo click):

Badge: `03` | Nome: **Normatività implicita**

Una descrizione del funzionamento evolutivo diventa implicitamente **prescrizione**: suggerisce cosa è normale, cosa è adeguato, cosa dovrebbe succedere.

❌ *"L'adulto deve rallentare, attendere tre secondi e poi nominare l'immagine."*
✓ *"Quando l'adulto accelera troppo la sequenza, il bambino interrompe lo scambio; quando attende, il bambino riprende a indicare e vocalizzare."*

Cosa si perde: *La descrizione si trasforma in norma. Il professionista si trova a dire cosa si deve fare, non cosa si vede.*

**Blocco conclusivo** (appare solo dopo che tutte e tre le card sono visibili):

Separatore orizzontale, poi testo centrato in blockquote:

> *Le tre anomalie hanno un'origine comune: il passaggio diretto tra discipline senza un livello intermedio che protegga la struttura del concetto.*

---

## SLIDE 1.3 — La definizione di traduzione interdisciplinare

**Tipo**: `standard`
**Titolo**: Cosa significa tradurre senza ridurre
**Sottotitolo**: La definizione operativa

**Contenuto principale**:

Layout a due sezioni verticali separate da divisore.

**Sezione superiore — la definizione**:

Grande blockquote centrato, bordo sinistro spesso, sfondo --color-primary-light:

> *"Il processo mediante cui un concetto mantiene la propria funzione strutturale pur cambiando linguaggio disciplinare."*

Sotto, a destra in piccolo e corsivo: *— F2 — Traduzione Interdisciplinare*

Spiegazione in due righe:

La parola chiave è **funzione strutturale**: non si chiede che il concetto rimanga identico (sarebbe impossibile tra discipline diverse), ma che conservi il lavoro che fa nella comprensione del fenomeno.

**Sezione inferiore — traduzione ≠ semplificazione**:

Tre mini-card affiancate, ognuna con icona e breve testo:

| | Non è... | Non è... | È... |
|---|---|---|---|
| | **Semplificazione** | **Adattamento** | **Traduzione strutturale** |
| | Togliere complessità | Cambiare il concetto per renderlo familiare | Cambiare linguaggio mantenendo la funzione |
| | *"Spiego in modo facile"* | *"Uso un termine equivalente"* | *"Uso un altro linguaggio che fa lo stesso lavoro strutturale"* |

Esempio visivo — tre riquadri collegati da frecce:

```
[F1: "Soggetto incarnato, relazionale, temporale"]
                    ↓  traduzione strutturale
[F2: "Il bambino entra in un campo di esperienza condivisibile"]
                    ↓  traduzione strutturale
[F2: "Il bambino usa il libro come occasione di scambio con l'adulto"]
```

Ogni passaggio ha un colore diverso (--color-f1, --color-f2, --color-f2 più scuro). La funzione strutturale è conservata: il bambino come soggetto relazionale che abita un campo.

**Nota in footer**:
*La traduzione interdisciplinare non è un compromesso: è un'operazione metodologica precisa con criteri verificabili. I criteri sono nella prossima slide.*

---

## SLIDE 1.4 — I criteri di validità: flip cards

**Tipo**: `interactive`
**Titolo**: Come si riconosce una traduzione valida
**Sottotitolo**: Dieci criteri con esempi dal caso-guida

**Contenuto principale**:

Componente a **flip-card** interattivo. Usa i dati da `CRITERI_VALIDITA` (10 criteri selezionati).

**Layout**: griglia 5 × 2 di card (5 colonne, 2 righe) su desktop. Su tablet 3 × 4. Le card sono più piccole delle card standard per stare in griglia.

**Stato di default (fronte della card)**:

Ogni card mostra:
- Numero criterio (grande, --color-accent)
- Nome del criterio (es. "Non-diagnosticità")
- Domanda guida in corsivo (es. *"Evita ogni etichetta?"*)
- Piccola icona ↩ in basso a destra che invita al flip

**Stato flippato (retro della card)**:

Ogni card mostra due sezioni impilate:

**✓ Valido** (sfondo verde molto chiaro):
Testo dell'esempio valido (campo `valido.testo`)
*In piccolo: perché è valido* (campo `valido.perche`)

**✗ Non valido** (sfondo rosso molto chiaro):
Testo dell'esempio non valido (campo `nonValido.testo`)
*In piccolo: perché non è valido* (campo `nonValido.perche`)

Il flip avviene con click o tap. Tutte le card sono indipendenti (si possono tenere più card flippate contemporaneamente).

**Elemento aggiuntivo — Tabella di riformulazione** (sotto la griglia di card, collassata di default):

Un link/pulsante "Mostra la tabella di riformulazione rapida" apre una tabella compatta con le cinque coppie dal campo `TABELLA_RIFORMULAZIONI`:

| Formulazione riduttiva | Formulazione metodologicamente valida |
|----------------------|--------------------------------------|
| Il bambino ha scarsa attenzione | Il campo condiviso si interrompe rapidamente... |
| Il genitore stimola poco | L'adulto offre poche aperture allo scambio... |
| Il bambino non parla | La partecipazione simbolica avviene più attraverso gesto... |
| Il bambino è oppositivo | Il limite produce rottura del campo... |
| Il bambino è bravo | La sequenza mostra buona integrazione... |

Questo elemento è collassato di default per non sovraccaricare visivamente la slide.

**Nota sull'implementazione**:
Il flip CSS usa `transform: rotateY(180deg)` con `perspective` e `backface-visibility: hidden`. La transizione dura 400ms. Su click, il flipback avviene con il secondo click sulla stessa card.

---

## SLIDE 1.5 — La formula conclusiva

**Tipo**: `narrative`
**Titolo**: Il criterio in una frase
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Slide narrativa, minimalista, a colonna singola. Tono di chiusura del modulo e apertura verso il M2.

**Sezione superiore — la sintesi**:

Grande blockquote centrato, font --text-3xl, peso light:

> *"Un esempio valido della Fase 2 non dice ancora che cosa fare.*
> *Mostra che cosa diventa leggibile."*

Sotto, in testo normale, una riga:

Questo è il criterio che raccoglie tutti gli altri. La F2 produce **leggibilità strutturale** — non azione, non diagnosi, non giudizio.

**Sezione centrale — la tabella delle tre anomalie riepilogate**:

Tabella compatta, tre righe, tre colonne:

| Anomalia | Errore | Protezione F2 |
|---------|--------|--------------|
| Riduzione psicologica | Il concetto diventa tratto del bambino | Mantiene il campo relazionale come unità di osservazione |
| Tecnicizzazione precoce | La lettura diventa procedura | Separa esplicitamente osservazione e decisione operativa |
| Normatività implicita | La descrizione diventa prescrizione | Produce configurazioni, non norme |

**Sezione inferiore — collegamento al M2**:

Separatore, poi in testo secondario:

*Come si costruisce concretamente la leggibilità? Attraverso una sequenza precisa di sette operatori.*

Freccia o indicatore visivo che punta al Modulo 2 "Pipeline di traducibilità".

Badge del modulo successivo: `→ Modulo 2 — La pipeline di traducibilità`

**Nota in footer**:
*Nel Modulo 2 vedrai come ogni operatore della pipeline è progettato per prevenire esattamente una di queste anomalie.*

---

## Note per l'implementazione

### Animazione della slide 1.2

La rivelazione progressiva delle tre anomalie non usa la navigazione tra slide: avviene all'**interno** della stessa slide con un bottone "Mostra prossima anomalia". Questo significa che la slide ha uno stato interno gestito da `onEnter` e dall'interazione utente.

Implementare con un contatore interno (`let revealed = 0`). All'`onEnter` della slide, `revealed` si resetta a 1 (la prima anomalia è già visibile). Cliccando "Mostra prossima", `revealed` incrementa e la card corrispondente compare con una transizione `fade-in + slide-up` (200ms).

Il blocco conclusivo (blockquote) è nascosto (`opacity: 0, height: 0`) e appare solo quando `revealed === 3`.

Il pulsante "Mostra prossima anomalia" cambia testo in "Mostra anomalia 2 di 3", poi "Mostra anomalia 3 di 3", poi scompare (o diventa "Leggi la conclusione").

### Navigazione dalla slide 1.2

La freccia → di navigazione tra slide è **disabilitata** finché `revealed < 3`. Solo quando tutte e tre le anomalie sono state rivelate si sblocca il passaggio alla slide successiva. Questo forza una lettura consapevole. Mostrare un messaggio discreto: *"Rivela tutte e tre le anomalie per continuare."*

### Flip cards della slide 1.4

Le 10 card hanno altezze diverse a causa dei testi. Per uniformità visiva, imporre `min-height: 180px` al fronte e `min-height: 260px` al retro. Il retro può fare scroll se il contenuto è molto lungo.

Aggiungere un pulsante globale "Gira tutte" / "Torna al fronte" per uso didattico in aula (il formatore può mostrare tutti i fronti o tutti i retri insieme).

### Transizione tra M0 → M1

All'entrata nel Modulo 1, mostrare per 600ms un titolo di transizione: *"La scena che hai visto nel Modulo 0 — come la leggiamo metodologicamente?"* — poi dissolvenza verso la prima slide. Questo rafforza la continuità col caso-guida.
