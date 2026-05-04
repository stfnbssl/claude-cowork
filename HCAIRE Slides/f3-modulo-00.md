# f3-modulo-00 — Orientamento F3
**Numero slide**: 5
**Colore accent**: `#2d9cdb`
**Tipo prevalente**: narrative + diagram

---

## Nota sull'architettura del corso F3

Questo è il primo file di specifica per il **corso F3 — Strumenti Operativi Contestualizzati**. Il corso è strutturato in **9 moduli (M0–M8)**, per un totale di circa 60 slide. È un'applicazione separata da F1 e F2, con la stessa architettura tecnica descritta in `ISTRUZIONI_CLAUDE_CODE.md`.

### Mappa dei moduli e colori accent

| Modulo | Titolo | Slide | Colore accent |
|--------|--------|-------|---------------|
| M0 | Orientamento F3 | 5 | `#2d9cdb` |
| M1 | Il principio del campo | 6 | `#1e8bc3` |
| M2 | Dalla CE allo strumento | 7 | `#0e8f7f` |
| M3 | Il nodo dominante | 6 | `#e67e22` |
| M4 | Le quattro funzioni | 7 | `#3498db` |
| M5 | Il micro-dispositivo | 8 | `#2d6a4f` |
| M6 | La tipologia U1–U6 | 8 | `#16a085` |
| M7 | Logica decisionale | 7 | `#c0392b` |
| M8 | Pipeline F3 completa | 7 | `#1a6b8a` |

---

## Estensione di `window.CASO_GUIDA`

In `app.js` del corso F3, aggiungere all'oggetto `window.CASO_GUIDA` la sezione `f3`. Questa sezione contiene tutti i dati prodotti dall'applicazione della F3 al caso-guida e viene usata progressivamente da M2 in poi.

```javascript
window.CASO_GUIDA.f3 = {
  nodoDominante: {
    codice: 'N3',
    nome: 'Accesso al mondo condiviso simbolico',
    colore: '#2980b9',
    motivazione: 'N3 è il nodo la cui apertura muove il campo nella direzione evolutiva indicata (D↗). Non è il nodo più basso numericamente (N4↓), ma è quello la cui attivazione produce il cambiamento più rilevante per l\'abitabilità complessiva.'
  },
  nodoSostegno: {
    codice: 'N2',
    nome: 'Campo relazionale / Co-regolazione',
    colore: '#27ae60',
    ruolo: 'N2 è sostenuto (↑) e costituisce la risorsa su cui si appoggia l\'intervento: senza co-regolazione attiva, l\'accesso al mondo condiviso non si produce.'
  },
  nodoInTensione: {
    codice: 'N4',
    nome: 'Apertura / Esplorazione del mondo',
    colore: '#8e44ad',
    nota: 'N4↓ è il nodo limitante secondario. Non è il target dell\'intervento in questo contesto, ma va tenuto presente: un dispositivo che sovraccarica il campo riduce ulteriormente l\'esplorabilità.'
  },
  funzione: 'MEDIAZIONE',
  funzioneDescrizione: 'Coordinare N2 (attivo) e N3 (neutro), stabilizzando le condizioni che rendono possibile l\'accesso al mondo condiviso simbolico. Non stabilizzare (il campo non è in collasso), non ampliare (sarebbe prematuro con N4↓), ma mediare la transizione già in corso.',
  campoBersaglio: 'Stabilità e durata dello scambio condiviso simbolico',
  microAzioni: [
    'Il genitore segue l\'interesse del bambino senza anticiparlo né dirigerlo',
    'Nomina ciò che il bambino indica, con voce calma e ritmo lento',
    'Attende la risposta del bambino senza riempire il silenzio',
    'Espande senza correggere ("Sì, il cane — e guarda qui...")',
    'Il pediatra osserva senza interrompere la sequenza bambino-genitore'
  ],
  tempoReale: '5 minuti durante il bilancio pediatrico',
  indicatoreRisonanza: 'Il bambino include l\'adulto nella sequenza con sguardo condiviso, gesto e vocalizzazione integrati. La sequenza si allunga: non termina al primo giro.',
  tipoUniversale: ['U2', 'U4'],
  tipoUniversaleNome: 'Sintonizzazione (U2) + Mediazione Simbolica (U4)',
  outputTipo: {
    A: 'Il bambino orienta il libro verso l\'adulto: il mondo appare condiviso ma discontinuo. L\'alternanza di sguardo è presente; la sequenza di scambio si interrompe e non sempre riprende autonomamente.',
    B: 'Emergenza di posizione riconoscibile: il bambino indica, vocalizza, cerca la risposta dell\'adulto. La permanenza nel legame è presente ma non ancora stabile — dipende dalla qualità della risposta adulta.',
    C: 'Limite tollerato: la condivisione si interrompe e può riprendere. Non collassa. La "fine" della sequenza non produce disorganizzazione.',
    D: 'In questa situazione il campo appare strutturato prevalentemente come accesso intermittente al mondo condiviso simbolico, con campo relazionale attivo come sostegno e apertura esplorativa ridotta.',
    E: 'Rafforzare la stabilità del campo condiviso sostenendo la sequenza del bambino senza anticiparne i gesti. Non ampliare (sovraccarico), non correggere, ma rendere lo scambio più duraturo.'
  }
};
```

