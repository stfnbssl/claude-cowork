# F1 — Modulo 6: Asse 6 e la gerarchia strutturale completa

## Metadati

| Campo | Valore |
|-------|--------|
| ID modulo | M6 |
| Titolo breve | Asse 6 e la gerarchia completa |
| Titolo operativo | La storia che il campo porta con sé |
| Colore accent A6 | `#d35400` |
| Colore accent modulo (header/nav) | `#d35400` |
| Tipo di modulo | Asse strutturale + sintesi architettonica |
| Slide count | 7 |
| File JS | `F1/f1_m06.js` |
| Dipendenze globali | `window.SEI_ASSI`, `window.CASO_GUIDA_F1` |

---

## Nota metodologica

M6 è il modulo a doppia funzione: introduce A6 (Storicità e temporalità) e, per la prima volta nel corso, mostra tutti e sei gli assi come architettura completa. È il momento in cui la "mappa del campo" diventa visibile nella sua interezza — finora ogni modulo aveva illuminato uno o due assi; M6 li mostra tutti insieme, colorati e attivi.

**A6 — Storicità e temporalità** non è il sesto asse in ordine di importanza: è il sesto perché dipende strutturalmente da tutti i precedenti. Non aggiunge biografia al bambino, non introduce la storia clinica, non introduce i milestone evolutivi. Aggiunge questa lettura strutturale: il campo che osserviamo non è mai un inizio — ha già una storia, e quella storia è strutturalmente presente nel momento osservato.

**Il titolo operativo** "La storia che il campo porta con sé" cattura questo: non "la storia del bambino" (formula biografica), ma "la storia che il campo porta" (formula strutturale). La vocalizzazione anticipatoria del bambino che sa già quale immagine viene dopo non è un fatto di memoria — è il campo che mostra la propria storicità.

