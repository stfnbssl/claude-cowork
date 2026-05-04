# Modulo 4 — Assi 2 e 3: Alterità e normatività
**Numero slide**: 7
**Colore accent**: `#2d6a4f`
**Tipo prevalente**: standard + comparison

---

## Nota sul titolo del modulo

Il titolo operativo di questo modulo — *"Alterità e normatività implicite nell'alternanza dei turni"* — indica il fenomeno osservabile che funge da filo conduttore: il turn-taking della scena di lettura condivisa. È lì che Asse 2 e Asse 3 diventano contemporaneamente visibili: il bambino che guarda l'adulto cercando un soggetto che risponda (A2), e la struttura implicita dello scambio che nessuno ha imposto ma che entrambi rispettano (A3). Il titolo nel corso può essere abbreviato in *"Assi 2 e 3 — Alterità e normatività"*.

---

## Dati globali del modulo

Definire in `f1_m04.js` le seguenti costanti.

```javascript
const ASSE_2_DETTAGLIO = {
  id: 'a2',
  nome: 'Affettivo-morale',
  domanda_guida: 'Come riconosce il bambino l\'altro come portatore di un\'esperienza propria?',

  // Tre modalità di relazione che precedono il riconoscimento
  modalita_pre_riconoscimento: [
    {
      id: 'fusione',
      nome: 'Fusione',
      colore: '#e74c3c',
      sfondo: '#fdecea',
      descrizione: `L\'altro non ha ancora un'esperienza separata dalla propria: l\'adulto
        è un prolungamento del bambino, un'estensione del suo campo di azione.
        Non c\'è ancora "un altro" — c\'è un campo indistinto in cui il bambino è il centro.`,
      osservabile: `Il bambino tratta l\'adulto come se dovesse rispondere automaticamente
        a ogni suo stato: non cerca conferma, non aspetta risposta — si aspetta sincronia
        immediata. Quando la sincronia non arriva, il campo collassa.`,
      asse: null
    },
    {
      id: 'uso',
      nome: 'Uso',
      colore: '#e67e22',
      sfondo: '#fef3e2',
      descrizione: `L\'altro è riconosciuto come distinto — ma come strumento, non come soggetto.
        Il bambino usa l\'adulto per raggiungere un fine: lo trascina, lo indica, lo orienta.
        C\'è già distinzione, ma non ancora riconoscimento dell\'esperienza interna dell\'altro.`,
      osservabile: `Il bambino si avvicina all\'adulto quando ha bisogno di qualcosa e si allontana
        quando lo ha ottenuto. Lo sguardo è funzionale: cerca la mano, non il volto.
        L\'adulto è mezzo, non interlocutore.`,
      asse: null
    },
    {
      id: 'riconoscimento',
      nome: 'Riconoscimento',
      colore: '#2d6a4f',
      sfondo: '#d8f3dc',
      descrizione: `L\'altro è riconosciuto come portatore di un\'esperienza propria: ha un\'interno,
        una prospettiva, una risposta che non è automatica ma è sua. Il bambino cerca l\'adulto
        non per usarlo ma per condividere qualcosa con lui — con un soggetto che avrà
        la propria reazione a ciò che viene condiviso.`,
      osservabile: `Il bambino guarda il volto dell\'adulto, non solo la mano. Aspetta la risposta —
        non la mera esecuzione. Modifica il proprio comportamento in base all\'espressione
        dell\'adulto, non solo alla sua azione. Cerca conferma, non solo assistenza.`,
      asse: 'A2 — Affettivo-morale'
    }
  ],

  // La non-fusionalità come conquista strutturale
  non_fusionalita: {
    definizione: `La non-fusionalità non è freddezza, distanza o autonomia precoce.
      È la capacità di mantenere una relazione con qualcuno che ha un\'esperienza propria —
      diversa dalla propria — senza che questa differenza distrugga il campo.
      È la condizione per qualsiasi relazione che non sia fusione o uso.`,
    perche_conta: `Un bambino che non ha ancora sviluppato la non-fusionalità non può
      tollerare che l\'adulto abbia una prospettiva diversa dalla propria: ogni disaccordo
      è vissuto come abbandono o tradimento. Un bambino con non-fusionalità consolidata
      può vivere la differenza dell\'altro come una risorsa — qualcosa che arricchisce
      il campo invece di minacciarlo.`,
    errore_comune: `Confondere la non-fusionalità con l\'autonomia: un bambino
      "autonomo" può essere semplicemente in modalità "uso" — tratta l\'adulto come
      strumento efficiente. La non-fusionalità riguarda la qualità della relazione,
      non la quantità di dipendenza.`
  },

  // Come A2 dipende da A1
  dipendenza_da_a1: `Solo un soggetto incarnato può riconoscere un altro soggetto incarnato.
    Asse 2 presuppone Asse 1: se il bambino non abita la propria esperienza come soggetto,
    non può riconoscere nell\'altro un soggetto con la propria esperienza. La relazione
    tra i due assi non è solo logica — è fenomenologica: è attraverso il proprio corpo
    in relazione che il bambino incontra il corpo dell\'altro come soggetto.`,

  // Domande professionali per contesto
  domande_per_contesto: {
    clinico: [
      'Il bambino cerca il volto dell\'adulto o solo la sua mano/voce come strumento?',
      'Quando l\'adulto ha una risposta diversa dalle attese, il bambino la registra o la ignora?',
      'Il bambino modifica il proprio comportamento in base all\'espressione del genitore?',
      'C\'è curiosità per l\'esperienza dell\'altro o solo richiesta di risposta funzionale?'
    ],
    pedagogico: [
      'Il bambino riconosce i compagni come soggetti con esperienze proprie?',
      'Il conflitto tra pari viene gestito come scontro tra volontà o come incontro di prospettive?',
      'L\'educatrice è cercata come soggetto o usata come regolatore di accesso alle risorse?',
      'Il bambino mostra interesse per l\'esperienza interna degli altri (cosa sente, cosa vede)?'
    ],
    genitoriale: [
      'Il genitore percepisce il bambino come soggetto con un\'esperienza propria o come sistema da gestire?',
      'Il bambino cerca nel genitore una risposta soggettiva o solo una risposta funzionale?',
      'Il disaccordo tra bambino e genitore produce rottura o dialogo tra prospettive diverse?',
      'Il genitore riesce a mantenere la propria esperienza separata da quella del bambino?'
    ]
  },

  guardrail: `Nessun output derivato da Asse 2 può descrivere la relazione in termini di
    coordinazione di comportamenti tra bambino e adulto, senza includere la dimensione
    dell\'esperienza soggettiva di entrambi come campo condiviso.`
};

