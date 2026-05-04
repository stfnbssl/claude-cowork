# F1 — Modulo 7: Statuto epistemologico e passaggio a F2

## Metadati

| Campo | Valore |
|-------|--------|
| ID modulo | M7 |
| Titolo breve | Statuto epistemologico e passaggio a F2 |
| Titolo operativo | Cosa abbiamo imparato a fare — e dove andiamo |
| Colore accent | `#2c3e50` |
| Colore accent modulo (header/nav) | `#2c3e50` |
| Tipo di modulo | Epistemologico / conclusivo |
| Slide count | 7 |
| File JS | `F1/f1_m07.js` |
| Dipendenze globali | `window.SEI_ASSI`, `window.CASO_GUIDA_F1` |

---

## Nota metodologica

M7 è il modulo di chiusura di F1. Non introduce un settimo asse né aggiunge contenuto strutturale: chiarisce il tipo di conoscenza che F1 produce, i suoi limiti costitutivi e la funzione che svolge come fondazione di F2.

**La sfida centrale:** il rischio di M7 è l'astrazione. Il professionista ha lavorato per sei moduli su fenomeni osservabili (la vocalizzazione anticipatoria, la mano tesa verso il libro chiuso, la chiusura dell'albo). Tornare a una domanda epistemologica ("che tipo di sapere stiamo producendo?") potrebbe sembrare un passo indietro. La strategia è inversa: M7 risponde alla domanda epistemologica mostrando cosa cambia nella pratica concreta quando il professionista ha F1 a disposizione.

**Il cuore di M7:** "Il campo mostra..." è una forma linguistica epistemologicamente precisa. Non è "il bambino è...", non è "la situazione dimostra che...", non è "secondo la teoria...". È una terza via: la lettura strutturale. M7 deve rendere visibile questa terza via con esempi concreti, non con definizioni astratte.

**Struttura pedagogica:**
- Slide 7.1: entrata dalla domanda pratica — cosa è cambiato nel modo di osservare?
- Slide 7.2: statuto epistemologico — le tre proprietà della lettura strutturale
- Slide 7.3: i limiti di F1 — cosa non può dire (e perché questo è un punto di forza)
- Slide 7.4: il passaggio a F2 — cosa F1 porta e cosa F2 aggiunge
- Slide 7.5: la scena annotata finale — tutti e sei gli assi simultaneamente visibili
- Slide 7.6: il guardrail come pratica professionale — tre scenari concreti
- Slide 7.7: la fondazione è posta — chiusura del corso

**Nota sul tono:** M7 deve avere un tono di chiusura, non di riepilogo. Non si ripassano i sei assi — si mostra cosa significa averli. Il professionista che termina M7 non sa "più cose" sul bambino: sa leggere il campo in modo strutturalmente diverso.

---

## Costanti JavaScript (`F1/f1_m07.js`)

