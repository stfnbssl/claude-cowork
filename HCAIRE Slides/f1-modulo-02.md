# Modulo 2 — Gli assi strutturali: logica e architettura
**Numero slide**: 7
**Colore accent**: `#4a5568`
**Tipo prevalente**: diagram + interactive

---

## Dati globali del modulo

Definire in `f1_m02.js` le seguenti costanti. Sono la sorgente di dati per tutte le slide del modulo — e alcune (`SEI_ASSI`) saranno importate anche dai moduli M3–M7 come riferimento master. Definire `SEI_ASSI` in `app.js` come costante globale; le altre costanti restano locali a `f1_m02.js`.

```javascript
// ─── COSTANTE GLOBALE — definire in app.js ────────────────────────────────
window.SEI_ASSI = [
  {
    id: 'a1',
    numero: 1,
    nome: 'Ontologico-fenomenologico',
    nome_breve: 'Abitare l\'esperienza',
    colore: '#6c63ff',
    sfondo: '#f0eeff',
    domanda_guida: 'In che modo il bambino riesce ad abitare l\'esperienza che sta vivendo?',
    funzione_strutturale: `Chiarisce che tipo di soggetto è il bambino: incarnato, temporale, relazionale.
      Stabilisce il principio per cui ogni asse successivo è possibile. Ha funzione fondativa:
      tutti gli altri assi lo presuppongono. Senza Asse 1, il bambino sarebbe un organismo
      che processa stimoli — non un soggetto che abita l\'esperienza.`,
    dipendenze: [],   // non dipende da nessun altro asse
    contesto_clinico: 'Come si organizza l\'esperienza del bambino durante la visita? Il campo regge?',
    contesto_pedagogico: 'Il bambino abita l\'ambiente del nido o lo subisce?',
    contesto_genitoriale: 'Il genitore sente il bambino come soggetto della propria esperienza?',
    errore_tipico: 'Confondere una difficoltà di organizzazione dell\'esperienza con un deficit specifico.',
    guardrail: 'Nessun output derivato da Asse 1 può descrivere il bambino separato dal campo in cui abita l\'esperienza.'
  },
  {
    id: 'a2',
    numero: 2,
    nome: 'Affettivo-morale',
    nome_breve: 'Riconoscimento dell\'alterità',
    colore: '#2d6a4f',
    sfondo: '#d8f3dc',
    domanda_guida: 'Come riconosce il bambino l\'altro come portatore di un\'esperienza propria?',
    funzione_strutturale: `Introduce progressivamente la dimensione dell\'alterità come istanza interna.
      Il riconoscimento dell\'altro come portatore di un\'esperienza propria — non riducibile alla propria —
      è la condizione per qualsiasi relazione non fusionale. Presuppone Asse 1: solo un soggetto incarnato
      può riconoscere un altro soggetto incarnato.`,
    dipendenze: ['a1'],
    contesto_clinico: 'Il bambino cerca l\'adulto come altro soggetto o lo usa come strumento?',
    contesto_pedagogico: 'L\'educatore è percepito come portatore di un\'esperienza propria o come funzione?',
    contesto_genitoriale: 'Il genitore riconosce nel bambino un soggetto con la propria esperienza?',
    errore_tipico: 'Ridurre il riconoscimento dell\'altro a empatia, a lettura delle emozioni o a compliance sociale.',
    guardrail: 'Nessun output derivato da Asse 2 può descrivere la relazione in termini di "stimolo-risposta" tra soggetti o come semplice coordinazione di comportamenti.'
  },
  {
    id: 'a3',
    numero: 3,
    nome: 'Normativo-educativo',
    nome_breve: 'Normatività emergente',
    colore: '#27ae60',
    sfondo: '#eafaf1',
    domanda_guida: 'Come emerge la capacità di orientare l\'azione secondo criteri condivisi?',
    funzione_strutturale: `Introduce la possibilità del giudizio e della responsabilità.
      Non la norma imposta dall\'esterno, ma l\'emergenza interna della capacità di orientare l\'azione
      secondo criteri condivisi. Presuppone Asse 2: non si orienta l\'azione secondo criteri condivisi
      senza aver prima riconosciuto l\'altro come portatore di esperienza propria.`,
    dipendenze: ['a1', 'a2'],
    contesto_clinico: 'Il bambino partecipa a strutture di scambio con criteri impliciti condivisi?',
    contesto_pedagogico: 'Le regole del gruppo sono normatività condivisa o imposizione esterna?',
    contesto_genitoriale: 'Il bambino percepisce i limiti come criteri relazionali o come arbitrio?',
    errore_tipico: 'Confondere normatività emergente con obbedienza, compliance o rispetto di regole imposte.',
    guardrail: 'Nessun output derivato da Asse 3 può contenere giudizi di valore sul rispetto o mancato rispetto di norme da parte del bambino.'
  },
  {
    id: 'a4',
    numero: 4,
    nome: 'Separazione e limite reale',
    nome_breve: 'Incontro con il reale',
    colore: '#c0392b',
    sfondo: '#fdecea',
    domanda_guida: 'Come incontra il bambino la resistenza del reale?',
    funzione_strutturale: `Introduce una discontinuità strutturale: il reale come eccedenza che interrompe
      ogni fantasia di regolazione totale. L\'incontro con il limite non è un fallimento dello sviluppo,
      ma una condizione del suo proseguimento. Presuppone gli assi precedenti: senza Asse 1–2–3,
      il limite non può essere incontrato come strutturante — diventa solo interruzione.`,
    dipendenze: ['a1', 'a2', 'a3'],
    contesto_clinico: 'Il bambino incontra il limite della visita come strutturante o come distruttivo?',
    contesto_pedagogico: 'Il confine del gruppo organizza o schiaccia l\'esperienza del bambino?',
    contesto_genitoriale: 'Il "no" del genitore genera apprendimento o ritiro dalla relazione?',
    errore_tipico: 'Trattare l\'incontro con il limite come indicatore di difficoltà di regolazione emotiva o di bassa tolleranza alla frustrazione.',
    guardrail: 'Nessun output derivato da Asse 4 può moralizzare il comportamento del bambino davanti al limite ("fa i capricci", "è testardo").'
  },
  {
    id: 'a5',
    numero: 5,
    nome: 'Desiderio',
    nome_breve: 'Direzione dell\'esperienza',
    colore: '#e67e22',
    sfondo: '#fef3e2',
    domanda_guida: 'Come si orienta il bambino verso possibilità che eccedono il presente?',
    funzione_strutturale: `Riorganizza l\'orientamento del soggetto dopo l\'incontro con il limite.
      Il desiderio non è carenza ma direzione: la capacità del bambino di proiettarsi verso un mondo
      che eccede la situazione presente. Dipende da Asse 4: solo un soggetto che ha incontrato la
      resistenza del reale può sviluppare una direzione propria che non sia mera reazione.`,
    dipendenze: ['a1', 'a4'],
    contesto_clinico: 'Il bambino mostra iniziativa spontanea? C\'è una direzione nell\'azione?',
    contesto_pedagogico: 'Il bambino ha interessi propri o è orientato solo da ciò che l\'adulto propone?',
    contesto_genitoriale: 'Il genitore riconosce la direzione del bambino o la scambia per capriccio?',
    errore_tipico: 'Ridurre il desiderio a preferenza, motivazione estrinseca o interesse per uno stimolo specifico.',
    guardrail: 'Nessun output derivato da Asse 5 può descrivere l\'iniziativa del bambino come semplice preferenza ("gli piace", "vuole") senza leggere la direzione strutturale dell\'esperienza.'
  },
  {
    id: 'a6',
    numero: 6,
    nome: 'Rapporto con il mondo storico-culturale',
    nome_breve: 'Partecipazione al mondo condiviso',
    colore: '#d35400',
    sfondo: '#fef0e7',
    domanda_guida: 'Come entra il bambino nella partecipazione al mondo condiviso?',
    funzione_strutturale: `Non fonda nuove strutture, ma traduce e mette alla prova tutte le precedenti
      nel mondo concreto — linguaggi, istituzioni, pratiche, oggetti culturali. È il livello in cui
      lo sviluppo diventa partecipazione al mondo condiviso. Presuppone tutti gli altri assi:
      senza di essi, la partecipazione è esecuzione, non co-costruzione.`,
    dipendenze: ['a1', 'a2', 'a3', 'a4', 'a5'],
    contesto_clinico: 'Il bambino usa gli oggetti culturali come mediatori di mondo condiviso?',
    contesto_pedagogico: 'L\'apprendimento è partecipazione al mondo comune o esecuzione di compiti?',
    contesto_genitoriale: 'Il bambino entra nella cultura della famiglia o vi viene solo esposto?',
    errore_tipico: 'Ridurre la partecipazione al mondo storico-culturale a competenze linguistiche, a riconoscimento di simboli o a performance cognitive.',
    guardrail: 'Nessun output derivato da Asse 6 può ridurre la partecipazione al mondo condiviso a una prestazione misurabile (vocabolario, riconoscimento, denominazione).'
  }
];

