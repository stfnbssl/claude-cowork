# f3-modulo-02 — Dalla CE allo strumento
**Numero slide**: 7
**Colore accent**: `#0e8f7f`
**Tipo prevalente**: diagram + comparison

---

## Dati globali del modulo

Definire in `m02.js` le seguenti costanti. La sorgente di dati principale è `PIPELINE_F3`, che alimenta sia la slide della pipeline astratta (F3.2.2) sia quella del caso-guida (F3.2.6): stessa struttura, stessi step — cambia il pannello laterale che si apre.

```javascript
const PIPELINE_F3 = [
  {
    id: 'osservazioni',
    label: 'Osservazioni',
    sublabel: 'La scena, il campo, il comportamento osservato',
    type: 'input',
    color: 'var(--color-primary)',
    descrizione: `Il punto di partenza: ciò che è osservabile nel campo
                  bambino-adulto-contesto. Non "il comportamento del bambino"
                  come unità isolata — la configurazione dell'incontro.
                  Cosa vedo? Cosa accade nel campo?`,
    casoGuida: `Il bambino prende il libro, lo apre, guarda alcune immagini,
                indica una figura, vocalizza, guarda l'adulto.
                Il genitore nomina l'immagine, sorride, aspetta.
                Il bambino torna al libro, gira pagina, mostra un'altra figura.
                Contesto: bilancio pediatrico · bambino 18-24 mesi · 3-5 minuti.`
  },
  {
    id: 'operatore',
    label: 'Operatore di lettura',
    sublabel: 'Operatore triadico — Campo / Posizione / Limite',
    type: 'operator',
    color: 'var(--color-f2)',
    descrizione: `Lo strumento concettuale prodotto in F2 che organizza
                  le osservazioni. Tre dimensioni simultanee:
                  Campo condiviso, Posizione soggettiva, Rapporto con il limite.
                  Non è una griglia: è la forma in cui il professionista vede.`,
    casoGuida: `Campo: bambino e adulto si orientano verso il libro
                come oggetto comune (gesto + sguardo + parola).
                Posizione: il bambino indica e mostra — c'è iniziativa soggettiva.
                Limite: il bambino accetta di condividere il controllo del libro;
                la sequenza si interrompe e riprende senza collasso.`
  },
  {
    id: 'ce',
    label: 'Configurazione Evolutiva (CE)',
    sublabel: 'Struttura del campo: nodi · direzione · tenuta · abitabilità',
    type: 'operator',
    color: 'var(--color-f2)',
    descrizione: `L'output della F2: la descrizione strutturale del campo.
                  Non descrive il bambino: descrive la configurazione
                  relazionale in cui il bambino esiste in quel momento.
                  Contiene il materiale grezzo con cui F3 lavora.`,
    casoGuida: `N1~ · N2↑ · N3~ · N4↓ · N5~ · N6~ · N7~
                Relazione: N2→N3 (MED) · Direzione: ↗ · Tenuta: T2 · Abitabilità: A±
                "Campo relazionale forte che sostiene accesso al mondo condiviso,
                con esplorazione ridotta ma in espansione. Configurazione fragile
                ma evolutivamente aperta."`
  },
  {
    id: 'nodo-dominante',
    label: 'Nodo dominante',
    sublabel: 'Non il nodo più basso — quello che muove di più il campo',
    type: 'operator',
    color: 'var(--color-f3)',
    descrizione: `Il primo passo F3: identificare il nodo la cui attivazione
                  produce il cambiamento più rilevante per l'abitabilità
                  del campo nella direzione evolutiva indicata (D).
                  Non è automatico: richiede lettura della CE per l'azione.`,
    casoGuida: `N3 (Accesso al mondo condiviso simbolico).
                Non N4↓ — che ha lo stato più basso — perché in questo contesto
                e con questa direzione (D↗), è N3 la porta verso cui il campo
                si sta già muovendo. N2↑ è la risorsa di sostegno.
                N4↓ è una tensione da non esacerbare, non il punto di lavoro.`
  },
  {
    id: 'funzione',
    label: 'Funzione dell\'azione',
    sublabel: 'Stabilizzare / Ampliare / Mediare / Proteggere',
    type: 'operator',
    color: 'var(--color-f3)',
    descrizione: `Il secondo passo F3: scegliere la funzione che il dispositivo
                  svolge sul campo. Non si sceglie la tecnica — si sceglie
                  la funzione. La funzione orienta tutta la costruzione del
                  dispositivo. Approfondita nel Modulo 4.`,
    casoGuida: `MEDIAZIONE — coordinare N2 (↑, risorsa) e N3 (~, zona di lavoro).
                Non stabilizzare: il campo non è in collasso (T2, non T0).
                Non ampliare: N4↓ sconsiglia di forzare ulteriore apertura.
                Mediare: sostenere la transizione già in corso N2→N3.`
  },
  {
    id: 'dispositivo',
    label: 'Micro-dispositivo contestualizzato',
    sublabel: 'Breve · integrabile · non specialistico · osservabile',
    type: 'final',
    color: 'var(--color-accent)',
    descrizione: `Il terzo passo F3: il dispositivo concreto che modifica
                  il campo relazionale di esperienza. Nasce dalla funzione,
                  non dalla tecnica. Deve soddisfare le tre proprietà (M1):
                  breve e integrabile, non specialistico e reversibile,
                  osservabile nei suoi effetti.`,
    casoGuida: `Il genitore segue l'interesse del bambino, nomina ciò che indica,
                attende, espande senza correggere.
                Il pediatra osserva senza interrompere la sequenza.
                Tempo: 5 minuti nel bilancio pediatrico.
                Indicatore di risonanza: la sequenza bambino-adulto si allunga
                e il bambino include l'adulto con sguardo + gesto + vocalizzazione.`
  }
];

