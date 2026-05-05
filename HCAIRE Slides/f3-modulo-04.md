# f3-modulo-04 — Le quattro funzioni
**Numero slide**: 7
**Colore accent**: `#3498db`
**Tipo prevalente**: interactive + standard

---

## Dati globali del modulo

Definire in `m04.js` le seguenti costanti. `QUATTRO_FUNZIONI` è la sorgente primaria del modulo e viene usata in più slide.

```javascript
const QUATTRO_FUNZIONI = [
  {
    id: 'stabilizzare',
    nome: 'Stabilizzare',
    colore: 'var(--color-fn-stabilizzare)',
    badge: 'STA',
    azione_sul_campo: 'Ridurre la disorganizzazione in atto',
    quando: `Quando il campo è in collasso o sotto forte stress (T0–T1).
             La priorità è che l'esperienza non si frammenti ulteriormente.
             Non si lavora su nessun altro nodo finché il campo non regge.`,
    nodi_tipici: ['N1', 'N2'],
    segnali_CE: [
      'N1↓ o N2↓',
      'Tenuta T0 o T1 (bassa o critica)',
      'Abitabilità A– (campo non abitabile)',
      'Direzione D↙ (contrazione)'
    ],
    micro_azioni: [
      'Ridurre gli stimoli ambientali: meno input simultanei',
      'Introdurre ritmo e prevedibilità nella sequenza dell\'incontro',
      'Presenza adulta regolativa: voce calma, postura stabile, movimenti lenti',
      'Ridurre durata e complessità dell\'interazione'
    ],
    esempio: `Bilancio pediatrico: durante l'esame fisico il bambino si irrigidisce,
              piange, cerca il genitore. Il campo si sta disorganizzando (N1↓).
              Il genitore lo prende, gli parla piano. Il pediatra rallenta e aspetta.
              Prima di qualsiasi altra cosa il campo deve poter reggere.
              Questa è stabilizzazione.`,
    errore: `"Stimolo il bambino per farlo uscire dalla crisi."
             L'opposto: durante la disorganizzazione, la stimolazione
             aumenta il carico. Prima si stabilizza, poi si lavora su altro.`,
    non_confondere: `Con Proteggere: Stabilizzare risponde a una disorganizzazione
                     già in atto. Proteggere la previene prima che avvenga.`
  },
  {
    id: 'ampliare',
    nome: 'Ampliare',
    colore: 'var(--color-fn-ampliare)',
    badge: 'AMP',
    azione_sul_campo: 'Aumentare l\'esplorabilità del campo',
    quando: `Quando il campo è stabile e l'abitabilità è buona,
             ma c'è poco movimento evolutivo. Il bambino potrebbe esplorare
             ma il campo non gli offre abbastanza apertura,
             o l'iniziativa spontanea non trova sostegno.`,
    nodi_tipici: ['N4', 'N7'],
    segnali_CE: [
      'N4↓ o N7~ in campo stabile',
      'Tenuta T2–T3 (sufficiente o buona)',
      'Abitabilità A± o A+ con D→ (stabilità senza espansione)',
      'N1 e N2 sostenuti: il campo regge'
    ],
    micro_azioni: [
      'Introdurre un elemento nuovo ma tollerabile accanto ai familiari',
      'Sostenere e amplificare l\'iniziativa spontanea senza dirigerla',
      'Ridurre leggermente la prevedibilità (sorpresa tollerabile)',
      'Lasciare spazio al bambino per avvicinarsi al nuovo senza pressione'
    ],
    esempio: `Al nido, un bambino con buona regolazione (N1~, N2↑)
              che torna sempre agli stessi oggetti (N7~, N4↓ in campo stabile).
              L'educatrice posiziona un oggetto nuovo vicino a quelli familiari
              e aspetta senza commentare. Il bambino si avvicina da solo.
              Questo è ampliamento.`,
    errore: `"Amplio il campo anche quando il bambino è agitato."
             Se T0–T1, la novità amplifica la disorganizzazione già presente.
             Ampliare richiede che il campo regga già.`,
    non_confondere: `Con Mediare: Ampliare apre verso il nuovo (non ancora presente).
                     Mediare sostiene una transizione già avviata tra nodi che ci sono.`
  },
  {
    id: 'mediare',
    nome: 'Mediare',
    colore: 'var(--color-fn-mediare)',
    badge: 'MED',
    azione_sul_campo: 'Sostenere una transizione già in corso tra nodi',
    quando: `Quando una risorsa attiva (↑) sta già spingendo verso un nodo neutro (~)
             e la relazione R lo indica. Il campo è già in transizione:
             non si tratta di avviarla, ma di sostenerla perché si completi.`,
    nodi_tipici: ['N2→N3', 'N1↔N4'],
    segnali_CE: [
      'R: Nodo↑ → Nodo~ (la transizione è già in corso)',
      'Direzione D↗ (espansione in atto)',
      'Tenuta T2 (fragile ma aperto)',
      'Abitabilità A±'
    ],
    micro_azioni: [
      'Sostenere la sequenza che il bambino ha già avviato senza interromperla',
      'Rallentare il ritmo per lasciare che la transizione si completi',
      'Nominare senza anticipare: l\'adulto segue, non guida',
      'Mantenere la continuità dello scambio senza aggiungere elementi nuovi'
    ],
    esempio: `Il caso-guida: N2↑ sta già sostenendo N3~. R: N2→N3.
              La transizione è in corso — il bambino indica, vocalizza, cerca l'adulto.
              Il genitore rallenta, nomina ciò che il bambino indica, aspetta.
              Non introduce novità. Non dirige. Sostiene ciò che si sta già muovendo.
              Questo è mediazione.`,
    errore: `"Medierò introducendo un elemento nuovo che faciliti il passaggio."
             Non è mediazione: è ampliamento. Mediare non aggiunge nulla al campo:
             sostiene ciò che è già in movimento. Aggiungere elementi nuovi
             può interrompere la transizione invece di sostenerla.`,
    non_confondere: `Con Ampliare: Mediare non introduce novità — sostiene una transizione già avviata.
                     Con Stabilizzare: Mediare presuppone un campo abbastanza stabile
                     da poter fare la transizione (almeno T2).`
  },
  {
    id: 'proteggere',
    nome: 'Proteggere',
    colore: 'var(--color-fn-proteggere)',
    badge: 'PRO',
    azione_sul_campo: 'Prevenire il sovraccarico prima che avvenga',
    quando: `Quando il campo è a rischio di collasso per eccesso di stimoli,
             richieste o aspettative — ma non è ancora disorganizzato.
             Proteggere è preventiva per definizione:
             agisce prima che la disorganizzazione avvenga.`,
    nodi_tipici: ['N1', 'N4 (con ↓)'],
    segnali_CE: [
      'N1~ con tenuta T1 (fragile)',
      'N4↓ con contesto ad alto carico percettivo',
      'Abitabilità A± con rischio di deterioramento',
      'Contesto: molti adulti, rumore, tempo limitato, procedure complesse'
    ],
    micro_azioni: [
      'Ridurre preventivamente il numero di richieste e interlocutori',
      'Creare o mantenere una zona di minore stimolazione nel contesto',
      'Interrompere l\'interazione prima che il bambino si saturi',
      'Anticipare i momenti di carico e prepararli (prevedibilità protettiva)'
    ],
    esempio: `Un bambino in un setting affollato con N1~ e N4↓.
              Prima che N1 scenda a ↓, il professionista riduce il numero
              di adulti presenti, abbassa il volume dell'ambiente,
              accorcia la durata dell'esame.
              Non c'è ancora disorganizzazione — si previene.
              Questo è protezione.`,
    errore: `"Proteggo aspettando che il bambino si agiti."
             Troppo tardi: è già Stabilizzare. Proteggere è preventiva.
             Se aspetto che N1 scenda a ↓ per intervenire,
             la funzione necessaria è cambiata.`,
    non_confondere: `Con Stabilizzare: Proteggere è preventiva (prima del collasso),
                     Stabilizzare è reattiva (durante o dopo).
                     Il segnale discriminante è lo stato di N1: ~ → Proteggere, ↓ → Stabilizzare.`
  }
];