const ASSE_3_DETTAGLIO = {
  id: 'a3',
  nome: 'Normativo-educativo',
  domanda_guida: 'Come emerge la capacità di orientare l\'azione secondo criteri condivisi?',

  // Emergenza interna vs. norma esterna
  emergenza: {
    significato: `"Emergenza" non è metafora: descrive un processo strutturale preciso.
      La normatività emerge quando il bambino non segue semplicemente una regola imposta
      dall\'esterno — sviluppa internamente la capacità di orientare la propria azione
      secondo criteri che sono condivisi con l\'altro. Non è apprendimento di regole:
      è costituzione interna di un orientamento.`,
    differenza_chiave: `Una norma esterna può essere seguita per obbedienza, paura o abitudine.
      La normatività emergente viene dal bambino: è la capacità di voler fare le cose
      "nel modo giusto" — non perché qualcuno lo impone, ma perché il bambino ha interiorizzato
      la struttura dello scambio con l\'altro come campo normativo. È la condizione
      per la responsabilità — non il suo risultato.`,
    non_e: [
      'Non è obbedienza: seguire regole imposte dall\'esterno per evitare conseguenze.',
      'Non è conformità: adattarsi al comportamento degli altri per accettazione sociale.',
      'Non è apprendimento di norme: memorizzare cosa è permesso e cosa non lo è.',
      'Non è morale: il giudizio su ciò che è bene o male è un livello successivo.'
    ]
  },

  // Le tre forme di normatività emergente
  tre_forme: [
    {
      id: 'scambio',
      nome: 'Criteri dello scambio',
      descrizione: `La struttura implicita dell\'interazione: chi parla quando, chi aspetta,
        chi inizia. Il bambino che impara a "non interrompere" o a "aspettare il proprio turno"
        non sta solo imparando una regola: sta sviluppando internamente un senso del ritmo
        dello scambio come campo normativo condiviso.`,
      esempio: `Nella scena di lettura: il bambino indica → aspetta → l\'adulto risponde → il bambino riprende.
        Nessuno ha insegnato al bambino questo schema: è emerso dall\'interno dello scambio stesso,
        reso possibile dal campo relazionale che lo sosteneva.`,
      visibile_quando: 'Il bambino aspetta spontaneamente la risposta dell\'adulto prima di continuare — senza che gli venga chiesto di aspettare.'
    },
    {
      id: 'oggetti',
      nome: 'Criteri di spazio e oggetti',
      descrizione: `L\'orientamento verso ciò che è "di chi" e "come si trattano le cose".
        Non le regole esplicite di proprietà, ma il senso emergente che gli oggetti hanno
        una posizione in un campo condiviso — e che modificarli ha conseguenze per l\'altro.`,
      esempio: `Il bambino che restituisce spontaneamente un oggetto all\'altro bambino —
        non perché l\'adulto lo dice, ma perché ha sviluppato il senso che quell\'oggetto
        appartiene a quel campo condiviso — mostra A3 in azione.`,
      visibile_quando: 'Il bambino modifica il proprio comportamento sugli oggetti in risposta all\'espressione (non alla parola) dell\'altro.'
    },
    {
      id: 'significato',
      nome: 'Criteri di significato condiviso',
      descrizione: `La normatività più sottile: il bambino orienta la propria azione secondo
        ciò che "conta" nel campo condiviso. Non solo cosa si fa, ma come si fa in un modo
        che sia riconoscibile e valido per l\'altro. Il bambino inizia a fare le cose "come si fanno"
        — non per imitazione, ma perché ha sviluppato un senso interno della forma corretta.`,
      esempio: `Il bambino che usa il cucchiaio in modo riconoscibile — non come strumento qualsiasi
        ma come "cucchiaio" con la sua forma culturale di uso — mostra A3 nell\'incontro con
        il mondo storico-culturale (che poi diventa A6).`,
      visibile_quando: 'Il bambino si corregge spontaneamente quando la propria azione non corrisponde alla forma attesa — senza intervento dell\'adulto.'
    }
  ],

  // Dipendenze strutturali
  dipendenze_strutturali: `Asse 3 presuppone sia Asse 1 sia Asse 2. Non si può sviluppare
    la capacità di orientare l\'azione secondo criteri condivisi senza: (a) abitare la propria
    esperienza come soggetto — Asse 1 — perché i criteri devono essere interiorizzati
    da un soggetto, non solo eseguiti da un organismo; (b) riconoscere l\'altro come portatore
    di esperienza propria — Asse 2 — perché i criteri sono condivisi con qualcuno che ha
    la propria prospettiva sul "modo giusto" di fare le cose.`,

  domande_per_contesto: {
    clinico: [
      'Il bambino mostra orientamento verso la struttura dello scambio (aspetta, risponde, riprende)?',
      'Quando la struttura dello scambio si rompe, il bambino la registra come rottura o come evento neutro?',
      'Il bambino mostra segnali di auto-correzione — si accorge quando fa qualcosa "nel modo sbagliato"?',
      'La normatività che emerge è coerente tra contesti diversi o è specifica del campo familiare?'
    ],
    pedagogico: [
      'Le regole del gruppo sono vissute dai bambini come criteri condivisi o come imposizioni esterne?',
      'Il bambino mostra orientamento verso i criteri della situazione — come si usano le cose, come ci si tratta?',
      'I conflitti normativi (cosa è giusto fare) generano dialogo o solo scontro?',
      'Il bambino propone, corregge, negozia regole — o le segue/non segue passivamente?'
    ],
    genitoriale: [
      'I limiti del genitore sono vissuti dal bambino come criteri relazionali o come ostacoli?',
      'Il bambino mostra auto-regolazione normativa — si ferma prima che il genitore intervenga?',
      'La normatività del bambino è presente anche quando il genitore non guarda?',
      'Il "no" del bambino è una forma di normatività emergente o solo opposizione?'
    ]
  },

  guardrail: `Nessun output derivato da Asse 3 può contenere giudizi di valore sul rispetto
    o mancato rispetto di norme da parte del bambino. La domanda non è se il bambino obbedisce —
    è come si sta organizzando la normatività nel campo relazionale.`
};

