# f3-modulo-08 — Pipeline F3 completa
**Numero slide**: 7
**Colore accent**: `#1a6b8a`
**Tipo prevalente**: narrative + diagram + interactive

---

## Dati globali del modulo

M8 è il modulo capstone: non introduce nuovi dati né nuove costanti proprie. Tutte le costanti vengono da `window.CASO_GUIDA_F3` (definito in `app.js`) e dai moduli precedenti, richiamati nella forma sintetica appropriata a una visione d'insieme.

Definire in `m08.js` una sola costante di servizio per la pipeline completa, che aggrega i riferimenti:

```javascript
// Aggregato di riferimento per la pipeline completa del caso-guida
// Non ridefinisce dati: li raccoglie dai sorgenti già esistenti
const PIPELINE_CASO_GUIDA = {

  // ─── Step 0: Scena osservata ────────────────────────────────────────────
  scena: window.CASO_GUIDA_F3.scena,
  scenaTitolo: window.CASO_GUIDA_F3.titolo,

  // ─── Step 1: CE prodotta ────────────────────────────────────────────────
  ce: window.CASO_GUIDA_F3.ce,

  // ─── Step 2: Nodo dominante ─────────────────────────────────────────────
  nodoDominante: window.CASO_GUIDA_F3.f3.nodoDominante,
  nodoSostegno:  window.CASO_GUIDA_F3.f3.nodoSostegno,
  nodoInTensione: window.CASO_GUIDA_F3.f3.nodoInTensione,

  // ─── Step 3: Funzione ────────────────────────────────────────────────────
  funzione:        window.CASO_GUIDA_F3.f3.funzione,
  funzioneColore:  window.CASO_GUIDA_F3.f3.funzioneColore,
  funzioneDescrizione: window.CASO_GUIDA_F3.f3.funzioneDescrizione,

  // ─── Step 4: Template F3 ─────────────────────────────────────────────────
  campoBersaglio:       window.CASO_GUIDA_F3.f3.campoBersaglio,
  microAzioni:          window.CASO_GUIDA_F3.f3.microAzioni,
  tempoReale:           window.CASO_GUIDA_F3.f3.tempoReale,
  indicatoreRisonanza:  window.CASO_GUIDA_F3.f3.indicatoreRisonanza,

  // ─── Step 5: Tipo universale ─────────────────────────────────────────────
  tipoUniversale:          window.CASO_GUIDA_F3.f3.tipoUniversale,
  tipoUniversaleNome:      window.CASO_GUIDA_F3.f3.tipoUniversaleNome,
  tipoUniversaleMotivazione: window.CASO_GUIDA_F3.f3.tipoUniversaleMotivazione,

  // ─── Step 6: Verifica e output-tipo ──────────────────────────────────────
  verificaCoerenza: window.CASO_GUIDA_F3.f3.verificaCoerenza,
  outputTipo:       window.CASO_GUIDA_F3.f3.outputTipo,

  // ─── Logica decisionale (D1–D4) ─────────────────────────────────────────
  logicaDecisionale: window.CASO_GUIDA_F3.f3.logicaDecisionale,

  // ─── Guardrail ──────────────────────────────────────────────────────────
  guardrail: window.CASO_GUIDA_F3.guardrail
};
```

---

## SLIDE F3.8.1 — Dall'inizio

**Tipo**: `narrative`
**Titolo**: Ripartiamo dalla scena
**Sottotitolo**: Tutto quello che abbiamo imparato — in una scena di cinque minuti

**Contenuto principale**:

Layout a colonna singola. Slide di apertura capstone: nessun concetto nuovo, solo il riposizionamento del partecipante prima del percorso completo.

**Sezione superiore — la scena del caso-guida**:

Card narrativa (sfondo `--color-primary-light`, bordo sinistro spesso `--color-primary`, testo in corsivo):

Testo da `window.CASO_GUIDA_F3.scena` — **citare testualmente, non parafrasare.**

