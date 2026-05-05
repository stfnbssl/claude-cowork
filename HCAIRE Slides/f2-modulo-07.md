# Modulo 7 — L'Operatore di Lettura

**Accent color**: `#d35400`  
**Slides**: 5  
**Obiettivo**: Far comprendere cosa è l'operatore triadico di lettura — come funziona, come si applica e, soprattutto, cosa *non* fa. Il modulo connette le domande professionali (operatore 4 della pipeline) alla CE (operatore 5) e prepara il terreno per l'output-tipo (operatore 7, modulo 8).

---

## JS Data (costanti del modulo)

```javascript
// --- OPERATORE_TRIADICO ---
// Le tre domande strutturali dell'operatore triadico.
// Usato nella slide 7.2 (accordion interattivo) e nella 7.3 (applicazione al caso-guida)
const OPERATORE_TRIADICO = [
  {
    id: 'campo',
    numero: '1',
    nome: 'Campo condiviso',
    domanda: 'Qui si sta costruendo un mondo comune o solo esecuzione parallela?',
    spiegazione: 'Il campo condiviso non è semplice vicinanza fisica. È la qualità dell\'orientamento reciproco: bambino e adulto si rivolgono insieme verso qualcosa, costruendo un riferimento condiviso. Senza campo condiviso, i gesti e le parole rimangono azioni parallele senza costruire scambio.',
    segnali_presenti: [
      'Il bambino indica e guarda l\'adulto (gesto proto-dichiarativo)',
      'Adulto e bambino si orientano insieme verso la stessa immagine',
      'C\'è alternanza di sguardo tra oggetto e partner',
      'Il bambino porta un oggetto all\'adulto come condivisione'
    ],
    segnali_assenti: [
      'Il bambino usa l\'oggetto senza cercare l\'adulto',
      'L\'adulto nomina ma non attende la risposta del bambino',
      'Le azioni si svolgono in parallelo senza intrecciare sguardi'
    ],
    casoGuida: 'Il bambino e l\'adulto si orientano verso qualcosa di comune (il libro), con gesto, sguardo e parola che si intrecciano.',
    colore: '#16a085'
  },
  {
    id: 'posizione',
    numero: '2',
    nome: 'Posizione soggettiva',
    domanda: 'Il bambino prende posizione dentro l\'esperienza o reagisce soltanto alle proposte dell\'adulto?',
    spiegazione: 'La posizione soggettiva non è autonomia totale né ribellione all\'adulto. È la presenza di un\'iniziativa che parte dal bambino — una scelta, una preferenza, un gesto che apre la sequenza piuttosto che risponderle. Anche un rifiuto può essere un indicatore di posizione.',
    segnali_presenti: [
      'Sceglie una pagina o torna su una figura',
      'Vocalizza davanti a un\'immagine prima che l\'adulto nomini',
      'Porta il libro all\'adulto (iniziativa di condivisione)',
      'Respinge una proposta dell\'adulto e ne introduce un\'altra'
    ],
    segnali_assenti: [
      'Il bambino segue passivamente la proposta adulta senza iniziativa',
      'Ogni azione è una risposta/adattamento senza apertura autonoma',
      'Il bambino imita ma non trasforma ciò che imita'
    ],
    casoGuida: 'Il bambino indica, mostra, vocalizza: c\'è iniziativa soggettiva e non solo reazione all\'adulto.',
    colore: '#8e44ad'
  },
  {
    id: 'limite',
    numero: '3',
    nome: 'Rapporto con il limite',
    domanda: 'Le interruzioni, le attese e i passaggi distruggono il campo o possono essere integrati?',
    spiegazione: 'Il limite è inevitabile nell\'interazione: un adulto che gira pagina, una pausa, una proposta diversa. Non si valuta se il bambino "tollera bene" il limite nel senso comportamentale. Si osserva se il limite può essere integrato nel campo condiviso o lo destabilizza fino a interrompere lo scambio.',
    segnali_presenti: [
      'Il bambino accetta una pausa e poi riprende l\'interazione',
      'Tollera che l\'adulto nomini qualcosa di diverso da ciò che guarda',
      'Usa il genitore per recuperare lo scambio dopo un\'interruzione',
      'Il cambio di pagina non distrugge il campo — viene negoziato'
    ],
    segnali_assenti: [
      'Il bambino chiude il libro e si allontana senza recupero',
      'Ogni proposta dell\'adulto produce protesta o ritiro',
      'Il limite produce iperattivazione o collasso dell\'attenzione'
    ],
    casoGuida: 'Il bambino accetta di condividere il controllo del libro con l\'adulto; la sequenza si interrompe e riprende.',
    colore: '#d35400'
  }
];

// --- PROPRIETA_VALIDO ---
// Le 5 proprietà di un operatore di lettura valido.
// Usato nella slide 7.4
const PROPRIETA_VALIDO = [
  {
    id: 'non-riduttivo',
    nome: 'Non riduttivo',
    descrizione: 'L\'operatore non semplifica il comportamento osservato in un\'unica causa. Non riduce a biologia, a comportamento, a cognitivo isolato. Mantiene la complessità strutturale dell\'esperienza.',
    esempio: 'Non: "il bambino non presta attenzione" → Sì: "il campo condiviso si stabilizza solo in alcune sequenze e dipende dalla qualità del sostegno adulto"',
    colore: '#16a085'
  },
  {
    id: 'non-moralizzante',
    nome: 'Non moralizzante',
    descrizione: 'L\'operatore non giudica la famiglia né l\'adulto di riferimento. Non produce valutazioni su "quanto bene" l\'adulto si è comportato. Legge il campo relazionale come sistema, non come prestazione.',
    esempio: 'Non: "il genitore non è abbastanza responsivo" → Sì: "il campo condiviso richiede un rallentamento adulto per stabilizzarsi"',
    colore: '#e67e22'
  },
  {
    id: 'non-patologizzante',
    nome: 'Non patologizzante',
    descrizione: 'L\'operatore descrive configurazioni funzionali, non sintomi. Non etichetta il bambino con categorie diagnostiche. Una posizione soggettiva assente è un dato osservativo, non una diagnosi.',
    esempio: 'Non: "assenza di attenzione condivisa — segnale di rischio DSA" → Sì: "la posizione soggettiva non è emersa in questa sequenza specifica"',
    colore: '#e74c3c'
  },
  {
    id: 'sistemico',
    nome: 'Sistemico',
    descrizione: 'L\'operatore include sempre adulto e contesto nel campo di lettura. Non isola il comportamento del bambino. Il campo condiviso, la posizione e il limite si leggono sempre nella triade bambino–adulto–situazione.',
    esempio: 'Non: "il bambino non interagisce" → Sì: "in questa situazione, con questo adulto, la costruzione del campo condiviso è fragile"',
    colore: '#2980b9'
  },
  {
    id: 'trasversale',
    nome: 'Trasversale',
    descrizione: 'Lo stesso operatore funziona in contesti diversi — ambulatorio pediatrico, nido, casa, consultorio. Non è progettato per un solo setting. Questo è il criterio che distingue un operatore da una checklist specifica.',
    esempio: 'La domanda "si sta costruendo un campo condiviso?" vale in un bilancio pediatrico come in una osservazione educativa come in un colloquio familiare.',
    colore: '#8e44ad'
  }
];

// --- LETTURA_SINTETICA ---
// Lettura sintetica finale del caso-guida tramite operatore triadico
// Usato nella slide 7.3
const LETTURA_SINTETICA = {
  testo: 'Campo condiviso presente ma fragile: il bambino cerca l\'adulto attraverso gesto e sguardo, prende iniziativa su alcune figure, ma la continuità dello scambio dipende molto dalla capacità dell\'adulto di attendere e seguire il ritmo del bambino.',
  guardrail: {
    codice: 'C4',
    etichetta: 'Separazione',
    testo: 'Questa lettura non dice ancora che cosa fare. Non prescrive un intervento. Organizza la leggibilità.'
  }
};

// --- PIPELINE_POSIZIONE ---
// Posizione dell'operatore di lettura nella pipeline (passo 5 di 7)
// Usato nella slide 7.5 per mostrare il contesto della pipeline
const PIPELINE_POSIZIONE = {
  passoCorrente: 5,
  label: 'Operatore di lettura',
  precedente: { passo: 4, label: 'Domande professionali', modulo: 'M3/M4' },
  successivo: { passo: 6, label: 'Famiglie di output', nota: '(cenno)' },
  uscita: { label: 'CE — Configurazione Evolutiva', modulo: 'M6' }
};
```