const SEGNALI_CE_FUNZIONE = [
  {
    id: 'sta',
    segnale: 'N1↓ o N2↓ · T0–T1 · A– · D↙',
    funzione: 'stabilizzare',
    colore: 'var(--color-fn-stabilizzare)',
    motivazione: 'Il campo è in collasso o ci va vicino. La priorità assoluta è che l\'esperienza non si frammenti. Nessun altro lavoro prima di questo.'
  },
  {
    id: 'amp',
    segnale: 'N4↓ o N7~ in T2–T3 · A± o A+ · D→',
    funzione: 'ampliare',
    colore: 'var(--color-fn-ampliare)',
    motivazione: 'Il campo regge ma è fermo. C\'è abitabilità senza espansione. Si apre il campo verso possibilità nuove che il bambino può esplorare in sicurezza.'
  },
  {
    id: 'med',
    segnale: 'R: Nodo↑→Nodo~ · D↗ · T2 · A±',
    funzione: 'mediare',
    colore: 'var(--color-fn-mediare)',
    motivazione: 'Una transizione è già in corso. Il campo si sta muovendo da solo: si accompagna, non si forza. Aggiungere troppo interromperebbe il movimento.'
  },
  {
    id: 'pro',
    segnale: 'N1~ con T1 · N4↓ · contesto ad alto carico',
    funzione: 'proteggere',
    colore: 'var(--color-fn-proteggere)',
    motivazione: 'Il campo non è ancora in crisi ma è esposto. Si interviene preventivamente prima che N1 scenda o che il sovraccarico produca disorganizzazione.'
  }
];