const LETTURA_CE_PER_AZIONE = [
  {
    elemento: 'Nodo ↑ (sostenuto)',
    colore: 'var(--color-valid)',
    lettura_f2: 'Il campo regge su questa dimensione.',
    lettura_f3: 'Risorsa disponibile — su cui costruire il dispositivo. Non è il punto di lavoro: è il terreno.',
    esempio: 'N2↑ nel caso-guida: il campo relazionale è la risorsa che il dispositivo usa come leva.'
  },
  {
    elemento: 'Nodo ~ (neutro)',
    colore: 'var(--color-warning)',
    lettura_f2: 'Il campo non è né rinforzato né limitato su questa dimensione.',
    lettura_f3: 'Zona di possibile movimento — il candidato principale per il nodo dominante. È lo spazio in cui il campo può muoversi con un intervento lieve.',
    esempio: 'N3~ nel caso-guida: la condivisione del mondo simbolico è presente ma non stabile. È qui che si lavora.'
  },
  {
    elemento: 'Nodo ↓ (limitante)',
    colore: 'var(--color-invalid)',
    lettura_f2: 'Il campo è in tensione su questa dimensione.',
    lettura_f3: 'Tensione da considerare — ma non necessariamente il punto di lavoro. Va tenuta presente per non esacerbarla con il dispositivo.',
    esempio: 'N4↓ nel caso-guida: l\'esplorazione è ridotta. Un dispositivo che sovraccarica il campo ridurrebbe ulteriormente N4. Va evitato, non "riparato".'
  },
  {
    elemento: 'Relazione dominante (R)',
    colore: 'var(--color-f2)',
    lettura_f2: 'Il nodo che sostiene e il nodo che viene sostenuto: la direzione dell\'energia del campo.',
    lettura_f3: 'Orienta la scelta della funzione: se R è già N2→N3, la funzione è mediare quella transizione — non crearne un\'altra.',
    esempio: 'R: N2→N3 nel caso-guida suggerisce MEDIAZIONE: la risorsa (N2) sta già spingendo verso la zona di lavoro (N3).'
  },
  {
    elemento: 'Direzione (D)',
    colore: 'var(--color-f3)',
    lettura_f2: 'La traiettoria evolutiva del campo: espansione ↗, contrazione ↙, stabilità →, incertezza ↔.',
    lettura_f3: 'Vincolo sulla funzione: D↗ esclude stabilizzare come scelta principale. Il campo è già in espansione — si accompagna, non si ferma.',
    esempio: 'D↗ nel caso-guida: il campo si sta espandendo. Stabilizzare sarebbe incongruente. Mediare è coerente con la direzione.'
  },
  {
    elemento: 'Tenuta (T)',
    colore: 'var(--color-text-secondary)',
    lettura_f2: 'La solidità strutturale della configurazione: da T0 (collasso) a T3 (robusta).',
    lettura_f3: 'Indica la fragilità del campo e orienta la scelta della funzione e della scala del dispositivo. T2 = fragile ma aperta: il dispositivo deve essere leggero, non destabilizzante.',
    esempio: 'T2 nel caso-guida: la configurazione è fragile. Un micro-dispositivo lieve (5 minuti, modifica del ritmo) è appropriato. Un intervento intensivo sarebbe controindicato.'
  },
  {
    elemento: 'Abitabilità (A)',
    colore: 'var(--color-primary)',
    lettura_f2: 'La qualità dell\'esperienza nel campo: da A- (non abitabile) a A+ (pienamente abitabile).',
    lettura_f3: 'Indica l\'urgenza relativa dell\'intervento. A± = abitabilità moderata: non è un\'emergenza, ma c\'è spazio e motivazione per intervenire.',
    esempio: 'A± nel caso-guida: il campo è abbastanza abitabile da permettere una lettura condivisa. Non è in crisi — è un campo su cui un dispositivo leggero può fare differenza.'
  }
];

