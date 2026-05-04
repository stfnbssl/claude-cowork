# ISTRUZIONI PER CLAUDE CODE
## Corso: Fase 3 — Strumenti Operativi Contestualizzati
## Progetto: HCAIRE — Applicazione formativa HTML/CSS/JS

---

## 1. Contesto del progetto

Stai costruendo un'applicazione web formativa single-page per un corso destinato a **professionisti della prima infanzia** (pediatri, educatori, psicologi, coordinatori di servizi). Il corso illustra la **Fase 3 — Strumenti Operativi Contestualizzati** di un metodo per la lettura dello sviluppo infantile.

Esistono già due corsi analoghi per le fasi precedenti: F1 (Fondazione Ontologica) e F2 (Traduzione Interdisciplinare). Questa applicazione segue la stessa architettura tecnica di quei corsi, nella propria cartella autonoma. **Le tre applicazioni sono indipendenti**: non condividono JS né HTML, ma condividono le convenzioni di design system descritte di seguito.

Il piano completo del corso comprende **9 moduli (M0–M8), ~60 slide totali**. Tu lavori **un modulo alla volta**. Ogni modulo viene definito da un file di contenuto (`f3-modulo-XX.md`) che trovi nella stessa cartella di questo file. Le istruzioni architetturali qui sotto valgono per l'intera applicazione.

**Prerequisito implicito del corso**: F3 riceve i suoi input dalla F2. Al momento dell'ingresso nel corso, il partecipante ha già prodotto (o visto produrre) una Configurazione Evolutiva (CE) sul caso-guida. Il corso F3 prende in consegna quella CE e la trasforma in un micro-dispositivo di campo contestualizzato.

**Filo rosso del corso**: il caso-guida è la stessa scena delle fasi precedenti — una situazione di *lettura condivisa adulto-bambino* durante un bilancio pediatrico — ma stavolta viene lavorata in chiave operativa. A differenza di F2 (che costruisce la CE progressivamente) e di F1 (che rilumina la scena asse per asse), in F3 **la CE è già in mano** all'inizio del corso. Il percorso porta dalla CE prodotta al micro-dispositivo contestualizzato: nodo dominante → funzione → template → tipo universale → logica decisionale → pipeline completa.

**Principio operativo fondamentale**: lo strumento F3 non corregge il bambino. Modifica il campo relazionale di esperienza. Questo principio non è etico ma metodologico: emerge direttamente dall'Asse 1 (il bambino è soggetto incarnato, temporale e relazionale — non si interviene sul soggetto isolato). Deve riflettersi nel design di ogni slide.

---

## 2. Struttura dei file

```
F3/
├── index.html               ← shell principale, navigation, router
├── css/
│   └── style.css            ← design system completo
├── js/
│   ├── app.js               ← logica di navigazione, stato globale, window.CASO_GUIDA_F3
│   └── modules/
│       ├── m00.js           ← Modulo 0: dati + interattività
│       ├── m01.js           ← Modulo 1: dati + interattività
│       ├── m02.js           ← Modulo 2: dati + interattività
│       └── ...              ← fino a m08.js
└── ISTRUZIONI_CLAUDE_CODE_F3.md
```

La cartella `F3/` è una directory autonoma, separata da quelle di F1 e F2. Crea e lavora sempre all'interno di `F3/`.

### Responsabilità di ogni file

**`index.html`**: struttura DOM fissa (sidebar, area slide, controlli), carica tutti i moduli JS, non contiene contenuto delle slide.

**`style.css`**: design system completo. Non usare stili inline nelle slide — ogni variazione va come classe CSS o variabile CSS.

**`app.js`**: gestisce stato globale (modulo corrente, slide corrente), router, keybindings (frecce), animazioni di transizione tra slide, e definisce `window.CASO_GUIDA_F3` (oggetto completo descritto nella §7).

**`js/modules/mXX.js`**: esporta un oggetto `ModuleXX` con:
- `id`, `title`, `color` (colore accent del modulo)
- `slides`: array di oggetti slide
- `init()`: funzione chiamata quando il modulo viene caricato per la prima volta
- `onSlide(index)`: funzione chiamata ogni volta che si entra in una slide (per attivare animazioni o reset)

---

## 3. Design system

### 3.1 Palette colori

```css
:root {
  /* Base */
  --color-bg: #f5f6f8;
  --color-surface: #ffffff;
  --color-text: #1e2a3a;
  --color-text-secondary: #4a5568;
  --color-text-muted: #718096;
  --color-border: #e2e8f0;

  /* Brand primario */
  --color-primary: #1a6b8a;
  --color-primary-dark: #124f67;
  --color-primary-light: #e8f4f8;

  /* Accenti modulo (cambiano per modulo) */
  --color-accent: var(--module-accent, #2d9cdb);

  /* Colori per i Nodi Trasversali */
  --color-n1: #e67e22;   /* N1 Regolazione */
  --color-n2: #27ae60;   /* N2 Campo relazionale */
  --color-n3: #2980b9;   /* N3 Mondo condiviso */
  --color-n4: #8e44ad;   /* N4 Apertura */
  --color-n5: #e74c3c;   /* N5 Limite reale */
  --color-n6: #1abc9c;   /* N6 Continuità */
  --color-n7: #f39c12;   /* N7 Desiderio */

  /* Colori per le Funzioni F3 */
  --color-fn-stabilizzare: #2980b9;   /* Stabilizzare */
  --color-fn-ampliare:     #27ae60;   /* Ampliare */
  --color-fn-mediare:      #8e44ad;   /* Mediare */
  --color-fn-proteggere:   #e67e22;   /* Proteggere */

  /* Colori per i Tipi Universali U1–U6 */
  --color-u1: #2980b9;   /* U1 Regolazione */
  --color-u2: #27ae60;   /* U2 Sintonizzazione */
  --color-u3: #8e44ad;   /* U3 Apertura */
  --color-u4: #1abc9c;   /* U4 Mediazione Simbolica */
  --color-u5: #e74c3c;   /* U5 Limite Generativo */
  --color-u6: #f39c12;   /* U6 Riattivazione del Desiderio */

  /* Colori per i Controlli (guard-rail) */
  --color-guardrail: #2d6a4f;
  --color-guardrail-bg: #d8f3dc;

  /* Fasi */
  --color-f1: #6c63ff;
  --color-f2: #1a6b8a;
  --color-f3: #2d9cdb;

  /* Feedback */
  --color-valid: #27ae60;
  --color-invalid: #e74c3c;
  --color-warning: #f39c12;
}
```

