# ISTRUZIONI PER CLAUDE CODE
## Corso: Fase 1 — Fondazione Ontologica
## Progetto: HCAIRE — Applicazione formativa HTML/CSS/JS

---

## 1. Contesto del progetto

Stai costruendo un'applicazione web formativa single-page per un corso destinato a **professionisti della prima infanzia** (pediatri, educatori, psicologi, coordinatori di servizi). Il corso illustra la **Fase 1 — Fondazione Ontologica** di un metodo per la lettura dello sviluppo infantile.

Esiste già un corso analogo per la Fase 2 (Traduzione Interdisciplinare): questa applicazione segue la stessa architettura tecnica di quel corso, nella propria cartella autonoma. **Le due applicazioni sono indipendenti**: non condividono JS né HTML, ma condividono le convenzioni di design system descritte di seguito.

Il piano completo del corso comprende **8 moduli (M0–M7), ~55 slide totali**. Tu lavori **un modulo alla volta**. Ogni modulo viene definito da un file di contenuto (`f1-modulo-XX.md`) che trovi nella stessa cartella di questo file. Le istruzioni architetturali qui sotto valgono per l'intera applicazione.

**Filo rosso del corso**: il caso-guida è la stessa scena del corso F2 — una situazione di *lettura condivisa adulto-bambino* (Dialogic Book Sharing) durante un bilancio pediatrico — ma viene utilizzata in modo diverso. In F1 la scena non viene analizzata attraverso una pipeline: viene **riluminata** modulo per modulo attraverso lenti diverse. Ogni asse strutturale mostra nella stessa scena qualcosa che senza di esso non si vedrebbe. Nessuna animazione di avanzamento — la luce cambia, la scena resta.

---

## 2. Struttura dei file

```
F1/
├── index.html               ← shell principale, navigation, router
├── css/
│   └── style.css            ← design system completo
├── js/
│   ├── app.js               ← logica di navigazione e stato globale
│   └── modules/
│       ├── m00.js           ← Modulo 0: dati + interattività
│       ├── m01.js           ← Modulo 1: dati + interattività
│       ├── m02.js           ← Modulo 2: dati + interattività
│       └── ...              ← fino a m07.js
└── ISTRUZIONI_CLAUDE_CODE_F1.md
```

La cartella `F1/` è una directory autonoma, separata da quella del corso F2 (che usa la radice del progetto). Crea e lavora sempre all'interno di `F1/`.

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

  /* Accento modulo (cambia per modulo) */
  --color-accent: var(--module-accent, #6c63ff);

  /* Colori per i Nodi Trasversali (usati nelle slide di raccordo con F2) */
  --color-n1: #e67e22;
  --color-n2: #2ecc71;
  --color-n3: #3498db;
  --color-n4: #9b59b6;
  --color-n5: #e74c3c;
  --color-n6: #1abc9c;
  --color-n7: #f39c12;

  /* Colori per i Controlli (guard-rail) */
  --color-guardrail: #2d6a4f;
  --color-guardrail-bg: #d8f3dc;

  /* Fasi */
  --color-f1: #6c63ff;
  --color-f2: #1a6b8a;
  --color-f3: #2d9cdb;

  /* Colori semantici per gli assi strutturali */
  --color-a1: #6c63ff;   /* Asse 1 — Ontologico-fenomenologico */
  --color-a2: #2d6a4f;   /* Asse 2 — Affettivo-morale */
  --color-a3: #27ae60;   /* Asse 3 — Normativo-educativo */
  --color-a4: #c0392b;   /* Asse 4 — Separazione e limite reale */
  --color-a5: #e67e22;   /* Asse 5 — Desiderio */
  --color-a6: #d35400;   /* Asse 6 — Mondo storico-culturale */

  /* Feedback */
  --color-valid: #27ae60;
  --color-invalid: #e74c3c;
  --color-warning: #f39c12;
}
```

### 3.2 Colori accent per modulo

Ogni modulo ha un `--module-accent` che colora la barra superiore, i badge e le evidenziazioni:

| Modulo | Titolo | Colore accent |
|--------|--------|--------------|
| M0 — Orientamento | Perché una fondazione? | `#6c63ff` |
| M1 — Il soggetto | Il bambino come soggetto | `#5c35a0` |
| M2 — Gli assi | Logica e architettura | `#4a5568` |
| M3 — Asse 1 | Abitare l'esperienza | `#1a6b8a` |
| M4 — Assi 2 e 3 | Alterità e normatività | `#2d6a4f` |
| M5 — Assi 4 e 5 | Limite reale e desiderio | `#c0392b` |
| M6 — Asse 6 | Il mondo storico-culturale | `#d35400` |
| M7 — Epistemologia | Statuto e passaggio a F2 | `#2c3e50` |

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
│    ...        │                                             │
│  · M7         │                                             │
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
- Badge piccolo `F1` nella topbar, colorato in `--color-f1`, per distinguere visivamente questa applicazione da quella F2