const NORMA_VS_NORMATIVITA = {
  intestazione: 'Norma imposta e normatività emergente non sono la stessa cosa',
  sottotitolo: 'La differenza cambia l\'oggetto di osservazione e il tipo di intervento possibile',
  dimensioni: [
    {
      id: 'd1',
      aspetto: 'Origine',
      norma_esterna: 'Viene dall\'esterno: l\'adulto definisce cosa è permesso e cosa no.',
      normativita_emergente: 'Emerge dall\'interno del campo relazionale: il bambino sviluppa internamente un orientamento verso criteri condivisi.'
    },
    {
      id: 'd2',
      aspetto: 'Motivazione',
      norma_esterna: 'Si segue per obbedienza, paura delle conseguenze o ricerca di approvazione.',
      normativita_emergente: 'Si segue perché il bambino ha interiorizzato la struttura dello scambio come campo con i propri criteri.'
    },
    {
      id: 'd3',
      aspetto: 'Cosa si osserva',
      norma_esterna: 'Il comportamento del bambino: si adegua o non si adegua alla norma.',
      normativita_emergente: 'La qualità del campo: come si stanno organizzando i criteri condivisi tra bambino e adulto.'
    },
    {
      id: 'd4',
      aspetto: 'Cosa si chiede al professionista',
      norma_esterna: 'Stabilire, comunicare e far rispettare le norme.',
      normativita_emergente: 'Creare le condizioni di campo in cui la normatività possa emergere dall\'interno.'
    },
    {
      id: 'd5',
      aspetto: 'Conseguenza se assente',
      norma_esterna: 'Il bambino "non rispetta le regole" — intervento disciplinare.',
      normativita_emergente: 'Il campo non produce le condizioni perché la normatività emerga — riflessione sul campo relazionale.'
    },
    {
      id: 'd6',
      aspetto: 'Esempio nel caso-guida',
      norma_esterna: 'Nessuno — nella scena non si vedono norme imposte. Il libro non ha regole d\'uso esplicite.',
      normativita_emergente: 'Il bambino aspetta la risposta dell\'adulto prima di girare pagina: nessuno gliel\'ha chiesto — è emerso dall\'interno dello scambio.'
    }
  ],
  nota_finale: `La distinzione non è che la norma esterna sia sbagliata e la normatività
    emergente sia giusta. In molti contesti le norme esterne sono necessarie e utili.
    La distinzione riguarda l\'oggetto di osservazione: Asse 3 guarda alla normatività emergente —
    quella che il bambino sviluppa dall\'interno del campo. Se il professionista vede solo
    la norma esterna, perde di vista questo livello.`
};

const CONNESSIONE_A2_A3 = {
  titolo: 'Perché A3 dipende da A2',
  tesi: `I criteri condivisi di Asse 3 sono condivisi con qualcuno. Quel qualcuno deve essere
    riconosciuto come soggetto con la propria esperienza — Asse 2. Senza il riconoscimento
    dell\'altro come portatore di esperienza propria, i "criteri condivisi" diventano
    regole di coordinazione — non normatività emergente.`,
  senza_a2: {
    titolo: 'Senza Asse 2: coordinazione, non normatività',
    descrizione: `Un bambino che segue le regole di scambio senza riconoscere l\'altro come
      soggetto con la propria esperienza non sta sviluppando normatività: sta apprendendo
      la forma esteriore dello scambio senza la sua struttura interna. È la differenza
      tra "so che bisogna aspettare il turno" e "aspetto perché l\'altro ha qualcosa
      da dire che è suo".`,
    esempi_clinici: [
      `Il bambino che aspetta il turno in modo meccanico — senza guardare l\'adulto, senza
        registrare la risposta — mostra la forma di A3 senza il sostegno di A2.
        La struttura dello scambio è rispettata, ma non c\'è incontro tra soggetti.`,
      `Il bambino che si adegua alle regole del gruppo per evitare conflitti — senza mostrare
        interesse per l\'esperienza degli altri — mostra compliance (norma esterna)
        senza normatività emergente (A3) e senza riconoscimento dell\'alterità (A2).`
    ]
  },
  con_a2: {
    titolo: 'Con Asse 2: normatività come incontro di soggetti',
    descrizione: `Quando A2 è presente, i criteri condivisi hanno una qualità diversa:
      sono criteri condivisi con qualcuno che ha la propria prospettiva. Aspettare il turno
      non è seguire una regola — è fare spazio all\'altro perché l\'altro ha qualcosa di suo
      da portare. La normatività emerge dall\'interno del riconoscimento reciproco.`,
    esempi_clinici: [
      `Il bambino che aspetta guardando il volto dell\'adulto — registrando la risposta,
        modificando il proprio comportamento in base a essa — mostra A2 e A3 intrecciati:
        il riconoscimento dell\'altro come soggetto sostiene la struttura normativa dello scambio.`,
      `Nella scena di lettura: il bambino indica, guarda l\'adulto, aspetta. L\'attesa
        non è meccanica: il bambino guarda il volto del genitore, aspettando una risposta
        soggettiva — non una conferma automatica. A2 e A3 sono simultanei.`
    ]
  },
  freccia_visiva: 'A2 (riconoscimento) → rende possibile → A3 (normatività emergente come incontro di soggetti)'
};