**Nota sui colori delle Funzioni**: Le quattro funzioni (Stabilizzare, Ampliare, Mediare, Proteggere) hanno ognuna un colore semantico stabile. Questi colori devono essere usati coerentemente in tutti i moduli che citano le funzioni: M4, M5, M7, M8. La funzione del caso-guida è MEDIAZIONE → `--color-fn-mediare: #8e44ad`.

**Nota sui colori dei Tipi Universali**: I sei tipi U1–U6 hanno ognuno un colore stabile. Usare coerentemente in M6, M8 e nelle slide che citano i tipi.

### 3.2 Colori accent per modulo

Ogni modulo ha un `--module-accent` che colora la barra superiore, i badge e le evidenziazioni:

| Modulo | Titolo | Colore accent |
|--------|--------|--------------|
| M0 — Orientamento F3 | Da dove si agisce | `#2d9cdb` |
| M1 — Il principio del campo | Lo strumento modifica il campo | `#1e8bc3` |
| M2 — Dalla CE allo strumento | La pipeline di trasformazione | `#0e8f7f` |
| M3 — Il nodo dominante | Come si legge la CE per l'azione | `#e67e22` |
| M4 — Le quattro funzioni | Stabilizzare / Ampliare / Mediare / Proteggere | `#3498db` |
| M5 — Il micro-dispositivo | Template F3 e output-tipo | `#2d6a4f` |
| M6 — La tipologia U1–U6 | Le sei forme universali | `#16a085` |
| M7 — Logica decisionale | Chi sceglie cosa fare | `#c0392b` |
| M8 — Pipeline F3 completa | Il caso-guida dall'osservazione al dispositivo | `#1a6b8a` |

### 3.3 Tipografia

```css
--font-display: 'Inter', system-ui, sans-serif;
--font-body: 'Inter', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;

--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 1.875rem;
--text-4xl: 2.25rem;

--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.7;
```

Carica Inter da Google Fonts nell'`<head>`.

### 3.4 Spaziatura

Usa multipli di 4px: `--space-1: 4px`, `--space-2: 8px`, ..., `--space-16: 64px`.

### 3.5 Ombre e bordi

```css
--shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
--shadow-md: 0 4px 12px rgba(0,0,0,0.10);
--shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
--radius-sm: 6px;
--radius-md: 10px;
--radius-lg: 16px;
```

---

## 4. Layout dell'applicazione

```
┌─────────────────────────────────────────────────────────────┐
│  TOPBAR: logo + titolo modulo corrente + progress dots      │
├───────────────┬─────────────────────────────────────────────┤
│               │                                             │
│  SIDEBAR      │   AREA SLIDE                                │
│  (moduli)     │   (contenuto della slide corrente)          │
│               │                                             │
│  · M0 ●       │                                             │
│  · M1         │                                             │
│  · M2         │                                             │
│    ...        │                                             │
│  · M8         │                                             │
│               │                                             │
├───────────────┴────────┬──────────────────────┬─────────────┤
│  [← SLIDE PRECEDENTE]  │  ●●●○○○○○ (dots)    │  [PROSSIMA →]│
└────────────────────────┴──────────────────────┴─────────────┘
```

### Sidebar

- Larghezza: 240px, collassabile su schermi piccoli
- Lista moduli: numero + titolo abbreviato + indicatore progresso
- Il modulo attivo è evidenziato con `--module-accent`
- I moduli non ancora raggiunti sono leggermente opachi (non bloccati, solo visivamente non attivi)
- Badge piccolo `F3` nella topbar, colorato in `--color-f3`, per distinguere visivamente questa applicazione da F1 e F2

### Area slide

- Occupa il resto della larghezza disponibile
- Ogni slide è un `<section class="slide">` con layout flessibile
- Le slide hanno un'area principale (contenuto) e opzionalmente un footer con nota o guardrail
- Transizione tra slide: slide-fade (200ms opacity + 8px translate-y)

### Controlli

- Frecce ← → sempre visibili; la freccia sinistra è disabilitata alla prima slide del primo modulo
- I dot indicators mostrano la posizione nella slide corrente (non nel modulo)
- Shortcut tastiera: ← → per navigare, numero 0-8 per saltare a un modulo

---

## 5. Struttura di una slide

Ogni slide è un oggetto JS con questa struttura:

```javascript
{
  id: 'slide-id',                    // stringa unica nel formato 'f3-mXX-YY'
  type: 'standard' | 'diagram' | 'interactive' | 'comparison' | 'narrative',
  title: 'Titolo della slide',
  subtitle: 'Sottotitolo opzionale',
  content: '...',                    // HTML o funzione che ritorna HTML
  notes: 'Nota per il relatore',     // opzionale, mostrata in footer discreto
  guardrail: {                       // opzionale, mostrato se presente
    code: 'C-F3',
    label: 'Vincolo metodologico F3',
    text: 'Se lo strumento chiude possibilità evolutive anziché aprirle, è fuori modello.'
  },
  onEnter: function() { ... },       // opzionale, chiamata all'entrata nella slide
  onLeave: function() { ... },       // opzionale, chiamata all'uscita
}
```

**Convenzione per gli id**: usare il formato `f3-m00-01` (fase-modulo-slide). Questo evita collisioni se le applicazioni dovessero mai condividere un namespace comune.

### Tipi di slide

**`standard`**: testo, titolo, eventuale elemento visivo. Layout colonna singola o due colonne.

**`diagram`**: elemento visivo dominante (schema, pipeline, grafo). Il testo è secondario o in tooltip.

**`interactive`**: contiene un componente interattivo (card espandibili, F3Builder, DecisionCycle, matrice). L'area principale è occupata dal componente.

**`comparison`**: due colonne affiancate. In F3 usata soprattutto per: azione sul comportamento / modifica del campo; scelta per tecnica / scelta per funzione; strumento valido / strumento fuori modello.

**`narrative`**: testo narrativo più lungo, layout tipografico. Usata per il caso-guida, le slide di apertura dei moduli, le slide di chiusura capstone.

---

## 6. Componenti interattivi riutilizzabili

Questi componenti devono essere definiti in `js/app.js` come funzioni/classi e riutilizzati da tutti i moduli.

I componenti §6.1–§6.4 sono identici a quelli già definiti per F2 (e adattati in F1): riutilizza le stesse implementazioni. I componenti §6.5 e §6.6 sono **nuovi specifici di F3**.

### 6.1 `ExpandableCards(data, container, options)`

Crea un set di card espandibili.

```javascript
// data: array di oggetti
[{
  id: 'fn-mediare',
  color: '#8e44ad',        // colore accent della card
  badge: 'MED',            // etichetta breve
  title: 'Mediare',
  summary: 'Coordinare nodi in tensione tra loro...',
  detail: '<p>Nodi tipici: N2→N3, N1↔N4</p><p>Domanda guida: ...</p>'
}]

// options
{
  multiOpen: false,        // default: false — una sola card aperta alla volta
  defaultOpen: null        // indice della card aperta al caricamento (opzionale)
}
```

Usato in: M4 (quattro funzioni), M6 (sei tipi universali U1–U6).

### 6.2 `ComparisonPanel(left, right, container, footer)`

Due colonne affiancate.

```javascript
{
  left: {
    label: 'Azione sul comportamento',
    color: '#e74c3c',
    title: 'Correggere il bambino',
    content: 'HTML...'
  },
  right: {
    label: 'Modifica del campo',
    color: '#2d9cdb',
    title: 'Modificare le condizioni relazionali',
    content: 'HTML...'
  },
  footer: {                       // opzionale, a piena larghezza sotto le colonne
    label: 'Principio operativo',
    content: 'HTML...',
    color: '#2d9cdb'
  }
}
```