const ERRORI_FUNZIONE = [
  {
    id: 'ef1',
    errore: 'Ampliare quando il campo è fragile (T0–T1)',
    situazione: 'Il bambino è in difficoltà, agitato o disorganizzato. Il professionista introduce novità per "stimolarlo".',
    cosa_succede: 'La novità aumenta il carico su un campo già sotto stress. L\'agitazione peggiora.',
    funzione_corretta: 'Stabilizzare. Prima che il campo regga, non si aggiunge nulla.'
  },
  {
    id: 'ef2',
    errore: 'Stabilizzare quando il campo è già regolato (T2–T3)',
    situazione: 'Il campo è stabile e l\'abitabilità è buona. Il professionista riduce comunque la complessità e introduce routine eccessive.',
    cosa_succede: 'Stagnazione. Il bambino non ha stimolo per muoversi. Il campo si "addormenta" invece di espandersi.',
    funzione_corretta: 'Ampliare o Mediare, a seconda dei nodi e di R.'
  },
  {
    id: 'ef3',
    errore: 'Mediare senza che R indichi la transizione',
    situazione: 'Il professionista sceglie un nodo ~ come "obiettivo" e cerca di mediare un passaggio verso di lui — ma R non punta in quella direzione e D non è coerente.',
    cosa_succede: 'Si "medierebbe" una transizione che il campo non ha avviato. Il dispositivo è privo di aggancio: non trova risonanza.',
    funzione_corretta: 'Rivalutare la CE. Se la transizione non è in corso, la funzione è Ampliare (per avviarla) o Stabilizzare (se il campo non regge).'
  },
  {
    id: 'ef4',
    errore: 'Confondere Proteggere e Stabilizzare sul timing',
    situazione: 'Il bambino si è già disorganizzato. Il professionista riduce gli stimoli preventivamente — ma la disorganizzazione è già in atto.',
    cosa_succede: 'Le misure preventive non bastano quando la crisi è già iniziata. Si perde tempo prezioso di regolazione attiva.',
    funzione_corretta: 'Stabilizzare: la disorganizzazione è in atto. Proteggere vale prima, non durante.'
  }
];

