# Modulo 9 — Pipeline completa: il caso-guida dall'inizio alla fine

**Accent color**: `#c0392b`  
**Slides**: 12  
**Obiettivo**: Attraversare l'intera pipeline F2 una sola volta, in continuità, usando esclusivamente il caso-guida come filo conduttore. Questo modulo non introduce contenuti nuovi — sintetizza, consolida e mostra il metodo in azione. Ogni slide corrisponde a un passaggio della pipeline; ogni guardrail compare al momento giusto.

---

## Componente trasversale: PipelineProgress

Questo modulo ha un **indicatore di progresso persistente** che appare come barra orizzontale nella parte superiore di ogni slide dalla 9.2 alla 9.12. La barra mostra tutti i nodi della pipeline; il nodo corrente è evidenziato.

```
[F1] → [1 Campo] → [2 Concetto] → [3 Nodo] → [4 Domande] → [5 Operatore] → [6 Famiglie] → [7 Template] → [CE] → [F3]
```

Ogni chip nella barra ha tre stati:
- **visited** (passi già visti): sfondo grigio chiaro, testo normale, opacità 0.7
- **current** (passo corrente): sfondo `#c0392b`, testo bianco, `font-weight: 600`
- **upcoming** (passi non ancora visti): bordo tratteggiato, testo tenue, opacità 0.4

La barra si aggiorna automaticamente al cambio slide tramite il metodo `updatePipelineProgress(stepId)` chiamato dall'`onEnter()` di ogni slide.

---

## JS Data (costanti del modulo)

