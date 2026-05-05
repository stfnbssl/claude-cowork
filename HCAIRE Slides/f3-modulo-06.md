# f3-modulo-06 — La tipologia U1–U6
**Numero slide**: 8
**Colore accent**: `#16a085`
**Tipo prevalente**: interactive + standard

---

## Dati globali del modulo

Definire in `m06.js` le seguenti costanti. `SEI_TIPI_UNIVERSALI` è la sorgente primaria del modulo e viene usata nell'ExpandableCards e nella slide del caso-guida.

```javascript
// Sei forme universali di sostegno del campo
const SEI_TIPI_UNIVERSALI = [
  {
    id: 'u1',
    codice: 'U1',
    nome: 'Regolazione',
    colore: 'var(--color-u1)',
    badge: 'U1',
    forma_universale: 'Stabilizzare il registro regolativo del campo',
    descrizione: `Azioni che riducono la disorganizzazione del campo intervenendo
                  sul ritmo, sulla prevedibilità, sulla quantità di stimolazione.
                  Non è regolazione del bambino: è regolazione delle condizioni
                  che permettono al bambino di restare nel campo.`,
    nodo_tipico: 'N1 — Regolazione',
    colore_nodo: 'var(--color-n1)',
    funzioni_associate: ['stabilizzare', 'proteggere'],
    segnali_indicativi: [
      'N1↓ — campo disorganizzato',
      'T0–T1 — tenuta bassa o critica',
      'A– — campo non abitabile',
      'Contesto ad alto carico percettivo'
    ],
    forme_concrete: [
      'Ridurre il numero di adulti presenti o il volume dell\'ambiente',
      'Introdurre ritmo e prevedibilità nella sequenza (es. routine di avvio)',
      'Rallentare i movimenti e abbassare il tono della voce',
      'Ridurre la durata e la complessità dell\'interazione'
    ],
    esempio: `Durante il bilancio, il bambino si irrigidisce per l'esame fisico.
              Il pediatra rallenta, abbassa la voce, fa cenno al genitore di avvicinarsi.
              Il genitore parla al bambino piano, lo tiene. Il campo si riorganizza.
              Nessun materiale aggiuntivo, nessuna tecnica specifica: solo
              regolazione delle condizioni relazionali e ambientali del campo.`,
    combinazioni_tipiche: ['U5'],
    avvertimento: `Non è "calmarlo": è riorganizzare le condizioni esterne
                   del campo in modo che il sistema bambino-adulto-contesto
                   possa reggere. L'azione è sull'adulto e sul setting, non sul bambino.`
  },
  {
    id: 'u2',
    codice: 'U2',
    nome: 'Sintonizzazione',
    colore: 'var(--color-u2)',
    badge: 'U2',
    forma_universale: 'Seguire e rispecchiare l\'iniziativa del bambino senza dirigerla',
    descrizione: `Azioni che rispecchiano il ritmo, il gesto, la vocalizzazione o
                  l'intenzione del bambino, rendendola condivisibile senza modificarla.
                  La sintonizzazione non corregge, non anticipa, non riempie:
                  crea uno spazio in cui l'esperienza del bambino diventa relazionalmente visibile.`,
    nodo_tipico: 'N2 — Campo relazionale / Co-regolazione',
    colore_nodo: 'var(--color-n2)',
    funzioni_associate: ['mediare', 'ampliare'],
    segnali_indicativi: [
      'N2↑ — campo relazionale attivo',
      'R: N2→N3 — transizione in corso',
      'D↗ — espansione in atto',
      'Bambino con iniziativa presente ma risposta adulta direttiva'
    ],
    forme_concrete: [
      'Nominare ciò che il bambino fa, senza commentare o valutare',
      'Attendere la risposta del bambino prima di agire o parlare',
      'Rispecchiare il gesto o la vocalizzazione con variazione minima',
      'Seguire la sequenza del bambino senza anticiparne i passi'
    ],
    esempio: `Nel caso-guida: il bambino indica un'immagine e vocalizza.
              Il genitore nomina ciò che il bambino ha indicato — non un'altra immagine.
              Aspetta. Il bambino si orienta di nuovo verso il libro, gira pagina.
              Il genitore aspetta ancora. La sintonizzazione non aggiunge:
              riflette e lascia spazio perché la sequenza possa continuare.`,
    combinazioni_tipiche: ['U4', 'U3'],
    avvertimento: `La sintonizzazione non è approvazione né rinforzo.
                   Non si tratta di rispondere "bravo!" — si tratta di rendere
                   l'esperienza del bambino relazionalmente presente.
                   L'adulto non diventa uno specchio passivo: rimane presente e responsivo.`
  },
  {
    id: 'u3',
    codice: 'U3',
    nome: 'Apertura',
    colore: 'var(--color-u3)',
    badge: 'U3',
    forma_universale: 'Introdurre novità tollerabile che apre il campo a nuove possibilità',
    descrizione: `Azioni che ampliano la gamma di esperienze disponibili nel campo,
                  introducendo un elemento nuovo in modo che non produca sovraccarico.
                  L'apertura non è stimolazione generica: è calibrata al campo attuale
                  (T e A devono reggere) e lascia al bambino la scelta se avvicinarsi.`,
    nodo_tipico: 'N4 — Apertura / Esplorazione · N7 — Desiderio',
    colore_nodo: 'var(--color-n4)',
    funzioni_associate: ['ampliare'],
    segnali_indicativi: [
      'N4↓ o N7~ in campo stabile',
      'T2–T3 — tenuta sufficiente',
      'A± o A+ — campo abitabile',
      'D→ — stabilità senza espansione evolutiva'
    ],
    forme_concrete: [
      'Posizionare un oggetto nuovo vicino a quelli familiari senza commentarlo',
      'Introdurre una variazione nella routine (sorpresa tollerabile)',
      'Aprire una possibilità di esplorazione lasciando il bambino libero di avvicinarsi',
      'Ampliare il repertorio dell\'adulto (nuovi gesti, nuove modulazioni vocali)'
    ],
    esempio: `Al nido, un bambino con buona regolazione ma poco movimento esplorativo.
              L'educatrice posiziona un oggetto non familiare accanto agli oggetti che
              il bambino usa di solito. Non lo nomina, non lo mostra. Lascia.
              Il bambino si avvicina, lo esplora, lo abbandona.
              Questo è apertura: il campo ha ricevuto una possibilità, non un compito.`,
    combinazioni_tipiche: ['U2', 'U6'],
    avvertimento: `L'apertura richiede che il campo regga (T2+). Su un campo T0–T1,
                   la novità amplifica la disorganizzazione. La combinazione U3+U1
                   (apertura su campo stabilizzato) è valida — U3 da sola su T0 è un errore.`
  },
  {
    id: 'u4',
    codice: 'U4',
    nome: 'Mediazione Simbolica',
    colore: 'var(--color-u4)',
    badge: 'U4',
    forma_universale: 'Usare oggetti, linguaggio o simboli come mediatori dell\'esperienza condivisa',
    descrizione: `Azioni che trasformano un oggetto, una parola o un'immagine in un
                  mediatore dell'incontro relazionale. Non si usa l'oggetto per istruire
                  il bambino: si usa l'oggetto come ponte tra l'esperienza del bambino
                  e l'esperienza dell'adulto, rendendo lo scambio simbolicamente ricco.`,
    nodo_tipico: 'N3 — Mondo condiviso simbolico',
    colore_nodo: 'var(--color-n3)',
    funzioni_associate: ['mediare'],
    segnali_indicativi: [
      'N3~ — accesso al mondo condiviso in transizione',
      'R: N2→N3 — campo relazionale spinge verso condivisione simbolica',
      'Oggetto presente nella scena che il bambino ha già indicato o toccato'
    ],
    forme_concrete: [
      'Nominare l\'immagine che il bambino indica con una frase breve e condivisibile',
      'Espandere senza correggere: "Sì, il cane — e guarda qui..."',
      'Usare il libro, il gioco o l\'oggetto come terreno di incontro, non come materiale didattico',
      'Mantenere il riferimento simbolico condiviso senza sovraccaricarlo di significati'
    ],
    esempio: `Nel caso-guida: il libro illustrato non è un testo da leggere e un sussidio didattico.
              È il mediatore simbolico dell'incontro bambino-genitore.
              Il genitore nomina le immagini che il bambino indica — non le immagini che
              lui ritiene importanti. Il libro diventa il campo condiviso dentro il quale
              si produce la transizione N2→N3.`,
    combinazioni_tipiche: ['U2', 'U6'],
    avvertimento: `La mediazione simbolica non è insegnamento del linguaggio.
                   Non si tratta di "stimolare il lessico": si tratta di rendere
                   lo scambio simbolicamente denso e condivisibile.
                   Il bambino non impara parole: esperisce che l'esperienza può essere condivisa.`
  },
  {
    id: 'u5',
    codice: 'U5',
    nome: 'Limite Generativo',
    colore: 'var(--color-u5)',
    badge: 'U5',
    forma_universale: 'Stabilire limiti che generano lo spazio dell\'esperienza invece di bloccarla',
    descrizione: `Azioni che introducono una discontinuità, un confine o una fine — non
                  per bloccare l'esperienza, ma per darle forma. Il limite generativo non è
                  la negazione dell'esperienza: è ciò che la rende possibile come esperienza
                  limitata, finita, e quindi ripetibile. Senza limite, l'esperienza è informe.`,
    nodo_tipico: 'N5 — Limite reale · N1 — Regolazione',
    colore_nodo: 'var(--color-n5)',
    funzioni_associate: ['proteggere', 'stabilizzare'],
    segnali_indicativi: [
      'N5~ o N5↓ — il limite è assente o non tollerato',
      'Difficoltà nella transizione tra attività',
      'Assenza di discontinuità: l\'esperienza non ha "fine" riconoscibile',
      'Contesto senza struttura temporale riconoscibile'
    ],
    forme_concrete: [
      'Anticipare verbalmente la fine di un\'attività prima che avvenga',
      'Introdurre una routine di chiusura riconoscibile (gesto, frase, azione)',
      'Mantenere la discontinuità senza negoziare: il limite è condiviso, non imposto',
      'Lasciare che il bambino esperisca la fine senza sostituirla immediatamente'
    ],
    esempio: `Al nido, al momento del riordino, l'educatrice annuncia: "Adesso mettiamo via."
              Non aspetta che il bambino finisca — lo anticipa mentre finisce.
              La sequenza è: annuncio → azione congiunta → pausa → attività successiva.
              Il limite non è un "no": è una struttura temporale che l'esperienza
              può concludere e quindi ricominciare.`,
    combinazioni_tipiche: ['U1', 'U2'],
    avvertimento: `Il limite generativo non è disciplina. Non si tratta di far obbedire:
                   si tratta di dare forma all'esperienza attraverso la discontinuità.
                   Un limite che produce disorganizzazione non è generativo — richiede
                   prima stabilizzazione (U1) e poi può essere reintrodotto.`
  },
  {
    id: 'u6',
    codice: 'U6',
    nome: 'Riattivazione del Desiderio',
    colore: 'var(--color-u6)',
    badge: 'U6',
    forma_universale: 'Riattivare la dimensione motivazionale quando il campo è stagnante',
    descrizione: `Azioni che restituiscono vitalità al campo quando il movimento evolutivo si
                  è fermato: il bambino non esplora, non ha iniziativa, il campo è fermo
                  pur essendo stabile. Non si tratta di "motivare" il bambino: si tratta
                  di modificare le condizioni del campo in modo che il desiderio possa
                  riemergere come orientamento spontaneo verso l'esperienza.`,
    nodo_tipico: 'N7 — Desiderio / Motivazione · N4 — Apertura',
    colore_nodo: 'var(--color-n7)',
    funzioni_associate: ['ampliare'],
    segnali_indicativi: [
      'N7~ o N7↓ — dimensione motivazionale assente o compressa',
      'Campo stabile ma senza movimento (D→ prolungata)',
      'Iniziativa spontanea del bambino assente o molto ridotta',
      'Adulto che riempie continuamente lo spazio senza lasciare pause'
    ],
    forme_concrete: [
      'Introdurre una pausa nel ritmo adulto per lasciare spazio all\'iniziativa del bambino',
      'Presentare una scelta concreta tra due possibilità tollerabili',
      'Creare una situazione incompleta che invita il bambino a completarla',
      'Ridurre la direttività adulta per lasciare emergere il desiderio spontaneo'
    ],
    esempio: `Il bambino che al nido non esplora, aspetta, replica.
              L'educatrice riduce le proposte e lascia una pausa di 30 secondi
              senza organizzare nulla. Il bambino guarda in giro, si orienta
              verso un cestino di oggetti. Si avvicina da solo.
              Non è stata introdotta novità (U3): è stato tolto l'eccesso di offerta
              perché il desiderio avesse spazio per emergere.`,
    combinazioni_tipiche: ['U3', 'U2'],
    avvertimento: `La riattivazione del desiderio non è motivazione estrinseca.
                   Non si tratta di premiare o lodare il bambino perché esplori.
                   Si tratta di modificare le condizioni del campo — spesso sottraendo
                   invece di aggiungere — perché il movimento evolutivo possa riattivarsi.`
  }
];

