# f3-modulo-01 — Il principio del campo
**Numero slide**: 6
**Colore accent**: `#1e8bc3`
**Tipo prevalente**: standard + comparison

---

## Dati globali del modulo

Definire in `m01.js` le seguenti costanti. Sono la sorgente di dati per tutte le slide del modulo.

```javascript
const COMPONENTI_CAMPO = [
  {
    id: 'bambino',
    label: 'Bambino',
    descrizione: `Soggetto incarnato, temporale e relazionale.
                  Non è l'oggetto dell'intervento F3: è uno dei poli del campo.
                  Modificare il bambino direttamente significa isolare il soggetto
                  dalle condizioni che rendono possibile il suo sviluppo.`,
    colore: 'var(--color-n3)',
    nota: 'Il bambino non è mai il bersaglio del micro-dispositivo — anche quando il cambiamento osservabile riguarda il suo comportamento.'
  },
  {
    id: 'adulto',
    label: 'Adulto',
    descrizione: `Il professionista, il genitore, l'educatore — chiunque condivida
                  il campo con il bambino. Polo del campo su cui l'intervento F3
                  agisce direttamente: le micro-azioni riguardano quasi sempre
                  una modifica nel comportamento adulto, nel ritmo, nella risposta.`,
    colore: 'var(--color-n2)',
    nota: 'Il più delle volte il micro-dispositivo F3 chiede qualcosa all\'adulto — non al bambino.'
  },
  {
    id: 'contesto',
    label: 'Contesto',
    descrizione: `Setting, ritmo, oggetti, struttura dell'incontro, tempo disponibile.
                  Le condizioni materiali e temporali entro cui il campo si organizza.
                  Un micro-dispositivo può agire sul contesto modificando la durata,
                  l'oggetto presente, la disposizione spaziale.`,
    colore: 'var(--color-primary)',
    nota: 'Un oggetto diverso, una posizione diversa, cinque minuti in più: sono modifiche di contesto che cambiano il campo.'
  }
];

const TRE_PROPRIETA = [
  {
    id: 'integrabile',
    numero: '1',
    nome: 'Breve e integrabile',
    testo: `Si inserisce nel contesto professionale reale senza richiedere
            setting separati, tempi aggiuntivi o strutture dedicate.
            Un dispositivo che funziona solo in una sessione terapeutica apposita
            non è un micro-dispositivo di campo: è un intervento specialistico.`,
    test: 'Funziona nel tempo e nel setting in cui già ci troviamo?',
    esempio_ok: 'Cinque minuti durante il bilancio pediatrico.',
    esempio_no: 'Una serie di sedute di stimolazione logopedica settimanale.'
  },
  {
    id: 'reversibile',
    numero: '2',
    nome: 'Non specialistico e reversibile',
    testo: `Non richiede una competenza tecnica specialistica per essere applicato.
            Può essere modificato o interrotto senza danno se il campo
            non risponde. La reversibilità non è un limite: è la condizione
            che permette di osservare davvero gli effetti prima di continuare.`,
    test: 'Se smetto, il campo torna com\'era? Posso rivalutare senza conseguenze?',
    esempio_ok: 'Rallentare il ritmo della risposta adulta. Attendere prima di nominare.',
    esempio_no: 'Avviare un programma di training ABA con protocollo fisso.'
  },
  {
    id: 'osservabile',
    numero: '3',
    nome: 'Osservabile nei suoi effetti',
    testo: `Produce modificazioni visibili nel campo entro il tempo reale
            dell'intervento. L'indicatore di risonanza — che cosa ci si aspetta
            cambi nel campo — viene definito prima dell'azione, non dopo.
            Se l'effetto non è osservabile, non è possibile rivalutare la CE.`,
    test: 'Definisco prima cosa cerco. Lo vedo entro il tempo dell\'incontro?',
    esempio_ok: 'La sequenza bambino-adulto si allunga? Il bambino include l\'adulto? → Osservabile in cinque minuti.',
    esempio_no: '"I risultati si vedranno nel tempo." → Non è un micro-dispositivo di campo.'
  }
];