const CONFRONTO_LETTURA = {
  sinistra: {
    label: 'Lettura F2 — per la descrizione',
    colore: 'var(--color-f2)',
    titolo: 'Che stato ha il campo?',
    domanda: '"Come è organizzata questa configurazione?"',
    produce: [
      'Descrizione strutturale del campo (CE)',
      'Stato di ciascun nodo (↑ ↓ ~)',
      'Relazione dominante tra nodi',
      'Direzione evolutiva, tenuta, abitabilità',
      'Linguaggio condivisibile tra discipline'
    ],
    non_produce: 'F2 non risponde alla domanda: "Cosa faccio?"'
  },
  destra: {
    label: 'Lettura F3 — per l\'azione',
    colore: 'var(--color-f3)',
    titolo: 'Dove può muoversi il campo?',
    domanda: '"Da questa configurazione, verso dove si può andare?"',
    produce: [
      'Identificazione del nodo dominante (M3)',
      'Scelta della funzione dell\'azione (M4)',
      'Costruzione del micro-dispositivo (M5)',
      'Template F3 e output-tipo (M5)',
      'Logica decisionale (M7)'
    ],
    non_produce: 'F3 non modifica la CE: la legge in chiave operativa.'
  },
  footer: {
    colore: 'var(--color-f3)',
    testo: 'La stessa CE viene letta due volte: prima in F2 (cosa è questo campo?), poi in F3 (dove può andare questo campo?). La lettura F3 non invalida quella F2 — la usa come punto di partenza.'
  }
};