// Matrice tendenziale funzione → tipi universali (non meccanica: orientativa)
const MATRICE_FUNZIONE_TIPO = [
  {
    funzione: 'stabilizzare',
    funzione_colore: 'var(--color-fn-stabilizzare)',
    badge: 'STA',
    tipi_principali: ['U1', 'U5'],
    tipi_secondari: [],
    logica: `Stabilizzare richiede ridurre la disorganizzazione (U1: Regolazione)
             e dare forma all'esperienza attraverso la discontinuità (U5: Limite Generativo).
             I due tipi si combinano frequentemente in contesti di alta instabilità.`,
    nota: 'U5 in contesto di stabilizzazione è il limite che contiene, non che apre: il limite come protezione.'
  },
  {
    funzione: 'ampliare',
    funzione_colore: 'var(--color-fn-ampliare)',
    badge: 'AMP',
    tipi_principali: ['U3', 'U6'],
    tipi_secondari: ['U2'],
    logica: `Ampliare introduce possibilità nuove (U3: Apertura) e riattiva il desiderio
             di esplorazione (U6). La sintonizzazione (U2) spesso accompagna
             l'apertura: l'adulto segue l'avvicinamento del bambino alla novità.`,
    nota: 'U2 è secondario nell\'ampliamento: serve a sostenere l\'esplorazione che U3 ha aperto, non ad aprire.'
  },
  {
    funzione: 'mediare',
    funzione_colore: 'var(--color-fn-mediare)',
    badge: 'MED',
    tipi_principali: ['U2', 'U4'],
    tipi_secondari: [],
    logica: `Mediare sostiene una transizione già in corso: la sintonizzazione (U2)
             segue il ritmo del bambino senza dirigerlo, la mediazione simbolica (U4)
             usa oggetti o linguaggio come terreno condiviso dell'incontro.
             La combinazione U2+U4 è la più frequente nelle situazioni di mediazione.`,
    nota: 'Caso-guida: la lettura condivisa adulto-bambino (DBS) è U2+U4. La sintonizzazione segue il bambino; il libro è il mediatore simbolico.'
  },
  {
    funzione: 'proteggere',
    funzione_colore: 'var(--color-fn-proteggere)',
    badge: 'PRO',
    tipi_principali: ['U5', 'U1'],
    tipi_secondari: [],
    logica: `Proteggere previene il sovraccarico: il limite generativo (U5) riduce
             le richieste e le aspettative prima che producano disorganizzazione,
             la regolazione (U1) mantiene il registro del campo in condizioni
             di bassa stimolazione preventiva.`,
    nota: 'La differenza tra Stabilizzare e Proteggere si riflette nei tipi: stessa coppia U1+U5, ma U5 in Proteggere è preventivo — riduce prima che la crisi avvenga.'
  }
];