// ─── COSTANTI LOCALI — definire in f1_m02.js ─────────────────────────────

const QUATTRO_PROPRIETA = [
  {
    id: 'p1',
    numero: '1',
    nome: 'Compresenza',
    sommario: 'Tutti e sei gli assi sono attivi simultaneamente in qualsiasi momento dello sviluppo.',
    testo: `Tutti e sei gli assi sono attivi e compresenti lungo tutto l\'arco evolutivo: non si
      attivano a turno, non si sostituiscono, non si "completano". In un qualsiasi momento dello
      sviluppo del bambino, tutti e sei stanno funzionando — anche se non con uguale salienzaIn questa configurazione relazionale, e anche se non tutti sono egualmente visibili.`,
    test: 'In questa scena, sto leggendo un solo asse o sto ignorando gli altri cinque che sono comunque attivi?',
    implicazione: `Nessuno strumento può "misurare un asse alla volta" come se gli altri fossero assenti.
      Ogni configurazione osservativa deve tener conto che gli altri assi stanno operando — anche
      se la slide o lo strumento ne mette a fuoco uno in particolare.`,
    esempio: `Durante la lettura condivisa, Asse 1 (come il bambino abita il campo), Asse 2 (riconosce
      il genitore come soggetto), Asse 3 (partecipa a una struttura con criteri impliciti), Asse 4
      (incontra il limite delle pagine), Asse 5 (ha una direzione verso il prossimo scambio) e Asse 6
      (usa il libro come oggetto culturale) sono tutti attivi insieme.`
  },
  {
    id: 'p2',
    numero: '2',
    nome: 'Dipendenza strutturale',
    sommario: 'Gli assi superiori presuppongono i precedenti; Asse 1 non richiede la presenza degli altri.',
    testo: `Esiste una gerarchia strutturale — non valutativa né cronologica — che indica dipendenze
      logiche tra le dimensioni. Asse 2 non può funzionare senza Asse 1. Asse 6 presuppone tutti
      gli assi precedenti. Ma Asse 1 non richiede la presenza di nessun altro asse per funzionare:
      è fondativo in senso assoluto. La gerarchia non dice quale asse è "più importante":
      dice quale asse è condizione logica degli altri.`,
    test: 'Se rimuovo Asse 1 da questa lettura, l\'Asse che sto usando regge ancora? Se no, lo sto presupponendo senza dirlo.',
    implicazione: `La gerarchia ha conseguenze sulla costruzione degli strumenti: uno strumento che
      lavora su Asse 3 (normatività) deve poter rendere conto di Asse 1 e Asse 2 come condizioni
      di sfondo — anche se non li "misura" esplicitamente.`,
    esempio: `Un educatore che osserva la normatività emergente in un bambino (Asse 3) sta implicitamente
      presupponendo che il bambino abiti un'esperienza (Asse 1) e riconosca l'altro come soggetto (Asse 2).
      Se queste condizioni mancano, quello che osserva non è normatività emergente: è qualcosa d'altro.`
  },
  {
    id: 'p3',
    numero: '3',
    nome: 'Variabilità relativa',
    sommario: 'Il peso di ciascun asse non è costante: varia per momento, contesto e configurazione.',
    testo: `Il peso di ciascun asse non è costante lungo lo sviluppo né tra situazioni diverse.
      In alcuni momenti o contesti un asse è più saliente, più sollecitato, più visibile. Un bambino
      che incontra il limite (Asse 4 saliente) in una situazione di scarsa regolazione (Asse 1 fragile)
      si trova in una configurazione diversa rispetto a uno che incontra lo stesso limite in un campo
      relazionale solido. Gli assi non cambiano: cambia il loro peso relativo nel campo specifico.`,
    test: 'Sto descrivendo la variabilità come proprietà del bambino o come configurazione situata di questo campo in questo momento?',
    implicazione: `La variabilità relativa rende impossibile qualsiasi "profilo d\'asse" stabile:
      un bambino non ha "Asse 4 debole" come tratto — ha una configurazione in cui Asse 4 risulta
      particolarmente sollecitato in quel campo specifico. La descrizione è sempre situata.`,
    esempio: `Lo stesso bambino può mostrare Asse 5 (desiderio) molto saliente al nido con l\'educatrice
      preferita, e Asse 1 (organizzazione dell\'esperienza) fragile durante la visita pediatrica.
      Non è incoerente: sono due configurazioni diverse, in due campi diversi.`
  },
  {
    id: 'p4',
    numero: '4',
    nome: 'Non-esclusività disciplinare',
    sommario: 'Nessun asse appartiene a una sola disciplina: ogni asse è leggibile da tutte.',
    testo: `Nessun asse appartiene a una sola disciplina. Asse 2 (riconoscimento dell\'alterità) non è
      "la psicologia": la pediatria lo legge nella qualità del contatto genitore-bambino durante la
      visita, la neuropsichiatria nella capacità di intersoggettività, la pedagogia nelle forme di
      riconoscimento tra pari al nido. Ogni asse attraversa tutti i contesti professionali — con
      linguaggi diversi, ma attraverso la stessa struttura.`,
    test: 'Sto assegnando questo asse a una disciplina specifica, o sto mantenendo la sua trasversalità?',
    implicazione: `La non-esclusività è la condizione che rende possibile il dialogo interdisciplinare
      in F2: se ogni asse appartenesse a una sola disciplina, la traduzione sarebbe impossibile. Gli assi
      sono il livello in cui le discipline si possono incontrare — prima di dividersi nei propri strumenti.`,
    esempio: `Asse 6 (mondo storico-culturale) non è "la pedagogia". Il pediatra lo legge nell\'uso
      del libro durante il bilancio, il neurologo nella capacità di condivisione referenziale, il counselor
      nelle pratiche culturali della famiglia, l\'educatore nelle forme di partecipazione al gruppo.`
  }
];