```javascript
// ─────────────────────────────────────────────
// M7 — Statuto epistemologico e passaggio a F2
// Modulo conclusivo del corso F1
// ─────────────────────────────────────────────

// ─────────────────────────────────────────────
// STATUTO EPISTEMOLOGICO
// ─────────────────────────────────────────────
const STATUTO_EPISTEMOLOGICO = {
  formula: "Il campo mostra...",
  spiegazione: "Questa formula non è un vezzo stilistico: è una posizione epistemologica. Dire 'il campo mostra' significa che la lettura strutturale si colloca tra la pura descrizione fenomenologica ('ho osservato che...') e la spiegazione causale ('questo succede perché...'). Né solo descrizione né spiegazione: lettura strutturale.",
  tre_proprieta: [
    {
      id: "p1",
      nome: "Relazionale",
      sottotitolo: "La lettura è sempre del campo, mai del bambino isolato",
      descrizione: "Una lettura strutturale descrive il campo — il sistema relazionale composto da bambino, adulto, oggetti, spazio, tempo. Non è possibile produrre una lettura strutturale F1 di un bambino isolato: non esistono assi 'del bambino', esistono assi 'del campo'.",
      esempio_corretto: "Il campo della lettura condivisa mostra A1 attivo: il bambino abita corporalmente lo spazio del libro.",
      esempio_scorretto: "Il bambino mostra un buon livello di A1.",
      perche_conta: "Questa proprietà protegge dal riduzionismo: F1 non produce profili individuali. Produce letture di campo."
    },
    {
      id: "p2",
      nome: "Non-valutativa",
      sottotitolo: "Gli assi non misurano: illuminano struttura",
      descrizione: "La presenza o assenza di un asse nel campo non è una valutazione positiva o negativa. A6 molto visibile non è 'meglio' di A6 poco visibile: significa che il campo ha una storia sedimentata, tutto qui. F1 non produce giudizi — produce descrizioni strutturali.",
      esempio_corretto: "In questo campo A3 è poco visibile: le forme di scambio sono ancora in costruzione.",
      esempio_scorretto: "Questo bambino ha un A3 basso: c'è un deficit nella normatività emergente.",
      perche_conta: "Questa proprietà protegge dall'uso diagnostico improprio: F1 non misura, non norma, non stabilisce soglie."
    },
    {
      id: "p3",
      nome: "Non-causale",
      sottotitolo: "F1 descrive strutture, non origini",
      descrizione: "La lettura strutturale dice come è fatto il campo adesso, non perché è fatto così. Non risponde a 'perché questo bambino fa X': risponde a 'che struttura ha il campo in cui X si produce'. Le spiegazioni causali appartengono ad altri framework — clinici, neurobiologici, biografici.",
      esempio_corretto: "Il campo mostra A4 incontrato con resistenza prolungata: la discontinuità produce un orientamento intenso (A5 molto visibile).",
      esempio_scorretto: "Questo bambino incontra i limiti con difficoltà probabilmente a causa di un attaccamento ansioso.",
      perche_conta: "Questa proprietà protegge dall'inferenza prematura: F1 non spiega le cause dei fenomeni — li struttura, lasciando alle altre fasi del metodo HCAIRE il compito dell'analisi causale."
    }
  ],
  cosa_produce: [
    "un vocabolario strutturale condiviso tra professionisti diversi",
    "letture di campo che descrivono senza giudicare",
    "una base comune per il dialogo interprofessionale",
    "il materiale su cui F2 può lavorare"
  ],
  cosa_non_produce: [
    "diagnosi o valutazioni cliniche",
    "prescrizioni educative o terapeutiche",
    "spiegazioni causali o eziologiche",
    "profili individuali del bambino"
  ]
};

// ─────────────────────────────────────────────
// I TRE LIMITI COSTITUTIVI DI F1
// ─────────────────────────────────────────────
const LIMITI_F1 = [
  {
    id: "l1",
    limite: "F1 non diagnostica",
    descrizione: "F1 non produce diagnosi cliniche, funzionali o evolutive. Gli assi strutturali non sono criteri diagnostici: non misurano competenze, non stabiliscono soglie, non collocano il bambino in categorie nosografiche.",
    perche_non_e_un_difetto: "F1 non diagnostica perché non è uno strumento diagnostico: è uno strumento di lettura ontologica. La diagnosi richiede confronto con norme, campioni, scale — F1 non lavora su quel piano. Chi vuole diagnosticare ha bisogno di altri strumenti (F2, F3, protocolli clinici specifici).",
    cosa_fa_invece: "F1 produce una descrizione strutturale del campo che può alimentare il processo diagnostico senza sostituirlo.",
    rischio_da_evitare: "Usare i sei assi come check-list ('A1: presente / A3: carente') equivale a trasformare F1 in uno strumento di screening — uso scorretto che ne snatura la funzione."
  },
  {
    id: "l2",
    limite: "F1 non prescrive",
    descrizione: "F1 non dice cosa fare. Non produce indicazioni terapeutiche, educative, riabilitative. La lettura strutturale del campo non implica automaticamente un intervento.",
    perche_non_e_un_difetto: "F1 non prescrive perché la fondazione ontologica precede la decisione pratica — non la determina. Sapere che A2 è in consolidamento in un campo non dice ancora nulla su come intervenire: dipende dal contesto, dalla fase HCAIRE, dagli obiettivi specifici.",
    cosa_fa_invece: "F1 produce la base su cui F2 può analizzare il funzionamento delle pratiche di cura, e da lì — con F3 e oltre — si costruiscono le indicazioni operative.",
    rischio_da_evitare: "Leggere una presenza debole di A5 come indicazione a 'stimolare il desiderio' è un uso prescrittivo scorretto: F1 descrive, non prescrive."
  },
  {
    id: "l3",
    limite: "F1 non spiega causalmente",
    descrizione: "F1 non risponde alla domanda 'perché'. Non spiega perché un bambino mostra certi pattern, non identifica cause di difficoltà, non ricostruisce catene eziologiche.",
    perche_non_e_un_difetto: "F1 non spiega perché la lettura strutturale è sincronica, non diacronica: descrive come è fatto il campo adesso, non come ci è arrivato. Le spiegazioni causali — neurobiologiche, relazionali, biografiche — appartengono ad altri livelli dell'analisi HCAIRE.",
    cosa_fa_invece: "F1 produce la struttura del campo che le spiegazioni causali potranno poi tentare di spiegare. Prima si descrive cosa c'è; poi si cerca perché c'è.",
    rischio_da_evitare: "Costruire inferenze causali dalla lettura strutturale ('A4 incontrato con difficoltà → probabilmente trauma pregresso') è un salto epistemologico che F1 non autorizza."
  }
];

// ─────────────────────────────────────────────
// IL PASSAGGIO A F2
// ─────────────────────────────────────────────
const PASSAGGIO_F2 = {
  cosa_fa_f2: "F2 analizza il funzionamento delle pratiche di cura: come un intervento, un setting, una relazione terapeutica o educativa si struttura nel campo ontologico definito da F1. F2 usa il vocabolario di F1 per leggere non solo 'cosa c'è nel campo' ma 'come il metodo HCAIRE agisce su quel campo'.",
  metafora: "F1 costruisce la mappa del territorio; F2 analizza come ci si muove in quel territorio con pratiche specifiche di cura.",
  cosa_porta_f1_a_f2: [
    {
      id: "c1",
      da_f1: "Il bambino come soggetto (M1)",
      permette_a_f2: "F2 può analizzare le pratiche di cura sapendo che si rivolgono a un soggetto incarnato, relazionale e temporale — non a un organismo da riparare o a un comportamento da correggere."
    },
    {
      id: "c2",
      da_f1: "I sei assi strutturali (M2–M6)",
      permette_a_f2: "F2 ha un vocabolario preciso per descrivere cosa accade nel campo quando una pratica di cura interviene: quali assi attiva, quali trascura, come modifica la struttura relazionale."
    },
    {
      id: "c3",
      da_f1: "Lo statuto epistemologico (M7)",
      permette_a_f2: "F2 sa di lavorare su letture strutturali, non su diagnosi. Può analizzare le pratiche senza pretendere di spiegarne le cause o prescriverne i risultati."
    }
  ],
  domande_che_f2_puo_fare: [
    "Come si struttura questa pratica di cura nel campo degli assi?",
    "Quali assi la pratica di cura attiva, rafforza o trascura?",
    "Come si trasforma il campo prima, durante e dopo l'intervento?",
    "Il setting di cura crea le condizioni per i sei assi o ne ostacola qualcuno?"
  ],
  domande_che_solo_f3_oltre_possono_fare: [
    "Questa pratica è efficace per questo bambino?",
    "Qual è il trattamento indicato?",
    "Come si modifica la diagnosi alla luce dell'osservazione?"
  ],
  confine_chiaro: "F1 finisce dove comincia la prescrizione. F2 è l'analisi delle pratiche. F3 e oltre sono le fasi operative e valutative del metodo HCAIRE."
};

// ─────────────────────────────────────────────
// GUARDRAIL F1 — forma completa e scenari
// Questo è il guardrail del corso, non del singolo modulo
// ─────────────────────────────────────────────
const GUARDRAIL_F1_COMPLETO = {
  id: "g-f1",
  testo_breve: "Nessun output di F1 descrive il bambino isolato.",
  testo_medio: "La lettura strutturale descrive sempre il campo — il bambino in relazione, non il bambino.",
  testo_completo: "Ogni output di F1 deve essere utilizzabile senza descrivere il bambino come individuo isolato. Questo non significa negare l'individualità del bambino: significa che lo strumento F1 non produce descrizioni individuali. Produce letture di campo. Un output di F1 che descriva solo il bambino — senza il campo relazionale in cui si trova — ha già violato la fondazione ontologica.",
  test_pratico: "Prendi l'output che stai per produrre e cancella mentalmente tutti i riferimenti al bambino. Se rimane qualcosa di significativo (la struttura del campo, le relazioni tra gli assi, le condizioni di possibilità), l'output era strutturale. Se non rimane nulla, era una descrizione individuale.",
  tre_scenari: [
    {
      id: "s1",
      contesto: "Pediatra — restituzione post-visita",
      violazione: "Lorenzo mostra un A1 buono ma A3 in fase di consolidamento. Il desiderio (A5) è presente ma non ancora ben strutturato.",
      compliance: "Il campo della visita pediatrica mostra un bambino che abita corporalmente lo spazio (A1 attivo) in un contesto per lui nuovo, con forme di scambio ancora in costruzione con questa persona (A3 in consolidamento) e orientamento prevalente verso l'uscita (A5 verso il limite della situazione). Non c'è nulla di patologico: è la struttura di un campo di primo incontro.",
      cosa_cambia: "La violazione descrive il bambino come se gli assi fossero sue proprietà permanenti. La compliance descrive il campo di questa situazione — reversibile, contestuale, strutturale."
    },
    {
      id: "s2",
      contesto: "Educatrice — documentazione",
      violazione: "Sofia è una bambina che abita bene l'esperienza ma ha ancora difficoltà con l'alterità. Fatica a riconoscere l'altro come davvero diverso da sé.",
      compliance: "Il campo delle attività di lettura condivisa mostra Sofia che abita corporalmente lo spazio del libro (A1 molto visibile) in un campo di alterità con l'educatrice ancora in fase di co-costruzione (A2 in consolidamento). Nelle attività individuali con materiali strutturati A2 appare più consolidata.",
      cosa_cambia: "La violazione trasforma un'osservazione di campo in un tratto della bambina. La compliance specifica il campo e lascia aperta la variabilità contestuale."
    },
    {
      id: "s3",
      contesto: "Neuropsichiatra infantile — colloquio con i genitori",
      violazione: "Il profilo strutturale di Marco mostra A1 nella norma, A4 con qualche rigidità e A5 molto elevato. Questo potrebbe indicare una difficoltà nell'incontro con il reale.",
      compliance: "F1 non produce profili individuali né confronti con norme. Le letture di campo prodotte durante le osservazioni mostrano che i campi in cui Marco è inserito hanno strutture diverse: nel campo familiare A5 è molto visibile (orientamento forte verso oggetti e attività familiari), nel campo clinico A4 è più presente (molti limiti nuovi da incontrare). Queste osservazioni alimentano l'analisi ma non costituiscono di per sé un profilo diagnostico.",
      cosa_cambia: "La violazione usa F1 per costruire un profilo — uso strutturalmente scorretto. La compliance specifica che F1 produce letture di campo plurali, non un profilo individuale."
    }
  ]
};

// ─────────────────────────────────────────────
// SCENE HTML — pre-costruita con span annotabili
// La scena più ricca del corso: tutti e sei gli assi visibili
// Scena: il bambino porta il libro, lettura, richiesta di rilettura
// Un unico momento che attraversa l'intera struttura
// ─────────────────────────────────────────────
const SCENE_HTML_M7 = `
<p>Il bambino attraversa la stanza 
<span class="annotabile" data-annotation-id="m7-a1-1">portando il peso del corpo in avanti</span>, 
l'albo stretto tra le braccia. 
<span class="annotabile" data-annotation-id="m7-a6-1">Lo porta già orientato nel verso giusto</span>. 
Arriva all'educatrice e 
<span class="annotabile" data-annotation-id="m7-a2-1">glielo porge</span> 
— non lo lascia cadere, non lo lancia: 
lo consegna, guardandola.</p>