// Analisi U2+U4 per il caso-guida DBS
const CASO_GUIDA_M6 = {
  tipiScelti: ['U2', 'U4'],
  funzione: 'MEDIAZIONE',
  funzioneColore: 'var(--color-fn-mediare)',

  u2: {
    codice: 'U2',
    nome: 'Sintonizzazione',
    colore: 'var(--color-u2)',
    come_si_manifesta: `Il genitore segue il bambino: nomina ciò che lui ha indicato,
                        non ciò che il genitore ritiene importante.
                        Attende dopo ogni risposta. Non anticipa. Non riempie il silenzio.
                        Il ritmo è del bambino — l'adulto si sincronizza su di esso.`,
    micro_azioni_corrispondenti: [
      window.CASO_GUIDA_F3.f3.microAzioni[0],  // segue l'interesse del bambino
      window.CASO_GUIDA_F3.f3.microAzioni[1],  // nomina ciò che indica
      window.CASO_GUIDA_F3.f3.microAzioni[2]   // attende la risposta
    ]
  },

  u4: {
    codice: 'U4',
    nome: 'Mediazione Simbolica',
    colore: 'var(--color-u4)',
    come_si_manifesta: `Il libro illustrato non è un materiale didattico: è il mediatore.
                        Le immagini diventano il terreno condiviso dell'incontro.
                        Il genitore usa il linguaggio per rendere l'immagine condivisibile
                        — "Sì, il cane — e guarda qui..." — senza trasformarlo in lezione.`,
    micro_azioni_corrispondenti: [
      window.CASO_GUIDA_F3.f3.microAzioni[3]   // espande senza correggere
    ]
  },

  perche_non_u3: `U3 (Apertura) sarebbe inappropriato: N4↓ sconsiglia di introdurre
                  novità. Ampliare su un campo con esplorazione già ridotta
                  aumenta il carico su un nodo in tensione.`,
  perche_non_u6: `U6 (Riattivazione del Desiderio) non è indicato: il bambino
                  ha già iniziativa presente (indica, vocalizza, cerca l'adulto).
                  Il desiderio non è assente — è il campo che non lo sostiene abbastanza.`,
  perche_non_u1_u5: `U1 e U5 (Regolazione e Limite Generativo) non sono il focus:
                     il campo non è in disorganizzazione (N1~, T2). Non serve stabilizzare
                     né proteggere — serve sostenere la transizione già in corso.`
};
```

---

## SLIDE F3.6.1 — Dalla funzione alla forma

**Tipo**: `standard`
**Titolo**: Oltre la funzione: le forme universali
**Sottotitolo**: Lo stesso dispositivo può essere descritto in due modi

**Contenuto principale**:

Layout a colonna singola. Slide di apertura che stabilisce perché esiste la Tipologia U — e cosa aggiunge rispetto alla scelta della funzione già fatta in M4.

**Sezione superiore — il punto di arrivo di M4–M5**:

Due chip affiancati, separati da una freccia `→`:

```
[MEDIAZIONE]  →  [Template F3 compilato]
```

Sotto i chip, testo `--text-base` `--color-text-secondary`:
*Sappiamo la funzione. Sappiamo le micro-azioni. Sappiamo il campo bersaglio e l'indicatore di risonanza.*

*Il dispositivo è pronto.*

**Sezione centrale — la domanda di M6**:

Testo `--text-2xl`, centrato, con spazio verticale:

*"Ma cosa sta facendo, più in profondità, questo dispositivo?"*

Sotto, due righe `--text-base`, `--color-text-secondary`, centrate:

*Seguire il bambino senza dirigerlo. Usare il libro come terreno condiviso.*
*Questi sono gesti tecnici contestuali — e al tempo stesso forme universali.*

**Sezione inferiore — la distinzione**:

Due box affiancati, stessa dimensione, sfondo `--color-bg`, bordo `--color-border`:

**Box sinistra** — "Il livello della funzione":
*Descrive cosa il dispositivo fa al campo (Stabilizzare / Ampliare / Mediare / Proteggere).*
*È contestuale alla CE: varia al variare della configurazione.*
*Risponde alla domanda: quale funzione ha questa azione sul campo?*

**Box destra** — "Il livello del tipo universale":
*Descrive la forma dell'azione come modalità di sostegno dell'esperienza.*
*È trasversale ai contesti, ai professionisti, alle popolazioni.*
*Risponde alla domanda: quale forma prende il sostegno del campo in questa azione?*

Sotto i due box, freccia verso il basso con testo centrato:
*Un dispositivo si descrive sempre a entrambi i livelli. La funzione orienta la scelta; il tipo universale descrive la forma che l'azione prende nel campo.*

**Nota in footer**:
*La Tipologia U non è una classificazione di tecniche: è un vocabolario per descrivere le forme dell'incontro relazionale. La stessa forma (es. U2: Sintonizzazione) può essere espressa da dispositivi molto diversi in contesti molto diversi.*

---

## SLIDE F3.6.2 — La mappa dei sei tipi

**Tipo**: `diagram`
**Titolo**: Sei forme, una mappa
**Sottotitolo**: U1–U6: le forme universali di sostegno del campo relazionale

**Contenuto principale**:

Schema visivo centrale: sei blocchi disposti in due colonne di tre, con colori `--color-uX`. Non è un ExpandableCards — è una mappa panoramica che mostra la struttura dell'intera tipologia prima di esplorarla nel dettaglio.

**Layout schema** (3 righe × 2 colonne):

```
  [U1 Regolazione]          [U4 Mediazione Simbolica]
  [U2 Sintonizzazione]       [U5 Limite Generativo]
  [U3 Apertura]              [U6 Riattivazione del Desiderio]