const SEQUENZA_DECISIONALE = [
  {
    id: 's1',
    passo: '① Leggi T e A nella CE',
    domanda: 'Il campo regge? Qual è l\'abitabilità?',
    logica: [
      { condizione: 'T0–T1 o A–', esito: '→ Stabilizzare è la prima priorità. Stop.', colore: 'var(--color-fn-stabilizzare)' },
      { condizione: 'T1 + contesto ad alto carico', esito: '→ Proteggere preventivamente.', colore: 'var(--color-fn-proteggere)' },
      { condizione: 'T2–T3 e A± o A+', esito: '→ Continua al passo ②.', colore: 'var(--color-text-muted)' }
    ]
  },
  {
    id: 's2',
    passo: '② Leggi R e D nella CE',
    domanda: 'C\'è una transizione già in corso?',
    logica: [
      { condizione: 'R: Nodo↑ → Nodo~ e D↗', esito: '→ Mediare: la transizione è avviata. Accompagnala.', colore: 'var(--color-fn-mediare)' },
      { condizione: 'R assente o D→ o D↙', esito: '→ Continua al passo ③.', colore: 'var(--color-text-muted)' }
    ]
  },
  {
    id: 's3',
    passo: '③ Leggi N4 e N7 nella CE',
    domanda: 'Il campo è stabile ma poco espansivo?',
    logica: [
      { condizione: 'N4↓ o N7~ in campo stabile con D→', esito: '→ Ampliare: il campo è pronto per muoversi ma non si muove.', colore: 'var(--color-fn-ampliare)' },
      { condizione: 'N4 e N7 già sostenuti', esito: '→ Rivalutare il nodo dominante. La CE può richiedere un\'altra lettura.', colore: 'var(--color-text-muted)' }
    ]
  }
];
```

---

## SLIDE F3.4.1 — Funzione, non tecnica

**Tipo**: `comparison`
**Titolo**: La domanda sbagliata e quella giusta
**Sottotitolo**: Il punto di partenza di ogni strumento F3

**Contenuto principale**:

Componente `ComparisonPanel`. La slide stabilisce il principio fondamentale del modulo prima di qualsiasi contenuto sulle quattro funzioni.

**Colonna sinistra** — "La domanda per tecnica" (bordo `--color-invalid`, sfondo rosso tenuissimo):

**Titolo**: *"Quale tecnica uso?"*

Tre esempi di domande per tecnica:
- *"Uso la lettura dialogica? Il play-based therapy? Lo scaffolding?"*
- *"Qual è il protocollo indicato per questo caso?"*
- *"Cosa funziona di solito con bambini come questo?"*

Sotto, in corsivo `--color-text-secondary`:
Il punto di partenza è la tecnica. La CE serve, se serve, per giustificare la scelta già fatta.

**Colonna destra** — "La domanda per funzione" (bordo `--color-f3`, sfondo tenue):

**Titolo**: *"Quale funzione deve svolgere il dispositivo?"*

Tre esempi di domande per funzione:
- *"Questo campo deve essere stabilizzato, ampliato, mediato o protetto?"*
- *"Cosa deve fare il dispositivo sul campo — non come si chiama?"*
- *"La funzione nasce dal nodo dominante e dalla CE — poi si sceglie il dispositivo."*

Sotto, in corsivo `--color-f3`:
La CE orienta la funzione. La funzione orienta il dispositivo. La tecnica viene ultima — se viene.

**Footer a piena larghezza** (sfondo `--color-primary-light`, bordo `--color-f3`):

*"Lo strumento nasce scegliendo la funzione, non la tecnica."*

Sotto: *La stessa funzione (es. Mediare) può essere svolta da dispositivi molto diversi: lettura dialogica, gioco imitativo, routine di nomina condivisa. Ciò che li accomuna non è la forma ma la funzione che svolgono sul campo.*

**Elemento visivo aggiuntivo** — schema orizzontale centrato sotto il pannello:

```
[CE + nodo dominante]  →  [FUNZIONE]  →  [Dispositivo]  →  [Tecnica (se utile)]
                                ↑
                          qui si decide
