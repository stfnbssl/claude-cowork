# Modulo 5 — La Dinamica tra Nodi
**Numero slide**: 7
**Colore accent**: `#8e44ad`
**Tipo prevalente**: diagram + standard

---

## Dati globali del modulo

Definire in `m05.js` le seguenti costanti.

```javascript
// I quattro tipi di relazione tra Nodi
const TIPI_RELAZIONE = [
  {
    id: 'CPL',
    codice: 'CPL',
    nome: 'Sostegno',
    colore: '#27ae60',
    descrizione: 'Un Nodo rende possibile l\'attivazione di un altro. Non è una causa diretta: è una condizione di possibilità. Se il Nodo che sostiene è fragile, quello sostenuto collassa o non si attiva pienamente.',
    esempio_principale: {
      catena: ['N1', 'N4', 'N7'],
      frecce: ['→', '→'],
      testo: 'Senza regolazione (N1), l\'esplorazione (N4) collassa. Senza esplorazione stabile, il desiderio (N7) non trova direzione.'
    },
    domanda_controllo: 'Questo Nodo è una condizione affinché un altro possa attivarsi?'
  },
  {
    id: 'VIN',
    codice: 'VIN',
    nome: 'Vincolo',
    colore: '#e74c3c',
    descrizione: 'Un Nodo limita fisiologicamente un altro, in entrambe le direzioni. Il vincolo non è patologico: è strutturale. Troppo di uno schiaccia l\'altro; troppo poco produce disorganizzazione nell\'altro.',
    esempio_principale: {
      catena: ['N5', '↔', 'N7'],
      frecce: ['↔'],
      testo: 'Troppo limite (N5 dominante) → ritiro del desiderio (N7↓). Assenza di limite (N5 assente) → desiderio disorganizzato (N7!).'
    },
    domanda_controllo: 'L\'eccesso o il difetto di questo Nodo altera strutturalmente un altro?'
  },
  {
    id: 'MED',
    codice: 'MED',
    nome: 'Mediazione',
    colore: '#2980b9',
    descrizione: 'Un Nodo coordina e rende possibile la connessione tra due domini diversi. Senza il Nodo mediatore, i due domini resterebbero disconnessi o si attiverebbero in modo non integrato.',
    esempio_principale: {
      catena: ['N2', '→', 'N3'],
      frecce: ['→'],
      testo: 'Il simbolico (N3) emerge solo dentro relazione regolata (N2). Senza campo relazionale funzionante, l\'accesso al mondo condiviso rimane frammentato o puramente funzionale.'
    },
    domanda_controllo: 'Questo Nodo rende possibile il collegamento tra due configurazioni che altrimenti resterebbero separate?'
  },
  {
    id: 'CMP',
    codice: 'CMP',
    nome: 'Compensazione',
    colore: '#e67e22',
    descrizione: 'Un Nodo sostiene parzialmente una fragilità in un altro, permettendo al campo di restare abitabile anche in presenza di difficoltà. La compensazione non annulla il problema: lo rende temporaneamente gestibile. Fondamentale per evitare letture deficit-based.',
    esempio_principale: {
      catena: ['N2↑', 'compensa', 'N1↓'],
      frecce: [],
      testo: 'Una relazione adulta solida (N2↑) può sostenere una regolazione fragile (N1↓): il bambino si regola attraverso l\'adulto anche quando non riesce ancora a farlo autonomamente.'
    },
    domanda_controllo: 'Questo Nodo permette al campo di restare abitabile nonostante la fragilità di un altro?'
  }
];

// I sette Nodi come nodi del grafo (posizioni e colori per la visualizzazione)
const NODI_GRAFO = [
  { id: 'N1', label: 'N1\nRegolazione',      colore: '#e67e22', x: 50,  y: 20  },
  { id: 'N2', label: 'N2\nCo-regolazione',   colore: '#27ae60', x: 80,  y: 50  },
  { id: 'N3', label: 'N3\nMondo condiviso',  colore: '#2980b9', x: 50,  y: 80  },
  { id: 'N4', label: 'N4\nApertura',         colore: '#8e44ad', x: 20,  y: 50  },
  { id: 'N5', label: 'N5\nLimite reale',     colore: '#e74c3c', x: 80,  y: 80  },
  { id: 'N6', label: 'N6\nContinuità',       colore: '#16a085', x: 20,  y: 80  },
  { id: 'N7', label: 'N7\nDesiderio',        colore: '#f39c12', x: 50,  y: 50  }
];

// Le relazioni tra nodi per il grafo (usate nella slide 5.2)
const RELAZIONI_GRAFO = [
  { da: 'N1', a: 'N4',  tipo: 'CPL', label: 'Sostegno' },
  { da: 'N4', a: 'N7',  tipo: 'CPL', label: 'Sostegno' },
  { da: 'N1', a: 'N7',  tipo: 'CPL', label: 'Sostegno indiretto' },
  { da: 'N5', a: 'N7',  tipo: 'VIN', label: 'Vincolo', bidirezionale: true },
  { da: 'N2', a: 'N3',  tipo: 'MED', label: 'Mediazione' },
  { da: 'N2', a: 'N1',  tipo: 'CMP', label: 'Compensazione' },
  { da: 'N5', a: 'N6',  tipo: 'VIN', label: 'Vincolo lieve' },
  { da: 'N7', a: 'N3',  tipo: 'CPL', label: 'Sostegno' }
];

// Le quattro configurazioni tipiche
const CONFIGURAZIONI_TIPICHE = [
  {
    id: 'A',
    nome: 'Espansiva integrata',
    colore: '#27ae60',
    descrizione: 'Campo espansivo, alta abitabilità. I Nodi si sostengono reciprocamente in una dinamica di apertura. La direzione è verso maggiore complessità e ricchezza esperienziale.',
    stati: { N1: '↑', N2: '↑', N3: '↑', N4: '↑', N5: '~', N6: '~', N7: '↑' },
    relazione_dominante: 'CPL (sostegno)',
    direzione: '↗ espansione',
    stabilita: 'T2 ricorrente',
    abitabilita: 'A+',
    contesti: 'Contesti familiari e educativi ben funzionanti; prevenzione universale; percorsi di promozione dello sviluppo.',
    lettura: 'Il bambino esplora, condivide, desidera, regola e si relaziona in modo integrato. Non è assenza di difficoltà: è presenza di risorse.'
  },
  {
    id: 'B',
    nome: 'Accesso situazionale',
    colore: '#f39c12',
    descrizione: 'Competenze presenti ma uso discontinuo. N3 è visibile, ma N1 e N2 instabili rendono la mediazione fragile: l\'accesso al mondo condiviso appare e scompare in base al sostegno disponibile.',
    stati: { N1: '~', N2: '~', N3: '~', N4: '~', N5: '~', N6: '~', N7: '~' },
    note_stati: 'N3 presente nelle sequenze supportate; N1 e N2 instabili fuori dal sostegno adulto diretto',
    relazione_dominante: 'MED fragile (N2→N3 discontinuo)',
    direzione: '→ stabilizzazione',
    stabilita: 'T1 situazionale',
    abitabilita: 'A±',
    contesti: 'Frequente nei bilanci pediatrici: il bambino mostra competenze nella situazione strutturata ma non le usa stabilmente. Zona di osservazione e sostegno preventivo.',
    lettura: 'Le competenze ci sono ma sono dipendenti dal sostegno adulto. Non è patologia: è una configurazione che richiede attenzione e accompagnamento.'
  },
  {
    id: 'C',
    nome: 'Campo ristretto',
    colore: '#e67e22',
    descrizione: 'Una fragilità in N1 si propaga per sostegno mancato a N4 e poi a N7. Il bambino mostra bassa iniziativa, usa l\'adulto in modo prevalentemente funzionale, esplora poco. Il campo è abitabile ma ristretto.',
    stati: { N1: '↓', N2: '~', N3: '~', N4: '↓', N5: '~', N6: '~', N7: '↓' },
    relazione_dominante: 'CPL mancato (N1↓ → N4 non si attiva → N7 basso)',
    direzione: '↘ restringimento',
    stabilita: 'T2 ricorrente',
    abitabilita: 'A±',
    contesti: 'Zona preventiva critica. Segnali di bassa iniziativa e poca esplorazione che possono passare inosservati perché il bambino non è "difficile". Richiede lettura attenta e sostegno precoce.',
    lettura: 'Il campo è abitabile ma non espansivo. La compensazione relazionale (N2) può sostenere temporaneamente, ma la fragilità di fondo rimane.'
  },
  {
    id: 'D',
    nome: 'Disorganizzazione',
    colore: '#e74c3c',
    descrizione: 'Collasso dell\'esperienza: N1 fragile impedisce la regolazione, N2 incoerente non offre sostegno, N5 caotico distrugge il campo invece di strutturarlo. Il risultato è ritiro o iperattivazione.',
    stati: { N1: '↓', N2: '!', N3: '↓', N4: '↓', N5: '!', N6: '↓', N7: '?' },
    relazione_dominante: 'Relazioni interrotte o caotiche',
    direzione: '↘ collasso',
    stabilita: 'T3 stabilizzata (se non interviene sostegno)',
    abitabilita: 'A−',
    contesti: 'Soglia NPI / clinica. Richiede valutazione specialistica e intervento. Non si tratta di "gestire un bambino difficile": si tratta di ricostruire le condizioni di abitabilità del campo.',
    lettura: 'La configurazione non descrive il bambino: descrive un campo che non riesce più a sostenere lo sviluppo. L\'intervento riguarda il campo, non solo il bambino.'
  }
];

// Legenda dei codici di stato (usata in più slide)
const CODICI_STATO = [
  { codice: '↑', significato: 'Espansivo',        colore: '#27ae60' },
  { codice: '~', significato: 'Stabile',           colore: '#2980b9' },
  { codice: '↓', significato: 'Ristretto',         colore: '#e67e22' },
  { codice: '!', significato: 'Disorganizzato',    colore: '#e74c3c' },
  { codice: '?', significato: 'Non leggibile',     colore: '#95a5a6' }
];
```

