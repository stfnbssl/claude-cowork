# F1 — Modulo 5: Assi 4 e 5 — Limite e desiderio nell'incontro con il libro

## Metadati

| Campo | Valore |
|-------|--------|
| ID modulo | M5 |
| Titolo breve | Assi 4 e 5: Limite e desiderio |
| Titolo operativo | Limite e desiderio nell'incontro con il libro |
| Colore accent A4 | `#c0392b` |
| Colore accent A5 | `#8e44ad` |
| Colore accent modulo (header/nav) | `#c0392b` |
| Tipo di modulo | Asse strutturale (coppia) |
| Slide count | 7 |
| File JS | `F1/f1_m05.js` |
| Dipendenze globali | `window.SEI_ASSI`, `window.CASO_GUIDA_F1` |

---

## Nota metodologica

Il titolo operativo "Limite e desiderio nell'incontro con il libro" posiziona l'albo illustrato come il fenomeno osservabile che rende A4 e A5 simultaneamente visibili — esattamente come l'alternanza dei turni aveva reso visibili A2 e A3 nel modulo precedente. La chiusura del libro (A4) e la richiesta di rilettura (A5) non sono due eventi separati: sono il campo che mostra la coppia strutturale nel suo funzionamento.

**Struttura pedagogica del modulo:**
- Slide 5.1 entra dall'errore (frustrazione/capriccio) per creare il bisogno di un'alternativa
- Slide 5.2–5.3 presentano A4 e A5 separatamente con le forme osservabili nell'albo
- Slide 5.4 mostra la coppia strutturale: il limite rende possibile il desiderio (non si oppone ad esso)
- Slide 5.5 inserisce A4 e A5 nella catena completa (A1→A2→A3→A4→A5)
- Slide 5.6 presenta gli errori tipici in formato ExpandableCards 2×2
- Slide 5.7 è l'AnnotatedScene bicolore: il momento della rilettura nel caso-guida

**Nota sui colori:** A4 usa `#c0392b` (rosso — il limite come struttura dura del reale), A5 usa `#8e44ad` (viola — il desiderio come orientamento che eccede il dato). Le due tinte devono essere chiaramente distinguibili nelle annotazioni della scena e nei badge assi.

**Nota sulle dipendenze:** A4 dipende da A1 (il limite è incontrato corporalmente, non solo cognitivizzato) e da A2 (il limite emerge in un campo di alterità, non in isolamento). A5 dipende da A4 (non può esserci desiderio senza un limite verso cui orientarsi) e da A3 (la forma del desiderio è normativamente riconoscibile). Queste dipendenze vanno visualizzate nella slide 5.5 e richiamate nelle definizioni.

---

## Costanti JavaScript (`F1/f1_m05.js`)

