# Modulo 1 — Il bambino come soggetto
**Numero slide**: 7
**Colore accent**: `#5c35a0`
**Tipo prevalente**: standard + comparison

---

## Dati globali del modulo

Definire in `f1_m01.js` le seguenti costanti. Sono la sorgente di dati per tutte le slide del modulo.

```javascript
const TRE_IMMAGINI_BAMBINO = [
  {
    id: 'a',
    etichetta: 'A',
    titolo: 'L\'organismo che accumula competenze',
    colore: '#e74c3c',
    sfondo: '#fdecea',
    presupposto: 'Lo sviluppo è un processo di accumulo progressivo: competenze, capacità, prestazioni. Il bambino cresce aggiungendo — e ciò che non ha ancora è ciò che deve acquisire.',
    conseguenza_strumenti: 'Gli strumenti misurano ciò che c\'è e ciò che manca rispetto a una norma di riferimento. Il confronto con soglie è strutturale: senza normativa, lo strumento non funziona.',
    errore_tipico: 'Il bambino viene descritto in termini di distanza dalla norma. La domanda implicita è sempre: "ce la fa?" o "è in ritardo?".',
    esempio: '"Ha un vocabolario di 50 parole a 18 mesi, nella norma." La domanda è quantitativa e normativa — non strutturale, non relazionale, non situata.'
  },
  {
    id: 'b',
    etichetta: 'B',
    titolo: 'L\'insieme di funzioni in maturazione',
    colore: '#e67e22',
    sfondo: '#fef3e2',
    presupposto: 'Lo sviluppo è il dispiegarsi sequenziale di funzioni relativamente autonome: motricità, linguaggio, cognizione, emozione. Ognuna ha la sua traiettoria, i suoi indicatori, i suoi specialisti.',
    conseguenza_strumenti: 'Gli strumenti sono settoriali per costruzione: valutano una funzione per volta. L\'integrazione tra domini è un passaggio aggiunto successivamente, non una struttura originaria.',
    errore_tipico: 'Il bambino viene frammentato in profili funzionali. Un bambino reale non ha mai "funzione linguistica" separata da "funzione relazionale" — ma gli strumenti lo trattano come se ce l\'avesse.',
    esempio: '"Buona cognizione, linguaggio nella norma bassa, qualche difficoltà motoria." Tre valutazioni funzionali parallele. Nessuna lettura del bambino che le vive insieme, in un campo, in un momento specifico.'
  },
  {
    id: 'c',
    etichetta: 'C',
    titolo: 'Il soggetto incarnato, temporale e relazionale',
    colore: '#6c63ff',
    sfondo: '#f0eeff',
    presupposto: 'Lo sviluppo è la traiettoria aperta di un soggetto incarnato in un campo di esperienze e relazioni. Non accumula e non matura: diventa, attraverso un campo che è condizione strutturale del suo diventare.',
    conseguenza_strumenti: 'Gli strumenti leggono configurazioni relazionali ed esperienziali. Non confrontano con norma: descrivono la forma che l\'esperienza ha assunto in un momento dato, in quel campo, con quegli adulti. Possono farlo senza punteggi, senza soglie, senza diagnosi.',
    errore_tipico: 'Nessuno — questa è l\'assunzione del progetto. Ma il rischio è quello di ricadere nelle immagini A o B quando la pressione operativa è alta.',
    esempio: '"Il bambino e il genitore costruiscono un campo di scambio simbolico attorno al libro. La condivisione è presente ma dipende fortemente dalla risposta adulta: evolutivamente aperta." Strutturale, relazionale, non normativa.'
  }
];

const DIMENSIONI_SOGGETTO = [
  {
    id: 'incarnato',
    nome: 'Incarnato',
    colore: '#5c35a0',
    titolo_riduttivo: 'Il corpo come strumento',
    titolo_ontologico: 'Il corpo come modo di essere nel mondo',
    testo_riduttivo: 'Il bambino usa il corpo per percepire, per agire, per comunicare. Il corpo è il mezzo attraverso cui le funzioni cognitive, linguistiche ed emotive si esprimono verso il mondo esterno.',
    testo_ontologico: 'Il bambino è il suo corpo in relazione. Il corpo non è lo strumento dell\'esperienza — è la condizione dell\'esperienza. Non c\'è un "bambino" separato dal corpo che lo abita: c\'è un soggetto incarnato che esiste nel mondo attraverso il proprio corpo, prima ancora di agire su di esso.',
    conseguenza: 'Ogni osservazione che separa il "bambino" dal suo corpo (es. "ha buone capacità cognitive nonostante la difficoltà motoria") opera una scissione che il soggetto reale non vive. Il corpo non è un problema tecnico da risolvere: è il soggetto stesso in una delle sue dimensioni.',
    esempio_caso: 'Nella scena di lettura: la postura orientata verso il libro, il gesto dell\'indicare, il voltarsi verso l\'adulto — non sono comportamenti che il bambino produce: sono il modo in cui il bambino è presente in quel campo.'
  },
  {
    id: 'temporale',
    nome: 'Temporale',
    colore: '#5c35a0',
    titolo_riduttivo: 'Lo sviluppo come accumulo nel tempo',
    titolo_ontologico: 'Lo sviluppo come traiettoria aperta',
    testo_riduttivo: 'Lo sviluppo avviene nel tempo: il bambino cresce, acquisisce, progredisce. Il tempo è lo sfondo in cui le competenze si accumulano e le funzioni si dispiegano. Si può misurare a che punto è arrivato.',
    testo_ontologico: 'Il bambino è temporale: la sua esistenza si costituisce nel tempo come apertura verso possibilità future non ancora determinate. Non c\'è una forma di arrivo rispetto a cui misurare il presente. Nessuna configurazione evolutiva è definitiva. Lo sviluppo non produce un prodotto finale — produce traiettorie, sempre aperte, sempre reversibili, sempre situate.',
    conseguenza: 'Non esiste una "forma finale" rispetto a cui misurare il bambino presente. Ogni configurazione è situata nel tempo e nello spazio relazionale. La valutazione non è mai un bilancio di accumulo: è la lettura di una traiettoria in un momento.',
    esempio_caso: 'Il bambino di 20 mesi nella scena: la sua capacità di condividere il simbolico non è una tappa che ha raggiunto o mancato — è una configurazione che si sta organizzando, in questo campo, con questo adulto, in questo momento. Potrebbe essere diversa domani.'
  },
  {
    id: 'relazionale',
    nome: 'Relazionale',
    colore: '#5c35a0',
    titolo_riduttivo: 'Il campo relazionale come sfondo',
    titolo_ontologico: 'Il campo relazionale come condizione strutturale',
    testo_riduttivo: 'Il bambino si sviluppa in un contesto relazionale. Le relazioni influenzano, supportano o ostacolano lo sviluppo. L\'ambiente affettivo è importante — ma il bambino rimane l\'unità di analisi: si può valutarlo anche da solo, anche senza il genitore, anche in una stanza standardizzata.',
    testo_ontologico: 'Il bambino non si sviluppa nonostante il campo relazionale — si sviluppa attraverso di esso come condizione strutturale. Il campo non è lo sfondo su cui il bambino si muove: è la condizione di possibilità del suo sviluppo. Non c\'è un soggetto separabile dal campo: c\'è sempre un soggetto-in-relazione.',
    conseguenza: 'L\'oggetto di osservazione pertinente non è il bambino isolato, ma la configurazione relazionale ed esperienziale in cui il bambino esiste. Osservare il bambino senza il campo non è solo incompleto — è metodologicamente scorretto rispetto ai fondamenti del progetto.',
    esempio_caso: 'Nella scena di lettura: non "il bambino indica una figura" ma "il bambino indica in un campo in cui l\'adulto è disponibile alla risposta". La struttura dell\'azione cambia a seconda di come è fatto il campo.'
  }
];

const CONSEGUENZE_OPERATIVE = [
  {
    id: 'co1',
    dimensione: 'Cosa si osserva',
    riduttivo: 'Il bambino: le sue prestazioni, i suoi comportamenti, le sue risposte agli stimoli. L\'adulto è variabile di contesto.',
    ontologico: 'La configurazione relazionale ed esperienziale: come bambino e adulto co-costruiscono il campo. Come l\'esperienza si organizza. Qual è la qualità dello scambio. L\'adulto è parte strutturale dell\'oggetto di osservazione.',
    esempio_cambio: 'Non "quante parole produce a 18 mesi" ma "come si organizza lo scambio simbolico tra questo bambino e questo adulto in questa situazione".'
  },
  {
    id: 'co2',
    dimensione: 'Come si costruisce uno strumento',
    riduttivo: 'Si operazionalizzano le competenze da misurare, si definiscono soglie normative di riferimento, si producono punteggi comparabili. La norma è il cuore dello strumento.',
    ontologico: 'Si costruiscono strutture di lettura che descrivono configurazioni senza soglie né punteggi. La domanda è "che forma ha l\'esperienza in questo campo?" — non "quanto è sviluppato il bambino rispetto alla norma?".',
    esempio_cambio: 'Non una checklist di competenze con range normativi, ma un operatore di lettura che descrive la qualità del campo bambino-adulto e le sue condizioni di abitabilità.'
  },
  {
    id: 'co3',
    dimensione: 'Come si restituisce',
    riduttivo: '"Il bambino è nella norma / mostra un ritardo in... / ha raggiunto le tappe attese." Il riferimento implicito è sempre una norma esterna. Il bambino viene misurato rispetto a qualcosa che non lo riguarda specificatamente.',
    ontologico: '"In questa situazione, il campo mostra... Il bambino e il genitore costruiscono uno scambio caratterizzato da... La configurazione è evolutivamente aperta perché..." Il riferimento è la struttura del campo, non una norma astratta.',
    esempio_cambio: 'Non "competenza linguistica nella norma bassa", ma "lo scambio simbolico è presente ma dipende fortemente dalla risposta adulta: la condivisione è accessibile ma fragile in assenza di sostegno".'
  },
  {
    id: 'co4',
    dimensione: 'Cosa si evita',
    riduttivo: 'La diagnosi è implicita in ogni valutazione normativa: qualsiasi confronto con la norma produce una distanza e quindi un giudizio. Il professionista diventa custode di soglie.',
    ontologico: 'Nessun output descrive il bambino in termini di distanza da una norma. Nessun output prescrive cosa fare. Il professionista diventa lettore di configurazioni e di traiettorie evolutive.',
    esempio_cambio: 'Il pediatra non chiude il bilancio con "nella norma" o "da monitorare": apre una descrizione di come lo sviluppo si sta organizzando in quel campo relazionale, e lascia la decisione operativa alla propria disciplina.'
  }
];

const ANNOTAZIONI_CASO_M1 = [
  {
    id: 'a1',
    estratto: 'Il bambino prende il libro',
    dimensione: 'incarnato',
    label: 'Incarnato',
    colore: '#5c35a0',
    annotazione: 'Il prendere non è l\'esecuzione di un compito motorio: è il modo incarnato in cui il bambino si orienta verso l\'oggetto. Il corpo organizza l\'intenzione prima che ci sia un\'intenzione esplicita.'
  },
  {
    id: 'a2',
    estratto: 'indica una figura, vocalizza qualcosa e guarda l\'adulto',
    dimensione: 'relazionale',
    label: 'Relazionale',
    colore: '#1a6b8a',
    annotazione: 'L\'azione si completa solo nel campo: indicare, vocalizzare e guardare l\'adulto non sono tre comportamenti separati — sono un unico atto relazionale che ha senso solo se c\'è un campo disponibile a riceverlo. Il bambino non indica per sé: indica verso.'
  },
  {
    id: 'a3',
    estratto: 'Il genitore nomina l\'immagine, sorride, aspetta',
    dimensione: 'relazionale',
    label: 'Campo come condizione',
    colore: '#1a6b8a',
    annotazione: 'Il campo risponde. Il "aspetta" del genitore non è passività: è la forma in cui il campo si rende disponibile a ricevere l\'iniziativa del bambino. Senza questa disponibilità strutturale, il gesto del bambino cambia significato.'
  },
  {
    id: 'a4',
    estratto: 'Il bambino torna a guardare il libro, gira pagina',
    dimensione: 'temporale',
    label: 'Temporale',
    colore: '#d35400',
    annotazione: 'La sequenza ha continuità: dopo la risposta dell\'adulto, il bambino prosegue la traiettoria — non ricomincia da zero. Il tornare al libro non è ripetizione: è il filo temporale dell\'esperienza che si mantiene attraverso l\'interruzione dello scambio.'
  },
  {
    id: 'a5',
    estratto: 'poi mostra un\'altra figura all\'adulto',
    dimensione: 'temporale',
    label: 'Traiettoria aperta',
    colore: '#d35400',
    annotazione: 'Il mostrare una nuova figura non è un capriccio né un salto: è la direzione della traiettoria che si apre. Il bambino non ripete lo stesso atto — lo varia, lo porta avanti. Lo sviluppo si vede qui: nella direzione, non nel punteggio.'
  }
];

const GUARDRAIL_M1 = {
  code: 'G-F1',
  label: 'Guardrail fondativo — Fase 1',
  text: 'Ogni output derivato da questo framework deve poter essere usato senza descrivere il bambino come individuo isolato. Se una descrizione ha senso solo riferita al bambino separato dal campo, è metodologicamente scorretta rispetto ai fondamenti del progetto.',
  esempi_violazione: [
    '"Il bambino ha un vocabolario di X parole." — Separa la prestazione linguistica dal campo in cui il linguaggio emerge e viene usato.',
    '"Il bambino è poco collaborativo." — Attribuisce un tratto stabile all\'individuo senza leggere la configurazione relazionale in cui si trova.',
    '"Sviluppo cognitivo nella norma." — Isola una funzione dal soggetto incarnato che la vive in un campo specifico.'
  ],
  esempi_rispetto: [
    '"In questa situazione, il campo permette al bambino di condividere un oggetto simbolico con l\'adulto." — Descrive la configurazione relazionale.',
    '"La sequenza di scambio si mantiene quando l\'adulto risponde in modo non direttivo." — Specifica le condizioni del campo.',
    '"La regolazione dell\'esperienza dipende fortemente dalla presenza adulta: non è ancora autosufficiente." — Legge il campo, non il bambino isolato.'
  ]
};
```