```

**Nota in footer**:
*In questo modulo impariamo le quattro funzioni. Il Modulo 5 costruisce il dispositivo a partire da esse.*

---

## SLIDE F3.4.2 — Le quattro funzioni

**Tipo**: `interactive`
**Titolo**: Quattro funzioni, una logica
**Sottotitolo**: Cosa può fare un dispositivo F3 sul campo

**Contenuto principale**:

Componente `ExpandableCards` con i dati da `QUATTRO_FUNZIONI`, `multiOpen: false` — una card alla volta.

**Struttura card fronte** (stato compatto):

```
[Badge colorato: STA/AMP/MED/PRO]  [Nome grande]
[azione_sul_campo — corsivo]
[quando — prima frase]
[Chip nodi tipici: es. "N1 · N2"]          [↓ Espandi]
```

**Card espansa** (aggiunge cinque sezioni):

**Sezione 1 — Quando si usa** (bordo sinistro nel colore della funzione):
Testo `quando` completo.

**Sezione 2 — Segnali CE** (sfondo `--color-bg`):
Etichetta *"Segnali nella CE:"* + lista da `segnali_CE` con chip piccoli colorati.

**Sezione 3 — Micro-azioni esemplari** (lista ordinata):
Etichetta *"Micro-azioni tipiche:"* + lista da `micro_azioni`.

**Sezione 4 — Esempio** (box narrativo, sfondo tenue, corsivo):
Etichetta *"Esempio:"* + testo `esempio`.

**Sezione 5 — Da non confondere** (box con bordo `--color-warning`):
Due righe: *"Errore tipico:"* testo `errore` · *"Non confondere con:"* testo `non_confondere`.

**Elemento sopra le card** — quattro chip fissi affiancati come indice rapido delle funzioni:

```
[● STA Stabilizzare]  [● AMP Ampliare]  [● MED Mediare]  [● PRO Proteggere]
```

Ogni chip è cliccabile e apre direttamente la card corrispondente. I colori dei chip sono `--color-fn-X`.

**Pulsante globale** "Espandi tutto / Comprimi tutto" (in alto a destra).

**Nota in footer**:
*Le quattro funzioni non sono esaustive di tutto ciò che un professionista può fare — sono le quattro forme legittime di azione nel perimetro metodologico di F3.*

---

## SLIDE F3.4.3 — Dalla CE alla funzione: i segnali

**Tipo**: `standard`
**Titolo**: Come la CE orienta la scelta
**Sottotitolo**: Quattro segnali, quattro funzioni

**Contenuto principale**:

Layout a colonna singola. La slide traduce i segnali CE in funzioni in modo diretto e visivamente chiaro.

**Sezione superiore — il principio**:

Testo `--text-lg`:
La funzione non si sceglie dall'esterno della CE: emerge da ciò che la CE contiene.
Quattro configurazioni di segnali corrispondono alle quattro funzioni.

*Non è una regola meccanica: è un orientamento. La lettura configurazionale richiede sempre giudizio professionale.*

**Sezione centrale — tabella orientativa** (dati da `SEGNALI_CE_FUNZIONE`):

Tabella a tre colonne:

| Segnali nella CE | Funzione | Motivazione |
|-----------------|----------|-------------|

Ogni riga ha:
- **Colonna 1**: i segnali come chip piccoli nel colore semantico (↑↓~ + T/A/D/R simboli)
- **Colonna 2**: badge funzione colorato (`STA` / `AMP` / `MED` / `PRO`) + nome
- **Colonna 3**: motivazione in `--text-sm`, corsivo

Le righe hanno un bordo sinistro sottile nel colore della funzione corrispondente.

**Sezione inferiore — priorità tra funzioni**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

**Se ci sono più segnali presenti contemporaneamente:**

Ordine di priorità:
1. **Stabilizzare** — sempre prima, se T0–T1 o A–. Nessun altro lavoro prima.
2. **Proteggere** — subito dopo, se il campo è a rischio imminente.
3. **Mediare** — se il campo regge e R indica una transizione in corso.
4. **Ampliare** — se il campo regge, R non indica transizioni e D→.

*La priorità non è una gerarchia di valore: è una sequenza logica. Stabilizzare prima di ampliare non significa che stabilizzare sia "più importante" — significa che un campo instabile non può ampliare.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-40`
- Label: Non invertire la sequenza
- Testo: *Un dispositivo che amplia su un campo T0 produce disorganizzazione. Un dispositivo che stabilizza un campo T3 produce stagnazione. La funzione e la tenuta devono essere coerenti.*