const CONFRONTO_AZIONE = {
  sinistra: {
    label: 'Azione sul bambino',
    colore: 'var(--color-invalid)',
    titolo: 'Il bambino come bersaglio',
    items: [
      {
        testo: 'Insegnare al bambino a indicare',
        problema: 'Il gesto di indicare emerge dal campo condiviso — non è un abilità isolabile da allenare.'
      },
      {
        testo: 'Stimolare il linguaggio del bambino',
        problema: 'Il linguaggio emerge nello scambio relazionale. Stimolarlo direttamente bypassa le condizioni che lo rendono possibile.'
      },
      {
        testo: 'Aumentare la frequenza di un comportamento target',
        problema: 'Prende il comportamento come unità di intervento e perde di vista la configurazione relazionale che lo produce.'
      }
    ],
    nota: 'Queste azioni non sono sbagliate in assoluto. Il punto è che non sono strumenti F3: agiscono sul soggetto isolato, non sul campo.'
  },
  destra: {
    label: 'Modifica del campo relazionale',
    colore: 'var(--color-f3)',
    titolo: 'Il campo come bersaglio',
    items: [
      {
        testo: 'Rallentare il ritmo dell\'adulto perché il gesto del bambino trovi uno spazio di risposta',
        nota: 'Agisce sulla condizione relazionale che rende possibile il gesto — non sul gesto stesso.'
      },
      {
        testo: 'Aumentare la stabilità dello scambio condiviso così che il bambino possa mantenere l\'iniziativa',
        nota: 'Il linguaggio emerge quando il campo è stabile. Si lavora sul campo, non sul bambino.'
      },
      {
        testo: 'Creare le condizioni perché la sequenza del bambino possa completarsi',
        nota: 'L\'unità di intervento è la configurazione relazionale, non il singolo comportamento osservato.'
      }
    ],
    nota: null
  },
  footer: {
    label: 'Principio operativo fondamentale',
    colore: 'var(--color-f3)',
    testo: 'Lo strumento F3 non corregge il bambino: modifica il campo relazionale di esperienza in cui il bambino esiste.'
  }
};

const CASO_GUIDA_M1 = {
  lettura_campo: {
    adulto: [
      'Rallentare il ritmo: attendere che la sequenza del bambino si completi prima di rispondere',
      'Nominare ciò che il bambino indica — non ciò che si vorrebbe che indicasse',
      'Ridurre le domande dirette ("Cos\'è questo?") che interrompono l\'iniziativa del bambino',
      'Tenere le mani ferme: non girare le pagine, non indicare prima del bambino'
    ],
    contesto: [
      'Proporre il libro solo quando il campo relazionale è già regolato (non all\'inizio della visita)',
      'Ridurre le interruzioni esterne nel momento della lettura condivisa',
      'Scegliere un libro con immagini semplici e ben distanziate (meno conflitti per l\'attenzione)'
    ],
    bambino_non_target: `Nessuna micro-azione riguarda direttamente il bambino.
                          Non si chiede al bambino di indicare, di nominare, di guardare.
                          Si modificano le condizioni del campo — il bambino risponde
                          (o non risponde) a quelle condizioni.`
  }
};
```

---

## SLIDE F3.1.1 — La domanda dell'azione

**Tipo**: `standard`
**Titolo**: Dopo la CE, cosa si fa?
**Sottotitolo**: Il punto di partenza di ogni strumento

**Contenuto principale**:

Layout a due colonne. Abbondante spazio bianco. Font principale `--text-xl`.

**Colonna sinistra** (45% — "La risposta naturale"):

Card con sfondo `--color-bg`, bordo `--color-border`:

**La risposta naturale**

Il professionista ha in mano la CE. Sa che il campo relazionale è attivo (N2↑), che l'accesso al mondo condiviso è presente ma discontinuo (N3~), che l'esplorazione è ridotta (N4↓).

La risposta naturale — quella che emerge per prima — è spesso questa:

> *"Bisogna lavorare sul bambino. Stimolarlo. Aumentare la frequenza del gesto di indicare. Migliorare il linguaggio."*

Questo impulso è comprensibile: è il linguaggio dei programmi di intervento precoce, della stimolazione cognitiva, del training di competenze.

**Colonna destra** (55% — "Il problema metodologico"):

Card con sfondo `--color-primary-light`, bordo sinistro `--color-f3`:

**Il problema metodologico**

Questa risposta poggia su un'assunzione implicita: che il bambino sia un'unità isolabile su cui si può intervenire direttamente.

La Fase 1 ha stabilito che questa assunzione è sbagliata rispetto ai fondamenti del progetto: il bambino non è un organismo che accumula competenze — è un soggetto incarnato, temporale e relazionale. Il suo sviluppo non avviene *nonostante* il campo relazionale: avviene *attraverso* di esso.

Agire sul bambino isolato dalla configurazione relazionale significa agire sull'effetto senza toccare le condizioni che lo producono.

**Elemento visivo sotto le colonne** — freccia con domanda al centro:

```
[Azione sul bambino]  ←  oppure  →  [Modifica del campo]
                         ?