---

## SLIDE 1.1 — Tre immagini del bambino

**Tipo**: `interactive`
**Titolo**: Tre immagini del bambino
**Sottotitolo**: Prima di costruire strumenti: cosa si assume?

**Contenuto principale**:

Tre card espandibili disposte in riga orizzontale. Usa i dati da `TRE_IMMAGINI_BAMBINO`. Il componente è `ExpandableCards` con `multiOpen: false` — una sola card aperta alla volta, per favorire il confronto sequenziale.

**Fronte di ogni card** (stato compatto):

```
[Badge colorato: A / B / C]
[Titolo dell'immagine]
[Prima frase del campo presupposto]
[↓ Espandi]
```

I badge usano i colori `colore` dal dato: A in rosso, B in arancio, C in viola (`#6c63ff`). Il titolo della card C ha un bordo bottom sottile colorato in `#6c63ff` per segnalarne il ruolo privilegiato — senza testo esplicito.

**Card espansa** (aggiunge quattro sezioni, separate da divisori):

1. **Presupposto** — testo dal campo `presupposto`, etichetta in piccolo sopra: *"Cosa assume"*
2. **Conseguenza sugli strumenti** — testo dal campo `conseguenza_strumenti`, etichetta: *"Cosa produce"*
3. **Errore tipico** — testo dal campo `errore_tipico` in sfondo tenue rosso/arancio (per A e B) o sfondo verde chiaro (per C), etichetta: *"Rischio"* / *"Assunzione adottata"*
4. **Esempio concreto** — testo dal campo `esempio` in corsivo, sfondo `--color-primary-light`, etichetta: *"Esempio"*