### Area slide

- Occupa il resto della larghezza disponibile
- Ogni slide è un `<section class="slide">` con layout flessibile
- Le slide hanno un'area principale (contenuto) e opzionalmente un footer con nota o guardrail
- Transizione tra slide: slide-fade (200ms opacity + 8px translate-y)

### Controlli

- Frecce ← → sempre visibili; la freccia sinistra è disabilitata alla prima slide del primo modulo
- I dot indicators mostrano la posizione nella slide corrente (non nel modulo)
- Shortcut tastiera: ← → per navigare, numero 0-7 per saltare a un modulo

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
    code: 'G-F1',
    label: 'Guardrail fondativo',
    text: 'Ogni output deve poter essere usato senza descrivere il bambino come individuo isolato.'
  },
  onEnter: function() { ... },       // opzionale, chiamata all'entrata nella slide
  onLeave: function() { ... },       // opzionale, chiamata all'uscita
}
```

### Tipi di slide

**`standard`**: testo, titolo, eventuale elemento visivo. Layout colonna singola o due colonne.

**`diagram`**: elemento visivo dominante (schema, gerarchia, grafo). Il testo è secondario o in tooltip.

**`interactive`**: contiene un componente interattivo (card espandibili, matrice, annotazioni). L'area principale è occupata dal componente.

**`comparison`**: due colonne affiancate (ontologia riduttiva / ontologia del progetto, oppure con-campo / senza-campo). Usata sistematicamente per le distinzioni strutturali di F1.

**`narrative`**: testo narrativo più lungo, layout tipografico. Usata per il caso-guida e per le slide di riluminazione della scena attraverso gli assi.

---

## 6. Componenti interattivi riutilizzabili

Questi componenti devono essere definiti in `js/app.js` come funzioni/classi e riutilizzati da tutti i moduli.

### 6.1 `ExpandableCards(data, container, options)`

Crea un set di card espandibili.

```javascript
// data: array di oggetti
[{
  id: 'a1',
  color: '#6c63ff',       // colore accent della card
  badge: 'A',             // etichetta breve (lettera, numero, sigla)
  title: 'Titolo della card',
  summary: 'Testo breve visibile nel fronte...',
  detail: '<p>Contenuto espanso HTML</p>'
}]