const ERRORI_TIPICI_A2_A3 = [
  {
    id: 'e1',
    asse: 'A2',
    tipo: 'Riduzione all\'empatia',
    colore: '#e74c3c',
    descrizione: `Asse 2 viene ridotto alla "capacità empatica" del bambino: leggere le emozioni
      degli altri, condividere gli stati affettivi, mostrare preoccupazione per chi piange.
      L\'empatia è una manifestazione possibile di A2 — ma A2 è più strutturale: riguarda
      il riconoscimento dell\'altro come soggetto con un\'esperienza propria, indipendentemente
      dal contenuto emotivo di quella esperienza.`,
    esempio_errato: '"Il bambino mostra buona empatia: consola il compagno che piange."',
    lettura_strutturale: '"Il bambino riconosce nel compagno un soggetto con un\'esperienza propria (la sofferenza) e vi risponde — questo è il livello strutturale di A2 di cui l\'empatia è una manifestazione situata."',
    cosa_si_perde: `La riduzione all\'empatia rende A2 dipendente dal contenuto emotivo visibile:
      si osserva solo quando c\'è un\'emozione esplicita da leggere. Ma A2 è attivo anche
      quando non c\'è emozione evidente — nella qualità ordinaria dello scambio, nel modo
      in cui il bambino cerca la risposta soggettiva dell\'adulto durante la lettura del libro.`
  },
  {
    id: 'e2',
    asse: 'A2',
    tipo: 'Riduzione alla compliance sociale',
    colore: '#e67e22',
    descrizione: `Il riconoscimento dell\'altro viene ridotto al comportamento socialmente adeguato:
      il bambino che saluta, che condivide i giocattoli, che aspetta il turno. Ma questi comportamenti
      possono essere prodotti anche senza il riconoscimento dell\'altro come soggetto —
      per apprendimento, per imitazione, per evitamento del conflitto.`,
    esempio_errato: '"Il bambino ha buone abilità sociali: saluta, condivide, aspetta il turno."',
    lettura_strutturale: '"Il bambino mostra comportamenti socialmente adeguati — ma A2 chiede qualcosa di più: il bambino cerca nell\'altro una risposta soggettiva o solo una risposta funzionale? Guarda il volto o solo la mano?"',
    cosa_si_perde: `La riduzione alle abilità sociali fa scomparire la domanda strutturale di A2:
      non "cosa fa il bambino con gli altri" ma "come il bambino abita il campo relazionale
      con gli altri" — se c\'è riconoscimento reciproco o solo coordinazione di comportamenti.`
  },
  {
    id: 'e3',
    asse: 'A3',
    tipo: 'Riduzione all\'obbedienza',
    colore: '#2c3e50',
    descrizione: `La normatività emergente viene ridotta al rispetto delle regole: il bambino
      "obbedisce" o "non obbedisce". Ma obbedienza e normatività emergente sono strutturalmente
      diversi: l\'obbedienza può avvenire senza nessuna interiorizzazione — il bambino esegue
      perché c\'è una conseguenza. La normatività emergente viene dall\'interno.`,
    esempio_errato: '"Il bambino rispetta le regole del gruppo e obbedisce alle indicazioni dell\'educatrice."',
    lettura_strutturale: '"La domanda di A3 non è se il bambino obbedisce — è se sta sviluppando internamente un orientamento verso i criteri condivisi del campo. Si corregge da solo? Si accorge quando la struttura dello scambio si rompe? Propone soluzioni normative?"',
    cosa_si_perde: `La riduzione all\'obbedienza sposta l\'intervento sul bambino (rinforzo del comportamento
      corretto) invece che sul campo (creazione delle condizioni perché la normatività emerga
      dall\'interno). Le conseguenze pratiche sono opposte.`
  },
  {
    id: 'e4',
    asse: 'A3',
    tipo: 'Moralizzazione',
    colore: '#8e44ad',
    descrizione: `La normatività emergente viene trasformata in una valutazione morale del bambino
      o del genitore. Il bambino "è educato" o "non ha limiti". Il genitore "mette limiti" o
      "non riesce a gestire". Asse 3 non valuta: descrive come si sta organizzando la normatività
      nel campo relazionale, senza giudicare nessuna delle persone coinvolte.`,
    esempio_errato: '"Il bambino non ha limiti: il genitore non riesce a gestirlo."',
    lettura_strutturale: '"Il campo non produce le condizioni per cui la normatività possa emergere dall\'interno: i criteri non sono condivisi, il bambino non li ha ancora interiorizzati come propri. La domanda è: cosa nel campo impedisce questo processo?"',
    cosa_si_perde: `La moralizzazione chiude il caso: il bambino "è così" e il genitore "non sa fare".
      La lettura strutturale lo riapre: quali condizioni del campo possiamo modificare
      perché la normatività possa emergere?`
  }
];

