# ISTRUZIONI PER CLAUDE CODE
## Corso: Fase 2 — Traduzione Interdisciplinare
## Progetto: HCAIRE — Applicazione formativa HTML/CSS/JS

---

## 1. Contesto del progetto

Stai costruendo un'applicazione web formativa single-page per un corso destinato a **professionisti della prima infanzia** (pediatri, educatori, psicologi, coordinatori di servizi). Il corso illustra la **Fase 2 — Traduzione Interdisciplinare** di un metodo per la lettura dello sviluppo infantile.

Il piano completo del corso comprende 10 moduli (~69 slide totali). Tu lavori **un modulo alla volta**. Ogni modulo viene definito da un file di contenuto (`modulo-XX.md`) che trovi nella stessa cartella di questo file. Le istruzioni architetturali qui sotto valgono per l'intera applicazione.

**Filo rosso del corso**: un caso-guida unico attraversa tutti i moduli — una situazione di *lettura condivisa adulto-bambino* (Dialogic Book Sharing) durante un bilancio pediatrico. Il caso appare nel Modulo 0 e viene approfondito modulo per modulo fino alla pipeline completa nel Modulo 9.

---

## 2. Struttura dei file

```
/
├── index.html               ← shell principale, navigation, router
├── css/
│   └── style.css            ← design system completo
├── js/
│   ├── app.js               ← logica di navigazione e stato globale
│   └── modules/
│       ├── m00.js           ← Modulo 0: dati + interattività
│       ├── m01.js           ← Modulo 1 (da fare dopo)
│       ├── m02.js           ← Modulo 2: dati + interattività
│       └── ...              ← un file per modulo
└── ISTRUZIONI_CLAUDE_CODE.md
```

### Responsabilità di ogni file

**`index.html`**: struttura DOM fissa (sidebar, area slide, controlli), carica tutti i moduli JS, non contiene contenuto delle slide.

**`style.css`**: design system completo. Non usare stili inline nelle slide — ogni variazione va come classe CSS o variabile CSS.

