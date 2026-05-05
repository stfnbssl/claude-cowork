# Modulo 6 — La Grammatica delle Configurazioni

**Accent color**: `#16a085`  
**Slides**: 7  
**Obiettivo**: Far comprendere la CE come unità grammaticale — come si costruisce, come si legge, cosa descrive e cosa non descrive. Il modulo culmina nel CEBuilder interattivo e si chiude con la soglia verso F3.

---

## JS Data (costanti del modulo)

```javascript
// --- CINQUE_DIMENSIONI ---
// Usato nella slide 6.2 (accordion/card interattivo)
const CINQUE_DIMENSIONI = [
  {
    codice: 'S',
    nome: 'Stato dei nodi',
    sottotitolo: 'Come stanno funzionando i nodi in questo momento',
    descrizione: 'Lo stato non è un punteggio e non è permanente. Descrive il modo in cui ciascun Nodo Trasversale si manifesta nel campo osservato. Non riguarda il bambino in sé, ma la qualità della sua esperienza nel contesto.',
    opzioni: [
      { codice: '↑', etichetta: 'Espansivo', colore: '#27ae60', note: 'Il nodo si esprime con piena disponibilità nel campo' },
      { codice: '~', etichetta: 'Stabile',   colore: '#2980b9', note: 'Il nodo è funzionante ma non in fase espansiva' },
      { codice: '↓', etichetta: 'Ristretto', colore: '#e67e22', note: 'Il nodo mostra contrazione o ridotta espressione' },
      { codice: '!', etichetta: 'Disorganizzato', colore: '#e74c3c', note: 'Il nodo perde coerenza interna; segnale di attenzione' },
      { codice: '?', etichetta: 'Non leggibile', colore: '#95a5a6', note: 'Insufficiente osservazione per descrivere lo stato' }
    ],
    esempio: 'N1~ N2↑ N3~ N4↓ N5~ N6~ N7~',
    colore: '#16a085'
  },
  {
    codice: 'R',
    nome: 'Relazioni dominanti',
    sottotitolo: 'Come i nodi interagiscono tra loro nel campo',
    descrizione: 'Non tutti i nodi hanno lo stesso peso in ogni configurazione. La dimensione R identifica le relazioni strutturalmente attive — quelle che organizzano il funzionamento complessivo del campo. Una CE può avere una o più relazioni dominanti.',
    opzioni: [
      { codice: 'CPL', etichetta: 'Sostegno',     colore: '#27ae60', note: 'Un nodo espansivo amplifica la disponibilità di un altro' },
      { codice: 'VIN', etichetta: 'Vincolo',       colore: '#e74c3c', note: 'Un nodo ristretto limita l\'espressione di un altro' },
      { codice: 'MED', etichetta: 'Mediazione',    colore: '#2980b9', note: 'Un nodo orienta e traduce l\'attività di un altro' },
      { codice: 'CMP', etichetta: 'Compensazione', colore: '#e67e22', note: 'Un nodo stabile bilancia la fragilità di un altro' }
    ],
    esempio: 'N2→N3 (MED), N7→N3 (CPL), N2→N1 (CMP)',
    colore: '#2980b9'
  },
  {
    codice: 'D',
    nome: 'Direzione dinamica',
    sottotitolo: 'La traiettoria evolutiva del campo',
    descrizione: 'La direzione non descrive un miglioramento o un peggioramento: descrive il movimento della configurazione nel tempo osservato. Una configurazione ↘ può essere gestibile; una ↗ può essere fragile. Dipende dal campo.',
    opzioni: [
      { codice: '↗', etichetta: 'Espansione',      colore: '#27ae60', note: 'Il campo si apre verso nuove possibilità evolutive' },
      { codice: '→', etichetta: 'Stabilizzazione', colore: '#2980b9', note: 'Il campo mantiene la sua forma; nessun movimento netto' },
      { codice: '↘', etichetta: 'Restringimento',  colore: '#e74c3c', note: 'Il campo si chiude; riduzione delle possibilità' }
    ],
    esempio: '↗',
    colore: '#27ae60'
  },
  {
    codice: 'T',
    nome: 'Stabilità temporale',
    sottotitolo: 'Con quale frequenza e continuità si manifesta questa configurazione',
    descrizione: 'La stabilità non è sinonimo di rigidità: descrive se la configurazione è un fenomeno isolato, uno schema ricorrente, o una forma strutturata nel tempo. Questo orienta l\'attenzione del professionista sulla soglia di intervento.',
    opzioni: [
      { codice: 'T1', etichetta: 'Situazionale', colore: '#95a5a6', note: 'Osservata in questo momento specifico; non confermata' },
      { codice: 'T2', etichetta: 'Ricorrente',   colore: '#e67e22', note: 'Si manifesta in più occasioni simili' },
      { codice: 'T3', etichetta: 'Stabilizzata', colore: '#e74c3c', note: 'Schema consolidato nel tempo; richiede attenzione continuativa' }
    ],
    esempio: 'T2',
    colore: '#e67e22'
  },
  {
    codice: 'A',
    nome: 'Abitabilità esperienziale',
    sottotitolo: 'La qualità complessiva del campo dal punto di vista dello sviluppo',
    descrizione: 'L\'abitabilità non è una valutazione del bambino o dell\'adulto. È una stima della qualità del campo come spazio evolutivo. Deriva dalla normatività intrinseca dello sviluppo — non da norme esterne, prescrizioni o confronti.',
    opzioni: [
      { codice: 'A+',  etichetta: 'Alta abitabilità', colore: '#27ae60', note: 'Il campo offre condizioni favorevoli all\'esperienza evolutiva' },
      { codice: 'A±',  etichetta: 'Fragile',          colore: '#e67e22', note: 'Il campo è attivo ma presenta elementi di fragilità; monitorare' },
      { codice: 'A−',  etichetta: 'Rischio collasso',  colore: '#e74c3c', note: 'Il campo è a rischio di cedere; necessaria attenzione clinica/educativa' }
    ],
    esempio: 'A±',
    colore: '#8e44ad'
  }
];

// --- CE_CASO_GUIDA ---
// Configurazione Evolutiva completa del caso-guida (lettura condivisa)
// Usata nelle slide 6.3, 6.6 e nel seed del CEBuilder
const CE_CASO_GUIDA = {
  S: { N1: '~', N2: '↑', N3: '~', N4: '↓', N5: '~', N6: '~', N7: '~' },
  R: [
    { da: 'N2', a: 'N3', tipo: 'MED', testo: 'Il campo relazionale orienta l\'accesso al mondo simbolico' },
    { da: 'N7', a: 'N3', tipo: 'CPL', testo: 'L\'agentività del bambino sostiene il processo condiviso' },
    { da: 'N2', a: 'N1', tipo: 'CMP', testo: 'La relazione compensa la stabilità della presenza' }
  ],
  D: '↗',
  T: 'T2',
  A: 'A±',
  testoNaturale: 'Campo relazionale espansivo che orienta e sostiene l\'accesso al mondo condiviso, con esplorazione ancora ridotta. La configurazione è fragile ma con direzione evolutiva aperta.',
  contesto: 'Bilancio pediatrico, bambino 18-24 mesi, 3-5 minuti di lettura condivisa con genitore presente'
};

// --- BUILDER_TESTI ---
// Frasi template per la generazione del testo naturale nel CEBuilder
// Il builder combina questi frammenti in base alle selezioni dell'utente
const BUILDER_TESTI = {
  nodi: {
    N1: {
      '↑': 'presenza piena e attiva nel campo',
      '~': 'presenza stabile nel campo',
      '↓': 'presenza fragile o discontinua nel campo',
      '!': 'presenza disorganizzata nel campo',
      '?': null
    },
    N2: {
      '↑': 'campo relazionale espansivo',
      '~': 'campo relazionale stabile',
      '↓': 'campo relazionale fragile',
      '!': 'campo relazionale incoerente',
      '?': null
    },
    N3: {
      '↑': 'accesso al mondo condiviso pienamente espresso',
      '~': 'accesso al mondo condiviso presente',
      '↓': 'accesso al mondo condiviso ridotto',
      '!': 'accesso al mondo condiviso compromesso',
      '?': null
    },
    N4: {
      '↑': 'esplorazione attiva e diversificata',
      '~': 'esplorazione funzionante',
      '↓': 'esplorazione ridotta o contenuta',
      '!': 'esplorazione disorganizzata',
      '?': null
    },
    N5: {
      '↑': 'regolazione fluida e adattiva',
      '~': 'regolazione stabile',
      '↓': 'regolazione rigida o ridotta',
      '!': 'regolazione disorganizzata',
      '?': null
    },
    N6: {
      '↑': 'partecipazione piena ai rituali condivisi',
      '~': 'partecipazione ai rituali presente',
      '↓': 'partecipazione ai rituali ridotta',
      '!': 'partecipazione ai rituali compromessa',
      '?': null
    },
    N7: {
      '↑': 'agentività piena ed espressa',
      '~': 'agentività presente',
      '↓': 'agentività ridotta o poco espressa',
      '!': 'agentività frammentata',
      '?': null
    }
  },
  relazioni: {
    CPL: 'sostegno reciproco tra nodi',
    VIN: 'vincolo che limita l\'espansione',
    MED: 'mediazione che orienta lo sviluppo',
    CMP: 'compensazione che bilancia la fragilità'
  },
  direzioni: {
    '↗': 'in espansione evolutiva',
    '→': 'in stabilizzazione',
    '↘': 'in restringimento'
  },
  stabilita: {
    T1: 'osservazione situazionale',
    T2: 'schema ricorrente',
    T3: 'configurazione stabilizzata nel tempo'
  },
  abitabilita: {
    'A+':  'alta abitabilità esperienziale',
    'A±':  'configurazione fragile ma evolutivamente aperta',
    'A−':  'rischio di collasso esperienziale'
  }
};

// --- REGOLA_FONDAMENTALE ---
// Usata nella slide 6.5
const REGOLA_FONDAMENTALE = {
  testo: 'La configurazione descrive il campo, non attribuisce proprietà al bambino.',
  cosa_e: [
    'Una descrizione del campo relazionale in un momento situato',
    'Uno strumento di leggibilità per il professionista',
    'Una forma reversibile e dinamica — mai definitiva',
    'Il prodotto finale della Fase 2'
  ],
  cosa_non_e: [
    'Una diagnosi o una classificazione del bambino',
    'Un giudizio sulla famiglia o sull\'adulto di riferimento',
    'Un piano di intervento (questo è compito di F3)',
    'Una misura di normalità o patologia'
  ]
};
```