**Struttura pedagogica:**
- Slide 6.1: entrata dalla domanda temporale — "quando è cominciato?"
- Slide 6.2: A6 in dettaglio (definizione, non è/è, forme nell'albo)
- Slide 6.3: la gerarchia strutturale completa — momento culminante del corso
- Slide 6.4: gerarchia strutturale ≠ gerarchia di valore (chiarimento critico)
- Slide 6.5: errori tipici di A6 (4 cards)
- Slide 6.6: AnnotatedScene attraverso A6 — la lettura condivisa vista nella sua storicità
- Slide 6.7: tutti e sei i badge attivi + GuardrailBadge + annuncio di M7

**Nota sulla co-presenza:** La gerarchia è strutturale, non osservativa. Nel campo, tutti e sei gli assi sono sempre co-presenti. La sequenza A1→A6 descrive le condizioni di possibilità, non l'ordine in cui si osservano. M6 deve rendere questo esplicito, soprattutto nella slide 6.3.

---

## Costanti JavaScript (`F1/f1_m06.js`)

```javascript
// ─────────────────────────────────────────────
// M6 — Asse 6: Storicità e temporalità
//       + Gerarchia strutturale completa
// ─────────────────────────────────────────────

const ASSE_6_DETTAGLIO = {
  id: "a6",
  nome: "Storicità e temporalità",
  colore: "#d35400",
  verbo_chiave: "situarsi",
  // "Situarsi" si oppone a: cominciare da zero, istantanizzarsi, azzerare, ripetere
  contrari: ["cominciare da zero", "istantanizzarsi", "azzerare", "presentificare"],
  definizione: "La storicità è la struttura temporale del campo: il momento osservato non è mai un inizio, ma porta con sé una storia e si orienta verso un futuro possibile. Non è la biografia del bambino né la sequenza dei milestone, ma il fatto strutturale che ogni campo ha passato e futuro incorporati nel presente.",
  non_e: [
    "l'anamnesi o la storia clinica del bambino",
    "la sequenza degli stadi evolutivi",
    "la memoria autobiografica del bambino",
    "il peso del trauma passato",
    "la progressione cronologica delle acquisizioni"
  ],
  e: [
    "la struttura temporale del campo: presente che porta passato e futuro",
    "il fatto che ogni osservazione è sempre già una ri-osservazione",
    "la sedimentazione delle forme di campo precedenti",
    "l'orientamento del campo verso possibilità future",
    "una dimensione strutturale, non un contenuto biografico"
  ],
  dipendenza_da_tutti: "A6 è il sesto asse perché per situarsi temporalmente il campo deve già: abitare l'esperienza (A1), riconoscere l'alterità (A2), scambiare forme normativamente condivise (A3), incontrare limiti reali (A4), orientarsi con desiderio (A5). La storicità è la struttura che integra e situa tutti gli assi precedenti nel tempo.",
  tre_dimensioni: [
    {
      id: "d1",
      nome: "Passato incorporato",
      descrizione: "Il campo porta tracce delle interazioni precedenti: il bambino che anticipa la pagina sa già cosa viene dopo non per inferenza, ma perché quella sequenza è diventata struttura del campo.",
      osservabile_nel_libro: "La vocalizzazione che precede la pagina; il dito che punta prima che l'immagine sia visibile; il gesto di voltare pagina che il bambino ha già interiorizzato"
    },
    {
      id: "d2",
      nome: "Presente situato",
      descrizione: "Ogni momento è già situato: non un punto neutro ma un campo con una storia. L'albo 'consumato' porta nel presente tutte le letture precedenti, materializzate nel dorso rovinato, nelle pagine con le orecchie.",
      osservabile_nel_libro: "Il libro portato con familiarità; il modo in cui il bambino lo apre (già sa il verso); il rituale di inizio già consolidato"
    },
    {
      id: "d3",
      nome: "Futuro anticipato",
      descrizione: "Il campo si orienta verso possibilità: il bambino che sa dove va a finire la storia orienta già il presente verso la fine. La storicità non è solo retrospettiva — è anche protensione strutturale.",
      osservabile_nel_libro: "L'eccitazione crescente verso le pagine 'attese'; la resistenza più o meno intensa alla chiusura a seconda di quante pagine restano; il riconoscimento del finale"
    }
  ],
  forme_nel_libro: [
    {
      id: "fl1",
      forma: "La vocalizzazione anticipatoria",
      descrizione: "Il bambino vocalizza prima che la pagina successiva sia visibile. Non anticipa per inferenza cognitiva: la sequenza delle immagini è diventata struttura del campo attraverso le letture precedenti. È la storicità che si mostra nel gesto.",
      osservabile: "La vocalizzazione che precede il voltare pagina; il gesto di indicare un'immagine non ancora apparsa",
      asse: "a6"
    },
    {
      id: "fl2",
      forma: "Il libro portato con familiarità",
      descrizione: "Il bambino che porta all'adulto un albo già letto molte volte non trasporta solo un oggetto: porta una storia di incontri condivisi. Il modo in cui lo prende, lo tiene, lo apre — tutto mostra la sedimentazione delle esperienze precedenti.",
      osservabile: "L'orientamento corretto del libro (sa il verso); l'apertura diretta a una pagina specifica; la postura familiare nell'aprirlo",
      asse: "a6"
    },
    {
      id: "fl3",
      forma: "Il riconoscimento anticipato del finale",
      descrizione: "Nelle ultime pagine il bambino cambia tono: più eccitazione, o al contrario resistenza. Sa che sta per finire. Questo sapere non è cognitivo — è la struttura temporale del campo che orienta il presente verso un futuro già 'noto'.",
      osservabile: "Il cambio di ritmo corporeo nelle ultime pagine; la resistenza alla chiusura che cresce avvicinandosi alla fine; l'eccitazione climax per il finale atteso",
      asse: "a6"
    },
    {
      id: "fl4",
      forma: "Il rituale consolidato",
      descrizione: "La lettura condivisa non è ogni volta un inizio: ha un rituale (posto fisico, postura, tempo della giornata, frase di inizio) che porta la storia di tutte le letture precedenti. Il rituale è la forma più densa di A6: la storicità del campo istituzionalizzata in rito.",
      osservabile: "L'educatrice sa già dove si siedono; il bambino sa già cosa fare con il proprio corpo; le prime parole della lettura hanno già un tono riconosciuto",
      asse: "a6"
    }
  ],
  domande_per_contesto: {
    clinico: "Qual è la storia di questo campo? Da quanto si incontrano? Quali forme di campo si sono sedimentate? C'è storicità o ogni incontro sembra ricominciare da zero?",
    pedagogico: "Il setting educativo costruisce storicità (rituali, libri familiari, continuità delle persone)? O ogni proposta è presentata come nuova? La lettura condivisa ha storia?",
    genitoriale: "Quando ha cominciato a leggere con voi? Ci sono libri che conosce 'a memoria'? Ha un rituale di lettura? Cosa porta il momento di lettura di ciò che è stato costruito prima?"
  },
  guardrail: "A6 non richiede di raccogliere la storia biografica del bambino. Chiede di riconoscere che il campo ha sempre già una storia strutturale — osservabile nel presente senza necessità di risalire al passato."
};

// ─────────────────────────────────────────────
// GERARCHIA STRUTTURALE COMPLETA
// Tutti e sei gli assi in relazione
// ─────────────────────────────────────────────
const GERARCHIA_COMPLETA = {
  principio: "La gerarchia strutturale descrive condizioni di possibilità, non gradi di importanza. A1 non è meno importante di A6: A6 non sarebbe possibile senza A1. L'ordine è logico-strutturale, non valutativo.",
  co_presenza: "Nel campo osservato, tutti e sei gli assi sono sempre co-presenti. La sequenza A1→A6 non descrive l'ordine in cui si osservano, ma le condizioni strutturali che li legano. Si può osservare A5 senza aver analizzato A1 — ma la comprensione strutturale richiede l'intera catena.",
  catena: [
    {
      asse: "A1",
      nome: "Abitare l'esperienza",
      colore: "#1a6b8a",
      posizione: 1,
      fonda: "A2, indirettamente tutti",
      dipende_da: null,
      condizione_che_offre: "Il bambino è nel campo come soggetto incarnato: percepisce, sente, si orienta corporalmente. Senza questa fondazione, nessun altro asse ha materiale su cui operare.",
      domanda_strutturale: "Il bambino abita questa esperienza o ne è ai margini?"
    },
    {
      asse: "A2",
      nome: "Alterità",
      colore: "#2d6a4f",
      posizione: 2,
      fonda: "A3",
      dipende_da: "A1",
      condizione_che_offre: "Il campo si struttura come relazione: c'è un altro riconosciuto come tale. L'alterità non aggiunta dall'esterno ma emergente dall'incontro. Senza A2, non c'è campo relazionale in cui A3 possa emergere.",
      domanda_strutturale: "L'altro è riconosciuto come alterità o come prolungamento del sé?"
    },
    {
      asse: "A3",
      nome: "Normatività emergente",
      colore: "#27ae60",
      posizione: 3,
      fonda: "A4, A5",
      dipende_da: "A1, A2",
      condizione_che_offre: "Il campo produce forme condivise di scambio: gesti, vocalizzazioni, strutture di alternanza che entrambi i partecipanti riconoscono. Senza A3, il campo non ha forma — è incontro ma non comunicazione.",
      domanda_strutturale: "Lo scambio ha forme normativamente riconoscibili o è caotico/unidirezionale?"
    },
    {
      asse: "A4",
      nome: "Limite reale",
      colore: "#c0392b",
      posizione: 4,
      fonda: "A5",
      dipende_da: "A1, A2",
      condizione_che_offre: "Il campo incontra discontinuità strutturali: ciò che è e non cambia. Il limite non è imposto dall'adulto ma emerge dalla struttura del reale. Senza A4, non c'è polo verso cui il desiderio possa orientarsi.",
      domanda_strutturale: "Il campo contiene limiti reali? Come vengono incontrati?"
    },
    {
      asse: "A5",
      nome: "Desiderio come orientamento",
      colore: "#8e44ad",
      posizione: 5,
      fonda: "A6",
      dipende_da: "A4, A3",
      condizione_che_offre: "Il campo mostra un orientamento strutturale verso poli significativi. Il desiderio non è mancanza interna ma tensione osservabile: il campo si dirige. Senza A5, A6 non avrebbe dove collocare la storicità — storia di cosa?",
      domanda_strutturale: "Il campo mostra orientamento verso poli stabili? Il desiderio ha forma riconoscibile?"
    },
    {
      asse: "A6",
      nome: "Storicità e temporalità",
      colore: "#d35400",
      posizione: 6,
      fonda: null,
      dipende_da: "A1, A2, A3, A4, A5",
      condizione_che_offre: "Il campo è temporalmente situato: porta una storia e si orienta verso un futuro. L'osservazione non è mai un primo incontro — è sempre già inserita in una sequenza. A6 integra e situa tutti gli assi precedenti nel tempo.",
      domanda_strutturale: "Qual è la storia di questo campo? Cosa porta con sé il momento osservato?"
    }
  ],
  lettura_corretta: "Osservando il bambino che porta il libro familiare all'educatrice, tutti e sei gli assi sono simultaneamente attivi: il corpo che porta (A1), la direzione verso l'adulto (A2), il gesto del porgere come forma condivisa (A3), il libro come limite reale (A4), il portarlo come desiderio orientato (A5), il farlo con la familiarità di chi lo ha già fatto molte volte (A6).",
  lettura_errata: "Prima osservo A1, poi A2, poi A3... La sequenza è logica, non osservativa. Nel campo tutto avviene insieme."
};

// ─────────────────────────────────────────────
// GERARCHIA ≠ SCALA DI VALORE
// Chiarimento critico — dati per slide 6.4
// ─────────────────────────────────────────────
const GERARCHIA_NON_VALUTATIVA = {
  principio: "La sequenza A1→A6 indica dipendenza strutturale, non importanza crescente. A1 non è 'primitivo' né 'più semplice': è la condizione fondante senza la quale nessun altro asse ha dove operare.",
  tre_equivoci: [
    {
      id: "eq1",
      equivoco: "A6 è l'asse più importante perché è l'ultimo",
      risposta: "A6 è il più complesso perché dipende da tutti gli altri. Non è il più importante: è il più integrato. Senza A1, A6 non esiste.",
      analogia: "La volta di un arco non è la pietra più importante: è quella che tiene le altre insieme, ma dipende da ciascuna di esse."
    },
    {
      id: "eq2",
      equivoco: "Un bambino che mostra molti indicatori di A6 è 'più sviluppato'",
      risposta: "Gli assi non misurano. La presenza osservabile di A6 non indica uno sviluppo superiore: indica che il campo ha una storia. Un bambino appena inserito in un contesto ha meno storia in quel campo — non meno struttura.",
      analogia: "Un libro appena aperto ha meno orecchie alle pagine di uno letto cento volte. Non è un libro migliore o peggiore."
    },
    {
      id: "eq3",
      equivoco: "La gerarchia è una sequenza di sviluppo: prima A1, poi A2...",
      risposta: "La gerarchia è strutturale, non temporale. Non si 'completa A1 prima di passare ad A2'. Tutti gli assi sono operativi dal primo incontro. La sequenza descrive dipendenze logiche, non tappe.",
      analogia: "Una fondazione non precede temporalmente i muri: li rende possibili. Ma in una casa finita, tutto coesiste."
    }
  ],
  schema_corretto: "A1 fonda A2 (non: A1 viene prima di A2 nello sviluppo). A6 integra A1-A5 (non: A6 è la fase finale di un percorso)."
};

// ─────────────────────────────────────────────
// ERRORI TIPICI DI A6
// ─────────────────────────────────────────────
const ERRORI_TIPICI_A6 = [
  {
    id: "e1",
    tipo: "riduzione biografica",
    colore: "#d35400",
    etichetta: "A6 → anamnesi e storia clinica",
    descrizione: "La storicità strutturale viene confusa con la raccolta di informazioni biografiche: 'per capire questo bambino devo sapere la sua storia'. A6 non chiede di risalire al passato biografico — chiede di riconoscere che il campo porta già con sé la sua storia, osservabile nel presente.",
    esempio_errato: "Prima di osservare come legge, ho bisogno di sapere da quando frequenta il nido, se ci sono stati cambiamenti in famiglia, che tipo di attaccamento ha...",
    lettura_strutturale: "Il campo porta già la propria storia: il modo in cui porta il libro, come lo apre, la vocalizzazione anticipatoria — sono tracce della storicità del campo, osservabili senza raccogliere informazioni pregresse.",
    cosa_si_perde: "La storicità come struttura del presente. Si cerca il passato dietro il campo invece di leggere il passato nel campo."
  },
  {
    id: "e2",
    tipo: "riduzione evolutiva",
    colore: "#d35400",
    etichetta: "A6 → milestone e tappe di sviluppo",
    descrizione: "La dimensione temporale di A6 viene letta come collocazione su una scala evolutiva: 'a 20 mesi dovrebbe già...', 'questo comportamento è tipico della fase...'. A6 non è una metrica di avanzamento evolutivo: è la struttura temporale del campo specifico che osserviamo.",
    esempio_errato: "La vocalizzazione anticipatoria è normale a questa età? È un indicatore di sviluppo linguistico nella norma?",
    lettura_strutturale: "La vocalizzazione anticipatoria mostra che il campo ha una storia: questo bambino in questo contesto con questi adulti ha costruito una storia di lettura condivisa. Non indica uno stadio evolutivo.",
    cosa_si_perde: "La specificità del campo. La domanda evolutiva è legittima ma appartiene a F2, non a F1. F1 legge la struttura del campo, non il posto del bambino su una curva."
  },
  {
    id: "e3",
    tipo: "riduzione traumatica",
    colore: "#d35400",
    etichetta: "A6 → storia come trauma o deficit",
    descrizione: "La storicità viene attivata solo quando il campo mostra difficoltà: 'ha avuto questa difficoltà perché nella sua storia c'è stato X'. A6 non è un asse eziologico: la storia del campo non spiega le difficoltà, ne mostra la struttura temporale.",
    esempio_errato: "Se questo bambino fatica a stare in un'attività di lettura, dobbiamo chiederci cosa è successo nella sua storia.",
    lettura_strutturale: "Il campo mostra una storia di incontri con la lettura condivisa che ha prodotto questa forma. La storicità non spiega — situa. Chiede: cosa porta questo campo? Non: chi è colpevole di questo deficit?",
    cosa_si_perde: "La neutralità strutturale di A6. Lo si trasforma in uno strumento di indagine causale quando è invece uno strumento di lettura strutturale."
  },
  {
    id: "e4",
    tipo: "assenza di A6",
    colore: "#7f3d00",
    etichetta: "Osservazione senza storia: il 'momento zero'",
    descrizione: "L'errore opposto: trattare ogni osservazione come se fosse un primo incontro, senza storia. 'Osservo solo quello che vedo adesso.' Questo è l'a-storicismo strutturale: negare che il campo porta sempre con sé una sedimentazione.",
    esempio_errato: "Non voglio sapere niente di questo bambino prima di osservarlo: guardo solo quello che fa adesso, senza pregiudizi.",
    lettura_strutturale: "Non c'è osservazione senza storia: anche l'osservazione del primo incontro è già storicamente situata (chi sei tu come professionista, che storia ha il setting, cosa porta il bambino dal suo contesto di origine). A6 non è pregiudizio — è struttura.",
    cosa_si_perde: "La possibilità di leggere il campo come campo: ogni campo ha già una storia che è strutturalmente presente, non aggiunta dall'osservatore."
  }
];

// ─────────────────────────────────────────────
// SCENE HTML — pre-costruita con span annotabili
// Scena: lettura di un albo familiare — il campo porta la sua storia
// Contesto: educatrice + bambino 22 mesi, libro già letto molte volte
// ─────────────────────────────────────────────
const SCENE_HTML_M6 = `
<p>Il bambino attraversa la stanza portando tra le braccia 
<span class="annotabile" data-annotation-id="m6-a6-1">l'albo con il dorso consumato</span> — 
quello con l'orso che dorme. 
<span class="annotabile" data-annotation-id="m6-a6-2">Lo porta già orientato nel verso giusto</span>, 
copertina in su, come ha imparato a fare. 
L'educatrice lo vede arrivare e 
<span class="annotabile" data-annotation-id="m6-a6-3">sposta già il cuscino per fare posto</span>: 
sa cosa viene dopo.</p>

<p>Si siedono. L'educatrice apre alla prima pagina. 
Il bambino, 
<span class="annotabile" data-annotation-id="m6-a6-4">prima ancora che l'immagine sia completamente visibile</span>, 
emette una vocalizzazione breve e ascendente — 
già sa cosa c'è: l'orso tra gli alberi. 
A metà libro, arriva la pagina con la luna. 
<span class="annotabile" data-annotation-id="m6-a6-5">Il bambino alza il dito verso l'angolo in alto a destra</span> 
prima che l'educatrice dica qualcosa: 
è sempre lì, la luna, su quella pagina.</p>

<p>Ultima pagina. L'orso dorme. 
<span class="annotabile" data-annotation-id="m6-a6-6">Il bambino abbassa la voce</span> — 
anche lui, come l'educatrice ha sempre fatto, 
come se l'orso potesse sentire. 
Il campo ha costruito questa forma insieme, 
lettura dopo lettura.</p>
`;

const ANNOTAZIONI_M6 = [
  {
    id: "m6-a6-1",
    label: "A6 — Storicità (oggetto)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Il dorso consumato è la storicità del campo resa materialmente visibile: ogni lettura ha lasciato una traccia sull'oggetto. Il bambino porta non solo il libro ma tutte le letture che quel libro incorpora.",
    note_tecniche: "Badge A6 arancione (#d35400). La materialità dell'oggetto come traccia della storia del campo."
  },
  {
    id: "m6-a6-2",
    label: "A6 — Storicità (postura)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Portarlo 'nel verso giusto' non è una competenza acquisita astrattamente: è la forma che le letture precedenti hanno sedimentato nel campo. Il bambino ha interiorizzato la struttura dell'oggetto attraverso la ripetizione situata.",
    note_tecniche: "Badge A6. Connessione con A1 (incarnato): la postura corretta è acquisizione corporale, non cognitiva."
  },
  {
    id: "m6-a6-3",
    label: "A6 — Storicità (anticipazione adulta)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "L'educatrice che anticipa il gesto mostra la storicità del campo dal lato adulto: anche lei porta la storia delle letture precedenti. A6 non è solo nel bambino — è nel campo relazionale, nei suoi due poli.",
    note_tecniche: "Badge A6 con nota: 'La storicità è del campo, non solo del bambino.' Importante per evitare la riduzione individualista."
  },
  {
    id: "m6-a6-4",
    label: "A6 — Storicità (vocalizzazione anticipatoria)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Vocalizzare prima che l'immagine sia visibile è la forma più pura di A6 osservabile nell'albo: la sequenza delle immagini è diventata struttura del campo. Non è memoria cognitiva — è il campo che porta la propria storia nel gesto.",
    note_tecniche: "Badge A6. Questo è l'osservabile più citabile per spiegare A6 a professionisti: concreto, inequivocabile, non riducibile ad altre spiegazioni."
  },
  {
    id: "m6-a6-5",
    label: "A6 — Storicità (anticipazione spaziale)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Il dito verso l'angolo dove 'sarà' la luna anticipa nello spazio un'immagine non ancora visibile. Il campo porta la struttura spaziale delle pagine passate nel momento presente: storicità incarnata (A6+A1).",
    note_tecniche: "Badge A6 con richiamo A1. Doppio badge opzionale: A6 primario, A1 secondario."
  },
  {
    id: "m6-a6-6",
    label: "A6 — Storicità (forma co-costruita)",
    colore: "#d35400",
    asse: "a6",
    annotazione: "Abbassare la voce come fa l'educatrice è la forma più intensa di storicità: il bambino ha incorporato una prassi del campo che non ha imparato esplicitamente, ma ha assorbito lettura dopo lettura. Il campo ha prodotto questa norma condivisa (A6+A3) attraverso il tempo.",
    note_tecniche: "Badge doppio A6+A3: la norma emergente (A3) è qui osservabile come sedimentazione storica (A6). Annotazione conclusiva della scena — il momento più denso."
  }
];

// ─────────────────────────────────────────────
// GUARDRAIL M6
// ─────────────────────────────────────────────
const GUARDRAIL_M6 = {
  id: "g-m6",
  modulo: "M6",
  testo: "A6 non chiede di raccogliere la storia biografica del bambino né di collocarlo in una sequenza evolutiva. Chiede di riconoscere che il campo osservato porta sempre già una storia strutturale — leggibile nel presente senza risalire al passato. La storicità è del campo, non del bambino isolato.",
  violazione: "Per capire come legge con sua madre devo sapere quando hanno cominciato, cosa leggono di solito, se c'è stato qualche cambiamento in famiglia ultimamente.",
  compliance: "Il modo in cui porta il libro, come lo apre, la vocalizzazione anticipatoria — il campo mostra già la propria storia. Posso leggere la storicità (A6) senza raccogliere informazioni pregresse.",
  versione_compatta: "A6 legge la storia nel campo presente. Non risale al passato: lo trova nel gesto."
};
```

---

## Slide — Specifiche

### Slide 6.1 — "Quando è cominciato? La domanda temporale"

**Tipo:** `standard`
**Accent:** `#d35400`
**Dati:** costruiti inline — nessuna costante dedicata

**Layout:** tre registri verticali

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] La stessa scena, una domanda diversa              │
├─────────────────────────────────────────────────────────────┤
│  [Citazione dalla scena — bordo arancione sinistro]         │
│  "Il bambino vocalizza prima ancora che l'immagine sia       │
│   visibile. Sa già cosa viene dopo."                         │
├─────────────────────────────────────────────────────────────┤
│  Due domande a confronto — layout a freccia                 │
│                                                             │
│  [Domanda comune]            [Domanda strutturale]          │
│  "Ha buona memoria?"         "Quando è cominciato           │
│  "È un bambino attento?"      questo campo?"                │
│  "Impara in fretta?"         "Cosa porta con sé             │
│                               questo momento?"              │
│  [chip: individuali,         [chip: strutturali,            │
│   competenze]                 temporalità del campo]        │
│                                                             │
│            ↓                                                │
│  [Box arancione]                                            │
│  La prima domanda guarda al bambino.                        │
│  La seconda domanda guarda al campo nel tempo.              │
│  Questa differenza ha un nome: Asse 6.                      │
└─────────────────────────────────────────────────────────────┘
```

**Comportamento:** Statico. Il box finale arancione (#d35400, sfondo tenue) introduce A6 senza ancora definirlo — lascia la tensione aperta per la slide successiva.

---

### Slide 6.2 — "Asse 6: Storicità e temporalità"

**Tipo:** `standard`
**Accent:** `#d35400`
**Dati:** `ASSE_6_DETTAGLIO`
**Badge assi visibili:** A6 (grande, in evidenza)

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Badge A6 grande: "Asse 6 — Storicità e temporalità"]      │
│  Verbo chiave: SITUARSI                                     │
│  (non: cominciare da zero / istantanizzarsi / azzerare)     │
├─────────────────────────────────────────────────────────────┤
│  [Blockquote definizione — bordo sinistro arancione]        │
│  "La storicità è la struttura temporale del campo:          │
│   il momento osservato non è mai un inizio, ma porta con    │
│   sé una storia e si orienta verso un futuro possibile."    │
├──────────────────────┬──────────────────────────────────────┤
│  NON È               │  È                                   │
│  · anamnesi clinica  │  · struttura temporale del campo    │
│  · tappe evolutive   │  · presente che porta passato        │
│  · memoria biograf.  │  · sedimentazione delle forme        │
│  · peso del trauma   │  · orientamento verso il futuro      │
├─────────────────────────────────────────────────────────────┤
│  TRE DIMENSIONI DI A6 — tabs orizzontali                   │
│  [Passato incorporato] [Presente situato] [Futuro anticipato]│
│                                                             │
│  [Tab attivo mostra: nome + descrizione + osservabile]      │
│  Default: "Passato incorporato" attivo                      │
├─────────────────────────────────────────────────────────────┤
│  QUATTRO FORME NELL'ALBO                                    │
│  [grid 2×2 — accordion come M5]                             │
│  [fl1] Vocaliz.  │ [fl2] Il libro  │                        │
│        anticipat.│       portato   │                        │
│  [fl3] Riconosc. │ [fl4] Il rituale│                        │
│        del finale│       consolidato│                       │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione tabs:** Le tre dimensioni di A6 usano `ASSE_6_DETTAGLIO.tre_dimensioni`. Tre tab cliccabili (non accordion): click su un tab sostituisce il contenuto del panel centrale. Stile minimale: tab come testo sottolineato/bordato in basso, senza box pesanti.

