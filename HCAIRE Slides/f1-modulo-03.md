# Modulo 3 — Asse 1: Abitare l'esperienza
**Numero slide**: 8
**Colore accent**: `#1a6b8a`
**Tipo prevalente**: standard + narrative

---

## Dati globali del modulo

Definire in `f1_m03.js` le seguenti costanti. Estendono i dati di `window.SEI_ASSI[0]` senza modificarli.

```javascript
const ASSE_1_DETTAGLIO = {
  id: 'a1',
  nome: 'Ontologico-fenomenologico',
  domanda_guida: 'In che modo il bambino riesce ad abitare l\'esperienza che sta vivendo?',

  // Scomposizione del verbo chiave
  verbo_chiave: {
    parola: 'abitare',
    contrari: [
      {
        id: 'c1',
        parola: 'percepire',
        perche_insufficiente: `"Percepire" descrive il bambino come ricevitore passivo di stimoli
          dall\'esterno. Il bambino percepisce il libro. Ma "abitare" significa qualcosa di più:
          il bambino esiste nell\'esperienza del libro come in un luogo che lo contiene e che lui
          contribuisce a costruire. Non è un meccanismo di input — è un soggetto in un campo.`
      },
      {
        id: 'c2',
        parola: 'reagire',
        perche_insufficiente: `"Reagire" descrive il bambino come sistema di risposta a stimoli:
          la voce del genitore produce una risposta nel bambino. Ma "abitare" significa che il
          bambino non risponde dall\'esterno — è dentro l\'esperienza, ne è parte costitutiva.
          La reazione presuppone una separazione tra bambino e campo che "abitare" dissolve.`
      },
      {
        id: 'c3',
        parola: 'processare',
        perche_insufficiente: `"Processare" è il termine delle neuroscienze computazionali:
          il cervello del bambino processa l\'informazione sensoriale. Ma "abitare" significa
          che l\'esperienza non è un dato da elaborare — è un campo in cui si esiste.
          Il processamento avviene dentro un soggetto incarnato, non è il soggetto stesso.`
      },
      {
        id: 'c4',
        parola: 'subire',
        perche_insufficiente: `"Subire" descrive il bambino come passivo di fronte
          all\'esperienza: la visita pediatrica è qualcosa che gli capita. Ma "abitare"
          implica una forma di presenza attiva — anche fragile, anche disorganizzata —
          che è diversa dalla pura passività. Un bambino che piange e cerca il genitore
          non sta subendo: sta abitando quella difficoltà, anche se faticosamente.`
      }
    ],
    cosa_significa: `"Abitare" l\'esperienza significa esserci dentro come soggetto: il bambino
      non è davanti all\'esperienza né ne è travolto — la vive dall\'interno, contribuisce a
      darle forma, può abitarla più o meno pienamente a seconda di come è fatto il campo
      che lo circonda. L\'esperienza ha la struttura di un luogo in cui si dimora — non di
      un evento che accade.`
  },

  // Funzione fondativa rispetto agli altri assi
  fondazione: {
    testo: `Asse 1 ha funzione fondativa perché chiarisce che tipo di soggetto è il bambino
      prima di qualsiasi altra domanda. Senza questa chiarezza, tutti gli altri assi rischiano
      di descrivere funzioni di un organismo invece di dimensioni di un soggetto.`,
    senza_asse_1: [
      {
        asse: 'A2 — Affettivo-morale',
        cosa_diventa: 'Il riconoscimento dell\'altro diventa "risposta empatica" o "coordinazione comportamentale" — non riconoscimento tra soggetti.'
      },
      {
        asse: 'A3 — Normativo-educativo',
        cosa_diventa: 'La normatività emergente diventa "compliance a regole esterne" o "condizionamento" — non orientamento interno condiviso.'
      },
      {
        asse: 'A4 — Separazione e limite reale',
        cosa_diventa: 'L\'incontro con il limite diventa "regolazione emotiva" o "tolleranza alla frustrazione" — non discontinuità strutturale dell\'esperienza.'
      },
      {
        asse: 'A5 — Desiderio',
        cosa_diventa: 'Il desiderio diventa "preferenza" o "motivazione estrinseca" — non direzione dell\'esperienza di un soggetto.'
      },
      {
        asse: 'A6 — Mondo storico-culturale',
        cosa_diventa: 'La partecipazione culturale diventa "apprendimento di competenze culturali" o "esposizione a stimoli" — non co-costruzione di mondo condiviso.'
      }
    ]
  }
};

const TRE_DIMENSIONI_A1 = [
  {
    id: 'corpo',
    nome: 'Corpo',
    icona: '⬡',
    colore: '#1a6b8a',
    titolo: 'Il corpo come modo di essere nel mondo',
    testo: `Il bambino non usa il corpo per fare esperienza — è il corpo che fa esperienza.
      Il corpo non è lo strumento di un soggetto che sta altrove: è la condizione stessa
      dell\'esistenza del soggetto. La postura, il ritmo, il tono muscolare, il gesto
      non sono espressioni esterne di stati interni — sono il modo in cui il bambino
      è presente in quel campo, in quel momento.`,
    implicazione: `Osservare il bambino "attraverso" il corpo — cercandovi segnali di stati
      cognitivi o emotivi interni — è già una riduzione. Il corpo va osservato come il
      luogo in cui l\'esperienza si organizza, non come il mezzo attraverso cui si esprime.`,
    domanda_professionale: 'Come si organizza il corpo del bambino in questo campo? La postura apre o chiude verso l\'adulto? Il ritmo corporeo è regolato o frammentato?',
    esempio_caso: `Nella scena di lettura: la postura del bambino orientata verso il libro e
      verso l\'adulto non è un comportamento volontario — è il modo in cui il bambino è
      incarnato in quel campo di scambio. Il corpo organizza l\'intenzione prima che ci sia
      un\'intenzione esplicita.`
  },
  {
    id: 'relazione',
    nome: 'Relazione',
    icona: '⟺',
    colore: '#1a6b8a',
    titolo: 'La relazione come struttura dell\'esperienza',
    testo: `La relazione non è qualcosa che il bambino "ha" con l\'adulto: è la struttura
      stessa dell\'esperienza del bambino. Il campo relazionale non è lo sfondo su cui il
      bambino si muove — è la condizione che rende possibile l\'esperienza stessa. Senza
      un campo relazionale strutturato, l\'esperienza non si organizza — si frammenta.`,
    implicazione: `L\'osservazione rilevante non è mai "il bambino isolato": è sempre il bambino
      in un campo. La qualità del campo relazionale non è una variabile di contesto da
      controllare — è parte costitutiva dell\'oggetto di osservazione.`,
    domanda_professionale: 'Come è fatto il campo relazionale che circonda questo bambino in questo momento? Sostiene, amplifica o frammenta l\'esperienza?',
    esempio_caso: `Nella scena: il genitore che "aspetta" non è solo un comportamento dell\'adulto —
      è la forma in cui il campo relazionale si rende disponibile a ricevere l\'iniziativa del
      bambino. Senza questa disponibilità, il gesto del bambino cambia struttura.`
  },
  {
    id: 'mondo',
    nome: 'Mondo',
    icona: '◎',
    colore: '#1a6b8a',
    titolo: 'Il mondo come orizzonte di significato',
    testo: `Il bambino non percepisce un ambiente neutro di stimoli: abita un mondo già carico
      di significato. Il libro illustrato non è uno stimolo visivo — è un oggetto che porta
      con sé pratiche, convenzioni, storie. Il gesto del genitore non è un input comportamentale —
      è un atto che ha senso in un orizzonte culturale condiviso. L\'esperienza è sempre
      esperienza-in-un-mondo.`,
    implicazione: `Il "mondo" non è l\'insieme degli oggetti fisici presenti in una stanza.
      È l\'orizzonte di significato in cui l\'esperienza ha senso. Diversi campi relazionali
      producono mondi diversi per lo stesso bambino — e mondi diversi rendono accessibili
      esperienze diverse.`,
    domanda_professionale: 'Che tipo di mondo questo campo relazionale rende accessibile al bambino? È un mondo esplorabile, prevedibile, condivisibile?',
    esempio_caso: `Il libro nella scena non è neutro: è già un oggetto che appartiene a un mondo
      condiviso di pratiche di lettura, di nominazione, di scambio simbolico. Il bambino
      non "scopre" il libro — entra in un mondo in cui il libro ha già un senso.`
  }
];