---

## Slide 6.1 — La CE come unità minima
**Tipo**: `standard`  
**Titolo**: "La Configurazione Evolutiva"  
**Sottotitolo**: "Descrivere senza classificare"

### Contenuto

Paragrafo narrativo di apertura (corpo testo, non bullet):

> Quando la Fase 2 è completa, il professionista dispone di un linguaggio strutturato per descrivere ciò che ha osservato. Non una diagnosi. Non una valutazione. Una **forma**: la Configurazione Evolutiva.

Segue una card definitoria centrata — bordo accent `#16a085`, sfondo tenue:

> **Una Configurazione Evolutiva** è la forma temporaneamente stabile assunta dalla dinamica tra Nodi Trasversali in un determinato campo relazionale.

Tre chip sotto la card, in riga:
1. **Situata** — dipende dal campo, dall'adulto, dal contesto
2. **Reversibile** — può cambiare; non è una sentenza
3. **Dinamica** — descrive movimento, non stato fisso

Poi un secondo paragrafo:

> Una CE non dice cosa è il bambino. Dice come il campo relazionale funziona in questo momento. Questo è il senso preciso di "produrre leggibilità" — l'obiettivo della Fase 2.

### Note implementative
- Font della card definitoria: `font-style: italic; font-size: 1.15rem`
- Chips: fondo `#e8f8f5`, bordo `#16a085`, testo scuro — layout inline-flex con gap
- Secondo paragrafo: `color: var(--text-secondary)`