<p>Si siedono. L'educatrice apre alla prima pagina. 
Il bambino, 
<span class="annotabile" data-annotation-id="m7-a6-2">prima ancora che l'immagine sia visibile</span>, 
emette una vocalizzazione breve. 
<span class="annotabile" data-annotation-id="m7-a3-1">L'educatrice risponde con la stessa intonazione</span>: 
hanno già un modo di cominciare. 
A metà lettura, 
<span class="annotabile" data-annotation-id="m7-a4-1">l'educatrice chiude il libro un istante</span> 
per aggiustare la posizione. 
Il bambino 
<span class="annotabile" data-annotation-id="m7-a5-1">tende immediatamente la mano verso il libro chiuso</span> 
e vocalizza verso di lei. 
Lei riapre. 
Il campo riprende.</p>

<p>Ultima pagina. 
<span class="annotabile" data-annotation-id="m7-a6-3">Il bambino abbassa la voce come ha imparato a fare</span>. 
L'educatrice chiude. Un momento. 
Poi il bambino 
<span class="annotabile" data-annotation-id="m7-a5-2">porta il libro verso di lei ancora una volta</span> — 
<span class="annotabile" data-annotation-id="m7-a3-2">con la stessa forma di prima</span>, 
la stessa vocalizzazione ascendente. 
Il campo conosce questa richiesta.</p>
`;

const ANNOTAZIONI_M7 = [
  {
    id: "m7-a1-1",
    label: "A1 — Abitare l'esperienza",
    colore: "#1a6b8a",
    asse: "a1",
    annotazione: "Il peso del corpo in avanti è A1: il bambino abita corporalmente il movimento verso l'altro e verso il libro. Non è un gesto intenzionale astratto — è il campo incarnato che si orienta.",
    note_tecniche: "Badge A1 teal. Prima annotazione della scena: A1 è sempre la fondazione visibile."
  },
  {
    id: "m7-a6-1",
    label: "A6 — Storicità",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Portare il libro 'nel verso giusto' è la storicità del campo incarnata nel gesto: le letture precedenti hanno sedimentato questa forma. Il bambino non sta imparando a tenere il libro — lo tiene già come lo ha sempre tenuto con questa educatrice.",
    note_tecniche: "Badge A6 arancione. Appare subito accanto ad A1: storicità e incarnato co-presenti dall'inizio."
  },
  {
    id: "m7-a2-1",
    label: "A2 — Alterità",
    colore: "#2d6a4f",
    asse: "a2",
    annotazione: "Consegnare guardando è il riconoscimento dell'alterità: il libro non viene depositato ma dato — e il bambino guarda mentre lo fa. L'educatrice è riconosciuta come alterità che riceve, non come superficie su cui appoggiare.",
    note_tecniche: "Badge A2 verde. Il gesto del porgere + lo sguardo sono gli osservabili di A2 più densi."
  },
  {
    id: "m7-a6-2",
    label: "A6 — Anticipazione (storicità nel gesto)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Vocalizzare prima che l'immagine sia visibile è la forma più pura di A6: la sequenza è già struttura del campo. Il bambino porta il futuro nel presente perché il passato glielo ha consegnato come forma.",
    note_tecniche: "Badge A6. Seconda apparizione: la storicità si mostra anche nel mezzo della lettura, non solo all'inizio."
  },
  {
    id: "m7-a3-1",
    label: "A3 — Normatività emergente",
    colore: "#27ae60",
    asse: "a3",
    annotazione: "L'educatrice che risponde con la stessa intonazione mostra A3 in azione: hanno costruito insieme una forma di scambio riconoscibile. Non è imitazione né abitudine: è la normatività emergente del campo — una forma condivisa che entrambi riconoscono come 'il nostro modo di cominciare'.",
    note_tecniche: "Badge A3 verde chiaro. A3 appare nella risposta dell'adulto: la norma emerge da entrambi i poli del campo."
  },
  {
    id: "m7-a4-1",
    label: "A4 — Limite reale",
    colore: "#c0392b",
    asse: "a4",
    annotazione: "La chiusura del libro — anche momentanea, anche accidentale — è il limite reale: il campo grafico scompare, il flusso della lettura si interrompe. A4 è strutturale: non dipende dall'intenzione dell'adulto.",
    note_tecniche: "Badge A4 rosso. Il limite qui è quasi incidentale (aggiustare la posizione) — ma strutturalmente identico a una chiusura intenzionale. A4 non dipende dall'intenzione."
  },
  {
    id: "m7-a5-1",
    label: "A5 — Desiderio come orientamento",
    colore: "#8e44ad",
    asse: "a5",
    annotazione: "La mano tesa immediatamente verso il libro chiuso è A5 nella sua forma più rapida: il desiderio si orienta verso il limite nel momento stesso in cui il limite si produce. Non c'è attesa, non c'è elaborazione — il campo si orienta.",
    note_tecniche: "Badge A5 viola. La rapidità della risposta (immediatamente) mostra la strutturalità di A5: non è una scelta, è l'orientamento del campo."
  },
  {
    id: "m7-a6-3",
    label: "A6 — Storicità (forma co-costruita)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Abbassare la voce 'come ha imparato a fare' è la storicità nella sua forma più intensa: una prassi del campo co-costruita lettura dopo lettura, ora incorporata. Il bambino non imita — ha fatto propria una forma del campo.",
    note_tecniche: "Badge doppio A6+A3: la norma emergente (A3) è qui osservabile come sedimentazione storica (A6). Annotazione tra le più dense della scena."
  },
  {
    id: "m7-a5-2",
    label: "A5 — Desiderio (richiesta di rilettura)",
    colore: "#8e44ad",
    asse: "a5",
    annotazione: "Portare ancora il libro dopo la chiusura finale è il desiderio orientato verso il polo significativo che ha incontrato il limite (A4). Il campo si orienta nuovamente: non verso un oggetto qualsiasi, ma verso questo libro, in questo campo, con questa persona.",
    note_tecniche: "Badge A5. Seconda apparizione: il desiderio si riproduce dopo il limite finale — mostrando che A5 non si esaurisce in un singolo gesto."
  },
  {
    id: "m7-a3-2",
    label: "A3 — Stessa forma, riconosciuta",
    colore: "#27ae60",
    asse: "a3",
    annotazione: "Usare 'la stessa forma di prima' non è ripetizione meccanica: è la normatività emergente in azione. Il bambino sa che questa forma funziona in questo campo — la usa perché l'ha imparata come forma efficace di richiesta. Il campo la riconosce.",
    note_tecniche: "Badge doppio A3+A6: la forma normativamente riconoscibile (A3) porta la storia delle richieste precedenti (A6). Annotazione finale della scena — il campo chiude con la massima densità strutturale."
  }
];

// ─────────────────────────────────────────────
// SINTESI DEI SEI VERBI — per la slide di chiusura
// ─────────────────────────────────────────────
const SEI_VERBI_CHIAVE = [
  { asse: "A1", verbo: "abitare",    colore: "#1a6b8a" },
  { asse: "A2", verbo: "riconoscere",colore: "#2d6a4f" },
  { asse: "A3", verbo: "scambiare",  colore: "#27ae60" },
  { asse: "A4", verbo: "incontrare", colore: "#c0392b" },
  { asse: "A5", verbo: "orientarsi", colore: "#8e44ad" },
  { asse: "A6", verbo: "situarsi",   colore: "#d35400" }
];

const CHIUSURA_CORSO = {
  titolo: "La fondazione è posta",
  testo: "F1 non ha insegnato a osservare meglio. Ha insegnato a osservare diversamente: il campo invece del bambino, la struttura invece del comportamento, la lettura invece della valutazione. Questo cambiamento non si misura in competenze acquisite — si misura in domande che ora si pongono in modo diverso.",
  domanda_finale: "Quando osservi un bambino e un adulto leggere insieme, cosa vedi adesso che non vedevi prima?",
  verso_f2: "F2 analizzerà come le pratiche di cura si strutturano in questo campo. Porta con te il vocabolario: ne avrai bisogno."
};
```