---

## SLIDE 5.1 — I Nodi non sono indipendenti

**Tipo**: `standard`
**Titolo**: Lo sviluppo è una configurazione
**Sottotitolo**: Non una somma di Nodi

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore — il principio**:

Grande blockquote centrato, bordo sinistro --color-accent:

> *"Lo stato evolutivo di un bambino corrisponde a una configurazione di Nodi simultaneamente attivi, non alla loro somma."*

Sotto, in testo normale:

I sette Nodi Trasversali non sono indipendenti. Lo sviluppo è un'**organizzazione dinamica** dell'esperienza: ogni Nodo influenza gli altri, ne rende possibili alcuni, ne limita altri, ne compensa altri ancora. Guardare un Nodo alla volta è come ascoltare un accordo una nota alla volta: si perde la musica.

**Sezione inferiore — tre conseguenze operative**:

Tre card orizzontali affiancate, con icona e testo:

**Card 1 — Per la lettura**:
🔍 *Nessun Nodo, da solo, identifica il rischio o la risorsa. È la configurazione che parla.*

**Card 2 — Per l'intervento**:
🎯 *L'intervento non si rivolge al "Nodo debole": si rivolge alla configurazione. Si sostiene il campo, non si "riparano" i Nodi.*

**Card 3 — Per la comunicazione interdisciplinare**:
🗣 *Due professionisti che leggono Nodi diversi non si contraddicono: stanno descrivendo aspetti della stessa configurazione.*