```javascript
// ─────────────────────────────────────────────
// M5 — Assi 4 e 5: Limite e desiderio nell'incontro con il libro
// ─────────────────────────────────────────────

const ASSE_4_DETTAGLIO = {
  id: "a4",
  nome: "Limite reale",
  colore: "#c0392b",
  verbo_chiave: "incontrare",
  // "Incontrare" si oppone a: subire, scontrarsi, evitare, superare
  contrari: ["subire", "scontrarsi", "evitare", "superare"],
  definizione: "Il limite reale è la discontinuità strutturale del campo: ciò che è e non cambia indipendentemente dall'intenzione o dall'investimento del bambino. Non è un confine imposto dall'esterno né una mancanza da colmare, ma la condizione entro cui il desiderio trova direzione.",
  non_e: [
    "la frustrazione emotiva conseguente al limite",
    "la regola stabilita dall'adulto",
    "l'ostacolo da superare o negoziare",
    "il trauma da evitare",
    "il 'no' educativo"
  ],
  e: [
    "la discontinuità strutturale che il campo presenta",
    "la resistenza del reale all'investimento",
    "la condizione che rende possibile l'orientamento (A5)",
    "un dato strutturale, non una valutazione"
  ],
  dipendenza_da_a1: "Il limite è incontrato corporalmente: il bambino lo percepisce con il corpo prima di rappresentarlo. Senza A1 (abitare l'esperienza), il limite resterebbe un concetto astratto.",
  dipendenza_da_a2: "Il limite emerge come limite in un campo di alterità: non è il bambino da solo che incontra il muro, ma il campo bambino-adulto-oggetto che produce la discontinuità.",
  forme_nel_libro: [
    {
      id: "fl1",
      forma: "La pagina che si volta",
      descrizione: "Ogni pagina girata è un limite reale: l'immagine scompare, quella precedente non è più accessibile senza azione. Il bambino incontra la sequenzialità irreversibile dell'albo.",
      osservabile: "Lo sguardo che insegue la pagina che scompare; il tentativo di tornare indietro",
      asse: "a4"
    },
    {
      id: "fl2",
      forma: "Il libro che si chiude",
      descrizione: "La chiusura del libro è la forma più densa di A4 nell'albo: il campo grafico scompare, l'accesso all'immagine è interrotto dal gesto dell'adulto o dal tempo.",
      osservabile: "Il seguire con lo sguardo il gesto di chiusura; la mano tesa verso il libro chiuso",
      asse: "a4"
    },
    {
      id: "fl3",
      forma: "L'immagine che non risponde",
      descrizione: "Le figure nell'albo non agiscono: il bambino può indicarle, vocalizzare, toccarle — ma non cambiano. Questa non-responsività è un limite reale, non un difetto dell'oggetto.",
      osservabile: "Il toccare ripetuto della figura; il vocalizzare verso di essa come si vocalizza verso una persona",
      asse: "a4"
    },
    {
      id: "fl4",
      forma: "La storia che ha una fine",
      descrizione: "L'albo ha struttura narrativa con conclusione. Il bambino incontra il limite della narrazione come limite del reale: la storia finisce, non perché qualcuno l'abbia deciso, ma perché ha quella forma.",
      osservabile: "La reazione alla pagina finale; la richiesta di continuazione o di riinizio",
      asse: "a4"
    }
  ],
  domande_per_contesto: {
    clinico: "Quali forme di limite reale il bambino incontra nella sessione? Come le incontra (corporalmente, relazionalmente)? C'è evitamento strutturale del limite?",
    pedagogico: "L'attività proposta contiene limiti reali o solo regole esterne? Il limite dell'albo è lasciato emergere o viene anticipato/ammorbidito dall'adulto?",
    genitoriale: "Come descrive il momento in cui il bambino incontra un limite? Usa il linguaggio della frustrazione o riesce a osservare la struttura del campo?"
  },
  guardrail: "A4 non misura la tolleranza alla frustrazione né la capacità di accettare i limiti. Descrive la struttura del campo: ci sono o non ci sono discontinuità reali, e come il bambino le incontra."
};

const ASSE_5_DETTAGLIO = {
  id: "a5",
  nome: "Desiderio come orientamento",
  colore: "#8e44ad",
  verbo_chiave: "orientarsi",
  // "Orientarsi" si oppone a: mancare, volere, preferire, bramare
  contrari: ["mancare", "bramare", "pretendere", "dipendere"],
  definizione: "Il desiderio è la direzione strutturale del campo verso qualcosa di significativo. Non descrive uno stato interno del bambino (ciò che gli manca o vuole), ma una tensione osservabile: il campo si orienta. Il desiderio non è assenza di qualcosa, ma presenza di una direzione.",
  non_e: [
    "la volontà soggettiva di avere qualcosa",
    "il capriccio o il bisogno non regolato",
    "la preferenza individuale per uno stimolo",
    "la mancanza da colmare",
    "l'attaccamento a un oggetto specifico"
  ],
  e: [
    "l'orientamento strutturale del campo verso un polo",
    "la tensione attiva che il campo esprime",
    "la direzione che il limite (A4) rende possibile",
    "un osservabile strutturale, non uno stato interno"
  ],
  dipendenza_da_a4: "Il desiderio si orienta verso qualcosa perché esiste un limite reale: senza la discontinuità di A4, non c'è una direzione verso cui orientarsi. Il limite non si oppone al desiderio: lo istituisce.",
  dipendenza_da_a3: "La forma del desiderio è normativamente riconoscibile: il bambino non si orienta in modo caotico, ma con gesti e vocalizzazioni che hanno forma condivisa (A3). La normatività emergente dà forma osservabile al desiderio.",
  forme_nel_libro: [
    {
      id: "fo1",
      forma: "Il puntare verso il libro",
      descrizione: "Il gesto deittico verso l'albo chiuso è orientamento strutturale: il campo si dirige verso il limite incontrato. Non è 'volere il libro' come oggetto, ma il campo che si orienta verso il polo significativo.",
      osservabile: "L'indice teso verso il libro; la direzione dello sguardo che anticipa e segue",
      asse: "a5"
    },
    {
      id: "fo2",
      forma: "La richiesta di rilettura",
      descrizione: "Chiedere di rileggere l'albo appena finito è la forma più chiara di A5: il campo si orienta nuovamente verso il limite superato. Non è ripetizione per abitudine, ma ri-orientamento strutturale.",
      osservabile: "La vocalizzazione ascendente; il portare il libro all'adulto; il gesto di apertura imitato",
      asse: "a5"
    },
    {
      id: "fo3",
      forma: "La vocalizzazione anticipatoria",
      descrizione: "Prima ancora che la pagina si volti, il bambino vocalizza anticipando l'immagine successiva. Il campo si orienta verso ciò che viene, mostrando un desiderio orientato nel tempo.",
      osservabile: "La vocalizzazione che precede il voltare pagina; l'eccitazione motoria anticipatoria",
      asse: "a5"
    },
    {
      id: "fo4",
      forma: "La resistenza strutturale alla chiusura",
      descrizione: "Quando il libro si chiude, il bambino mantiene il corpo orientato verso di esso — mano tesa, sguardo fisso, peso in avanti. Non è una protesta: è il campo che continua a mostrare il suo orientamento oltre il limite.",
      osservabile: "La postura protesa; la mano che non si ritira; l'assenza di reorientamento verso altro",
      asse: "a5"
    }
  ],
  domande_per_contesto: {
    clinico: "Verso quali poli il campo mostra orientamento strutturale? Il desiderio ha forme riconoscibili (A3) o è frammentato? C'è orientamento verso l'adulto o solo verso l'oggetto?",
    pedagogico: "L'ambiente proposto offre poli verso cui orientarsi? Il desiderio del bambino è letto come capriccio o come orientamento? L'adulto risponde alla direzione o solo al comportamento?",
    genitoriale: "Riesce a descrivere verso cosa il bambino si orienta senza interpretare subito cosa 'vuole' o 'cerca'?"
  },
  guardrail: "A5 non misura la forza del desiderio né la sua appropriatezza. Descrive la struttura del campo: c'è un orientamento, ha forma osservabile, e dipende da un limite (A4) e da una norma emergente (A3)."
};

const COPPIA_STRUTTURALE_A4_A5 = {
  principio: "Il limite reale rende possibile il desiderio come orientamento. Senza una discontinuità strutturale (A4), non esiste una direzione verso cui il campo possa orientarsi (A5). I due assi non sono opposti: sono complementari strutturalmente.",
  contro_intuizione: "La cultura comune tratta limite e desiderio come antagonisti: più limite, meno desiderio. La lettura strutturale inverte questa logica: è il limite che istituisce la direzione del desiderio.",
  schema_visivo: [
    {
      passo: 1,
      asse: "A4",
      colore: "#c0392b",
      evento: "Il libro si chiude",
      struttura: "Il campo incontra una discontinuità reale: il limite è là, non negoziabile"
    },
    {
      passo: 2,
      asse: "A4→A5",
      colore: "#a0306a",
      evento: "Il limite genera direzione",
      struttura: "La discontinuità produce un polo: il campo si orienta verso di esso"
    },
    {
      passo: 3,
      asse: "A5",
      colore: "#8e44ad",
      evento: "Il bambino tende la mano verso il libro chiuso",
      struttura: "Il desiderio è osservabile: è il campo che si orienta, non 'il bambino che vuole'"
    },
    {
      passo: 4,
      asse: "A5+A3+A2",
      colore: "#7d3c98",
      evento: "La richiesta prende forma",
      struttura: "Il desiderio usa la norma (A3) e si rivolge all'altro (A2): il campo si complessa"
    }
  ],
  esempio_nel_libro: {
    situazione: "Fine della lettura condivisa: l'adulto chiude l'albo",
    a4: "La chiusura è il limite reale: il campo grafico scompare, il gesto non è reversibile dal bambino",
    a5: "Il bambino si orienta verso il libro chiuso con mano tesa, vocalizzazione, peso del corpo",
    connessione: "La chiusura (A4) non blocca il desiderio: lo dirige. Il bambino sa verso cosa orientarsi perché il libro è là — chiuso, reale, presente nel suo limite",
    nota: "Se il libro non ci fosse affatto, non ci sarebbe limite reale; se il bambino non lo avesse 'abitato' (A1), il limite non avrebbe consistenza esperienziale"
  },
  dipendenze_complete: "A4 ← A1 (incarnato) + A2 (alterità). A5 ← A4 (limite) + A3 (normatività). La catena strutturale completa: A1 fonda A4 che fonda A5 che si esprime attraverso A3 verso A2."
};

const CATENA_STRUTTURALE_M5 = [
  {
    asse: "A1",
    nome: "Abitare l'esperienza",
    colore: "#1a6b8a",
    ruolo_verso_a4: "Il bambino incontra il limite corporalmente: lo sente nella postura, nel peso, nel gesto che non completa. Senza A1, il limite sarebbe un'astrazione cognitiva.",
    attivo: true
  },
  {
    asse: "A2",
    nome: "Alterità",
    colore: "#2d6a4f",
    ruolo_verso_a4: "Il limite emerge in un campo di alterità: non è il bambino solo contro il reale, ma il campo relazionale che produce e contiene la discontinuità.",
    attivo: true
  },
  {
    asse: "A3",
    nome: "Normatività emergente",
    colore: "#27ae60",
    ruolo_verso_a5: "Il desiderio prende forma normativamente riconoscibile: il bambino si orienta con gesti e vocalizzazioni che hanno struttura condivisa.",
    attivo: true
  },
  {
    asse: "A4",
    nome: "Limite reale",
    colore: "#c0392b",
    ruolo_nella_catena: "Produce il polo verso cui il desiderio si orienta. Fonda A5.",
    attivo: true
  },
  {
    asse: "A5",
    nome: "Desiderio come orientamento",
    colore: "#8e44ad",
    ruolo_nella_catena: "La tensione strutturale che emerge dal limite. Dipende da A4 e si esprime attraverso A3 verso A2.",
    attivo: true
  },
  {
    asse: "A6",
    nome: "Storicità e temporalità",
    colore: "#95a5a6",
    ruolo_nella_catena: "Sarà analizzato nel modulo successivo.",
    attivo: false
  }
];

const ERRORI_TIPICI_A4_A5 = [
  {
    id: "e1",
    asse: "A4",
    tipo: "riduzione psicologica",
    colore: "#c0392b",
    etichetta: "Il limite → frustrazione emotiva",
    descrizione: "Il limite reale viene letto come evento emotivo: il bambino 'si frustra', 'non tollera l'attesa', 'ha bassa soglia di frustrazione'. L'analisi scivola dall'osservabile strutturale all'inferenza sullo stato interno.",
    esempio_errato: "Quando chiudo il libro piange sempre. Ha difficoltà a gestire la frustrazione.",
    lettura_strutturale: "Il campo mostra un bambino nell'incontro con il limite reale (A4): la reazione è l'orientamento del campo verso il polo perduto, non la prova di una difficoltà emotiva.",
    cosa_si_perde: "La differenza tra 'incontrare un limite' (strutturale) e 'essere frustrati' (psicologico). Il primo è un osservabile; il secondo è un'inferenza che richiede dati diversi."
  },
  {
    id: "e2",
    asse: "A4",
    tipo: "riduzione pedagogica",
    colore: "#c0392b",
    etichetta: "Il limite → regola da insegnare",
    descrizione: "Il limite strutturale viene sostituito da una regola normativa: 'dobbiamo insegnare che i libri non si strappano', 'deve imparare che quando finisce, finisce'. La norma esterna cancella il limite come fatto strutturale del campo.",
    esempio_errato: "Ogni volta che chiudo l'albo lo uso come momento per insegnargli che bisogna accettare quando le cose finiscono.",
    lettura_strutturale: "Il bambino già incontra il limite come struttura del reale (A4). Sovrapporgli una norma esterna non aggiunge nulla strutturalmente: sposta l'analisi dal campo al comportamento.",
    cosa_si_perde: "La possibilità di osservare come il bambino incontra il limite (con quale forma corporale, relazionale, temporale) senza immediatamente trasformarlo in un'occasione pedagogica."
  },
  {
    id: "e3",
    asse: "A5",
    tipo: "riduzione comportamentale",
    colore: "#8e44ad",
    etichetta: "Il desiderio → capriccio o abitudine",
    descrizione: "L'orientamento strutturale del campo viene letto come comportamento individuale problematico: 'vuole sempre rileggere lo stesso libro', 'fa i capricci quando smettono', 'si è fissato'. La strutturalità del desiderio scompare.",
    esempio_errato: "Ogni sera vuole che gli rileggiamo lo stesso albo almeno tre volte. È diventato un capriccio.",
    lettura_strutturale: "Il campo mostra un orientamento strutturale stabile verso un oggetto significativo (A5). La ripetizione non è capriccio: è il desiderio che si orienta con consistenza verso qualcosa che ha valore strutturale nel campo.",
    cosa_si_perde: "La possibilità di riconoscere nel desiderio ripetuto un indicatore strutturale positivo: il campo ha poli di orientamento stabili, il desiderio ha forma riconoscibile, l'adulto è riconosciuto come agente."
  },
  {
    id: "e4",
    asse: "A5",
    tipo: "riduzione cognitivista",
    colore: "#8e44ad",
    etichetta: "Il desiderio → preferenza per stimoli",
    descrizione: "Il desiderio viene spiegato attraverso le proprietà dell'oggetto: 'preferisce questo libro perché ha i colori vivaci', 'gli piace perché c'è il cane e lui ha un cane'. La strutturalità del desiderio viene ridotta a stimulus-response.",
    esempio_errato: "Preferisce gli albi con molti colori e animali. È la sua preferenza cognitiva.",
    lettura_strutturale: "Il campo mostra un orientamento (A5) che non si spiega solo con le proprietà dell'oggetto. L'albo è un polo di desiderio perché è stato abitato (A1) in un campo di alterità (A2) con forme riconoscibili (A3): non perché abbia certi colori.",
    cosa_si_perde: "La dimensione strutturale e relazionale del desiderio: il bambino non si orienta verso un oggetto-stimolo, ma verso un polo che ha acquisito valore nel campo."
  }
];

// ─────────────────────────────────────────────
// SCENE HTML — pre-costruita con span annotabili
// Scena: fine della lettura condivisa — il bambino chiede di rileggere
// Contesto: educatrice + bambino 20 mesi, albo illustrato sul tavolo basso
// ─────────────────────────────────────────────
const SCENE_HTML_M5 = `
<p>L'educatrice arriva all'ultima pagina dell'albo. 
<span class="annotabile" data-annotation-id="m5-a4-1">Chiude il libro con un gesto lento</span>, 
posandolo sul tavolo. Il bambino, seduto di fronte a lei, 
<span class="annotabile" data-annotation-id="m5-a1-1">segue il movimento con lo sguardo e con il corpo</span> — 
il peso che si sposta leggermente in avanti, le mani che smettono di muoversi. 
Un momento di pausa nel campo.</p>