---

## SLIDE F3.4.4 — Errori di funzione

**Tipo**: `interactive`
**Titolo**: Quando la funzione è sbagliata
**Sottotitolo**: Quattro errori e cosa producono nel campo

**Contenuto principale**:

Quattro card orizzontali compatte (non `ExpandableCards` — tutte visibili, non espandibili) con i dati da `ERRORI_FUNZIONE`. Layout verticale, una sotto l'altra.

**Struttura di ogni card** (sempre visibile):

```
┌─────────────────────────────────────────────────────────────┐
│  [Numero ①②③④ in --color-invalid]  [errore in --text-base grassetto]
│  
│  Situazione: [situazione in --text-sm, --color-text-secondary]
│  
│  Cosa succede: [cosa_succede in --text-sm, bordo sinistro --color-warning]
│  
│  Funzione corretta: [chip badge colorato] [funzione_corretta in --text-sm]
└─────────────────────────────────────────────────────────────┘
```

Le card sono separate da un divisore `--color-border`.

**Elemento visivo aggiuntivo** — sopra le card, riga di quattro chip in rosso molto tenue con etichetta introduttiva:

*"Quattro errori ricorrenti nella scelta della funzione:"*

**Sezione inferiore** — testo di raccordo in `--text-sm`, `--color-text-muted`, centrato:

*Questi errori hanno quasi sempre la stessa radice: la funzione viene scelta prima di aver letto la CE, oppure la CE viene letta ma non il segnale rilevante (T, R, D). L'antidoto è la sequenza decisionale — che vediamo nella slide successiva.*

---

## SLIDE F3.4.5 — La sequenza decisionale

**Tipo**: `diagram`
**Titolo**: Tre domande, in ordine
**Sottotitolo**: Dalla CE alla funzione: una sequenza, non un algoritmo

**Contenuto principale**:

Schema visivo centrale a tre livelli verticali (non `PipelineAnimator` — schema personalizzato più ramificato) con i dati da `SEQUENZA_DECISIONALE`.

**Struttura dello schema**:

Ogni livello è un blocco con:
- Titolo del passo (`①②③`) in grassetto, `--color-accent`
- Domanda in corsivo
- Due o tre rami condizionali (`se... allora...`), ognuno con:
  - Condizione in `--text-sm`, sfondo tenue
  - Esito: badge funzione + testo, oppure freccia verso il passo successivo

```
┌─────────────────────────────────────────┐
│  ① Leggi T e A nella CE                 │
│     "Il campo regge?"                   │
│                                         │
│  T0–T1 o A– ────────────── → [STA]      │
│  T1 + alto carico ─────────── → [PRO]   │
│  T2–T3 e A± ───────────────── → ②       │
└─────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  ② Leggi R e D nella CE                 │
│     "C'è una transizione già in corso?" │
│                                         │
│  R: ↑→~ e D↗ ──────────────── → [MED]  │
│  R assente o D→/↙ ──────────── → ③      │
└─────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  ③ Leggi N4 e N7                        │
│     "Il campo è stabile ma fermo?"      │
│                                         │
│  N4↓ o N7~ in T2 + D→ ─────── → [AMP]  │
│  N4 e N7 già sostenuti ────────── rivaluta│
└─────────────────────────────────────────┘
```

I badge funzione nello schema usano i colori `--color-fn-X`. Le frecce che portano a una funzione sono solide e colorate; le frecce che portano al passo successivo sono tratteggiate e grigie.

**Comportamento interattivo**: cliccando su uno dei badge funzione nello schema, si apre un pannello laterale compatto con i `segnali_CE` e `quando` corrispondenti (da `QUATTRO_FUNZIONI`). Questo evita di dover tornare alla slide precedente.