```javascript
// --- PIPELINE_COMPLETA ---
// L'intera pipeline F2 con tutti i dati del caso-guida per ogni passo.
// Struttura master usata dalla PipelineProgress e da tutte le slide del modulo.
const PIPELINE_COMPLETA = [
  {
    id: 'F1',
    passo: 0,
    label: 'F1 — Fondamento',
    labelBreve: 'F1',
    guardrail: null,
    tesiCentrale: 'Il bambino è un soggetto incarnato, relazionale, temporalmente situato, progressivamente capace di abitare un mondo condiviso.',
    casoGuida: 'La lettura condivisa non è una prestazione linguistica né un test di sviluppo. È una configurazione di esperienza condivisa.',
    erroreEvitato: 'Ridurre il bambino a una somma di funzioni isolate (linguistica, attentiva, cognitiva).',
    colore: '#1a6b8a',
    slideModulo: '9.2'
  },
  {
    id: 'campo',
    passo: 1,
    label: '1 — Campo di lavoro',
    labelBreve: '1 Campo',
    guardrail: { codice: 'C0', nome: 'Vincolo di contesto', testo: 'La situazione è valida perché è delimitata. Non diciamo genericamente "sviluppo simbolico", ma osserviamo una situazione concreta: adulto, bambino, libro, interazione breve.' },
    prodotto: 'Contorno osservativo: chi, dove, con che cosa, quanto tempo, cosa si può vedere.',
    casoGuida: 'Lettura condivisa adulto-bambino in ambulatorio pediatrico. Bambino 18-24 mesi, genitore presente, libro illustrato, 3-5 minuti.',
    vincoli: [
      { elemento: 'Contesto', valore: 'Ambulatorio pediatrico / casa / nido' },
      { elemento: 'Attori', valore: 'Bambino, genitore, eventualmente pediatra/osservatore' },
      { elemento: 'Oggetto mediatore', valore: 'Libro illustrato' },
      { elemento: 'Tempo', valore: '3-5 minuti' },
      { elemento: 'Osservabile', valore: 'Corpo, sguardo, gesto, voce, alternanza adulto-oggetto, iniziativa, risposta adulta' },
      { elemento: 'Non osservabile', valore: 'Motivazione interna, intenzione psicologica profonda, competenza stabile' }
    ],
    colore: '#2d6a4f',
    slideModulo: '9.3'
  },
  {
    id: 'concetto',
    passo: 2,
    label: '2 — Concetto-ponte',
    labelBreve: '2 Concetto',
    guardrail: { codice: 'C1', nome: 'Non-riduzionismo', testo: 'Il concetto-ponte è valido se mantiene insieme corpo, relazione, oggetto, gesto, parola e significato. Non deve diventare una singola variabile.' },
    prodotto: 'Linguaggio che traduce il contenuto teorico senza ridurlo a una categoria tecnica troppo stretta.',
    casoGuida: '"Accesso al mondo condiviso" — il bambino usa il libro come occasione per entrare con l\'adulto in un campo condiviso di sguardo, gesto, voce e significato.',
    formulazioneValida: 'Il bambino usa il libro come occasione per entrare con l\'adulto in un campo condiviso di sguardo, gesto, voce e significato.',
    formulazioniRiduttive: [
      { formula: '"Il bambino presta attenzione"', problema: 'Riduce il campo a funzione attentiva' },
      { formula: '"Il bambino sa indicare"', problema: 'Riduce la configurazione a comportamento' },
      { formula: '"Il genitore stimola bene"', problema: 'Sposta subito verso giudizio sull\'adulto' }
    ],
    colore: '#6c63ff',
    slideModulo: '9.4'
  },
  {
    id: 'nodo',
    passo: 3,
    label: '3 — Nodo trasversale',
    labelBreve: '3 Nodo',
    guardrail: { codice: 'C2', nome: 'Attraversamento', testo: 'Il nodo è valido perché non appartiene a un solo asse. Non è solo linguaggio, non è solo relazione, non è solo attenzione. È una configurazione multi-asse.' },
    prodotto: 'Motore strutturale che attraversa più assi e più discipline.',
    casoGuida: 'N3 — Accesso al mondo condiviso simbolico. Nella lettura condivisa, il bambino può trasformare il libro in un luogo di accesso al mondo comune, attraverso l\'intreccio tra gesto, sguardo, voce adulta, interesse e significato culturale.',
    assiCoinvolti: [
      { asse: 'Asse 1 — Ontologico-fenomenologico', presenza: 'Il bambino abita una situazione incarnata: corpo, sguardo, postura, orientamento' },
      { asse: 'Asse 2 — Affettivo-morale', presenza: 'Il clima relazionale sostiene o ostacola lo scambio' },
      { asse: 'Asse 5 — Desiderio', presenza: 'Alcune immagini attraggono il bambino e orientano la sua iniziativa' },
      { asse: 'Asse 6 — Storico-culturale', presenza: 'Il libro introduce un mondo simbolico, linguistico e culturale condiviso' }
    ],
    colore: '#e67e22',
    slideModulo: '9.5'
  },
  {
    id: 'domande',
    passo: 4,
    label: '4 — Domande professionali',
    labelBreve: '4 Domande',
    guardrail: { codice: 'C3', nome: 'Non-diagnostico', testo: 'Le domande sono valide perché rendono leggibile la situazione senza classificare il bambino, il genitore o la relazione.' },
    prodotto: 'Interrogazioni osservabili usabili da pediatra, educatore, ricercatore.',
    casoGuida: 'Il libro resta un oggetto isolato o diventa qualcosa da condividere? Il bambino alterna lo sguardo tra libro e adulto? Il gesto indica, mostra, chiede? Lo scambio si mantiene, si interrompe, si riprende?',
    domandeValide: [
      'Il libro diventa oggetto comune o resta in uso parallelo?',
      'C\'è alternanza di sguardo tra libro e adulto?',
      'Il gesto apre una relazione o rimane azione solitaria?',
      'Lo scambio si mantiene, si interrompe, si riprende?',
      'Il bambino introduce qualcosa di proprio o risponde solo alle proposte adulte?'
    ],
    domandeNonValide: [
      { formula: '"Il bambino è in ritardo?"', motivo: 'Diagnostica' },
      { formula: '"Il genitore legge bene?"', motivo: 'Valutativa' },
      { formula: '"Bisogna insegnare al genitore?"', motivo: 'Già operativa' }
    ],
    colore: '#2980b9',
    slideModulo: '9.6'
  },
  {
    id: 'operatore',
    passo: 5,
    label: '5 — Operatore di lettura',
    labelBreve: '5 Operatore',
    guardrail: { codice: 'C4', nome: 'Separazione', testo: 'Questa lettura non dice ancora che cosa fare. Non prescrive un intervento. Organizza la leggibilità.' },
    prodotto: 'Lettura sintetica del campo — non valutazione, non diagnosi.',
    casoGuida: {
      campo: 'Il bambino e l\'adulto si orientano verso qualcosa di comune (il libro), con gesto, sguardo e parola che si intrecciano.',
      posizione: 'Il bambino indica, mostra, vocalizza: c\'è iniziativa soggettiva e non solo reazione all\'adulto.',
      limite: 'Il bambino accetta di condividere il controllo del libro con l\'adulto; la sequenza si interrompe e riprende.',
      sintesi: 'Campo condiviso presente ma fragile: il bambino cerca l\'adulto attraverso gesto e sguardo, prende iniziativa su alcune figure, ma la continuità dello scambio dipende molto dalla capacità dell\'adulto di attendere e seguire il ritmo del bambino.'
    },
    colore: '#d35400',
    slideModulo: '9.7'
  },
  {
    id: 'famiglie',
    passo: 6,
    label: '6 — Famiglie di output',
    labelBreve: '6 Famiglie',
    guardrail: { codice: 'C5', nome: 'Scalabilità', testo: 'La stessa grammatica può generare output diversi: clinici, educativi, genitoriali, formativi, di ricerca. Questo mostra che il nodo è davvero trasversale.' },
    prodotto: 'Classi di prodotti possibili — non ancora strumenti definitivi.',
    casoGuida: [
      { famiglia: 'Osservativa',   forma: 'Scheda di osservazione della lettura condivisa' },
      { famiglia: 'Formativa',     forma: 'Micro-modulo per pediatri o educatori' },
      { famiglia: 'Restitutiva',   forma: 'Traccia di colloquio con il genitore' },
      { famiglia: 'Ricerca',       forma: 'Griglia per confrontare sequenze video' },
      { famiglia: 'Organizzativa', forma: 'Protocollo per i bilanci di salute' },
      { famiglia: 'AI-assistita',  forma: 'Prompt per analizzare trascrizioni di sequenze' }
    ],
    colore: '#27ae60',
    slideModulo: '9.8'
  },
  {
    id: 'template',
    passo: 7,
    label: '7 — Output-tipo vuoto',
    labelBreve: '7 Template',
    guardrail: { codice: 'C6', nome: 'Completezza', testo: 'Il template è completo perché può essere usato come base per futuri strumenti, ma resta ancora vuoto: non prescrive, non valuta, non assegna punteggi.' },
    prodotto: 'Stampo riusabile — struttura compilabile, neutra, adattabile in F3.',
    casoGuida: {
      titolo: 'Scheda vuota di leggibilità del mondo condiviso',
      formulaVuota: 'In questa situazione, il campo condiviso appare _______; l\'iniziativa del bambino si manifesta attraverso _______; la risposta adulta tende a _______; la continuità dello scambio è _______; il rapporto con il limite appare _______. La configurazione complessiva suggerisce _______.',
      formulaCompilata: 'In questa situazione, il campo condiviso appare presente ma discontinuo; l\'iniziativa del bambino si manifesta attraverso indicazione e alternanza di sguardo; la risposta adulta tende a sostenere quando attende, ma a interrompere quando anticipa; la continuità dello scambio è fragile ma recuperabile; il rapporto con il limite appare tollerabile se mediato dall\'adulto. La configurazione complessiva suggerisce un accesso al mondo condiviso sostenuto dalla relazione ma non ancora autonomamente stabile.'
    },
    colore: '#27ae60',
    slideModulo: '9.9'
  }
];

// --- CE_FINALE ---
// Configurazione Evolutiva completa del caso-guida come prodotto della pipeline
const CE_FINALE = {
  S: { N1: '~', N2: '↑', N3: '~', N4: '↓', N5: '~', N6: '~', N7: '~' },
  R: [
    { testo: 'N2→N3 (MED)', descrizione: 'Il campo relazionale orienta e sostiene l\'accesso al mondo condiviso' },
    { testo: 'N7→N3 (CPL)', descrizione: 'L\'agentività del bambino sostiene il processo condiviso' },
    { testo: 'N2→N1 (CMP)', descrizione: 'La relazione compensa la fragilità della presenza' }
  ],
  D: '↗',
  T: 'T2',
  A: 'A±',
  testoNaturale: 'Campo relazionale espansivo che orienta e sostiene l\'accesso al mondo condiviso, con esplorazione ancora ridotta. La configurazione è fragile ma con direzione evolutiva aperta.',
  letturaSintetica: 'In questa situazione, l\'accesso al mondo condiviso è possibile, sostenuto dalla relazione, ma non ancora pienamente stabile.'
};

// --- SOGLIA_F3 ---
// Strumenti possibili in F3 per ogni contesto + C7
const SOGLIA_F3 = {
  guardrail: {
    codice: 'C7',
    nome: 'Responsabilità',
    testo: 'La decisione operativa appartiene alla Fase 3 e alle responsabilità disciplinari specifiche. La Fase 2 produce solo la grammatica di traducibilità.'
  },
  strumenti: [
    { contesto: 'Clinico',       strumento: 'Scheda breve per osservare la lettura condivisa nei bilanci di salute' },
    { contesto: 'Pedagogico',    strumento: 'Traccia per educatori del nido su libro e campo condiviso' },
    { contesto: 'Genitoriale',   strumento: 'Scheda semplice per aiutare il genitore a riconoscere i momenti di condivisione' },
    { contesto: 'Ricerca',       strumento: 'Griglia per codifica qualitativa di brevi video' },
    { contesto: 'Formativo',     strumento: 'Micro-caso per formazione di pediatri o volontari DBS/NPL' },
    { contesto: 'AI-assistito',  strumento: 'Prompt per trasformare descrizioni narrative in configurazioni leggibili' }
  ],
  cosaNonAncoraFatto: [
    'Punteggi e soglie', 'Protocolli operativi', 'Istruzioni per l\'adulto',
    'Raccomandazioni cliniche', 'Criteri di inclusione/esclusione',
    'Giudizi sull\'adulto', 'Classificazioni del bambino'
  ]
};

// --- PERCHE_FUNZIONA ---
// 9 ragioni per cui questo esempio funziona (§2.13 degli esempi)
// Usato nella slide 9.12
const PERCHE_FUNZIONA = [
  'Parte da una situazione semplice e osservabile',
  'Conserva il riferimento alla fondazione ontologica',
  'Evita di ridurre il fenomeno a linguaggio, attenzione o comportamento',
  'Mostra la multi-asseità del nodo',
  'Produce domande professionali non diagnostiche',
  'Costruisce un operatore di lettura strutturato',
  'Genera famiglie di output diverse con la stessa grammatica',
  'Arriva a un template vuoto riusabile',
  'Resta sulla soglia di F3 senza oltrepassarla'
];
```