<p>Poi il bambino 
<span class="annotabile" data-annotation-id="m5-a5-1">tende la mano verso il libro chiuso</span>. 
<span class="annotabile" data-annotation-id="m5-a5-2">Emette una vocalizzazione ascendente</span>, 
breve, orientata: non verso il tavolo, ma verso l'educatrice. 
Lei incontra lo sguardo: «Ancora?».</p>

<p>Il bambino 
<span class="annotabile" data-annotation-id="m5-a4-2">non distoglie la mano dal libro</span> — 
il limite è là, reale, chiuso, sul tavolo. 
<span class="annotabile" data-annotation-id="m5-a5-3">Sposta il peso del corpo in avanti</span>: 
tutto l'orientamento del campo converge sull'albo. 
L'educatrice riapre alla prima pagina.</p>
`;

const ANNOTAZIONI_M5 = [
  {
    id: "m5-a4-1",
    label: "A4 — Limite reale",
    colore: "#c0392b",
    asse: "a4",
    annotazione: "La chiusura del libro è il limite reale per eccellenza nell'albo: il campo grafico scompare, l'accesso all'immagine è interrotto. Non è una regola, non è una sanzione — è la struttura dell'oggetto che si manifesta nel gesto.",
    note_tecniche: "Badge A4 rosso (#c0392b). Questo è il limite inaugurale della sequenza: tutto ciò che segue (A5) dipende da questo momento."
  },
  {
    id: "m5-a1-1",
    label: "A1 — Incarnato",
    colore: "#1a6b8a",
    asse: "a1",
    annotazione: "Il bambino incontra il limite prima di tutto corporalmente: il peso che si sposta, le mani che si fermano. A1 è la fondazione: il limite reale (A4) è percepito corporalmente, non astrattamente elaborato.",
    note_tecniche: "Badge A1 blu. Annotazione secondaria rispetto al focus A4/A5 del modulo. Evidenzia la dipendenza strutturale A4←A1."
  },
  {
    id: "m5-a5-1",
    label: "A5 — Desiderio (orientamento)",
    colore: "#8e44ad",
    asse: "a5",
    annotazione: "La mano tesa verso il libro chiuso è il desiderio reso osservabile: il campo si orienta verso il limite incontrato. Non è 'volere il libro' come oggetto — è la direzione strutturale del campo dopo l'incontro con A4.",
    note_tecniche: "Badge A5 viola (#8e44ad). Prima apparizione esplicita di A5 nella scena: il limite ha prodotto il polo."
  },
  {
    id: "m5-a5-2",
    label: "A5 + A3 — Desiderio con forma",
    colore: "#8e44ad",
    asse: "a5",
    annotazione: "La vocalizzazione ascendente è il desiderio che prende forma normativamente riconoscibile (A3): non un suono casuale, ma un pattern prosodico che il campo adulto-bambino ha co-costruito come richiesta. Il desiderio (A5) si esprime attraverso la norma emergente (A3).",
    note_tecniche: "Badge doppio A5+A3 o badge A5 con nota A3. La vocalizzazione è osservabile sia come orientamento (A5) che come forma condivisa (A3)."
  },
  {
    id: "m5-a4-2",
    label: "A4 — Il limite permane",
    colore: "#c0392b",
    asse: "a4",
    annotazione: "Il libro è ancora chiuso: il limite non è scomparso con il desiderio. L'analisi strutturale mostra due assi simultanei — il limite (A4) resta reale mentre il desiderio (A5) si orienta verso di esso. Non si escludono: coesistono.",
    note_tecniche: "Badge A4 rosso. Momento chiave per mostrare la simultaneità: A4 e A5 nello stesso campo, non in sequenza."
  },
  {
    id: "m5-a5-3",
    label: "A5 — Il campo intero si orienta",
    colore: "#8e44ad",
    asse: "a5",
    annotazione: "Lo spostamento del peso è orientamento incarnato (A1+A5): non solo la mano, ma tutto il corpo del bambino esprime la direzione del campo. Il desiderio non è nella testa — è nel campo, osservabile nella postura, nel peso, nella tensione muscolare.",
    note_tecniche: "Badge A5 viola con richiamo a A1. Annotazione conclusiva: mostra come il desiderio pervade il campo strutturalmente, non solo gestualmente."
  }
];

const GUARDRAIL_M5 = {
  id: "g-m5",
  modulo: "M5",
  testo: "A4 e A5 descrivono strutture del campo, non stati interni del bambino. 'Incontrare un limite' non equivale a 'essere frustrati'. 'Orientarsi con desiderio' non equivale a 'volere qualcosa'. Le strutture sono osservabili nel campo; gli stati interni sono inferenze che richiedono dati e framework diversi.",
  violazione: "Marco si è frustrato quando ho chiuso il libro. Non riesce ad accettare i limiti.",
  compliance: "Il campo mostra il bambino nell'incontro con il limite reale dell'albo (A4); il desiderio si orienta verso la rilettura con forma riconoscibile (A5). Non osserviamo stati interni: osserviamo strutture.",
  versione_compatta: "A4 e A5 sono strutture del campo. Non descrivono come il bambino 'si sente'."
};
```