**Istruzione di navigazione sotto le card**:

Prima dell'entrata nella slide, le tre card sono chiuse. L'utente è invitato a espanderle in ordine. Testo in piccolo sotto la griglia:
*Apri le tre card in sequenza: le prime due mostrano le immagini che il metodo supera. La terza è l'assunzione che tutto il corso costruirà.*

**Nota in footer**:
*Queste non sono posizioni teoriche equivalenti. Il progetto adotta la terza. Le prime due rimangono rilevanti perché sono le assunzioni implicite di molti strumenti attualmente in uso: riconoscerle è la condizione per poterle superare.*

---

## SLIDE 1.2 — Incarnato: il corpo non è strumento

**Tipo**: `comparison`
**Titolo**: Incarnato
**Sottotitolo**: Il corpo come modo di essere nel mondo

**Contenuto principale**:

Layout a due colonne affiancate con intestazione colorata — componente `ComparisonPanel`. Usa i dati da `DIMENSIONI_SOGGETTO[0]` (id: `incarnato`).

**Intestazione sinistra** (sfondo rosso tenue, bordo rosso):
**Il corpo come strumento**
*"Il bambino usa il corpo per…"*

**Intestazione destra** (sfondo viola tenue, bordo `#5c35a0`):
**Il corpo come modo di essere**
*"Il bambino è il suo corpo in relazione"*