const CONTINUITA_DISCONTINUITA = {
  titolo: 'L\'esperienza si mantiene — o si frammenta',
  introduzione: `Una delle manifestazioni più visibili di Asse 1 nel lavoro professionale
    è la capacità dell\'esperienza di mantenersi attraverso le discontinuità: interruzioni,
    cambiamenti, frustrazioni, transizioni. Un bambino il cui Asse 1 è ben sostenuto nel
    campo non riparte da zero ogni volta che qualcosa si interrompe — riprende il filo.
    Un bambino il cui Asse 1 è fragile in quel campo perde il filo: ogni interruzione
    è come ricominciare da capo.`,
  forme: [
    {
      id: 'f1',
      tipo: 'Continuità sostenuta',
      colore: '#27ae60',
      sfondo: '#eafaf1',
      descrizione: `L\'esperienza si mantiene attraverso le pause, le interruzioni, i cambiamenti.
        Il bambino può "tornare" a ciò che stava facendo dopo un\'interruzione. La traiettoria
        dell\'esperienza è riconoscibile nel tempo — non è una serie di episodi slegati.`,
      osservabile: `Il bambino riprende il gioco dopo che l\'adulto lo ha interrotto. Gira
        pagina e continua la sequenza della lettura. Dopo il pianto, torna alla situazione
        con qualcosa della situazione precedente ancora vivo.`,
      domanda: 'L\'esperienza ha un filo che si mantiene? Il bambino "riprende" o "ricomincia"?'
    },
    {
      id: 'f2',
      tipo: 'Continuità fragile',
      colore: '#f39c12',
      sfondo: '#fef9e7',
      descrizione: `L\'esperienza si mantiene con fatica: le interruzioni producono una rottura
        parziale, il ritorno è possibile ma richiede sostegno adulto. La traiettoria esiste
        ma dipende fortemente dalla disponibilità del campo a supportarla.`,
      osservabile: `Il bambino torna alla situazione solo se l\'adulto lo aiuta a ritrovarla.
        La sequenza si interrompe frequentemente e riprende con qualcosa di perso.
        Il campo deve "ricordare" per il bambino ciò che stava facendo.`,
      domanda: 'L\'esperienza riprende con sostegno adulto? Il campo compensa la fragilità della continuità?'
    },
    {
      id: 'f3',
      tipo: 'Continuità interrotta',
      colore: '#e74c3c',
      sfondo: '#fdecea',
      descrizione: `Le interruzioni producono una rottura: il bambino non riprende il filo, ogni
        episodio è separato dai precedenti. L\'esperienza non ha una traiettoria riconoscibile —
        è una serie di momenti slegati. Il campo non riesce a sostenere la continuità.`,
      osservabile: `Ogni interruzione azzera: il bambino non torna a ciò che stava facendo.
        La sequenza di scambio si dissolve a ogni pausa. Il campo non produce abbastanza
        struttura per sostenere la continuità dell\'esperienza.`,
      domanda: 'L\'esperienza si azzera a ogni interruzione? Il campo è abbastanza strutturato da sostenere la continuità?'
    }
  ],
  nota: `Le tre forme non sono diagnosi e non descrivono il bambino come individuo:
    descrivono la configurazione del campo in un momento specifico. Lo stesso bambino
    può mostrare continuità sostenuta al nido con l\'educatrice di riferimento e continuità
    interrotta durante la visita pediatrica. Il campo fa la differenza.`
};