---

## Slide 9.1 — La mappa del viaggio
**Tipo**: `standard`  
**Titolo**: "Pipeline completa"  
**Sottotitolo**: "Il caso-guida dall'inizio alla fine"  
**PipelineProgress**: non mostrata (è la slide di apertura)

### Contenuto

**Paragrafo di apertura**:
> Nei moduli precedenti hai attraversato ogni passaggio della Fase 2 separatamente. Ora li percorri tutti insieme, in sequenza, usando il caso-guida come filo continuo. La scena è sempre la stessa: un bambino di 18-24 mesi, un genitore, un libro illustrato, un bilancio pediatrico.

**Scena del caso-guida** — box narrativo centrale (fondo tenue, bordo `#c0392b`, corsivo):
> *Durante un bilancio di salute, il pediatra propone una breve situazione di lettura condivisa. Il bambino prende il libro, lo apre, indica una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina l'immagine, sorride, aspetta. Il bambino gira pagina, poi mostra un'altra figura all'adulto.*

**Mappa della pipeline** — diagramma a 10 nodi in riga orizzontale (o a due righe su mobile):

```
[F1]  →  [1. Campo]  →  [2. Concetto]  →  [3. Nodo]  →  [4. Domande]
                                                               ↓
[F3]  ←  [CE]  ←  [7. Template]  ←  [6. Famiglie]  ←  [5. Operatore]
```

