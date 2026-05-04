# Modulo 0 — Perché una fondazione?
**Numero slide**: 5
**Colore accent**: `#6c63ff`
**Tipo prevalente**: narrative + diagram

---

## Dati globali del modulo

Definire in `f1_m00.js` le seguenti costanti.

```javascript
const TRE_OSSERVATORI = [
  {
    id: 'pediatra',
    icona: '🩺',
    disciplina: 'Pediatra',
    lettura_comune: 'Competenza linguistica nella norma?',
    domanda_implicita: 'Ha raggiunto le tappe di sviluppo attese per l\'età?',
    assunzione_implicita: `Lo sviluppo è un processo di accumulo di competenze misurabili rispetto
      a una norma. Il bambino è l'unità di analisi: si valuta individualmente, rispetto a una
      traiettoria standard. Il campo relazionale è rilevante ma non costitutivo.`,
    cosa_non_vede: `Non vede il campo relazionale che rende possibile o impossibile lo scambio.
      Non vede il libro come oggetto culturale. Non vede la struttura dello scambio: vede
      solo la prestazione del bambino in quel momento.`,
    tipo_riduzione: 'Riduzione normativa',
    colore: '#1a6b8a'
  },
  {
    id: 'educatore',
    icona: '📚',
    disciplina: 'Educatore',
    lettura_comune: 'Buona attenzione sostenuta?',
    domanda_implicita: 'Il bambino riesce a mantenere l\'attenzione su un compito cognitivo?',
    assunzione_implicita: `Lo sviluppo è il dispiegarsi di funzioni cognitive relativamente autonome.
      L'attenzione è una funzione valutabile indipendentemente dal campo relazionale e dall'oggetto
      culturale. Quello che si vede è un comportamento del bambino, non una configurazione
      del campo.`,
    cosa_non_vede: `Non vede che il bambino non sta "prestando attenzione" — sta costruendo
      un mondo condiviso con l'adulto. Non vede che l'attenzione dipende dal campo, non dal
      bambino. Non vede la qualità dello scambio simbolico.`,
    tipo_riduzione: 'Riduzione funzionale',
    colore: '#2d6a4f'
  },
  {
    id: 'npi',
    icona: '🧠',
    disciplina: 'Neuropsichiatra / Psicologo',
    lettura_comune: 'Assenza di segnali di allerta?',
    domanda_implicita: 'Il comportamento del bambino è nella norma o indica un rischio?',
    assunzione_implicita: `Il bambino è portatore di possibili profili patologici. L'osservazione
      è orientata dalla ricerca di segnali di scarto rispetto a traiettorie standard. Il campo
      relazionale è variabile di contesto — importante, ma non l'oggetto principale
      dell'osservazione.`,
    cosa_non_vede: `Non vede ciò che c'è — vede l'assenza di ciò che non dovrebbe esserci.
      Non vede la qualità del campo condiviso, la ricchezza dello scambio simbolico, la
      struttura della relazione. Vede solo che non ci sono segnali di allerta.`,
    tipo_riduzione: 'Riduzione diagnostica',
    colore: '#8e44ad'
  }
];

const ARCHITETTURA_F1 = {
  fasi: [
    {
      id: 'f1',
      label: 'F1 — Fondazione ontologica',
      sottotitolo: '← Siamo qui',
      colore: '#6c63ff',
      attiva: true,
      funzione: `Stabilisce che tipo di realtà è lo sviluppo infantile e che tipo di soggetto
        è il bambino. Non produce strumenti operativi diretti. Definisce i vincoli
        concettuali che rendono possibile qualsiasi strumento successivo.`,
      input: 'Nessuno — è il punto di partenza del framework.',
      output: 'I sei assi strutturali come condizioni di possibilità per F2.',
      domanda_fondante: 'Che tipo di realtà è lo sviluppo? Che tipo di soggetto è il bambino?'
    },
    {
      id: 'f2',
      label: 'F2 — Traduzione interdisciplinare',
      sottotitolo: null,
      colore: '#1a6b8a',
      attiva: false,
      funzione: `Costruisce condizioni di traducibilità tra livelli disciplinari differenti
        senza perdita dello statuto teorico originario. Rende lo sviluppo leggibile
        nei contesti professionali.`,
      input: 'I sei assi strutturali di F1.',
      output: 'Nodi Trasversali, Matrice di traducibilità, Grammatica configurazionale.',
      domanda_fondante: 'Come si rende leggibile lo sviluppo senza ridurlo?'
    },
    {
      id: 'f3',
      label: 'F3 — Strumenti operativi',
      sottotitolo: null,
      colore: '#2d9cdb',
      attiva: false,
      funzione: `Trasforma la leggibilità prodotta da F2 in micro-azioni coerenti senza
        produrre protocolli, diagnosi o prescrizioni. Richiede F2 come prerequisito.`,
      input: 'Configurazioni Evolutive e operatori di lettura di F2.',
      output: 'Dispositivi di sostegno contestualizzati, output-tipo vuoti, strumenti disciplinari.',
      domanda_fondante: 'Come si agisce coerentemente con la struttura dello sviluppo?'
    }
  ],
  parole_chiave: [
    { fase: 'f1', parola: 'DEFINISCE' },
    { fase: 'f2', parola: 'RENDE LEGGIBILE' },
    { fase: 'f3', parola: 'RENDE POSSIBILE L\'AZIONE' }
  ]
};