```

Ogni blocco contiene:
- Codice grande (`U1`…`U6`) colorato `--color-uX`
- Nome in `--text-base` grassetto
- `forma_universale` in `--text-sm` corsivo
- Chip piccolo con nodo tipico (`N1`, `N2`…) nel colore del nodo

**Organizzazione visiva** — due annotazioni ai lati dello schema:

A sinistra, etichetta verticale tenue:
*← Campo più stabile — Campo in movimento →*

I tipi non seguono un ordine esatto di "stabilità", ma U1/U5 sono legati alla regolazione/contenimento e U3/U6 all'espansione/apertura. Questa indicazione visiva non è prescrittiva.

**Sezione inferiore — due principi organizzativi**:

Due box sfondo `--color-bg`, bordo `--color-border`, affiancati:

**Box 1** — "Non sono gerarchici":
*I sei tipi non hanno priorità intrinseca. U1 non è "più importante" di U6: la rilevanza dipende dalla CE. In contesti diversi, tipi diversi sono primari.*

**Box 2** — "Non sono esclusivi":
*I dispositivi reali combinano quasi sempre due tipi. La combinazione non è un'eccezione: è la norma. La Tipologia U descrive forme che si intrecciano nell'azione concreta.*

**Nota in footer**:
*Nella slide successiva esploriamo ogni tipo nel dettaglio. La mappa qui è solo orientamento: non classificare le azioni in un unico tipo prima di aver letto il campo.*

---

## SLIDE F3.6.3 — I sei tipi nel dettaglio

**Tipo**: `interactive`
**Titolo**: U1–U6: il dettaglio
**Sottotitolo**: Sei forme di sostegno, sei domande al campo

**Contenuto principale**:

Componente `ExpandableCards` con i dati da `SEI_TIPI_UNIVERSALI`, `multiOpen: false`.

**Elemento sopra le card** — sei chip fissi come indice rapido:

```
[● U1 Regolazione]  [● U2 Sintonizzazione]  [● U3 Apertura]
[● U4 Med. Simbolica]  [● U5 Limite Gen.]  [● U6 Riattivazione]
```

Ogni chip è cliccabile e apre la card corrispondente. Colori `--color-uX`. Il chip `U2` e `U4` hanno un piccolo badge aggiuntivo: `★ caso-guida` (verde tenue) — sono i tipi del caso DBS.

**Struttura card fronte** (stato compatto):

```
[Badge colorato: U1…U6]  [Nome grande]
[forma_universale — corsivo]
[Chip nodo tipico: es. "N1 · N2"]   [↓ Espandi]
```

**Card espansa** (cinque sezioni):

**Sezione 1 — Forma universale** (bordo sinistro `--color-uX`):
`descrizione` completo.

**Sezione 2 — Quando emerge nella CE** (sfondo `--color-bg`):
Etichetta *"Segnali indicativi:"* + lista `segnali_indicativi` come chip piccoli.

**Sezione 3 — Forme concrete** (lista ordinata):
Etichetta *"Come si manifesta:"* + lista `forme_concrete`.

**Sezione 4 — Esempio** (box narrativo, sfondo `--color-primary-light`, corsivo):
Etichetta *"Esempio:"* + testo `esempio`.

**Sezione 5 — Nota e combinazioni** (sfondo tenue, bordo `--color-warning`):
Due righe:
- *"Si combina con:"* chip `combinazioni_tipiche` colorati
- *"Avvertimento:"* testo `avvertimento` in `--text-sm`

**Pulsante globale** "Espandi tutto / Comprimi tutto" in alto a destra.

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-60`
- Label: I tipi descrivono forme, non tecniche
- Testo: *U2 (Sintonizzazione) non è la "Tecnica della Sintonizzazione". È una forma che può essere espressa da gesti, parole, movimenti, silenzi. I tipi descrivono la grammatica dell'azione — non il suo vocabolario tecnico.*