---

## Slide — Specifiche

### Slide 7.1 — "Cosa è cambiato nel modo di osservare?"

**Tipo:** `standard`
**Accent:** `#2c3e50`
**Dati:** costruiti inline

**Layout:** layout narrativo — due momenti temporali a confronto

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Prima e dopo: la stessa scena, uno sguardo diverso│
├─────────────────────────────────────────────────────────────┤
│  [Citazione scena — bordo grigio-blu]                       │
│  "Il bambino tende la mano verso il libro chiuso            │
│   e vocalizza verso l'educatrice."                          │
├──────────────────────────┬──────────────────────────────────┤
│  PRIMA DI F1             │  CON F1                          │
│  [sfondo bianco]         │  [sfondo #f8f9fa]                │
│                          │                                  │
│  "Non vuole smettere"    │  Il campo mostra A4 (limite      │
│  "È un capriccio"        │  reale: libro chiuso) e A5       │
│  "Ha voglia di ancora"   │  (desiderio orientato: mano      │
│  "Va gestito"            │  tesa, vocalizzazione verso      │
│                          │  l'adulto — A2 riconosciuta).    │
│  [chips: comportamento,  │  [chips: struttura, campo,       │
│   stato interno]         │   relazionale]                   │
│                          │                                  │
│  → Cosa non si vede:     │  → Cosa diventa visibile:        │
│  la struttura del campo  │  la struttura del campo          │
└──────────────────────────┴──────────────────────────────────┘
```

**Nota:** La colonna "Prima di F1" non è caricaturale — usa le letture più comuni, quelle che ogni professionista riconosce come proprie. La colonna "Con F1" non è superiore: è semplicemente diversa. Il tono deve essere rispettoso delle letture precedenti, non trionfalistico.

**Comportamento:** Statico. La citazione in cima è la stessa scena del caso-guida — il professionista la riconosce dai moduli precedenti.

---

### Slide 7.2 — "Statuto epistemologico: cosa significa 'il campo mostra'"

**Tipo:** `standard`
**Accent:** `#2c3e50`
**Dati:** `STATUTO_EPISTEMOLOGICO`

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Box centrale — bordo grigio-blu spesso]                   │
│  "Il campo mostra..."                                       │
│  [testo grande, quasi tipografico]                          │
│  Non: "il bambino è..."                                     │
│  Non: "la situazione dimostra che..."                       │
│  Non: "secondo la mia interpretazione..."                   │
├─────────────────────────────────────────────────────────────┤
│  TRE PROPRIETÀ DELLA LETTURA STRUTTURALE                    │
│  [Tre card verticali — cliccabili]                          │
│                                                             │
│  [P1 Relazionale]  [P2 Non-valutativa]  [P3 Non-causale]   │
│  [sottotitolo]     [sottotitolo]         [sottotitolo]      │
│                                                             │
│  [Card cliccata espande panel con:]                         │
│  · descrizione                                              │
│  · esempio_corretto (box verde)                             │
│  · esempio_scorretto (box rosato)                           │
│  · perche_conta (corsivo)                                   │
├─────────────────────────────────────────────────────────────┤
│  [Due colonne: produce / non produce]                       │
│  F1 PRODUCE                │  F1 NON PRODUCE               │
│  · vocabolario strutturale │  · diagnosi                   │
│  · letture di campo        │  · prescrizioni               │
│  · base per dialogo inter- │  · spiegazioni causali        │
│    professionale           │  · profili individuali        │
│  · materiale per F2        │                               │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:** Le tre card delle proprietà usano uno stile tab/card orizzontale. Click su una card → espande un panel sotto le tre card (non dentro la card stessa, per non spezzare il layout). Il panel mostra i quattro campi. Una sola card espansa alla volta.

**Nota di tono:** Il box "Il campo mostra..." deve essere tipograficamente dominante nella slide — è la formula-cardine di tutto F1. Grandi, centrata, nel colore `#2c3e50`. I tre "Non:" sotto sono in tono minore, grigio, ma leggibili.

---

### Slide 7.3 — "I tre limiti costitutivi di F1"

**Tipo:** `standard`
**Accent:** `#2c3e50`
**Dati:** `LIMITI_F1`

**Layout:** Tre blocchi verticali con ExpandableCards

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Tre cose che F1 non può fare — e perché va bene   │
├─────────────────────────────────────────────────────────────┤
│  [Box introduttivo]                                         │
│  "I limiti di F1 non sono difetti: sono scelte strutturali. │
│  F1 è uno strumento specifico — usarlo bene significa       │
│  sapere dove finisce."                                      │
├─────────────────────────────────────────────────────────────┤
│  [L1] F1 non diagnostica          [ExpandableCard — chiusa] │
│       ↓ click                                               │
│  [descrizione]                                              │
│  [perche_non_e_un_difetto — box verde]                      │
│  [cosa_fa_invece — box neutro]                              │
│  [rischio_da_evitare — box rosato]                          │
│                                                             │
│  [L2] F1 non prescrive            [ExpandableCard — chiusa] │
│  [L3] F1 non spiega causalmente   [ExpandableCard — chiusa] │
└─────────────────────────────────────────────────────────────┘
```

**Comportamento:** Tre ExpandableCards verticali (non a griglia). Ogni card mostra il limite nello stato chiuso. Al click espande con i quattro sottocampi. Una sola espansa alla volta.

**Nota critica:** Il campo `rischio_da_evitare` è il più importante in questa slide: mostra concretamente cosa succede quando F1 viene usato oltre i suoi limiti. Deve essere visivamente distinto — sfondo rosato o arancione tenue, bordo sottile — non allarmistico, ma preciso.

---

### Slide 7.4 — "Il passaggio a F2: dalla fondazione all'analisi"

**Tipo:** `diagram`
**Accent:** `#2c3e50`
**Dati:** `PASSAGGIO_F2`

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Diagramma a due livelli]                                  │
│                                                             │
│  ┌──────────────────────┐    ┌──────────────────────────┐  │
│  │  F1                  │───→│  F2                      │  │
│  │  Fondazione          │    │  Analisi delle pratiche  │  │
│  │  ontologica          │    │  di cura                 │  │
│  │  "Il campo è..."     │    │  "Come la cura agisce    │  │
│  │                      │    │   nel campo"             │  │
│  └──────────────────────┘    └──────────────────────────┘  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  COSA PORTA F1 A F2 — tre bridge                           │
│  [Tre righe, cliccabili]                                    │
│                                                             │
│  [c1] Il bambino come soggetto →  F2 analizza pratiche     │
│       verso un soggetto, non un oggetto                     │
│  [c2] I sei assi strutturali   →  F2 ha il vocabolario     │
│       per descrivere gli effetti delle pratiche             │
│  [c3] Lo statuto epistemol.    →  F2 lavora su letture     │
│       di campo, non su diagnosi                             │
├─────────────────────────────────────────────────────────────┤
│  DUE COLONNE: domande di F2 / domande di F3 e oltre        │
│  "F2 può chiedere:"       │  "Solo F3 e oltre possono:     │
│  [lista domande F2]       │  [lista domande F3+]           │
├─────────────────────────────────────────────────────────────┤
│  [Box confine — bordo tratteggiato]                         │
│  "F1 finisce dove comincia la prescrizione."               │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:** Il diagramma F1→F2 è semplice: due box con freccia. Le tre righe "bridge" non sono cliccabili — sono testo statico con una freccia visiva (→) tra da_f1 e permette_a_f2. Le due colonne di domande usano `domande_che_f2_puo_fare` e `domande_che_solo_f3_oltre_possono_fare`. Il box confine finale è visivamente separato con bordo tratteggiato `#2c3e50`.