**Testo colonna sinistra**: campo `testo_riduttivo`

**Testo colonna destra**: campo `testo_ontologico`

**Sotto le colonne — divisore sottile — due sezioni a piena larghezza**:

**Conseguenza operativa** (sfondo `--color-primary-light`, bordo sinistro `#5c35a0`):
Etichetta in piccolo: *"Cosa cambia nel lavoro"*
Testo: campo `conseguenza`

**Nella scena** (sfondo `--color-surface`, bordo sinistro `#d35400`):
Etichetta in piccolo: *"Nel caso-guida"*
Testo: campo `esempio_caso`

**Nota in footer**:
*Questa distinzione non è solo concettuale: ha conseguenze dirette su cosa si chiede in una valutazione, come si scrive una restituzione, cosa si considera rilevante osservare. Un bambino "con difficoltà motorie" e un bambino "il cui corpo fatica a organizzarsi nella relazione" sono la stessa persona descritta con due ontologie diverse.*

---

## SLIDE 1.3 — Temporale: traiettorie aperte

**Tipo**: `standard`
**Titolo**: Temporale
**Sottotitolo**: Lo sviluppo come traiettoria aperta

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — due colonne affiancate (30% / 70%):

**Colonna sinistra** — blocco testuale:
Usa i campi `testo_riduttivo` e `testo_ontologico` da `DIMENSIONI_SOGGETTO[1]` (id: `temporale`), presentati uno sotto l'altro con etichette "Accumulo" / "Traiettoria" e chip colorati (grigio / viola).