---

## SLIDE F3.6.4 — Funzione e tipo: la relazione

**Tipo**: `standard`
**Titolo**: Come funzione e tipo si collegano
**Sottotitolo**: Non una regola meccanica: un orientamento tendenziale

**Contenuto principale**:

Layout a colonna singola. Tabella orientativa funzione → tipi con spiegazione della logica. Dati da `MATRICE_FUNZIONE_TIPO`.

**Sezione superiore — il principio**:

Testo `--text-base`:
*La scelta della funzione (M4) orienta, ma non determina, il tipo universale.*
*La stessa funzione può esprimersi attraverso tipi diversi a seconda del campo specifico.*
*La matrice qui sotto è tendenziale: indica le associazioni più frequenti, non le uniche possibili.*

**Sezione centrale — tabella** (4 righe, una per funzione):

Tabella a quattro colonne:

| Funzione | Tipi principali | Tipi secondari | Logica |
|----------|-----------------|----------------|--------|

Ogni riga:
- **Colonna 1**: badge funzione colorato + nome
- **Colonna 2**: chip `--color-uX` per i tipi principali
- **Colonna 3**: chip `--color-uX` tenue per i secondari (se presenti) — oppure `—`
- **Colonna 4**: `logica` in `--text-sm` corsivo

La riga MEDIARE ha un bordo sinistro più spesso `var(--color-fn-mediare)` + etichetta piccola `★ caso-guida` a destra.