Su desktop: riga unica a 10 chip. Su mobile: due righe con frecce.

Ogni chip: colore del modulo di riferimento (da `PIPELINE_COMPLETA[i].colore`), con etichetta breve.

**Nota** sotto la mappa (piccolo, centrato):
> Ogni passo produce qualcosa di preciso. Ogni guardrail controlla che non si faccia troppo presto.

### Note implementative
- Il diagramma è SVG inline oppure HTML puro con flex/grid
- I chip della mappa in questa slide sono tutti dello stesso peso visivo (nessuno evidenziato) — è la panoramica, non il percorso
- La scena narrativa ha `font-style: italic; line-height: 1.8; max-width: 680px; margin: 0 auto`

---

## Slide 9.2 — F1: il punto di partenza
**Tipo**: `standard`  
**Titolo**: "Fondamento ontologico (F1)"  
**Sottotitolo**: "La tesi da cui tutto parte"  
**PipelineProgress**: `current: 'F1'`

### Contenuto

**Barra PipelineProgress** in cima alla slide (come da specifica del componente trasversale).

**Paragrafo** (breve — F1 è già stato trattato in modulo 0):
> Prima che la pipeline cominci, c'è una scelta teorica. Il metodo assume che il bambino non sia riducibile a una somma di funzioni isolate: è un soggetto incarnato, relazionale, temporalmente situato, che costruisce progressivamente la capacità di abitare un mondo condiviso.

**Card F1** (bordo `#1a6b8a`):
> Il bambino non "ha" competenze che si sommano.  
> **Abita** situazioni che possono diventare campo di esperienza condivisa.

**Come cambia la lettura** — due colonne compatte:

| Senza F1 | Con F1 |
|---|---|
| "Il bambino sa indicare" | "Il bambino usa il gesto per aprire uno scambio con l'adulto" |
| "Il bambino ha buone competenze linguistiche" | "Il libro diventa mediatore di un campo comune" |
| "Il bambino non presta attenzione" | "Il campo condiviso fatica a stabilizzarsi in questa sequenza" |

**Transizione** (testo piccolo in fondo):
> Da questa tesi, la pipeline può cominciare.

### Note implementative
- La tabella è compatta: `font-size: 0.875rem; padding: 0.4rem 0.7rem`
- Colonna "Senza F1": testo barrato o rosso tenue
- Colonna "Con F1": testo verde scuro / accent

---

## Slide 9.3 — Passo 1: Campo di lavoro
**Tipo**: `diagram`  
**Titolo**: "Passo 1 — Campo di lavoro"  
**Sottotitolo**: "Delimitare il contesto osservativo"  
**PipelineProgress**: `current: 'campo'`

### Layout
Due colonne (60/40):
- **Sinistra**: la tabella dei vincoli del caso-guida
- **Destra**: il box "Cosa produce questo passo" + GuardrailBadge C0

### Colonna sinistra — tabella vincoli

| Elemento | Caso-guida |
|---|---|
| Contesto | Ambulatorio pediatrico / casa / nido |
| Attori | Bambino 18-24m, genitore, eventualmente pediatra |
| Oggetto mediatore | Libro illustrato |
| Tempo | 3-5 minuti |
| Osservabile | Corpo, sguardo, gesto, voce, alternanza adulto-oggetto |
| Non osservabile | Motivazione interna, competenza stabile, intenzione profonda |

La riga "Non osservabile" ha sfondo leggermente diverso (grigio tenue) per segnalare che il campo delimita anche ciò che *non* si misura.