**Elemento visivo**: sette cerchi colorati (N1–N7) disposti in cerchio, con linee tratteggiate che li connettono tutti — un "campo" visivo che suggerisce interdipendenza. Nessun testo sulle linee ancora: è solo un'anticipazione del grafo che verrà nella slide 5.2.

**Nota in footer**:
*Questo è il motivo per cui il metodo non diagnostica: individua traiettorie. La traiettoria dipende dalla configurazione, non da un Nodo singolo.*

---

## SLIDE 5.2 — Il grafo delle relazioni

**Tipo**: `diagram`
**Titolo**: Quattro tipi di relazione tra Nodi
**Sottotitolo**: Come i Nodi si influenzano reciprocamente

**Contenuto principale**:

Visualizzazione principale: **grafo interattivo** dei sette Nodi con le relazioni codificate per tipo e colore.

**Layout del grafo**: i sette Nodi come cerchi colorati disposti in ellisse o esagono irregolare, con le relazioni come frecce/linee tra di loro. Ogni tipo di relazione ha colore e stile di linea diversi:

| Tipo | Colore linea | Stile | Freccia |
|------|-------------|-------|---------|
| CPL — Sostegno | `#27ae60` | continua | → (direzionata) |
| VIN — Vincolo | `#e74c3c` | tratteggiata | ↔ (bidirezionale) |
| MED — Mediazione | `#2980b9` | continua spessa | → |
| CMP — Compensazione | `#e67e22` | punteggiata | → |