---

## Slide — Specifiche

### Slide 5.1 — "Frustrazione o struttura? Il problema di leggere il momento"

**Tipo:** `standard`
**Accent:** `#c0392b`
**Dati:** costruiti localmente — non richiede costanti dedicate

**Layout:** due colonne simmetriche con header e separatore visivo centrale

```
┌─────────────────────────────────────────────────────────────┐
│  Il bambino tende la mano verso il libro appena chiuso      │
│  e vocalizza verso l'educatrice.                            │
│  Come leggiamo questo momento?                              │
├──────────────────────┬──────────────────────────────────────┤
│  LETTURA COMUNE      │  COSA QUESTA LETTURA NON PUÒ VEDERE  │
│                      │                                      │
│  "Non vuole smettere"│  Il limite come struttura del reale  │
│  "Si è abituato"     │  Il desiderio come orientamento      │
│  "È un capriccio"    │  La relazione tra finire e volere    │
│  "Lo stiamo viziando │  La capacità di incontrare il reale  │
│   a forza di rile-   │  e di mantenersi orientati verso    │
│   ggere?"            │  di esso                             │
│                      │                                      │
│  [chips rossi: stato │  [chip viola: struttura]             │
│   interno, comporta- │                                      │
│   mento]             │                                      │
└──────────────────────┴──────────────────────────────────────┘
  → Questi due assi strutturali hanno un nome: A4 e A5
```