**Sezione centrale — la stessa scena, tre fasi**:

Schema orizzontale a tre blocchi con frecce:

```
[F1 — Fondazione]  →  [F2 — CE]  →  [F3 — Dispositivo]
  Sei assi ontologici     N1~ N2↑ N3~     MEDIAZIONE
  Come leggere il         N4↓, R, D↗      U2 + U4
  soggetto nel campo      T2, A±          Template compilato
```

Ogni blocco ha il colore della fase (`--color-f1`, `--color-f2`, `--color-f3`). Il blocco F3 ha sfondo tenue `--color-accent-light` per segnalare che è il focus di questo corso.

Testo sotto lo schema, `--text-sm` `--color-text-muted` centrato:
*Questa scena è stata lavorata tre volte. Ogni fase ha aggiunto uno strato di lettura. Adesso la percorriamo in F3 dall'inizio alla fine — senza fermarci.*

**Sezione inferiore — cosa fa M8**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*M8 non introduce nuovi concetti. Percorre la pipeline F3 completa applicata al caso-guida: sette passi, dal campo osservato al micro-dispositivo contestualizzato.*

*Ogni slide di M8 corrisponde a un passo della pipeline. Al termine, il caso-guida è completo — e la pipeline è percorribile mentalmente su qualsiasi nuovo caso.*

Schema pipeline ridotta orizzontale (sette chip con frecce):
`[Scena] → [CE] → [Nodo dom.] → [Funzione] → [Template] → [Tipo U] → [Verifica]`

---

## SLIDE F3.8.2 — Passo 1–2: dal campo alla CE

**Tipo**: `diagram`
**Titolo**: Osservare e leggere
**Sottotitolo**: Dall'osservazione della scena alla Configurazione Evolutiva

**Contenuto principale**:

Layout a due aree: sinistra l'osservazione, destra la CE con `CEDisplay`. La slide comprime M1 e M2 in una sola vista.

**Area sinistra** (40%) — "Cosa si osserva nel campo":

Titolo area: *"Passo 1 — Osservare"* con chip numerato `①` `--color-accent`.

Tre elementi osservati nella scena, in lista ordinata:

1. *Il bambino orienta il libro verso l'adulto, indica immagini, vocalizza e cerca lo sguardo.*
2. *Il genitore risponde con nome, sorriso, attesa. Il campo relazionale è attivo.*
3. *La sequenza si interrompe: il bambino non mantiene il filo del ciclo condiviso.*

Sotto la lista, box sfondo `--color-bg`, bordo `--color-border`:
*Lettura immediata: il campo non è in collasso (T non è T0). C'è scambio. Ma la sequenza condivisa si esaurisce prima di consolidarsi.*

**Area destra** (60%) — "CE prodotta":

Titolo area: *"Passo 2 — Leggere (CE)"* con chip numerato `②` `--color-accent`.

`CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N2', 'N3', 'N4'], compact: false })`

Sotto la CE, tre righe di lettura F3 in `--text-sm`:

- **Risorsa attiva**: *N2↑ — il campo relazionale regge. Base di lavoro disponibile.*
- **Zona di movimento**: *N3~ — accesso al mondo condiviso in transizione. R: N2→N3.*
- **Nodo in tensione**: *N4↓ — esplorazione ridotta. Non è il target in questo contesto.*

**Connettivo visivo**: freccia grande tra le due aree con etichetta `F2 → F3`.

**Nota in footer**:
*La CE è l'output di F2, l'input di F3. In questo corso la CE era già disponibile dall'inizio — nella pratica professionale, questo passaggio richiede l'applicazione dell'operatore triadico F2.*

---

## SLIDE F3.8.3 — Passo 3–4: nodo dominante e funzione

**Tipo**: `standard`
**Titolo**: Identificare e orientare
**Sottotitolo**: Dal nodo dominante alla funzione dell'azione

**Contenuto principale**:

Layout a due aree verticali (non colonne: impilate con spazio tra loro). La slide comprime M3 e M4.