const CINQUE_CONTESTI_A1 = [
  {
    id: 'ctx1',
    contesto: 'Ambulatorio pediatrico',
    colore: '#1a6b8a',
    domande_operative: [
      'Come si organizza l\'esperienza del bambino durante la visita? Il campo regge l\'intensità della situazione?',
      'Il bambino può "tornare" a una forma di disponibilità dopo la fase più invasiva della visita?',
      'Il genitore contribuisce a mantenere la continuità dell\'esperienza o aumenta la disorganizzazione?',
      'Cosa segnala il corpo del bambino sulla qualità dell\'esperienza in quel momento?'
    ],
    cosa_si_vede: `Il bambino che si irrigidisce durante lo spogliarsi, poi ritrova disponibilità
      quando il genitore parla piano — questo è Asse 1 in azione: il campo regge la discontinuità
      e permette la ripresa. Il bambino che rimane in uno stato di allerta per tutta la visita —
      anche dopo la parte invasiva — mostra un campo che non sostiene la ripresa.`,
    cosa_non_si_dice: 'Non: "il bambino è poco collaborativo" o "è ansioso". Sì: "il campo non sostiene la ripresa dell\'esperienza dopo la fase invasiva della visita".'
  },
  {
    id: 'ctx2',
    contesto: 'Nido / scuola dell\'infanzia',
    colore: '#2d6a4f',
    domande_operative: [
      'Il bambino abita lo spazio del nido o lo subisce? C\'è una presenza incarnata nel campo?',
      'L\'esperienza del bambino ha continuità durante la giornata o si frammenta nei passaggi?',
      'I momenti di transizione (ingresso, pasto, sonno) interrompono o strutturano l\'esperienza?',
      'L\'educatrice è parte del campo che sostiene l\'esperienza o è esterna a essa?'
    ],
    cosa_si_vede: `Il bambino che all\'ingresso riesce a "prendere il campo" — orientarsi nello
      spazio, riconoscere gli oggetti, ritrovare la propria posizione — mostra un Asse 1
      sostenuto dall\'ambiente. Il bambino che non riesce a "entrare" nel campo del nido dopo
      settimane mostra che il campo non ha ancora la struttura per rendersi abitabile.`,
    cosa_non_si_dice: 'Non: "il bambino ha difficoltà di inserimento" o "non si adatta". Sì: "il campo del nido non è ancora sufficientemente strutturato da permettere al bambino di abitarlo".'
  },
  {
    id: 'ctx3',
    contesto: 'Counseling genitoriale',
    colore: '#8e44ad',
    domande_operative: [
      'Il genitore percepisce il bambino come soggetto della propria esperienza — o come portatore di comportamenti da gestire?',
      'Il genitore è consapevole di essere parte del campo che struttura (o frammenta) l\'esperienza del bambino?',
      'La narrativa del genitore include il campo relazionale, o isola il bambino come unità di analisi?',
      'Cosa cambia nell\'esperienza del bambino quando cambia il modo in cui il genitore è presente?'
    ],
    cosa_si_vede: `Un genitore che descrive il figlio in termini di "fa questo / non fa quello"
      sta leggendo comportamenti, non esperienza. Un genitore che dice "quando mi avvicino così
      lui si calma" sta già leggendo il campo — è lì che si lavora. La domanda operativa
      per il counseling: come aiutare il genitore a diventare lettore del campo invece
      che gestore di comportamenti.`,
    cosa_non_si_dice: 'Non: "il genitore non capisce il bambino". Sì: "il genitore non ha ancora gli strumenti per leggere il campo relazionale come condizione dell\'esperienza del bambino".'
  },
  {
    id: 'ctx4',
    contesto: 'Supervisione d\'équipe',
    colore: '#d35400',
    domande_operative: [
      'Quando l\'équipe discute un bambino, sta descrivendo l\'esperienza del bambino o i suoi comportamenti?',
      'Il linguaggio dell\'équipe include il campo relazionale come parte dell\'oggetto di discussione?',
      'I professionisti si riconoscono come parte del campo che struttura l\'esperienza del bambino?',
      'Come cambia la lettura del caso se si sposta l\'attenzione dal bambino al campo?'
    ],
    cosa_si_vede: `Una supervisione che usa Asse 1 non discute "il bambino X": discute "il campo
      in cui X esiste in quel servizio". La differenza nel linguaggio è la differenza tra
      "X ha difficoltà di regolazione" e "il campo del servizio non produce le condizioni
      per cui X possa organizzare la propria esperienza". Il secondo apre possibilità
      di intervento; il primo le chiude.`,
    cosa_non_si_dice: 'Non: "questo bambino è difficile da gestire". Sì: "il campo del servizio non ha ancora trovato la forma per sostenere l\'esperienza di questo bambino".'
  },
  {
    id: 'ctx5',
    contesto: 'Ricerca sullo sviluppo',
    colore: '#4a5568',
    domande_operative: [
      'Il disegno di ricerca include il campo relazionale come variabile strutturale o solo come controllo?',
      'I costrutti misurati descrivono funzioni del bambino isolato o configurazioni del campo?',
      'Le procedure di osservazione permettono di leggere la qualità dell\'esperienza o solo la frequenza dei comportamenti?',
      'I risultati vengono attribuiti al bambino o alla configurazione campo-bambino-contesto?'
    ],
    cosa_si_vede: `La ricerca che usa Asse 1 come frame teorico produce disegni diversi: invece
      di misurare "la competenza di X in Y bambini", misura "la configurazione del campo in cui
      X emerge o non emerge". Il soggetto della ricerca non è il bambino — è la configurazione
      relazionale. Questo cambia il tipo di dati raccolti, le procedure di analisi e
      il tipo di conclusioni possibili.`,
    cosa_non_si_dice: 'Non: "i bambini del gruppo X mostrano maggiore Y". Sì: "nei campi relazionali con le caratteristiche Z, l\'esperienza Y risulta più accessibile".'
  }
];