**Relazioni da mostrare nel grafo** (dati da `RELAZIONI_GRAFO`):
- N1 → N4 (CPL)
- N4 → N7 (CPL)
- N1 → N7 (CPL, linea più sottile / tratteggiata lunga — sostegno indiretto)
- N5 ↔ N7 (VIN)
- N2 → N3 (MED)
- N2 → N1 (CMP, punteggiata)
- N5 → N6 (VIN lieve)
- N7 → N3 (CPL)

**Comportamento interattivo**:

- **Default**: tutte le relazioni visibili contemporaneamente, leggermente sbiadite
- **Hover su un tipo nella legenda**: evidenzia solo le relazioni di quel tipo, le altre sbiadiscono
- **Click su un Nodo**: evidenzia tutte le relazioni che lo coinvolgono (in entrata e in uscita); compare un tooltip con il nome del Nodo
- **Click su una relazione (freccia)**: compare un tooltip con: tipo di relazione, nome dei Nodi coinvolti, breve descrizione dell'effetto

**Legenda a destra del grafo** (quattro righe, una per tipo):

Ogni riga ha: campione colore + stile linea + codice (CPL/VIN/MED/CMP) + nome + definizione in una riga.

**Sotto il grafo — regola di lettura**:

*Per leggere il grafo: segui una freccia → un Nodo influenza l'altro in quel modo. Una relazione VIN ↔ significa che l'influenza è reciproca.*

---

## SLIDE 5.3 — Sostegno e Vincolo

**Tipo**: `standard`
**Titolo**: CPL e VIN — Sostegno e Vincolo
**Sottotitolo**: Come i Nodi si abilitano e si limitano reciprocamente

**Contenuto principale**:

Due sezioni verticali con divisore orizzontale.

**Sezione superiore — Sostegno (CPL)**:

Header verde: `CPL — Sostegno`

Definizione: *Un Nodo rende possibile l'attivazione di un altro. Non è causalità diretta: è condizione di possibilità.*

**Schema visivo** — catena orizzontale:

```
[N1 Regolazione] ──CPL──▶ [N4 Apertura] ──CPL──▶ [N7 Desiderio]
```

Sotto lo schema, spiegazione passo per passo:

- **N1 → N4**: perché esplorare richiede di non essere sopraffatti dall'esperienza. Senza una regolazione sufficientemente stabile, il bambino non ha le risorse per avvicinarsi a ciò che non conosce.
- **N4 → N7**: perché il desiderio nasce nell'incontro con un mondo aperto. Senza possibilità di esplorazione, l'iniziativa non trova dove andare.
- **Implicazione**: N1 fragile → N4 ridotto → N7 basso. La catena si rompe alla radice, ma l'effetto si vede all'altro capo.

Sotto, in testo secondario: *Notare: in questa catena, N1 non "causa" direttamente N7. Ma la sua fragilità si propaga attraverso N4. Questo spiega perché il bambino con bassa iniziativa non ha "un problema di desiderio": spesso ha un problema di regolazione.*

---

**Sezione inferiore — Vincolo (VIN)**:

Header rosso: `VIN — Vincolo`

Definizione: *Un Nodo limita fisiologicamente un altro, in entrambe le direzioni. Il vincolo non è un difetto del sistema: è strutturale.*

**Schema visivo** — doppia freccia orizzontale:

```
[N5 Limite reale] ◀──VIN──▶ [N7 Desiderio]
```

Sotto lo schema, due scenari affiancati:

| Scenario | N5 | N7 | Risultato |
|----------|----|----|-----------|
| Limite assente / caotico | ! | ! | Desiderio disorganizzato, impulsività |
| Limite eccessivo / rigido | ↑ dominante | ↓ | Ritiro, inibizione dell'iniziativa |
| Limite abitabile | ~ | ~ | Desiderio orientato, iniziativa stabile |

*Il VIN tra N5 e N7 mostra perché il limite non è "il nemico del desiderio": il limite ben calibrato è ciò che dà forma al desiderio. Il confine tra "troppo" e "troppo poco" è la configurazione da leggere.*

---

## SLIDE 5.4 — Mediazione e Compensazione

**Tipo**: `standard`
**Titolo**: MED e CMP — Mediazione e Compensazione
**Sottotitolo**: Come i Nodi coordinano e si sostituiscono parzialmente

**Contenuto principale**:

Due sezioni verticali con divisore orizzontale.

**Sezione superiore — Mediazione (MED)**:

Header blu: `MED — Mediazione`

Definizione: *Un Nodo coordina due domini diversi rendendone possibile la connessione. Senza di esso, i due rimangono disconnessi.*

**Schema visivo**:

```
[N2 Campo relazionale] ──MED──▶ [N3 Mondo condiviso simbolico]
```

Spiegazione:

Il simbolico non emerge nel vuoto. Emerge dentro una relazione che lo sostiene. Senza un campo relazionale funzionante (N2), l'accesso al mondo condiviso (N3) rimane frammentato, funzionale, o assente.

*Nella lettura condivisa: il bambino non "sviluppa il linguaggio" da solo. È la qualità dello scambio adulto-bambino (N2) che media il passaggio dal gesto individuale al significato condiviso (N3). Se N2 è incoerente — l'adulto non risponde, anticipa sempre, si distrae — N3 non si stabilizza.*

**Card esplicativa** con bordo blu:

Questo spiega un pattern frequente: bambini con competenze simboliche presenti ma discontinue. Non è che "N3 non funziona": è che N2 non offre mediazione stabile. L'intervento non va su N3 (linguaggio, indicare, condividere) — va su N2 (la qualità del campo relazionale).

---

**Sezione inferiore — Compensazione (CMP)**:

Header arancio: `CMP — Compensazione`

Definizione: *Un Nodo sostiene parzialmente una fragilità in un altro, rendendo il campo abitabile anche in presenza di difficoltà.*

**Schema visivo** con freccia curva:

```
[N2↑ Campo relazionale forte]
        │
        └──CMP──▶ [N1↓ Regolazione fragile]
                  (il campo diventa più abitabile)
```

Spiegazione:

Una relazione adulta solida e coerente (N2↑) può compensare una regolazione interna fragile (N1↓): il bambino si regola attraverso l'adulto, anche quando non riesce ancora a farlo autonomamente.

**Due note importanti** (card gialla tenue):

**1. La compensazione non annulla il problema**: N1 resta fragile. La compensazione rende il campo abitabile oggi, ma non sostituisce il lavoro su N1 nel tempo.

**2. La compensazione cambia la lettura del rischio**: un bambino con N1↓ ma N2↑ ha risorse che non emergono se si guarda solo N1. La lettura deficit-based rischia di perdere la compensazione.

*Per questo la configurazione è l'unità di lettura — non il singolo Nodo.*

---

## SLIDE 5.5 — Le quattro configurazioni tipiche

**Tipo**: `interactive`
**Titolo**: Quattro configurazioni tipiche
**Sottotitolo**: A · B · C · D

**Contenuto principale**:

Quattro card grandi con toggle (una visibile alla volta, oppure tutte visibili in griglia 2×2 su schermi larghi). Usa i dati da `CONFIGURAZIONI_TIPICHE`.

**Struttura di ogni card**:

Header colorato con: lettera grande (A / B / C / D) + nome configurazione

**Corpo della card** — tre zone:

**Zona 1 — Visualizzazione stati** (riga orizzontale di sette badge Nodo):

Sette cerchi piccoli colorati con il codice del Nodo (N1–N7), ognuno con il proprio simbolo di stato (↑ ~ ↓ ! ?) in sovrimpressione. Il colore del cerchio e il simbolo comunicano insieme lo stato.

Sotto la riga: relazione dominante + direzione + stabilità + abitabilità (i quattro elementi della CE).

**Zona 2 — Descrizione** (testo normale):

Testo dal campo `descrizione` + testo dal campo `lettura`.

**Zona 3 — Contesti di riferimento** (chip tenue):

Testo dal campo `contesti`. Indica dove e quando questa configurazione si incontra tipicamente.

---

**Card A — Espansiva integrata** (verde):

Visualizzazione: N1↑ N2↑ N3↑ N4↑ N5~ N6~ N7↑
R: CPL prevalente | D: ↗ | T: T2 | A: A+

*Campo espansivo, alta abitabilità. I Nodi si sostengono in una dinamica di apertura verso maggiore complessità esperienziale.*

*Il bambino esplora, condivide, desidera, regola e si relaziona in modo integrato. Non è assenza di difficoltà: è presenza di risorse.*

Contesti: contesti familiari/educativi funzionanti; prevenzione universale.

---

**Card B — Accesso situazionale** (gialla):

Visualizzazione: N1~ N2~ N3~ N4~ N5~ N6~ N7~
*(con nota: N3 presente nelle sequenze supportate; N1 e N2 instabili fuori dal sostegno diretto)*

R: MED fragile (N2→N3 discontinuo) | D: → | T: T1 | A: A±

*Competenze presenti ma uso discontinuo. Il bambino mostra N3 nella situazione strutturata ma non lo usa stabilmente senza sostegno.*

*Non è patologia: è una configurazione che richiede attenzione. Le competenze ci sono — serve accompagnamento affinché si stabilizzino.*

Contesti: frequente nei bilanci pediatrici; zona di osservazione preventiva.

---

**Card C — Campo ristretto** (arancione):

Visualizzazione: N1↓ N2~ N3~ N4↓ N5~ N6~ N7↓

R: CPL mancato (N1↓ → N4 non si attiva → N7 basso) | D: ↘ | T: T2 | A: A±

*Una fragilità in N1 si propaga per sostegno mancato. Il bambino mostra bassa iniziativa, usa l\'adulto in modo funzionale, esplora poco.*

*Può passare inosservato perché il bambino non è "difficile". È la zona preventiva critica: il campo è abitabile ma non espansivo.*

Contesti: zona preventiva critica; richiede lettura attenta.

---

**Card D — Disorganizzazione** (rossa):

Visualizzazione: N1↓ N2! N3↓ N4↓ N5! N6↓ N7?

R: Relazioni interrotte o caotiche | D: ↘ collasso | T: T3 | A: A−

*Collasso dell\'esperienza. N1 fragile impedisce la regolazione, N2 incoerente non offre sostegno, N5 caotico distrugge il campo invece di strutturarlo.*

*La configurazione non descrive il bambino: descrive un campo che non riesce più a sostenere lo sviluppo. L\'intervento riguarda il campo, non solo il bambino.*

Contesti: soglia NPI/clinica; richiede valutazione specialistica.

---

**Legenda dei codici di stato** (fissa, sotto le card):

Sette chip orizzontali da `CODICI_STATO`: ↑ Espansivo · ~ Stabile · ↓ Ristretto · ! Disorganizzato · ? Non leggibile — con colori corrispondenti.

---

## SLIDE 5.6 — La proprietà emergente decisiva

**Tipo**: `standard`
**Titolo**: È la configurazione che legge il rischio
**Sottotitolo**: Non il singolo Nodo