**Area superiore** — "Passo 3 — Nodo dominante":

Titolo area con chip `③` `--color-accent`.

Layout orizzontale a tre blocchi:

**Blocco N3** (bordo spesso `var(--color-n3)`, sfondo tenuissimo):
Badge grande `N3 Mondo condiviso` colore `var(--color-n3)`.
Etichetta: `NODO DOMINANTE`.
Testo `--text-sm`:
*La sua apertura muove il campo verso D↗.*
*R: N2→N3 indica che la transizione è già in corso.*
*Attivare N3 produce il cambiamento più rilevante per l'abitabilità del campo.*

**Blocco N2** (bordo `var(--color-n2)`, sfondo tenuissimo, dimensione minore):
Badge `N2 Campo relazionale` colore `var(--color-n2)`.
Etichetta: `NODO DI SOSTEGNO`.
Testo `--text-sm`:
*N2↑ è la risorsa su cui si appoggia il dispositivo. Senza co-regolazione attiva l'accesso a N3 non si produce.*

**Blocco N4** (bordo `var(--color-n4)` tratteggiato, sfondo tenuissimo, dimensione minore):
Badge `N4 Apertura` colore `var(--color-n4)`.
Etichetta: `NODO IN TENSIONE`.
Testo `--text-sm`:
*N4↓ è il nodo limitante secondario. Non è il target: il bilancio non è il contesto per lavorare l'esplorazione. Va tenuto presente: non sovraccaricare il campo.*

**Area inferiore** — "Passo 4 — Funzione":

Titolo area con chip `④` `--color-accent`.

Layout a tre chip di sequenza decisionale:

```
[T2 · A±  →  campo regge]   →   [R: N2→N3 · D↗  →  transizione in corso]   →   [MEDIAZIONE]
   Passo ① non STA/PRO              Passo ② → MED                              badge MED grande
```

Ogni chip ha colore semantico: i primi due `--color-text-muted`, l'ultimo `var(--color-fn-mediare)` con dimensione aumentata.

Sotto il chip MEDIAZIONE, testo `--text-sm` `--color-fn-mediare`:
*Sostenere la transizione N2→N3 già in corso — non avviarla, non ampliarla, non stabilizzare un campo che non è in crisi.*

---

## SLIDE F3.8.4 — Passo 5: il template F3

**Tipo**: `standard`
**Titolo**: Costruire il dispositivo
**Sottotitolo**: Il Template F3 del caso-guida compilato

**Contenuto principale**:

Layout a colonna singola. Il Template F3 compilato in forma densa ma leggibile — tutti i sette campi visibili contemporaneamente. La slide non usa il F3Builder interattivo (già presente in M5): qui il template è in forma statica per una lettura complessiva.

**Chip intestazione**:

Riga di chip affiancati che mostrano la catena:
`[CE] → [N3 nodo dom.] → [MED funzione] → [Template F3]`

**Template compilato** — sette righe verticali in una griglia `label | valore`:

```
┌────────────────────┬────────────────────────────────────────────┐
│  CE di origine     │  [window.CASO_GUIDA_F3.ce.grammaticale]    │
├────────────────────┼────────────────────────────────────────────┤
│  Nodo dominante    │  N3 — Accesso al mondo condiviso simbolico  │
├────────────────────┼────────────────────────────────────────────┤
│  Funzione          │  [badge MED Mediazione colore fn-mediare]   │
├────────────────────┼────────────────────────────────────────────┤
│  Campo bersaglio   │  [window.CASO_GUIDA_F3.f3.campoBersaglio]  │
├────────────────────┼────────────────────────────────────────────┤
│  Micro-azioni      │  1. [microAzioni[0]]                        │
│  (lista ordinata)  │  2. [microAzioni[1]]                        │
│                    │  3. [microAzioni[2]]                        │
│                    │  4. [microAzioni[3]]                        │
│                    │  5. [microAzioni[4]]                        │
├────────────────────┼────────────────────────────────────────────┤
│  Tempo reale       │  [window.CASO_GUIDA_F3.f3.tempoReale]      │
├────────────────────┼────────────────────────────────────────────┤
│  Indicatore        │  [window.CASO_GUIDA_F3.f3.indicatoreRisonanza] │
│  di risonanza      │                                             │
└────────────────────┴────────────────────────────────────────────┘
```