const CONCETTI_PONTE_A1 = {
  asse: 'A1 — Ontologico-fenomenologico',
  colore: '#1a6b8a',
  introduzione: `Asse 1 non appartiene a nessuna disciplina specifica: attraversa tutte le discipline
    che si occupano dello sviluppo. Ogni disciplina ha i propri concetti-ponte — termini che, nel
    proprio linguaggio, si avvicinano a ciò che Asse 1 descrive. Conoscerli serve a riconoscere
    quando una disciplina sta "parlando di Asse 1" senza dirlo esplicitamente — e a tradurre
    tra linguaggi diversi senza perdere la struttura.`,
  discipline: [
    {
      id: 'd1',
      nome: 'Psicologia dello sviluppo',
      colore: '#6c63ff',
      concetti_ponte: [
        {
          termine: 'Senso di sé nucleare (Stern)',
          connessione: `Il "senso di sé nucleare" di Stern — l\'esperienza preriflessiva di essere
            un agente con un corpo, un affetto e una continuità nel tempo — è la descrizione
            più vicina a Asse 1 nella letteratura psicologica. Non è identico all\'asse
            (che è più ampio e strutturale), ma la direzione è la stessa.`,
          rischio_riduzione: 'Ridurre Asse 1 a "senso di sé" come costrutto psicologico individuale, perdendo la dimensione relazionale e corporea costitutiva.'
        },
        {
          termine: 'Soggettività emergente',
          connessione: `La soggettività emergente non è una competenza che si acquisisce ma una
            struttura che si organizza progressivamente nel campo relazionale. Vicina ad Asse 1,
            ma il rischio è trattarla come tappa piuttosto che come dimensione sempre attiva.`,
          rischio_riduzione: 'Fare della soggettività una tappa dello sviluppo ("il bambino acquisisce la soggettività") invece di una struttura sempre in organizzazione.'
        }
      ]
    },
    {
      id: 'd2',
      nome: 'Pediatria',
      colore: '#1a6b8a',
      concetti_ponte: [
        {
          termine: 'Qualità della presenza',
          connessione: `Il pediatra che descrive "un bambino presente" o "un bambino che non c\'è"
            sta usando un linguaggio che si avvicina ad Asse 1: la presenza non è un comportamento
            misurabile, è una qualità dell\'abitare il campo. È un concetto clinico informale
            ma strutturalmente pertinente.`,
          rischio_riduzione: 'Trattare la "qualità della presenza" come indicatore di un deficit neurologico specifico invece che come lettura della configurazione del campo.'
        },
        {
          termine: 'Regolazione fisiologica nel contesto relazionale',
          connessione: `La ricerca sulla regolazione fisiologica in contesto relazionale (variabilità
            della frequenza cardiaca, cortisolo, sistemi di risposta allo stress) si avvicina
            ad Asse 1 quando include il campo relazionale come variabile strutturale — non solo
            come moderatore.`,
          rischio_riduzione: 'Ridurre la regolazione a parametri fisiologici senza includere il campo relazionale come condizione costitutiva.'
        }
      ]
    },
    {
      id: 'd3',
      nome: 'Neuropsichiatria infantile',
      colore: '#8e44ad',
      concetti_ponte: [
        {
          termine: 'Integrazione sensoriale (Ayres)',
          connessione: `Il framework dell\'integrazione sensoriale descrive come il sistema nervoso
            organizza le informazioni sensoriali per produrre risposte adattive. Si avvicina
            ad Asse 1 nella misura in cui descrive l\'organizzazione dell\'esperienza — ma
            resta dentro un paradigma di processamento individuale, senza il campo relazionale.`,
          rischio_riduzione: 'Confondere Asse 1 con integrazione sensoriale: il primo descrive l\'abitare l\'esperienza in un campo relazionale; il secondo descrive il processamento sensoriale del sistema nervoso individuale.'
        },
        {
          termine: 'Organizzazione dell\'esperienza soggettiva',
          connessione: `In NPI clinica, la distinzione tra "bambino che organizza l\'esperienza"
            e "bambino frammentato nell\'esperienza" è un giudizio clinico fondamentale che
            precede qualsiasi diagnosi. Questo è esattamente il livello di Asse 1 —
            anche se raramente viene reso esplicito come tale.`,
          rischio_riduzione: 'Saltare dalla frammentazione dell\'esperienza a una diagnosi senza passare per la lettura del campo relazionale che produce o non produce quella frammentazione.'
        }
      ]
    },
    {
      id: 'd4',
      nome: 'Pedagogia / Educazione',
      colore: '#27ae60',
      concetti_ponte: [
        {
          termine: 'Abitabilità dell\'ambiente educativo',
          connessione: `La domanda pedagogica "questo ambiente è abitabile per questo bambino?"
            è una traduzione diretta di Asse 1 nel contesto educativo. L\'abitabilità
            dell\'ambiente non è una proprietà dello spazio fisico: è la qualità del campo
            relazionale che quell\'ambiente produce.`,
          rischio_riduzione: 'Trattare l\'abitabilità come problema di arredamento o di stimolazione sensoriale, perdendo la dimensione relazionale costitutiva.'
        },
        {
          termine: 'Partecipazione vs. esecuzione',
          connessione: `La distinzione tra un bambino che "partecipa" e un bambino che "esegue"
            è una lettura implicita di Asse 1: partecipare significa abitare l\'esperienza
            dell\'attività dal proprio interno; eseguire significa produrre comportamenti
            richiesti dall\'esterno senza abitarli.`,
          rischio_riduzione: 'Valutare la partecipazione come comportamento osservabile (alza la mano, risponde alle domande) invece che come qualità dell\'esperienza.'
        }
      ]
    },
    {
      id: 'd5',
      nome: 'Neuroscienze',
      colore: '#c0392b',
      concetti_ponte: [
        {
          termine: 'Embodied cognition',
          connessione: `Il paradigma dell\'embodied cognition afferma che la cognizione non avviene
            "nel cervello" separato dal corpo, ma è strutturata dalla corporalità del soggetto
            e dalla sua interazione con l\'ambiente. È la traduzione neuroscientifica più vicina
            alla dimensione "incarnato" di Asse 1.`,
          rischio_riduzione: 'Ridurre l\'embodied cognition a "il corpo influenza la cognizione" invece di "il corpo è la condizione dell\'esperienza" — perdendo la radicalità della proposta.'
        },
        {
          termine: 'Predictive processing e interoception',
          connessione: `Il framework del predictive processing descrive come il cervello costruisce
            modelli predittivi del proprio stato corporeo e del mondo. L\'interoception —
            la percezione degli stati corporei interni — è un correlato neuroscientifica
            di quello che Asse 1 descrive come "abitare incarnato". Ma il framework resta
            dentro un paradigma di processamento individuale.`,
          rischio_riduzione: 'Identificare Asse 1 con un meccanismo neurale (interoception, predictive processing) invece che con la struttura dell\'esperienza soggettiva del bambino-in-campo.'
        }
      ]
    }
  ]
};

const ERRORI_TIPICI_A1 = [
  {
    id: 'e1',
    tipo: 'Riduzione a deficit specifico',
    colore: '#e74c3c',
    descrizione: `La riduzione più comune: una difficoltà nell\'organizzazione dell\'esperienza
      viene interpretata come deficit di una funzione specifica — disturbo dell\'attenzione,
      difficoltà di processamento sensoriale, ritardo cognitivo.`,
    esempio_errato: '"Il bambino non riesce a stare fermo durante la visita: potrebbe esserci un disturbo dell\'attenzione."',
    lettura_strutturale: '"Il campo della visita pediatrica non produce le condizioni per cui questo bambino possa organizzare la propria esperienza: il carico sensoriale e relazionale è troppo alto rispetto alle risorse di regolazione disponibili nel campo."',
    cosa_si_perde: `Si perde il campo: la difficoltà viene attribuita al bambino come caratteristica
      stabile, invece di essere letta come configurazione situata. La conseguenza è che
      l\'intervento si orienta verso il bambino (trattamento del disturbo) invece che verso
      il campo (modifica delle condizioni che rendono l\'esperienza difficile da abitare).`
  },
  {
    id: 'e2',
    tipo: 'Riduzione comportamentale',
    colore: '#e67e22',
    descrizione: `L\'esperienza del bambino viene tradotta direttamente in comportamenti osservabili
      e misurabili: frequenza, durata, intensità. La qualità dell\'esperienza — la sua forma
      interna, la sua continuità, il suo orientamento — scompare.`,
    esempio_errato: '"Il bambino ha mostrato 3 episodi di pianto della durata media di 2 minuti durante la visita."',
    lettura_strutturale: '"Il campo della visita ha prodotto tre momenti di disorganizzazione dell\'esperienza; in due dei tre il bambino ha ripreso disponibilità dopo la risposta del genitore; nel terzo la disorganizzazione è rimasta per tutto il resto della visita."',
    cosa_si_perde: `Si perde la struttura dell\'esperienza: i tre episodi diventano equivalenti
      (sono tutti "pianto") invece di essere diversi per qualità (il primo ha una ripresa,
      il terzo no). La continuità — che è esattamente ciò che Asse 1 chiede — diventa invisibile.`
  },
  {
    id: 'e3',
    tipo: 'Riduzione cognitiva',
    colore: '#8e44ad',
    descrizione: `L\'abitare l\'esperienza viene ridotto a funzione cognitiva: attenzione,
      memoria, esecutivo centrale. Il corpo, la relazione e il mondo — le tre dimensioni
      di Asse 1 — diventano variabili di sfondo rispetto al "funzionamento cognitivo".`,
    esempio_errato: '"Il bambino mostra buona attenzione sostenuta e memoria di lavoro adeguata per l\'età."',
    lettura_strutturale: '"Il bambino abita il campo del nido con continuità nelle situazioni di scambio diadico con l\'adulto; la continuità si frammenta nei momenti di attività di gruppo non strutturata."',
    cosa_si_perde: `Si perde la situazionalità: le "funzioni cognitive" appaiono come proprietà
      stabili del bambino, mentre la lettura strutturale rivela che la stessa "funzione"
      varia radicalmente a seconda del campo. Questa variabilità è l\'informazione più utile
      per il professionista.`
  },
  {
    id: 'e4',
    tipo: 'Moralizzazione',
    colore: '#2c3e50',
    descrizione: `La difficoltà nell\'abitare l\'esperienza viene trasformata in una valutazione
      morale del bambino o del genitore: il bambino "non si impegna", "non vuole collaborare";
      il genitore "non gestisce bene", "non mette limiti".`,
    esempio_errato: '"Il bambino durante la visita non collabora e il genitore non riesce a contenerlo."',
    lettura_strutturale: '"Il campo della visita produce una disorganizzazione dell\'esperienza che il bambino non riesce ad abitare; il campo relazionale disponibile (genitore + pediatra) non trova nell\'immediato la forma per sostenere la ripresa."',
    cosa_si_perde: `Si perde completamente la dimensione strutturale: le difficoltà diventano
      tratti di personalità o mancanze di volontà. La conseguenza pratica è che nessuna
      delle persone presenti — bambino, genitore, pediatra — si sente in grado di fare
      qualcosa di diverso. La lettura strutturale, al contrario, apre possibilità di modifica
      del campo.`
  }
];