**Colonna destra** — visualizzazione comparativa:

Due diagrammi SVG sovrapposti verticalmente, semplici e chiari:

*Diagramma 1 — Accumulo lineare* (linea tratteggiata che sale da sinistra a destra, con pallini che segnano tappe):
```
●──────●──────●──────●──────● → FORMA FINALE
  +1    +1    +1    +1
```
Etichetta sotto: *"Tappa raggiunta / tappa mancata"*

*Diagramma 2 — Traiettoria aperta* (curva sinuosa senza punto terminale, con biforcazioni):
```
    ╭──╮
────┤  ├──⟶ ?
    ╰──╯╲
         ╲──⟶ ?
```
Etichetta sotto: *"Configurazione in movimento — nessun punto di arrivo"*

**Sezione inferiore** — tre card orizzontali (chip testuali):

Tre proprietà della temporalità del soggetto, ognuna in una mini-card:

**Nessuna configurazione è definitiva**
*Reversibile, dinamica, situata. La valutazione di oggi non descrive il bambino: descrive il campo in questo momento.*

**Non c'è una forma di arrivo**
*Nessuno strumento può misurare la distanza da un'architettura che non esiste. La domanda "è in ritardo?" presuppone una linea di arrivo che il modello non ammette.*

**Il tempo non è sfondo, è struttura**
*Il bambino non si sviluppa nel tempo come in un contenitore: la temporalità è una dimensione costitutiva del suo essere soggetto.*

**Nella scena** — card narrativa in basso (sfondo `--color-primary-light`):
Testo: campo `esempio_caso` da `DIMENSIONI_SOGGETTO[1]`