const CONFRONTO_ASSE_COMPETENZA = {
  intestazione: 'Asse e competenza non sono la stessa cosa',
  sottotitolo: 'Una distinzione che cambia la forma degli strumenti',
  righe: [
    {
      id: 'r1',
      dimensione: 'Natura',
      asse: 'Struttura interpretativa — sempre attiva, non si acquisisce',
      competenza: 'Abilità o capacità — si acquisisce, si consolida, si può misurare'
    },
    {
      id: 'r2',
      dimensione: 'Temporalità',
      asse: 'Non arriva e non scompare: si trasforma nel peso relativo ma resta sempre presente',
      competenza: 'Segue una traiettoria: assente → emergente → consolidata → automatizzata'
    },
    {
      id: 'r3',
      dimensione: 'Relazione con la norma',
      asse: 'Non ha soglie normative: non esiste un "livello adeguato di Asse 3"',
      competenza: 'Ha soglie normative per età: una competenza può essere "nella norma" o "in ritardo"'
    },
    {
      id: 'r4',
      dimensione: 'Funzione negli strumenti',
      asse: 'Orienta la costruzione degli strumenti; non è operazionalizzato direttamente',
      competenza: 'È operazionalizzata direttamente: è ciò che lo strumento misura o valuta'
    },
    {
      id: 'r5',
      dimensione: 'Soggetto grammaticale',
      asse: 'Descrive il campo relazionale ed esperienziale in cui il bambino esiste',
      competenza: 'Descrive il bambino individuale ("il bambino sa / riesce a / ha raggiunto")'
    },
    {
      id: 'r6',
      dimensione: 'Esempio concreto',
      asse: '"Come il bambino abita lo scambio con l\'adulto attorno al libro" (Asse 1 + Asse 6)',
      competenza: '"Competenza referenziale: usa il pointing per condividere informazioni" (tappa 18 mesi)'
    }
  ],
  nota_finale: `La distinzione non è teorica: un professionista che confonde asse e competenza
    costruisce strumenti che sembrano leggere la struttura dello sviluppo ma in realtà misurano
    prestazioni. Il risultato è normativo anche quando non si intende esserlo.`
};