const CONFRONTO_ERRORE = {
  sinistra: {
    label: 'Partire dal sintomo',
    colore: 'var(--color-invalid)',
    titolo: 'Il sintomo come punto di partenza',
    items: [
      {
        sintomo: '"Il bambino non indica"',
        azione_errata: 'Training sul gesto di pointing',
        problema: 'Il pointing è un fenomeno di superficie. Intervenire su di esso non tocca il nodo (N3) che lo rende possibile.'
      },
      {
        sintomo: '"Il bambino non parla ancora"',
        azione_errata: 'Stimolazione linguistica diretta',
        problema: 'Il linguaggio emerge dallo scambio condiviso stabile. Lavorare sulla produzione verbale salta la configurazione che la produce.'
      },
      {
        sintomo: '"Il bambino è agitato durante la visita"',
        azione_errata: 'Strategie di gestione comportamentale',
        problema: 'L\'agitazione è la manifestazione di una configurazione (N1↓ in un campo non regolato). Gestire il comportamento non tocca la configurazione.'
      }
    ]
  },
  destra: {
    label: 'Partire dal nodo',
    colore: 'var(--color-f3)',
    titolo: 'Il nodo come punto di partenza',
    items: [
      {
        nodo: 'N3 (Mondo condiviso) ~ in campo con N2↑',
        lettura: 'Il gesto emerge quando il campo condiviso è stabile e sostenuto. La risorsa (N2) è già attiva.',
        azione: 'Mediare: aumentare la stabilità dello scambio condiviso perché la sequenza bambino-adulto si allunghi.'
      },
      {
        nodo: 'N3 ~ con R: N2→N3 e D↗',
        lettura: 'Il campo si sta già muovendo nella direzione giusta. Il linguaggio verrà quando N3 si stabilizza.',
        azione: 'Non stimolare la produzione verbale. Sostenere il campo in cui il linguaggio può emergere.'
      },
      {
        nodo: 'N1↓ in campo con T2',
        lettura: 'Il campo è fragile e la regolazione è sotto stress. Prima di qualsiasi altra cosa, il campo deve poter reggere.',
        azione: 'Stabilizzare: agire su ritmo e prevedibilità dell\'incontro prima di lavorare su qualsiasi altro nodo.'
      }
    ]
  }
};
```

---

## SLIDE F3.2.1 — La CE come input

**Tipo**: `narrative`
**Titolo**: Un output che diventa un input
**Sottotitolo**: Il passaggio F2 → F3

**Contenuto principale**:

Layout a colonna singola, narrativo. Abbondante spazio bianco.

**Sezione superiore — la posizione del professionista**:

Testo in `--text-xl`, centrato, con due righe evidenziate:

*Alla fine della Fase 2, il professionista ha in mano una Configurazione Evolutiva.*

*Non è la fine di un percorso — è l'inizio di un altro.*

**Sezione centrale — il contenuto della CE** (card con sfondo `--color-bg`, bordo `--color-border`):

Titolo in grassetto: *La CE contiene:*

Due colonne affiancate:

**Colonna sinistra** — "Ciò che la CE descrive":
- Lo stato di ciascun nodo (↑ sostenuto · ~ neutro · ↓ limitante)
- La relazione dominante tra nodi
- La direzione evolutiva del campo
- La tenuta strutturale e l'abitabilità

**Colonna destra** — "Ciò che la CE non contiene ancora":
- Il nodo su cui intervenire
- La funzione dell'azione
- Il dispositivo contestualizzato
- La decisione del professionista

Sotto le due colonne, un divisore sottile e il testo in corsivo:
*La CE produce leggibilità. F3 prende questa leggibilità e la trasforma in orientamento per l'azione.*

**Sezione inferiore — la domanda di F3** (blockquote, bordo sinistro `--color-f3`):

> *"Da questa configurazione, verso dove si può andare?
> Cosa nel campo può muoversi, con quale funzione, in quale direzione?"*

Sotto il blockquote, in `--text-sm`, `--color-text-muted`:
*Questa è la domanda che la pipeline F3 risponde — in tre passi.*

**Nota in footer**:
*In questo modulo vediamo la pipeline nella sua struttura completa. I moduli 3, 4 e 5 approfondiscono ciascun passo.*

---

## SLIDE F3.2.2 — I sei passi della trasformazione

**Tipo**: `diagram`
**Titolo**: La pipeline F3
**Sottotitolo**: Dall'osservazione al micro-dispositivo

**Contenuto principale**:

Componente `PipelineAnimator` con i dati da `PIPELINE_F3`. Modalità: **astratta** — ogni pannello laterale mostra il campo `descrizione` dello step, non il `casoGuida`.

**Comportamento della slide**:

All'entrata, tutti i nodi della pipeline sono visibili ma con opacity 0.3. Un testo introduttivo al centro (`--text-base`, `--color-text-muted`): *"Clicca su ogni passo per esplorarlo — o usa il pulsante per animare la sequenza."*

Un pulsante in alto a destra: `▶ Anima sequenza` — attiva l'animazione progressiva (600ms per step): ogni step si illumina in sequenza, il pannello laterale si aggiorna automaticamente.

**Pannello laterale fisso** (a destra della pipeline, 40% larghezza):

Per ogni step selezionato, mostra:
- Badge colorato con `label`
- `sublabel` in `--text-sm`, `--color-text-secondary`
- `descrizione` in testo normale
- Separatore
- Chip distinto per step F2 (`--color-f2`) o F3 (`--color-f3`), con etichetta:
  - Step 1–3: `← Prodotto da F2`
  - Step 4–6: `← Passi F3`

**Nota visiva importante**: il confine F2/F3 deve essere reso visibile nella pipeline con una linea tratteggiata orizzontale tra il nodo CE (step 3) e il nodo Nodo dominante (step 4), con l'etichetta: *"F2 → F3"* in `--text-sm`.

**Legenda in basso**:
Due chip:
- `● Input` (colore `--color-primary`)
- `● Operatori F2` (colore `--color-f2`)
- `● Operatori F3` (colore `--color-f3`)
- `● Output` (colore `--color-accent`)

**Nota in footer**:
*I passi 1–3 sono il territorio della F2 — già percorso. I passi 4–6 sono il territorio della F3 — il corso da qui in poi.*

---

## SLIDE F3.2.3 — Come si legge la CE per l'azione

**Tipo**: `standard`
**Titolo**: La CE è un testo da leggere due volte
**Sottotitolo**: Cosa cerca F3 in una Configurazione Evolutiva

**Contenuto principale**:

Layout a colonna singola con tabella interattiva. La slide insegna come ogni elemento della CE si legge in chiave F3.

**Sezione superiore — il principio**:

Testo in `--text-lg`:

F2 legge la CE per descrivere lo stato del campo.
F3 rilegge la stessa CE per capire dove il campo può muoversi.

*Stessa CE. Due domande diverse. Due letture diverse.*

**Sezione centrale — la tabella** (usa i dati da `LETTURA_CE_PER_AZIONE`):

Tabella a tre colonne con riga di intestazione:

| Elemento CE | Lettura F2 — "Che stato?" | Lettura F3 — "Cosa fa?" |
|-------------|--------------------------|------------------------|

Ogni riga ha:
- **Colonna 1**: chip colorato con l'elemento (↑ verde / ~ arancione / ↓ rosso / lettere per R, D, T, A)
- **Colonna 2**: lettura F2 in `--color-text-secondary`, corsivo
- **Colonna 3**: lettura F3 in `--color-text`, testo normale — leggermente più in risalto

Le righe sono espandibili: cliccando una riga si apre sotto di essa il campo `esempio` in una box tenue (`--color-bg`, bordo `--color-border`), con etichetta *"Nel caso-guida:"* in `--text-sm`.

**Sezione inferiore — la regola operativa**:

Box con sfondo `--color-primary-light`, bordo sinistro `--color-f3`:

**Regola di lettura F3**

- I nodi **↑** sono risorse — su di loro si costruisce il dispositivo
- I nodi **~** sono zone di movimento — il nodo dominante si cerca qui
- I nodi **↓** sono tensioni — non sono automaticamente il punto di lavoro; vanno rispettati per non esacerbarli
- La **relazione R** orienta la funzione
- La **direzione D** vincola la scelta: D↗ esclude stabilizzare come prima opzione
- La **tenuta T** calibra la scala del dispositivo

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-20`
- Label: Errore di lettura tipico
- Testo: *Il nodo dominante non è il nodo con lo stato più basso. Un nodo ↓ può essere una tensione da non esacerbare, non il punto di lavoro. Confondere i due porta a dispositivi controproducenti.*