**Nota:** F2 non deve essere descritto in dettaglio: il professionista sta per entrarci. Bastano la metafora e le domande-guida.

---

### Slide 7.5 — "La scena annotata finale: tutti e sei gli assi"

**Tipo:** `narrative`
**Accent:** `#2c3e50`
**Dati:** `SCENE_HTML_M7`, `ANNOTAZIONI_M7`
**Componente:** `AnnotatedScene` — esacromatico (tutti e sei i colori)

**Questa è la scena più densa del corso: 10 annotazioni, 6 assi, alcuni badge doppi.**

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] La scena letta con tutti e sei gli assi           │
├─────────────────────────────────────────────────────────────┤
│  [Legenda completa — 6 colori, 2 righe]                     │
│  [■ A1 teal] [■ A2 verde] [■ A3 verde ch.]                  │
│  [■ A4 rosso] [■ A5 viola] [■ A6 arancio]                   │
├─────────────────────────────────────────────────────────────┤
│  [AnnotatedScene — 10 span cliccabili]                      │
│  "Il bambino attraversa la stanza portando il peso          │
│   del corpo in avanti..."                                    │
│                                                             │
│  [Ogni span evidenziato nel colore del suo asse]            │
│  [Badge doppi per le annotazioni con due assi]              │
├─────────────────────────────────────────────────────────────┤
│  [Nota sotto la scena]                                      │
│  "Tutti gli assi sono co-presenti. La sequenza con cui      │
│   li hai esplorati nei moduli non è l'ordine in cui         │
│   compaiono nel campo: compaiono tutti insieme."            │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione AnnotatedScene esacromatica:**