La colonna label usa `--text-sm` grassetto `--color-text-secondary`. La colonna valore usa `--text-sm` `--color-text`. La riga Funzione ha la cella valore con sfondo `var(--color-fn-mediare)` tenuissimo. La riga Micro-azioni è più alta delle altre — le cinque voci si impilano verticalmente nella cella.

**Sezione inferiore — il tipo universale**:

Due chip affiancati grandi:
`[U2 Sintonizzazione]` colore `var(--color-u2)` + `[U4 Mediazione Simbolica]` colore `var(--color-u4)`

Sotto i chip, testo `--text-sm` `--color-text-secondary`:
*Il dispositivo esprime U2 perché segue il bambino senza dirigerlo, e U4 perché usa il libro come mediatore simbolico dell'incontro.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-80`
- Label: Il template descrive il campo — non il bambino
- Testo: *Ogni voce del template ha come soggetto il campo relazionale o l'adulto. "Il bambino deve..." non compare: non è la grammatica di F3.*

---

## SLIDE F3.8.5 — Passo 6: verifica e output-tipo

**Tipo**: `standard`
**Titolo**: Verificare la coerenza
**Sottotitolo**: Il dispositivo rispetta il perimetro metodologico di F3?

**Contenuto principale**:

Layout a due colonne. Sinistra la verifica di coerenza (5 domande), destra l'output-tipo (5 sezioni A–E) in forma compatta. La slide comprime M5 in una vista sintetica.

**Colonna sinistra** (45%) — "Verifica di coerenza":

Titolo con chip `⑥a` `--color-accent`.

Cinque righe compatte (non i blocchi espansi di M5 — qui la forma è sintetica):

Ogni riga: `[✓ verde]` + sintesi brevissima da `window.CASO_GUIDA_F3.f3.verificaCoerenza[i].check` + nota brevissima `--text-xs` `--color-text-muted`.

Sotto le cinque righe, testo `--text-sm` `--color-valid`:
*Tutte le domande di verifica ricevono risposta affermativa. Il dispositivo è coerente con il perimetro metodologico di F3.*

**Colonna destra** (55%) — "Output-tipo compilato":

Titolo con chip `⑥b` `--color-accent`.

Cinque sezioni A–E in forma compatta. Ogni sezione:
- Lettera `[A]`…`[E]` in badge colorato `--color-accent`, dimensione `--text-base`
- Testo da `window.CASO_GUIDA_F3.f3.outputTipo.A`…`.E` in `--text-xs`, corsivo
- Divisore sottile tra le sezioni

La sezione E ha bordo sinistro più spesso `--color-accent`: è l'ipotesi operativa, l'esito di tutta la lettura.

**Sezione inferiore a piena larghezza** — il nesso tra le due colonne:

Box sfondo `--color-bg`, bordo `--color-border`:

*La verifica di coerenza assicura che il dispositivo sia nel perimetro F3.*
*L'output-tipo trasforma la lettura del campo in un documento condivisibile tra professionisti.*
*I due strumenti non si sostituiscono: il primo verifica l'azione, il secondo descrive il campo.*

---

## SLIDE F3.8.6 — La pipeline completa: vista d'insieme

**Tipo**: `diagram`
**Titolo**: Tutto insieme
**Sottotitolo**: La pipeline F3 del caso-guida — dall'osservazione al dispositivo

**Contenuto principale**:

`PipelineAnimator(PIPELINE_F3, container, { mode: 'caso', initialOpacity: 1.0 })` — la pipeline completa da `PIPELINE_F3` (definita in M2, richiamata qui) con tutti gli step visibili, in modalità `caso` (con i dati reali del caso-guida).