---

## SLIDE F3.2.4 — Leggere per la descrizione, leggere per l'azione

**Tipo**: `comparison`
**Titolo**: La stessa CE, due letture
**Sottotitolo**: F2 e F3 davanti alla stessa Configurazione Evolutiva

**Contenuto principale**:

Componente `ComparisonPanel` con i dati da `CONFRONTO_LETTURA`.

**Colonna sinistra** — "Lettura F2" (bordo `--color-f2`, sfondo tenue):
- Titolo grande: *"Che stato ha il campo?"*
- Domanda in corsivo
- Lista `produce` con bullet sottili
- Nota `non_produce` in `--text-sm`, `--color-text-muted`

**Colonna destra** — "Lettura F3" (bordo `--color-f3`, sfondo tenue):
- Titolo grande: *"Dove può muoversi il campo?"*
- Domanda in corsivo
- Lista `produce` con bullet sottili
- Nota `non_produce` in `--text-sm`, `--color-text-muted`

**Footer a piena larghezza** (sfondo `--color-primary-light`, bordo sinistro `--color-f3`):
Testo da `CONFRONTO_LETTURA.footer.testo`.

**Elemento aggiuntivo sopra il pannello** — visualizzazione visiva del passaggio:

Schema orizzontale centrato (`--text-sm`):

```
  [CE]  ──────── legge ──────────▶  [F2: "Questo campo è..."]
   │
   └──── rilegge ────────────────▶  [F3: "Questo campo può..."]
```

La doppia freccia dallo stesso punto (la CE) verso due destinazioni diverse rende visiva l'idea di "due letture, stessa sorgente".

---

## SLIDE F3.2.5 — L'errore tipico: il sintomo invece del nodo

**Tipo**: `comparison`
**Titolo**: Dal sintomo al nodo, non il contrario
**Sottotitolo**: L'errore che svuota la pipeline

**Contenuto principale**:

Componente `ComparisonPanel` con i dati da `CONFRONTO_ERRORE`.