**Nota:** Il parallelismo con M3/M4/M5 (stessa struttura di slide per la definizione di un asse) è voluto. La differenza è che A6 ha le "tre dimensioni" al posto del semplice "verbo chiave + contrari" — A6 è più complesso perché integra tutti gli altri.

---

### Slide 6.3 — "La gerarchia strutturale completa"

**Tipo:** `diagram`
**Accent:** `#d35400`
**Dati:** `GERARCHIA_COMPLETA`

**Questa è la slide culminante del corso. Tutti e sei gli assi appaiono per la prima volta completi e colorati insieme.**

**Layout a due livelli:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Sei assi. Una struttura. Un campo.                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LIVELLO 1 — Catena delle dipendenze (orizzontale)          │
│                                                             │
│  [A1]──→[A2]──→[A3]──→[A4]──→[A5]──→[A6]                  │
│  teal   verde  verde  rosso  viola  arancio                 │
│  (tutti colorati, tutti attivi)                             │
│                                                             │
│  [Badge cliccabile per ciascun asse]                        │
│  Click → panel sotto con condizione_che_offre +             │
│           domanda_strutturale                               │
├─────────────────────────────────────────────────────────────┤
│  LIVELLO 2 — Co-presenza nel campo                          │
│                                                             │
│  [Box centrale sfumato — sfondo grigio chiarissimo]         │
│  "Nel campo osservato, tutti e sei gli assi sono            │
│   simultaneamente attivi."                                   │
│                                                             │
│  [Esempio testo]                                            │
│  Il bambino che porta il libro familiare all'educatrice:    │
│  corpo che porta (A1) · verso l'adulto (A2) ·               │
│  con gesto riconoscibile (A3) · libro come limite (A4) ·    │
│  orientamento attivo (A5) · familiarità sedimentata (A6)    │
│                                                             │
│  → I sei punti usano i colori degli assi corrispondenti    │
├─────────────────────────────────────────────────────────────┤
│  [Nota a piè di slide — testo piccolo]                      │
│  La freccia → descrive dipendenza strutturale,              │
│  non sequenza osservativa.                                   │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:**