---

## Slide 6.2 — Le cinque dimensioni grammaticali
**Tipo**: `interactive`  
**Titolo**: "Cinque dimensioni"  
**Sottotitolo**: "I parametri della grammatica configurazionale"

### Layout
5 cards cliccabili in griglia — su desktop: 3+2 (prima riga: S, R, D; seconda riga: T, A). Su mobile: colonna singola.

Ogni card ha:
- **Lettera codice** grande (top-left) nel colore della dimensione
- **Nome** della dimensione
- **Sottotitolo** (breve)
- Al click → espande un pannello sotto (accordion): descrizione estesa + tabella opzioni + esempio

Le 5 cards devono essere **tutte cliccabili contemporaneamente** (`multiOpen: true`).

### Comportamento accordion
Ogni card aperta mostra:
1. Testo descrittivo (da `CINQUE_DIMENSIONI[i].descrizione`)
2. Tabella compatta: colonna Codice (monospace) + colonna Significato + colonna Note
3. Box "Esempio nel caso-guida": `font-family: monospace; background: var(--code-bg)`

### Dati
Usa `CINQUE_DIMENSIONI` — array di 5 oggetti definito sopra.

### Colori dimensioni (in ordine S/R/D/T/A):
`#16a085` / `#2980b9` / `#27ae60` / `#e67e22` / `#8e44ad`