**Nota in footer**:
*L'apertura della traiettoria non è una limitazione degli strumenti — è una proprietà dello sviluppo. Il metodo non rinuncia alla precisione: rinuncia alla normatività. Le descrizioni sono precise, strutturate e metodicamente fondate — ma non misurano distanze da un'architettura di arrivo che non esiste.*

---

## SLIDE 1.4 — Relazionale: il campo è condizione

**Tipo**: `standard`
**Titolo**: Relazionale
**Sottotitolo**: Il campo relazionale come condizione strutturale

**Contenuto principale**:

Layout a colonna singola, con grande citazione centrale e sviluppo sottostante.

**Citazione centrale** (blockquote stilizzato, bordo sinistro `#5c35a0`, font grande --text-2xl):

> *"Il bambino non si sviluppa nonostante il campo relazionale, né attraverso di esso come se fosse un ambiente separato: si sviluppa costitutivamente come soggetto-in-relazione."*

**Sotto la citazione** — due box affiancati:

**Box sinistro** (sfondo rosso tenue, bordo rosso):
**Il campo come sfondo**
Testo: campo `testo_riduttivo` da `DIMENSIONI_SOGGETTO[2]`

**Box destro** (sfondo viola tenue, bordo `#5c35a0`):
**Il campo come condizione strutturale**
Testo: campo `testo_ontologico` da `DIMENSIONI_SOGGETTO[2]`

**Sotto i box** — divisore — **Conseguenza operativa diretta**:

Grande callout evidenziato (sfondo `--color-primary-light`, padding generoso, bordo sinistro spesso `#5c35a0`):

*L'oggetto di osservazione pertinente non è il bambino isolato, ma la **configurazione relazionale ed esperienziale** in cui il bambino esiste. Osservare il bambino separato dal campo non è solo incompleto — è metodologicamente scorretto rispetto ai fondamenti del progetto.*

**Sotto il callout** — card narrativa del caso-guida (sfondo `--color-primary-light`):
Testo: campo `esempio_caso` da `DIMENSIONI_SOGGETTO[2]`

**Elemento finale** — `GuardrailBadge` con codice `G-F1`:
Mostrare il guardrail in forma breve (label + prima riga di testo). La versione completa verrà nella slide 1.7.

**Nota in footer**:
*Questo non è un principio teorico che si applica "quando è rilevante". È una condizione strutturale: vale sempre. Quando un professionista usa uno strumento che non include il campo relazionale come parte dell'oggetto di osservazione, non sta solo usando uno strumento parziale — sta usando uno strumento costruito su un'ontologia diversa da quella del progetto.*

---

## SLIDE 1.5 — Conseguenze operative

**Tipo**: `interactive`
**Titolo**: Cosa cambia nella pratica
**Sottotitolo**: Dall'ontologia all'osservazione, agli strumenti, alla restituzione

**Contenuto principale**:

Tabella interattiva a tre colonne usando i dati da `CONSEGUENZE_OPERATIVE`. Ogni riga è espandibile (click sulla riga apre il dettaglio sottostante).

**Intestazioni**:
| Dimensione | Con le immagini A–B | Con l'immagine C |

**Struttura di ogni riga**:

*Stato compatto*:
```
[Dimensione in grassetto]  |  [Testo riduttivo breve]  |  [Testo ontologico breve]
```

*Riga espansa* (aggiunge sotto la riga):
Box a piena larghezza, sfondo `--color-primary-light`:
**Esempio concreto del cambiamento**: testo dal campo `esempio_cambio`

Le intestazioni delle colonne centrale e destra hanno chip colorati: la centrale in rosso/arancio (immagini A–B), la destra in viola (immagine C).

**Sotto la tabella** — testo enfatizzato centrato:

*Queste quattro dimensioni non sono modifiche superficiali di linguaggio. Richiedono uno strumento costruito su basi diverse — un framework diverso. Questo è esattamente ciò che il metodo costruisce.*

**Nota in footer**:
*Le conseguenze operative non emergono automaticamente dall'assunzione ontologica: richiedono che la Fase 2 costruisca gli strumenti di traduzione (Nodi, Matrice, Grammatica) e la Fase 3 li renda operativi nei contesti professionali. M1 stabilisce il punto di partenza; il resto del corso costruirà il percorso.*