// Scena annotata per il componente AnnotatedScene (M3-specifica: solo lente Asse 1)
const SCENE_HTML_M3 = `<p>Durante un bilancio di salute, il pediatra propone per alcuni minuti
una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi.
È presente un genitore. Sul tavolo c'è un piccolo libro illustrato
con immagini semplici: animali, oggetti familiari, figure umane.</p>
<p><span class="annotabile" data-annotation-id="m3-a1">Il bambino prende il libro, lo apre,</span>
guarda alcune immagini,
<span class="annotabile" data-annotation-id="m3-a2">indica una figura, vocalizza qualcosa</span>
e guarda l'adulto.
<span class="annotabile" data-annotation-id="m3-a3">Il genitore nomina l'immagine, sorride, aspetta.</span>
<span class="annotabile" data-annotation-id="m3-a4">Il bambino torna a guardare il libro, gira pagina,</span>
poi
<span class="annotabile" data-annotation-id="m3-a5">mostra un'altra figura all'adulto.</span></p>`;

const ANNOTAZIONI_M3 = [
  {
    id: 'm3-a1',
    label: 'Corpo che abita',
    colore: '#1a6b8a',
    annotazione: `Il prendere e l\'aprire non sono atti motori separati dall\'esperienza:
      sono il modo incarnato in cui il bambino si orienta verso quel campo. Il corpo
      organizza l\'apertura verso l\'oggetto-mondo prima che ci sia un\'intenzione esplicita
      formulabile. Questo è il bambino che abita, non che "usa" il libro.`,
    asse: 'A1 — Corpo come modo di essere'
  },
  {
    id: 'm3-a2',
    label: 'Esperienza in atto',
    colore: '#1a6b8a',
    annotazione: `Il gesto di indicare e la vocalizzazione non sono due comportamenti separati
      (motorio + comunicativo): sono un unico atto dell\'esperienza incarnata. Il bambino
      non "indica" e poi "vocalizza" — è in una configurazione corporea-relazionale che
      produce gesto e voce insieme come forma dell\'abitare quel campo.`,
    asse: 'A1 — Corpo, relazione, mondo intrecciati'
  },
  {
    id: 'm3-a3',
    label: 'Campo che sostiene',
    colore: '#1a6b8a',
    annotazione: `"Aspetta" è il modo in cui il campo relazionale si struttura per sostenere
      la continuità dell\'esperienza del bambino. L\'aspettare del genitore non è un
      comportamento passivo: è la forma attiva con cui il campo si rende disponibile
      a ricevere l\'esperienza del bambino invece di sovrapporsi ad essa.`,
    asse: 'A1 — Campo relazionale come condizione'
  },
  {
    id: 'm3-a4',
    label: 'Continuità del filo',
    colore: '#1a6b8a',
    annotazione: `"Torna a guardare" — non ricomincia da zero. L\'esperienza ha un filo che
      si mantiene attraverso lo scambio con l\'adulto. Il girare pagina è un atto di
      continuità dell\'esperienza: il bambino riprende il campo del libro dopo la parentesi
      relazionale con l\'adulto. Questo è Asse 1 visibile come continuità.`,
    asse: 'A1 — Continuità dell\'esperienza'
  },
  {
    id: 'm3-a5',
    label: 'Traiettoria aperta',
    colore: '#1a6b8a',
    annotazione: `"Un\'altra figura" — non la stessa. La traiettoria dell\'esperienza si apre
      verso qualcosa di nuovo. Il bambino non è saturato, non è nel loop: ha una direzione
      che lo porta verso una nuova possibilità di scambio. La traiettoria è aperta —
      e il campo è strutturato abbastanza da sostenerla.`,
    asse: 'A1 — Traiettoria aperta dell\'esperienza'
  }
];
```

---

## SLIDE 3.1 — Perché Asse 1 fonda tutti gli altri

**Tipo**: `standard`
**Titolo**: Il fondamento del fondamento
**Sottotitolo**: Perché Asse 1 viene prima di tutti gli altri

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — testo introduttivo (colonna singola):

Testo dal campo `ASSE_1_DETTAGLIO.fondazione.testo`. Poi, su riga separata, in grassetto e con sfondo `--color-primary-light`:

*Senza Asse 1, gli altri cinque assi descrivono funzioni di un organismo — non dimensioni di un soggetto.*

**Sezione centrale** — cinque card orizzontali compatte, una per ciascuna voce di `ASSE_1_DETTAGLIO.fondazione.senza_asse_1`:

Ogni card:
```
[Badge colorato: A2 / A3 / A4 / A5 / A6]
[Nome asse]
[cosa_diventa — in corsivo, testo che mostra cosa succede senza A1]
```

Sfondo di ogni card: leggerissimo rosso tenue. Il badge usa il colore dell'asse corrispondente da `window.SEI_ASSI`. La formula ricorrente in ogni card è la stessa: *"senza A1, [nome asse] diventa…"* — il pattern crea ritmo e riconoscibilità.

**Sezione inferiore** — diagramma a dipendenze semplificato:

Visualizzazione compatta (non il PipelineAnimator completo — quello è in M2): un blocco centrale `A1` con frecce che escono verso `A2`, `A3`, `A4`, `A5`, `A6`. Le frecce non puntano verso A1 — A1 fonda, non dipende. Sotto ogni asse satellite: in microtype, il colore del relativo asse.

Il titolo del diagramma in piccolo: *"A1 è condizione logica di tutti gli altri — non precede gli altri nel tempo: li fonda nella struttura."*

**Nota in footer**:
*La dipendenza strutturale non significa che A1 venga "prima" nello sviluppo del bambino. Significa che qualsiasi osservazione che usa A2, A3, A4, A5 o A6 sta presupponendo A1 — anche quando non lo dice. Questo modulo rende esplicita quella presupposizione.*

---

## SLIDE 3.2 — La domanda guida

**Tipo**: `narrative`
**Titolo**: La domanda guida di Asse 1
**Sottotitolo**: Prima di capire cosa fa il bambino, chiediamoci come lo fa

**Contenuto principale**:

Layout a colonna singola. Grande domanda centrale con scomposizione interattiva del verbo chiave.

**Elemento principale** — grande blockquote centrato (font `--text-3xl`, `--leading-relaxed`):

> *"In che modo il bambino riesce ad abitare l'esperienza che sta vivendo?"*

Bordo sinistro spesso in `#1a6b8a`. Sfondo `--color-primary-light` tenue.