### Colonna destra

**Box "Cosa produce"** (fondo `#eafaf1`, bordo `#2d6a4f`):
> Il campo di lavoro definisce **dove**, **con chi** e **con quali vincoli** il metodo può operare. Non è ancora il tema — è il luogo.

**Formula di controllo** (piccolo, corsivo):
> "Posso immaginare una scena osservabile? Se no, non siamo ancora davanti a un campo di lavoro."

**GuardrailBadge C0** sotto:
`GuardrailBadge('C0', 'Vincolo di contesto', 'Cosa è osservabile? Cosa è decidibile nel campo?')`

### Dati
Usa `PIPELINE_COMPLETA[1]` (id: 'campo') per tutti i testi.

---

## Slide 9.4 — Passo 2: Concetto-ponte
**Tipo**: `comparison`  
**Titolo**: "Passo 2 — Concetto-ponte"  
**Sottotitolo**: "Tradurre senza ridurre"  
**PipelineProgress**: `current: 'concetto'`

### Layout
Tre zone verticali:
1. **Zona top**: il concetto-ponte del caso-guida (box centrato)
2. **Zona centrale**: ComparisonPanel — formulazione valida vs. riduttive
3. **Zona bottom**: GuardrailBadge C1

### Zona top — box concetto-ponte

**Label**: "Concetto-ponte"  
**Testo**: "Accesso al mondo condiviso"  
**Spiegazione sotto** (testo piccolo):
> Non "attenzione condivisa" (rischia di diventare competenza psicologica specifica).  
> Ma "accesso al mondo condiviso" — mantiene l'ampiezza ontologica: corpo, gesto, parola, attesa, significato culturale insieme.

### Zona centrale — ComparisonPanel

**Colonna sinistra** "Formulazione valida" (verde `#27ae60`):
> "Il bambino usa il libro come occasione per entrare con l'adulto in un campo condiviso di sguardo, gesto, voce e significato."

**Colonna destra** "Formulazioni riduttive" (rosso tenue) — lista di 3:
- "Il bambino presta attenzione" → *riduce a funzione attentiva*
- "Il bambino sa indicare" → *riduce a comportamento*
- "Il genitore stimola bene" → *sposta verso giudizio sull'adulto*

### Zona bottom
`GuardrailBadge('C1', 'Non-riduzionismo', 'Il concetto-ponte mantiene la funzione strutturale ed è osservabile in almeno due discipline diverse?')`

### Dati
Usa `PIPELINE_COMPLETA[2]` (id: 'concetto').

---

## Slide 9.5 — Passo 3: Nodo trasversale
**Tipo**: `diagram`  
**Titolo**: "Passo 3 — Nodo trasversale"  
**Sottotitolo**: "N3 — Accesso al mondo condiviso simbolico"  
**PipelineProgress**: `current: 'nodo'`

### Layout
Due colonne (50/50):
- **Sinistra**: card del nodo N3 + formulazione del caso-guida
- **Destra**: tabella assi coinvolti + GuardrailBadge C2

### Colonna sinistra

**Card N3** (colore nodo `#e67e22`, stessa grafica dei nodi in modulo 3):
- Header: "N3 — Accesso al mondo condiviso simbolico"
- Corpo: *"Nella lettura condivisa, il bambino può trasformare il libro in un luogo di accesso al mondo comune, attraverso l'intreccio tra gesto, sguardo, voce adulta, interesse e significato culturale."*

Sotto la card, un breve testo:
> Il libro non è solo un oggetto. È un mediatore di mondo: permette al bambino e all'adulto di orientarsi verso qualcosa che sta tra loro.

### Colonna destra

**Tabella assi coinvolti** (4 righe):

| Asse | Presenza nella situazione |
|---|---|
| A1 — Ontologico-fenomenologico | Il bambino abita la situazione con corpo, sguardo, postura |
| A2 — Affettivo-morale | Il clima relazionale sostiene o ostacola lo scambio |
| A5 — Desiderio | Alcune immagini attraggono e orientano l'iniziativa |
| A6 — Storico-culturale | Il libro introduce un mondo simbolico e culturale condiviso |

**Nota sotto**: "4 assi su 6 attivati — è un nodo, non una variabile singola."

`GuardrailBadge('C2', 'Attraversamento', 'Il nodo collega più assi? Integra corpo, relazione e senso?')`

### Dati
Usa `PIPELINE_COMPLETA[3]` (id: 'nodo').

---

## Slide 9.6 — Passo 4: Domande professionali
**Tipo**: `interactive`  
**Titolo**: "Passo 4 — Domande professionali"  
**Sottotitolo**: "Rendere il nodo interrogabile in contesti reali"  
**PipelineProgress**: `current: 'domande'`

### Layout
Due colonne:
- **Sinistra**: lista domande valide del caso-guida (5 domande)
- **Destra**: ComparisonPanel — domande da evitare + GuardrailBadge C3

### Colonna sinistra

**Header**: "Domande valide — lettura condivisa"