// options
{
  multiOpen: false,        // default: false — una sola card aperta alla volta
  defaultOpen: 0           // indice della card aperta al caricamento (opzionale)
}
```

La card mostra badge + title + summary. Cliccando si espande a mostrare il detail. Con `multiOpen: false`, chiudere la card precedente prima di aprire la nuova. Con `multiOpen: true`, più card possono essere aperte contemporaneamente — aggiungere un pulsante globale "Espandi tutto / Comprimi tutto".

### 6.2 `ComparisonPanel(left, right, container, footer)`

Due colonne affiancate con intestazione colorata (sinistra in rosso tenue, destra in verde o viola tenue) e contenuto.

```javascript
{
  left: {
    label: 'Lettura riduttiva',    // intestazione colonna sinistra
    color: '#e74c3c',
    title: 'Il corpo come strumento',
    content: 'Testo HTML...'
  },
  right: {
    label: 'Lettura strutturale',  // intestazione colonna destra
    color: '#6c63ff',
    title: 'Il corpo come modo di essere',
    content: 'Testo HTML...'
  },
  footer: {                        // opzionale, a piena larghezza sotto le colonne
    label: 'Conseguenza operativa',
    content: 'Testo HTML...',
    color: '#6c63ff'               // colore del bordo sinistro
  }
}
```

### 6.3 `PipelineAnimator(steps, container)`

Visualizza una gerarchia o sequenza come nodi verticali collegati da frecce. Ogni step appare con animazione progressiva.

```javascript
// steps: array ordinato
[{
  id: 'a1',
  label: 'Asse 1 — Ontologico-fenomenologico',
  sublabel: 'Fondativo per tutti gli altri',
  type: 'foundation',   // foundation | axis | output
  color: '#6c63ff',
  dependsOn: []         // array di id che questo asse presuppone
}, {
  id: 'a2',
  label: 'Asse 2 — Affettivo-morale',
  sublabel: 'Presuppone Asse 1',
  type: 'axis',
  color: '#2d6a4f',
  dependsOn: ['a1']
}, ...]
```

In F1 questo componente viene usato per visualizzare la **gerarchia strutturale degli assi** (M2, M6) e lo schema di mediazione metodologica F1→F2→F3 (M7).

### 6.4 `InteractiveMatrix(rows, cols, cells, container)`

Griglia con intestazioni di riga e colonna. Cliccando su una cella si mostra il contenuto. Hover su una riga evidenzia tutta la riga; hover su una colonna evidenzia tutta la colonna.

```javascript
{
  rows: [{ id: 'a1', label: 'Asse 1 — Ontologico', color: '#6c63ff' }, ...],
  cols: [{ id: 'psicologia', label: 'Psicologia' }, { id: 'pediatria', label: 'Pediatria' }, ...],
  cells: {
    'a1-psicologia': 'Testo del concetto-ponte...',
    'a1-pediatria': 'Testo del concetto-ponte...',
    ...
  }
}
```

In F1 la matrice principale è **Assi × Discipline** (concetti-ponte per asse, M3–M6).

### 6.5 `GuardrailBadge(code, label, text, examples)`

Componente badge/callout per i guardrail metodologici. Sfondo verde scuro (`--color-guardrail-bg`), bordo sinistro spesso (`--color-guardrail`), icona scudo. In F1 esistono due varianti:

- **Variante breve**: usata in footer di slide, mostra solo code + label + prima riga di testo
- **Variante espansa**: usata nella slide dedicata (es. 1.7), mostra il testo completo + lista esempi di violazione e rispetto

```javascript
GuardrailBadge({
  code: 'G-F1',
  label: 'Guardrail fondativo — Fase 1',
  text: 'Testo principale...',
  examples: {
    violations: ['Esempio violazione 1', 'Esempio violazione 2'],
    compliant: ['Esempio corretto 1', 'Esempio corretto 2']
  },
  variant: 'compact' | 'expanded'   // default: 'compact'
})
```

### 6.6 `AnnotatedScene(sceneHtml, annotations, container)`

**Componente nuovo specifico di F1.** Visualizza il testo della scena del caso-guida con parole o frasi evidenziate cliccabili. Cliccando su una frase evidenziata, appare un pannello annotazione sotto il paragrafo corrispondente.

```javascript
// sceneHtml: stringa HTML pre-costruita con <span class="annotabile" data-annotation-id="a1">...
// Le frasi evidenziate hanno sottolineatura punteggiata in --color-accent