const COSA_FA_F1 = {
  produce: [
    {
      id: 'p1',
      testo: 'Un\'ontologia del soggetto in sviluppo',
      note: 'Il bambino come soggetto incarnato, temporale e relazionale — non come organismo o insieme di funzioni.'
    },
    {
      id: 'p2',
      testo: 'I sei assi strutturali di sviluppo',
      note: 'Dimensioni sempre attive — non fasi da attraversare né competenze da acquisire.'
    },
    {
      id: 'p3',
      testo: 'Un sistema di vincoli contro le riduzioni',
      note: 'Ogni guardrail di F2 e F3 deriva da un\'assunzione di F1. La fondazione agisce come rete di sicurezza metodologica.'
    },
    {
      id: 'p4',
      testo: 'Le condizioni di possibilità per F2',
      note: 'Gli assi non si usano direttamente — rendono possibile la costruzione dei Nodi e della Matrice di F2.'
    }
  ],
  non_produce: [
    {
      id: 'np1',
      testo: 'Strumenti operativi',
      note: 'F1 non produce nulla che si possa usare direttamente in ambulatorio, al nido o in counseling.'
    },
    {
      id: 'np2',
      testo: 'Domande osservative dirette',
      note: 'Le domande professionali nascono in F2. F1 produce le domande che orientano la costruzione di quelle domande.'
    },
    {
      id: 'np3',
      testo: 'Indicatori o criteri di valutazione',
      note: 'F1 è rigorosamente pre-normativo: non definisce soglie, livelli, profili o categorie di rischio.'
    },
    {
      id: 'np4',
      testo: 'Diagnosi o prescrizioni',
      note: 'Nessun asse strutturale dice al professionista cosa fare. La decisione operativa rimane sempre fuori dal metodo.'
    }
  ]
};