---

## SLIDE 1.6 — Il caso-guida: il bambino come soggetto

**Tipo**: `narrative`
**Titolo**: Il bambino come soggetto
**Sottotitolo**: La stessa scena, letta con lenti diverse

**Contenuto principale**:

Layout narrativo a colonna singola. La scena del caso-guida appare una volta sola — ma con annotazioni marginali cliccabili che rivelano come ogni dettaglio illumina le tre dimensioni del soggetto.

**Istruzione iniziale** (testo piccolo, centrato, in `--color-text-muted`):
*Clicca sulle parole evidenziate per vedere come si leggono le tre dimensioni del soggetto*

**Testo della scena** — da `window.CASO_GUIDA.scena` — con parole/frasi specifiche che sono cliccabili (evidenziate con sottolineatura punteggiata in `#5c35a0`). Le parole evidenziate corrispondono agli `estratto` in `ANNOTAZIONI_CASO_M1`.

Frasi evidenziabili:
- `"Il bambino prende il libro"` → annotazione A1 (incarnato)
- `"indica una figura, vocalizza qualcosa e guarda l'adulto"` → annotazione A2 (relazionale)
- `"Il genitore nomina l'immagine, sorride, aspetta"` → annotazione A3 (campo come condizione)
- `"Il bambino torna a guardare il libro, gira pagina"` → annotazione A4 (temporale)
- `"poi mostra un'altra figura all'adulto"` → annotazione A5 (traiettoria aperta)

Cliccando su una frase evidenziata, compare un pannello laterale (o un tooltip espanso sotto il paragrafo) con:
- Badge colorato con `label` dell'annotazione
- Testo dell'annotazione
- Asse di riferimento in piccolo

Un solo pannello aperto alla volta.

**Sotto la scena — separatore — sezione comparativa**:

Due card affiancate, con intestazione:

**Card sinistra** — *"Come si leggerebbe con l'immagine A o B"*:
```
"Il bambino di 20 mesi mostra competenze linguistiche nella norma:
indica, vocalizza, usa il gesto di pointing. Attenzione sostenuta.
Il genitore stimola adeguatamente."
```
Chip sotto: `prestazionale` · `normativa` · `individua il bambino come unità`

**Card destra** — *"Come si legge con l'immagine C"*:
```
"Il campo relazionale è disponibile alla risposta: bambino e adulto
costruiscono uno scambio attorno a un oggetto comune. Il bambino
apre l'interazione e l'adulto la sostiene senza dirigerla.
La configurazione è evolutivamente aperta."
```
Chip sotto: `configurazionale` · `relazionale` · `descrive il campo, non il bambino`

**Nota in footer**:
*Questo sarà il modo in cui il caso-guida ci accompagnerà per tutti e sette i moduli di F1: la stessa scena, riluminata ogni volta da una lente diversa. Non si aggiunge contenuto alla scena — si cambia la domanda con cui la si guarda.*

---

## SLIDE 1.7 — Il guardrail fondativo

**Tipo**: `standard`
**Titolo**: Il guardrail che attraversa tutto il corso
**Sottotitolo**: Una regola strutturale, non un'indicazione di stile

**Contenuto principale**:

Layout a colonna singola con grande `GuardrailBadge` come elemento principale, seguito da esempi.

**Elemento principale** — `GuardrailBadge` in versione espansa (tutta la slide è organizzata attorno ad esso):

Box con sfondo `--color-guardrail-bg` (`#d8f3dc`), bordo sinistro spesso `--color-guardrail` (`#2d6a4f`), icona scudo.

**Codice**: `G-F1`
**Etichetta**: *Guardrail fondativo — Fase 1*
**Testo**: campo `text` da `GUARDRAIL_M1`

**Sotto il guardrail** — due colonne:

**Colonna sinistra — Esempi di violazione**:
Intestazione: `⚠ Formulazioni che violano il guardrail`
Lista puntata: campo `esempi_violazione` da `GUARDRAIL_M1`
Ogni voce su sfondo rosso tenue con bordo sinistro rosso.