**Contenuto principale**:

**Sezione superiore — la regola**:

Grande blockquote centrato:

> *"Nessun Nodo, da solo, identifica il rischio: lo fa la configurazione."*

Sotto: *Questo è il motivo per cui il metodo non diagnostica — individua traiettorie.*

**Sezione centrale — dimostrazione con N3**:

Tre scenari affiancati che mostrano come lo stesso Nodo (N3 presente) abbia significati radicalmente diversi nelle configurazioni A, B e D:

**Scenario 1** — N3 in configurazione A:

Badge: N3~ + sfondo verde
N1↑ N2↑ **N3↑** N4↑ N7↑

*N3 espansivo in campo integrato. Il bambino partecipa pienamente al mondo condiviso. Nessun segnale di attenzione.*

**Scenario 2** — N3 in configurazione B:

Badge: N3~ + sfondo giallo
N1~ N2~ **N3~** N4~ N7~

*N3 presente ma discontinuo. Il bambino accede al mondo condiviso nelle sequenze strutturate, ma non lo stabilizza. Zona di osservazione.*

**Scenario 3** — N3 in configurazione D:

Badge: N3↓ + sfondo rosso
N1↓ N2! **N3↓** N4↓ N7?

*N3 ristretto in campo disorganizzato. L'accesso al mondo condiviso è compromesso non perché "N3 sia rotto", ma perché il campo relazionale non lo sostiene più.*

**Freccia che collega i tre scenari** con la nota:

*Stesso Nodo. Tre configurazioni. Tre traiettorie completamente diverse.*

**Sezione inferiore — implicazione per la pratica**:

Due box affiancati:

**Box verde — Cosa la configurazione permette**:
- Leggere risorse e fragilità insieme
- Identificare compensazioni (N2↑ con N1↓)
- Non confondere la manifestazione (bassa iniziativa) con la causa (N1 fragile → N4 → N7)
- Orientare l'intervento sul campo, non sul sintomo

**Box rosso — Cosa evita**:
- Diagnosticare dal Nodo singolo
- Patologizzare configurazioni che hanno risorse
- Perdere la compensazione
- Confondere discontinuità con deficit

---

## SLIDE 5.7 — Il caso-guida: la lettura condivisa come configurazione B

**Tipo**: `narrative`
**Titolo**: Il caso-guida nella dinamica dei Nodi
**Sottotitolo**: La lettura condivisa come configurazione B — accesso situazionale

**Contenuto principale**:

**Sezione superiore — la scena** (richiamo da `window.CASO_GUIDA.scena`):

Card narrativa in corsivo, sfondo --color-primary-light:

*Il bambino prende il libro, lo apre, guarda alcune immagini, indica una figura, vocalizza e guarda l'adulto. Il genitore nomina l'immagine, sorride, aspetta. Il bambino torna a guardare il libro, gira pagina, poi mostra un'altra figura all'adulto.*

**Sezione centrale — la configurazione nella dinamica**:

Due colonne:

**Colonna sinistra — I Nodi e i loro stati**:

Riga di sette badge con stati (dalla CE del caso-guida in `window.CASO_GUIDA.pipeline.ce`):

N1~ | N2↑ | N3~ | N4↓ | N5~ | N6~ | N7~

Sotto ogni badge, una riga di spiegazione:

- N2↑: *Il genitore nomina, sorride, aspetta — campo relazionale attivo*
- N3~: *Il bambino indica, vocalizza, alterna sguardo — accesso presente ma non stabilizzato*
- N4↓: *Esplorazione ridotta: il bambino non si allontana, resta nella sequenza strutturata*
- N7~: *Interesse per alcune figure — desiderio presente ma dipendente dalla struttura*

**Colonna destra — Le relazioni attive**:

**N2 → N3 (MED)**: la co-regolazione del genitore (attende, risponde, sostiene) media l'accesso al mondo condiviso. Quando il genitore anticipa o cambia ritmo, N3 si interrompe.

**N7 → N3 (CPL)**: l'interesse del bambino per alcune figure sostiene i momenti di accesso condiviso. Le sequenze più ricche avvengono sulle figure che attraggono il bambino.