---

## Slide 7.1 — Che cos'è un operatore di lettura
**Tipo**: `standard`  
**Titolo**: "L'Operatore di Lettura"  
**Sottotitolo**: "Una forma mentale, non uno strumento"

### Contenuto

Paragrafo di apertura:

> Il professionista che ha attraversato F2 dispone di nodi, domande e configurazioni. Ma come li usa davanti a una situazione reale? Come organizza ciò che vede senza già valutarlo, classificarlo o prescrivere?  
> L'operatore di lettura è la risposta a questa domanda.

Card definitoria centrata (bordo sinistro accent `#d35400`):

> L'operatore di lettura è la struttura mentale attraverso cui il professionista organizza ciò che vede.  
> **Non è una griglia. Non è un modulo. Non è una checklist.**  
> È la forma applicativa del Nodo — senza diventare strumento.

Sotto la card, un `ComparisonPanel` compatto a due colonne:

| **Un operatore di lettura è** | **Un operatore di lettura non è** |
|---|---|
| Una forma mentale strutturata | Una scheda da compilare |
| Un modo di organizzare l'osservazione | Un criterio di valutazione |
| Applicabile prima di costruire strumenti | Uno strumento già pronto |
| Reversibile e situato nel campo | Una classificazione del bambino |

Nota a fondo slide (piccola, corsiva):