**Colonna destra — Esempi di rispetto**:
Intestazione: `✓ Formulazioni coerenti con il guardrail`
Lista puntata: campo `esempi_rispetto` da `GUARDRAIL_M1`
Ogni voce su sfondo verde tenue con bordo sinistro verde.

**Sotto le colonne** — divisore — blocco finale:

Testo enfatizzato centrato:
*Questo guardrail non è una raccomandazione di buona prassi. È un vincolo strutturale che deriva dall'ontologia del soggetto stabilita in questo modulo. Ogni strumento costruito nel framework — in F2 come in F3 — viene verificato rispetto a esso.*

Sotto, in testo più piccolo (`--color-text-muted`):
*Nei moduli successivi vedremo come questo vincolo si traduce nei sei assi strutturali di sviluppo — e come ciascun asse porta con sé il proprio guardrail specifico.*

**Badge modulo successivo**:
`→ Modulo 2 — Gli assi strutturali: logica e architettura`

**Nota in footer**:
*Il guardrail G-F1 agisce come vincolo di coerenza su tutto il framework: dal primo asse strutturale (M3) all'ultimo strumento operativo (F3). Ogni volta che uno strumento descrive il bambino come individuo isolato — senza campo, senza relazione, senza contesto — è questo vincolo che segnala lo scarto.*

---

## Note per l'implementazione

### Slide 1.1 — ExpandableCards con indicatore di progressione

Le tre card A–B–C hanno una logica narrativa: si aprono idealmente in sequenza. Per supportare questo senza obbligare:

- Al caricamento della slide, la card A è aperta di default (unica aperta, `multiOpen: false`).
- Aggiungere un testo di orientamento sopra le card: *"Le immagini A e B descrivono assunzioni diffuse che il metodo supera. L'immagine C è l'assunzione che questo corso costruirà."*
- La card C ha un bordo `#6c63ff` leggermente più spesso delle altre due, per segnalarne la diversa natura senza testo aggiuntivo.

### Slide 1.2, 1.3, 1.4 — Sequenza incarnato / temporale / relazionale

Le tre slide formano una progressione. È utile che il navigatore mostri un mini-breadcrumb orizzontale sopra il titolo: `Incarnato · Temporale · Relazionale` con la dimensione corrente evidenziata. Questo può essere implementato come piccolo componente inline nella slide, non nella sidebar globale.

### Slide 1.5 — Tabella interattiva

La tabella `CONSEGUENZE_OPERATIVE` ha quattro righe. Su desktop 1280px+ sono tutte visibili senza scroll. La riga espansa aggiunge circa 80-100px: la slide può crescere verticalmente in questo caso. Non usare scroll interno alla slide — lasciare che la slide stessa si allunghi se necessario.

Alternativa se la tabella risulta troppo densa: usare ExpandableCards verticali (una card per dimensione) anziché una tabella. Il contenuto è lo stesso; il layout è più generoso.

### Slide 1.6 — Annotazioni cliccabili sulla scena

Le parole/frasi evidenziabili nel testo richiedono un rendering personalizzato della stringa `window.CASO_GUIDA.scena`: le parole corrispondenti agli `estratto` in `ANNOTAZIONI_CASO_M1` devono essere marcate con `<span class="annotabile" data-annotation-id="a1">` ecc.

Poiché il testo del caso-guida è fisso e noto, il markup può essere pre-costruito in `f1_m01.js` come stringa HTML con i tag già inseriti, anziché cercare e sostituire dinamicamente. Questo è più robusto.

Il pannello annotazione appare su click con `slide-down` (200ms). Su click su una seconda frase evidenziata, il pannello corrente si chiude e si apre il nuovo (transizione breve).

### Slide 1.7 — Chiusura del modulo

La slide 1.7 è la più "formale" del modulo: nessuna animazione, nessuna interattività. È intenzionalmente statica — il guardrail deve avere autorevolezza visiva. Usare padding generoso e spazio bianco.

Il badge `→ Modulo 2` è un link visivo, non un bottone di navigazione (la navigazione avviene con le frecce). Stile: chip con bordo `#4a5568`, sfondo trasparente, testo `--color-text-secondary`.