const MAPPA_MODULI_F1 = [
  {
    id: 'm0',
    numero: 'M0',
    titolo: 'Perché una fondazione?',
    titolo_breve: 'Orientamento',
    colore: '#6c63ff',
    introduce: 'Il problema delle assunzioni implicite e l\'architettura del metodo.',
    slide: 5
  },
  {
    id: 'm1',
    numero: 'M1',
    titolo: 'Il bambino come soggetto',
    titolo_breve: 'Il soggetto',
    colore: '#5c35a0',
    introduce: 'L\'ontologia del soggetto incarnato, temporale e relazionale. Il guardrail fondativo.',
    slide: 7
  },
  {
    id: 'm2',
    numero: 'M2',
    titolo: 'Gli assi strutturali: logica e architettura',
    titolo_breve: 'Architettura',
    colore: '#4a5568',
    introduce: 'Cosa sono gli assi, la gerarchia strutturale, le quattro proprietà, la differenza con le competenze.',
    slide: 7
  },
  {
    id: 'm3',
    numero: 'M3',
    titolo: 'Asse 1 — Abitare l\'esperienza',
    titolo_breve: 'Asse 1',
    colore: '#1a6b8a',
    introduce: 'Il soggetto incarnato: come il bambino abita l\'esperienza. Asse fondativo di tutti gli altri.',
    slide: 8
  },
  {
    id: 'm4',
    numero: 'M4',
    titolo: 'Assi 2 e 3 — Alterità e normatività',
    titolo_breve: 'Assi 2–3',
    colore: '#2d6a4f',
    introduce: 'Il riconoscimento dell\'altro come soggetto. L\'emergenza interna della normatività.',
    slide: 7
  },
  {
    id: 'm5',
    numero: 'M5',
    titolo: 'Assi 4 e 5 — Limite reale e desiderio',
    titolo_breve: 'Assi 4–5',
    colore: '#c0392b',
    introduce: 'L\'incontro con la resistenza del reale. Il desiderio come direzione, non carenza.',
    slide: 7
  },
  {
    id: 'm6',
    numero: 'M6',
    titolo: 'Asse 6 e la gerarchia completa',
    titolo_breve: 'Asse 6',
    colore: '#d35400',
    introduce: 'La partecipazione al mondo storico-culturale. Il sistema degli assi come mappa relazionale.',
    slide: 7
  },
  {
    id: 'm7',
    numero: 'M7',
    titolo: 'Statuto epistemologico e passaggio a F2',
    titolo_breve: 'Epistemologia',
    colore: '#2c3e50',
    introduce: 'Gli assi come strutture interpretative. La circolazione controllata. Il ponte verso F2.',
    slide: 7
  }
];
```

---

## SLIDE 0.1 — La stessa scena, tre osservatori

**Tipo**: `narrative`
**Titolo**: La stessa scena, tre osservatori
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Layout a colonna singola. La slide si svolge in due fasi narrative ben distinte, separate da un divisore visivo. La seconda fase è nascosta all'entrata nella slide e appare solo dopo un'interazione esplicita dell'utente.

**Fase 1 — La scena** (visibile all'entrata):

Testo narrativo in corsivo, font --text-lg, su sfondo `--color-primary-light`, bordo sinistro `--color-primary`. Testo da `window.CASO_GUIDA_F1.scena`.

Sotto la card narrativa, tre chip affiancati con le letture disciplinari. Usa i dati da `TRE_OSSERVATORI`:

```
[🩺 Pediatra]          [📚 Educatore]          [🧠 NPI / Psicologo]
"Competenza            "Buona attenzione        "Assenza di segnali
linguistica            sostenuta?"              di allerta?"
nella norma?"
```

Ogni chip ha il colore del proprio osservatore (`colore` da `TRE_OSSERVATORI`), sfondo tenue, bordo colorato. I chip non sono ancora cliccabili in questa fase.

Sotto i chip, una frase centrata in `--color-text-secondary`, `--text-lg`:
*Tre osservatori, tre domande diverse — sulla stessa scena.*

**Elemento di transizione tra le due fasi**:

Dopo 1.5s dall'entrata nella slide (o immediatamente se l'utente interagisce), appare sotto la frase un bottone discreto:

```
[ Cosa sta assumendo ciascuno? ↓ ]
```

Stile: chip con bordo `#6c63ff`, sfondo trasparente, testo `#6c63ff`. Il click fa scorrere verso il basso con smooth scroll e rivela la Fase 2.

**Fase 2 — Le assunzioni implicite** (appare al click):

Titolo piccolo centrato in `--color-text-muted`: *Le domande non sono il problema. Lo sono le assunzioni che le producono.*

Tre card verticali espandibili, una per osservatore. Usa il componente `ExpandableCards` con `multiOpen: true`. Ogni card:

**Fronte** (compatto):
```
[Chip disciplina colorato]   [lettura_comune in corsivo]
[domanda_implicita in testo normale]
                                              [↓ Vedi l'assunzione]
```

**Card espansa**:

Sezione 1 — *"Cosa assume"* (etichetta piccola sopra):
Testo dal campo `assunzione_implicita`. Sfondo leggermente colorato con il colore dell'osservatore (opacità 6-8%).

Sezione 2 — *"Cosa non vede"* (etichetta piccola sopra, bordo sinistro rosso tenue):
Testo dal campo `cosa_non_vede`.

Chip in fondo alla card, in piccolo: `tipo_riduzione` (es. "Riduzione normativa").

**Sotto le tre card** — testo di chiusura, centrato, `--text-lg`, `--color-text`:

*Il problema non è che le domande siano sbagliate — sono domande competenti, professionali, legittime.*
*Il problema è che nascono da assunzioni implicite su cosa è lo sviluppo e chi è il bambino.*

*Rendere esplicite quelle assunzioni è il compito della Fase 1.*