I badge degli assi sono identici ai badge usati nelle slide precedenti (stessi colori, stessa dimensione). La catena usa frecce CSS semplici (→). Il click su un badge attiva un panel di testo unico (non accordion: un panel condiviso che si aggiorna). Il panel mostra:
- `nome` e `posizione`
- `condizione_che_offre` (il contributo strutturale dell'asse)
- `domanda_strutturale` in box evidenziato
- `dipende_da` e `fonda` come chip colorati

L'esempio di co-presenza ("Il bambino che porta il libro...") usa inline colori: ogni asse citato ha il proprio colore nel testo. Questo richiede che il testo dell'esempio sia HTML con `<span style="color: ...">` per ogni asse citato.

**Effetto visivo desiderato:** Per la prima volta nel corso, il professionista vede la palette completa dei sei colori tutti attivi insieme. È il momento di riconoscimento architettonico.

---

### Slide 6.4 — "Gerarchia strutturale ≠ gerarchia di valore"

**Tipo:** `comparison`
**Accent:** `#d35400`
**Dati:** `GERARCHIA_NON_VALUTATIVA`

**Layout:** tre blocchi verticali (uno per ogni equivoco)

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] L'ordine è strutturale, non valutativo            │
│  [Sottotitolo] Tre equivoci da sciogliere                   │
├─────────────────────────────────────────────────────────────┤
│  [Box principio — bordo arancione]                          │
│  "A1 non è meno importante di A6: A6 non sarebbe           │
│   possibile senza A1."                                       │
├─────────────────────────────────────────────────────────────┤
│  EQUIVOCO 1                    [ExpandableCard — chiusa]    │
│  "A6 è l'asse più importante" ────────────────────────→     │
│                                [Risposta + analogia]        │
│                                                             │
│  EQUIVOCO 2                    [ExpandableCard — chiusa]    │
│  "Più A6 = più sviluppato"    ────────────────────────→     │
│                                [Risposta + analogia]        │
│                                                             │
│  EQUIVOCO 3                    [ExpandableCard — chiusa]    │
│  "Prima A1, poi A2..."        ────────────────────────→     │
│                                [Risposta + analogia]        │
├─────────────────────────────────────────────────────────────┤
│  [Schema corretto — testo evidenziato]                      │
│  "A1 fonda A2" (non: "A1 viene prima di A2")               │
│  "A6 integra A1-A5" (non: "A6 è la fase finale")           │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:** Tre `ExpandableCard` verticali (non a griglia). Ogni card mostra l'equivoco nello stato chiuso. Al click espande e mostra: `risposta` (paragrafo) + `analogia` (box in corsivo, sfondo giallo pallido — le analogie sono i momenti didatticamente più forti). Stato iniziale: tutte chiuse.