**Sotto la domanda** — separatore — istruzione interattiva:

Testo piccolo centrato in `--color-text-muted`:
*"Abitare" non è una metafora decorativa. Clicca sulla parola per vedere da cosa si distingue.*

**Parola `"abitare"` nel testo della domanda**: resa come `<span class="parola-chiave">abitare</span>` con sottolineatura punteggiata in `#1a6b8a`. Cliccandola, si apre il pannello dei contrari.

**Pannello dei contrari** (appare sotto la domanda con slide-down, 200ms):

Quattro mini-card affiancate in griglia 2×2, una per ogni voce di `ASSE_1_DETTAGLIO.verbo_chiave.contrari`. Ogni mini-card:

```
[Parola in grigio barrata: "percepire" / "reagire" / "processare" / "subire"]
[perche_insufficiente — testo completo]
```

Le parole sono "barrate" visivamente (non con `<del>` HTML, ma con uno stile che le posiziona come superate — colore `--color-text-muted`, dimensione leggermente ridotta, senza effetto strikethrough testuale che sarebbe confusivo).

**Sotto le quattro mini-card** — a piena larghezza — il significato di "abitare":

Box con sfondo `--color-primary-light`, bordo sinistro `#1a6b8a`, padding generoso:

**Cos'è "abitare" l'esperienza**
Testo: campo `ASSE_1_DETTAGLIO.verbo_chiave.cosa_significa`

**Nota in footer**:
*La domanda guida non è un indicatore da rispondere sì/no: è un orientamento dell\'osservazione. Non esiste un bambino che "non abita" la propria esperienza — esistono campi che rendono l\'abitare più o meno possibile, più o meno continuo, più o meno sostenuto. La domanda chiede come — non se.*

---

## SLIDE 3.3 — Corpo, relazione, mondo

**Tipo**: `diagram`
**Titolo**: Tre dimensioni intrecciate
**Sottotitolo**: Non tre componenti separati — un unico nodo strutturale

**Contenuto principale**:

Layout a due colonne (40% / 60%).

**Colonna sinistra** — diagramma visivo:

Tre cerchi parzialmente sovrapposti in disposizione triangolare (diagramma di Venn a tre insiemi), ciascuno colorato in `#1a6b8a` con opacità diversa:
- `Corpo` (cerchio in alto a sinistra)
- `Relazione` (cerchio in alto a destra)
- `Mondo` (cerchio in basso al centro)

L'intersezione centrale dei tre cerchi — l'area dove si sovrappongono tutti e tre — è l'area di Asse 1: colorata piena in `#1a6b8a`, con testo sovrapposto in bianco: *"Abitare l'esperienza"*.

Ogni cerchio è cliccabile: cliccando, il pannello a destra cambia per mostrare la dimensione corrispondente.

Sotto il diagramma, testo piccolo centrato:
*Le tre dimensioni non si "combinano": sono sempre già intrecciate. Separarle analiticamente (come fa questa slide) è una semplificazione necessaria — non una descrizione della realtà.*

**Colonna destra** — pannello di dettaglio (cambia al click sul diagramma):

Pannello default: mostra il testo introduttivo del triangolo:

*Asse 1 descrive il bambino come soggetto incarnato, temporale e relazionale. Queste tre parole non sono aggettivi indipendenti: descrivono un unico modo di esistere nel mondo. Clicca sui tre cerchi per esplorare ciascuna dimensione.*

Pannello per `Corpo` (click sul cerchio "Corpo"):
- Titolo: `TRE_DIMENSIONI_A1[0].titolo`
- Testo: `TRE_DIMENSIONI_A1[0].testo`
- Implicazione: `TRE_DIMENSIONI_A1[0].implicazione` (sfondo tenue, bordo sinistro)
- Domanda professionale: `TRE_DIMENSIONI_A1[0].domanda_professionale` (in corsivo)

Identica struttura per `Relazione` e `Mondo` con i dati corrispondenti.

**Nota in footer**:
*Il diagramma di Venn è un'approssimazione utile ma imprecisa: suggerisce che le tre dimensioni siano separate con zone di sovrapposizione. In realtà Asse 1 descrive qualcosa di più radicale: non ci sono tre dimensioni che si sovrappongono — c'è un unico modo di essere soggetto che è sempre già incarnato, relazionale e nel-mondo. La separazione analitica serve all'apprendimento, non alla descrizione.*

---

## SLIDE 3.4 — Continuità e discontinuità dell'esperienza

**Tipo**: `interactive`
**Titolo**: L'esperienza si mantiene — o si frammenta
**Sottotitolo**: La continuità come manifestazione principale di Asse 1 nel lavoro professionale

**Contenuto principale**:

Layout a colonna singola.

**Sezione superiore** — testo introduttivo:
Testo: campo `CONTINUITA_DISCONTINUITA.introduzione`

**Sezione centrale** — tre card orizzontali affiancate, una per ciascuna forma in `CONTINUITA_DISCONTINUITA.forme`:

Ogni card ha intestazione colorata (verde / arancio / rosso secondo il `colore` della forma), sfondo corrispondente, e struttura:

```
[Intestazione colorata: tipo]
[descrizione]
─────────────────────────────
[etichetta: "Come si vede"]
[osservabile in corsivo]
─────────────────────────────
[etichetta: "Domanda operativa"]
[domanda in grassetto]
```

Le tre card hanno larghezza uguale. Su hover la card si solleva leggermente (shadow più pronunciata). Nessuna espansione — il contenuto è già tutto visibile.

**Separatore** — sotto le card, in `--color-text-muted`, centrato:

Frecce che indicano la direzione possibile del campo:
```
Continuità sostenuta  ←→  Continuità fragile  ←→  Continuità interrotta
```
Le frecce ←→ indicano che la direzione dipende dal campo, non dal bambino. Il campo può spostarsi in entrambe le direzioni.

**Sezione inferiore** — box a piena larghezza con bordo sinistro `#f39c12`:

Testo: campo `CONTINUITA_DISCONTINUITA.nota`

**Nota in footer**:
*La continuità dell\'esperienza è visibile nel lavoro professionale senza strumenti specialistici: basta spostare l\'attenzione dai comportamenti del bambino alla traiettoria dell\'esperienza. "Il bambino riprende?" è la domanda più semplice e più informativa che Asse 1 suggerisce.*

---

## SLIDE 3.5 — Come si manifesta professionalmente

**Tipo**: `interactive`
**Titolo**: Asse 1 nei cinque contesti professionali
**Sottotitolo**: Le stesse domande — linguaggi diversi

**Contenuto principale**:

Cinque card espandibili verticali usando il componente `ExpandableCards` con `multiOpen: false`. Usa i dati da `CINQUE_CONTESTI_A1`.

**Fronte di ogni card** (compatto):

```
[Badge colorato con nome contesto]
[Domanda principale dal primo elemento di domande_operative]
[↓ Espandi per le domande complete e l'esempio]
```

Il badge usa il `colore` del contesto. I badge hanno un'icona piccola: 🩺 ambulatorio | 🏫 nido | 👥 counseling | 👁 supervisione | 🔬 ricerca.

**Card espansa**:

Sezione 1 — *"Domande operative"* (etichetta piccola):
Lista puntata di tutte le voci di `domande_operative`. Bullets in `#1a6b8a`.

Sezione 2 — *"Come si legge in questo contesto"* (etichetta piccola, sfondo `--color-primary-light`):
Testo dal campo `cosa_si_vede` in testo normale.

Sezione 3 — *"Guardrail linguistico"* (etichetta piccola, sfondo rosso tenue / verde tenue a due colonne):
Colonna sinistra — bordo rosso: testo `cosa_non_si_dice` (la parte "Non:...")
Colonna destra — bordo verde: testo `cosa_non_si_dice` (la parte "Sì:...")

**Sotto le cinque card** — testo centrato, `--color-text-secondary`:

*Asse 1 non cambia passando da un contesto all\'altro. Cambia il linguaggio in cui le domande vengono poste, il tipo di situazione in cui si manifestano, il tipo di risposta professionale che diventano possibili.*

**Nota in footer**:
*Le cinque domande operative per contesto non sono un elenco da memorizzare: sono esempi del tipo di domanda che Asse 1 genera. Il professionista che ha interiorizzato Asse 1 produce domande simili spontaneamente — senza bisogno di consultare un elenco.*

---

## SLIDE 3.6 — Concetti-ponte nei linguaggi disciplinari

**Tipo**: `interactive`
**Titolo**: Asse 1 nei linguaggi delle discipline
**Sottotitolo**: Come ogni disciplina si avvicina a Asse 1 — e dove rischia di perderlo

**Contenuto principale**:

Usa i dati da `CONCETTI_PONTE_A1`. Layout a due sezioni verticali.

**Sezione superiore** — testo introduttivo:
Campo `CONCETTI_PONTE_A1.introduzione` (2-3 righe, centrato).

**Sezione centrale** — accordion verticale a cinque voci, una per disciplina:

Ogni voce accordion ha un'intestazione cliccabile:

```
[Chip colorato con nome disciplina]   [▶ / ▼]
```

Il colore del chip è il `colore` della disciplina in `CONCETTI_PONTE_A1.discipline`.

**Sezione espansa** per ogni disciplina: due sotto-card affiancate (una per `concetti_ponte`):

Ogni sotto-card:
```
[termine in grassetto, colore disciplina]
───────────────────────────────────────
[connessione — testo che spiega il legame con Asse 1]
───────────────────────────────────────
[⚠ Rischio di riduzione]
[rischio_riduzione — in testo rosso tenue]
```

Una sola disciplina aperta alla volta (accordion standard). Al caricamento, nessuna disciplina è aperta: l'utente sceglie da dove iniziare.

**Sotto l'accordion** — box a piena larghezza (sfondo `--color-primary-light`):

*I concetti-ponte non sono sinonimi di Asse 1: sono traduzioni parziali in linguaggi disciplinari specifici. Il loro valore è pratico: permettono al professionista di riconoscere quando la propria disciplina sta "parlando di Asse 1" — e di tenere presente la struttura più ampia che il proprio linguaggio non cattura completamente.*

**Nota in footer**:
*Ogni disciplina ha le proprie riduzione caratteristiche: la pediatria tende alla riduzione normativa (nella norma / fuori norma), la NPI alla riduzione diagnostica (segnali di allerta / profilo di rischio), la pedagogia alla riduzione funzionale (livello di partecipazione / competenza). Asse 1 non elimina questi linguaggi — fornisce un livello strutturale da cui possono confrontarsi.*

---

## SLIDE 3.7 — L'errore tipico

**Tipo**: `interactive`
**Titolo**: Quattro riduzioni da riconoscere
**Sottotitolo**: Cosa si perde quando Asse 1 viene ignorato

**Contenuto principale**:

Quattro card espandibili in griglia 2×2, usando i dati da `ERRORI_TIPICI_A1`. Componente `ExpandableCards` con `multiOpen: false`.

**Fronte di ogni card** (compatto):

```
[Chip rosso con tipo di riduzione]
[Prima frase di descrizione]
[↓ Vedi esempio e lettura alternativa]
```

Tutti i chip hanno sfondo rosso tenue con il `colore` specifico della card. Il fronte non è allarmante: è sobrio, descrittivo.

**Card espansa**:

Sezione 1 — *"Descrizione"*:
Campo `descrizione` completo.

Sezione 2 — *"Esempio di formulazione riduttiva"* (bordo sinistro rosso, sfondo rosso tenue):
Campo `esempio_errato` in corsivo, preceduto da `⚠`.

Sezione 3 — *"Lettura strutturale alternativa"* (bordo sinistro verde, sfondo verde tenue):
Campo `lettura_strutturale` in corsivo, preceduto da `✓`.