**Nota in footer**:
*Questo modulo apre con la stessa scena che ha aperto il corso F2 — ma con una domanda diversa. In F2 la domanda era: "come leggiamo questa scena senza ridurla?" In F1 la domanda è: "cosa sta assumendo implicitamente chiunque la guardi?" Sono due livelli diversi dello stesso problema.*

---

## SLIDE 0.2 — L'architettura del metodo vista da F1

**Tipo**: `diagram`
**Titolo**: Un metodo in tre fasi
**Sottotitolo**: Vista da F1

**Contenuto principale**:

Diagramma verticale interattivo con tre blocchi collegati da frecce. Struttura analoga alla slide 0.2 del corso F2, con le seguenti differenze:
- Il blocco F1 ha bordo più spesso e chip `← Siamo qui`
- I blocchi F2 e F3 hanno opacità leggermente ridotta (non bloccati, solo visivamente in secondo piano)
- Il pannello F1 è già aperto al caricamento della slide

Usa i dati da `ARCHITETTURA_F1.fasi`.

**Schema visivo**:

```
┌──────────────────────────────────────────────────┐
│  F1 — Fondazione ontologica   ← Siamo qui        │  ← colore: #6c63ff, bordo 2px
│  "Che tipo di realtà è lo sviluppo?"              │
└─────────────────────┬────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────┐
│  F2 — Traduzione interdisciplinare               │  ← colore: #1a6b8a, opacità 70%
│  "Come si rende leggibile lo sviluppo?"          │
└─────────────────────┬────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────┐
│  F3 — Strumenti operativi                        │  ← colore: #2d9cdb, opacità 70%
│  "Come si agisce coerentemente?"                 │
└──────────────────────────────────────────────────┘
```

**Pannello espanso cliccando F1** (aperto di default):

Titolo: *"Fase 1 — Fondazione ontologica ← Siamo qui"*

Quattro righe di contenuto con etichette:
- **Funzione**: testo dal campo `funzione` di `ARCHITETTURA_F1.fasi[0]`
- **Domanda fondante**: testo dal campo `domanda_fondante`, in corsivo e in grande (`--text-xl`)
- **Input**: testo dal campo `input`
- **Output verso F2**: testo dal campo `output`

**Pannello espanso cliccando F2**:
Stesse quattro righe per F2. Aggiunta di una nota: *"Il corso F2 — Traduzione Interdisciplinare è già disponibile come applicazione separata."*

**Pannello espanso cliccando F3**:
Stesse quattro righe per F3. Nota: *"F3 richiede F2 come prerequisito. La decisione clinica o educativa resta fuori dal metodo."*

**Sotto il diagramma** — riga di parole chiave:

```
DEFINISCE   →   RENDE LEGGIBILE   →   RENDE POSSIBILE L'AZIONE
   F1                F2                        F3
```

Font `--text-sm`, colori rispettivi delle tre fasi, spaziatura generosa.

**Nota in footer**:
*In F2 questo stesso schema appariva con F2 evidenziata come "siamo qui". Qui è F1 ad essere al centro. Non è ridondanza: F1 e F2 sono due corsi autonomi che esplorano due livelli diversi del metodo. È possibile seguirli in ordine o separatamente — ma F1 è la radice da cui F2 trae i propri vincoli.*

---

## SLIDE 0.3 — Cosa fa F1 — e cosa non fa

**Tipo**: `standard`
**Titolo**: Cosa fa F1
**Sottotitolo**: E cosa non fa — una distinzione che vale tenerere a mente per tutto il corso

**Contenuto principale**:

Layout a due colonne affiancate, speculare alla slide 0.4 del corso F2 ma con i contenuti specifici di F1. Usa i dati da `COSA_FA_F1`.

**Colonna sinistra** — Box verde (sfondo `--color-valid` molto chiaro, bordo verde `#27ae60`):

Intestazione: **✓ F1 produce**

Lista dal campo `produce` di `COSA_FA_F1`. Ogni voce è su due righe:
- Riga 1: `testo` in grassetto
- Riga 2: `note` in testo normale, `--color-text-secondary`, `--text-sm`

Spaziatura generosa tra le voci (non una lista bullet densa — ogni voce ha il suo spazio).

**Colonna destra** — Box rosso (sfondo `--color-invalid` molto chiaro, bordo rosso `#e74c3c`):