```

Testo sotto: *La Fase 3 risponde a questa domanda in modo preciso. Non è una scelta etica: è una scelta metodologica.*

**Nota in footer**:
*La risposta naturale non è sbagliata in assoluto — è fuori modello rispetto a questo framework. Il Modulo 1 spiega perché e propone l'alternativa.*

---

## SLIDE F3.1.2 — Il fondamento: il bambino non è isolabile

**Tipo**: `standard`
**Titolo**: Un'eredità dalla Fase 1
**Sottotitolo**: Perché non si agisce sul bambino isolato

**Contenuto principale**:

Layout a colonna singola, leggero. La slide richiama in modo sintetico il fondamento ontologico di F1 — non lo ri-spiega, lo usa come premessa già acquisita.

**Sezione superiore — il richiamo a F1**:

Blockquote centrato, bordo sinistro `--color-f1`, sfondo tenue:

> *"Il bambino non è un organismo che accumula competenze né un insieme di funzioni che maturano in sequenza. È un soggetto incarnato, temporale e relazionale, la cui esistenza è costitutivamente dipendente da un campo di esperienze e relazioni che non può essere separato da lui senza perderne il senso."*

Badge piccolo in basso a destra del blockquote: `← F1 — Fondazione ontologica`

**Sezione centrale — tre conseguenze operative**:

Tre blocchi verticali con numero grande in `--color-f1` (1, 2, 3):

**① Il campo non è lo sfondo**
Il campo relazionale non è il contesto in cui lo sviluppo avviene: è la *condizione* che lo rende possibile. Lo sviluppo bambino-adulto-contesto non è descrivibile come sviluppo del bambino più il suo ambiente.

**② L'oggetto di osservazione pertinente è la configurazione**
Ciò che si osserva non è il bambino isolato (le sue competenze, i suoi comportamenti, il suo sviluppo individuale) ma la configurazione relazionale in cui il bambino esiste in quel momento.

**③ Lo strumento deve agire sulla configurazione**
Un dispositivo che osserva e modifica il bambino come unità indipendente non è semplicemente incompleto: è metodologicamente incoerente rispetto ai fondamenti del progetto. F3 eredita questo vincolo direttamente.

**Sezione inferiore — la formulazione operativa**:

Testo centrato, `--text-lg`, grassetto leggero, colore `--color-f3`:

*Lo strumento F3 non corregge il bambino: modifica il campo relazionale di esperienza.*

Sotto, in `--text-base`, `--color-text-secondary`:
*Questa non è una posizione etica. È la conseguenza operativa dell'Asse 1.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-10`
- Label: Vincolo fondativo
- Testo: *Un dispositivo F3 che ha senso solo riferito al bambino separato dal campo — "il bambino deve fare X" — non è coerente con il metodo. Il soggetto grammaticale delle micro-azioni è sempre il campo, non il bambino.*

---

## SLIDE F3.1.3 — Cos'è il campo: una definizione operativa

**Tipo**: `diagram`
**Titolo**: Il campo relazionale di esperienza
**Sottotitolo**: I tre poli e le loro relazioni

**Contenuto principale**:

Schema visivo centrale: un **triangolo** con i tre vertici etichettati (Bambino / Adulto / Contesto). I tre lati del triangolo sono frecce bidirezionali, indicando la reciprocità delle relazioni. Al centro del triangolo, in testo piccolo: *"campo relazionale"*.

Ogni vertice è un nodo cliccabile. Cliccando un vertice si apre un pannello laterale (destra) con il contenuto corrispondente da `COMPONENTI_CAMPO`.