**Nota:** La colonna sinistra usa chip di colore rosso-arancio per marcare le letture comuni. La colonna destra usa chip viola neutro per indicare "strutture osservabili". La freccia finale introduce i due assi del modulo senza ancora nominarli formalmente — li nominerà la slide 5.2.

**Comportamento:** Nessuna interattività. Layout statico. Il titolo della slide usa un punto interrogativo deliberato per mantenere la tensione aperta.

---

### Slide 5.2 — "Asse 4: Il limite reale"

**Tipo:** `standard`
**Accent:** `#c0392b`
**Dati:** `ASSE_4_DETTAGLIO`
**Badge assi visibili:** A4 (grande, in evidenza)

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Badge A4 grande: "Asse 4 — Limite reale"]                 │
│  Verbo chiave: INCONTRARE                                    │
│  (non: subire / scontrarsi / evitare / superare)            │
├─────────────────────────────────────────────────────────────┤
│  [Blockquote definizione — bordo sinistro rosso]            │
│  "Il limite reale è la discontinuità strutturale del campo: │
│   ciò che è e non cambia indipendentemente dall'intenzione   │
│   o dall'investimento del bambino..."                        │
├──────────────────────┬──────────────────────────────────────┤
│  NON È               │  È                                   │
│  · frustrazione      │  · discontinuità strutturale         │
│  · regola esterna    │  · resistenza del reale              │
│  · ostacolo          │  · condizione del desiderio (A5)     │
│  · trauma            │  · dato strutturale                  │
├─────────────────────────────────────────────────────────────┤
│  QUATTRO FORME NELL'ALBO ILLUSTRATO                         │
│  [grid 2×2 — card cliccabili]                               │
│  [fl1] La pagina │ [fl2] Il libro  │                        │
│        che si    │       che si    │                        │
│        volta     │       chiude    │                        │
│  [fl3] L'immagine│ [fl4] La storia │                        │
│        che non   │       che ha    │                        │
│        risponde  │       una fine  │                        │
└─────────────────────────────────────────────────────────────┘
```

**Comportamento grid:** Le 4 card sono cliccabili. Ogni card, al click, espande un panel sotto la grid con `descrizione` e `osservabile` dalla forma corrispondente in `ASSE_4_DETTAGLIO.forme_nel_libro`. Una sola card aperta alla volta (accordion).

**Nota:** Il verbo chiave "INCONTRARE" è tipograficamente in evidenza (font-size maggiore, colore #c0392b). I contrari appaiono in piccolo sotto con una barratura leggera — non cancellati, ma secondari.

---

### Slide 5.3 — "Asse 5: Il desiderio come orientamento"

**Tipo:** `standard`
**Accent:** `#8e44ad`
**Dati:** `ASSE_5_DETTAGLIO`
**Badge assi visibili:** A5 (grande, in evidenza)