**N2 compensa N1 (CMP)**: la regolazione non è ancora autonoma — il bambino si regola attraverso il campo adulto. La co-presenza del genitore è condizione dell'esperienza.

**Sezione inferiore — perché è configurazione B**:

Card gialla (colore configurazione B):

**Configurazione B — Accesso situazionale**

La lettura condivisa mostra N3 presente nelle sequenze supportate dall'adulto, ma non ancora stabilizzato in modo autonomo. N1 e N2 sono sufficiente base ma fragile: quando l'adulto cambia ritmo o anticipa, la sequenza si interrompe.

Questo non è un problema: è una configurazione evolutivamente aperta (A±, D: ↗). Il campo può espandersi con accompagnamento.

**CE dal caso-guida** (formato standard):

```
CE =
  S: N1~ N2↑ N3~ N4↓ N5~ N6~ N7~
  R: N2→N3 (MED), N7→N3 (CPL), N2→N1 (CMP)
  D: ↗
  T: T1/T2
  A: A±
```

*Traduzione naturale: Campo relazionale forte che media l'accesso al mondo condiviso; il desiderio del bambino orienta le sequenze più ricche; la regolazione è sostenuta dall'adulto più che autonoma; la configurazione è fragile ma evolutivamente aperta.*

**Chiusura del modulo**:

Testo centrato, leggero:

*Nel Modulo 6 costruiremo la Grammatica delle Configurazioni: il sistema formale che permette di scrivere, leggere e comunicare le CE tra professionisti.*

Badge: `→ Modulo 6 — La Grammatica delle Configurazioni`

---

## Note per l'implementazione

### Slide 5.2 — Il grafo interattivo

Opzione 1 (consigliata): usare una libreria leggera come **D3.js force-directed graph** con nodi fissi e archi colorati per tipo. I nodi hanno posizioni semi-fisse (non completamente force-directed per evitare che si sovrappongano ogni volta).

Opzione 2 (alternativa): SVG puro con posizioni hardcoded per i sette Nodi. Più semplice da implementare, meno flessibile. Su schermi piccoli il grafo diventa una tabella di relazioni.

Suggerisci l'opzione 2 se il tempo è limitato: la tabella delle relazioni trasmette le stesse informazioni in modo più leggibile, anche se meno visivamente d'impatto.

Tabella alternativa:

| Da | A | Tipo | Descrizione |
|----|---|------|-------------|
| N1 | N4 | CPL | N1 rende possibile N4 |
| N4 | N7 | CPL | N4 rende possibile N7 |
| N5 | N7 | VIN | N5 e N7 si limitano reciprocamente |
| N2 | N3 | MED | N2 media l'attivazione di N3 |
| N2 | N1 | CMP | N2 può compensare fragilità di N1 |
| N5 | N6 | VIN | N5 vincola lievemente N6 |
| N7 | N3 | CPL | N7 sostiene N3 |

### Slide 5.5 — Toggle delle configurazioni

Su schermi larghi (> 1200px): griglia 2×2 con tutte e quattro le configurazioni visibili.
Su schermi medi (900–1200px): due card visibili alla volta, con pulsanti ← → per scorrere.
Su schermi stretti (< 900px): una card alla volta con pulsanti.

Aggiungere un indicatore "A / B / C / D" sempre visibile per orientarsi.

### Slide 5.7 — Integrazione con CASO_GUIDA

La CE della slide 5.7 deve essere recuperata da `window.CASO_GUIDA.pipeline.ce` — non duplicare i dati. Verificare che la struttura dell'oggetto corrisponda a quanto definito in `ISTRUZIONI_CLAUDE_CODE.md`.

### Transizione M4 → M5

All'entrata nel modulo, 2-3 righe di transizione: *"Nel Modulo 4 hai visto come lo stesso Nodo genera domande diverse nei diversi contesti. In questo modulo scopriamo che i Nodi non lavorano mai da soli: si sostengono, si limitano, si compensano. È la configurazione complessiva che dice qualcosa di significativo."*