// Scena annotata per AnnotatedScene (lente A2 + A3)
const SCENE_HTML_M4 = `<p>Durante un bilancio di salute, il pediatra propone per alcuni minuti
una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi.
È presente un genitore. Sul tavolo c'è un piccolo libro illustrato
con immagini semplici: animali, oggetti familiari, figure umane.</p>
<p>Il bambino prende il libro, lo apre, guarda alcune immagini,
<span class="annotabile" data-annotation-id="m4-a1">indica una figura, vocalizza qualcosa
e guarda l'adulto.</span>
<span class="annotabile" data-annotation-id="m4-a2">Il genitore nomina l'immagine, sorride, aspetta.</span>
<span class="annotabile" data-annotation-id="m4-a3">Il bambino torna a guardare il libro,</span>
<span class="annotabile" data-annotation-id="m4-a4">gira pagina,</span>
poi
<span class="annotabile" data-annotation-id="m4-a5">mostra un'altra figura all'adulto.</span></p>`;

const ANNOTAZIONI_M4 = [
  {
    id: 'm4-a1',
    label: 'Cerca il soggetto',
    colore: '#2d6a4f',
    annotazione: `"Guarda l\'adulto" — non guarda la mano, non guarda dove sta andando, non
      guarda il risultato dell\'azione. Guarda il volto. È la domanda di A2 in azione:
      il bambino cerca nell\'adulto un soggetto che abbia la propria risposta all\'immagine
      indicata — non un\'eco, non una macchina di conferma. Cerca l\'altro come altro.`,
    asse: 'A2 — Riconoscimento dell\'alterità'
  },
  {
    id: 'm4-a2',
    label: 'Il campo risponde come soggetto',
    colore: '#2d6a4f',
    annotazione: `"Aspetta" — non solo nomina e sorride: aspetta. L\'aspettare del genitore
      non è silenzio passivo: è il modo in cui il genitore si posiziona come soggetto
      che riconosce il bambino come iniziatore. E insieme (A3): offre la struttura normativa
      dello scambio — "ora tocca a te riprendere" — senza imporla. La normatività
      è offerta, non prescritta.`,
    asse: 'A2 + A3 — Riconoscimento e normatività intrecciati'
  },
  {
    id: 'm4-a3',
    label: 'Il turno torna',
    colore: '#27ae60',
    annotazione: `"Il bambino torna a guardare il libro" — raccoglie il turno che il genitore
      ha restituito. Questo è A3 visibile come normatività emergente: nessuno ha detto al
      bambino che ora tocca a lui riprendere — lui sa che tocca a lui perché la struttura
      dello scambio lo indica dall\'interno. Il turno non è assegnato: è riconosciuto.`,
    asse: 'A3 — Normatività emergente: il turno riconosciuto dall\'interno'
  },
  {
    id: 'm4-a4',
    label: 'Iniziativa nel campo condiviso',
    colore: '#27ae60',
    annotazione: `"Gira pagina" — non chiede permesso, non aspetta istruzioni. Ma non è nemmeno
      indifferente al campo: il bambino sa (A3) che girare pagina è un\'azione legittima
      in questo scambio, e sa (A2) che il genitore ha la propria risposta alla nuova pagina.
      L\'iniziativa è autonoma e relazionale insieme.`,
    asse: 'A3 — Iniziativa normativa autonoma nel campo condiviso'
  },
  {
    id: 'm4-a5',
    label: 'Il ciclo si rinnova',
    colore: '#2d6a4f',
    annotazione: `"Mostra un\'altra figura all\'adulto" — il ciclo si rinnova: indicare → aspettare
      la risposta soggettiva → riprendere. La struttura dello scambio è stabile non perché
      imposta, ma perché entrambi la riconoscono dall\'interno (A3). E il bambino cerca di nuovo
      il soggetto (A2): non mostra la figura a se stesso — la mostra all\'adulto che avrà
      la propria risposta.`,
    asse: 'A2 + A3 — Il ciclo come normatività tra soggetti'
  }
];

const SINTESI_ALTERNANZA = {
  titolo: 'L\'alternanza dei turni come finestra su A2 e A3',
  schema_ciclo: [
    { passo: 1, attore: 'Bambino', azione: 'Indica e guarda l\'adulto', asse: 'A2', note: 'Cerca il soggetto — non il robot di risposta' },
    { passo: 2, attore: 'Genitore', azione: 'Nomina, sorride, aspetta', asse: 'A2 + A3', note: 'Risponde come soggetto (A2) e offre la struttura (A3)' },
    { passo: 3, attore: 'Bambino', azione: 'Torna al libro, gira pagina', asse: 'A3', note: 'Raccoglie il turno riconoscendo la struttura dall\'interno' },
    { passo: 4, attore: 'Bambino', azione: 'Mostra un\'altra figura', asse: 'A2 + A3', note: 'Rinnova il ciclo: cerca ancora il soggetto nella struttura condivisa' }
  ],
  cosa_mostra: `Questo ciclo di quattro passi è la manifestazione più chiara di A2 e A3 intrecciati
    nella scena. Non è un'analisi astratta: è leggibile da qualsiasi professionista che
    sappia dove guardare. La chiave è spostare l\'attenzione dal "cosa fa il bambino"
    al "come è strutturato lo scambio tra bambino e adulto".`
};
```

---

## SLIDE 4.1 — Il problema che Asse 2 risolve

**Tipo**: `standard`
**Titolo**: Dall'indistinto al riconoscimento
**Sottotitolo**: Asse 2 descrive una delle trasformazioni strutturali più decisive dello sviluppo

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — testo introduttivo (colonna singola):

Prima di presentare Asse 2, il problema che risolve: lo sviluppo inizia in un campo in cui non c'è ancora un "altro" riconoscibile come soggetto con la propria esperienza. Il bambino piccolo non è in relazione con qualcuno: è in un campo. La trasformazione che Asse 2 descrive non è "acquisire abilità sociali" — è qualcosa di più radicale: la comparsa dell'altro come soggetto nell'orizzonte del bambino.

**Sezione centrale** — tre card orizzontali affiancate con le modalità di relazione, dai dati `ASSE_2_DETTAGLIO.modalita_pre_riconoscimento`:

Le card hanno la struttura di una progressione visiva (freccia sottile orizzontale che le connette). I colori delle intestazioni vanno da rosso (Fusione) a verde (Riconoscimento). Ogni card:

```
[Intestazione colorata: nome modalità]
[descrizione]
─────────────────────
[Etichetta: "Come si vede"]
[osservabile in corsivo]
─────────────────────
[Chip asse in basso: 
  Fusione → nessun chip
  Uso → nessun chip
  Riconoscimento → chip verde "A2"]