**Colonna sinistra** — "Partire dal sintomo" (bordo `--color-invalid`, sfondo rosso tenuissimo):

Titolo: *"Il sintomo come punto di partenza"*

Tre blocchi da `CONFRONTO_ERRORE.sinistra.items`, ognuno con:
- `sintomo` in grassetto, virgolettato, `--text-base`
- `azione_errata` con etichetta *"Risposta frequente:"* in `--text-sm`
- `problema` in corsivo, `--color-text-secondary`, con icona ⚠ discreta

**Colonna destra** — "Partire dal nodo" (bordo `--color-f3`, sfondo blu tenuissimo):

Titolo: *"Il nodo come punto di partenza"*

Tre blocchi da `CONFRONTO_ERRORE.destra.items`, ognuno con:
- `nodo` come chip colorato con il colore del nodo corrispondente
- `lettura` in corsivo, `--color-text-secondary`
- `azione` in grassetto con etichetta *"F3:"* in `--text-sm`, `--color-f3`

**Elemento visivo tra le colonne** — freccia diagonale (SVG semplice) con etichetta:
*"La pipeline parte dall'osservazione, non dal sintomo"*

**Sezione inferiore** — testo di raccordo (`--text-base`, `--color-text-secondary`, centrato):

*Il sintomo è l'effetto visibile di una configurazione. Intervenire sul sintomo significa agire sull'effetto senza modificare le condizioni che lo producono. La pipeline F3 parte dall'osservazione del campo e percorre la catena fino al dispositivo — non parte dall'effetto cercando la causa.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-21`
- Label: Errore della corsia rapida
- Testo: *Vedere un comportamento problematico e costruire un dispositivo diretto su quel comportamento — saltando CE, nodo dominante e funzione — non è F3. È la "corsia rapida" che bypassa la leggibilità e ricade nella tecnicizzazione precoce identificata in F2.*

---

## SLIDE F3.2.6 — La pipeline del caso-guida

**Tipo**: `interactive`
**Titolo**: La pipeline applicata
**Sottotitolo**: Il caso-guida passo per passo

**Contenuto principale**:

Stesso componente `PipelineAnimator` della slide F3.2.2, ma con modalità **caso-guida** — ogni pannello laterale mostra il campo `casoGuida` dello step, non la `descrizione`.

**Differenze visive rispetto a F3.2.2**:

1. La pipeline parte già completamente illuminata (opacity 1.0 su tutti i nodi) — l'utente non deve "scoprire" i passi, deve leggerli applicati.
2. In alto sopra la pipeline, una card narrativa compatta (sfondo `--color-primary-light`, bordo `--color-primary`, testo `--text-sm` in corsivo) richiama la scena del caso-guida. **Testo da `window.CASO_GUIDA_F3.scena`** — primissime due righe, seguite da `[...]`.
3. Il confine F2/F3 (linea tratteggiata tra step 3 e step 4) è più prominente: sopra la linea, etichetta *"F2 — prodotto nel corso precedente"*, sotto, etichetta *"F3 — stiamo costruendo questo"*.

**Pannello laterale** — per ogni step selezionato mostra:
- Chip colorato con label e fase (F2/F3)
- `casoGuida` in testo normale, eventualmente su più righe con `<br>` come separatori
- Per gli step F3 (nodo dominante, funzione, dispositivo): etichetta *"— Approfondito in M3 / M4 / M5"* in `--text-sm`, `--color-text-muted`

**Step 3 (CE)**: questo pannello usa il componente `CEDisplay` in formato compatto — la tabella dei nodi con stati e colori — invece di solo testo. Richiamare `CEDisplay(window.CASO_GUIDA_F3.ce, container, { compact: true })`.

**Pulsante animazione**: `▶ Percorri la pipeline` — stesso comportamento di F3.2.2 ma più lento (900ms per step) dato il contenuto più ricco.

**Nota in footer**:
*Nei prossimi tre moduli (M3, M4, M5) ogni step F3 verrà approfondito singolarmente. Qui vediamo la forma completa: la pipeline come struttura, il caso-guida come materiale.*

---

## SLIDE F3.2.7 — Il confine che la pipeline tiene

**Tipo**: `standard`
**Titolo**: F2 produce leggibilità. F3 orienta l'azione.
**Sottotitolo**: Il confine che non si deve attraversare al contrario

**Contenuto principale**:

Layout a colonna singola. Slide concettualmente densa ma visivamente pulita.

**Sezione superiore — il confine in una frase**:

Blockquote centrato (bordo sinistro `--color-f3`):

> *"La CE prodotta da F2 è un input per F3, non un prodotto che F3 può riscrivere.
> F3 legge la CE per l'azione — non la modifica per adattarla all'azione desiderata."*

**Sezione centrale — le due direzioni illegittime** (due chip/box affiancati, sfondo rosso tenuissimo, bordo `--color-invalid`):

**Direzione illegittima ①** — da F3 verso F2:
*"La CE dice N3~, ma io voglio lavorare su N4. Rileggere la CE come se N4 fosse il nodo dominante."*
→ Problema: si modifica la descrizione per adattarla all'intervento già deciso. La leggibilità viene sacrificata all'azione.

**Direzione illegittima ②** — saltare F2 per arrivare a F3:
*"Non ho una CE formale ma so che il bambino ha difficoltà linguistiche. Costruisco direttamente il dispositivo."*
→ Problema: senza CE non c'è nodo dominante fondato. Il dispositivo poggia su un sintomo, non su una configurazione.

**Sezione inferiore — la regola**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

**La pipeline funziona in una sola direzione**

F1 → F2 → F3: ogni fase riceve dall'anteriore e produce per la successiva.

Tornare indietro a modificare la CE per renderla compatibile con l'azione che si vuole fare è l'errore metodologico più grave di F3: trasforma la leggibilità in giustificazione post-hoc.

*Il confine F2/F3 non è una formalità procedurale — è la garanzia che l'azione professionale poggia su una lettura strutturale fondata, non sull'intenzione del professionista.*

**Chiusura del modulo** — testo centrato, spazio bianco sopra, `--text-lg`, corsivo:

*La pipeline è chiara. Il confine è solido. Da qui in poi si percorre il lato F3 della pipeline — passo per passo.*

Badge modulo successivo: `→ Modulo 3 — Il nodo dominante`

---

## Note per l'implementazione

### Slide F3.2.2 e F3.2.6 — PipelineAnimator con due modalità

Il componente `PipelineAnimator` viene istanziato due volte in questo modulo, con gli stessi dati (`PIPELINE_F3`) ma con un parametro di modalità diverso:

```javascript
// Slide F3.2.2 — modalità astratta
PipelineAnimator(PIPELINE_F3, container, { mode: 'abstract', initialOpacity: 0.3 });