**Differenza rispetto a M2**: in M2 la pipeline era mostrata in modalità astratta e poi in modalità caso separatamente. In M8 compare solo in modalità caso, con tutti i sei step visibili dall'inizio (non animati progressivamente) — la slide è una vista d'insieme, non una scoperta.

**Ogni step nella modalità `caso`** mostra:
- Label + sublabel (come in M2)
- Box dati reali aggiunto sotto il sublabel, sfondo `--color-bg`, bordo `--color-border`:
  - Step `ce`: grammaticale della CE
  - Step `nodo-dominante`: "N3 — Accesso al mondo condiviso simbolico"
  - Step `funzione`: badge `MED Mediazione`
  - Step `dispositivo`: campo bersaglio + "5 micro-azioni · 5 minuti · U2+U4"

**Sotto la pipeline** — tre proprietà di riepilogo:

Tre chip affiancati, sfondo `--color-bg`, bordo `--color-accent`:
- `Breve` — *5 minuti nel bilancio*
- `Integrabile` — *nella scena già in corso, senza ristrutturarla*
- `Osservabile` — *indicatore di risonanza presente/assente in tempo reale*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-81`
- Label: La pipeline è un orientamento, non un algoritmo
- Testo: *I sei passi non sono sempre percorsi nell'ordine esatto. In contesti di alta instabilità (T0), il ciclo si comprime: si osserva, si stabilizza, si osserva di nuovo. La pipeline descrive la logica del metodo — non prescrive una sequenza temporale rigida.*

---

## SLIDE F3.8.7 — Il campo continua

**Tipo**: `narrative`
**Titolo**: Cosa rimane dopo F3
**Sottotitolo**: Chiusura del corso

**Contenuto principale**:

Layout a colonna singola. Slide di chiusura del corso intero — non solo di M8. Ariosa, poco testo, molto respiro visivo.

**Sezione superiore — il percorso compiuto**:

Schema a tre fasi (identico nella struttura al diagramma F1→F2→F3 di M0, ma in forma retrospettiva):

```
[F1]           [F2]           [F3]
Fondazione     Traduzione     Strumenti
Ontologica     Interdiscipl.  Operativi
               ↓
         [Campo osservato]
               ↓
         [CE prodotta]
               ↓
         [Micro-dispositivo]
               ↓
         [Campo aggiornato]