```javascript
AnnotatedScene(SCENE_HTML_M7, ANNOTAZIONI_M7, container);
```

La legenda in questa slide deve mostrare obbligatoriamente tutti e sei i colori — due righe di tre. La nota sotto la scena è il momento epistemologico più diretto dell'intera slide: "compaiono tutti insieme" chiude il cerchio aperto dalla distinzione gerarchia/co-presenza di M6.

**Gestione badge doppi:** Le annotazioni `m7-a6-3` (A6+A3) e `m7-a3-2` (A3+A6) mostrano due badge nel tooltip/panel. Ogni tooltip in questa scena deve essere costruito per reggere visivamente due badge affiancati — verificare che il layout non si rompa.

**Nota di densità:** 10 annotazioni in una scena sono molte. Considerare un layout in cui gli span di assi diversi abbiano underline di spessori leggermente diversi (A1 più spesso, A6 più sottile) per facilitare la distinzione a schermo — mantenendo però i colori come criterio primario.

---

### Slide 7.6 — "Il guardrail come pratica professionale"

**Tipo:** `comparison`
**Accent:** `#2c3e50`
**Dati:** `GUARDRAIL_F1_COMPLETO`

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [GuardrailBadge — variante expanded]                       │
│  G-F1: "Ogni output di F1 deve essere utilizzabile          │
│  senza descrivere il bambino come individuo isolato."       │
│                                                             │
│  [Test pratico — box evidenziato]                           │
│  "Cancella mentalmente i riferimenti al bambino.            │
│   Se rimane qualcosa di significativo, l'output era         │
│   strutturale. Se non rimane nulla, era una descrizione     │
│   individuale."                                             │
├─────────────────────────────────────────────────────────────┤
│  TRE SCENARI — ExpandableCards (una per contesto)           │
│                                                             │
│  [S1] Pediatra — restituzione post-visita                  │
│  [S2] Educatrice — documentazione                          │
│  [S3] Neuropsichiatra — colloquio con i genitori           │
│                                                             │
│  [Ogni card espande:]                                       │
│  · VIOLAZIONE (box rosato): descrizione individuale         │
│  · COMPLIANCE (box verde): lettura di campo                 │
│  · COSA CAMBIA (corsivo): la differenza operativa           │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:** Il `GuardrailBadge` in cima usa il `testo_completo` del guardrail. Il box del "test pratico" è visivamente distinto — sfondo giallo pallido, bordo sottile, testo in corsivo parziale. I tre scenari sono ExpandableCards verticali, stessa logica delle slide precedenti.