---

## Dati globali del modulo

Definire in `m00.js` le seguenti costanti. Sono la sorgente di dati per le slide del Modulo 0.

```javascript
const TRE_RESPONSABILITA = [
  {
    id: 'f2',
    livello: 'F2 — Metodo',
    funzione: 'Rende leggibile',
    descrizione: 'Produce la Configurazione Evolutiva: una descrizione strutturale del campo bambino-adulto-contesto. Non interviene, non decide, non prescrive.',
    output: 'Configurazione Evolutiva (CE)',
    colore: 'var(--color-f2)'
  },
  {
    id: 'f3',
    livello: 'F3 — Professionista guidato dal metodo',
    funzione: 'Valuta e orienta',
    descrizione: 'Identifica il nodo dominante, sceglie la funzione dell\'azione, costruisce il micro-dispositivo contestualizzato. La responsabilità operativa è sua.',
    output: 'Micro-dispositivo di campo',
    colore: 'var(--color-f3)'
  },
  {
    id: 'disciplina',
    livello: 'Disciplina',
    funzione: 'Decide',
    descrizione: 'Assume la responsabilità professionale della scelta finale. Il metodo orienta la decisione — non si sostituisce ad essa.',
    output: 'Decisione disciplinare',
    colore: 'var(--color-primary)'
  }
];

const F3_PRODUCE = [
  'Micro-dispositivi di campo contestualizzati',
  'Identificazione della funzione dell\'intervento (stabilizzare / ampliare / mediare / proteggere)',
  'Template F3 compilabili',
  'Output-tipo vuoto',
  'Logica decisionale non prescrittiva'
];

const F3_NON_PRODUCE = [
  'Diagnosi',
  'Protocolli d\'intervento standardizzati',
  'Prescrizioni terapeutiche o educative',
  'Raccomandazioni universali',
  'Trattamenti o piani d\'azione prefissati'
];

const PIANO_CORSO_F3 = [
  { id: 'm0', titolo: 'Orientamento F3', slide: 5, colore: '#2d9cdb' },
  { id: 'm1', titolo: 'Il principio del campo', slide: 6, colore: '#1e8bc3' },
  { id: 'm2', titolo: 'Dalla CE allo strumento', slide: 7, colore: '#0e8f7f' },
  { id: 'm3', titolo: 'Il nodo dominante', slide: 6, colore: '#e67e22' },
  { id: 'm4', titolo: 'Le quattro funzioni', slide: 7, colore: '#3498db' },
  { id: 'm5', titolo: 'Il micro-dispositivo', slide: 8, colore: '#2d6a4f' },
  { id: 'm6', titolo: 'La tipologia U1–U6', slide: 8, colore: '#16a085' },
  { id: 'm7', titolo: 'Logica decisionale', slide: 7, colore: '#c0392b' },
  { id: 'm8', titolo: 'Pipeline F3 completa', slide: 7, colore: '#1a6b8a' }
];
```

---

## SLIDE F3.0.1 — Il passaggio

**Tipo**: `narrative`
**Titolo**: Da qui si agisce
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Layout a colonna singola centrata. Testo narrativo con abbondante spazio bianco. Font principale `--text-2xl`.

**Sezione superiore — la situazione**:

Card narrativa (sfondo `--color-primary-light`, bordo sinistro `--color-f2`):

*Alla fine della Fase 2, il professionista ha in mano una Configurazione Evolutiva.*
*Sa leggere la situazione. Sa descrivere il campo. Sa quali nodi sono attivi, quali in tensione.*

*Adesso cosa fa?*

**Divisore sottile** (linea orizzontale `--color-border`)

**Sezione centrale — il confine**:

Testo normale, `--text-lg`, centrato:

La Fase 2 ha fatto il suo lavoro: ha trasformato un'osservazione in una descrizione strutturata del campo evolutivo. Ha prodotto leggibilità senza produrre azione.

La **Fase 3** inizia esattamente qui: nel momento in cui la leggibilità deve orientare qualcosa di reale.

**Sezione inferiore — tre domande** (tre chip/tag affiancati, stile interrogativo, sfondo molto tenue):

- `Quale nodo è dominante in questo campo?`
- `Quale funzione può aumentare l'abitabilità?`
- `Quale dispositivo è coerente con questa configurazione?`

Sotto i chip, in testo secondario (`--color-text-muted`, `--text-base`):
*Questo corso risponde a queste tre domande — sul caso-guida che abbiamo già incontrato.*

**Nota in footer**:
*F3 non ricomincia da zero: riceve da F2 e trasforma. Il prerequisito è aver lavorato la Configurazione Evolutiva.*

---

## SLIDE F3.0.2 — Siamo in Fase 3

**Tipo**: `diagram`
**Titolo**: L'architettura del metodo: siamo qui
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Stesso diagramma verticale interattivo a tre blocchi del Modulo 0 di F2 (F1→F2→F3 collegati da frecce), ma adesso il blocco attivo è **F3** — bordo più spesso, opacity piena, colore `--color-f3`. F1 e F2 hanno opacity ridotta (80%), a indicare che sono prerequisiti completati.

```
┌─────────────────────────────┐
│  F1 — Fondazione ontologica │  ← --color-f1, opacity 0.7, "completata"
│  "Cosa è lo sviluppo"       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  F2 — Traduzione            │  ← --color-f2, opacity 0.7, "completata"
│  Interdisciplinare          │
│  "Come si rende leggibile"  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  F3 — Strumenti operativi   │  ← --color-f3, bordo spesso, "siamo qui"
│  contestualizzati           │
│  "Come si agisce"           │
└─────────────────────────────┘
```

**Pannello espanso cliccando F1** (appare a destra):
- Titolo: "Fase 1 — Fondazione ontologica ✓"
- Funzione: Stabilisce che tipo di realtà è lo sviluppo infantile e che tipo di soggetto è il bambino.
- Output verso F2: I sei assi strutturali come condizioni di possibilità.
- Stato: *Prerequisito. Costituisce i vincoli che impediscono le riduzioni lungo tutto il metodo.*

**Pannello espanso cliccando F2**:
- Titolo: "Fase 2 — Traduzione Interdisciplinare ✓"
- Funzione: Ha reso lo sviluppo leggibile nei contesti professionali — senza perderlo.
- Output verso F3: La Configurazione Evolutiva (CE): struttura del campo, nodi, direzione, abitabilità.
- Stato: *Prerequisito. La CE prodotta in F2 è l'input di F3.*