const MEDIAZIONE_STRUMENTI = {
  titolo: 'Gli assi orientano — non prescrivono',
  livelli: [
    {
      id: 'l1',
      livello: 'Livello 1',
      label: 'Assi strutturali (F1)',
      sublabel: 'Strutture interpretative — orientano l\'osservazione',
      colore: '#6c63ff',
      tipo: 'foundation',
      descrizione: 'I sei assi definiscono le dimensioni strutturali dell\'esperienza del soggetto in sviluppo. Non si usano direttamente nel lavoro professionale. Fondano i vincoli che rendono possibile qualsiasi strumento successivo.'
    },
    {
      id: 'l2',
      livello: 'Livello 2',
      label: 'Nodi Trasversali e Matrice (F2)',
      sublabel: 'Configurazioni traducibili — rendono leggibile il campo',
      colore: '#1a6b8a',
      tipo: 'operator',
      descrizione: 'I sette Nodi Trasversali sono configurazioni in cui più assi si co-organizzano producendo qualcosa di osservabile e interrogabile da discipline diverse. La Matrice li traduce nei linguaggi professionali. Questo è il livello intermedio che rende possibile il passaggio agli strumenti.'
    },
    {
      id: 'l3',
      livello: 'Livello 3',
      label: 'Strumenti operativi (F3)',
      sublabel: 'Dispositivi contestualizzati — rendono possibile l\'azione',
      colore: '#2d9cdb',
      tipo: 'output',
      descrizione: 'Gli strumenti di F3 nascono dalla grammatica configurazionale di F2, che a sua volta porta in sé i vincoli di F1. Ogni strumento — anche il più operativo — porta in sé la fondazione ontologica come guardrail implicito.'
    },
    {
      id: 'l4',
      livello: 'Livello 4',
      label: 'Ricerca empirica',
      sublabel: 'Validazione degli strumenti — non degli assi',
      colore: '#4a5568',
      tipo: 'output',
      descrizione: 'La verificabilità empirica riguarda gli strumenti costruiti nel quadro dei Nodi e della Matrice — non gli assi direttamente. La ricerca non "misura gli assi": valida se gli strumenti costruiti nel loro quadro funzionano nei contesti reali.'
    }
  ],
  frecce: [
    { da: 'l1', a: 'l2', label: 'traduce in configurazioni osservabili' },
    { da: 'l2', a: 'l3', label: 'genera strumenti contestualizzati' },
    { da: 'l3', a: 'l4', label: 'consente validazione empirica' }
  ],
  nota: 'Questo schema vale per tutti i moduli del corso. F1 abita il Livello 1. Nei moduli M3–M7 vedremo come ciascun asse entra nel Livello 2 attraverso i Nodi e la Matrice.'
};