Intestazione: **✗ F1 non produce**

Stessa struttura, dai dati `non_produce` di `COSA_FA_F1`.

**Sotto le colonne** — divisore sottile — elemento a piena larghezza:

Testo centrato, `--text-lg`, `--color-text`:
*F1 resta sullo sfondo di tutto il resto del metodo — non come contenuto da applicare, ma come insieme di vincoli che impediscono le riduzioni.*

Sotto, in `--color-text-secondary`:
*Ogni volta che uno strumento di F3 rischia di trasformare l'abitabilità in punteggio, o il campo relazionale in comportamento del bambino — è la fondazione ontologica che segnala lo scarto.*

**Nota in footer**:
*La distinzione tra ciò che F1 produce e ciò che non produce non è una limitazione: è la condizione che rende il framework metodologicamente coerente. Un framework che produce tutto — fondazione, leggibilità, strumenti, diagnosi — non ha livelli distinti e perde i guardrail tra un livello e l'altro.*

---

## SLIDE 0.4 — La domanda fondativa

**Tipo**: `narrative`
**Titolo**: *(nessuno — la slide è occupata dalla domanda)*
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Slide volutamente minimale. Nessuna sidebar di contenuto laterale. Nessun elemento decorativo. Solo testo che respira, con spazio bianco generoso.

**Layout centrato verticalmente e orizzontalmente** nell'area slide. Nessuna animazione all'entrata.

**Elemento principale** — grande blockquote centrato:

```
Che tipo di realtà è lo sviluppo infantile?

Che tipo di soggetto è il bambino?
```

Font: `--text-4xl` per la prima frase, `--text-3xl` per la seconda.
Colore: `--color-text` (non in grigio, non in muted — il testo pieno).
Interlinea: `--leading-relaxed`.
Nessun bordo laterale, nessun sfondo colorato — solo le due domande nello spazio bianco.

**Sotto le domande** — separatore sottile (`--color-border`, 1px, larghezza 60px centrata):

Testo in `--color-text-secondary`, `--text-base`, centrato:

*Prima di costruire qualsiasi strumento, prima di scegliere qualsiasi metodo di osservazione, prima di formare un professionista a riconoscere qualcosa — bisogna rispondere a queste domande.*

*Non esplicitamente. Non sempre. Ma implicitamente: ogni strumento già le risponde — nel modo in cui è costruito.*

**Sotto ancora** — in `--color-text-muted`, `--text-sm`, centrato:

*Rendere esplicita questa risposta è il compito della Fase 1.*

**Nota in footer**:
*Questa slide non ha interattività. È l'unica del corso in cui si chiede al partecipante solo di stare con una domanda. La velocità della navigazione è nelle mani di chi segue il corso — ma questa slide è pensata per essere lenta.*

---

## SLIDE 0.5 — Il corso che costruiremo

**Tipo**: `diagram`
**Titolo**: Il corso che costruiremo insieme
**Sottotitolo**: Otto moduli, una progressione

**Contenuto principale**:

Mappa visiva degli 8 moduli disposti in due colonne di quattro (4 sinistra + 4 destra), con frecce che indicano la progressione. Usa i dati da `MAPPA_MODULI_F1`.

**Layout griglia 2 × 4**:

Ogni card modulo contiene:
- Badge colorato con numero (`M0` … `M7`) nel colore `colore` del modulo
- Titolo breve (`titolo_breve`) in grassetto
- Testo breve (`introduce`) in `--color-text-secondary`, `--text-sm`
- Pill in basso a destra con numero di slide: `5 slide`, `7 slide`, `8 slide`

La card `M0` (il modulo corrente) ha un bordo più spesso e sfondo leggermente colorato per indicare la posizione attuale.

**Freccia di progressione**: una freccia sottile curva connette M0 → M1 → … → M7 nello stesso ordine visivo della griglia, scorrendo dall'alto verso il basso e da sinistra a destra.

**Sotto la griglia** — due elementi testuali:

**Sinistra** (25% larghezza):
*Il caso-guida — la scena della lettura condivisa — appare in ogni modulo. Non si aggiunge contenuto alla scena: cambia la domanda con cui la si guarda.*

**Destra** (75% larghezza) — callout con bordo sinistro `#6c63ff`:
*Ogni modulo è autonomo: si può rileggere singolarmente. Ma la progressione ha una logica: M1 pone la domanda ontologica, M2 introduce il sistema degli assi, M3–M6 approfondiscono ciascun asse, M7 chiude il cerchio epistemologico e prepara il passaggio a F2.*