Struttura del pannello (aperto di default sul vertice "Adulto" all'entrata nella slide):
- Etichetta grande in `--color-accent` del componente
- Descrizione estesa
- Nota in corsivo, testo muto

**Didascalia sotto il triangolo**:

*Il campo non è la somma di tre elementi: è la configurazione delle relazioni tra loro.*

**Sezione inferiore — cosa F3 può modificare**:

Tre chip etichettati, ognuno con una domanda:

`Bambino` → *Non è il bersaglio dell'azione*
`Adulto` → *È il polo più direttamente modificabile*
`Contesto` → *Setting, ritmo, oggetti: modifiche possibili e immediate*

Sotto i chip, testo in `--color-text-secondary`:
*Il micro-dispositivo F3 agisce sul polo adulto e/o sul contesto. Il bambino risponde alla modificazione del campo — non è il destinatario delle istruzioni.*

**Nota in footer**:
*Nel caso-guida: il pediatra e il genitore sono il polo adulto. Il bilancio pediatrico e il libro illustrato sono il contesto. Nessuna micro-azione riguarderà direttamente il bambino.*

---

## SLIDE F3.1.4 — La distinzione centrale

**Tipo**: `comparison`
**Titolo**: Azione sul bambino o modifica del campo
**Sottotitolo**: Una distinzione strutturalmente necessaria

**Contenuto principale**:

Componente `ComparisonPanel` con i dati da `CONFRONTO_AZIONE`.

**Colonna sinistra** — "Azione sul bambino" (bordo superiore `--color-invalid`, sfondo rosso molto tenue):
- Titolo: *Il bambino come bersaglio*
- Tre esempi da `CONFRONTO_AZIONE.sinistra.items`:
  - Per ogni esempio: testo dell'azione in grassetto + problema in corsivo sotto, separati da un trattino sottile

**Colonna destra** — "Modifica del campo relazionale" (bordo superiore `--color-f3`, sfondo blu tenue):
- Titolo: *Il campo come bersaglio*
- Tre esempi da `CONFRONTO_AZIONE.destra.items`:
  - Per ogni esempio: testo dell'azione in grassetto + nota in corsivo sotto

**Footer a piena larghezza** (sfondo `--color-primary-light`, bordo sinistro `--color-f3`):
Testo da `CONFRONTO_AZIONE.footer.testo` in grassetto, centrato:
*"Lo strumento F3 non corregge il bambino: modifica il campo relazionale di esperienza in cui il bambino esiste."*

**Elemento aggiuntivo sotto il pannello** — in `--text-sm`, `--color-text-muted`, centrato:

*Nota: Le azioni della colonna sinistra non sono necessariamente sbagliate in altri framework. Il punto è che non sono strumenti F3: presuppongono il bambino come unità isolabile di intervento, il che è incoerente con i fondamenti di questo metodo.*

Questo testo rispetta il tono di `tono.md`: non critica le altre discipline, segnala solo l'incompatibilità con il framework.

---

## SLIDE F3.1.5 — Le tre proprietà del micro-dispositivo

**Tipo**: `interactive`
**Titolo**: Cosa rende un'azione un micro-dispositivo di campo
**Sottotitolo**: Tre proprietà, tutte necessarie

**Contenuto principale**:

Tre card espandibili verticali (componente `ExpandableCards`, `multiOpen: true`) con i dati da `TRE_PROPRIETA`.

**Struttura di ogni card** (stato compatto):

```
[Numero grande in --color-accent]  [Nome della proprietà]
[Prima frase del campo testo]
[Domanda-test in corsivo, sfondo tenue]          [↓ Espandi]
```

**Card espansa** (aggiunge tre sezioni sotto il fronte):

Testo completo della proprietà (`testo`), poi:

Riga con due chip affiancati:
- Chip verde (`--color-valid` bg): `✓ Es. — [esempio_ok]`
- Chip rosso (`--color-invalid` bg): `✗ Es. — [esempio_no]`

**Elemento visivo importante** — sotto le tre card, testo centrato in `--text-lg`:

*Un'azione che non rispetta anche una sola di queste proprietà non è un micro-dispositivo di campo: è un'altra cosa (un protocollo, una tecnica, un training). Non è sbagliata in assoluto — è fuori dal perimetro di F3.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-11`
- Label: Vincolo di scala
- Testo: *F3 produce micro-dispositivi, non programmi. Se il dispositivo richiede più incontri, setting separati o competenza tecnica specialistica per essere applicato, va riconsiderato alla luce di queste tre proprietà.*

---

## SLIDE F3.1.6 — Il caso-guida: il campo in cinque minuti

**Tipo**: `narrative`
**Titolo**: Cosa si modifica nel bilancio pediatrico
**Sottotitolo**: Applicazione del principio al caso-guida

**Contenuto principale**:

Layout a colonna singola, narrativo.

**Sezione superiore — la scena** (card narrativa, sfondo `--color-primary-light`, bordo sinistro `--color-primary`, testo da `window.CASO_GUIDA_F3.scena`):

*(Testo della scena in corsivo — non duplicare nel modulo, richiamare da `window.CASO_GUIDA_F3.scena`)*

**Sezione centrale — cosa si può modificare** (titolo `--text-lg`, grassetto: *"Il campo in questo caso ha tre poli. Cosa può cambiare?"*):

Due colonne:

**Colonna sinistra** (45%) — "Polo adulto: cosa chiediamo":

Lista ordinata con i dati da `CASO_GUIDA_M1.lettura_campo.adulto`. Ogni voce inizia con una piccola icona freccia (`→`) e testo normale. Nessun linguaggio imperativo: non "deve fare", ma "rallentare il ritmo", "nominare ciò che il bambino indica".

**Colonna destra** (55%) — "Polo contesto: setting e oggetti":

Lista ordinata con i dati da `CASO_GUIDA_M1.lettura_campo.contesto`. Stessa struttura della colonna sinistra.

**Sezione inferiore — il bambino non è nel target** (box separato, bordo superiore `--color-border`, sfondo `--color-bg`):

Titolo piccolo in `--text-sm`, `--color-text-muted`: *"Il bambino nel dispositivo"*

Testo da `CASO_GUIDA_M1.lettura_campo.bambino_non_target` in corsivo, `--text-base`.

Sotto, in `--text-sm`, `--color-text-secondary`:
*Il bambino risponderà (o non risponderà) alla modificazione del campo. Questa risposta è l'indicatore di risonanza che guiderà la rivalutazione della CE nel Modulo 2.*

**Chiusura del modulo** — testo centrato con spazio bianco sopra, `--text-lg`, corsivo:

*Nella prossima sezione vediamo come questa scena si traduce in una pipeline di trasformazione: dalla CE al dispositivo, passo per passo.*

Badge modulo successivo: `→ Modulo 2 — Dalla CE allo strumento`

---

## Note per l'implementazione

### Slide F3.1.1 — Schema visivo freccia

Lo schema `[Azione sul bambino] ← oppure → [Modifica del campo]` con la domanda al centro può essere realizzato come un semplice `<div>` flex con tre elementi (`span` sinistra, `span` centrale con punto interrogativo, `span` destra), separati da frecce SVG inline. Nessuna animazione richiesta — è statico.

### Slide F3.1.3 — Triangolo interattivo

Il triangolo dei tre poli è l'unico elemento visivo con SVG in questo modulo. Implementazione suggerita:

```javascript
// Struttura SVG essenziale: tre vertici + tre lati + testo centrale
// I vertici hanno: cerchio colorato (40px r) + etichetta testo
// I lati: path con frecce bidirezionali (marker-start e marker-end)
// Click sui cerchi: toggle del pannello laterale
// Stato active: cerchio con outline 3px e drop-shadow
```

Vertici (colori da `COMPONENTI_CAMPO`):
- Bambino: posizione in alto al centro → colore `var(--color-n3)`
- Adulto: posizione in basso a sinistra → colore `var(--color-n2)`
- Contesto: posizione in basso a destra → colore `var(--color-primary)`

Alternativa semplificata se SVG è complesso: tre card `position: relative` disposte a triangolo con CSS (`flex` + `margin auto` per il vertice superiore), con linee simulate da `border` o `::before`/`::after`. Risultato visivamente equivalente.

### Slide F3.1.5 — ExpandableCards

La slide usa `ExpandableCards` con `multiOpen: true` — il docente può tenere tutte e tre le proprietà aperte contemporaneamente per confrontarle. Aggiungere il pulsante globale "Espandi tutto / Comprimi tutto" come già definito per il Modulo 3 di F2.

L'animazione di apertura è `slide-down` con opacity (200ms). I chip verde/rosso degli esempi usano i colori semantici (`--color-valid-bg` e `--color-invalid-bg`), non i colori pieni — la distinzione non è valoriale ma esemplificativa.

### Slide F3.1.4 — Nota sul tono

La nota in fondo al `ComparisonPanel` ("Le azioni della colonna sinistra non sono necessariamente sbagliate in altri framework...") è un elemento deliberato di rispetto del tono del progetto (`tono.md`). Non deve essere rimossa o spostata — serve a comunicare che il confronto non è critica disciplinare ma delimitazione metodologica del perimetro F3.

### Transizione M0 → M1

All'entrata nel Modulo 1, nessuna transizione animata speciale. Il titolo del modulo appare con il normale fade-in (400ms). Opzionalmente: nella prima slide (F3.1.1), il blockquote con la "risposta naturale" può entrare con un leggero delay (300ms) rispetto al titolo — a enfatizzare che è la voce del professionista, non del corso.