**Layout:** speculare a 5.2 ma con colore viola

```
┌─────────────────────────────────────────────────────────────┐
│  [Badge A5 grande: "Asse 5 — Desiderio come orientamento"]  │
│  Verbo chiave: ORIENTARSI                                    │
│  (non: mancare / bramare / pretendere / dipendere)          │
├─────────────────────────────────────────────────────────────┤
│  [Blockquote definizione — bordo sinistro viola]            │
│  "Il desiderio è la direzione strutturale del campo verso   │
│   qualcosa di significativo. Non descrive uno stato interno  │
│   del bambino, ma una tensione osservabile: il campo si      │
│   orienta."                                                  │
├──────────────────────┬──────────────────────────────────────┤
│  NON È               │  È                                   │
│  · volontà           │  · orientamento strutturale          │
│  · capriccio         │  · tensione attiva del campo         │
│  · preferenza        │  · direzione resa possibile da A4    │
│  · mancanza          │  · osservabile strutturale           │
├─────────────────────────────────────────────────────────────┤
│  QUATTRO FORME NELL'ALBO ILLUSTRATO                         │
│  [grid 2×2 — card cliccabili, accordeon come 5.2]          │
│  [fo1] Il puntare │ [fo2] La richiesta│                     │
│        verso il   │       di rilettura│                     │
│        libro      │                   │                     │
│  [fo3] La vocal.  │ [fo4] La resistenza│                    │
│        anticipat. │       alla chiusura│                    │
└─────────────────────────────────────────────────────────────┘
```

**Nota tecnica:** La slide 5.3 è strutturalmente identica alla 5.2 (stesso layout, stessa logica accordion) ma usa `#8e44ad` ovunque 5.2 usa `#c0392b`. Questo parallelismo visivo è intenzionale: le due slide mostrano che A4 e A5 hanno la stessa forma analitica, ma descrivono fenomeni complementari.

---

### Slide 5.4 — "La coppia strutturale: il limite rende possibile il desiderio"