Sezione 4 — *"Cosa si perde"* (sfondo `--color-primary-light`, bordo sinistro `#1a6b8a`):
Campo `cosa_si_perde`.

**Elemento sotto la griglia** — testo centrato, `--text-lg`:

*Nessuna di queste formulazioni riduttive è "sbagliata" in assoluto: sono linguaggi professionali competenti che servono a scopi precisi. Diventano riduzioni quando sono l'unica lettura disponibile — quando non c'è un livello strutturale da cui partire.*

**Nota in footer**:
*Il riconoscimento delle riduzioni non serve a criticare i colleghi di altre discipline: serve a riconoscere i propri automatismi linguistici. Ogni professionista ha le proprie riduzioni caratteristiche, legate al proprio training e ai propri strumenti. Asse 1 non le elimina — le rende visibili.*

---

## SLIDE 3.8 — Il caso-guida letto attraverso Asse 1

**Tipo**: `narrative`
**Titolo**: La scena di lettura — vista da Asse 1
**Sottotitolo**: Come cambia la domanda quando si abita il framework

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — `AnnotatedScene`:

Usa il componente `AnnotatedScene` con:
- `sceneHtml`: `SCENE_HTML_M3`
- `annotations`: `ANNOTAZIONI_M3`
- `container`: elemento DOM della sezione

Istruzione iniziale sopra la scena (testo piccolo, centrato, `--color-text-muted`):
*Clicca sulle frasi evidenziate per leggere la scena attraverso Asse 1*

Ogni annotazione mostra il badge `A1 — [label]` in `#1a6b8a` + testo + `asse` in piccolo.

**Sezione inferiore** — confronto esplicito:

Titolo piccolo centrato: *"La stessa scena — due domande diverse"*

Due card affiancate, stessa struttura di M1 slide 1.6:

**Card sinistra** — *"Senza Asse 1"*:
```
"Il bambino di 20 mesi mostra pointing, vocalizzazione e attenzione condivisa
adeguati all'età. La qualità dello scambio con il genitore è buona."
```
Chip sotto: `prestazionale` · `individuale` · `normativa implicita`

**Card destra** — *"Con Asse 1"*:
```
"Il bambino abita il campo della lettura con continuità: il corpo è orientato verso
il libro e verso l'adulto, il filo dell'esperienza si mantiene attraverso lo scambio,
la traiettoria è aperta verso nuove possibilità. Il campo relazionale sostiene l'abitare."
```
Chip sotto: `strutturale` · `configurazionale` · `descrive il campo`

**Chiusura** — testo centrato, `--color-text-secondary`:

*Nel Modulo 4 aggiungeremo a questa lettura le lenti di Asse 2 e Asse 3: vedremo come la stessa scena rivela altri strati strutturali quando si guarda al riconoscimento dell\'alterità e alla normatività emergente dello scambio.*

Badge modulo successivo: `→ Modulo 4 — Assi 2 e 3: Alterità e normatività`

**Nota in footer**:
*Questa è la prima volta che il componente AnnotatedScene viene usato in modalità "monodisciplinare": tutte le annotazioni sono lette solo attraverso Asse 1. Nel Modulo 7, la stessa scena verrà riletta con tutti e sei gli assi insieme — come chiusura dell\'intero percorso di F1.*

---

## Note per l'implementazione

### Slide 3.2 — Parola cliccabile nel blockquote

Il testo della domanda guida contiene la parola `"abitare"` resa come `<span class="parola-chiave" data-target="panel-abitare">abitare</span>`. Il pannello dei contrari ha `id="panel-abitare"` ed è nascosto di default (`hidden`). Al click sulla parola: il pannello appare con `slide-down` (200ms) e la parola riceve la classe `parola-chiave--attiva` (sfondo colorato leggero). Al click di nuovo: il pannello si chiude.

Il pannello dei contrari deve rimanere nella slide — non in overlay. Si inserisce subito dopo il blockquote della domanda, in modo che la slide si allunghi verticalmente quando è aperto. Nessun scroll forzato: l'utente vede il pannello apparire sotto la domanda.

### Slide 3.3 — Diagramma di Venn interattivo

Il diagramma non richiede librerie esterne: può essere costruito in SVG inline. I tre cerchi sono `<circle>` SVG con riempimento `#1a6b8a` e opacità progressiva (0.15 / 0.20 / 0.25). L'intersezione centrale è un'area `<path>` riempita piena.

Ogni cerchio ha un `<text>` SVG sovrapposto con il nome della dimensione. I cerchi sono cliccabili con `cursor: pointer`. Il pannello di dettaglio a destra cambia contenuto con una transizione breve (`fade`, 150ms) al click.

Dimensioni suggerite: viewBox `0 0 300 280`, cerchi di raggio 100px, centri a circa (-60, -40), (+60, -40), (0, +60) rispetto al centro del viewBox.

### Slide 3.4 — Le tre card affiancate

Le tre card `Continuità sostenuta / fragile / interrotta` hanno altezza fissa eguale per l'intestazione colorata. Il contenuto interno può variare in altezza — allineare le card in alto, non centrare verticalmente.

**Importante**: le tre forme non hanno hover che le rende cliccabili — non portano a pannelli aggiuntivi. Sono descrittive, non interattive. L'unica interazione è il gentle lift on hover (shadow).

### Slide 3.5 — Accordion vs. ExpandableCards

In questa slide la struttura è un accordion verticale semplice (non le card espandibili di M2 o M3-F2): cinque voci in lista, ognuna con intestazione cliccabile. L'accordin è verticale — non a griglia. Questo perché i cinque contesti hanno contenuto testuale lungo e richiedono spazio verticale, non una griglia orizzontale compatta.

### Slide 3.6 — Accordion discipline

Identica struttura all'accordion di 3.5, con cinque discipline. Le sotto-card dei concetti-ponte all'interno di ogni disciplina sono affiancate (due colonne) su desktop, impilate su mobile.

### Slide 3.8 — AnnotatedScene: solo lente Asse 1

In M3, il componente `AnnotatedScene` viene usato con sole 5 annotazioni, tutte leggenti la scena attraverso Asse 1. Questo è diverso dall'uso in M1 (dove le annotazioni coprivano le tre dimensioni del soggetto) e dall'uso futuro in M7 (dove tutte le lenti saranno presenti insieme). Claude Code deve assicurarsi che il componente sia configurabile per mostrare badge di colore uniforme (`#1a6b8a`) in questa slide — non i colori per asse del sistema globale.

### Transizione M2 → M3

All'entrata nel Modulo 3, brevissima sovrapposizione (fade out dopo 2s):
*"Nel Modulo 2 abbiamo visto la gerarchia degli assi come sistema. Ora entriamo nel primo — quello che fonda tutti gli altri. La domanda è semplice: come abita il bambino l\'esperienza che sta vivendo?"*