**Pannello espanso cliccando F3** (default aperto all'entrata nella slide):
- Titolo: "Fase 3 — Strumenti operativi contestualizzati ← *Siamo qui*"
- Funzione: Trasforma la leggibilità in micro-azioni coerenti. Non produce protocolli, diagnosi o prescrizioni: orienta il professionista verso un'azione minima e situata.
- Input: la CE prodotta dalla F2.
- Output: micro-dispositivi di campo, template F3, logica decisionale.
- Vincolo fondamentale: *la decisione disciplinare resta fuori dal metodo.*

**Riga in basso** — tre parole in grassetto con frecce:
`DEFINISCE` → `RENDE LEGGIBILE` → `RENDE POSSIBILE L'AZIONE`

---

## SLIDE F3.0.3 — Le tre responsabilità

**Tipo**: `standard`
**Titolo**: Chi fa cosa
**Sottotitolo**: Una distinzione strutturalmente necessaria

**Contenuto principale**:

Layout a colonna singola. La slide costruisce progressivamente la tavola delle responsabilità.

**Sezione superiore — il problema**:

Testo introduttivo (`--text-lg`):

Trasformare la leggibilità in azione solleva una domanda che il metodo deve rispondere esplicitamente:

*Chi decide cosa fare?*

Se risponde il metodo → tecnocrazia: il professionista esegue una procedura.
Se risponde solo la disciplina → arbitrarietà: la lettura configurazionale non serve a nulla.

Il metodo propone una **terza via**: la responsabilità è distribuita su tre livelli distinti, ciascuno con una funzione specifica.

**Sezione centrale — la tavola** (usa dati da `TRE_RESPONSABILITA`):

Tre card verticali affiancate (larghezza uguale, altezza uniforme), senza interattività. Ogni card ha:
- Colore del livello come bordo superiore spesso (4px)
- Livello (`livello`) in grassetto, `--text-sm`, `--color-text-secondary`
- Funzione (`funzione`) in `--text-2xl`, grassetto — la parola chiave grande
- Descrizione (`descrizione`) in testo normale
- Output (`output`) in piccolo, in corsivo, sfondo tenue: *"Output: …"*

Ordine visivo: F2 (sinistra) → F3 (centro, leggermente più alta di 4px per indicare il focus) → Disciplina (destra).

**Sezione inferiore — la regola fondamentale**:

Blockquote stilizzato (bordo sinistro `--color-f3`, sfondo `--color-primary-light`):

> *"Il metodo non decide. Orienta la decisione."*

Sotto il blockquote, in testo normale:
La responsabilità disciplinare — che si tratti del pediatra, dell'educatore o dello psicologo — non viene assorbita dal metodo. F3 produce gli strumenti per decidere bene; la decisione finale è e rimane professionale.

**Nota in footer**:
*Questa distinzione non è formale: è la garanzia che F3 non diventi un protocollo prescrittivo.*

---

## SLIDE F3.0.4 — Cosa F3 produce (e non produce)

**Tipo**: `standard`
**Titolo**: Cosa produce la Fase 3
**Sottotitolo**: E cosa rimane fuori

**Contenuto principale**:

Layout a due sezioni verticali separate da divisore sottile — stesso schema della Slide 0.4 del corso F2, applicato a F3.

**Sezione superiore — la funzione in una frase**:

Blockquote centrato (bordo sinistro `--color-f3`):

> *"Trasformare la leggibilità configurazionale in micro-azioni coerenti senza produrre protocolli, diagnosi o prescrizioni."*

**Sezione inferiore — due box affiancati** (usa dati da `F3_PRODUCE` e `F3_NON_PRODUCE`):

**Box verde** (sfondo `--color-valid` molto chiaro, bordo verde, `--color-valid`):
**✓ F3 produce**
Lista degli elementi da `F3_PRODUCE`, con bullet sottili.

**Box rosso** (sfondo `--color-invalid` molto chiaro, bordo rosso, `--color-invalid`):
**✗ F3 non produce**
Lista degli elementi da `F3_NON_PRODUCE`, con bullet sottili.

**Elemento aggiuntivo** — sotto i due box, centrato, in testo enfatizzato (`--text-lg`, corsivo):

*F3 modifica il campo relazionale di esperienza. Non corregge il bambino.*

Questa frase è il principio operativo fondamentale della Fase 3 e tornerà in forma esplicita nel Modulo 1.

**Guardrail** (componente `GuardrailBadge`, in fondo alla slide):
- Codice: `C-F3`
- Label: Vincolo fondamentale
- Testo: *Se uno strumento prodotto in F3 richiede diagnosi, attribuisce tratti stabili al bambino, o prescrive sequenze obbligate di azioni, non è coerente con il metodo.*

---

## SLIDE F3.0.5 — Il caso-guida: da dove partiamo

**Tipo**: `narrative`
**Titolo**: Il caso-guida in mano
**Sottotitolo**: La CE che abbiamo prodotto in F2

**Contenuto principale**:

Layout a colonna singola, narrativo. Questa slide mostra il punto di partenza concreto del corso: la CE già prodotta dalla F2 applicata al caso-guida della lettura condivisa.

**Sezione superiore — richiamo della scena** (card narrativa, sfondo `--color-primary-light`, bordo sinistro `--color-primary`, testo da `window.CASO_GUIDA.scena`):

*Durante un bilancio di salute, il pediatra propone per alcuni minuti una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi. È presente un genitore. Sul tavolo c'è un piccolo libro illustrato con immagini semplici…*

*(testo completo da `window.CASO_GUIDA.scena` — non duplicare nel modulo)*

**Sezione centrale — la CE prodotta in F2**:

Titolo in `--text-lg`, grassetto: *La Configurazione Evolutiva — output della F2*

Tabella compatta a tre colonne: `Nodo` | `Stato` | `Lettura*`

| Nodo | Stato | Lettura |
|------|-------|---------|
| N1 — Regolazione | `~` neutro | Il campo non collassa, non è particolarmente stabile |
| N2 — Campo relazionale | `↑` sostenuto | Il genitore co-regola attivamente — risorsa principale |
| N3 — Mondo condiviso | `~` neutro | L'accesso al simbolico è presente ma discontinuo |
| N4 — Apertura/Esplorazione | `↓` limitante | L'esplorazione autonoma è ridotta nel contesto del bilancio |
| N5 — Limite | `~` neutro | Il limite non è un tema dominante nella scena |
| N6 — Continuità | `~` neutro | La sequenza si interrompe e riprende — sufficiente |
| N7 — Desiderio | `~` neutro | L'iniziativa è presente ma non direzionata |

Righe di riepilogo sotto la tabella (non in tabella, ma in testo):
- **Relazione dominante**: N2 → N3 (MED) — il campo relazionale sostiene l'accesso al mondo condiviso
- **Direzione evolutiva**: ↗ espansione in corso
- **Tenuta**: T2 — configurazione fragile ma evolutivamente aperta
- **Abitabilità**: A± — moderata

Nota asterisco in piccolo: *\*Le letture riportate qui sono sintesi. Il Modulo 2 mostrerà come si legge una CE in chiave F3.*

**Sezione inferiore — il percorso del corso** (barra orizzontale di progress, stile tag):

Testo introduttivo (`--text-base`):
*In questo corso, questa CE diventa il materiale di lavoro di ogni modulo:*

Sequenza orizzontale di chip con frecce, colori dei moduli corrispondenti:

`M2 Lettura per l'azione` → `M3 Nodo dominante` → `M4 Funzione` → `M5 Dispositivo` → `M6 Tipologia` → `M7 Decisione` → `M8 Pipeline completa`

Sotto i chip, in testo muto:
*Il caso-guida resta invariante. Ogni modulo aggiunge un pezzo.*

**Chiusura** — testo centrato, `--text-lg`, corsivo, con spazio bianco sopra:

*La CE è in mano. Il corso inizia da qui.*

Badge modulo successivo: `→ Modulo 1 — Il principio del campo`

---

## Note per l'implementazione

### All'entrata nel Modulo 0

Mostrare una breve transizione di benvenuto identica a quella del M0 di F2: fade-in del titolo del modulo (400ms). Il testo del benvenuto è:

*"Fase 3 — Strumenti Operativi Contestualizzati"*

### Slide F3.0.2 — Pannello default

Il pannello F3 deve essere già aperto al caricamento della slide, come il pannello F2 nel M0 del corso F2. I pannelli F1 e F2 si aprono al clic.

### Slide F3.0.3 — Card responsabilità

Le tre card non sono interattive (nessun hover/click che le modifica). Hanno solo uno stato hover leggero (box-shadow aumenta di intensità). Il focus visivo sul livello F3 (card centrale leggermente rialzata) serve a comunicare che questo è il livello su cui il corso si concentra.

### Slide F3.0.5 — Tabella CE

La tabella della CE usa le stesse variabili di colore dei Nodi definite nel design system (`--color-n1`, `--color-n2`, …`--color-n7`) per colorare le celle della colonna "Nodo". Gli stati (↑ ↓ ~) usano colori semantici: ↑ → `--color-valid`, ↓ → `--color-invalid`, ~ → `--color-text-muted`.

La riga di N2 (↑ sostenuto) e la riga di N4 (↓ limitante) hanno uno sfondo leggermente evidenziato nelle rispettive colonne colore, per far risaltare visivamente i due nodi non neutri.

### Slide F3.0.5 — Chip del percorso

I chip del percorso del corso nella sezione inferiore sono cliccabili (non naviga, ma mostra una tooltip con il titolo completo del modulo e il numero di slide). Non devono portare fuori dalla slide.

### `window.CASO_GUIDA.f3`

Il blocco `window.CASO_GUIDA.f3` definito nella sezione "Estensione di `window.CASO_GUIDA`" qui sopra deve essere aggiunto in `app.js` **prima** del caricamento di qualsiasi modulo. A differenza del corso F2 — dove il caso-guida veniva costruito progressivamente — in F3 l'oggetto è già completo fin dall'inizio: viene svelato ai partecipanti gradualmente attraverso il corso, ma il dato è disponibile per tutti i moduli dall'avvio.

### Colori accent per tutti i moduli

I `--module-accent` per i 9 moduli F3 sono definiti nella tabella della sezione "Nota sull'architettura del corso F3" all'inizio di questo file. In `app.js`, registrare i moduli F3 con questi colori nell'array `MODULES` (come avviene per F2).
