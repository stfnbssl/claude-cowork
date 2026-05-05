# Modulo 3 — Il Nodo Trasversale
**Numero slide**: 9
**Colore accent**: `#e67e22`
**Tipo prevalente**: standard + interactive

---

## Dati globali del modulo

Definire in `m03.js` le seguenti costanti. Sono la sorgente di dati per tutte le slide del modulo.

```javascript
const SETTE_PROPRIETA = [
  {
    id: 'p1',
    numero: '1',
    nome: 'Multi-asseità costitutiva',
    testo: 'Coinvolge simultaneamente almeno tre assi strutturali. Se appartiene a un asse solo, non è un Nodo — è una dimensione di quell\'asse.',
    test: 'Quanti assi sono contemporaneamente attivi in questa configurazione?'
  },
  {
    id: 'p2',
    numero: '2',
    nome: 'Emergenza non riducibile',
    testo: 'Produce configurazioni che non sono la somma dei singoli assi. Il tutto è strutturalmente diverso dalle parti: quello che emerge non sarebbe visibile guardando un asse alla volta.',
    test: 'Questa configurazione si vede già nel singolo asse, o appare solo dall\'intreccio?'
  },
  {
    id: 'p3',
    numero: '3',
    nome: 'Traducibilità interrogabile',
    testo: 'Genera domande professionali reali, osservabili e discutibili tra discipline diverse. Se non produce domande concrete per il professionista, non è un Nodo.',
    test: 'Questo Nodo genera almeno tre domande usabili in contesti professionali diversi?'
  },
  {
    id: 'p4',
    numero: '4',
    nome: 'Neutralità normativa',
    testo: 'Non dice cosa fare, non valuta adeguatezza, non definisce normalità. Può descrivere configurazioni fragili o disorganizzate senza per questo prescrivere o classificare.',
    test: 'Questo Nodo può essere letto senza implicare cosa si deve fare?'
  },
  {
    id: 'p5',
    numero: '5',
    nome: 'Generatività operativa',
    testo: 'Permette la costruzione di operatori di lettura e famiglie di output diverse. Se non genera nulla in direzione della Fase 3, manca di questa proprietà.',
    test: 'Da questo Nodo posso ricavare operatori, template e famiglie di output?'
  },
  {
    id: 'p6',
    numero: '6',
    nome: 'Ricorrenza strutturale',
    testo: 'È una modalità organizzativa ricorrente dello sviluppo, non un evento episodico. Si riscontra in situazioni molto diverse mantenendo la stessa struttura di fondo.',
    test: 'Questa configurazione è riconoscibile in ambulatorio, al nido, a casa e in ricerca?'
  },
  {
    id: 'p7',
    numero: '7',
    nome: 'Necessità architetturale',
    testo: 'La sua assenza produce un vuoto teorico nel modello. Se lo si rimuove, il framework perde qualcosa di essenziale — non si può semplicemente sostituirlo con un altro Nodo.',
    test: 'Se tolgo questo Nodo, il modello perde la capacità di rendere conto di qualcosa di strutturalmente rilevante?'
  }
];

const SETTE_NODI = [
  {
    id: 'n1',
    numero: 'N1',
    colore: '#e67e22',
    nome: 'Regolazione / Integrazione dell\'esperienza',
    struttura: 'Capacità del sistema bambino-ambiente di mantenere continuità esperienziale nel tempo davanti a stimoli, frustrazioni, cambiamenti o sovraccarichi.',
    assi: ['1', '2', '4'],
    domande: [
      'L\'esperienza si mantiene o collassa?',
      'Il genitore riesce a sostenere una ripresa del campo?',
      'La regolazione avviene solo per contenimento fisico o anche attraverso voce, sguardo, ritmo?',
      'Dopo il momento critico, il bambino può recuperare disponibilità al contesto?'
    ],
    situazione: 'Durante una visita pediatrica, il bambino viene spogliato per l\'esame. Si irrigidisce, piange, cerca il genitore. Il genitore lo prende in braccio, gli parla piano. Dopo alcuni momenti il bambino guarda il pediatra e consente di proseguire.',
    lettura_valida: 'L\'esperienza si disorganizza durante il passaggio corporeo della visita, ma il campo relazionale permette una ripresa parziale. La regolazione non è autonoma, ma è sostenuta dalla presenza adulta.',
    errore: '"Il bambino è poco collaborativo." — Moralizza e attribuisce un tratto stabile. N1 chiede invece: che cosa succede all\'esperienza quando aumenta il carico?',
    famiglie: ['Osservativa: traccia su sequenze di disorganizzazione e recupero', 'Formativa: per pediatri su regolazione e clima ambulatoriale', 'Restitutiva: linguaggio per il genitore sul pianto senza colpevolizzazione', 'Organizzativa: rendere la visita più abitabile']
  },
  {
    id: 'n2',
    numero: 'N2',
    colore: '#27ae60',
    nome: 'Campo relazionale / Co-regolazione',
    struttura: 'Organizzazione reciproca degli stati tra bambino e ambiente umano: il modo in cui adulto e bambino si modulano, si amplificano, si interrompono o si sostengono reciprocamente.',
    assi: ['1', '2', '3'],
    domande: [
      'Il campo sostiene, amplifica o disorganizza?',
      'Il bambino può usare l\'adulto come sostegno senza perdere iniziativa?',
      'La risposta adulta sostituisce l\'azione del bambino o la rende nuovamente possibile?',
      'Il campo relazionale permette di trasformare la frustrazione in prosecuzione dell\'esperienza?'
    ],
    situazione: 'Al nido, un bambino non riesce ad infilare un pezzo in un gioco a incastro. Si agita e guarda l\'educatrice. Lei si avvicina, dice: "È difficile, proviamo a girarlo?". Il bambino prova di nuovo. Quando entra, sorride.',
    lettura_valida: 'Il campo relazionale sostiene la continuità dell\'esperienza: l\'adulto riconosce la difficoltà, non si sostituisce, e permette al bambino di restare soggetto dell\'azione.',
    errore: '"L\'educatrice è brava perché aiuta nel modo giusto." — Valutativo. In F2 non si giudica l\'adulto: si descrive la configurazione relazionale.',
    famiglie: ['Formativa: differenza tra sostegno e sostituzione', 'Osservativa: scheda neutra sulle forme di co-regolazione', 'Restitutiva: traccia per parlare con genitori o educatori', 'Ricerca: confronto qualitativo di sequenze adulto-bambino']
  },
  {
    id: 'n3',
    numero: 'N3',
    colore: '#2980b9',
    nome: 'Accesso al mondo condiviso simbolico',
    struttura: 'Transizione da azione individuale a significato condiviso. Non coincide con il linguaggio o il pointing, anche se può manifestarsi attraverso questi fenomeni.',
    assi: ['1', '2', '5', '6'],
    domande: [
      'Il bambino condivide o usa l\'altro?',
      'L\'oggetto diventa comune o resta solo manipolato?',
      'Il gesto del bambino apre uno scambio?',
      'La parola adulta sostiene il mondo condiviso o lo sostituisce?',
      'Il bambino cerca risposta dell\'adulto o lo usa solo in modo funzionale?'
    ],
    situazione: 'Durante la lettura di un libro illustrato, il bambino indica un cane, vocalizza "bau", guarda il genitore e torna a guardare la figura. Il genitore risponde: "Sì, è un cane!". Il bambino sorride e indica di nuovo.',
    lettura_valida: 'Il bambino trasforma l\'immagine del libro in un\'occasione di scambio: guarda, indica, vocalizza e cerca la risposta dell\'adulto. Il libro diventa mediatore di mondo.',
    errore: '"Sa indicare" o "Ha buone competenze referenziali." — Il pointing può essere manifestazione del Nodo, ma non è il Nodo. Riduce una configurazione strutturale a un comportamento.',
    famiglie: ['Osservativa: scheda su sequenze di mondo condiviso', 'Formativa: leggere la condivisione oltre il linguaggio', 'Restitutiva: parlare ai genitori dell\'indicare e del mostrare', 'Ricerca: analisi micro-sequenze libro-gesto-sguardo']
  },
  {
    id: 'n4',
    numero: 'N4',
    colore: '#8e44ad',
    nome: 'Apertura / Esplorabilità del mondo',
    struttura: 'Equilibrio tra sicurezza relazionale e possibilità di espansione. Come il bambino si orienta verso un mondo che eccede la situazione presente senza perdere il riferimento relazionale.',
    assi: ['1', '4', '5'],
    domande: [
      'Il bambino può esplorare mantenendo un riferimento relazionale?',
      'La vicinanza all\'adulto blocca o sostiene l\'apertura?',
      'Il mondo nuovo è affrontato come minaccia, possibilità o campo saturo?',
      'L\'esplorazione procede per cicli di andata e ritorno?'
    ],
    situazione: 'Un bambino entra per la prima volta al nido. Resta vicino al genitore, poi si avvicina a un cesto di oggetti, ne prende uno, torna verso il genitore. Dopo alcuni minuti, esplora una zona più ampia.',
    lettura_valida: 'L\'esplorazione si costruisce attraverso cicli brevi di allontanamento e ritorno: il riferimento adulto non sostituisce l\'apertura al mondo, ma la rende possibile.',
    errore: '"Il bambino è timido." — Trasforma una configurazione situata in un tratto psicologico stabile. N4 chiede: quanto il mondo è esplorabile per questo bambino, in questa situazione, con questi sostegni?',
    famiglie: ['Pedagogica: leggere l\'inserimento al nido', 'Genitoriale: comprendere andate e ritorni', 'Osservativa: griglia neutra sull\'esplorazione situata', 'Organizzativa: predisposizione degli spazi']
  },
  {
    id: 'n5',
    numero: 'N5',
    colore: '#e74c3c',
    nome: 'Separazione / Limite reale',
    struttura: 'Incontro tra l\'intenzionalità del bambino e la resistenza del reale. Se il limite può diventare forma, confine, mediazione — o se produce solo interruzione e ritiro.',
    assi: ['2', '3', '4'],
    domande: [
      'Il limite organizza o collassa?',
      'Il genitore riesce a porre il limite senza ritirare la relazione?',
      'Il bambino può protestare senza perdere completamente il contatto?',
      'Dopo il limite, esiste una possibilità di ripresa?',
      'Il limite genera apprendimento o ritiro?'
    ],
    situazione: 'A casa, il bambino vuole un oggetto fragile. Il genitore dice "No". Il bambino protesta, piange brevemente, guarda il genitore. Il genitore offre un altro oggetto. Dopo un\'esitazione, il bambino lo prende e riprende il gioco.',
    lettura_valida: 'Il limite produce una rottura breve, ma non distrugge il campo: la protesta del bambino resta dentro una relazione che può offrire continuità e riorganizzazione.',
    errore: '"Il bambino fa i capricci." — Moralizza e cancella la funzione strutturale del limite. N5 non chiede se il bambino obbedisce, ma come il campo regge l\'incontro con la resistenza del reale.',
    famiglie: ['Restitutiva: parlare del limite senza colpevolizzare', 'Formativa: distinguere limite organizzante e distruttivo', 'Genitoriale: osservare le sequenze di rottura e ripresa', 'Educativa: riflessioni su regole, confini, continuità relazionale']
  },
  {
    id: 'n6',
    numero: 'N6',
    colore: '#16a085',
    nome: 'Continuità temporale del Sé nascente',
    struttura: 'Persistenza dell\'esperienza attraverso discontinuità, interruzioni, frustrazioni. La possibilità che il bambino non sia ogni volta ricominciato da zero dall\'evento che interrompe.',
    assi: ['1', '2', '5'],
    domande: [
      'Il bambino riprende dopo fratture?',
      'Dopo l\'interruzione, la sequenza può riprendere?',
      'L\'adulto nomina la frattura senza cancellarla?',
      'La nuova azione conserva un legame con quella precedente?',
      'La perdita distrugge il campo o apre una ricostruzione?'
    ],
    situazione: 'Durante un gioco con costruzioni, una torre cade. Il bambino resta immobile, si lamenta. L\'adulto dice: "È caduta. Possiamo rifarla". Il bambino prende un pezzo, poi un altro, ricomincia più lento. Poi indica la torre nuova e guarda l\'adulto.',
    lettura_valida: 'La caduta interrompe l\'azione, ma non cancella la continuità dell\'esperienza: attraverso la mediazione adulta, il bambino riprende il filo e ricostruisce una direzione.',
    errore: '"Il bambino non tollera la frustrazione." — Troppo generale e tendenzialmente psicologizzante. N6 chiede di osservare se e come l\'esperienza può continuare dopo una frattura.',
    famiglie: ['Osservativa: tracce sulle sequenze interruzione-ripresa', 'Formativa: frustrazione, continuità e ricostruzione', 'Restitutiva: valorizzare il "riprendere" più che il "riuscire"', 'Ricerca: micro-sequenze di rottura e recupero']
  },
  {
    id: 'n7',
    numero: 'N7',
    colore: '#f39c12',
    nome: 'Desiderio / Direzione dell\'esperienza',
    struttura: 'Orientamento attivo verso possibilità significative. Non è preferenza, motivazione o scelta: è la direzione che l\'esperienza assume quando qualcosa acquista valore per il bambino.',
    assi: ['1', '5', '6'],
    domande: [
      'L\'iniziativa è presente?',
      'L\'azione del bambino mostra una direzione o resta dispersa?',
      'Qualcosa nel campo acquisisce valore?',
      'Il bambino può sostenere una sequenza orientata?',
      'C\'è saturazione? C\'è ritiro? C\'è espansione?'
    ],
    situazione: 'In una stanza con molti giochi, il bambino passa rapidamente da un oggetto all\'altro. Poi vede una cucina giocattolo, si ferma, apre uno sportello, fa finta di mescolare. Quando l\'adulto dice "Stai cucinando?", il bambino sorride e porge il cucchiaio.',
    lettura_valida: 'Dopo una fase dispersa, il bambino trova una direzione nell\'azione simbolica: l\'oggetto acquista valore, la sequenza si stabilizza, l\'adulto viene incluso nel gioco.',
    errore: '"Al bambino piace giocare con la cucina." — Può essere vero, ma è troppo povero. N7 non riguarda solo una preferenza: riguarda l\'emergere di una direzione significativa dell\'esperienza.',
    famiglie: ['Osservativa: traccia sulle forme dell\'iniziativa', 'Pedagogica: interesse, gioco e direzione dell\'esperienza', 'Genitoriale: valore delle iniziative spontanee', 'Formativa: differenza tra stimolare e riconoscere']
  }
];
```