### Note implementative
- Lettera codice: `font-size: 2.5rem; font-weight: 700; opacity: 0.15` come sfondo, più una versione `1.1rem` leggibile sopra
- Box esempi: `background: #f4f4f4; border-left: 3px solid var(--accent); padding: 0.5rem 1rem`
- Al click header card → toggle `expanded` class → altezza `auto` con `max-height` transition

---

## Slide 6.3 — Come si scrive una CE
**Tipo**: `diagram`  
**Titolo**: "La forma completa"  
**Sottotitolo**: "CE del caso-guida annotata"

### Layout
Due colonne (50/50):
- **Colonna sinistra**: il blocco CE in formato testuale annotato
- **Colonna destra**: traduzione in linguaggio naturale + contesto

### Colonna sinistra — blocco CE annotato

```
CE =
  S: N1~ N2↑ N3~ N4↓ N5~ N6~ N7~
  R: N2→N3 (MED), N7→N3 (CPL), N2→N1 (CMP)
  D: ↗
  T: T2
  A: A±
```

Ogni riga del blocco ha, sulla destra, un tooltip/label al hover che mostra il significato:
- Riga `S:` → label: "Stato funzionale di ciascun nodo nel campo"
- Riga `R:` → label: "Relazioni dominanti tra nodi (tipo e direzione)"
- Riga `D:` → label: "Traiettoria evolutiva: espansione"
- Riga `T:` → label: "Schema ricorrente, osservato in più bilanci"
- Riga `A:` → label: "Campo fragile ma evolutivamente aperto"

I simboli di stato nei nodi (`↑`, `~`, `↓`) hanno ciascuno il proprio colore:
- `↑` → `#27ae60` (verde)
- `~` → `#2980b9` (blu)
- `↓` → `#e67e22` (arancio)
- `!` → `#e74c3c` (rosso)

### Colonna destra
**Box testo naturale** (bordo `#16a085`, fondo `#e8f8f5`):
> *"Campo relazionale espansivo che orienta e sostiene l'accesso al mondo condiviso, con esplorazione ancora ridotta. La configurazione è fragile ma con direzione evolutiva aperta."*