**Sezione inferiore — la nota sul giudizio**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Questa sequenza è un orientamento, non un algoritmo. Non sostituisce il giudizio professionale situato: lo struttura. Una CE può avere segnali misti o ambigui — in quei casi la sequenza aiuta a identificare quale segnale è più rilevante nel contesto specifico.*

*Se la sequenza non porta a una risposta chiara, il passo successivo è rivalutare la CE — non forzare una funzione.*

**Nota in footer**:
*Nel caso-guida, la sequenza porta direttamente a MEDIAZIONE: T2 (campo fragile ma aperto) → passo ②: R: N2→N3 e D↗ → Mediare.*

---

## SLIDE F3.4.6 — Il caso-guida: perché MEDIAZIONE

**Tipo**: `narrative`
**Titolo**: La scelta nel caso-guida
**Sottotitolo**: Applicare la sequenza decisionale al bilancio pediatrico

**Contenuto principale**:

Layout a due aree: sinistra la CE e la sequenza applicata, destra la funzione scelta con le sue implicazioni.

**Area sinistra** (45%) — "Applicare la sequenza":

`CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N2', 'N3', 'N4'], compact: false })`

Sotto la CE, tre passi della sequenza applicati — stile minimalista (testo, non lo schema completo):

*① T2 e A±: il campo regge. Non è T0–T1. Niente Stabilizzare come priorità immediata.*

*② R: N2→N3 · D↗: la transizione è già in corso. → MEDIARE.*

*③ Non necessario: la risposta è arrivata al passo ②.*

Chip risultato: badge `MED Mediare` grande, colore `var(--color-fn-mediare)`.

**Area destra** (55%) — "La funzione scelta e le sue implicazioni":

Titolo `--text-lg`, grassetto, colore `var(--color-fn-mediare)`: *"MEDIAZIONE"*

Tre sezioni:

**Cosa fa sul campo** (bordo sinistro `var(--color-fn-mediare)`):
*Coordina N2 (↑, risorsa attiva) e N3 (~, zona di movimento). Sostiene la transizione già avviata dalla relazione R: N2→N3. Non crea il movimento: lo accompagna.*

**Perché non Ampliare** (sfondo rosso tenuissimo, `--text-sm`):
N4↓ sconsiglia di aggiungere novità al campo. Ampliare su un campo con N4↓ aumenta il carico esplorativo in un nodo già in tensione.

**Perché non Stabilizzare** (sfondo rosso tenuissimo, `--text-sm`):
T2 e A± indicano che il campo regge. Stabilizzare un campo che non è in crisi produce stagnazione: si ridurrebbe la complessità di un campo che ha invece lo spazio per muoversi.

**Sezione inferiore** — la prospettiva verso M5:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*MEDIAZIONE è la funzione. Dice cosa deve fare il dispositivo: sostenere la transizione N2→N3 rallentando il ritmo adulto e lasciando spazio alla sequenza del bambino.*

*Non dice ancora come. Non nomina tecniche. Non prescrive sequenze precise.*

*Il dispositivo — le micro-azioni concrete — si costruisce nel Modulo 5.*

**Nota in footer**:
*La funzione MEDIAZIONE è coerente con il tipo universale U2+U4 (Sintonizzazione + Mediazione Simbolica). Il collegamento tra funzione e tipo universale verrà esplorato nel Modulo 6.*

---

## SLIDE F3.4.7 — La funzione apre lo spazio

**Tipo**: `standard`
**Titolo**: La funzione non è il dispositivo
**Sottotitolo**: Cosa rimane da fare dopo aver scelto la funzione

**Contenuto principale**:

Layout a colonna singola. Slide di chiusura concettuale — ariosa, con poco testo e molto respiro visivo.

**Sezione superiore — la distinzione**:

Due box affiancati, dimensione uguale, sfondo `--color-bg`, bordo `--color-border`:

**Box sinistra** — "La funzione":
*Definisce cosa il dispositivo deve fare al campo.*
*È una categoria: Stabilizzare / Ampliare / Mediare / Proteggere.*
*Nasce dalla CE e dal nodo dominante.*
*È la stessa indipendentemente da chi la esegue e in quale contesto.*

**Box destra** — "Il dispositivo":
*Definisce come la funzione si realizza in questo campo specifico.*
*È contestuale: cambia con il professionista, il bambino, il setting, il tempo disponibile.*
*Nasce dalla funzione — non dalla tecnica.*
*Ha le tre proprietà: breve, reversibile, osservabile.*

Freccia verso il basso sotto i due box con testo centrato:
*"La stessa funzione (MEDIARE) può diventare dispositivi molto diversi:"*

**Sezione centrale — tre dispositivi dalla stessa funzione**:

Tre chip affiancati, colore `var(--color-fn-mediare)` (bordo), sfondo molto tenue:

- `Dialogic Book Sharing` — *il genitore segue, nomina, aspetta*
- `Gioco imitativo` — *l'educatrice replica il gesto del bambino senza dirigere*
- `Routine di nomina condivisa` — *il pediatra rallenta e lascia spazio al bambino*

Sotto i tre chip, in `--text-sm`, `--color-text-muted`:
*Stessa funzione. Tre contesti. Tre dispositivi. Stessa grammatica.*

**Sezione inferiore — la proprietà emergente**:

Blockquote centrato, bordo sinistro `--color-f3`:

> *"Strumenti diversi possono nascere dalla stessa funzione.
> La stessa funzione può servire configurazioni diverse.
> Lo strumento non è una soluzione: è un regolatore di campo."*

**Chiusura** — testo centrato, spazio bianco sopra, `--text-lg`, corsivo:

*Nel prossimo modulo costruiamo il dispositivo: il Template F3, le micro-azioni, l'output-tipo, la verifica di coerenza.*

Badge modulo successivo: `→ Modulo 5 — Il micro-dispositivo`

---

## Note per l'implementazione

### Slide F3.4.2 — Chip indice rapido

I quattro chip cliccabili sopra le card (`[● STA Stabilizzare]` ecc.) non richiedono logica complessa: ogni chip chiama `expandCard(index)` dove index è la posizione della card nell'array. Lo stato attivo del chip (background leggermente più scuro, bordo più spesso) riflette la card aperta in quel momento.

### Slide F3.4.3 — Tabella chip segnali CE

I segnali CE nella colonna 1 della tabella sono chip piccoli (`--text-xs`, padding ridotto) con colore semantico: ↑ verde, ↓ rosso, ~ arancione, poi chip neutri per T/A/D/R con sfondo `--color-bg` e bordo `--color-border`. Su righe molto dense, impilare i chip in colonna invece che in riga.

### Slide F3.4.5 — Schema ramificato

Lo schema non usa `PipelineAnimator` (lineare) ma un layout custom a tre livelli con rami. Implementazione suggerita: `<div class="decision-tree">` con `<div class="decision-node">` per ogni livello e `<div class="decision-branch">` per ogni ramo condizionale. Le frecce sono bordi CSS (`border-left` + `border-bottom` con `border-radius`) — più semplici di SVG per una struttura ad albero discendente. I rami che portano a una funzione usano `border-color: var(--color-fn-X)`; quelli che portano al livello successivo usano `border-color: var(--color-border)` tratteggiato.

### Slide F3.4.6 — Layout a due aree

Stesso layout a due aree della slide F3.3.5 (M3). Riutilizzare la classe CSS `.slide__two-col` già definita. L'unica differenza è la proporzione: qui 45/55 invece di 38/62. Aggiungere una variante `.slide__two-col--balanced` con proporzione definita come variabile CSS.

### Colori delle quattro funzioni

Tutti i colori `--color-fn-X` sono già definiti in `style.css` come variabili globali (dalla `ISTRUZIONI_CLAUDE_CODE_F3.md`). Nessuna ridefinizione locale nel file di modulo. Usare sempre le variabili, non i codici esadecimali diretti, per garantire coerenza nei moduli successivi (M5, M6, M7, M8) che citano le funzioni.