**Nota:** Questa è l'unica slide del corso in cui il guardrail viene applicato a tre contesti professionali diversi (pediatra, educatrice, neuropsichiatra). Il professionista che legge si riconosce almeno in uno dei tre. La riconoscibilità è il punto: non esempi astratti, ma situazioni che ogni professionista dell'area 0-6 ha già vissuto.

---

### Slide 7.7 — "La fondazione è posta"

**Tipo:** `standard`
**Accent:** `#2c3e50`
**Dati:** `SEI_VERBI_CHIAVE`, `CHIUSURA_CORSO`

**Slide di chiusura del corso. Nessun nuovo contenuto — solo la sintesi definitiva.**

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Sei verbi — riga orizzontale, tipograficamente dominanti] │
│                                                             │
│  abitare · riconoscere · scambiare ·                       │
│  incontrare · orientarsi · situarsi                         │
│                                                             │
│  [ogni verbo nel colore del suo asse]                       │
│  [font-size: 1.4em circa, semibold]                         │
├─────────────────────────────────────────────────────────────┤
│  [Sei badge assi — riga orizzontale, tutti colorati]        │
│  [A1] [A2] [A3] [A4] [A5] [A6]                             │
│  [non cliccabili: sono un'icona, non un'interazione]        │
├─────────────────────────────────────────────────────────────┤
│  [Testo di chiusura — centrato, non in colonna]             │
│  "F1 non ha insegnato a osservare meglio.                   │
│   Ha insegnato a osservare diversamente: il campo invece    │
│   del bambino, la struttura invece del comportamento,       │
│   la lettura invece della valutazione."                     │
├─────────────────────────────────────────────────────────────┤
│  [Domanda finale — box leggermente evidenziato]             │
│  "Quando osservi un bambino e un adulto leggere insieme,    │
│   cosa vedi adesso che non vedevi prima?"                   │
├─────────────────────────────────────────────────────────────┤
│  [Box verso F2 — grigio chiaro, discreto]                   │
│  → F2: Analisi delle pratiche di cura nel campo ontologico  │
│  "Porta con te il vocabolario: ne avrai bisogno."           │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione tipografica dei sei verbi:** I sei verbi usano `SEI_VERBI_CHIAVE`. Ogni verbo è un `<span>` con `color: [colore asse]`. Il separatore "·" è in `#95a5a6` neutro. I verbi non sono su una riga sola (troppo stretti): su due righe da 3, centrate. Font: semibold, dimensione maggiore del corpo del testo.