> Un operatore di lettura produce leggibilità. Non produce azione. L'azione è compito di F3.

### Note implementative
- Card definitoria: `font-size: 1.1rem; border-left: 5px solid #d35400; padding: 1rem 1.5rem; background: var(--surface-2)`
- La riga "Non è una griglia..." in grassetto, dimensione leggermente più grande
- ComparisonPanel: header "è" (verde `#27ae60`) / "non è" (grigio medio `#7f8c8d`) — meno drammatico del confronto in modulo 6 perché non è una regola critica ma una distinzione pratica

---

## Slide 7.2 — L'Operatore Triadico
**Tipo**: `interactive`  
**Titolo**: "Tre domande strutturali"  
**Sottotitolo**: "Campo · Posizione · Limite"

### Layout
Tre grandi cards cliccabili in riga orizzontale (una per dimensione). Su mobile: colonna singola. Ogni card ha numero e nome visibili sempre; al click espande il contenuto.

Le tre cards devono essere **aperibili individualmente** (`multiOpen: false` — una sola aperta per volta per guidare l'attenzione).

**Header fisso** sopra le tre cards (testo piccolo, centrato):
> Ogni situazione = Campo + Posizione + Limite

---

### Card 1 — Campo condiviso
**Colore**: `#16a085`

Header sempre visibile:
- Numero grande: **1**
- Nome: **Campo condiviso**
- Domanda (in corsivo): *"Qui si sta costruendo un mondo comune o solo esecuzione parallela?"*

Corpo espanso (al click):
1. **Spiegazione** (paragrafo — vedi `OPERATORE_TRIADICO[0].spiegazione`)
2. Due colonne affiancate: "Segnali di campo presente" (lista verde, check icon) + "Segnali di campo assente" (lista grigia, x icon)
3. Box caso-guida (fondo `#e8f8f5`, label "Nel caso-guida:"): testo da `OPERATORE_TRIADICO[0].casoGuida`

---

### Card 2 — Posizione soggettiva
**Colore**: `#8e44ad`

Header sempre visibile:
- Numero grande: **2**
- Nome: **Posizione soggettiva**
- Domanda (in corsivo): *"Il bambino prende posizione dentro l'esperienza o reagisce soltanto alle proposte dell'adulto?"*

Corpo espanso:
1. Spiegazione (da `OPERATORE_TRIADICO[1].spiegazione`)
2. Due colonne: "Segnali di posizione presente" (lista viola) + "Segnali di posizione assente" (lista grigia)
3. Box caso-guida

---

### Card 3 — Rapporto con il limite
**Colore**: `#d35400`

Header sempre visibile:
- Numero grande: **3**
- Nome: **Rapporto con il limite**
- Domanda (in corsivo): *"Le interruzioni, le attese e i passaggi distruggono il campo o possono essere integrati?"*

Corpo espanso:
1. Spiegazione (da `OPERATORE_TRIADICO[2].spiegazione`)
2. Due colonne: "Limite integrabile" (lista arancio) + "Limite destabilizzante" (lista grigia)
3. Box caso-guida

---

### Dati
Usa `OPERATORE_TRIADICO` — array di 3 oggetti definito sopra.

### Note implementative
- Numero grande nel corner top-left della card: `font-size: 3rem; font-weight: 800; opacity: 0.12` come watermark + versione leggibile sopra `1rem`
- Cards default: altezza fissa ~120px (header visibile), border-radius 12px, colore top-border 3px solid
- Card espansa: altezza `auto` con transizione; le altre due collassano (se `multiOpen: false`)
- Box caso-guida: bordo sinistra 3px solid, fondo molto leggero, label "Nel caso-guida" in uppercase xs
- I check/x icon possono essere emoji (✓/✗) o SVG inline

---

## Slide 7.3 — Applicazione al caso-guida
**Tipo**: `diagram`  
**Titolo**: "Lettura della scena"  
**Sottotitolo**: "L'operatore triadico applicato alla lettura condivisa"

### Layout
**Tre colonne affiancate** (stesso peso, 33% ciascuna), con un **box di sintesi** a larghezza piena sotto.

Ogni colonna ha:
- **Header colorato** con numero e nome della dimensione (stessi colori di slide 7.2)
- **Testo osservazione** (da `OPERATORE_TRIADICO[i].casoGuida`)
- **Label osservativo** (una frase molto breve che cristallizza la lettura)

---

**Colonna 1 — Campo condiviso** (header `#16a085`):
> Il bambino e l'adulto si orientano verso qualcosa di comune (il libro), con gesto, sguardo e parola che si intrecciano.

Label: `Campo condiviso: PRESENTE`

---

**Colonna 2 — Posizione soggettiva** (header `#8e44ad`):
> Il bambino indica, mostra, vocalizza: c'è iniziativa soggettiva e non solo reazione all'adulto.

Label: `Posizione soggettiva: EMERGENTE`

---

**Colonna 3 — Rapporto con il limite** (header `#d35400`):
> Il bambino accetta di condividere il controllo del libro con l'adulto; la sequenza si interrompe e riprende.

Label: `Limite: INTEGRABILE`

---

**Box sintesi** (larghezza piena, bordo `#d35400`, fondo `#fef0e7`, `margin-top: 1.5rem`):

> *"Campo condiviso presente ma fragile: il bambino cerca l'adulto attraverso gesto e sguardo, prende iniziativa su alcune figure, ma la continuità dello scambio dipende molto dalla capacità dell'adulto di attendere e seguire il ritmo del bambino."*

Sotto il box di sintesi, il **GuardrailBadge C4**:
`GuardrailBadge('C4', 'Separazione', 'Questa lettura non dice ancora che cosa fare. Non prescrive un intervento. Organizza la leggibilità.')`

### Dati
Usa `OPERATORE_TRIADICO` e `LETTURA_SINTETICA` definiti sopra.  
Oppure legge `window.CASO_GUIDA.pipeline.operatoreTryadico` per i testi delle tre colonne.

### Note implementative
- Labels: `display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; background: [colore]; color: white; margin-top: 0.5rem`
- Box sintesi: `font-style: italic; font-size: 1rem; line-height: 1.65`
- GuardrailBadge appare in fondo alla colonna del contenuto principale (non nel footer della slide)
- Su mobile: le 3 colonne diventano stack verticale; il box sintesi rimane in fondo

---

## Slide 7.4 — Le proprietà dell'operatore valido
**Tipo**: `standard`  
**Titolo**: "Cinque criteri di validità"  
**Sottotitolo**: "Come riconoscere un operatore che funziona"

### Layout
5 cards espandibili in colonna singola (`multiOpen: true` — tutte apribili insieme). Ogni card ha:
- **Nome** della proprietà (colore specifico per ogni proprietà — vedi `PROPRIETA_VALIDO`)
- Al click → espande: descrizione + esempio di riformulazione (Non/Sì)

### Rendering dell'esempio
L'esempio in ogni card usa una formattazione a due righe:
```
✗  "il bambino non presta attenzione"          [grigio, barrato o prefisso ✗]
✓  "il campo condiviso si stabilizza solo..."   [colore accent, grassetto leggero]
```

### Dati
Usa `PROPRIETA_VALIDO` — array di 5 oggetti definito sopra.

### Note implementative
- Cards in colonna: `border-left: 4px solid [colore proprietà]`
- Altezza header: ~60px; espanso: auto
- Esempio: due `<p>` con classi `.esempio-non` (testo barrato/grigio) e `.esempio-si` (testo accent/colore proprietà)
- Nessun guardrail in questa slide — il guardrail C4 è già comparso in slide 7.3

---

## Slide 7.5 — Dall'operatore alla CE
**Tipo**: `diagram`  
**Titolo**: "Da osservazione a configurazione"  
**Sottotitolo**: "Come l'operatore triadico produce la CE"

### Contenuto
Questa slide è un **bridge diagrammatico** che mostra il percorso dall'osservazione (in basso alla pipeline) alla CE (output del passo 5), e accenna al passo successivo (famiglie di output, passo 6).

### Struttura del diagramma
Un flusso verticale (o leggermente inclinato) in tre blocchi connessi da frecce:

```
┌─────────────────────────────────────────┐
│  DOMANDE PROFESSIONALI  (passo 4)        │
│  "Il bambino usa l'oggetto come          │
│   occasione di scambio con l'adulto?"    │
└──────────────────┬──────────────────────┘
                   │
                   ▼  applica l'operatore triadico
┌─────────────────────────────────────────┐
│  OPERATORE TRIADICO  (passo 5) ◀ QUI    │  ← evidenziato in #d35400
│  Campo condiviso · Posizione · Limite    │
│  → Lettura sintetica del campo           │
└──────────────────┬──────────────────────┘
                   │
                   ▼  produce
┌─────────────────────────────────────────┐
│  CONFIGURAZIONE EVOLUTIVA  (M6)          │
│  S: N1~ N2↑ N3~ N4↓... | D: ↗ | A: A±  │
└──────────────────┬──────────────────────┘
                   │
                   ▼  apre a
┌─────────────────────────────────────────┐
│  FAMIGLIE DI OUTPUT  (passo 6 — M8)      │  ← tono più tenue (prossimo modulo)
│  Osservativa · Formativa · Restitutiva…  │
└─────────────────────────────────────────┘
```

Il blocco "OPERATORE TRIADICO" ha uno sfondo `#fef0e7` con bordo `#d35400` (accent del modulo) e un'icona scudo o ◆ per segnalare il focus corrente.

### Testo di accompagnamento
A destra del diagramma (su desktop, 40% larghezza) oppure sotto (mobile), un box narrativo:

> L'operatore triadico **non sostituisce** la CE: la **produce**. Le tre domande strutturali (campo, posizione, limite) organizzano l'osservazione in una forma che può poi essere grammaticalizzata — tradotta nella notazione CE del modulo 6.  
>
> Non è un passaggio automatico: richiede la presenza del professionista nel campo. Ma è un passaggio **strutturato** — non soggettivo, non impressionistico.

Sotto il box narrativo, chip conclusivo (sfondo `#fef0e7`, bordo `#d35400`):
> Il passo 6 — famiglie di output — parte da qui. F3 costruisce gli strumenti. F2 produce la forma.

### Dati
Usa `PIPELINE_POSIZIONE` per colorare/evidenziare il passo corretto nel diagramma.  
Opzionalmente legge da `window.CASO_GUIDA.pipeline` per popolare i testi nei blocchi del diagramma.

### Note implementative
- Il diagramma è SVG inline o HTML puro (no D3 necessario — è un flusso statico)
- Il blocco corrente (`passo 5`) ha `box-shadow: 0 0 0 3px #d35400` e `background: #fef0e7`
- I blocchi precedenti (passo 4) e successivi (passo 6, CE) hanno stile "tenue": `opacity: 0.75`, bordo `var(--border)`
- Frecce: `▼` Unicode o `<svg>` con `<line>` + `<polygon>` arrowhead, colore `var(--text-secondary)`
- Su mobile: il box narrativo va sotto il diagramma; il diagramma si comprime in larghezza

---

## Note generali del modulo

### Posizione nella sequenza
Il modulo 7 è il più breve del corso (5 slide). Questa brevità è intenzionale: l'operatore triadico è concettualmente semplice — tre domande. La difficoltà non sta nel capirlo ma nell'applicarlo senza scivolare in valutazione, diagnosi o prescrizione. Le slide 7.3 e 7.4 servono esattamente a questo.

### Connessione con moduli precedenti
- `window.CASO_GUIDA.pipeline.operatoreTryadico` (campo/posizione/limite) è già definito nell'oggetto globale
- Il GuardrailBadge C4 che appare in slide 7.3 è lo stesso componente usato in modulo 2 (pipeline)
- Le etichette colore dei tre bracci (campo/posizione/limite) non corrispondono ai colori dei nodi N1–N7 — sono colori specifici di questo operatore; evitare confusione

### Connessione con modulo 8
Il modulo 8 (output-tipo vuoto) parte esattamente da dove finisce il 7: l'operatore triadico ha organizzato la leggibilità → ora si costruisce il template riutilizzabile. La slide 7.5 anticipa visualmente questa connessione senza anticipare il contenuto.

### Guardrail C4
Il C4 compare **una volta sola** (slide 7.3, box sintesi) — non ripetuto in ogni slide. Il suo messaggio è netto e non va diluito: l'operatore produce leggibilità, non azione. Punto.

### Design
- Accent `#d35400` (arancio bruciato) è lo stesso del modulo 7 nella palette del corso
- Le cards di slide 7.2 usano tre colori diversi (verde/viola/arancio) per differenziare le tre dimensioni; l'arancio bruciato della terza card (`#d35400`) si allinea all'accent del modulo
- Slide 7.5 è volutamente più "fredda" graficamente — è una slide di orientamento, non di contenuto nuovo