const ANNOTAZIONI_CASO_M2 = [
  {
    id: 'c1',
    estratto: 'Il bambino prende il libro, lo apre',
    assi_attivi: ['a1', 'a5'],
    annotazione: `A1: il corpo organizza l\'orientamento verso l\'oggetto prima di qualsiasi atto
      riflessivo. A5: c\'è già una direzione — non apre il libro a caso, ma come apertura verso
      una possibilità di scambio.`,
    nota_compresenza: 'Anche A2, A3, A6 sono attivi — ma A1 e A5 sono i più salienti in questo gesto.'
  },
  {
    id: 'c2',
    estratto: 'indica una figura, vocalizza qualcosa e guarda l\'adulto',
    assi_attivi: ['a2', 'a3', 'a6'],
    annotazione: `A2: il guardare l\'adulto è riconoscimento dell\'altro come soggetto. A3: l\'alternanza
      gesto-attesa rispetta una struttura di scambio con criteri impliciti. A6: la figura del libro
      diventa mediatore di mondo condiviso.`,
    nota_compresenza: 'A1 è la condizione di sfondo: senza A1, questo gesto complesso non sarebbe possibile.'
  },
  {
    id: 'c3',
    estratto: 'Il genitore nomina l\'immagine, sorride, aspetta',
    assi_attivi: ['a2', 'a3'],
    annotazione: `A2 (lato adulto): il genitore riconosce il bambino come soggetto che ha aperto
      uno scambio — non risponde al comportamento, risponde all\'intenzione. A3: l\'aspettare del
      genitore è la forma in cui la struttura normativa dello scambio viene rispettata e offerta
      come modello.`,
    nota_compresenza: 'Questo gesto adulto mostra come gli assi non descrivano solo il bambino, ma il campo relazionale.'
  },
  {
    id: 'c4',
    estratto: 'Il bambino torna a guardare il libro, gira pagina',
    assi_attivi: ['a4', 'a1'],
    annotazione: `A4: il libro ha un limite strutturale (pagine finite, non modificabili dal bambino).
      Il girare pagina è l\'incontro con questo limite — e la sua integrazione come struttura
      dell\'esperienza, non come ostacolo. A1: la continuità della sequenza si mantiene attraverso
      l\'interruzione.`,
    nota_compresenza: 'A5 è già orientato verso la prossima pagina: il limite diventa apertura.'
  },
  {
    id: 'c5',
    estratto: 'poi mostra un\'altra figura all\'adulto',
    assi_attivi: ['a5', 'a6'],
    annotazione: `A5: c\'è una nuova direzione — non ripetizione ma espansione verso una nuova
      possibilità di scambio. A6: il libro come oggetto culturale continua a fungere da mediatore
      di partecipazione al mondo condiviso.`,
    nota_compresenza: 'Tutti e sei gli assi sono attivi nella chiusura della sequenza: la scena è un esempio di compresenza totale.'
  }
];
```

---

## SLIDE 2.1 — Dimensioni, non fasi

**Tipo**: `standard`
**Titolo**: Dimensioni, non fasi
**Sottotitolo**: Un chiarimento che cambia tutto

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — Testo introduttivo breve (colonna singola, max 5 righe):

Prima di presentare i sei assi, è necessario chiarire cosa **non** sono. Tre parole vengono usate spesso come se fossero intercambiabili: *fase*, *competenza*, *dimensione strutturale*. Non lo sono. La confusione tra le tre produce strumenti fondati su presupposti sbagliati — anche quando il contenuto sembra simile.

**Sezione centrale** — Tre colonne affiancate, ciascuna con intestazione colorata:

**Colonna sinistra — Fase** (sfondo rosso tenue, chip rosso):
```
FASE
```
Un periodo dello sviluppo che si attraversa e si lascia alle spalle.
La fase orale, la fase senso-motoria, la fase di attaccamento ansioso.
*Si entra. Si supera. Si lascia.*

Una volta conclusa la fase, il bambino è diverso. Le fasi seguono una sequenza necessaria. Il bambino "è in" una fase: la fase lo descrive come posizione su una scala temporale.

**Colonna centrale — Competenza** (sfondo arancio tenue, chip arancio):
```
COMPETENZA
```
Un'abilità specifica che si acquisisce, si consolida e si può valutare.
Il pointing, la permanenza dell'oggetto, il linguaggio referenziale.
*Si acquisisce. Si consolida. Si misura.*

Una competenza ha soglie: attesa a una certa età, in ritardo se non compare. Il bambino "ha" o "non ha" una competenza: la competenza lo misura rispetto a una norma.

**Colonna destra — Asse strutturale** (sfondo viola tenue, chip viola `#6c63ff`):
```
ASSE STRUTTURALE
```
Una dimensione sempre attiva lungo tutto lo sviluppo.
Il modo in cui il bambino abita l'esperienza. Il riconoscimento dell'alterità. Il desiderio come direzione.
*Non si entra. Non si supera. Non si misura.*

Un asse non "arriva" e poi scompare — c'era prima ed è ancora qui. Non ha soglie normative. Il bambino non "è in" un asse: l'asse descrive una dimensione strutturale di ciò che sta vivendo.

**Sezione inferiore** — Callout a piena larghezza (sfondo `--color-primary-light`, bordo sinistro `#4a5568`):

*Gli assi strutturali di sviluppo sono dimensioni, non fasi. Non rappresentano tappe da attraversare né competenze da acquisire. Descrivono ciò che è strutturalmente in gioco nell'esperienza del bambino — in qualsiasi momento, in qualsiasi contesto.*

**Nota in footer**:
*La confusione più comune è con la "competenza": molti strumenti usano il termine "dimensione" per indicare ciò che è in realtà una competenza da valutare. La differenza si vede dalla domanda implicita: "il bambino ce la fa?" → competenza. "Come si organizza il campo?" → asse strutturale.*

---

## SLIDE 2.2 — La gerarchia strutturale

**Tipo**: `diagram`
**Titolo**: La gerarchia strutturale
**Sottotitolo**: Dipendenze logiche — non cronologiche, non valutative

**Contenuto principale**:

Visualizzazione verticale della gerarchia degli assi, costruita con il componente `PipelineAnimator` adattato. I dati vengono da `window.SEI_ASSI`.

**Schema visivo** (da rendere come grafo verticale interattivo):

```
  ┌─────────────────────────────────────────────────┐
  │  A1 — Ontologico-fenomenologico                 │  ← #6c63ff
  │  "Abitare l'esperienza"                         │
  │  Fondativo per tutti gli altri                  │
  └──────────────┬──────────────────────────────────┘
                 │ fonda
  ┌──────────────▼──────────────────────────────────┐
  │  A2 — Affettivo-morale                          │  ← #2d6a4f
  │  "Riconoscimento dell'alterità"                 │
  │  Presuppone A1                                  │
  └──────────────┬──────────────────────────────────┘
                 │ fonda
  ┌──────────────▼──────────────────────────────────┐
  │  A3 — Normativo-educativo                       │  ← #27ae60
  │  "Normatività emergente"                        │
  │  Presuppone A1, A2                              │
  └──────────────┬──────────────────────────────────┘
                 │ fonda
  ┌──────────────▼──────────────────────────────────┐
  │  A4 — Separazione e limite reale                │  ← #c0392b
  │  "Incontro con il reale"                        │
  │  Presuppone A1, A2, A3                          │
  └──────────────┬──────────────────────────────────┘
                 │ fonda
  ┌──────────────▼──────────────────────────────────┐
  │  A5 — Desiderio                                 │  ← #e67e22
  │  "Direzione dell'esperienza"                    │
  │  Presuppone A1, A4                              │
  └──────────────┬──────────────────────────────────┘
                 │ fonda (insieme agli altri)
  ┌──────────────▼──────────────────────────────────┐
  │  A6 — Mondo storico-culturale                   │  ← #d35400
  │  "Partecipazione al mondo condiviso"            │
  │  Presuppone tutti gli altri                     │
  └─────────────────────────────────────────────────┘
```