---

## SLIDE 3.1 — Il problema che il Nodo risolve

**Tipo**: `standard`
**Titolo**: Tra la fondazione e la pratica
**Sottotitolo**: Perché serve un livello intermedio

**Contenuto principale**:

Layout a tre blocchi verticali collegati da frecce — ripresa dello schema F1→F2→F3 del Modulo 0, ma zoomato sul passaggio F1→F2.

**Blocco F1** (colore --color-f1, opacità ridotta — "viene da lì"):

Gli assi strutturali sono astratti per definizione. Descrivono dimensioni dello sviluppo con precisione ontologica. Ma proprio per questo **non si usano direttamente nel lavoro professionale**.

Un pediatra non può concludere una visita scrivendo: "Asse 1 presente, Asse 4 in tensione." Un educatore non può osservare un bambino usando "Asse 5 — Desiderio" come categoria operativa.

**Freccia verso il basso** con domanda:
*Come si passa dalla fondazione alla leggibilità professionale senza perdere complessità?*

**Blocco centrale** — Il Nodo (colore --color-accent, evidenziato):

Il **Nodo Trasversale** è il livello intermedio che risolve questo problema.

Si colloca tra la struttura ontologica (assi, Livello 1) e i dispositivi operativi (Fase 3, Livello 3). È il punto dove:

- più assi si incontrano in una **configurazione riconoscibile**
- la configurazione diventa **interrogabile** da professionisti di discipline diverse
- la complessità ontologica non viene perduta ma **tradotta**

**Blocco F3** (colore --color-f3, opacità ridotta — "dove si arriva):

Senza il Nodo, il passaggio agli strumenti operativi produce le anomalie viste nel Modulo 1: riduzione, tecnicizzazione, normatività implicita.

**Nota metodologica in footer**:
*Il Nodo non è un nuovo asse, non è un'entità aggiuntiva, non è un meccanismo causale. È una configurazione teorica che rende intelligibili dinamiche già presenti negli assi — e le rende interrogabili.*

---

## SLIDE 3.2 — Definizione canonica

**Tipo**: `standard`
**Titolo**: Cos'è un Nodo Trasversale
**Sottotitolo**: La definizione canonica

**Contenuto principale**:

Layout a colonna singola centrata, abbondante spazio bianco. La slide è quasi tutta occupata dalla definizione e dalla sua scomposizione.

**La definizione** — grande blockquote centrale:

> *"Un Nodo Trasversale è una configurazione ontogenetica ricorrente in cui più assi strutturali si co-organizzano producendo una trasformazione emergente e strutturalmente necessaria, fenomenicamente densa e potenzialmente traducibile."*

**Sotto, la scomposizione parola per parola**:

Cinque chip/tag cliccabili, ognuno con una parola-chiave dalla definizione. Cliccandone uno, si apre un pannello espanso sotto (uno alla volta):

**`configurazione ontogenetica`**
→ *Non è un evento casuale: è un modo in cui lo sviluppo si organizza strutturalmente, ricorrente in bambini di età, contesti e culture diverse.*

**`più assi si co-organizzano`**
→ *Non appartiene a un asse solo. Emerge dall'intreccio simultaneo di almeno tre assi strutturali.*

**`trasformazione emergente`**
→ *Quello che produce non è la somma degli assi coinvolti. È qualcosa di nuovo che appare solo quando quegli assi lavorano insieme.*

**`strutturalmente necessaria`**
→ *Non è accessoria: la sua assenza produce un vuoto teorico. Il modello non può rendere conto di quel fenomeno senza di essa.*

**`potenzialmente traducibile`**
→ *Può diventare interrogabile da discipline diverse. Genera domande professionali usabili in ambulatorio, al nido, a casa, in ricerca.*

**Sezione inferiore — tre "non è"**:

Tre chip in rosso affiancati:

❌ Non è un nuovo asse
❌ Non è un meccanismo causale
❌ Non è un caso clinico

In testo sotto: *È la forma in cui assi già definiti si rendono leggibili come configurazione.*

---

## SLIDE 3.3 — Le sette proprietà necessarie

**Tipo**: `interactive`
**Titolo**: Sette proprietà, tutte necessarie
**Sottotitolo**: Un Nodo è valido solo se le soddisfa tutte

**Contenuto principale**:

Griglia 4 + 3 (quattro card in prima riga, tre in seconda) con le sette proprietà. Usa i dati da `SETTE_PROPRIETA`.

Ogni card è **espandibile** (usa `ExpandableCards` con `multiOpen: true` — più card possono essere aperte contemporaneamente):

**Fronte della card** (stato compatto):
- Numero grande in --color-accent (1–7)
- Nome della proprietà in grassetto
- Testo breve della proprietà (prima frase del campo `testo`)
- Icona ↓ che invita all'espansione

**Card espansa** (aggiunge sotto il fronte):
- Testo completo della proprietà (campo `testo`)
- Separatore
- Domanda-test in corsivo, sfondo tenue: *"Test: [campo `test`]"*

**Elemento visivo importante**: under la griglia, in grassetto centrato:

*Un elemento è considerato Nodo solo se soddisfa TUTTE e sette le condizioni.*
*Se manca anche una sola, è qualcosa di diverso — un asse, un dominio, una variabile, un comportamento.*

**Nota in footer**:
*Le sette proprietà si applicano anche come criteri di verifica durante la costruzione della pipeline: se il Nodo scelto non soddisfa tutte e sette, la catena di traducibilità non regge.*

---

## SLIDE 3.4 — Asse vs. Nodo: la differenza fondamentale

**Tipo**: `comparison`
**Titolo**: Asse e Nodo non sono la stessa cosa
**Sottotitolo**: Una distinzione strutturalmente necessaria

**Contenuto principale**:

**Sezione superiore — perché la distinzione conta**:

Questa distinzione non è accademica. Confondere Asse e Nodo porta a due errori opposti:
- trattare un Nodo come se fosse una dimensione permanente e solitaria (e perderne la multi-asseità)
- trattare un asse come se fosse un evento situato (e perderne la funzione fondativa)

**Sezione centrale — tabella comparativa** (componente `ComparisonPanel` adattato a tabella):

| | **Asse** | **Nodo** |
|---|---|---|
| **Natura** | Dimensione strutturale permanente | Configurazione ricorrente |
| **Funzione** | Condizione di possibilità | Evento strutturato ad alta densità |
| **Temporalità** | Sempre attivo, non è processo situato | Processo situato in un campo specifico |
| **Soggetto** | Descrive il campo dello sviluppo | Rende visibile l'interazione degli assi nel campo |
| **Relazione con gli altri** | Non presuppone gli assi successivi | Presuppone almeno tre assi contemporaneamente |
| **Forma** | Costante | Emergente |

**Sezione inferiore — esempio visivo**:

Due colonne:

**Colonna sinistra — Asse 2 (affettivo-morale)**:
*È sempre presente. Descrive come il bambino riconosce l'altro come portatore di esperienza propria. Non compare e scompare: orienta tutte le relazioni del bambino lungo tutto lo sviluppo.*

**Colonna destra — N2 (Campo relazionale / Co-regolazione)**:
*Appare quando Asse 1, Asse 2 e Asse 3 si co-organizzano in una specifica configurazione: la modulazione reciproca degli stati tra bambino e adulto. Non è sempre "attivato": è una configurazione che si osserva in situazioni concrete.*

**Regola in footer**:
*Se stai descrivendo qualcosa che è sempre presente → probabilmente è un asse.*
*Se stai descrivendo qualcosa che emerge da più assi in una situazione specifica → probabilmente è un Nodo.*

---

## SLIDE 3.5 — La logica dell'Atlante

**Tipo**: `standard`
**Titolo**: Nodo → contesti → domande
**Sottotitolo**: Non il contrario

**Contenuto principale**:

**Sezione superiore — il principio**:

Il progetto segue una logica strutturale precisa, che distingue questo metodo da una raccolta di buone pratiche:

Grande freccia/schema visivo centrato:

```
         NODO
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
Clinico  Pedag. Genitoriale  Istituz.
    │     │     │              │
 domanda  dom.  dom.          dom.
 diversa  div.  div.          div.
```

Sotto lo schema:
*I contesti non definiscono lo sviluppo: interrogano strutture già definite.*

**Sezione centrale — le due logiche a confronto**:

Due card affiancate con colori diversi:

**Card verde — Logica del metodo**:
`NODO → contesti diversi → domande diverse`

I Nodi vengono definiti *prima* delle contestualizzazioni applicative, per una ragione metodologica: chi guarda lo sviluppo da discipline diverse deve poter leggere la stessa configurazione con linguaggi diversi — senza che ogni disciplina si inventi il proprio modello.

**Card rossa — Logica alternativa (da evitare)**:
`Contesti → nodi diversi`

Se ogni contesto produce i propri Nodi, si ottiene frammentazione e colonizzazione disciplinare. La pediatria osserva "regolazione", la pedagogia osserva "cura", il counseling osserva "attaccamento" — e non si parlano più.

**Sezione inferiore — cosa significa l'Atlante**:

I sette Nodi non sono stati ricavati dai casi clinici, dai contesti educativi o dalle pratiche genitoriali. Sono stati definiti a partire dalla struttura del modello — poi applicati ai diversi contesti.

Questo è ciò che li rende **trasversali**: lo stesso N3 genera domande diverse in ambulatorio, al nido, a casa e nei servizi, ma la struttura del Nodo resta identica.

*Questa è esattamente la differenza tra una metodologia e una raccolta di buone pratiche.*

---

## SLIDE 3.6 — Il catalogo: N1–N4

**Tipo**: `interactive`
**Titolo**: I sette Nodi Trasversali — parte I
**Sottotitolo**: N1 · N2 · N3 · N4

**Contenuto principale**:

Quattro card espandibili verticali (layout verticale, una sotto l'altra) usando il componente `ExpandableCards`. Usa i dati da `SETTE_NODI[0..3]` (N1–N4).

**Struttura di ogni card** (fronte, stato compatto):

```
[Badge colorato: N1] [Nome del Nodo]
[Struttura in una frase]
[Assi coinvolti come chip: Asse 1 · Asse 2 · Asse 4]
                                              [↓ Espandi]
```

**Card espansa** (aggiunge quattro sezioni):

*Situazione concreta*: il testo dal campo `situazione` — presentato in box tenue con sfondo molto chiaro. Introduce il Nodo con una scena reale prima della teoria.

*Domande professionali*: lista puntata dal campo `domande`. Usare un colore tenue per i bullets.

*Lettura valida*: testo dal campo `lettura_valida` in corsivo, preceduto da "✓".

*Errore da evitare*: testo dal campo `errore` in rosso tenue, preceduto da "⚠".

**Nota di navigazione**: sotto le quattro card, un link/pulsante discreto: *"N5 · N6 · N7 → slide successiva"*

---

## SLIDE 3.7 — Il catalogo: N5–N7

**Tipo**: `interactive`
**Titolo**: I sette Nodi Trasversali — parte II
**Sottotitolo**: N5 · N6 · N7

**Contenuto principale**:

Tre card espandibili con la stessa struttura della slide precedente. Usa i dati da `SETTE_NODI[4..6]` (N5–N7).

**Aggiunta rispetto alla slide 3.6** — sotto le tre card, un riquadro di sintesi comparativa:

**Tavola di sintesi dei sette Nodi** (tabella compatta, collassata di default, espandibile):

| Nodo | Situazione esemplare | Domanda guida | Errore tipico |
|------|---------------------|---------------|--------------|
| N1 Regolazione | Bambino alla visita pediatrica | L'esperienza si mantiene o collassa? | "È poco collaborativo" |
| N2 Co-regolazione | Bambino al gioco con l'educatrice | Il campo sostiene o amplifica? | "L'educatrice è brava/sbagliata" |
| N3 Mondo condiviso | Bambino col libro e il genitore | L'oggetto diventa comune? | "Sa indicare" |
| N4 Apertura/Esplorazione | Bambino che entra al nido | Il mondo è esplorabile? | "È timido" |
| N5 Limite reale | Bambino davanti a un "no" | Il limite organizza o collassa? | "Fa i capricci" |
| N6 Continuità | Torre che cade e si ricostruisce | Riprende dopo fratture? | "Non tollera la frustrazione" |
| N7 Desiderio | Bambino che trova direzione nel gioco | C'è iniziativa? C'è saturazione? | "Gli piace la cucina" |

Il pulsante per aprire la tavola: "Mostra la sintesi comparativa dei 7 Nodi".

---

## SLIDE 3.8 — Panoramica grafica dei 7 Nodi

**Tipo**: `diagram`
**Titolo**: I sette Nodi nell'architettura del modello
**Sottotitolo**: Invarianti strutturali e assi coinvolti

**Contenuto principale**:

Visualizzazione grafica della relazione tra assi (orizzontale, numeri 1–6) e Nodi (elementi circolari sopra, colorati individualmente). I Nodi sono connessi agli assi che li attivano tramite linee.

```
  Asse 1   Asse 2   Asse 3   Asse 4   Asse 5   Asse 6
    │         │        │        │        │        │
    ├────────┬┘        │        │        │        │
    │   N2◄──┘────────┤        │        │        │
    │        │        │        │        │        │
  N1◄────────┘        │     ───┤        │        │
    │                 │    │            │        │
    │       N5◄───────┴────┘            │        │
    │        │                          │        │
  N4◄────────┼────────────────          │        │
    │        │                 │        │        │
  N6◄────────┘                          │        │
    │                                   │        │
  N3◄─────────────────────────────────┬─┘────────┤
    │                                 │          │
  N7◄─────────────────────────────────┘          │
                                                  │
```

Versione più pulita: **disposizione radiale** dei 7 Nodi attorno a un cerchio centrale. Ogni Nodo è un nodo colorato. Cliccandoci, si evidenziano gli assi coinvolti (con colori corrispondenti) e compare una tooltip con nome + struttura sintetica.

**Due elementi testuali fissi**:

Sinistra (in piccolo): *Assi: dimensioni sempre attive*
Destra (in piccolo): *Nodi: configurazioni ricorrenti dell'intreccio*

**Sotto il grafico — regola fondamentale**:

*I sette Nodi sono invarianti strutturali: non cambiano passando tra contesti professionali. Cambia solo il tipo di domanda, il livello di osservazione, il tipo di output.*

---

## SLIDE 3.9 — Focus N3 nel caso-guida

**Tipo**: `narrative`
**Titolo**: N3 nel caso della lettura condivisa
**Sottotitolo**: Come il Nodo più rilevante si manifesta nella scena

**Contenuto principale**:

**Sezione superiore — la scena** (richiamo dal caso-guida, testo da `window.CASO_GUIDA.scena`):

Card narrativa in corsivo, sfondo --color-primary-light:

*"Il bambino prende il libro, lo apre, guarda alcune immagini, indica una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina l'immagine, sorride, aspetta. Il bambino torna a guardare il libro, gira pagina, poi mostra un'altra figura all'adulto."*

**Sezione centrale — tre colonne**:

**Colonna 1 — Perché N3?**:

N3 è il Nodo dominante perché nella scena il bambino non sta solo guardando un libro: sta tentando di *trasformare l'immagine in un'occasione di scambio*.

- Il libro non è un oggetto da manipolare → è un **mediatore di mondo**
- Il gesto di indicare non è un riflesso → è un **atto di condivisione**
- La vocalizzazione non è rumore → è **invito all'altro**
- L'alternanza di sguardo non è distrazione → è **ricerca di conferma nel campo comune**

**Colonna 2 — Gli assi attivati**:

Quattro chip con colori:
`Asse 1` — Il corpo (postura, orientamento, gesto) organizza l'esperienza
`Asse 2` — La risposta del genitore sostiene il campo
`Asse 5` — L'interesse del bambino per la figura orienta l'iniziativa
`Asse 6` — Il libro introduce un mondo simbolico-culturale condiviso

Sotto: *Sono attivi tutti e quattro gli assi che definiscono N3. L'emergenza è riconoscibile.*

**Colonna 3 — N2 come Nodo di sostegno**:

N2 (Campo relazionale / Co-regolazione) è presente in secondo piano: senza co-regolazione tra adulto e bambino, l'accesso al mondo condiviso non si produce. Il genitore che nomina, sorride e aspetta non sta solo "stimolando" — sta **mantenendo il campo** che rende possibile la condivisione.

*Sostegno (CPL): N2 → N3*

**Sezione inferiore — due letture a confronto**:

Tabella due colonne:

| Lettura riduttiva | Lettura N3 |
|------------------|------------|
| "Il bambino sa indicare" | "Il gesto apre uno scambio con l'adulto" |
| "Il genitore stimola bene" | "Il campo relazionale sostiene l'accesso al simbolico" |
| "Buon livello di sviluppo linguistico" | "La sequenza mostra N3 presente ma uso discontinuo (configurazione B)" |
| "Il bambino presta attenzione al libro" | "Il bambino usa il libro come mediatore verso un campo condiviso" |

**Chiusura del modulo**:

Testo centrato, leggero:

*Nel Modulo 4 vedremo come questo stesso Nodo — N3 — genera domande completamente diverse quando cambia il contesto professionale. Il Nodo resta invariante; la prospettiva si trasforma.*

Badge modulo successivo: `→ Modulo 4 — La Matrice Nodo × Contesto`

---

## Note per l'implementazione

### Slide 3.2 — Chip cliccabili

La scomposizione della definizione usa chips/tag cliccabili. Un solo pannello espanso alla volta (accordion). L'animazione di apertura è `slide-down` con opacity (200ms). I chip hanno uno stato `active` che li marca visivamente quando espansi.

### Slide 3.3 — ExpandableCards con multi-open

Usare `multiOpen: true` nel componente `ExpandableCards` per permettere di tenere più card aperte in contemporanea. Questo è utile in formazione: il docente può espandere tutte le proprietà per confrontarle.

Aggiungere un pulsante globale "Espandi tutto / Comprimi tutto" come per le flip-card del Modulo 1.

### Slide 3.6 e 3.7 — ExpandableCards con dati completi

Il testo della `situazione` è quello che nella formazione cattura l'attenzione: la scena concreta prima della struttura astratta. Presentarlo **sempre per primo** nell'espansione — prima delle domande professionali. Questo rispetta la logica del corso: si parte sempre dall'osservabile.

### Slide 3.8 — Il grafo

Se la visualizzazione radiale è troppo complessa, alternativa accettabile: una tabella visiva con Nodi in righe e Assi in colonne, con punti colorati nelle intersezioni pertinenti. Il risultato è simile ma molto più semplice da implementare.

Assi che attivano ogni Nodo:
- N1: A1 A2 A4
- N2: A1 A2 A3
- N3: A1 A2 A5 A6
- N4: A1 A4 A5
- N5: A2 A3 A4
- N6: A1 A2 A5
- N7: A1 A5 A6

### Transizione M2 → M3

All'entrata nel Modulo 3, richiamare brevemente che nel Modulo 2 abbiamo visto il Nodo come **terzo operatore della pipeline** (il "motore"). Ora lo approfondiamo come struttura in sé. Un testo di 2-3 righe al primo caricamento, poi dissolvenza verso la slide 3.1.