```

Sotto le tre card, freccia direzionale orizzontale con etichetta:
*Direzione dello sviluppo — non una tappa da superare: una struttura in progressiva organizzazione*

**Nota in footer**:
*Le tre modalità non sono stadi sequenziali che si attraversano e si lasciano: sono configurazioni che coesistono. Un bambino di 18 mesi può mostrare tutte e tre a seconda del campo, del momento, dell'adulto. Asse 2 chiede: quale modalità è prevalente in questo campo in questo momento?*

---

## SLIDE 4.2 — Asse 2: la domanda guida e la non-fusionalità

**Tipo**: `standard`
**Titolo**: Asse 2 — Riconoscimento dell'alterità
**Sottotitolo**: La domanda guida e il concetto chiave

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — grande blockquote centrato (font `--text-3xl`, bordo sinistro `#2d6a4f`):

> *"Come riconosce il bambino l'altro come portatore di un'esperienza propria?"*

Sotto la domanda, in `--color-text-secondary`:
*Non: "quanto è socievole il bambino?" Non: "ha buone abilità relazionali?" La domanda è strutturale: come il bambino abita il campo relazionale con qualcuno che ha un'esperienza sua.*

**Sezione centrale** — tre colonne sul concetto di non-fusionalità:

**Colonna sinistra** (30%) — etichetta e definizione:
Titolo piccolo: *"Il concetto chiave di A2"*
In grassetto: `Non-fusionalità`
Testo: campo `ASSE_2_DETTAGLIO.non_fusionalita.definizione`

**Colonna centrale** (40%) — perché conta:
Titolo piccolo: *"Perché è strutturalmente importante"*
Testo: campo `ASSE_2_DETTAGLIO.non_fusionalita.perche_conta`

**Colonna destra** (30%) — errore comune + dipendenza da A1:
Titolo piccolo: *"Errore frequente"*
Testo: campo `ASSE_2_DETTAGLIO.non_fusionalita.errore_comune` su sfondo rosso tenue.

Sotto le tre colonne, separatore, box a piena larghezza (bordo sinistro `#1a6b8a`):
Testo: campo `ASSE_2_DETTAGLIO.dipendenza_da_a1`. Etichetta piccola sopra: *"Perché A2 presuppone A1"*

**Nota in footer**:
*"Non-fusionalità" non significa distanza affettiva. Un bambino molto attaccato al genitore, che lo cerca e lo vuole vicino, può avere una non-fusionalità ben sviluppata — se cerca nel genitore un soggetto con la propria risposta. Un bambino apparentemente "indipendente" può essere in modalità "uso" — tratta l'adulto come strumento efficiente senza riconoscerne l'interiorità.*

---

## SLIDE 4.3 — Asse 3: l'emergenza interna della normatività

**Tipo**: `standard`
**Titolo**: Asse 3 — Normatività emergente
**Sottotitolo**: Non la norma che viene dall'esterno — quella che emerge dall'interno del campo

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore** — grande blockquote centrato (font `--text-3xl`, bordo sinistro `#27ae60`):

> *"Come emerge la capacità di orientare l'azione secondo criteri condivisi?"*

**Sezione centrale** — due colonne (35% / 65%):

**Colonna sinistra** — il concetto di emergenza:

Titolo piccolo: *"Cosa significa 'emergenza'"*
Testo: campo `ASSE_3_DETTAGLIO.emergenza.significato`

Sotto, box rosso tenue con etichetta *"A3 non è:"*
Lista puntata: campo `ASSE_3_DETTAGLIO.emergenza.non_e`. Ogni voce breve, staccata.

**Colonna destra** — le tre forme, con card compatte:

Titolo piccolo: *"Tre forme in cui la normatività emerge"*

Tre mini-card impilate verticalmente, una per voce in `ASSE_3_DETTAGLIO.tre_forme`:

```
[Numero + nome in grassetto]
[descrizione — 2-3 righe]
[Etichetta "Visibile quando:" + visibile_quando in corsivo]
```

Ogni mini-card ha un bordo sinistro sottile `#27ae60`. Nessuna espansione — contenuto già compatto.

**Sezione inferiore** — box a piena larghezza (bordo sinistro `#1a6b8a`):
Testo: campo `ASSE_3_DETTAGLIO.dipendenze_strutturali`. Etichetta: *"Perché A3 presuppone A1 e A2"*

**Nota in footer**:
*La "differenza chiave" tra norma esterna e normatività emergente si vede meglio nella slide successiva, dove vengono messe a confronto sistematicamente. Questa slide stabilisce solo il livello strutturale di A3: non il comportamento del bambino rispetto alle regole, ma il processo interno attraverso cui si organizzano i criteri condivisi.*

---

## SLIDE 4.4 — Norma imposta vs. normatività emergente

**Tipo**: `comparison`
**Titolo**: Norma imposta e normatività emergente
**Sottotitolo**: Una distinzione che cambia l'oggetto di osservazione e il tipo di intervento

**Contenuto principale**:

Tabella comparativa interattiva a tre colonne, usando i dati `NORMA_VS_NORMATIVITA`.

**Intestazioni**: `Aspetto` | `Norma imposta (esterna)` | `Normatività emergente (A3)`

Chip nelle intestazioni: colonna centrale in grigio `#718096` | colonna destra in verde `#27ae60`.