Ogni blocco è **cliccabile**: cliccando, appare a destra del diagramma un pannello che mostra:
- `nome` e `nome_breve` dell'asse
- `domanda_guida`
- `funzione_strutturale` (testo breve)
- Chip dei `dipendenze`: badge colorati degli assi che questo presuppone (vuoto per A1)

Al caricamento della slide, il pannello di **A1** è già aperto di default.

**Due note testuali fisse** — sotto il diagramma:

**Sinistra** (testo piccolo, `--color-text-muted`):
*La freccia indica dipendenza logica: A2 presuppone A1, non viceversa.*

**Destra** (testo piccolo, `--color-text-muted`):
*La gerarchia non è cronologica: tutti e sei gli assi sono attivi simultaneamente.*

**Nota in footer**:
*Una conseguenza pratica: un professionista che osserva A6 (partecipazione al mondo culturale) sta implicitamente presupponendo A1–A5 come condizioni di sfondo. Se A1 è fragile in quel campo, l'accesso a A6 sarà compromesso — indipendentemente dalle "competenze culturali" del bambino.*

---

## SLIDE 2.3 — Quattro proprietà degli assi

**Tipo**: `interactive`
**Titolo**: Quattro proprietà degli assi
**Sottotitolo**: Come funzionano nell'architettura del modello

**Contenuto principale**:

Quattro card espandibili disposte in griglia 2×2. Usa i dati da `QUATTRO_PROPRIETA`. Componente `ExpandableCards` con `multiOpen: true` — più card possono essere aperte contemporaneamente — e pulsante "Espandi tutto / Comprimi tutto" in alto a destra.

**Fronte di ogni card** (stato compatto):

```
[Numero grande in --color-accent: 1 / 2 / 3 / 4]
[Nome della proprietà in grassetto]
[Sommario — prima frase dal campo sommario]
[↓ Espandi]
```

**Card espansa** (aggiunge tre sezioni):

1. **Definizione completa** — testo dal campo `testo`
2. **Implicazione pratica** — testo dal campo `implicazione`, su sfondo `--color-primary-light`, etichetta: *"Cosa significa per gli strumenti"*
3. **Esempio concreto** — testo dal campo `esempio` in corsivo
4. **Test** — testo dal campo `test` in box separato: *"Domanda-test: [testo]"*, sfondo tenue, stile simile ai test-domanda di M03-F2

**Elemento sotto la griglia** — testo enfatizzato centrato:

*Le quattro proprietà non sono indipendenti: la compresenza dipende dalla dipendenza strutturale; la variabilità relativa è possibile perché gli assi sono strutture non esclusive. Il sistema funziona come insieme.*

**Nota in footer**:
*Queste quattro proprietà tornano in ogni modulo successivo come criteri impliciti: quando un modulo mostra come un asse si manifesta in un contesto specifico, sta operando all'interno della variabilità relativa (proprietà 3) e della non-esclusività disciplinare (proprietà 4).*

---

## SLIDE 2.4 — Asse vs. competenza: una distinzione critica

**Tipo**: `comparison`
**Titolo**: Asse e competenza non sono la stessa cosa
**Sottotitolo**: Una distinzione che cambia la forma degli strumenti

**Contenuto principale**:

Usa i dati da `CONFRONTO_ASSE_COMPETENZA`.

**Sezione superiore** — testo breve motivazionale (colonna singola):

Questa distinzione non è accademica. Molti strumenti usano il termine "dimensione dello sviluppo" per indicare ciò che è in realtà una competenza valutata su scala normativa. Il risultato: strumenti che *sembrano* leggere la struttura dello sviluppo ma che in realtà misurano prestazioni e producono punteggi. La confusione ha conseguenze dirette su cosa si osserva e cosa si restituisce.

**Sezione centrale** — tabella comparativa interattiva a 3 colonne:

Intestazioni: `Dimensione` | `Asse strutturale` | `Competenza`

Chip nelle intestazioni: `Asse` in viola `#6c63ff` | `Competenza` in grigio `#718096`

Ogni riga è costruita dai dati `CONFRONTO_ASSE_COMPETENZA.righe`. Le righe hanno hover con sfondo `--color-primary-light`. La riga con id `r6` (esempio concreto) ha sfondo leggermente diverso per segnalarne il ruolo di caso reale.

**Sezione inferiore** — callout a piena larghezza:

Box con bordo sinistro `#4a5568`, sfondo `--color-surface`:
Testo: campo `nota_finale` da `CONFRONTO_ASSE_COMPETENZA`