**Tono della slide:** La slide non è un riepilogo. Non ripasssa i sei assi. Dice cosa è cambiato. La domanda finale ("cosa vedi adesso che non vedevi prima?") è retorica ma non decorativa: è la verifica pratica dell'intero corso. Il box verso F2 è sobrio e piccolo — non un teaser, ma un'indicazione di direzione.

**Comportamento:** Completamente statico. Nessuna interattività. La chiusura è silenziosa.

---

## Note tecniche trasversali

### La scena M7 come scena-sintesi
`SCENE_HTML_M7` è deliberatamente la più ricca del corso: 10 span annotabili, 6 assi, 2 badge doppi. Non è costruita per essere analizzata asse per asse (lo studente l'ha già fatto nei moduli precedenti): è costruita per essere vista tutta insieme, come campo. L'`AnnotatedScene` in M7 deve funzionare con 10 annotazioni senza degradare le performance: verificare che il lookup `data-annotation-id` rimanga O(n) con array piccolo.

### Badge doppi — pattern consolidato
In M7 appaiono due badge doppi (`m7-a6-3`: A6+A3, `m7-a3-2`: A3+A6). Il pattern è stato introdotto in M4 (bicolore A2+A3), riutilizzato in M5 e M6. Claude Code può considerare di estrarre un helper:
```javascript
function renderAnnotationBadges(annotation) {
  const assi = annotation.assi_multipli || [annotation.asse];
  return assi.map(a => renderBadge(window.SEI_ASSI.find(s => s.id === a))).join('');
}
```

### `SEI_VERBI_CHIAVE` e `window.SEI_ASSI`
`SEI_VERBI_CHIAVE` è una costante locale che rideclara i verbi chiave già presenti in `window.SEI_ASSI` (campo `verbo_chiave`). In alternativa, Claude Code può leggerli direttamente:
```javascript
const SEI_VERBI_CHIAVE = window.SEI_ASSI.map(a => ({
  asse: a.id.toUpperCase(),
  verbo: a.verbo_chiave,
  colore: a.colore
}));
```
Entrambi gli approcci sono corretti — la costante locale è più leggibile nel codice del modulo.

### Tono di M7 vs toni precedenti
M7 non ha asse strutturale da presentare: ha una funzione epistemologica e di chiusura. Il tono deve essere diverso — più riflessivo, meno dimostrativo. Le slide 7.1 e 7.7 in particolare devono evitare il formato "definizione + esempi + errori" che ha caratterizzato M3-M6. Sono slide narrative, non analitiche. Claude Code non deve applicare automaticamente i pattern degli assi a queste due slide.

### La domanda finale come ultimo output del corso
"Quando osservi un bambino e un adulto leggere insieme, cosa vedi adesso che non vedevi prima?" è la domanda con cui il corso chiude. Non ha risposta nella slide — la risposta è il corso intero. Questa domanda non deve essere trattata come un prompt interattivo (nessun campo di input, nessun bottone). È una domanda da lasciare aperta, visivamente isolata, tipograficamente in evidenza.