**Tipo:** `diagram`
**Accent:** `#c0392b` (primario) con `#8e44ad` (secondario)
**Dati:** `COPPIA_STRUTTURALE_A4_A5`

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo grande centrato]                                   │
│  "Il limite non si oppone al desiderio: lo istituisce"      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Diagramma sequenziale — 4 passi orizzontali]             │
│                                                             │
│  [1 - rosso]     [freccia]  [2 - sfumato]  [freccia]       │
│  Il libro                   Il limite                       │
│  si chiude                  genera                          │
│  A4 attivo                  direzione                       │
│                                                             │
│  [freccia]                  [freccia]                       │
│  [4 - viola scuro]          [3 - viola]                    │
│  La richiesta               Il bambino                      │
│  prende forma               tende la mano                   │
│  A5+A3+A2                   A5 attivo                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [Box centrale grigio chiaro]                               │
│  CONTRO-INTUIZIONE                                          │
│  La cultura comune: più limite → meno desiderio             │
│  La lettura strutturale: il limite istituisce il desiderio  │
│  Senza A4 non c'è polo verso cui A5 possa orientarsi        │
├─────────────────────────────────────────────────────────────┤
│  [Esempio nel libro — box evidenziato]                      │
│  Chiusura (A4) → mano tesa + vocalizzazione (A5)            │
│  Il gesto di chiudere non blocca: produce la direzione      │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione diagramma:** I 4 passi usano `COPPIA_STRUTTURALE_A4_A5.schema_visivo`. Ogni passo è un box colorato con la tinta del campo `colore`. Le frecce sono semplici elementi CSS (→). Il box "CONTRO-INTUIZIONE" ha sfondo `#fff3f3` con bordo `#c0392b` tratteggiato — è il momento più didatticamente pregnante della slide.

**Comportamento:** Statico. Nessuna animazione. Il contrasto visivo tra i colori dei 4 passi (rosso → sfumato → viola → viola scuro) deve suggerire la progressione senza confondere.

---

### Slide 5.5 — "A4 e A5 nella catena strutturale"

**Tipo:** `diagram`
**Accent:** `#c0392b`
**Dati:** `CATENA_STRUTTURALE_M5`

**Layout:** Pipeline orizzontale — tutti e 6 gli assi, i primi 5 colorati, A6 grigio

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Come si regge la catena: dal corpo al desiderio   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [A1]──→[A2]──→[A3]──→[A4]──→[A5]──→[A6 grigio]           │
│  teal   verde  verde  rosso  viola   grigio                 │
│                                                             │
│  [Panel cliccabile sotto ogni badge]                        │
│  Click su ciascun asse mostra:                              │
│  - ruolo_verso_a4 (per A1, A2)                              │
│  - ruolo_verso_a5 (per A3)                                  │
│  - ruolo_nella_catena (per A4, A5)                          │
│  - messaggio "M6" per A6 grigio                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [Nota didattica]                                           │
│  La gerarchia è strutturale, non valutativa.                │
│  A5 non è "più importante" di A1: dipende da A1.            │
│  Ogni asse è condizione del successivo.                     │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:** Usa `PipelineAnimator` o un layout flex custom. I 6 badge sono cliccabili: click su un badge attiva un panel testuale sotto la pipeline con il testo corrispondente dal campo `CATENA_STRUTTURALE_M5`. A6 è visivamente diverso (grigio, cursore normale, click mostra un messaggio: "A6 — Storicità e temporalità: sarà analizzato nel modulo 6").

**Differenza da M2 slide 2.2:** In M2 la pipeline mostra la struttura logica degli assi in astratto. In M5 la pipeline mostra le dipendenze specifiche di A4 e A5: il testo in ogni panel spiega come quell'asse fonda il successivo nell'esperienza concreta dell'albo illustrato.

---

### Slide 5.6 — "Errori tipici: quando la struttura scompare"

**Tipo:** `comparison`
**Accent:** `#c0392b`
**Dati:** `ERRORI_TIPICI_A4_A5`
**Componente:** `ExpandableCards` — griglia 2×2

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Quattro modi di perdere A4 e A5                   │
├───────────────────────┬─────────────────────────────────────┤
│  A4 — ASSE 4          │  A5 — ASSE 5                        │
│  [e1] Il limite →     │  [e3] Il desiderio →                │
│  frustrazione emotiva │  capriccio o abitudine              │
│  [bordo rosso scuro]  │  [bordo viola scuro]                │
│                       │                                     │
│  [e2] Il limite →     │  [e4] Il desiderio →                │
│  regola da insegnare  │  preferenza per stimoli             │
│  [bordo rosso chiaro] │  [bordo viola chiaro]               │
└───────────────────────┴─────────────────────────────────────┘
```

**Comportamento:** Ogni card mostra `etichetta` nello stato chiuso. Al click espande e mostra:
1. `descrizione` (paragrafo)
2. Box arancione/rosato: `esempio_errato` con etichetta "❌ Come si sente di solito"
3. Box verde: `lettura_strutturale` con etichetta "✓ Lettura strutturale"
4. Box grigio: `cosa_si_perde` con etichetta "Cosa rimane invisibile"

**Stato iniziale:** Tutte le card chiuse. L'utente esplora in autonomia.

**Colore bordo sinistro card:** Usa `colore` dal dato (`#c0392b` per A4, `#8e44ad` per A5). I colori chiari/scuri per e1/e2 e e3/e4 sono solo una guida visiva per differenziare le due card per asse — non indicano gerarchia.

---

### Slide 5.7 — "Il bambino che vuole ancora: la scena annotata"