// Slide F3.2.6 — modalità caso-guida
PipelineAnimator(PIPELINE_F3, container, { mode: 'caso', initialOpacity: 1.0 });
```

La differenza è nel pannello laterale: `mode: 'abstract'` mostra `step.descrizione`, `mode: 'caso'` mostra `step.casoGuida`. Per lo step CE in modalità caso-guida, il renderer controlla `step.id === 'ce'` e usa `CEDisplay` invece del testo.

### Slide F3.2.2 — Linea di confine F2/F3

La linea tratteggiata orizzontale tra step 3 e step 4 può essere implementata come un `<div class="pipeline-boundary">` assoluto posizionato a metà tra i due nodi. Con `border-top: 2px dashed var(--color-border)` e le etichette come `<span>` ai lati. Non interferisce con la logica del componente se i nodi sono già posizionati con margini definiti.

### Slide F3.2.3 — Tabella espandibile

Le righe della tabella usano lo stesso meccanismo accordion delle card espandibili: `data-expandable` sull'elemento `<tr>`, e un `<tr class="expanded-row">` che appare sotto. L'animazione è `slide-down` (200ms) — stessa usata per `ExpandableCards`.

### Slide F3.2.6 — CEDisplay compatto

Lo step CE nella pipeline del caso-guida richiede `CEDisplay` in modalità `compact: true`, che produce una versione ridotta della tabella (senza la colonna "Lettura", solo Nodo + Stato colorato + Label breve) con dimensione font `--text-sm`. Questo è l'unico punto nel corso dove CEDisplay viene usato dentro un altro componente.

### Transizione M1 → M2

All'entrata nel Modulo 2, nessuna transizione speciale. Il titolo del modulo appare con il normale fade-in (400ms). Opzionalmente: nella prima slide (F3.2.1), la card "Ciò che la CE non contiene ancora" può entrare con un leggero delay (400ms) rispetto alla card "Ciò che la CE descrive" — a enfatizzare la struttura prima / dopo.