// annotations: array di oggetti
[{
  id: 'a1',
  estratto: 'Il bambino prende il libro',   // usato per debug, non renderizzato
  label: 'Incarnato',
  colore: '#5c35a0',
  annotazione: 'Testo dell\'annotazione...',
  asse: 'Asse 1 — Incarnazione'             // mostrato in piccolo
}]
```

**Comportamento**:
- Al caricamento: nessun pannello aperto
- Click su frase evidenziata: apre pannello con slide-down (200ms); se c'era un pannello aperto, lo chiude prima
- Il pannello appare immediatamente dopo il paragrafo che contiene la frase, non in overlay
- Click sulla stessa frase di nuovo: chiude il pannello
- Il pannello mostra: badge colorato con `label` | testo `annotazione` | `asse` in piccolo

**Costruzione dello sceneHtml**: poiché il testo del caso-guida è fisso e noto, lo sceneHtml viene pre-costruito nel file di modulo JS come stringa con i `<span>` già inseriti. Non usare ricerca/sostituzione dinamica sul testo grezzo.

---

## 7. Il caso-guida F1 (filo rosso)

Il caso-guida è un oggetto globale accessibile da tutti i moduli. In F1 la scena è identica a quella di F2, ma l'oggetto è esteso con le letture per asse e le annotazioni per il componente `AnnotatedScene`.

```javascript
window.CASO_GUIDA_F1 = {

  // --- Scena base (identica a F2) ---
  titolo: 'Lettura condivisa adulto-bambino',
  scena: `Durante un bilancio di salute, il pediatra propone per alcuni minuti
          una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi.
          È presente un genitore. Sul tavolo c'è un piccolo libro illustrato
          con immagini semplici: animali, oggetti familiari, figure umane.
          Il bambino prende il libro, lo apre, guarda alcune immagini, indica
          una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina
          l'immagine, sorride, aspetta. Il bambino torna a guardare il libro,
          gira pagina, poi mostra un'altra figura all'adulto.`,

  // --- Letture per asse: come la scena cambia con ogni lente ---
  letture_per_asse: {
    a1: {
      asse: 'Asse 1 — Ontologico-fenomenologico',
      colore: '#6c63ff',
      domanda: 'Come abita il bambino questa esperienza?',
      lettura: `Il corpo del bambino organizza l'esperienza prima di qualsiasi atto intenzionale
                esplicito: la postura orientata verso il libro, il ritmo dell'alternanza sguardo-gesto,
                la continuità della sequenza nonostante le pause — sono il modo in cui il bambino
                è presente in quel campo, non comportamenti che produce.`,
      nota_riduzione: 'Lettura riduttiva: "il bambino presta attenzione al libro". Riduce a funzione attentiva ciò che è una modalità di abitare il campo.'
    },
    a2: {
      asse: 'Asse 2 — Affettivo-morale',
      colore: '#2d6a4f',
      domanda: 'Come riconosce il bambino l\'adulto come portatore di esperienza propria?',
      lettura: `Quando il bambino indica una figura e guarda l'adulto, non sta cercando
                conferma di una prestazione: sta cercando un altro soggetto che abbia
                un'esperienza propria della stessa immagine. Il "guarda l'adulto" è un
                atto di riconoscimento dell'alterità, non un controllo sociale.`,
      nota_riduzione: 'Lettura riduttiva: "il bambino cerca approvazione". Riduce il riconoscimento dell\'alterità a bisogno di conferma.'
    },
    a3: {
      asse: 'Asse 3 — Normativo-educativo',
      colore: '#27ae60',
      domanda: 'Come emerge la capacità di orientare l\'azione secondo criteri condivisi?',
      lettura: `L'alternanza dei turni — il bambino indica, l'adulto risponde, il bambino
                riprende — non è obbedienza a una regola esterna: è l'emergenza interna di
                una normativa condivisa dello scambio. Il bambino "aspetta" la risposta
                adulta perché partecipa a una forma di scambio che ha già interni i propri criteri.`,
      nota_riduzione: 'Lettura riduttiva: "segue le regole del gioco". Riduce la normatività emergente a conformità a regole imposte.'
    },
    a4: {
      asse: 'Asse 4 — Separazione e limite reale',
      colore: '#c0392b',
      domanda: 'Come incontra il bambino la resistenza del reale?',
      lettura: `Il libro ha pagine finite, immagini che non si muovono, una sequenza
                che non è controllabile completamente dal bambino. Il bambino incontra
                il limite dell'oggetto — e lo abita: gira pagina, sceglie, torna. Il limite
                non disorganizza il campo: lo struttura.`,
      nota_riduzione: 'Lettura riduttiva: il limite non è visibile in questa scena. Questo è già un dato: una scena in cui il limite non si manifesta è diversa da una in cui si manifesta e collassa.'
    },
    a5: {
      asse: 'Asse 5 — Desiderio',
      colore: '#e67e22',
      domanda: 'Come si orienta il bambino verso possibilità che eccedono il presente?',
      lettura: `Il mostrare una nuova figura all'adulto non è ripetizione: è apertura verso
                una nuova possibilità di scambio. Il bambino non è saturo: ha una direzione,
                un'iniziativa, un orientamento che eccede la situazione presente. Il desiderio
                si vede nella sequenza — non in un singolo atto.`,
      nota_riduzione: 'Lettura riduttiva: "il bambino è interessato al libro". Riduce la direzione dell\'esperienza a preferenza per uno stimolo.'
    },
    a6: {
      asse: 'Asse 6 — Rapporto con il mondo storico-culturale',
      colore: '#d35400',
      domanda: 'Come entra il bambino nella partecipazione al mondo condiviso?',
      lettura: `Il libro illustrato non è uno stimolo visivo o un task cognitivo: è un oggetto
                storico-culturale che porta con sé pratiche, convenzioni, storie condivise.
                Il bambino non sta guardando immagini — sta entrando in un modo di stare con
                l'adulto che ha la forma della cultura: indicare, nominare, condividere significati.`,
      nota_riduzione: 'Lettura riduttiva: "il bambino riconosce le immagini". Riduce la partecipazione culturale a capacità di riconoscimento percettivo.'
    }
  },

  // --- Annotazioni per il componente AnnotatedScene ---
  annotazioni: [
    {
      id: 'a1',
      estratto: 'Il bambino prende il libro',
      label: 'Incarnato',
      colore: '#5c35a0',
      annotazione: 'Il prendere non è l\'esecuzione di un compito motorio: è il modo incarnato in cui il bambino si orienta verso l\'oggetto. Il corpo organizza l\'intenzione prima che ci sia un\'intenzione esplicita.',
      asse: 'Asse 1 — Ontologico-fenomenologico'
    },
    {
      id: 'a2',
      estratto: 'indica una figura, vocalizza qualcosa e guarda l\'adulto',
      label: 'Relazionale',
      colore: '#1a6b8a',
      annotazione: 'L\'azione si completa solo nel campo: indicare, vocalizzare e guardare l\'adulto non sono tre comportamenti separati — sono un unico atto relazionale che ha senso solo se c\'è un campo disponibile a riceverlo.',
      asse: 'Relazionale — il campo come condizione'
    },
    {
      id: 'a3',
      estratto: 'Il genitore nomina l\'immagine, sorride, aspetta',
      label: 'Campo come condizione',
      colore: '#2d6a4f',
      annotazione: 'Il "aspetta" del genitore non è passività: è la forma in cui il campo si rende disponibile a ricevere l\'iniziativa del bambino. Senza questa disponibilità strutturale, il gesto del bambino cambia significato.',
      asse: 'Asse 2 — Riconoscimento dell\'alterità'
    },
    {
      id: 'a4',
      estratto: 'Il bambino torna a guardare il libro, gira pagina',
      label: 'Temporale',
      colore: '#d35400',
      annotazione: 'La sequenza ha continuità: dopo la risposta dell\'adulto, il bambino prosegue la traiettoria — non ricomincia da zero. Il tornare al libro è il filo temporale dell\'esperienza che si mantiene attraverso l\'interruzione dello scambio.',
      asse: 'Temporale — traiettoria aperta'
    },
    {
      id: 'a5',
      estratto: 'poi mostra un\'altra figura all\'adulto',
      label: 'Direzione',
      colore: '#e67e22',
      annotazione: 'Il mostrare una nuova figura non è ripetizione: è la direzione della traiettoria che si apre. Il bambino ha un orientamento che eccede la situazione presente — e lo porta verso il campo condiviso.',
      asse: 'Asse 5 — Desiderio come direzione'
    }
  ],

  // --- Letture comparative per slide di confronto ---
  lettura_riduttiva: `"Il bambino di 20 mesi mostra competenze linguistiche nella norma:
    indica, vocalizza, usa il gesto di pointing. Attenzione sostenuta adeguata all'età.
    Il genitore stimola adeguatamente."`,

  lettura_ontologica: `"Il campo relazionale è disponibile alla risposta: bambino e adulto
    costruiscono uno scambio attorno a un oggetto comune. Il bambino apre l'interazione
    e l'adulto la sostiene senza dirigerla. La configurazione è evolutivamente aperta."`,

  chip_riduttivi: [
    { label: 'prestazionale', color: '#e74c3c' },
    { label: 'normativa', color: '#e67e22' },
    { label: 'individua il bambino come unità', color: '#c0392b' }
  ],

  chip_ontologici: [
    { label: 'configurazionale', color: '#6c63ff' },
    { label: 'relazionale', color: '#2d6a4f' },
    { label: 'descrive il campo', color: '#27ae60' }
  ],

  // --- Guardrail fondativo ---
  guardrail: {
    code: 'G-F1',
    label: 'Guardrail fondativo — Fase 1',
    text: 'Ogni output derivato da questo framework deve poter essere usato senza descrivere il bambino come individuo isolato. Se una descrizione ha senso solo riferita al bambino separato dal campo, è metodologicamente scorretta rispetto ai fondamenti del progetto.',
    esempi_violazione: [
      '"Il bambino ha un vocabolario di X parole." — Separa la prestazione linguistica dal campo in cui il linguaggio emerge.',
      '"Il bambino è poco collaborativo." — Attribuisce un tratto stabile all\'individuo senza leggere la configurazione relazionale.',
      '"Sviluppo cognitivo nella norma." — Isola una funzione dal soggetto incarnato che la vive in un campo specifico.'
    ],
    esempi_rispetto: [
      '"In questa situazione, il campo permette al bambino di condividere un oggetto simbolico con l\'adulto."',
      '"La sequenza di scambio si mantiene quando l\'adulto risponde in modo non direttivo."',
      '"La regolazione dell\'esperienza dipende fortemente dalla presenza adulta: non è ancora autosufficiente."'
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
- BEM leggero per i componenti: `.slide__header`, `.card--expanded`, `.annotabile--active`
- Nessuno stile inline nel JS (eccetto variabili CSS dinamiche con `el.style.setProperty`)
- Mobile-first per le media query (anche se il corso è ottimizzato per desktop 1280px+)
- I colori degli assi (`--color-a1` … `--color-a6`) devono essere usati coerentemente in tutte le slide che citano un asse specifico

### HTML
- Markup semantico: `<section>`, `<article>`, `<nav>`, `<main>`
- Attributi `data-*` per i riferimenti JS: `data-slide`, `data-module`, `data-axis`, `data-annotation-id`
- `aria-label` e ruoli accessibili sui componenti interattivi
- Le frasi annotabili nella scena del caso-guida usano `<span class="annotabile" data-annotation-id="aX">`

---

## 9. Come aggiungere un nuovo modulo

1. Crea `js/modules/mXX.js` con la struttura `ModuleXX` descritta nella §5
2. Importa il file in `index.html` con `<script src="js/modules/mXX.js">`
3. Registra il modulo in `app.js` nell'array `MODULES`: `[Module00, Module01, ..., Module07]`
4. Il router gestisce automaticamente la navigazione e il rendering

Non modificare `index.html`, `style.css` o `app.js` per contenuti specifici del modulo.

---

## 10. Ordine di costruzione

Il piano completo prevede 8 moduli. Lavora in questo ordine:

| Priorità | Modulo | File contenuto | Note implementative |
|----------|--------|---------------|---------------------|
| 1 | M0 — Orientamento | `f1-modulo-00.md` | Prima il layout generale e la shell. Stabilisce il componente `AnnotatedScene` in forma semplice |
| 2 | M1 — Il soggetto | `f1-modulo-01.md` | Componente `ExpandableCards` (tre immagini del bambino), `ComparisonPanel`, `AnnotatedScene` completo |
| 3 | M2 — Gli assi | `f1-modulo-02.md` | `PipelineAnimator` per gerarchia assi, `InteractiveMatrix` semplificata |
| 4 | M3 — Asse 1 | `f1-modulo-03.md` | `ExpandableCards` per contesti professionali, `InteractiveMatrix` concetti-ponte |
| 5 | M4 — Assi 2 e 3 | `f1-modulo-04.md` | `ComparisonPanel` e `ExpandableCards` |
| 6 | M5 — Assi 4 e 5 | `f1-modulo-05.md` | `ComparisonPanel` per le coppie limite/desiderio |
| 7 | M6 — Asse 6 | `f1-modulo-06.md` | `PipelineAnimator` per gerarchia completa, `AnnotatedScene` estesa |
| 8 | M7 — Epistemologia | `f1-modulo-07.md` | `PipelineAnimator` mediazione F1→F2→F3, `GuardrailBadge` espanso per asse |

**Quando inizi un modulo**: leggi il file `f1-modulo-XX.md` corrispondente per il contenuto esatto delle slide.

---

## 11. Note metodologiche importanti

Queste regole emergono dalla Fase 1 del metodo e devono riflettersi nel design di ogni slide.

### 11.1 Regole fondamentali

1. **Il soggetto grammaticale è sempre il campo, non il bambino**
   Nelle slide che descrivono configurazioni evolutive, il soggetto grammaticale non è mai "il bambino" isolato: è sempre "il campo", "la configurazione", "la relazione". Esempi: non "il bambino regola l'esperienza" → "il campo permette la regolazione dell'esperienza"; non "il bambino indica" → "il gesto apre verso il campo condiviso".

2. **Gli assi non si misurano: orientano**
   Nessun elemento visivo — tabella, grafico, indicatore — deve suggerire che gli assi siano variabili su una scala o che abbiano soglie normative. Gli assi sono strutture interpretative, non variabili empiriche. Se ci sono scale o indicatori di stato, questi riguardano la *configurazione* (come in F2), non l'asse in sé.

3. **La gerarchia è strutturale, non valutativa**
   La gerarchia degli assi (Asse 1 fonda tutti gli altri) indica dipendenza logica — non importanza, non priorità clinica, non sequenza temporale di sviluppo. Nel design: la gerarchia si visualizza con frecce di dipendenza, non con dimensioni diverse o colori di "importanza".

4. **Nessun asse appartiene a una sola disciplina**
   Nelle slide che contestualizzano gli assi nei linguaggi professionali, ogni asse attraversa sempre almeno due discipline. Nessun elemento visivo deve associare un asse esclusivamente a pediatria, o a psicologia, o a pedagogia.

5. **La riluminazione della scena non aggiunge contenuto**
   Il caso-guida è sempre la stessa scena. Quando la scena viene riluminata da una lente diversa, **non si aggiunge informazione alla scena**: si cambia la domanda con cui la si guarda. Il design deve rendere evidente che la scena non cambia — le annotazioni e le letture sono sovrapposizioni, non modifiche.

6. **Il tono è espositivo, non prescrittivo**
   Le slide descrivono; non dicono cosa fare. Anche nelle slide che mostrano "errori da evitare", il tono rimane espositivo: si mostra cosa si perde con una lettura riduttiva, non si dice al professionista cosa deve pensare.

### 11.2 Distinzioni visive critiche

| Concetto | Visualizzazione corretta | Da evitare |
|----------|------------------------|-----------|
| Gerarchia degli assi | Frecce di dipendenza logica | Dimensioni diverse, colori graduati di "importanza" |
| Asse attivo in una slide | Badge colorato `--color-aX` | Indicatore numerico, percentuale, livello |
| Lettura riduttiva | Box rosso tenue, testo normale | Icona ❌ grande o linguaggio censorio |
| Lettura strutturale | Box verde o viola tenue | Icona ✓ grande o linguaggio celebrativo |
| Campo relazionale | Sempre incluso nell'illustrazione | Bambino isolato senza adulto/contesto |
| Guardrail | Badge verde `G-F1`, tono neutro | Avvertimento, triangolo di pericolo |

### 11.3 La scena del caso-guida in F1

La scena deve essere citata testualmente da `window.CASO_GUIDA_F1.scena` — mai duplicata o parafrasata nel codice del modulo. Nelle slide narrative, il testo appare in corsivo su sfondo `--color-primary-light` con bordo sinistro `--color-primary`.

Nelle slide di confronto (lettura riduttiva vs. lettura strutturale), usare:
- `window.CASO_GUIDA_F1.lettura_riduttiva` e `window.CASO_GUIDA_F1.lettura_ontologica`
- I chip da `chip_riduttivi` e `chip_ontologici`

Nelle slide con `AnnotatedScene`, usare:
- `window.CASO_GUIDA_F1.annotazioni` come array di annotazioni
- Lo `sceneHtml` pre-costruito nel file di modulo JS (non in `app.js`)

---

*Fine istruzioni. Per il contenuto metodologico di ogni slide, fare riferimento ai file `f1-modulo-XX.md` nella stessa cartella.*