**Tipo:** `narrative`
**Accent:** `#c0392b`
**Dati:** `SCENE_HTML_M5`, `ANNOTAZIONI_M5`, `GUARDRAIL_M5`
**Componente:** `AnnotatedScene` — bicolore (A4=#c0392b, A5=#8e44ad)

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Legenda — obbligatoria, sopra la scena]                   │
│  [■ A4 — Limite reale, #c0392b]  [■ A5 — Desiderio, #8e44ad]│
│  [■ A1 — Incarnato, #1a6b8a] (secondario)                   │
├─────────────────────────────────────────────────────────────┤
│  [AnnotatedScene bicolore]                                  │
│  L'educatrice arriva all'ultima pagina...                   │
│  [span cliccabili evidenziati con colori legenda]           │
│  [Tooltip/sidenote al click con annotazione]                │
├─────────────────────────────────────────────────────────────┤
│  [Box sintesi — 2 colonne]                                  │
│  A4 nel campo:            │  A5 nel campo:                  │
│  · Libro che si chiude    │  · Mano tesa verso il libro     │
│  · Limite che permane     │  · Vocalizzazione ascendente    │
│  · Non negoziabile        │  · Peso del corpo in avanti     │
├─────────────────────────────────────────────────────────────┤
│  [GuardrailBadge — variante expanded]                       │
│  G-M5: "A4 e A5 descrivono strutture del campo,            │
│  non stati interni del bambino..."                          │
│  [Violazione] → [Compliance]                                │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione AnnotatedScene:**
```javascript
AnnotatedScene(SCENE_HTML_M5, ANNOTAZIONI_M5, container);
```
- Ogni `<span class="annotabile" data-annotation-id="m5-aX-Y">` viene evidenziato con il colore dell'asse corrispondente (campo `colore` in `ANNOTAZIONI_M5`)
- La legenda sopra la scena è obbligatoria: 3 colori (A4 rosso, A5 viola, A1 teal) con etichette
- Al click su uno span, il tooltip/panel laterale mostra `label`, `annotazione` e il badge dell'asse
- A differenza di M4 (che aveva anche annotazioni "miste" A2+A3), qui ogni annotazione appartiene a un solo asse — tranne `m5-a5-2` che mostra A5+A3: il tooltip in questo caso mostra due badge

**Box sintesi:** Non è generato da una costante dedicata — viene costruito inline nel template della slide leggendo le prime `forme_nel_libro` di A4 e A5 (o, più semplicemente, come HTML statico). Deve essere leggibile come tabella a due colonne senza interattività.

**GuardrailBadge:** Usa `GUARDRAIL_M5` con `variant: "expanded"` (stesso formato di M1 slide 1.7 e M4 slide 4.7). Mostra `testo`, poi `violazione` (icona ✗, sfondo rosato) e `compliance` (icona ✓, sfondo verde chiaro).

---

## Note tecniche trasversali

### Parallelismo visivo M5 ↔ M4
Le slide 5.2 e 5.3 sono strutturalmente identiche tra loro (e analoghe alle slide 4.2/4.3 di M4). Questo parallelismo è intenzionale: il corso costruisce un'abitudine visiva che permette al professionista di riconoscere il pattern "asse = verbo chiave + definizione + non è/è + forme nell'albo". Claude Code può usare un helper comune per rendere questi layout.

### Colori e contrasto
A4 (`#c0392b`) e A5 (`#8e44ad`) devono essere chiaramente distinguibili sia tra loro che da A1 (`#1a6b8a`), A2 (`#2d6a4f`), A3 (`#27ae60`). Verificare il contrasto in tutti i browser target. Evitare di affiancare A3 (`#27ae60`) e A5 (`#8e44ad`) senza separatori: il verde e il viola reggono il contrasto, ma una leggera distanza visiva aiuta.

### AnnotatedScene in M5 vs M4
In M4 l'AnnotatedScene aveva colori "misti" su alcune annotazioni (simultaneità A2+A3). In M5 la scena è più pulita: quasi tutte le annotazioni appartengono a un asse preciso. Solo `m5-a5-2` ha doppio badge (A5+A3). La legenda deve quindi mostrare A4, A5 e A1 — non A2 e A3 (presenti nella scena come background strutturale, ma non come fuoco del modulo).

### Connessione con M4
Il bambino che chiede la rilettura dell'albo è esattamente il bambino che abbiamo visto nell'alternanza dei turni (M4). Il professionista che ha completato M4 riconosce: l'A2 (rivolgersi all'adulto), l'A3 (la vocalizzazione come forma condivisa). M5 illumina la stessa scena attraverso A4 e A5. Nella slide 5.7, se la UI lo permette, un chip di collegamento può ricordare: "A2 e A3 attivi in questa scena — analizzati in M4".

### `window.SEI_ASSI`
`CATENA_STRUTTURALE_M5` è una costante locale (non globale) che estrae e arricchisce i dati rilevanti da `window.SEI_ASSI` per la visualizzazione di M5. Claude Code non deve ridefinire gli assi: deve leggere da `window.SEI_ASSI` e aggiungere solo i campi specifici di M5 (`ruolo_verso_a4`, `ruolo_verso_a5`).

### Colore del modulo (nav/header)
L'accent di navigazione per M5 è `#c0392b` (A4). Questo non significa che A5 sia secondario: è una scelta di coerenza con la convenienza di avere un solo colore per modulo nell'interfaccia di navigazione. All'interno del modulo, A4 e A5 hanno parità visiva.