**`app.js`**: gestisce stato globale (modulo corrente, slide corrente), router, keybindings (frecce), animazioni di transizione tra slide.

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
  --color-accent: var(--module-accent, #1a6b8a);

  /* Colori per i Nodi Trasversali */
  --color-n1: #e67e22;   /* N1 Regolazione */
  --color-n2: #2ecc71;   /* N2 Campo relazionale */
  --color-n3: #3498db;   /* N3 Mondo condiviso */
  --color-n4: #9b59b6;   /* N4 Apertura */
  --color-n5: #e74c3c;   /* N5 Limite reale */
  --color-n6: #1abc9c;   /* N6 Continuità */
  --color-n7: #f39c12;   /* N7 Desiderio */

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

### 3.2 Colori accent per modulo

Ogni modulo ha un `--module-accent` che colora la barra superiore e le evidenziazioni:

| Modulo | Colore accent |
|--------|--------------|
| M0 — Orientamento | #1a6b8a (primary) |
| M1 — Traduzione | #6c63ff |
| M2 — Pipeline | #2d6a4f |
| M3 — Nodo Trasversale | #e67e22 |
| M4 — Matrice | #2980b9 |
| M5 — Dinamica | #8e44ad |
| M6 — Grammatica CE | #16a085 |
| M7 — Operatore Lettura | #d35400 |
| M8 — Output vuoto | #27ae60 |
| M9 — Pipeline completa | #c0392b |

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

### Area slide

- Occupa il resto della larghezza disponibile
- Ogni slide è un `<section class="slide">` con layout flessibile
- Le slide hanno un'area principale (contenuto) e opzionalmente un footer con nota o controllo di coerenza
- Transizione tra slide: slide-fade (200ms opacity + 8px translate-y)

### Controlli

- Frecce ← → sempre visibili; la freccia sinistra è disabilitata alla prima slide del primo modulo
- I dot indicators mostrano la posizione nella slide corrente (non nel modulo)
- Shortcut tastiera: ← → per navigare, numero 0-9 per saltare a un modulo

---

## 5. Struttura di una slide

Ogni slide è un oggetto JS con questa struttura:

```javascript
{
  id: 'slide-id',                    // stringa unica
  type: 'standard' | 'diagram' | 'interactive' | 'comparison' | 'narrative',
  title: 'Titolo della slide',
  subtitle: 'Sottotitolo opzionale',
  content: '...',                    // HTML o funzione che ritorna HTML
  notes: 'Nota per il relatore',     // opzionale, mostrata in footer discreto
  guardrail: {                       // opzionale, mostrato se presente
    code: 'C0',
    label: 'Vincolo di contesto',
    text: 'La situazione è valida perché è delimitata.'
  },
  onEnter: function() { ... },       // opzionale, chiamata all'entrata nella slide
  onLeave: function() { ... },       // opzionale, chiamata all'uscita
}
```

### Tipi di slide

**`standard`**: testo, titolo, eventuale elemento visivo. Layout colonna singola o due colonne.

**`diagram`**: elemento visivo dominante (schema, grafo, pipeline). Il testo è secondario o in tooltip.

**`interactive`**: contiene un componente interattivo (card espandibili, matrice, builder). L'area principale è occupata dal componente.

**`comparison`**: due colonne affiancate (valido / non valido, oppure prima / dopo). Usata per gli esempi metodologici.

**`narrative`**: testo narrativo più lungo, layout tipografico. Usata per il caso-guida e le introduzioni.

---

## 6. Componenti interattivi riutilizzabili

Questi componenti devono essere definiti in `js/app.js` come funzioni/classi e riutilizzati da tutti i moduli.

### 6.1 `ExpandableCards(data, container)`

Crea un set di card espandibili.

```javascript
// data: array di oggetti
[{
  id: 'n1',
  color: '#e67e22',       // colore accent della card
  badge: 'N1',           // etichetta breve
  title: 'Regolazione / Integrazione',
  summary: 'Capacità del sistema bambino-ambiente...',
  detail: '<p>Assi: 1–2–4</p><p>Domande: ...</p>'
}]
```

La card mostra badge + title + summary. Cliccando si espande a mostrare il detail. Un solo card alla volta può essere aperto, oppure più card simultaneamente (configurabile con `multiOpen: true`).

### 6.2 `ComparisonPanel(valid, invalid, container)`

Due colonne affiancate con intestazione colorata (verde/rosso) e contenuto.

```javascript
{
  label: 'Concetto-ponte',
  valid: {
    title: 'Formulazione valida',
    content: 'Il bambino usa il libro come occasione...'
  },
  invalid: {
    title: 'Formulazione riduttiva',
    items: [
      { text: 'Il bambino presta attenzione', problem: 'Riduce il campo a funzione attentiva' }
    ]
  }
}
```

### 6.3 `PipelineAnimator(steps, container)`

Visualizza la pipeline come sequenza verticale di nodi collegati da frecce. Ogni step appare con un'animazione quando si clicca "avanza" o quando si entra nella slide corrispondente.

```javascript
// steps: array ordinato
[{
  id: 'f1',
  label: 'F1 — Fondazione ontologica',
  sublabel: 'Assi + tesi + criteri',
  type: 'foundation',   // foundation | operator | output
  control: null
}, {
  id: 'op1',
  label: '① Campo di lavoro',
  sublabel: 'Contesto reale / dispositivo / popolazione',
  type: 'operator',
  control: { code: 'C0', label: 'Vincolo di contesto' }
}, ...]
```

### 6.4 `InteractiveMatrix(rows, cols, cells, container)`

Griglia con intestazioni di riga e colonna. Cliccando su una cella si mostra il contenuto. Hover su una riga evidenzia tutta la riga; hover su una colonna evidenzia tutta la colonna.

```javascript
{
  rows: [{ id: 'n1', label: 'N1 — Regolazione', color: '#e67e22' }, ...],
  cols: [{ id: 'c', label: 'Clinico' }, { id: 'p', label: 'Pedagogico' }, ...],
  cells: {
    'n1-c': 'L\'esperienza si mantiene o collassa?',
    'n1-p': 'Il contesto sovraccarica o sostiene?',
    ...
  }
}
```

### 6.5 `CEBuilder(container)`

Builder interattivo della Configurazione Evolutiva. Permette di selezionare lo stato di N1–N7, la relazione dominante, la direzione, la stabilità e l'abitabilità. Genera la forma standard e la traduzione in linguaggio naturale. Usato nel Modulo 6.

### 6.6 `GuardrailBadge(code, label, text)`

Componente badge/callout usato in ogni slide che presenta un controllo di coerenza. Sfondo verde scuro, bordo sinistro, icona scudo. Appare in footer della slide o come elemento separato.

---

## 7. Il caso-guida (filo rosso)

Il caso-guida è un oggetto globale accessibile da tutti i moduli:

```javascript
window.CASO_GUIDA = {
  titolo: 'Lettura condivisa adulto-bambino',
  scena: `Durante un bilancio di salute, il pediatra propone per alcuni minuti
          una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi.
          È presente un genitore. Sul tavolo c'è un piccolo libro illustrato
          con immagini semplici: animali, oggetti familiari, figure umane.
          Il bambino prende il libro, lo apre, guarda alcune immagini, indica
          una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina
          l'immagine, sorride, aspetta. Il bambino torna a guardare il libro,
          gira pagina, poi mostra un'altra figura all'adulto.`,
  pipeline: {
    campo: 'Bilancio pediatrico, bambino 18-24 mesi, genitore, libro illustrato, 3-5 min.',
    concettoPonte: 'Accesso al mondo condiviso',
    nodo: 'N3 — Accesso al mondo condiviso simbolico',
    domandeProf: [
      'Il bambino usa l\'oggetto come occasione di scambio con l\'adulto?',
      'C\'è alternanza di sguardo tra libro e adulto?',
      'Il gesto apre una relazione o rimane azione solitaria?'
    ],
    operatoreTryadico: {
      campo: 'Il bambino e l\'adulto si orientano verso qualcosa di comune (il libro), con gesto, sguardo e parola che si intrecciano.',
      posizione: 'Il bambino indica, mostra, vocalizza: c\'è iniziativa soggettiva e non solo reazione all\'adulto.',
      limite: 'Il bambino accetta di condividere il controllo del libro con l\'adulto; la sequenza si interrompe e riprende.'
    },
    ce: {
      S: { N1: '~', N2: '↑', N3: '~', N4: '↓', N5: '~', N6: '~', N7: '~' },
      R: 'N2→N3 (MED)',
      D: '↗',
      T: 'T2',
      A: 'A±'
    },
    ceNaturale: 'Campo relazionale forte che sostiene accesso al mondo condiviso, con esplorazione ridotta ma in espansione. Configurazione fragile ma evolutivamente aperta.'
  }
};
```

Ogni modulo può importare e visualizzare le sezioni rilevanti di questo oggetto.

---

## 8. Convenzioni di codice

### JavaScript
- ES6+ (const/let, arrow functions, template literals, destructuring)
- Nessun framework esterno — vanilla JS puro
- Nessun `var`
- Funzioni brevi e con nome esplicito
- Commenti in italiano (il progetto è in italiano)

### CSS
- BEM leggero per i componenti: `.slide__header`, `.card--expanded`
- Nessuno stile inline nel JS (eccetto variabili CSS dinamiche con `el.style.setProperty`)
- Mobile-first per le media query (anche se il corso è ottimizzato per desktop 1280px+)

### HTML
- Markup semantico: `<section>`, `<article>`, `<nav>`, `<main>`
- Attributi `data-*` per i riferimenti JS: `data-slide`, `data-module`, `data-node`
- `aria-label` e ruoli accessibili sui componenti interattivi

---

## 9. Come aggiungere un nuovo modulo

1. Crea `js/modules/mXX.js` con la struttura `ModuleXX` descritta nella §5
2. Importa il file in `index.html` con `<script src="js/modules/mXX.js">`
3. Registra il modulo in `app.js` nell'array `MODULES`: `[Module00, Module01, Module02, ...]`
4. Il router gestisce automaticamente la navigazione e il rendering

Non modificare `index.html`, `style.css` o `app.js` per contenuti specifici del modulo.

---

## 10. Ordine di costruzione

Il piano completo prevede 10 moduli. Lavora in questo ordine:

| Priorità | Modulo | File contenuto | Note |
|----------|--------|---------------|------|
| 1 | M0 — Orientamento | `modulo-00.md` | Prima il layout generale e la shell |
| 2 | M2 — Pipeline | `modulo-02.md` | Componente `PipelineAnimator` centrale |
| 3 | M3 — Nodo Trasversale | (da preparare) | Componente `ExpandableCards` N1–N7 |
| 4 | M1 — Traduzione | (da preparare) | Componente `ComparisonPanel` |
| 5 | M4 — Matrice | (da preparare) | Componente `InteractiveMatrix` |
| 6 | M5 — Dinamica | (da preparare) | Grafo nodi |
| 7 | M6 — Grammatica CE | (da preparare) | Componente `CEBuilder` |
| 8 | M7 — Operatore | (da preparare) | |
| 9 | M8 — Output vuoto | (da preparare) | |
| 10 | M9 — Pipeline completa | (da preparare) | Modulo capstone |

**Quando inizi un modulo**: leggi il file `modulo-XX.md` corrispondente per il contenuto esatto delle slide.

---

## 11. Note metodologiche importanti

Queste regole emergono dal metodo e devono riflettersi nel design:

1. **Mai diagnostico**: nessun elemento visivo che suggerisca punteggi, soglie di normalità o etichette cliniche.
2. **Mai prescrittivo**: le slide descrivono; non dicono cosa fare.
3. **La configurazione descrive il campo, non il bambino**: nelle slide che mostrano la CE, il soggetto grammaticale è sempre il campo relazionale, non il bambino.
4. **I Nodi sono invarianti**: nella matrice e nel grafo, il Nodo non cambia aspetto nei diversi contesti — cambia solo la domanda.
5. **F2 produce leggibilità, non azione**: nei footer e nelle note, ribadire questa distinzione quando pertinente.

---

*Fine istruzioni. Per domande sul contenuto metodologico, fare riferimento ai file nella cartella `context/`.*