Sotto il box, **chip contesto** in grigio chiaro:
> Bilancio pediatrico, bambino 18-24 mesi, 3-5 minuti di lettura condivisa con genitore presente

**Nota metodologica** in fondo a destra (piccolo, corsivo, `var(--text-secondary)`):
> Il testo naturale non è una diagnosi. È la restituzione leggibile della struttura — per il professionista, non per la famiglia.

### Dati
Usa `CE_CASO_GUIDA` definita sopra.

### Note implementative
- Blocco CE: `font-family: 'Courier New', monospace; font-size: 0.95rem; line-height: 2; background: var(--surface-2); padding: 1.5rem; border-radius: 8px`
- Etichette hover: `position: relative` + `:after` pseudo-element con label, visible on hover
- Su mobile: le due colonne diventano stack verticale (blocco CE sopra, testo naturale sotto)

---

## Slide 6.4 — CEBuilder
**Tipo**: `interactive`  
**Titolo**: "Costruisci una CE"  
**Sottotitolo**: "Usa il costruttore per esplorare la grammatica"

### Descrizione componente
Usa il componente `CEBuilder(container)` definito in ISTRUZIONI_CLAUDE_CODE.md §6.5.

L'interfaccia del builder è divisa in due zone:
- **Zona sinistra (60%): selettori** — il professionista costruisce la CE
- **Zona destra (40%): output live** — la CE si aggiorna in tempo reale

### Zona sinistra — selettori

**Dimensione S — Stato nodi** (7 righe, una per nodo):
Ogni riga: etichetta nodo (es. "N1 — Presenza") + 5 bottoni radio visuali (↑ / ~ / ↓ / ! / ?) colorati in base allo stato.  
Default iniziale: tutti i nodi a `~`.

Layout a griglia: 7 righe × (label + 5 bottoni radio visuali)

**Dimensione R — Relazione dominante** (select dropdown o 4 toggle buttons):
Opzioni: CPL / VIN / MED / CMP + "nessuna dominante" (default: nessuna selezionata)  
Nota: il campo R in questa versione semplificata del builder accetta una sola relazione dominante (il builder avanzato con relazioni multiple è fuori scope per questo modulo)

**Dimensione D — Direzione** (3 bottoni radio visuali: ↗ → ↘):  
Default: `→`

**Dimensione T — Stabilità** (3 bottoni radio visuali: T1 / T2 / T3):  
Default: `T1`

**Dimensione A — Abitabilità** (3 bottoni radio visuali: A+ / A± / A−):  
Default: `A±`

**Bottone "Carica caso-guida"**: precompila tutti i selettori con `CE_CASO_GUIDA`. Posizionato sopra i selettori, stile ghost button con bordo `#16a085`.

### Zona destra — output live

**Box CE formattato** (aggiornamento real-time ad ogni selezione):
```
CE =
  S: [valori selezionati]
  R: [relazione selezionata] o "—"
  D: [direzione selezionata]
  T: [stabilità selezionata]
  A: [abitabilità selezionata]
```

**Box testo naturale** (generato da `generaTestoNaturale(ce)` — vedi sotto):
Testo in italiano in corsivo, aggiornamento live.

**Bottone "Copia CE"**: copia il testo del blocco CE negli appunti. Stile secondario.

### Funzione `generaTestoNaturale(ce)`

La funzione costruisce un testo in italiano combinando frammenti da `BUILDER_TESTI`:

```javascript
function generaTestoNaturale(ce) {
  const frammenti = [];

  // 1. Raccoglie descrizioni dei nodi con stato non-null e non-'~'
  const nodiSalienti = Object.entries(ce.S)
    .filter(([nodo, stato]) => stato !== '?' && stato !== '~')
    .map(([nodo, stato]) => BUILDER_TESTI.nodi[nodo]?.[stato])
    .filter(Boolean);

  // Se nessun nodo saliente, usa i nodi stabili più rilevanti (N2, N3)
  const nodoPrincipale = nodiSalienti.length > 0
    ? nodiSalienti.slice(0, 2).join(', ')
    : BUILDER_TESTI.nodi['N2']?.['~'] || 'campo stabile';

  frammenti.push(capitalize(nodoPrincipale));

  // 2. Aggiunge relazione dominante se presente
  if (ce.R && BUILDER_TESTI.relazioni[ce.R]) {
    frammenti.push(`con ${BUILDER_TESTI.relazioni[ce.R]}`);
  }

  // 3. Aggiunge direzione
  if (BUILDER_TESTI.direzioni[ce.D]) {
    frammenti.push(BUILDER_TESTI.direzioni[ce.D]);
  }

  // 4. Costruisce frase base
  const frase1 = frammenti.join(', ') + '.';

  // 5. Aggiunge stabilità e abitabilità come frase conclusiva
  const t = BUILDER_TESTI.stabilita[ce.T] || '';
  const a = BUILDER_TESTI.abitabilita[ce.A] || '';
  const frase2 = (t || a) ? `${capitalize(t)}${t && a ? '; ' : ''}${a}.` : '';

  return [frase1, frase2].filter(Boolean).join(' ');
}
```

### Note implementative
- I bottoni radio visuali per gli stati dei nodi hanno colore di sfondo variabile: se selezionato `↑` → verde, `~` → blu, ecc. — ricavati da `CODICI_STATO` (già definiti nel modulo 5)
- La funzione `generaTestoNaturale` deve essere tollerante: se `ce.R` è null o 'nessuna', la omette senza errori
- Il box output usa `font-family: monospace` per il blocco CE, font normale per il testo naturale
- Il bottone "Carica caso-guida" usa `CE_CASO_GUIDA` (definita sopra)
- Su mobile: le due zone si impilano (selettori sopra, output sotto)

---

## Slide 6.5 — La regola fondamentale
**Tipo**: `standard`  
**Titolo**: "Una sola regola"  
**Sottotitolo**: "Il limite epistemologico della grammatica configurazionale"

### Layout
Centratura verticale. La slide è intenzionalmente "vuota" — una sola regola, molto spazio bianco.

**Callout principale** (bordo sinistro 5px `#16a085`, fondo `#e8f8f5`, padding generoso, testo grande):

> **La configurazione descrive il campo, non attribuisce proprietà al bambino.**

Sotto, un `ComparisonPanel` a due colonne:

| Una CE **è** | Una CE **non è** |
|---|---|
| Una descrizione del campo relazionale situato | Una diagnosi o classificazione del bambino |
| Uno strumento di leggibilità per il professionista | Un giudizio sulla famiglia o sull'adulto |
| Una forma reversibile e mai definitiva | Un piano di intervento (quello appartiene a F3) |
| Il prodotto finale della Fase 2 | Una misura di normalità o patologia |

Sotto la tabella, una nota esplicativa breve:

> Questa regola non è una cautela etica aggiuntiva: è strutturalmente necessaria. Una CE che descrivesse il bambino non sarebbe più una CE — sarebbe una diagnosi. Il metodo non prevede diagnosi.

### Dati
Usa `REGOLA_FONDAMENTALE` definita sopra.

### Note implementative
- Callout: `font-size: 1.25rem; font-weight: 600; letter-spacing: -0.01em`
- ComparisonPanel: due colonne, header "Una CE è" (verde `#27ae60`) / "Una CE non è" (rosso `#e74c3c`)
- Ogni cella: `padding: 0.6rem; border-bottom: 1px solid var(--border)`
- La nota finale: `font-size: 0.9rem; color: var(--text-secondary); margin-top: 1.5rem; font-style: italic`

---

## Slide 6.6 — Esercizio: decodifica la CE del caso-guida
**Tipo**: `interactive`  
**Titolo**: "Leggiamo la CE del caso-guida"  
**Sottotitolo**: "Decodifica guidata passo per passo"