**Nota in footer**:
*Esercizio mentale: prendi qualsiasi strumento di valutazione dello sviluppo che hai usato. Chiedi: le sue "dimensioni" hanno soglie normative per età? Se sì, sono competenze — non assi strutturali. Il metodo non sostituisce quegli strumenti: costruisce un livello diverso, sopra e prima di essi.*

---

## SLIDE 2.5 — Panoramica: i sei assi

**Tipo**: `interactive`
**Titolo**: I sei assi strutturali
**Sottotitolo**: Panoramica d'insieme prima dell'approfondimento

**Contenuto principale**:

Tabella interattiva a 3 colonne usando i dati da `window.SEI_ASSI`. Ogni riga è espandibile. Componente `InteractiveMatrix` semplificata (una sola dimensione variabile: l'asse).

**Struttura della tabella**:

Intestazioni: `#` | `Asse` | `Domanda guida`

**Riga compatta** per ogni asse:

```
[Badge colorato: A1…A6]  |  [Nome asse in grassetto + nome_breve in small]  |  [domanda_guida in corsivo]
```

Il badge usa il `colore` dell'asse. Asse 1 ha un leggero sfondo colorato sull'intera riga per segnalarne il ruolo fondativo.

**Riga espansa** (click sulla riga): pannello a piena larghezza sotto la riga, con tre sezioni:

1. **Funzione strutturale** — testo dal campo `funzione_strutturale`
2. **Dipende da** — chip badge degli assi in `dipendenze` (oppure testo "Fondativo — non presuppone altri assi" per A1)
3. **Errore tipico** — testo dal campo `errore_tipico`, su sfondo rosso tenue con etichetta `⚠ Riduzione da evitare`

Una sola riga espansa alla volta.

**Sotto la tabella** — nota orientativa:

*I moduli M3–M7 approfondiranno ciascun asse (o coppia di assi) con le letture per contesto professionale, i concetti-ponte e il caso-guida. Questa panoramica è il punto di partenza: torna a questa slide se in un modulo successivo perdi il filo della gerarchia.*

**Nota in footer**:
*La domanda guida di ogni asse non è un indicatore da valutare: è la forma in cui l'asse diventa interrogabile da un professionista. Nei moduli successivi vedremo come da ciascuna domanda guida nascono domande professionali diverse nei contesti clinico, pedagogico, genitoriale e istituzionale.*

---

## SLIDE 2.6 — Come gli assi orientano gli strumenti

**Tipo**: `diagram`
**Titolo**: Dalla fondazione agli strumenti
**Sottotitolo**: La mediazione necessaria

**Contenuto principale**:

Visualizzazione verticale della catena di mediazione F1→F2→F3→Ricerca empirica. Usa i dati da `MEDIAZIONE_STRUMENTI`. Componente `PipelineAnimator`.

**Schema a quattro livelli**:

I quattro blocchi di `MEDIAZIONE_STRUMENTI.livelli` vengono visualizzati come nodi verticali connessi da frecce. Ogni freccia porta l'etichetta dal campo `label` in `MEDIAZIONE_STRUMENTI.frecce`.

Il blocco `l1` (Assi strutturali / F1) ha un bordo più spesso e il chip `← Siamo qui` in `--color-f1`. Il font del testo in `l1` è leggermente più grande degli altri.

Cliccando su ogni blocco, si apre un pannello laterale con il `descrizione` del livello.

**Sotto il diagramma** — tre chip in riga orizzontale centrati:

```
[FONDANO I VINCOLI]   →   [RENDONO LEGGIBILE]   →   [RENDONO POSSIBILE L'AZIONE]
```

Chip in formato pill, colorati rispettivamente in `--color-f1`, `--color-f2`, `--color-f3`.

**Box in basso** (sfondo `--color-primary-light`, bordo sinistro `#4a5568`):

La mediazione non è un limite tecnico del metodo: è una **garanzia metodologica**. Se gli assi si usassero direttamente come strumenti, la complessità ontologica dello sviluppo verrebbe sacrificata nella corsa alla misurabilità immediata. La mediazione impedisce che questo accada.

**Nota in footer**:
*Questa slide anticipa l'intero percorso F1→F2→F3. Nei moduli successivi di questo corso vedremo come gli assi si trasformano in condizioni di possibilità per i Nodi Trasversali di F2. Questa è la freccia che il corso F1 prepara: non ancora il passaggio, ma le fondamenta da cui il passaggio diventa possibile.*

---

## SLIDE 2.7 — Il caso-guida: quali assi sono attivi?

**Tipo**: `narrative`
**Titolo**: La scena e i sei assi
**Sottotitolo**: Una prima lettura strutturata

**Contenuto principale**:

Layout narrativo in due sezioni verticali.

**Sezione superiore** — La scena del caso-guida:

Card narrativa in corsivo, sfondo `--color-primary-light`, bordo sinistro `--color-primary`. Testo da `window.CASO_GUIDA_F1.scena`.

Sotto la card, testo piccolo in `--color-text-muted`:
*Il testo non cambia nei moduli successivi. Cambieranno le domande con cui lo guardiamo.*

**Sezione inferiore** — Griglia annotazioni:

Cinque card orizzontali compatte, una per ogni annotazione in `ANNOTAZIONI_CASO_M2`. Ogni card:

```
[Badge colorato degli assi attivi: es. A1 · A5]
[Estratto della scena in corsivo]
[Annotazione]
[Nota compresenza in piccolo, --color-text-muted]
```

I badge degli assi usano il `colore` da `window.SEI_ASSI`. La nota sulla compresenza è importante: mostra che anche gli altri assi non citati sono attivi, solo meno salienti.

**Sotto le card** — sezione di sintesi:

Titolo piccolo: *"In questa scena, sono attivi:"*

Sei badge colorati in riga (uno per asse), ognuno con il nome breve. **Tutti e sei** sono colorati normalmente — nessuno è "spento" o in grigio — a indicare la compresenza totale.

Sotto i badge, in testo leggermente più grande:
*Non è una scena "ricca di stimoli" — è una scena in cui tutte le dimensioni strutturali dello sviluppo sono leggibili. Questo è ciò che fa di essa un caso-guida efficace.*

**Chiusura del modulo** — badge e testo di orientamento:

Testo centrato, in `--color-text-muted`:
*Nei prossimi moduli, ciascun asse verrà approfondito singolarmente. Ogni volta torneremo su questa scena con una sola lente — senza dimenticare che le altre cinque sono sempre attive.*

Badge moduli successivi:
`→ Modulo 3 — Asse 1: Abitare l'esperienza`

**Nota in footer**:
*Questa lettura per annotazioni è volutamente incompleta: non è un'analisi esaustiva della scena. È un'introduzione alla pratica della lettura per assi — che verrà approfondita, asse per asse, nei moduli M3–M6.*

---

## Note per l'implementazione

### Slide 2.1 — Tre colonne e layout su schermi medi

Le tre colonne (Fase / Competenza / Asse) devono essere visibili affiancate su desktop 1280px+. Su schermi più piccoli, impilare verticalmente mantenendo l'ordine. La colonna destra (Asse strutturale) ha un bordo leggermente più spesso degli altri due (`border-width: 2px` vs `1px`) per segnalarne la posizione privilegiata senza didascalia aggiuntiva.

### Slide 2.2 — PipelineAnimator per la gerarchia

La gerarchia degli assi non è una pipeline operativa come quella di F2: non ha "controlli di coerenza" per ogni freccia. Le frecce indicano solo dipendenza logica. L'etichetta sulla freccia è sempre la stessa: *"presuppone"* — non serve variare.

Il pannello laterale (che appare cliccando un blocco) deve avere larghezza fissa circa 280px, posizionato a destra del diagramma senza spostarlo. Su schermi più stretti, il pannello appare sotto il diagramma invece che accanto.

**Dati per il PipelineAnimator** — costruire dall'array `window.SEI_ASSI` con questa mappatura:
```javascript
const stepsGerarchia = window.SEI_ASSI.map(asse => ({
  id: asse.id,
  label: `A${asse.numero} — ${asse.nome}`,
  sublabel: asse.nome_breve,
  type: asse.numero === 1 ? 'foundation' : 'axis',
  color: asse.colore,
  control: null,
  dipendenze: asse.dipendenze
}));
```

### Slide 2.3 — Griglia 2×2 delle proprietà

Le quattro card in griglia 2×2 (non in colonna come in M3-F2). Su desktop: due colonne. Su tablet e mobile: una colonna. Il pulsante "Espandi tutto / Comprimi tutto" ha posizione `sticky top` nell'area slide, così rimane visibile anche quando le card sono espanse e la slide si allunga verticalmente.

### Slide 2.5 — Tabella interattiva degli assi

La riga espansa si apre con animazione `slide-down` (200ms). Il pannello espanso è a piena larghezza della riga (non solo della cella): fa "sfondare" la struttura della tabella per dare respiro al contenuto. Chiude cliccando di nuovo sulla riga, o aprendo un'altra riga.

**Importante**: la riga di Asse 1 ha `background-color: var(--color-a1)` con opacità molto bassa (8-10%) anche in stato normale — non solo al click. Questo la distingue visivamente come fondativa senza testo aggiuntivo.

### Slide 2.6 — Nota sulla differenza con F2

In F2, il `PipelineAnimator` mostrava la pipeline degli operatori (7 step con controlli di coerenza). In F1 il componente viene usato per due scopi diversi:
1. In slide 2.2: gerarchia degli assi (frecce di dipendenza verticali)
2. In slide 2.6: catena di mediazione F1→F2→F3 (frecce di traduzione verticali)

La struttura del componente è la stessa. Cambia solo il `tipo` dei nodi (`foundation` / `axis` / `operator` / `output`) e il fatto che in 2.6 le frecce hanno etichette diverse. Assicurarsi che il componente supporti entrambi i contesti senza duplicare il codice.

### Slide 2.7 — Transizione verso M3

All'entrata nel Modulo 2, richiamare con una breve sovrapposizione (2-3 righe, dissolve dopo 2s) che collega questo modulo con M1: *"Nel Modulo 1 abbiamo stabilito che il bambino è un soggetto incarnato, temporale e relazionale. In questo modulo costruiamo le sei dimensioni strutturali di quella realtà."* Poi dissolve verso la slide 2.1.

### Costante globale `window.SEI_ASSI`

Questa costante deve essere definita in `app.js` — non nel file di modulo. Tutti i moduli successivi (M3–M7) la importeranno per costruire badge, chip di riferimento e pannelli. Definirla in `app.js` garantisce che sia disponibile prima del caricamento di qualsiasi modulo.

Se un modulo ha bisogno di estendere i dati di un asse specifico (es. M3 aggiunge concetti-ponte dettagliati per A1), lo fa con costanti locali nel proprio file JS — senza modificare `window.SEI_ASSI`.