**Sezione inferiore — la nota sul giudizio professionale**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*La matrice non è un algoritmo. Casi reali producono configurazioni in cui:*
- *la funzione scelta suggerisce U1, ma il campo specifico richiede U5*
- *la funzione è Mediare, ma il campo ha anche bisogno di U1 per reggere*
- *due funzioni co-presenti richiedono tipi che normalmente non si combinano*

*In questi casi, la lettura del campo prevale sulla matrice. La matrice è utile per orientarsi — non per sostituire la lettura.*

**Nota in footer**:
*Nel caso-guida: funzione MEDIAZIONE → tipi principali U2+U4. La matrice lo indica correttamente. La slide successiva mostra perché.*

---

## SLIDE F3.6.5 — Le combinazioni

**Tipo**: `standard`
**Titolo**: I tipi si combinano
**Sottotitolo**: Perché i dispositivi reali esprimono quasi sempre più di un tipo

**Contenuto principale**:

Layout a colonna singola con tre sezioni: principio, esempi di combinazione, avvertimento sulle combinazioni non coerenti.

**Sezione superiore — il principio**:

Testo `--text-lg`:
*Un dispositivo F3 reale raramente esprime un tipo universale in stato puro.*
*Quasi sempre due tipi si intrecciano: uno principale, uno di supporto.*
*Questo non è un difetto — è la natura dell'azione relazionale contestualizzata.*

**Sezione centrale — esempi di combinazione**:

Quattro box affiancati (2×2), ognuno con una combinazione frequente:

**Box 1** — `U2 + U4` (caso-guida):
Chip U2 + chip U4 in grande.
*Sintonizzazione + Mediazione Simbolica*
*Il genitore segue il bambino (U2) usando il libro come terreno condiviso (U4).*
*Funzione: MEDIARE. La transizione N2→N3 si realizza nell'incontro sintonizzato intorno all'oggetto simbolico.*
Badge piccolo: `★ Caso-guida DBS`

**Box 2** — `U1 + U5`:
Chip U1 + chip U5.
*Regolazione + Limite Generativo*
*Il professionista riduce il carico (U1) e introduce una struttura temporale riconoscibile (U5).*
*Funzione: STABILIZZARE o PROTEGGERE. Campo in alta instabilità che ha bisogno di reggere.*

**Box 3** — `U3 + U2`:
Chip U3 + chip U2.
*Apertura + Sintonizzazione*
*Si introduce una possibilità nuova (U3) e si segue la risposta del bambino senza dirigerla (U2).*
*Funzione: AMPLIARE. Il campo regge — si apre verso nuove possibilità accompagnando l'avvicinamento del bambino.*

**Box 4** — `U6 + U3`:
Chip U6 + chip U3.
*Riattivazione del Desiderio + Apertura*
*Si riduce l'offerta adulta (U6) e si introduce una possibilità esplorativa (U3).*
*Funzione: AMPLIARE. Il campo è fermo non per mancanza di stabilità ma per eccesso di direttività adulta.*

**Sezione inferiore — combinazioni che non funzionano**:

Box sfondo rosso tenuissimo, bordo `--color-invalid`:

Titolo *"Combinazioni incoerenti:"* in `--text-sm` grassetto.

Due esempi compatti:

- `U3 + U1` su campo T0: *L'apertura richiede che il campo regga. Combinare apertura e regolazione su un campo T0 non funziona: la regolazione deve precedere, non accompagnare.*