Usato in: M1 (campo vs. comportamento), M2 (leggere per l'azione vs. per la descrizione), M5 (strumento valido vs. fuori modello).

### 6.3 `PipelineAnimator(steps, container)`

Visualizza la pipeline come sequenza verticale di nodi collegati da frecce. Ogni step appare con animazione progressiva al clic su "avanza" o all'entrata nella slide.

```javascript
// steps: array ordinato
[{
  id: 'osservazioni',
  label: 'Osservazioni',
  sublabel: 'La scena, il campo, il comportamento osservato',
  type: 'input',          // input | operator | output | final
  color: null             // null = usa --color-primary
}, {
  id: 'operatore',
  label: 'Operatore di lettura',
  sublabel: 'Operatore triadico (Campo + Posizione + Limite)',
  type: 'operator',
  color: 'var(--color-f2)'
}, {
  id: 'ce',
  label: 'Configurazione Evolutiva (CE)',
  sublabel: 'Struttura del campo, nodi, direzione, abitabilità',
  type: 'operator',
  color: 'var(--color-f2)'
}, {
  id: 'nodo-dominante',
  label: 'Identificazione del Nodo dominante',
  sublabel: 'Non il nodo più basso — quello che muove di più il campo',
  type: 'operator',
  color: 'var(--color-f3)'
}, {
  id: 'funzione',
  label: 'Funzione dell\'azione',
  sublabel: 'Stabilizzare / Ampliare / Mediare / Proteggere',
  type: 'operator',
  color: 'var(--color-f3)'
}, {
  id: 'dispositivo',
  label: 'Micro-dispositivo contestualizzato',
  sublabel: 'Breve, integrabile, non specialistico, osservabile',
  type: 'final',
  color: 'var(--color-accent)'
}]
```

Usato in: M2 (pipeline completa CE→dispositivo), M8 (pipeline capstone con caso-guida).

### 6.4 `GuardrailBadge(code, label, text)`

Componente badge/callout per i vincoli metodologici. Sfondo verde scuro (`--color-guardrail-bg`), bordo sinistro spesso (`--color-guardrail`), icona scudo. Appare in footer della slide o come elemento separato.

```javascript
GuardrailBadge({
  code: 'C-F3',
  label: 'Vincolo metodologico F3',
  text: 'Se lo strumento richiede diagnosi, attribuisce tratti stabili al bambino, o prescrive sequenze obbligate, non è coerente con il metodo.'
})
```

In F3 i guardrail sono più frequenti che nelle fasi precedenti: ogni modulo ne ha almeno uno. Il codice segue il pattern `C-F3-NM` dove N è il numero del modulo e M è il numero progressivo del guardrail (es. `C-F3-50` = primo guardrail del Modulo 5).

---

### 6.5 `F3Builder(container)` ← **Componente nuovo F3**

Builder interattivo del Template F3. Permette all'utente di costruire passo per passo un micro-dispositivo di campo a partire dalla CE. Usato nel Modulo 5.

**Struttura del template** (7 campi):

```javascript
// Il builder guida la compilazione di questo oggetto:
{
  ceOrigine: '',          // stringa: sintesi grammaticale della CE di partenza
  nodoDominante: '',      // stringa: codice + nome (es. "N3 — Mondo condiviso")
  funzione: '',           // enum: 'stabilizzare' | 'ampliare' | 'mediare' | 'proteggere'
  campoBersaglio: '',     // stringa: es. "Stabilità dello scambio condiviso simbolico"
  microAzioni: [],        // array di 3-5 stringhe (azioni osservabili)
  tempoReale: '',         // stringa: es. "5-10 minuti"
  indicatoreRisonanza: '' // stringa: cosa dovrebbe cambiare nel campo
}
```

**Comportamento UI**:

1. Il builder si presenta come un form a step progressivi (7 step). Ogni step occupa tutta l'area del componente.
2. I campi `ceOrigine` e `nodoDominante` sono pre-compilati con i dati del caso-guida (da `window.CASO_GUIDA_F3`) ma modificabili.
3. Il campo `funzione` è una selezione tra quattro opzioni visive (card selezionabili, ognuna con colore `--color-fn-X`).
4. Il campo `microAzioni` permette di aggiungere/rimuovere azioni (min 3, max 5) con un campo di testo libero per ciascuna.
5. Al completamento di tutti i campi, il builder genera una **descrizione in linguaggio naturale** del dispositivo — costruita da una funzione template string che compone i campi compilati in un testo coerente.
6. Un pulsante "Mostra descrizione naturale" fa apparire il risultato con una transizione slide-down.
7. Un pulsante "Ripristina caso-guida" ricarica i valori pre-compilati del caso-guida.

**Dati pre-compilati** (da `window.CASO_GUIDA_F3`):

```javascript
// Valori di default caricati all'inizializzazione del builder
const DEFAULT_TEMPLATE = {
  ceOrigine: window.CASO_GUIDA_F3.ce.grammaticale,
  nodoDominante: 'N3 — Accesso al mondo condiviso simbolico',
  funzione: 'mediare',
  campoBersaglio: window.CASO_GUIDA_F3.f3.campoBersaglio,
  microAzioni: window.CASO_GUIDA_F3.f3.microAzioni,
  tempoReale: window.CASO_GUIDA_F3.f3.tempoReale,
  indicatoreRisonanza: window.CASO_GUIDA_F3.f3.indicatoreRisonanza
};
```

---

### 6.6 `DecisionCycle(steps, container)` ← **Componente nuovo F3**

Schema circolare animato del Ciclo Decisionale Breve. Ogni nodo del ciclo è cliccabile e mostra il contenuto del passo. Usato nel Modulo 7.

```javascript
// steps: array di 5 oggetti (il ciclo è fisso: OSSERVA→LEGGI→ORIENTA→AGISCI→OSSERVA)
const CICLO_DECISIONALE = [
  {
    id: 'osserva',
    label: 'OSSERVA',
    descrizione: 'Osserva la situazione senza categorizzare. Cosa accade nel campo?',
    domanda: 'Cosa vedo nel campo bambino-adulto-contesto?',
    colore: 'var(--color-f2)',
    nota: 'Il punto di partenza non è il bambino, non è il problema: è la configurazione relazionale osservabile.'
  },
  {
    id: 'leggi',
    label: 'LEGGI (CE)',
    descrizione: 'Costruisci o aggiorna la Configurazione Evolutiva.',
    domanda: 'Quali nodi sono attivi, neutri, limitanti? Qual è la direzione del campo?',
    colore: 'var(--color-f2)',
    nota: 'La CE è il prodotto della F2. In contesto reale può essere parziale — basta che sia strutturalmente fondata.'
  },
  {
    id: 'orienta',
    label: 'ORIENTA (funzione)',
    descrizione: 'Identifica il nodo dominante e scegli la funzione dell\'azione.',
    domanda: 'Dove si restringe il campo? Cosa sta già funzionando? Quale funzione aumenta l\'abitabilità?',
    colore: 'var(--color-f3)',
    nota: 'Non si sceglie la tecnica: si sceglie la funzione. La funzione orienta la scelta del dispositivo.'
  },
  {
    id: 'agisci',
    label: 'AGISCI (micro-dispositivo)',
    descrizione: 'Implementa il micro-dispositivo. Minimo intervento sufficiente.',
    domanda: 'Qual è l\'azione minima che modifica il campo nella direzione evolutiva indicata?',
    colore: 'var(--color-f3)',
    nota: 'Il dispositivo deve essere breve, integrabile, osservabile nei suoi effetti. Non è un protocollo: è un aggiustamento situato.'
  },
  {
    id: 'osserva2',
    label: 'OSSERVA DI NUOVO',
    descrizione: 'Rileva cosa è cambiato nel campo dopo l\'azione.',
    domanda: 'Il campo ha risposto? L\'indicatore di risonanza è presente? Aggiorno la CE?',
    colore: 'var(--color-primary)',
    nota: 'Il ciclo non termina con l\'azione: termina con la nuova osservazione. Se il campo non ha risposto, si rivaluta la funzione — non si insiste con lo stesso dispositivo.'
  }
];
```

**Comportamento UI**:

1. Il componente si presenta come un cerchio con 5 nodi posizionati agli angoli di un pentagono regolare. Il cerchio ha frecce direzionali tra i nodi (senso orario).
2. All'entrata nella slide, i nodi appaiono in sequenza con un'animazione (200ms per nodo, delay progressivo).
3. Cliccando su un nodo, si apre un pannello laterale (a destra del cerchio) con: label grande + descrizione + domanda guida + nota. Il nodo cliccato viene evidenziato (outline + dimensione leggermente aumentata).
4. I nodi `osserva` e `osserva2` hanno lo stesso colore (il ciclo chiude su se stesso): rendere visiva la chiusura del ciclo con una freccia curva dal nodo 5 al nodo 1.
5. Un pulsante "Anima ciclo" percorre in sequenza tutti i nodi (800ms per nodo), aprendo ogni pannello automaticamente.
6. Tempo reale indicato sotto il componente: *"5–10 minuti nel contesto professionale reale."*

---

### 6.7 `CEDisplay(ceData, container)` ← **Funzione utility F3**

Funzione di utilità (non un componente completo) che renderizza una Configurazione Evolutiva nel formato visivo standard. Usata in M2, M3, M8.

```javascript
// ceData: oggetto con la struttura della CE
{
  nodi: {
    N1: { stato: '~', label: 'Regolazione', colore: 'var(--color-n1)' },
    N2: { stato: '↑', label: 'Campo relazionale', colore: 'var(--color-n2)' },
    N3: { stato: '~', label: 'Mondo condiviso', colore: 'var(--color-n3)' },
    N4: { stato: '↓', label: 'Apertura', colore: 'var(--color-n4)' },
    N5: { stato: '~', label: 'Limite', colore: 'var(--color-n5)' },
    N6: { stato: '~', label: 'Continuità', colore: 'var(--color-n6)' },
    N7: { stato: '~', label: 'Desiderio', colore: 'var(--color-n7)' }
  },
  relazione: 'N2→N3 (MED)',
  direzione: '↗',
  tenuta: 'T2',
  abitabilita: 'A±',
  grammaticale: 'Campo relazionale forte che sostiene accesso al mondo condiviso...'
}
```

**Output**: tabella compatta (Nodo | Stato | Label) con stati colorati semanticamente (↑ → `--color-valid`, ↓ → `--color-invalid`, ~ → `--color-text-muted`), seguita da righe di riepilogo (Relazione, Direzione, Tenuta, Abitabilità) e dalla frase grammaticale in corsivo.

La funzione prende un secondo parametro `highlights` (opzionale): array di codici nodo da evidenziare con sfondo tenue (es. `['N3', 'N2']` per la lettura F3 del caso-guida).

```javascript
// Utilizzo tipico in un modulo
const container = document.querySelector('#ce-display');
CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N3', 'N4'] });
```

---

## 7. Il caso-guida F3 (filo rosso)

Il caso-guida è un oggetto globale accessibile da tutti i moduli. In F3, a differenza di F1 e F2, **l'oggetto è completo fin dall'inizio**: contiene sia la scena base sia la CE prodotta dalla F2 sia tutti i dati prodotti dall'applicazione della F3. I moduli la svelano progressivamente al partecipante, ma il dato è disponibile per tutti i moduli dall'avvio.

Definire in `app.js`:

```javascript
window.CASO_GUIDA_F3 = {

  // ─── Scena base (identica a F2 e F1) ────────────────────────────────────
  titolo: 'Lettura condivisa adulto-bambino',
  scena: `Durante un bilancio di salute, il pediatra propone per alcuni minuti
          una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi.
          È presente un genitore. Sul tavolo c'è un piccolo libro illustrato
          con immagini semplici: animali, oggetti familiari, figure umane.
          Il bambino prende il libro, lo apre, guarda alcune immagini, indica
          una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina
          l'immagine, sorride, aspetta. Il bambino torna a guardare il libro,
          gira pagina, poi mostra un'altra figura all'adulto.`,

  // ─── CE prodotta dalla F2 (input di F3) ─────────────────────────────────
  ce: {
    nodi: {
      N1: { stato: '~', label: 'Regolazione', colore: 'var(--color-n1)' },
      N2: { stato: '↑', label: 'Campo relazionale', colore: 'var(--color-n2)' },
      N3: { stato: '~', label: 'Mondo condiviso', colore: 'var(--color-n3)' },
      N4: { stato: '↓', label: 'Apertura / Esplorazione', colore: 'var(--color-n4)' },
      N5: { stato: '~', label: 'Limite reale', colore: 'var(--color-n5)' },
      N6: { stato: '~', label: 'Continuità', colore: 'var(--color-n6)' },
      N7: { stato: '~', label: 'Desiderio', colore: 'var(--color-n7)' }
    },
    relazione: 'N2→N3 (MED)',
    direzione: '↗',
    tenuta: 'T2',
    abitabilita: 'A±',
    grammaticale: `Campo relazionale forte che sostiene accesso al mondo condiviso simbolico,
                   con esplorazione ridotta ma in espansione.
                   Configurazione fragile ma evolutivamente aperta.`
  },

  // ─── Applicazione F3 al caso-guida ──────────────────────────────────────
  f3: {

    // Step 1 — Nodo dominante
    nodoDominante: {
      codice: 'N3',
      nome: 'Accesso al mondo condiviso simbolico',
      colore: 'var(--color-n3)',
      motivazione: `N3 è il nodo la cui apertura muove il campo nella direzione evolutiva
                    indicata (D↗). Non è il nodo con lo stato più basso numericamente
                    (N4↓), ma è quello la cui attivazione produce il cambiamento più
                    rilevante per l'abitabilità complessiva del campo.`
    },
    nodoSostegno: {
      codice: 'N2',
      nome: 'Campo relazionale / Co-regolazione',
      colore: 'var(--color-n2)',
      ruolo: `N2 è sostenuto (↑) e costituisce la risorsa su cui si appoggia
              l'intervento: senza co-regolazione attiva, l'accesso al mondo
              condiviso non si produce.`
    },
    nodoInTensione: {
      codice: 'N4',
      nome: 'Apertura / Esplorazione del mondo',
      colore: 'var(--color-n4)',
      nota: `N4↓ è il nodo limitante secondario. Non è il target dell'intervento
             in questo contesto (il bilancio non è il luogo per lavorare l'esplorazione),
             ma va tenuto presente: un dispositivo che sovraccarica il campo
             riduce ulteriormente l'esplorabilità.`
    },

    // Step 2 — Funzione
    funzione: 'MEDIAZIONE',
    funzioneColore: 'var(--color-fn-mediare)',
    funzioneDescrizione: `Coordinare N2 (attivo, ↑) e N3 (neutro, ~), stabilizzando
                          le condizioni che rendono possibile l'accesso al mondo condiviso
                          simbolico. Non stabilizzare (il campo non è in collasso),
                          non ampliare (sarebbe prematuro con N4↓),
                          ma mediare la transizione già in corso.`,

    // Step 3 — Micro-dispositivo
    campoBersaglio: 'Stabilità e durata dello scambio condiviso simbolico',
    microAzioni: [
      'Il genitore segue l\'interesse del bambino senza anticiparlo né dirigerlo',
      'Nomina ciò che il bambino indica, con voce calma e ritmo lento',
      'Attende la risposta del bambino senza riempire il silenzio',
      'Espande senza correggere ("Sì, il cane — e guarda qui...")',
      'Il pediatra osserva senza interrompere la sequenza bambino-genitore'
    ],
    tempoReale: '5 minuti durante il bilancio pediatrico',
    indicatoreRisonanza: `Il bambino include l'adulto nella sequenza con sguardo condiviso,
                          gesto e vocalizzazione integrati. La sequenza si allunga:
                          non termina al primo giro.`,

    // Step 4 — Verifica di coerenza
    verificaCoerenza: [
      { ok: true,  check: 'Non etichetta il bambino', nota: 'Le micro-azioni descrivono il campo, non il bambino.' },
      { ok: true,  check: 'Non richiede diagnosi', nota: 'Il dispositivo è applicabile a prescindere da etichette cliniche.' },
      { ok: true,  check: 'Modifica interazioni osservabili', nota: 'Ogni micro-azione è osservabile e verificabile.' },
      { ok: true,  check: 'Produce nuova leggibilità', nota: 'L\'indicatore di risonanza permette di rileggere la CE dopo il dispositivo.' },
      { ok: true,  check: 'Permette rivalutazione della CE', nota: 'Se il bambino non risponde, si aggiorna la lettura — non si insiste.' }
    ],

    // Output-tipo vuoto compilato
    outputTipo: {
      A: `Il bambino orienta il libro verso l'adulto: il mondo appare condiviso
          ma discontinuo. L'alternanza di sguardo è presente; la sequenza di
          scambio si interrompe e non sempre riprende autonomamente.`,
      B: `Emergenza di posizione riconoscibile: il bambino indica, vocalizza,
          cerca la risposta dell'adulto. La permanenza nel legame è presente
          ma non ancora stabile — dipende dalla qualità della risposta adulta.`,
      C: `Limite tollerato: la condivisione si interrompe e può riprendere.
          Non collassa. La "fine" della sequenza non produce disorganizzazione.`,
      D: `In questa situazione il campo appare strutturato prevalentemente come
          accesso intermittente al mondo condiviso simbolico, con campo relazionale
          attivo come sostegno e apertura esplorativa ridotta.`,
      E: `Rafforzare la stabilità del campo condiviso sostenendo la sequenza del
          bambino senza anticiparne i gesti. Non ampliare (rischio di sovraccarico),
          non correggere, ma rendere lo scambio più duraturo.`
    },

    // Tipo universale
    tipoUniversale: ['U2', 'U4'],
    tipoUniversaleNome: 'Sintonizzazione (U2) + Mediazione Simbolica (U4)',
    tipoUniversaleMotivazione: `U2 perché il dispositivo segue l'iniziativa del bambino
                                 e rispecchia senza dirigere (funzione: rendere l'esperienza
                                 condivisibile). U4 perché trasforma l'oggetto-libro in
                                 mediatore simbolico attraverso la narrazione condivisa.`,

    // Logica decisionale applicata
    logicaDecisionale: {
      D1: `Il campo si restringe nella durata e stabilità dello scambio condiviso:
           la sequenza bambino-libro-adulto si interrompe prima che si consolidi.`,
      D2: `Il campo relazionale (N2) è attivo e sostenuto. Il genitore risponde,
           sorride, aspetta. Il bambino ha iniziativa (indica, vocalizza). Questi sono
           i punti di forza su cui costruire.`,
      D3: `Un'azione che rallenta il ritmo e riduce la direttività adulta aumenta
           l'abitabilità: il bambino può mantenere l'iniziativa più a lungo,
           la sequenza si allunga, N3 si stabilizza.`,
      D4: `Il minimo intervento sufficiente è modificare il comportamento adulto
           nel corso della scena (seguire, nominare, attendere, espandere):
           non aggiungere materiali, non ristrutturare il setting, non prescrivere
           sessioni separate.`
    }
  },

  // ─── Guardrail fondamentale F3 ───────────────────────────────────────────
  guardrail: {
    code: 'C-F3',
    label: 'Vincolo metodologico — Fase 3',
    text: `Lo strumento F3 non corregge il bambino: modifica il campo relazionale
           di esperienza. Se un dispositivo ha senso solo riferito al bambino
           separato dal campo, è metodologicamente scorretto.`,
    verifiche: [
      { ok: true,  label: 'Azione sul campo',   desc: 'Il dispositivo modifica le condizioni relazionali, non i comportamenti del bambino.' },
      { ok: false, label: 'Azione sul bambino', desc: 'Il dispositivo mira a far fare al bambino qualcosa di diverso. → Non conforme.' }
    ]
  }
};
```

---

## 8. Convenzioni di codice

### JavaScript
- ES6+ (const/let, arrow functions, template literals, destructuring)
- Nessun framework esterno — vanilla JS puro
- Nessun `var`
- Funzioni brevi e con nome esplicito
- Commenti in italiano (il progetto è in italiano)

### CSS
- BEM leggero per i componenti: `.slide__header`, `.card--expanded`, `.f3builder__step`, `.decision-cycle__node--active`
- Nessuno stile inline nel JS (eccetto variabili CSS dinamiche con `el.style.setProperty`)
- Mobile-first per le media query (anche se il corso è ottimizzato per desktop 1280px+)
- I colori delle Funzioni (`--color-fn-X`) e dei Tipi Universali (`--color-uX`) devono essere usati coerentemente: non sostituire con colori ad hoc nelle slide

### HTML
- Markup semantico: `<section>`, `<article>`, `<nav>`, `<main>`
- Attributi `data-*` per i riferimenti JS: `data-slide`, `data-module`, `data-node`, `data-function`, `data-utype`
- `aria-label` e ruoli accessibili sui componenti interattivi
- Il builder F3Builder usa `data-step` su ogni pannello di step
- Il DecisionCycle usa `data-cycle-node` su ogni nodo del cerchio

---

## 9. Come aggiungere un nuovo modulo

1. Crea `js/modules/mXX.js` con la struttura `ModuleXX` descritta nella §5
2. Importa il file in `index.html` con `<script src="js/modules/mXX.js">`
3. Registra il modulo in `app.js` nell'array `MODULES`: `[Module00, Module01, ..., Module08]`
4. Il router gestisce automaticamente la navigazione e il rendering

Non modificare `index.html`, `style.css` o `app.js` per contenuti specifici del modulo.

---

## 10. Ordine di costruzione

Il piano completo prevede 9 moduli. Lavora in questo ordine numerico:

| Priorità | Modulo | File contenuto | Componente chiave introdotto |
|----------|--------|---------------|------------------------------|
| 1 | M0 — Orientamento | `f3-modulo-00.md` | Layout shell + `CEDisplay` (versione semplice) |
| 2 | M1 — Principio del campo | `f3-modulo-01.md` | `ComparisonPanel` (campo vs. comportamento) |
| 3 | M2 — Dalla CE allo strumento | `f3-modulo-02.md` | `PipelineAnimator` (pipeline F3) + `CEDisplay` completo |
| 4 | M3 — Nodo dominante | `f3-modulo-03.md` | `CEDisplay` con highlights + lettura guidata |
| 5 | M4 — Le quattro funzioni | `f3-modulo-04.md` | `ExpandableCards` (4 funzioni) |
| 6 | M5 — Il micro-dispositivo | `f3-modulo-05.md` | `F3Builder` + form output-tipo |
| 7 | M6 — Tipologia U1–U6 | `f3-modulo-06.md` | `ExpandableCards` (6 tipi) |
| 8 | M7 — Logica decisionale | `f3-modulo-07.md` | `DecisionCycle` |
| 9 | M8 — Pipeline completa | `f3-modulo-08.md` | Tutti i componenti in forma ridotta (capstone) |

**Quando inizi un modulo**: leggi il file `f3-modulo-XX.md` corrispondente per il contenuto esatto delle slide.

**Note sull'ordine**: M5 introduce `F3Builder`, il componente più complesso. Prima di costruirlo, assicurati che `CEDisplay` e `ExpandableCards` siano stabili (M2–M4). `DecisionCycle` in M7 è tecnicamente autonomo ma concettualmente dipende dalla comprensione delle quattro funzioni (M4) e del template (M5).

---

## 11. Note metodologiche importanti

Queste regole emergono dalla F3 del metodo e devono riflettersi nel design di ogni slide. Alcune sono analoghe a quelle di F1 e F2; alcune sono specifiche di F3.

### 11.1 Regole fondamentali

1. **Lo strumento non corregge il bambino: modifica il campo**
   Conseguenza diretta dell'Asse 1. Il soggetto grammaticale delle micro-azioni non è mai "il bambino deve fare X" ma "le condizioni relazionali che permettono X". Esempi: non "insegnare al bambino a indicare" → "aumentare la stabilità dello scambio condiviso in cui il gesto del bambino trova risposta"; non "stimolare il linguaggio" → "modificare il ritmo dell'adulto perché la sequenza del bambino possa completarsi".

2. **Il nodo dominante non è il nodo con lo stato più basso**
   Errore frequente: identificare il nodo dominante con il nodo "più limitante" nella CE. Il nodo dominante è quello la cui attivazione muove di più il campo nella direzione evolutiva indicata. In una CE con N4↓ e N3~, il nodo dominante per l'intervento può essere N3 — perché la sua apertura traina il campo verso D↗. Nelle slide che mostrano la logica di identificazione del nodo dominante, rendere questa distinzione esplicita.

3. **F3 orienta la decisione: non la prende**
   La responsabilità della scelta finale è disciplinare (pediatra, educatore, psicologo). F3 produce vincoli di coerenza, non obblighi. In ogni slide che presenta un dispositivo, mantenere la distinzione tra "azione coerente con questa configurazione" e "azione prescritta". Non usare linguaggio imperativo nelle descrizioni dei dispositivi.

4. **Il minimo intervento sufficiente**
   Principio chiave di F3: intervenire meno possibile ma nel punto giusto. Nelle slide che presentano dispositivi, privilegiare sempre la versione più semplice e integrabile del dispositivo rispetto a quella più elaborata. Questo si riflette anche nel design: non sovraccaricare le slide di micro-azioni — 3 sono meglio di 7.

5. **Se lo strumento chiude possibilità → errore metodologico**
   Una decisione è corretta se mantiene apertura futura, non sostituisce il bambino, non aumenta dipendenza, genera nuova osservabilità. Nelle slide che mostrano errori decisionali, non usare linguaggio moralizzante o censorio: mostrare perché l'errore chiude possibilità, non giudicare il professionista.

6. **Nessuna normatività implicita**
   La F3 eredita il vincolo fondamentale di F1 e F2: nessun elemento visivo deve suggerire soglie di normalità, punteggi, confronti con standard attesi. I dispositivi descrivono micro-azioni contestualizzate, non best practice universali.

### 11.2 Distinzioni visive critiche

| Concetto | Visualizzazione corretta | Da evitare |
|----------|------------------------|-----------|
| Nodo dominante | Evidenziato nella CEDisplay con bordo spesso e colore pieno | Freccia "più importante" o dimensione maggiore |
| Nodo di sostegno | Badge secondario, colore pieno ma dimensione normale | Stessa evidenziazione del nodo dominante |
| Funzione scelta | Card selezionata con colore `--color-fn-X` | Icona di "conferma" o "correttezza" |
| Micro-azione | Lista ordinata (non puntata): sono passi in sequenza | Lista puntata senza ordine implicato |
| Verifica di coerenza | Checklist con ✓/✗ e testo esplicativo | Punteggio numerico o percentuale |
| Guardrail | Badge verde `C-F3`, tono neutro | Avvertimento rosso, triangolo di pericolo |
| Errore decisionale | Box rosso tenue con spiegazione della perdita | Icona ❌ grande o linguaggio giudicante |

### 11.3 Il caso-guida in F3

La scena deve essere citata testualmente da `window.CASO_GUIDA_F3.scena` — mai duplicata o parafrasata nel codice dei moduli. La CE viene renderizzata con `CEDisplay(window.CASO_GUIDA_F3.ce, container)` — mai riscritta manualmente nelle slide.

Il template F3 e l'output-tipo vuoto usano sempre i dati da `window.CASO_GUIDA_F3.f3` — questo garantisce coerenza tra tutti i moduli e facilita eventuali aggiornamenti.

### 11.4 Continuità visiva con F1 e F2

Anche se le tre applicazioni sono tecnicamente indipendenti, il partecipante ha già incontrato il caso-guida in F1 e F2. In F3:

- Le slide che mostrano la scena del caso-guida devono usare lo stesso stile visivo (card narrativa, sfondo `--color-primary-light`, bordo sinistro `--color-primary`, testo in corsivo) usato in F1 e F2.
- Il diagramma F1→F2→F3 in M0 deve essere visivamente coerente con lo stesso diagramma presente nel M0 di F2 — cambiano i colori attivi, non la struttura.
- I colori dei Nodi Trasversali (`--color-n1` … `--color-n7`) sono gli stessi usati in F2: questa coerenza è intenzionale e il partecipante la riconoscerà.

---

*Fine istruzioni. Per il contenuto metodologico di ogni slide, fare riferimento ai file `f3-modulo-XX.md` nella stessa cartella.*