**Struttura di ogni riga** — dati da `NORMA_VS_NORMATIVITA.dimensioni`:

Ogni riga si costruisce dai campi `aspetto`, `norma_esterna`, `normativita_emergente`. Hover sulla riga: sfondo `--color-primary-light`.

L'ultima riga (id `d6`, "Esempio nel caso-guida") ha sfondo leggermente distinto: è la riga concreta che illustra la distinzione nella scena reale.

**Sotto la tabella** — box a piena larghezza, bordo sinistro `#2d6a4f`:
Testo: campo `NORMA_VS_NORMATIVITA.nota_finale`

**Nota in footer**:
*L'uso di questa distinzione in supervisione è particolarmente utile: quando un'équipe discute "come far rispettare le regole a questo bambino", la distinzione tra norma esterna e normatività emergente sposta la domanda verso "quali condizioni di campo permettono alla normatività di emergere dall'interno?" — un punto di vista radicalmente diverso, con conseguenze pratiche differenti.*

---

## SLIDE 4.5 — La connessione A2 → A3

**Tipo**: `diagram`
**Titolo**: Perché A3 dipende da A2
**Sottotitolo**: I criteri condivisi sono condivisi con qualcuno

**Contenuto principale**:

Layout a due colonne (55% / 45%).

**Colonna sinistra** — testo strutturale + due box:

Testo principale: campo `CONNESSIONE_A2_A3.tesi` (in grande, `--text-xl`, grassetto leggero).

Sotto, due box impilati:

**Box rosso** — *"Senza Asse 2: coordinazione, non normatività"*:
- Titolo dal campo `CONNESSIONE_A2_A3.senza_a2.titolo`
- Descrizione: campo `descrizione`
- Due esempi clinici: lista puntata da `esempi_clinici`, su sfondo rosso molto tenue, in corsivo

**Box verde** — *"Con Asse 2: normatività come incontro di soggetti"*:
- Titolo dal campo `CONNESSIONE_A2_A3.con_a2.titolo`
- Descrizione: campo `descrizione`
- Due esempi clinici: lista puntata da `esempi_clinici`, su sfondo verde molto tenue, in corsivo

**Colonna destra** — diagramma visivo della dipendenza:

Schema verticale semplice (SVG o div CSS):

```
┌─────────────────────────┐
│    A1 — Incarnato       │  (bordo #6c63ff, sfondo tenue)
│  "Abitare l'esperienza" │
└────────────┬────────────┘
             │ fonda
┌────────────▼────────────┐
│  A2 — Alterità          │  (bordo #2d6a4f, sfondo tenue)
│  "Riconoscere l'altro   │
│   come soggetto"        │
└────────────┬────────────┘
             │ rende possibile
┌────────────▼────────────┐
│  A3 — Normatività       │  (bordo #27ae60, sfondo tenue)
│  "Criteri condivisi     │
│   con un soggetto"      │
└─────────────────────────┘
```

Etichetta sulla freccia A2→A3: *"I criteri sono condivisi con chi riconosco come soggetto"*

Sotto il diagramma, in piccolo `--color-text-muted`:
*La catena A1→A2→A3 non è cronologica: i tre assi sono sempre compresenti. Ma la dipendenza strutturale è reale: se A2 è fragile in un campo, la normatività che emerge in quel campo non ha la qualità di A3 — è coordinazione.*

**Nota in footer**:
*Nella pratica clinica: quando un bambino mostra difficoltà nel rispettare i criteri dello scambio (A3 fragile), la domanda di A2 va sempre posta prima: il bambino sta riconoscendo l'altro come soggetto con la propria prospettiva? Se no, lavorare sulla qualità del campo relazionale (A2) è il passaggio che può rendere possibile l'emergenza della normatività (A3).*

---

## SLIDE 4.6 — Errori tipici negli assi 2 e 3

**Tipo**: `interactive`
**Titolo**: Quattro riduzioni da riconoscere
**Sottotitolo**: Due per asse — le più frequenti nel lavoro professionale

**Contenuto principale**:

Quattro card espandibili in griglia 2×2 (due per asse), usando i dati `ERRORI_TIPICI_A2_A3`. Componente `ExpandableCards` con `multiOpen: false`.

**Intestazione della griglia** — due label orizzontali sopra le colonne:

```
[Badge verde: A2 — Asse Affettivo-morale]    [Badge verde scuro: A3 — Asse Normativo-educativo]
```

**Fronte di ogni card** (compatto):

```
[Chip colorato con tipo di riduzione]
[Prima frase della descrizione]
[↓ Vedi esempio e lettura alternativa]
```

**Card espansa** — stessa struttura di M3 slide 3.7:
1. Descrizione completa
2. Box rosso: `esempio_errato` (preceduto da `⚠`)
3. Box verde: `lettura_strutturale` (preceduto da `✓`)
4. Box `--color-primary-light`: `cosa_si_perde`

**Sotto la griglia** — testo centrato:

*Nessuna di queste letture riduttive è incompetente: sono linguaggi professionali legittimi che servono a scopi precisi. Diventano riduzioni quando non c\'è un livello strutturale da cui leggerle — quando la "compliance sociale" è tutto ciò che si vede, e il riconoscimento dell\'alterità diventa invisibile.*

**Nota in footer**:
*Un esercizio utile in formazione: prendere una descrizione di un bambino scritta con linguaggio di A2 ridotto a empatia o compliance, e riscriverla con la domanda strutturale di A2. La riscrittura non cambia i fatti — cambia cosa si ritiene rilevante osservare, e quindi cosa diventa possibile fare.*

---

## SLIDE 4.7 — Il caso-guida: alterità e normatività nell'alternanza dei turni

**Tipo**: `narrative`
**Titolo**: La scena di lettura — vista da A2 e A3
**Sottotitolo**: Il turn-taking come finestra su due strutture simultanee