- `U4 + U5` senza U2: *La mediazione simbolica senza sintonizzazione diventa insegnamento. L'oggetto si carica di significati adulti invece di diventare terreno condiviso. U2 è il prerequisito di U4.*

**Nota in footer**:
*Le combinazioni si descrivono sempre partendo dal tipo principale (quello che svolge la funzione primaria) e indicando il secondario come "di supporto". Nel caso-guida: U2 principale, U4 secondario — anche se nella scena sono difficilmente separabili.*

---

## SLIDE F3.6.6 — Il caso-guida: U2 + U4

**Tipo**: `narrative`
**Titolo**: La lettura condivisa come U2 + U4
**Sottotitolo**: Perché il Dialogic Book Sharing esprime Sintonizzazione e Mediazione Simbolica

**Contenuto principale**:

Layout a due aree: sinistra la CE e la funzione, destra la lettura per tipo universale. Dati da `CASO_GUIDA_M6`.

**Area sinistra** (42%) — "Il contesto":

`CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N2', 'N3'] })`

Sotto la CE:
- Chip `MED Mediazione` colore `var(--color-fn-mediare)`
- Testo `--text-sm`: *La funzione è già stata scelta (M4). I tipi universali descrivono la forma che MEDIAZIONE prende in questa scena specifica.*

**Area destra** (58%) — "Lettura per tipo universale":

**Blocco U2** (bordo sinistro spesso `var(--color-u2)`, sfondo `--color-u2` tenuissimo):

Badge `U2 Sintonizzazione` grande.

Testo `come_si_manifesta`.

Lista `micro_azioni_corrispondenti` da `CASO_GUIDA_M6.u2` — tre voci, lista ordinata.

**Blocco U4** (bordo sinistro spesso `var(--color-u4)`, sfondo `--color-u4` tenuissimo):

Badge `U4 Mediazione Simbolica` grande.

Testo `come_si_manifesta`.

Lista `micro_azioni_corrispondenti` da `CASO_GUIDA_M6.u4` — una voce.

**Sezione inferiore — perché non gli altri tipi**:

Box sfondo `--color-bg`, bordo `--color-border`. Titolo: *"Perché non U3, U6, U1, U5:"*

Tre righe `--text-sm`:
- `perche_non_u3`
- `perche_non_u6`
- `perche_non_u1_u5`

**Sezione conclusiva**:

Box sfondo `--color-primary-light`, bordo `--color-primary`:

*U2 e U4 non sono nomi di tecniche: descrivono cosa fa questa scena al campo.*
*Il genitore che segue il bambino è U2 perché la sua azione produce sintonizzazione.*
*Il libro che diventa terreno condiviso è U4 perché la sua presenza trasforma l'oggetto in mediatore dell'incontro.*

*La stessa forma U2+U4 potrebbe realizzarsi in un gioco imitativo, in una routine di pasti, in una passeggiata. La forma è universale — il dispositivo è contestuale.*

---

## SLIDE F3.6.7 — Il rischio del manuale di tecniche

**Tipo**: `comparison`
**Titolo**: La Tipologia U non è un catalogo
**Sottotitolo**: Il rischio di usare i tipi universali nel modo sbagliato

**Contenuto principale**:

`ComparisonPanel` tra uso corretto e uso errato della Tipologia U.

**Colonna sinistra** — "Uso della Tipologia U come catalogo di tecniche" (bordo `--color-invalid`):

Titolo: *"Il tipo come tecnica da applicare"*

Tre scenari problematici:
- *"Per questo bambino uso U2 — applico la Tecnica della Sintonizzazione."*
- *"La Tipologia dice U4: uso il libro con questa procedura specifica."*
- *"Ho scelto U2+U4 per tutti i casi di questo tipo."*

Sotto, corsivo `--color-text-secondary`:
*Trattare i tipi come tecniche pre-confezionate perde il punto: i tipi descrivono forme — non prescrivono azioni. "Usare U2" non dice nulla su cosa fare: dice solo qual è la forma dell'azione.*

**Colonna destra** — "Uso della Tipologia U come vocabolario di lettura" (bordo `--color-accent`):

Titolo: *"Il tipo come descrizione della forma dell'azione"*

Tre scenari corretti:
- *"Questa azione esprime U2 perché segue il ritmo del bambino senza dirigerlo."*
- *"Il dispositivo è U4: l'oggetto funziona da mediatore simbolico dell'incontro."*
- *"La combinazione U2+U4 descrive questa scena specifica — potrebbe non valere per un'altra scena con la stessa funzione."*

Sotto, corsivo `--color-accent`:
*I tipi sono un vocabolario condiviso tra professionisti: permettono di descrivere la forma dell'azione in modo riconoscibile, trasversale alle discipline e ai contesti.*

**Footer** a piena larghezza:

*La Tipologia U non risponde alla domanda "cosa fare?" (questo è compito del Template F3 e della scelta della funzione). Risponde alla domanda "come descrivere la forma di ciò che si fa?" — e questa è una domanda diversa.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-61`
- Label: Il tipo non sostituisce la lettura del campo
- Testo: *Scegliere un tipo universale prima di leggere la CE è un errore. I tipi emergono dalla lettura della funzione e del campo bersaglio — non dalla classificazione del bambino o della situazione.*

---

## SLIDE F3.6.8 — Un vocabolario condiviso

**Tipo**: `standard`
**Titolo**: La Tipologia U come linguaggio tra professionisti
**Sottotitolo**: Cosa resta dopo aver descritto il dispositivo per tipo universale

**Contenuto principale**:

Layout a colonna singola. Slide di chiusura — ariosa, poche parole, molto respiro visivo.

**Sezione superiore — il valore della tipologia**:

Testo `--text-lg`, centrato, spazio verticale:

*"La Tipologia U permette di parlare delle forme dell'azione relazionale al di là delle discipline, delle tecniche, dei protocolli."*

**Sezione centrale — tre proprietà del vocabolario**:

Tre blocchi verticali, separati da linee, sfondo `--color-surface`:

**Blocco 1** — Trasversale:
*U2 (Sintonizzazione) è riconoscibile in un bilancio pediatrico, in una sessione logopedica, in un'attività di nido, in una consultazione con la famiglia.*
*La stessa forma, contesti diversi.*

**Blocco 2** — Non diagnostico:
*I tipi non classificano il bambino: descrivono la forma del sostegno.*
*Non "bambini che hanno bisogno di U2" — ma "questa situazione richiede un'azione con forma U2".*

**Blocco 3** — Aggiornabile:
*Una CE aggiornata dopo il dispositivo può indicare che il tipo principale è cambiato.*
*Non si insiste: si rilegge il campo e, se necessario, si cambia forma.*

**Sezione inferiore — la prospettiva verso M7**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Abbiamo ora tutti gli elementi del micro-dispositivo:*
*la funzione (M4) → il template con le micro-azioni (M5) → la forma universale (M6).*

*Nel Modulo 7 affrontiamo la domanda che sta sotto tutto questo:*
*chi decide? Come si decide in tempo reale, nel contesto professionale, con il bambino davanti?*

*La logica decisionale è il ponte tra la CE prodotta dalla F2 e l'azione nella scena.*

Badge modulo successivo: `→ Modulo 7 — Logica decisionale`

---

## Note per l'implementazione

### Slide F3.6.2 — Mappa panoramica

La slide della mappa non usa `ExpandableCards`: è un layout CSS con sei blocchi fissi disposti in griglia 3×2. Ogni blocco è un `<div class="type-card">` non interattivo (no hover espansione), ma cliccabile: al click porta direttamente alla slide F3.6.3 con la card corrispondente aperta. Il click si gestisce con `navigateToSlide('f3-m06-03')` + `openCard(index)`. I due chip `★ caso-guida` su U2 e U4 sono badge piccoli `--text-xs` con sfondo `--color-guardrail-bg` e bordo `--color-guardrail`.

### Slide F3.6.3 — ExpandableCards sei tipi

Struttura identica a M4 slide F3.4.2 (quattro funzioni). L'unica differenza tecnica: sei card invece di quattro. L'indice rapido in cima usa due righe di tre chip invece di una riga di quattro. Riutilizzare lo stesso pattern CSS `chip-index` già definito in M4 aggiungendo `chip-index--wrap` per il wrapping automatico su due righe.

### Slide F3.6.4 — Tabella funzione → tipo

La tabella ha le stesse classi CSS della tabella dei segnali CE in M4 slide F3.4.3: `.signal-table` con colonne chip. Le colonne dei tipi principali e secondari usano chip `--color-uX` — sempre le variabili CSS, mai i codici esadecimali diretti. La riga MEDIAZIONE ha `class="row--highlighted"` con bordo sinistro e badge caso-guida.

### Slide F3.6.5 — Quattro box combinazioni

I quattro box (2×2) si implementano con CSS grid `grid-template-columns: 1fr 1fr`. I chip delle combinazioni (es. U2 + U4) sono due badge affiancati con uno `+` centrale in `--color-text-muted`. Il box `★ Caso-guida DBS` ha un bordo più spesso `--color-guardrail` e sfondo `--color-guardrail-bg` tenuissimo per distinguerlo dagli altri tre.

### Slide F3.6.6 — Layout due aree

Stesso pattern della slide F3.4.6 (caso-guida M4): usare `.slide__two-col` con proporzione 42/58 — variante `.slide__two-col--narrow-left`. I blocchi U2 e U4 nell'area destra sono separati da spazio verticale `--space-6`, non da una linea divisoria: la continuità visiva suggerisce che le due forme agiscono insieme nella stessa scena.

### Coerenza colori tipi universali

Tutti i colori `--color-uX` sono già definiti in `style.css` (dalla `ISTRUZIONI_CLAUDE_CODE_F3.md`). Nessuna ridefinizione locale. Le slide di M6 introducono un nuovo pattern: chip con due colori combinati (`U2 + U4`) — implementare come due chip `<span class="chip chip--uX">` affiancati con un `<span class="chip__separator">+</span>` tra loro, non come unico chip bicolore.