```

Tutti e tre i blocchi fase sono attivi (non opachi). La freccia discendente non è una pipeline: è un ciclo abbreviato — l'ultima freccia (`Campo aggiornato`) torna visivamente verso il blocco F1 con una curva, indicando che il processo ripartirà su un campo nuovo.

**Sezione centrale — tre cose che restano**:

Tre blocchi verticali, sfondo `--color-surface`, separati da spazio:

**Blocco 1**:
*Un vocabolario.*
*CE, nodo dominante, funzione, tipo universale: non sono concetti da memorizzare — sono parole per descrivere ciò che accade nel campo relazionale in modo comunicabile tra professionisti.*

**Blocco 2**:
*Una struttura di domande.*
*D1–D4 e il Ciclo Decisionale Breve non prescrivono cosa fare: orientano l'attenzione verso il punto del campo in cui un'azione minima può produrre il cambiamento più rilevante.*

**Blocco 3**:
*Un principio.*
*Lo strumento non corregge il bambino: modifica il campo relazionale di esperienza.*
*Questo principio non è etico — è metodologico. Emerge dall'Asse 1 di F1 e attraversa tutte e tre le fasi.*

**Sezione inferiore — la chiusura**:

Blockquote centrato, bordo sinistro `--color-f3`, testo `--text-xl`:

> *"Ogni nuova scena può diventare una CE.*
> *Ogni CE può diventare un dispositivo.*
> *Ogni dispositivo può tornare a essere osservazione."*

Sotto, in `--text-sm` `--color-text-muted` centrato, spazio bianco ampio sopra:

*Il caso-guida finisce qui. Il campo — no.*

**Elemento finale** — firma del corso:

Tre badge affiancati: `F1` colore `--color-f1` · `F2` colore `--color-f2` · `F3` colore `--color-f3`

Con testo sotto in `--text-xs` `--color-text-muted`:
*Fondazione Ontologica · Traduzione Interdisciplinare · Strumenti Operativi Contestualizzati*

---

## Note per l'implementazione

### M8 come modulo di riepilogo

M8 non ha JS constants proprie sostanziali: aggrega dati già esistenti in `window.CASO_GUIDA_F3`. La costante `PIPELINE_CASO_GUIDA` serve solo come punto di raccolta locale per rendere il codice del modulo leggibile — evita di scrivere `window.CASO_GUIDA_F3.f3.microAzioni` ripetutamente nelle slide. Non aggiunge dati.

### Slide F3.8.2 — CEDisplay in M8

`CEDisplay` in M8 è chiamata con le stesse opzioni del suo utilizzo più denso in M3. Highlights: `['N2', 'N3', 'N4']` — i tre nodi narrativamente rilevanti (sostegno, dominante, tensione). La funzione è già stabile da M2: nessuna nuova configurazione necessaria.

### Slide F3.8.4 — Template statico vs. F3Builder

Il template compilato in F3.8.4 è **statico** (HTML tabella), non il F3Builder interattivo di M5. La distinzione è intenzionale: M5 mostra la costruzione del template (processo), M8 mostra il template come risultato (prodotto). Implementare come `<table class="template-table">` con `<tr>` per ogni campo. I valori sono letti da `PIPELINE_CASO_GUIDA` — mai hardcodati come stringhe letterali nel markup.

### Slide F3.8.6 — PipelineAnimator in modalità caso

La chiamata corretta è:

```javascript
// In onEnter della slide F3.8.6
const container = document.querySelector('#pipeline-full-container');
PipelineAnimator(PIPELINE_F3, container, {
  mode: 'caso',
  initialOpacity: 1.0,        // tutti i nodi visibili subito
  showCaseData: true,         // mostra i box dati reali sotto ogni step
  caseData: PIPELINE_CASO_GUIDA  // sorgente dati reali
});
```

Il parametro `showCaseData` è nuovo rispetto all'uso di M2 e M8 — aggiornare la firma di `PipelineAnimator` in `app.js` per gestirlo. Quando `showCaseData: true`, ogni step aggiunge un `<div class="pipeline-node__case-data">` con il dato reale corrispondente.

### Slide F3.8.7 — Diagramma finale F1→F2→F3

Il diagramma finale riprende quello di M0 (slide F3.0.2) ma in forma retrospettiva: tutti i blocchi attivi, colori pieni. Riutilizzare lo stesso componente CSS — cambiare solo la classe da `.phase-diagram--f3-active` a `.phase-diagram--all-active`. Nessun nuovo SVG: è una variante del diagramma già costruito.

### Coerenza del caso-guida attraverso i moduli

M8 è l'unico modulo che cita esplicitamente tutti i dati del caso-guida insieme. Prima di implementare, verificare che `window.CASO_GUIDA_F3` sia correttamente definito in `app.js` con tutti i campi usati in M8 (in particolare `f3.microAzioni`, `f3.outputTipo`, `f3.verificaCoerenza`, `f3.logicaDecisionale`). Se durante lo sviluppo dei moduli precedenti alcuni campi fossero stati modificati, M8 è il punto di verifica della coerenza complessiva.

### Chiusura del corso

La slide F3.8.7 chiude il corso F3 ma non chiude il percorso HCAIRE — F1 e F2 esistono come applicazioni separate. Se in futuro le tre applicazioni venissero integrate in un'unica shell, la slide finale di M8 potrebbe linkare alla home comune. Per ora, la chiusura è autonoma.