### Struttura
Esercizio a 5 passi con **reveal progressivo**. Ogni passo mostra una dimensione della CE e pone una domanda riflessiva con risposta a scelta multipla (o risposta rivelata).

Controlli: bottone "Passo successivo →" (freccia destra o click). La navigazione tra slide è **bloccata** finché non si raggiunge il passo 5. (`completedSteps < 5`)

**Intestazione** (sempre visibile): blocco CE completo in monocromatico (`color: var(--text-disabled)`) — si "accende" dimensione per dimensione man mano che si avanza.

---

**Passo 1 — Dimensione S**

Si illumina la riga `S: N1~ N2↑ N3~ N4↓ N5~ N6~ N7~` nel blocco CE (gli altri rimangono grigi).

Domanda:
> Quale nodo è in stato espansivo? Cosa significa per il campo della lettura condivisa?

Risposta rivelata (non quiz — click "Mostra risposta"):
> **N2↑** — Il campo relazionale tra bambino e adulto è espansivo. Non è il bambino a essere "più bravo": è la qualità della relazione in questo contesto specifico che facilita lo scambio.

---

**Passo 2 — Dimensione R**

Si illumina la riga `R: N2→N3 (MED), N7→N3 (CPL), N2→N1 (CMP)`.

Domanda:
> Tre relazioni dominanti. Quale ti sembra la più importante strutturalmente?

Risposta rivelata:
> **N2→N3 (MED)** è la relazione cardine: la forza della relazione adulto-bambino orienta e rende possibile l'accesso al mondo condiviso simbolico. Senza N2↑, N3 resterebbe stabile ma non si espanderebbe.

---

**Passo 3 — Dimensione D**

Si illumina `D: ↗`.

Domanda:
> Il campo è in espansione. Ma N4 è ↓ (esplorazione ridotta). Come stanno insieme queste due informazioni?

Risposta rivelata:
> Non si contraddicono. L'espansione ↗ riguarda la direzione complessiva del campo, non lo stato di ogni singolo nodo. N4↓ segnala un'area di attenzione, ma la relazione (N2↑, MED) sostiene comunque un movimento evolutivo aperto.

---

**Passo 4 — Dimensioni T e A**

Si illuminano `T: T2` e `A: A±`.

Domanda:
> Schema ricorrente (T2) e abitabilità fragile (A±). Cosa orienta il professionista?

Risposta rivelata:
> T2 significa che questo pattern si è già osservato in bilanci precedenti: non è un'impressione isolata. A± segnala un campo che funziona ma mostra fragilità. Insieme: **monitorare**, non intervenire in modo direttivo. La CE non prescrive nulla.

---

**Passo 5 — Testo naturale completo**

Si illumina l'intera CE. Compare il testo naturale completo in un box:

> *"Campo relazionale espansivo che orienta e sostiene l'accesso al mondo condiviso, con esplorazione ancora ridotta. La configurazione è fragile ma con direzione evolutiva aperta."*

Messaggio conclusivo (verde, piccolo):
> ✓ Hai letto una CE completa. Ora puoi tornare al CEBuilder e costruirne una diversa.

Bottone "→ Prossima slide" si sblocca.

### Note implementative
- Stato: `completedSteps` (0–5). Il bottone di navigazione è `disabled` se `completedSteps < 5`
- Il blocco CE usa `color: var(--text-disabled)` per le dimensioni non ancora rivelate, poi `color: inherit` con transizione al reveal
- Pulsante "Mostra risposta" sostituisce il testo della domanda con la risposta (fade-in)
- "Passo successivo →": bottone accent con label "Passo X / 5" aggiornata dinamicamente
- Al passo 5: `completedSteps = 5` → sblocco navigazione automatico

---

## Slide 6.7 — Sintesi F2 e soglia F3
**Tipo**: `narrative`  
**Titolo**: "Cosa ha prodotto la Fase 2"  
**Sottotitolo**: "Dalla leggibilità all'azione"