Lista di 5 domande (card leggere, clickabili per expand con nota):

1. "Il libro diventa oggetto comune o resta in uso parallelo?" → *Legge la qualità del campo, non la competenza*
2. "C'è alternanza di sguardo tra libro e adulto?" → *Osservabile direttamente*
3. "Il gesto apre una relazione o rimane azione solitaria?" → *Distingue azione da comunicazione senza diagnosticare*
4. "Lo scambio si mantiene, si interrompe, si riprende?" → *Legge la continuità, non la durata come punteggio*
5. "Il bambino introduce qualcosa di proprio o risponde solo all'adulto?" → *Legge la posizione soggettiva senza valutarla*

### Colonna destra

**Header**: "Domande da evitare"

Lista di 3 domande con etichetta del problema:
- "Il bambino è in ritardo?" → **Diagnostica**
- "Il genitore legge bene?" → **Valutativa**
- "Bisogna insegnare al genitore?" → **Già operativa**

`GuardrailBadge('C3', 'Non-diagnostico', 'Le domande producono leggibilità senza classificazione o prescrizione?')`

### Note implementative
- Le 5 domande valide hanno un indicatore al click (piccola freccia) che mostra la nota esplicativa (1-2 righe)
- Le domande da evitare hanno sfondo rosso tenue con label badge a destra

---

## Slide 9.7 — Passo 5: Operatore di lettura
**Tipo**: `diagram`  
**Titolo**: "Passo 5 — Operatore di lettura"  
**Sottotitolo**: "Tre domande strutturali per organizzare ciò che si vede"  
**PipelineProgress**: `current: 'operatore'`