**Elemento finale** — piccolo, centrato, in `--color-text-muted`:

*La Fase 1 non produce strumenti. Produce la possibilità di costruirli bene.*

**Badge modulo successivo**:
`→ Modulo 1 — Il bambino come soggetto`

**Nota in footer**:
*All'entrata nel Modulo 0, mostrare una breve transizione di benvenuto: fade-in del badge `F1` e del titolo del corso per 400ms, poi dissolve verso la slide 0.1. Non usare testo di benvenuto verboso — la scena del caso-guida è il modo migliore per aprire il corso.*

---

## Note per l'implementazione

### Slide 0.1 — Il reveal delle assunzioni

La Fase 1 (scena + chip) e la Fase 2 (card espandibili delle assunzioni) non sono due sezioni navigate con le frecce: sono nella stessa slide, con la Fase 2 nascosta e rivelata da un bottone. Questo crea una piccola tensione narrativa: il partecipante vede prima le domande "ovvie" dei tre osservatori, poi viene invitato a scendere più in profondo.

**Implementazione**:
- Fase 2 è in un `<div class="fase-2" hidden>` all'inizio
- Al click del bottone: `div.hidden = false` + smooth scroll al div + breve fade-in (200ms)
- Il bottone scompare dopo il click (o si trasforma in un'etichetta statica: "↑ assunzioni implicite")
- I progress dots della slide non cambiano — siamo sempre in slide 0.1

**Alternativa più semplice** (se il reveal dinamico complica il router): usare le frecce di navigazione tra due sotto-slide (0.1a e 0.1b) con la stessa numerazione per i dot. In questo caso i dot mostrano 6 slide anziché 5.

### Slide 0.1 — Confronto con F2 M0

La slide 0.1 di F1 è costruita sullo stesso materiale della slide 0.1 di F2 (tre osservatori, stessa scena), ma con un angolo diverso. In F2, il focus era "tre linguaggi diversi" — il problema della traduzione. In F1, il focus è "tre assunzioni diverse" — il problema della fondazione. Questa differenza deve essere percepibile visivamente e nel testo: non è un doppione del corso F2.

La differenza chiave nel design:
- In F2: i chip mostravano direttamente le letture ("Competenza linguistica nella norma?")
- In F1: i chip mostrano prima le letture, poi rivelano le assunzioni sottostanti

Se il partecipante ha già seguito F2, la slide 0.1 di F1 deve sembrare familiare ma non identica — lo stesso punto di ingresso con una svolta inattesa.

### Slide 0.2 — Pannello laterale e stato dei blocchi

Il pannello laterale che appare cliccando un blocco F1/F2/F3 deve gestire correttamente lo stato:
- F1: pannello aperto di default, bordo pieno, testo pieno
- F2 e F3: pannello chiuso di default, opacità 70% sul blocco, si aprono al click
- Cliccando un blocco già aperto: non chiudere il pannello (il pannello di F1 non si chiude — resta sempre visibile come "siamo qui")

### Slide 0.4 — Nessuna animazione

Questa slide è progettata per essere immobile. Nessuna animazione all'entrata, nessun reveal progressivo. Le due domande appaiono subito, complete. Il silenzio visivo è intenzionale.

Se il sistema di transizione globale applica un fade-in automatico a tutte le slide, assicurarsi che qui sia ridotto al minimo (100ms opacity invece di 200ms + translate). La slide non deve "costruirsi" — deve semplicemente essere lì.

### Slide 0.5 — Hover sulle card modulo

Cliccando una card modulo nella mappa, non navigare verso quel modulo (il router non deve attivarsi). Le card sono informative, non link di navigazione. Al click, espandere un tooltip o una mini-descrizione aggiuntiva sotto la card. La navigazione ai moduli avviene solo dalla sidebar.

### Transizione M0 → M1

All'entrata nel Modulo 1 (la prima volta), mostrare una brevissima sovrapposizione (2-3 righe, fade out dopo 2.5s):
*"Nel Modulo 0 abbiamo visto che le assunzioni implicite determinano le domande. Ora iniziamo a costruire l'assunzione del progetto: chi è il bambino?"*
Poi dissolve verso la slide 1.1.