### Contenuto

**Paragrafo 1 — Riepilogo F2**:
> La Fase 2 ha tradotto le strutture di F1 in un linguaggio professionale condiviso. Abbiamo traversato sette nodi, costruito operatori di lettura, esplorato le relazioni configurazionali e imparato a descrivere senza classificare. Il prodotto finale è la CE: una forma grammaticale, non una sentenza.

**Box "Cosa ha prodotto F2"** — 3 righe con icona + testo (bordo `#16a085`):
1. 🔍 **Operatori di lettura** — domande strutturali che organizzano l'osservazione
2. 📐 **Configurazioni Evolutive** — descrizioni comparabili e reversibili del campo
3. 🌉 **Linguaggio condiviso** — traducibile in pediatria, NPI, educazione, counseling

**Separatore visivo** (linea tratteggiata, con testo al centro: "Soglia F3")

**Paragrafo 2 — Apertura verso F3**:
> La Fase 3 riempie le forme prodotte da F2. Ogni contesto (clinico, educativo, familiare, istituzionale) produce uno **strumento contestualizzato** diverso dallo stesso output-tipo — non una tecnica diversa, ma un'applicazione situata della stessa grammatica.

**Chip azione** (stile callout leggero, fondo `#fef9e7`, bordo `#f1c40f`):
> F2 produce **leggibilità**. F3 produce **azione**. La CE è il punto di passaggio.

**Collegamento al caso-guida** (piccolo, in fondo):
> Nel caso-guida: la CE `A±, T2, ↗` indica che il bilancio pediatrico non richiede un intervento direttivo, ma un protocollo di monitoraggio condiviso con la famiglia — questo è il compito di F3.

### Note implementative
- Separatore "Soglia F3": `border-top: 2px dashed var(--border); position: relative` con label centrata `background: var(--bg); padding: 0 1rem`
- Box "Cosa ha prodotto F2": flex column, ogni riga con gap, icona come `span` con emoji o SVG icon inline
- Chip azione: `display: inline-block; border-radius: 8px; font-size: 0.95rem; padding: 0.75rem 1.25rem`

---

## Note generali del modulo

### Progressione pedagogica
Il modulo segue una curva: **concetto → struttura → pratica → regola → esercizio → sintesi**. Il CEBuilder è il centro del modulo (slide 6.4) ma viene preceduto dalla comprensione delle dimensioni (6.2) e da un esempio annotato (6.3), e seguito da un esercizio guidato (6.6) per consolidare la lettura.

### Connessione con altri moduli
- `CE_CASO_GUIDA.S` è coerente con `CONFIGURAZIONI_TIPICHE[1]` (Configurazione B) del modulo 5
- Il CEBuilder condivide i colori degli stati con `CODICI_STATO` del modulo 5 — Claude Code riutilizza la stessa costante o la copia localmente nel modulo
- La funzione `generaTestoNaturale` è locale al modulo 6 (non globale)

### Blocco navigazione slide 6.6
Implementare come: `slide.lockNext = true` → `false` quando `completedSteps >= 5`. Il controllo va fatto nel gestore `nextSlide()` del modulo.

### Integrazione `window.CASO_GUIDA`
Il bottone "Carica caso-guida" nel CEBuilder legge `window.CASO_GUIDA.pipeline.ce` e precompila i selettori. Il campo `R` del caso-guida ha 3 relazioni (array): il builder semplificato ne usa la prima (`N2→N3, MED`) come relazione dominante.

### Design complessivo
- Accent `#16a085` (verde acqua scuro) — si abbina bene ai verdi già usati per `A+` e Configurazione A nel modulo 5, ma è sufficientemente distinto
- Evitare overuse di verde: usarlo per accent/highlight principali, non per ogni elemento
- Slide 6.5 è volutamente minimalista — molto spazio bianco, il callout domina la scena