### Layout
**Tre pannelli in colonna** (una per dimensione dell'operatore), ciascuno con:
- Header colorato: numero + nome (colori: `#16a085` / `#8e44ad` / `#d35400`)
- Testo di lettura del caso-guida (da `PIPELINE_COMPLETA[5].casoGuida`)

**Pannello 1 — Campo condiviso** (header `#16a085`):
> "Il bambino e l'adulto si orientano verso qualcosa di comune (il libro), con gesto, sguardo e parola che si intrecciano."

**Pannello 2 — Posizione soggettiva** (header `#8e44ad`):
> "Il bambino indica, mostra, vocalizza: c'è iniziativa soggettiva e non solo reazione all'adulto."

**Pannello 3 — Rapporto con il limite** (header `#d35400`):
> "Il bambino accetta di condividere il controllo del libro con l'adulto; la sequenza si interrompe e riprende."

**Box sintesi** sotto i tre pannelli (larghezza piena, bordo `#c0392b`):
> *"Campo condiviso presente ma fragile: il bambino cerca l'adulto attraverso gesto e sguardo, prende iniziativa su alcune figure, ma la continuità dello scambio dipende molto dalla capacità dell'adulto di attendere e seguire il ritmo del bambino."*

`GuardrailBadge('C4', 'Separazione', 'Questa lettura non dice ancora che cosa fare. Organizza la leggibilità.')`

### Dati
Usa `PIPELINE_COMPLETA[5]` (id: 'operatore'), campo `casoGuida`.

---

## Slide 9.8 — Passo 6: Famiglie di output
**Tipo**: `standard`  
**Titolo**: "Passo 6 — Famiglie di output"  
**Sottotitolo**: "La stessa grammatica genera prodotti diversi"  
**PipelineProgress**: `current: 'famiglie'`

### Layout
**Griglia 2×3** di card famiglie (da `PIPELINE_COMPLETA[6].casoGuida`). Ogni card:
- Nome famiglia (header colorato — un colore per famiglia, coerente con modulo 8)
- Possibile forma (testo)
- Label piccola: "non ancora lo strumento — la direzione"

Famiglie:
1. **Osservativa** `#2980b9` — Scheda di osservazione della lettura condivisa
2. **Formativa** `#16a085` — Micro-modulo per pediatri o educatori
3. **Restitutiva** `#8e44ad` — Traccia di colloquio con il genitore
4. **Ricerca** `#27ae60` — Griglia per confrontare sequenze video
5. **Organizzativa** `#c0392b` — Protocollo per i bilanci di salute
6. **AI-assistita** `#7f8c8d` — Prompt per analizzare trascrizioni

**Nota metodologica** sotto la griglia:
> Sei famiglie, un solo nodo, un solo concetto-ponte. La scalabilità è la prova che il nodo è davvero trasversale.

`GuardrailBadge('C5', 'Scalabilità', 'Più destinatari, stessa grammatica — funziona in ambulatorio, nido, casa, ricerca.')`

### Note implementative
- Le 6 card hanno altezza fissa, non espandibili — sono solo indicative in questo modulo (il dettaglio è in M8)
- Griglia: `display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem`

---

## Slide 9.9 — Passo 7: Output-tipo vuoto
**Tipo**: `diagram`  
**Titolo**: "Passo 7 — Output-tipo vuoto"  
**Sottotitolo**: "Lo stampo riusabile — ultimo passo di F2"  
**PipelineProgress**: `current: 'template'`

### Layout
Due zone verticali:
1. **Zona superiore** (60%): la formula di sintesi — prima vuota, poi compilata con toggle
2. **Zona inferiore** (40%): i due guardrail C6 + C7 affiancati + testo "F2 si ferma qui"

### Zona superiore

**Header**: "Scheda vuota di leggibilità del mondo condiviso"

**Toggle button**: "Mostra formula compilata" / "Nascondi compilazione"

**Stato vuoto** (monospace, testo tenue):
> "In questa situazione, il campo condiviso appare _______; l'iniziativa del bambino si manifesta attraverso _______; la risposta adulta tende a _______; la continuità dello scambio è _______; il rapporto con il limite appare _______. La configurazione complessiva suggerisce _______."

**Stato compilato** (normale, fondo `#eafaf1`, bordo `#27ae60`):
> "In questa situazione, il campo condiviso appare presente ma discontinuo; l'iniziativa del bambino si manifesta attraverso indicazione e alternanza di sguardo; la risposta adulta tende a sostenere quando attende, ma a interrompere quando anticipa; la continuità dello scambio è fragile ma recuperabile; il rapporto con il limite appare tollerabile se mediato dall'adulto. La configurazione complessiva suggerisce un accesso al mondo condiviso sostenuto dalla relazione ma non ancora autonomamente stabile."

### Zona inferiore

Testo centrato (piccolo, grassetto):
> Il template è completo. F2 si ferma qui.

Due GuardrailBadge affiancati:
- `GuardrailBadge('C6', 'Completezza', 'Il template è riusabile, resta vuoto, non prescrive, non valuta, non assegna punteggi.')`
- `GuardrailBadge('C7', 'Responsabilità', 'La decisione operativa appartiene a F3 e alle responsabilità disciplinari specifiche.')`

### Dati
Usa `PIPELINE_COMPLETA[7]` (id: 'template'), campo `casoGuida`.

---

## Slide 9.10 — La Configurazione Evolutiva
**Tipo**: `diagram`  
**Titolo**: "Configurazione Evolutiva del caso-guida"  
**Sottotitolo**: "Il prodotto grammaticale della pipeline"  
**PipelineProgress**: `current: 'CE'`

### Layout
Due colonne (50/50):
- **Sinistra**: blocco CE annotato
- **Destra**: testo naturale + lettura sintetica + nota metodologica

### Colonna sinistra — blocco CE

```
CE =
  S: N1~ N2↑ N3~ N4↓ N5~ N6~ N7~
  R: N2→N3 (MED)
     N7→N3 (CPL)
     N2→N1 (CMP)
  D: ↗
  T: T2
  A: A±
```

Stile: `font-family: monospace; font-size: 1rem; line-height: 2; background: var(--surface-2); padding: 1.5rem; border-radius: 8px`

Ogni stato dei nodi ha il suo colore (`↑` verde, `~` blu, `↓` arancio).  
Ogni relazione R ha il colore del tipo (MED `#2980b9`, CPL `#27ae60`, CMP `#e67e22`).

### Colonna destra

**Box testo naturale** (bordo `#16a085`, fondo `#e8f8f5`):
> *"Campo relazionale espansivo che orienta e sostiene l'accesso al mondo condiviso, con esplorazione ancora ridotta. La configurazione è fragile ma con direzione evolutiva aperta."*

**Lettura sintetica** (sotto, testo normale):
> In questa situazione, l'accesso al mondo condiviso è possibile, sostenuto dalla relazione, ma non ancora pienamente stabile.

**Nota metodologica** (piccola, corsiva):
> Questa CE non dice che il bambino è competente. Non dice che è in difficoltà. Dice come il campo relazionale funziona in questo momento specifico.

**Regola** (chip finale):
> La configurazione descrive il campo, non il bambino.

### Dati
Usa `CE_FINALE` definita sopra.  
Coerente con `window.CASO_GUIDA.pipeline.ce`.

---

## Slide 9.11 — Soglia F3
**Tipo**: `narrative`  
**Titolo**: "La soglia"  
**Sottotitolo**: "F2 produce la forma. F3 la riempie."  
**PipelineProgress**: `current: 'F3'`

### Contenuto

**Paragrafo**:
> La Fase 2 si ferma qui. Ha prodotto leggibilità — non ha prescritto nulla. Ciò che viene dopo appartiene alle responsabilità disciplinari di ciascun professionista e al contesto specifico in cui opererà lo strumento.

**Tabella strumenti possibili in F3** (da `SOGLIA_F3.strumenti`) — 6 righe, 2 colonne:

| Contesto | Strumento possibile |
|---|---|
| Clinico | Scheda breve per osservare la lettura condivisa nei bilanci di salute |
| Pedagogico | Traccia per educatori del nido su libro e campo condiviso |
| Genitoriale | Scheda semplice per aiutare il genitore a riconoscere i momenti di condivisione |
| Ricerca | Griglia per codifica qualitativa di brevi video |
| Formativo | Micro-caso per formazione di pediatri o volontari DBS/NPL |
| AI-assistito | Prompt per trasformare descrizioni narrative in configurazioni leggibili |

**Separatore**

**Box "Cosa non è ancora stato fatto in F2"** (sfondo `#fef9e7`, bordo `#f39c12`) — lista compatta:
> Punteggi · Soglie · Protocolli operativi · Istruzioni per l'adulto · Raccomandazioni cliniche · Classificazioni del bambino

**GuardrailBadge C7** (in footer):
`GuardrailBadge('C7', 'Responsabilità', 'La decisione clinica/educativa fuori dal metodo. F2 non prescrive, non gestisce, non interviene.')`

---

## Slide 9.12 — Conclusione: cosa ha reso possibile la Fase 2
**Tipo**: `narrative`  
**Titolo**: "Cosa ha reso possibile la Fase 2"  
**Sottotitolo**: "Nove motivi per cui questo esempio funziona"  
**PipelineProgress**: non mostrata (slide di chiusura)

### Contenuto

**Paragrafo di apertura**:
> Questo percorso non è stato costruito attorno alla lettura condivisa perché è una tecnica educativa o una buona pratica. Ma perché è una **situazione privilegiata di traducibilità**: attraverso il libro, il bambino può mostrare come accede a un mondo comune.

**9 punti** (da `PERCHE_FUNZIONA`) — numerati 1-9, in lista leggera (non accordion, non card — semplicità):

1. Parte da una situazione semplice e osservabile
2. Conserva il riferimento alla fondazione ontologica
3. Evita di ridurre il fenomeno a linguaggio, attenzione o comportamento
4. Mostra la multi-asseità del nodo
5. Produce domande professionali non diagnostiche
6. Costruisce un operatore di lettura strutturato
7. Genera famiglie di output diverse con la stessa grammatica
8. Arriva a un template vuoto riusabile
9. Resta sulla soglia di F3 senza oltrepassarla

**Separatore**

**Box finale** (fondo `#f9f9f9`, bordo `#c0392b`, testo centrato, font leggermente grande):
> La Fase 2 rende leggibile l'intreccio tra corpo, relazione, desiderio, simbolo e cultura.  
> Non dice ancora che cosa fare.  
> **Mostra che cosa diventa visibile.**

**Chip** sotto il box (stile minimal):
> Da qui, la Fase 3 può costruire con responsabilità.

### Note implementative
- I 9 punti si rivelano uno per uno al click (click su "punto successivo") oppure sono tutti visibili da subito — da decidere in fase di implementazione; la versione con reveal progressivo è pedagogicamente più efficace ma non obbligatoria
- Se si implementa il reveal progressivo: nessun blocco della navigazione (è l'ultimo modulo)
- Il box finale deve avere `padding: 2rem; margin-top: 2rem; text-align: center`
- Le tre righe del box finale: prima e terza riga in testo normale, seconda riga in corsivo, terza riga in grassetto

---

## Note generali del modulo

### Principio di progettazione
Il modulo 9 non introduce concetti nuovi. È un modulo di **sintesi visiva**: ogni slide deve essere più pulita, più diretta e meno densa dei moduli precedenti. Si mostrano i risultati, non si ri-insegna la struttura.

### Uso di `window.CASO_GUIDA`
Questo modulo usa `window.CASO_GUIDA` più di qualsiasi altro. Tutti i testi del caso-guida vengono letti dall'oggetto globale (o da `PIPELINE_COMPLETA` che ne replica le sezioni rilevanti). Non ci sono dati inventati.

### PipelineProgress — implementazione
Il componente `PipelineProgress` è specifico di questo modulo — non appartiene alla shell globale. Va implementato nel modulo M9 come elemento HTML posizionato nel `.slide-header` o come elemento fisso in cima all'area della slide.

Al cambio slide (`onEnter`), il modulo chiama:
```javascript
updatePipelineProgress(slide.pipelineStep);
```
dove `pipelineStep` è l'id del passo corrente (es. `'campo'`, `'nodo'`, `'CE'`, ecc.).

### Guardrail — gestione complessiva
Tutti gli 8 guardrail (C0–C7) compaiono esattamente una volta nel modulo, nella slide corrispondente. Non vengono aggregati in un'unica slide né ripetuti.

Il riassunto completo dei guardrail è:
- C0 → slide 9.3
- C1 → slide 9.4
- C2 → slide 9.5
- C3 → slide 9.6
- C4 → slide 9.7
- C5 → slide 9.8
- C6 + C7 → slide 9.9 (affiancati — sono i guardrail di soglia)

### Design
- Accent `#c0392b` (rosso scuro) — il colore del capstone: indica completamento, maturità, soglia
- Le slide di questo modulo devono avere meno interattività dei moduli 3-8: l'obiettivo è la fluidità narrativa
- Le uniche interazioni attive sono: toggle formula compilata (9.9), reveal punti finali (9.12 opzionale)
- La PipelineProgress è il principale elemento visivo ricorrente — deve essere visivamente coerente in tutte le slide