**Nota didattica:** Le analogie sono cruciali in questa slide. L'analogia della volta dell'arco (eq1), del libro con orecchie (eq2), della fondazione/muri (eq3) devono essere visivamente distinte dal testo principale — box separato, corsivo, bordo sottile.

---

### Slide 6.5 — "Errori tipici: quattro modi di distorcere A6"

**Tipo:** `comparison`
**Accent:** `#d35400`
**Dati:** `ERRORI_TIPICI_A6`
**Componente:** `ExpandableCards` — griglia 2×2

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Quattro distorsioni di A6                         │
├──────────────────────────┬──────────────────────────────────┤
│  [e1] A6 → anamnesi      │  [e3] A6 → trauma               │
│  bordo arancione scuro   │  bordo arancione medio           │
│                          │                                  │
│  [e2] A6 → milestone     │  [e4] A6 assente                 │
│  bordo arancione medio   │  bordo marrone scuro (#7f3d00)   │
└──────────────────────────┴──────────────────────────────────┘
```

**Comportamento:** Identico a M5 slide 5.6. Ogni card espande con:
1. `descrizione`
2. Box rosato: `esempio_errato` — "❌ Come si sente di solito"
3. Box verde: `lettura_strutturale` — "✓ Lettura strutturale"
4. Box grigio: `cosa_si_perde` — "Cosa rimane invisibile"

**Nota su e4:** L'errore e4 (A6 assente — "osservazione senza storia") ha colore diverso dagli altri (`#7f3d00` — marrone scuro) per marcare che è un errore di tipo opposto: non una distorsione di A6 ma la sua negazione. Il bordo più scuro segnala visivamente questa differenza.

---

### Slide 6.6 — "La scena annotata: il campo porta la sua storia"

**Tipo:** `narrative`
**Accent:** `#d35400`
**Dati:** `SCENE_HTML_M6`, `ANNOTAZIONI_M6`
**Componente:** `AnnotatedScene` — monocromatico A6 (con due badge doppi A6+A1 e A6+A3)

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Legenda — sopra la scena]                                 │
│  [■ A6 — Storicità, #d35400]                               │
│  (note: A1 e A3 appaiono come assi di supporto in          │
│   due annotazioni — indicati nei tooltip, non in legenda)   │
├─────────────────────────────────────────────────────────────┤
│  [AnnotatedScene — colore dominante arancione]              │
│  "Il bambino attraversa la stanza portando tra le braccia   │
│   l'albo con il dorso consumato..."                         │
│  [6 span annotabili, tutti evidenziati in arancione]        │
├─────────────────────────────────────────────────────────────┤
│  [Box note sotto la scena]                                  │
│  "Questa scena non è la prima: è sempre già una             │
│   ri-lettura. Il campo porta la sua storia."                │
└─────────────────────────────────────────────────────────────┘
```

**Scelta cromatica:** A differenza di M4 (bicolore A2+A3) e M5 (bicolore A4+A5), M6 usa prevalentemente un solo colore per le annotazioni (arancione A6). I due badge doppi (m6-a6-2 con A1, m6-a6-6 con A3) mostrano le interconnessioni ma A6 rimane dominante. La legenda sopra la scena mostra solo A6 — con una nota testuale che spiega che A1 e A3 appaiono in due annotazioni a supporto.

**Comportamento AnnotatedScene:** Identico alle slide precedenti. Click su span → tooltip/panel con label, annotazione, badge asse/i.

---

### Slide 6.7 — "La mappa completa: sei assi, un campo"

**Tipo:** `standard`
**Accent:** `#d35400`
**Dati:** `GUARDRAIL_M6`, `window.SEI_ASSI`

**Questa è la slide di chiusura di M6 e di tutta la parte "assi strutturali" (M2-M6). Mostra tutti e sei i badge colorati + guardrail + preparazione per M7.**

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  [Titolo] Sei assi strutturali: la fondazione è completa    │
├─────────────────────────────────────────────────────────────┤
│  [Sei badge assi — tutti colorati, riga orizzontale]        │
│  [A1 teal] [A2 verde] [A3 verde] [A4 rosso] [A5 viola] [A6 arancio]│
│                                                             │
│  [Sotto ogni badge: 3 parole — il verbo chiave dell'asse]  │
│  abitare  riconoscere  scambiare  incontrare  orientarsi  situarsi│
├─────────────────────────────────────────────────────────────┤
│  [GuardrailBadge M6 — variante expanded]                    │
│  "A6 non chiede di raccogliere la storia biografica..."     │
│  [Violazione] → [Compliance]                                │
├─────────────────────────────────────────────────────────────┤
│  [Box preparatorio M7 — sfondo grigio chiaro]               │
│  Prossimo modulo — M7                                       │
│  "Abbiamo costruito la fondazione ontologica.               │
│   Cosa ne possiamo fare? Qual è il suo statuto              │
│   epistemologico? E come passa a F2?"                       │
│  → Statuto epistemologico e passaggio a F2                  │
└─────────────────────────────────────────────────────────────┘
```

**Implementazione:**

I sei badge nella riga superiore usano i colori definitivi di ciascun asse da `window.SEI_ASSI`. Non sono cliccabili in questa slide (o, se cliccabili, mostrano solo il verbo chiave in un tooltip — nessun panel esteso, si è già visto tutto nei moduli precedenti).

Sotto ogni badge, il "verbo chiave" dell'asse in testo piccolo, stesso colore del badge. Questo crea una riga di sei "etichette sintetiche" che riassumono l'intera architettura F1 in sei verbi.

Il `GuardrailBadge` usa `GUARDRAIL_M6` con `variant: "expanded"`.

Il box M7 è visivamente neutro (grigio, nessun colore di asse): M7 è il modulo epistemologico e non ha un asse strutturale proprio. La domanda "cosa ne possiamo fare?" prepara la svolta di M7.

---

## Note tecniche trasversali

### Slide 6.3 — Il momento culminante
La slide 6.3 ("La gerarchia strutturale completa") è il momento più visivamente importante di tutto il corso F1. È la prima volta che tutti e sei i colori degli assi appaiono insieme, pienamente attivi. L'implementazione deve essere curata: badge della stessa dimensione degli altri moduli, frecce leggibili, panel testuale pulito. Evitare il sovraccarico visivo — il diagramma deve respirare.

### Co-presenza vs sequenza
La distinzione "dipendenza strutturale / non sequenza osservativa" è il punto più delicato di M6. Appare nella slide 6.3 (nota a piè), nella slide 6.4 (equivoco 3) e nella slide 6.7 (implicita nei sei verbi). Claude Code deve assicurarsi che questa distinzione sia presente in almeno due punti visibili, non solo in un'unica slide.

### `window.SEI_ASSI` e `GERARCHIA_COMPLETA`
`GERARCHIA_COMPLETA.catena` ridefinisce localmente i dati degli assi per aggiungere i campi specifici di M6 (`condizione_che_offre`, `domanda_strutturale`, `fonda`, `dipende_da`). Claude Code non deve duplicare i dati base degli assi: deve estendere `window.SEI_ASSI[i]` con questi campi aggiuntivi, oppure costruire `GERARCHIA_COMPLETA.catena` come array di oggetti che wrappano i dati globali.

Esempio pattern consigliato:
```javascript
const GERARCHIA_COMPLETA = {
  // ...
  catena: window.SEI_ASSI.map((asse, i) => ({
    ...asse,
    condizione_che_offre: [/* array locale */][i],
    domanda_strutturale: [/* array locale */][i],
    dipende_da: [null, "A1", "A1,A2", "A1,A2", "A4,A3", "A1-A5"][i],
    fonda: ["A2", "A3", "A4,A5", "A5", "A6", null][i]
  }))
};
```

### AnnotatedScene monocromatica in M6
M6 torna alla monocromaticità (come M3) dopo i due moduli bicromatici (M4, M5). La legenda sopra la scena mostra un solo colore — ma due annotazioni hanno badge doppi (A6+A1, A6+A3) per mostrare le interconnessioni. Questo è corretto: i badge doppi nei tooltip non richiedono una seconda voce in legenda se A1 e A3 sono secondari.

### Slide 6.7 come cerniera
La slide 6.7 ha una funzione di cerniera: chiude M6 e apre M7. Il box preparatorio per M7 deve essere visivamente sobrio — non un teaser, ma un'indicazione di direzione. La domanda "Cosa ne possiamo fare?" deve rimanere aperta, non preannunciare risposte.

### Sei verbi chiave nella slide 6.7
I sei verbi (abitare, riconoscere, scambiare, incontrare, orientarsi, situarsi) sono la sintesi verbale dell'intera architettura F1. Devono essere visivamente in evidenza — dimensione maggiore del testo normale, ciascuno nel colore del proprio asse. Possono diventare un'immagine riassuntiva del corso, citabile fuori contesto.