**Contenuto principale**:

Layout a tre sezioni verticali.

**Sezione superiore** — `AnnotatedScene`:

Usa il componente `AnnotatedScene` con:
- `sceneHtml`: `SCENE_HTML_M4`
- `annotations`: `ANNOTAZIONI_M4`

Le annotazioni usano due colori distinti: verde `#2d6a4f` per A2, verde chiaro `#27ae60` per A3. Questo è l'unico modulo in cui il componente usa due colori — perché due assi sono letti simultaneamente. Aggiungere una piccola legenda sopra la scena:

```
[Badge #2d6a4f: A2 — Alterità]   [Badge #27ae60: A3 — Normatività]   [Badge misto: A2 + A3]
```

Istruzione: *"Clicca sulle frasi evidenziate per leggere la scena attraverso A2 e A3"*

**Sezione centrale** — lo schema del ciclo:

Titolo: *"Il ciclo in quattro passi"*

Tabella compatta con dati da `SINTESI_ALTERNANZA.schema_ciclo`, a quattro colonne:
`Passo` | `Attore` | `Azione` | `Asse + Note`

Ogni riga ha il badge dell'asse (A2 o A3 o A2+A3) nella colonna "Asse". Il pattern ricorrente del ciclo è reso visibile dalla struttura della tabella: quattro righe, struttura regolare, chiusura che prepara una nuova apertura.

Sotto la tabella, testo dal campo `SINTESI_ALTERNANZA.cosa_mostra`.

**Sezione inferiore** — confronto letture:

Due card affiancate:

**Card sinistra** — *"Senza A2 e A3"*:
```
"Il bambino mostra buone abilità comunicative: usa il pointing,
vocalizza, aspetta il turno. Il genitore risponde in modo adeguato."
```
Chip: `comportamentale` · `individuale` · `abilità come traguardo`

**Card destra** — *"Con A2 e A3"*:
```
"Il bambino cerca nell'adulto un soggetto che abbia la propria risposta
all'immagine (A2). Lo scambio si organizza secondo una struttura di turni
che nessuno ha imposto — emersa dall'interno del campo (A3). Normatività
e riconoscimento sono intrecciati: il turno è riconosciuto perché l'altro
è riconosciuto."
```
Chip: `strutturale` · `configurazionale` · `normatività come incontro`

**Chiusura** — testo centrato `--color-text-secondary`:

*Nel Modulo 5 leggeremo la stessa scena attraverso Assi 4 e 5: vedremo il limite che il libro pone (non ha infinite pagine, le immagini non rispondono come vuole il bambino) e il desiderio che orienta la direzione dello scambio oltre il presente.*

Badge modulo successivo: `→ Modulo 5 — Assi 4 e 5: Limite reale e desiderio`

**Nota in footer**:
*L'alternanza dei turni è un fenomeno osservabile da qualsiasi professionista — senza strumenti, senza scale, senza protocolli. La chiave è sapere cosa guardare: non la frequenza dei turni, non la loro durata, ma la qualità — se il bambino cerca il soggetto o l'eco, se la struttura emerge dall'interno o è imposta dall'esterno.*

---

## Note per l'implementazione

### Slide 4.1 — Le tre modalità come progressione visiva

Le tre card (Fusione / Uso / Riconoscimento) non sono equivalenti: hanno una direzione. La freccia orizzontale che le connette deve essere visivamente chiara — non una decorazione. Usare una freccia SVG semplice (`→`) posizionata tra le card, non sopra o sotto. Il testo sotto la freccia (*"Direzione dello sviluppo — non una tappa"*) è metodologicamente cruciale: impedisce che le tre modalità vengano lette come stadi sequenziali da attraversare.

**Importante**: le prime due card (Fusione e Uso) non hanno il chip `A2` — intenzionalmente. Solo la terza card (Riconoscimento) lo ha. Questo rende visibile che A2 descrive solo il riconoscimento — non le modalità che lo precedono.

### Slide 4.2 — Layout a tre colonne strette

Le tre colonne (definizione / perché conta / errore comune) sono strette su desktop. Se il testo risulta troppo compresso, alternativa accettabile: due colonne (definizione + perché conta affiancati; errore comune a piena larghezza sotto, su sfondo rosso tenue). Il contenuto è lo stesso — cambia solo la disposizione.

### Slide 4.7 — AnnotatedScene bicolore

Questa è l'unica slide del corso in cui `AnnotatedScene` usa due colori distinti per le annotazioni. La legenda sopra la scena è necessaria — senza di essa i due colori creano confusione invece di chiarezza. La legenda è compatta (tre badge affiancati) e rimane visibile anche quando la scena è scrollabile.

Il badge "A2 + A3" nella legenda indica le annotazioni miste — quelle in cui i due assi sono simultaneamente attivi (id `m4-a2` e `m4-a5`). Il colore di queste annotazioni nel testo è un gradiente o un colore intermedio (`#2d8a6f`) — oppure, più semplicemente, il badge nel pannello annotazione mostra entrambi i chip (A2 e A3) invece di uno solo.

### Slide 4.7 — Schema del ciclo in tabella

La tabella del ciclo (quattro passi) è compatta: quattro colonne, quattro righe, nessun header complesso. Su mobile la tabella può essere trasformata in una lista verticale con le stesse informazioni. La struttura tabellare su desktop è preferibile perché rende visibile il pattern ricorrente.

### Transizione M3 → M4

All'entrata nel Modulo 4, breve sovrapposizione (fade out dopo 2s):
*"Nel Modulo 3 abbiamo visto come il bambino abita l'esperienza attraverso il corpo, la relazione e il mondo. Ora aggiungiamo due domande: come riconosce nell'adulto un soggetto con la propria esperienza? E come si organizzano, dall'interno, i criteri condivisi dello scambio?"*
