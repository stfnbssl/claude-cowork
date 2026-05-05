# f3-modulo-07 — Logica decisionale
**Numero slide**: 7
**Colore accent**: `#c0392b`
**Tipo prevalente**: diagram + standard + interactive

---

## Dati globali del modulo

Definire in `m07.js` le seguenti costanti. `QUATTRO_DOMANDE_DECISIONALI` è la sorgente concettuale del modulo; `CICLO_DECISIONALE` è già definito in `app.js` (§6.6 delle istruzioni) e viene richiamato qui tramite la funzione `DecisionCycle`.

```javascript
// Le quattro domande della logica decisionale F3
const QUATTRO_DOMANDE_DECISIONALI = [
  {
    id: 'd1',
    numero: 'D1',
    colore: 'var(--color-accent)',
    domanda: 'Dove si restringe il campo?',
    sottotitolo: 'La lettura della limitazione',
    spiegazione: `Non "qual è il problema del bambino" — ma "dove il campo
                  riduce la propria abitabilità?". La domanda è relazionale:
                  la restrizione è sempre una configurazione del campo,
                  non una proprietà isolata del bambino.
                  D1 emerge dalla lettura di T, A e dei nodi ↓ nella CE.`,
    nel_caso_guida: window.CASO_GUIDA_F3.f3.logicaDecisionale.D1,
    errore_tipico: `"Qual è il problema di questo bambino?"
                    Il soggetto grammaticale sbagliato: la restrizione non appartiene
                    al bambino — è una proprietà configurazionale del campo.`
  },
  {
    id: 'd2',
    numero: 'D2',
    colore: 'var(--color-accent)',
    domanda: 'Cosa funziona già?',
    sottotitolo: 'La lettura delle risorse',
    spiegazione: `Prima di cercare cosa non va, leggere cosa regge.
                  I nodi ↑ e i segnali di tenuta (T2+) indicano le risorse
                  su cui il dispositivo può appoggiarsi.
                  Un dispositivo che ignora le risorse esistenti
                  ricostruisce dal basso ciò che il campo ha già.
                  D2 emerge dalla lettura di N↑, T, A+ nella CE.`,
    nel_caso_guida: window.CASO_GUIDA_F3.f3.logicaDecisionale.D2,
    errore_tipico: `Saltare D2 e passare direttamente a D3.
                    Progettare l'azione senza conoscere le risorse porta
                    a dispositivi che lavorano in parallelo al campo
                    invece di appoggiarsi su ciò che già funziona.`
  },
  {
    id: 'd3',
    numero: 'D3',
    colore: 'var(--color-accent)',
    domanda: 'Qual è l\'azione che aumenta l\'abitabilità?',
    sottotitolo: 'La scelta dell\'orientamento',
    spiegazione: `Non "cosa sarebbe bello fare" — ma "quale azione, in questo campo
                  specifico, con queste risorse, nella direzione D indicata dalla CE,
                  produce un aumento dell'abitabilità?"
                  D3 è la domanda della funzione: orienta verso Stabilizzare,
                  Ampliare, Mediare o Proteggere in base alle risposte a D1 e D2.
                  Non prescrive il dispositivo: orienta la scelta della funzione.`,
    nel_caso_guida: window.CASO_GUIDA_F3.f3.logicaDecisionale.D3,
    errore_tipico: `Rispondere a D3 prima di D1 e D2.
                    La domanda "cosa fare?" senza aver letto la restrizione
                    e le risorse porta a scegliere la funzione per abitudine
                    o per preferenza professionale — non per lettura del campo.`
  },
  {
    id: 'd4',
    numero: 'D4',
    colore: 'var(--color-accent)',
    domanda: 'Qual è il minimo intervento sufficiente?',
    sottotitolo: 'Il principio della parsimonia',
    spiegazione: `Una volta identificata la funzione (D3), la quarta domanda
                  chiede: qual è la versione più semplice, più breve,
                  più integrabile che realizza quella funzione in questo campo?
                  Il principio del minimo intervento sufficiente non è rinuncia:
                  è precisione. Interventi più complessi rischiano di
                  sovraordinare l'azione professionale al campo invece di
                  inserirsi in esso.`,
    nel_caso_guida: window.CASO_GUIDA_F3.f3.logicaDecisionale.D4,
    errore_tipico: `"Se un dispositivo semplice funziona, uno più elaborato funzionerà meglio."
                    No: un dispositivo sovradimensionato rispetto al campo
                    può produrre nuove restrizioni (es. ampliare un campo
                    che ha bisogno di mediazione). Il minimo non è il meno
                    ambizioso — è il più calibrato.`
  }
];

// Errori decisionali ricorrenti
const ERRORI_DECISIONALI = [
  {
    id: 'ed1',
    titolo: 'Decidere senza leggere la CE',
    descrizione: `L'azione viene scelta sulla base di categorie preesistenti
                  (diagnosi, protocollo standard, preferenza tecnica)
                  senza che la CE abbia orientato la scelta della funzione.`,
    meccanismo: `Il professionista ha già una risposta prima che D1 venga posta.
                 La CE, se prodotta, serve per giustificare la scelta
                 già fatta — non per orientarla.`,
    conseguenza: `Il dispositivo è coerente con la categoria, non con il campo.
                  Può produrre effetti inappropriati: stabilizzare un campo
                  che andrebbe ampliato, ampliare un campo che andrebbe protetto.`,
    antidoto: `Porre D1 prima di qualsiasi altra domanda. La risposta a D1
               deve emergere dalla CE, non da ipotesi cliniche sul bambino.`
  },
  {
    id: 'ed2',
    titolo: 'Insistere quando l\'indicatore di risonanza è assente',
    descrizione: `Il dispositivo viene applicato ripetutamente anche quando
                  il campo non risponde — aumentando intensità, frequenza
                  o durata della stessa azione.`,
    meccanismo: `Il professionista interpreta l'assenza di risposta come
                 insufficienza del dispositivo ("non ne abbiamo fatto abbastanza")
                 invece che come segnale di riallineamento da leggere.`,
    conseguenza: `Il campo può rispondere con chiusura, rifiuto o aumento della
                  disorganizzazione. Si entra in un ciclo in cui il dispositivo
                  errato viene potenziato invece di essere rivalutato.`,
    antidoto: `L'assenza dell'indicatore di risonanza è un segnale di rientro:
               tornare a D1 con la CE aggiornata. Non si insiste: si rilegge.`
  },
  {
    id: 'ed3',
    titolo: 'Confondere il nodo bersaglio con il sintomo presentato',
    descrizione: `Il nodo dominante viene identificato con il comportamento
                  che il bambino esprime — il sintomo visibile — invece che
                  con il nodo la cui attivazione muove il campo.`,
    meccanismo: `Il professionista risponde a D1 ("dove si restringe il campo?")
                 descrivendo il comportamento del bambino invece della configurazione
                 del campo. Il nodo dominante diventa "il bambino che non parla"
                 invece di "N3 come condizione di accesso al mondo condiviso".`,
    conseguenza: `Il dispositivo punta al sintomo, non al campo.
                  Non produce effetti sulla configurazione relazionale
                  perché non ha agganciato il nodo giusto.`,
    antidoto: `Riformulare D1 in termini di configurazione del campo: non
               "il bambino che X" ma "il campo in cui X non è disponibile".`
  },
  {
    id: 'ed4',
    titolo: 'Usare il ciclo una volta sola',
    descrizione: `Il ciclo decisionale viene applicato una volta — all'inizio
                  del lavoro — e il dispositivo scelto viene mantenuto
                  invariato anche quando il campo cambia.`,
    meccanismo: `Il professionista tratta il ciclo come un protocollo di avvio
                 invece che come una struttura ricorrente. La CE non viene
                 aggiornata dopo l'applicazione del dispositivo.`,
    conseguenza: `Il dispositivo perde progressivamente coerenza con il campo
                  reale. Continua ad agire su una configurazione che non esiste più.
                  Il campo si muove; il dispositivo rimane fermo.`,
    antidoto: `Il ciclo non è lineare: torna su se stesso. Dopo ogni applicazione,
               il passo OSSERVA DI NUOVO richiede di rileggere il campo
               e aggiornare la CE — anche parzialmente.`
  }
];

// Applicazione del ciclo al caso-guida
const CICLO_CASO_GUIDA = {
  osserva: {
    label: 'OSSERVA',
    contenuto: `La scena: bilancio pediatrico. Bambino 18–24 mesi, genitore presente,
                libro illustrato sul tavolo. Il bambino prende il libro, indica immagini,
                vocalizza, cerca lo sguardo dell'adulto. Il genitore risponde, nomina,
                aspetta. Il pediatra osserva.
                Il campo è attivo: c'è scambio. Ma la sequenza si interrompe
                prima che si consolidi — il bambino non mantiene il filo del ciclo.`
  },
  leggi: {
    label: 'LEGGI (CE)',
    contenuto: `CE: N1~ N2↑ N3~ N4↓.
                R: N2→N3. D↗. T2. A±.
                Campo relazionale forte (N2↑) che sostiene accesso al mondo condiviso (N3~),
                con esplorazione ridotta (N4↓). Configurazione fragile ma evolutivamente aperta.`,
    highlight: ['N2', 'N3', 'N4']
  },
  orienta: {
    label: 'ORIENTA (funzione)',
    contenuto: `D1: La restrizione è nella durata della sequenza condivisa — N3 non si stabilizza.
                D2: La risorsa è N2↑: il campo relazionale regge. Il genitore risponde.
                D3: T2 e R: N2→N3 e D↗ → MEDIAZIONE: sostenere la transizione già in corso.
                D4: Il minimo è modificare il ritmo adulto nella scena — non aggiungere materiali.`
  },
  agisci: {
    label: 'AGISCI (micro-dispositivo)',
    contenuto: `Funzione: MEDIAZIONE. Tipi: U2+U4.
                Il genitore segue l'interesse del bambino, nomina con ritmo lento,
                attende, espande senza correggere.
                Il pediatra osserva senza interrompere.
                Tempo reale: 5 minuti nel bilancio.`
  },
  osservaDiNuovo: {
    label: 'OSSERVA DI NUOVO',
    contenuto: `Indicatore di risonanza: il bambino include l'adulto nella sequenza
                con sguardo condiviso, gesto e vocalizzazione integrati.
                La sequenza si allunga — non termina al primo giro.
                Se presente → la CE si aggiorna: N3 si stabilizza, T tende a T3.
                Se assente → rientrare a D1 con la CE aggiornata.`,
    indicatore: window.CASO_GUIDA_F3.f3.indicatoreRisonanza
  }
};
```

---

## SLIDE F3.7.1 — Chi decide?

**Tipo**: `standard`
**Titolo**: F3 orienta la decisione — non la prende
**Sottotitolo**: Il ruolo del professionista nella logica decisionale

**Contenuto principale**:

Layout a colonna singola. Slide di apertura che stabilisce il nodo etico-metodologico del modulo: la responsabilità della decisione è professionale, non algoritmica.

**Sezione superiore — la posizione di F3**:

Testo `--text-lg`, centrato, spazio verticale:

*F3 produce quattro cose: una lettura del campo (CE), un nodo dominante, una funzione, un dispositivo.*

*Non produce: la decisione di applicare il dispositivo.*

**Sezione centrale — tre livelli della decisione**:

Schema verticale a tre livelli, ognuno un blocco con bordo sinistro colorato:

**Livello 1** — bordo `--color-f2`:
*Livello della lettura (F2)*
*La CE descrive la configurazione del campo.*
*Non prescrive: descrive.*

**Livello 2** — bordo `--color-f3`:
*Livello dell'orientamento (F3)*
*Il nodo dominante e la funzione orientano la scelta del dispositivo.*
*Non prescrivono: orientano.*

**Livello 3** — bordo `--color-accent` (più spesso):
*Livello della decisione professionale*
*Il professionista legge il campo reale in tempo reale e decide se, quando e come applicare il dispositivo.*
*Questo livello non è automatizzabile: è situato, responsabile, disciplinare.*

Frecce discendenti tra i tre livelli. L'ultimo livello ha uno sfondo tenuissimo `--color-accent-light` per segnalarne il peso.

**Sezione inferiore — la domanda che resta**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Se F3 orienta ma non decide, come si decide in tempo reale? Come si pone la domanda giusta al momento giusto, con il bambino davanti, in un contesto che non aspetta?*

*Questo è il contenuto di M7: la logica decisionale come struttura di domande — non come algoritmo.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-70`
- Label: La responsabilità della decisione è professionale
- Testo: *F3 non sostituisce il giudizio professionale situato. Produce vincoli di coerenza metodologica — non obblighi. La responsabilità della scelta finale appartiene al professionista nella sua disciplina.*

---

## SLIDE F3.7.2 — Le quattro domande

**Tipo**: `interactive`
**Titolo**: Quattro domande, in ordine
**Sottotitolo**: La struttura della logica decisionale F3

**Contenuto principale**:

Quattro blocchi verticali sempre visibili (non ExpandableCards — tutti mostrati simultaneamente per consentire la lettura della sequenza). Dati da `QUATTRO_DOMANDE_DECISIONALI`.

**Elemento sopra i blocchi**:

Testo `--text-base` `--color-text-secondary`:
*La logica decisionale di F3 si struttura in quattro domande sequenziali. Ognuna dipende dalla risposta alla precedente. Saltare una domanda o invertire l'ordine produce errori decisionali — che esploriamo nella slide F3.7.5.*

**Struttura di ogni blocco** (sempre visibile):

```
┌─────────────────────────────────────────────────────────────┐
│  [D1/D2/D3/D4 — badge rosso --color-accent]
│  [domanda in --text-xl grassetto]
│  [sottotitolo in --text-sm corsivo --color-text-secondary]
│
│  [spiegazione in --text-base, bordo sinistro --color-accent]
│
│  [box "Nel caso-guida" — sfondo --color-primary-light]:
│    [nel_caso_guida — testo, --text-sm]
│
│  [box "Errore tipico" — sfondo rosso tenuissimo, --text-sm]:
│    [errore_tipico — corsivo]
└─────────────────────────────────────────────────────────────┘
```

I quattro blocchi sono separati da un divisore `--color-border`. La numerazione D1→D4 è progressiva: badge quadrati con numero grande `--text-2xl`.

**Elemento sotto i blocchi** — frecce connettive:

Tra ogni coppia di blocchi adiacenti, una piccola freccia verso il basso con testo `--text-xs` `--color-text-muted`:
- D1 → D2: *"Conoscendo la restrizione..."*
- D2 → D3: *"Conoscendo le risorse..."*
- D3 → D4: *"Scelta la funzione..."*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-71`
- Label: L'ordine delle domande non è arbitrario
- Testo: *D3 (qual è l'azione che aumenta l'abitabilità?) può essere posta solo dopo D1 e D2. Senza conoscere la restrizione e le risorse, la risposta a D3 è una preferenza — non una lettura del campo.*

---

## SLIDE F3.7.3 — Il Ciclo Decisionale Breve

**Tipo**: `diagram`
**Titolo**: Il ciclo che non finisce
**Sottotitolo**: Dalla CE all'azione — e di nuovo all'osservazione

**Contenuto principale**:

Componente `DecisionCycle(CICLO_DECISIONALE, container)` come descritto in `ISTRUZIONI_CLAUDE_CODE_F3.md` §6.6. Il componente usa i dati già definiti in `app.js` — `m07.js` lo richiama, non lo ridefinisce.

**Intestazione sopra il componente**:

Testo `--text-base` `--color-text-secondary`, centrato:
*Il Ciclo Decisionale Breve è la struttura operativa che integra le quattro domande in un percorso circolare. Non è lineare: il suo ultimo passo (OSSERVA DI NUOVO) riapre il primo.*

**Il componente `DecisionCycle`**:

Cerchio pentagonale con cinque nodi:

```
         OSSERVA
        /       \
OSSERVA          LEGGI
DI NUOVO         (CE)
        \       /
     AGISCI   ORIENTA
    (disp.)  (funz.)
```

Comportamento interattivo (dal §6.6):
1. Al caricamento della slide, i nodi appaiono in sequenza con animazione (200ms per nodo).
2. Clic su ogni nodo → pannello laterale destro con: label + descrizione + domanda guida + nota.
3. Pulsante "Anima ciclo" percorre tutti i nodi automaticamente (800ms per nodo).
4. La freccia dal nodo 5 (OSSERVA DI NUOVO) al nodo 1 (OSSERVA) è curva e ha colore `--color-accent` — evidenzia la chiusura del ciclo.

**Pannello laterale** (aperto di default su ORIENTA — il nodo metodologicamente centrale):

Il pannello mostra il contenuto del nodo selezionato da `CICLO_DECISIONALE` (in `app.js`). Il nodo ORIENTA ha `colore: var(--color-f3)` e la nota: *"Non si sceglie la tecnica: si sceglie la funzione."*

**Sezione inferiore** — la proprietà fondamentale del ciclo:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Il ciclo non è un algoritmo: è una struttura di attenzione.*
*Ogni professionista lo percorre con velocità e profondità diverse a seconda del contesto, del tempo disponibile, della familiarità con il campo.*
*In un bilancio pediatrico di 20 minuti, il ciclo può durare 2–3 minuti.*
*In una consultazione di valutazione, può durare una sessione intera.*

Indicazione temporale (dal §6.6): *"5–10 minuti nel contesto professionale reale."*

**Nota in footer**:
*Nel contesto di emergenza regolativa (campo T0), il ciclo si comprima: OSSERVA → valuta T → AGISCI con Stabilizzare. Le quattro domande D1–D4 non sempre richiedono formulazione esplicita — la struttura può essere percorsa tacitamente.*

---

## SLIDE F3.7.4 — Il ciclo nel caso-guida

**Tipo**: `narrative`
**Titolo**: Il ciclo applicato al bilancio pediatrico
**Sottotitolo**: Cinque passi, cinque minuti, un campo che risponde

**Contenuto principale**:

Layout a colonna singola con cinque blocchi sequenziali animati — stesso pattern della slide F3.3.5 (M3, step-by-step). Dati da `CICLO_CASO_GUIDA`.

**Intestazione**:

Scena del caso-guida in card narrativa (sfondo `--color-primary-light`, bordo `--color-primary`, testo da `window.CASO_GUIDA_F3.scena` in corsivo — **non parafrasare, usare il testo da `window.CASO_GUIDA_F3.scena`**).

**Cinque blocchi step-by-step**:

Al caricamento della slide, solo il primo blocco è visibile. Un pulsante "→ Passo successivo" rivela i blocchi uno alla volta. Un pulsante "Mostra tutto" li rivela tutti contemporaneamente.

**Blocco 1 — OSSERVA** (bordo sinistro `--color-f2`):
Badge `OSSERVA` + testo `CICLO_CASO_GUIDA.osserva.contenuto`.

**Blocco 2 — LEGGI (CE)** (bordo sinistro `--color-f2`):
Badge `LEGGI (CE)` + testo `CICLO_CASO_GUIDA.leggi.contenuto`.
Sotto il testo: `CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: CICLO_CASO_GUIDA.leggi.highlight, compact: true })`.

**Blocco 3 — ORIENTA** (bordo sinistro `--color-f3`, bordo più spesso):
Badge `ORIENTA (funzione)` + testo `CICLO_CASO_GUIDA.orienta.contenuto`.
Chip risultato: badge `D1 → D2 → D3 → D4` in sequenza, poi freccia `→` badge `MED Mediazione` colore `var(--color-fn-mediare)`.

**Blocco 4 — AGISCI** (bordo sinistro `--color-f3`):
Badge `AGISCI (micro-dispositivo)` + testo `CICLO_CASO_GUIDA.agisci.contenuto`.
Chip `U2 Sintonizzazione` + `U4 Mediazione Simbolica` affiancati.

**Blocco 5 — OSSERVA DI NUOVO** (bordo sinistro `--color-accent`, bordo curvo in alto a destra con freccia che torna al blocco 1):
Badge `OSSERVA DI NUOVO` + testo `CICLO_CASO_GUIDA.osservaDiNuovo.contenuto`.
Box verde `--color-guardrail-bg`: *"Indicatore di risonanza: [indicatore]"* con testo da `CICLO_CASO_GUIDA.osservaDiNuovo.indicatore`.

**Connettivo visivo**: a sinistra dei cinque blocchi, una linea verticale tratteggiata `--color-border`. Ogni blocco si attacca alla linea con un piccolo cerchio colorato. Dal blocco 5 la linea ha una freccia curva che risale verso il blocco 1 (rientro al ciclo), colorata `--color-accent`.

**Nota in footer**:
*In questo caso il ciclo porta a una risposta al passo 3 (ORIENTA). In altri casi il ciclo può ripartire più volte prima che l'azione sia identificata — specialmente quando la CE è parziale o i segnali sono ambigui.*

---

## SLIDE F3.7.5 — Errori decisionali

**Tipo**: `interactive`
**Titolo**: Quando il ciclo si inceppa
**Sottotitolo**: Quattro errori ricorrenti nella logica decisionale

**Contenuto principale**:

Quattro card orizzontali compatte, sempre visibili (stesso pattern delle slide errori in M3 e M4). Dati da `ERRORI_DECISIONALI`.

**Struttura di ogni card**:

```
┌─────────────────────────────────────────────────────────────┐
│  [Numero ①②③④ --color-accent]  [titolo grassetto]
│
│  Descrizione: [descrizione, --text-sm, --color-text-secondary]
│
│  ╔═══════════════════════════════════════════════════════╗
│  ║ Meccanismo: [meccanismo, --text-sm, bordo --color-warning] ║
│  ╚═══════════════════════════════════════════════════════╝
│
│  Conseguenza: [conseguenza, --text-sm, sfondo rosso tenue]
│
│  Antidoto: [antidoto, --text-sm, sfondo --color-guardrail-bg, bordo --color-guardrail]
└─────────────────────────────────────────────────────────────┘
```

Le card hanno bordo sinistro `--color-invalid`. La sezione "Antidoto" ha bordo sinistro `--color-valid` per segnalare il riorientamento.

**Elemento sopra le card**:

Riga di quattro chip rossi tenuissimi con le etichette brevi degli errori:
*"①Senza CE · ②Insistere · ③Sintomo per nodo · ④Ciclo lineare"*

**Sezione inferiore** — testo di raccordo `--text-sm` `--color-text-muted` centrato:

*Questi quattro errori condividono una radice comune: il ciclo viene percorso in modo lineare (una volta sola, in un'unica direzione) invece che circolare. L'antidoto non è fare il ciclo "meglio" — è fare il ciclo di nuovo, a partire dall'osservazione aggiornata.*

---

## SLIDE F3.7.6 — Il professionista come regolatore di campo

**Tipo**: `standard`
**Titolo**: Non un esecutore di protocolli
**Sottotitolo**: Il professionista come lettore adattivo del campo

**Contenuto principale**:

Layout a colonna singola. Slide di reframe identitario: non chiude il ciclo ma ridescrive il ruolo del professionista alla luce di tutto ciò che F3 ha costruito.

**Sezione superiore — la distinzione**:

`ComparisonPanel`:

**Colonna sinistra** — "Il professionista come esecutore" (bordo `--color-invalid`):

Titolo: *"Logica del protocollo"*

Tre caratteristiche:
- *Applica una sequenza predefinita indipendentemente dal campo.*
- *Valuta il successo in base alla fedeltà al protocollo, non alla risposta del campo.*
- *Aumenta la dose se il campo non risponde: più sessioni, più intensità.*

Sotto, corsivo `--color-text-secondary`:
*Non è un approccio sbagliato: è un approccio diverso, con una logica propria. Ma non è la logica di F3.*

**Colonna destra** — "Il professionista come regolatore di campo" (bordo `--color-accent`):

Titolo: *"Logica del ciclo adattivo"*

Tre caratteristiche:
- *Legge il campo prima di agire, durante l'azione, e dopo l'azione.*
- *Valuta il successo in base alla risposta del campo (indicatore di risonanza), non al dispositivo in sé.*
- *Se il campo non risponde, rivaluta la CE — non insiste.*

Sotto, corsivo `--color-accent`:
*Il professionista di F3 non è meno tecnico: ha una competenza tecnica più raffinata — quella di leggere il campo e modificare il dispositivo in base alla risposta.*

**Sezione inferiore — la competenza F3**:

Tre blocchi orizzontali, sfondo `--color-bg`, bordo `--color-border`:

**Blocco 1** — "Competenza di lettura":
*Leggere una CE in meno di tre minuti e identificare il nodo dominante e la funzione.*
*Non richiede sessioni separate: si integra nell'osservazione professionale già in atto.*

**Blocco 2** — "Competenza di azione minima":
*Scegliere il dispositivo più semplice che realizza la funzione.*
*Resistere alla tentazione di fare di più quando meno è sufficiente.*

**Blocco 3** — "Competenza di aggiornamento":
*Riconoscere quando l'indicatore di risonanza è assente e rientrare nel ciclo.*
*Non interpretare l'assenza di risposta come fallimento del bambino — come segnale di riallineamento.*

**Nota in footer**:
*Questa descrizione del professionista di F3 non prescinde dalla formazione disciplinare: la aggiunge. Il pediatra resta pediatra; l'educatrice resta educatrice. F3 offre un vocabolario di lettura del campo che si integra in ciascuna professione senza sostituirne il corpus tecnico.*

---

## SLIDE F3.7.7 — Tutto è in mano

**Tipo**: `narrative`
**Titolo**: La pipeline è completa
**Sottotitolo**: Dalla CE osservata al micro-dispositivo contestualizzato

**Contenuto principale**:

Layout a colonna singola. Slide di chiusura del modulo — bridge verso M8 che rivedrà tutto dall'inizio.

**Sezione superiore — il percorso compiuto**:

Schema orizzontale compatto — pipeline ridotta a otto elementi con frecce:

```
[Osservazione]  →  [CE]  →  [Nodo dominante]  →  [Funzione]
                                     ↓
[Indicatore risonanza]  ←  [Micro-dispositivo]  ←  [Tipo U]
```

Layout a due righe, frecce continue. Ogni elemento è un chip piccolo colorato (colori di modulo: F2 per i primi due, F3 per i successivi). La freccia di rientro (indicatore → osservazione nuova) è curva, colorata `--color-accent`.

Sotto lo schema, testo `--text-sm` `--color-text-muted` centrato:
*I moduli M0–M7 hanno costruito questa pipeline pezzo per pezzo.*
*M8 la percorre per intero in un unico movimento.*

**Sezione centrale — cosa M8 fa**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Nel Modulo 8 — l'ultimo — non introduciamo nuovi concetti.*
*Prendiamo il caso-guida dall'inizio: dalla scena osservata durante il bilancio pediatrico.*
*E lo portiamo fino in fondo: CE, nodo dominante, funzione, template, tipo universale, ciclo decisionale, indicatore di risonanza.*

*Tutto insieme. In sequenza. Con la stessa densità del lavoro professionale reale.*

**Sezione inferiore — la domanda aperta**:

Blockquote centrato, bordo sinistro `--color-accent`:

> *"Cosa rimane dopo M8?"*
> *Un vocabolario per leggere il campo.*
> *Una struttura per decidere in situazione.*
> *Un principio: lo strumento non corregge il bambino — modifica il campo.*

Sotto, in `--text-base` centrato:
*Con questi strumenti, ogni nuova scena può diventare una CE. Ogni CE può diventare un dispositivo. Ogni dispositivo può tornare a essere osservazione.*

Badge modulo successivo: `→ Modulo 8 — Pipeline F3 completa`

---

## Note per l'implementazione

### Slide F3.7.2 — Quattro blocchi sequenziali

I quattro blocchi D1–D4 non usano `ExpandableCards`: sono sempre espansi. Il motivo è pedagogico — il partecipante deve poter confrontare le quattro domande simultaneamente per percepire la sequenza. L'altezza totale può superare l'area slide visibile: rendere l'area slide scorrevole verticalmente per questa slide (`overflow-y: auto` sul container). Evitare paginazione interna.

### Slide F3.7.3 — DecisionCycle

Il componente `DecisionCycle` è definito in `app.js`. In `m07.js` si chiama semplicemente:

```javascript
// In onEnter della slide F3.7.3
const container = document.querySelector('#decision-cycle-container');
DecisionCycle(CICLO_DECISIONALE, container);
```

dove `CICLO_DECISIONALE` è la costante definita in `app.js` (§6.6 delle istruzioni). Non ridefinire la costante nel modulo.

Il pannello laterale si apre automaticamente sul nodo `orienta` (index 2) al caricamento — il nodo metodologicamente più importante per M7. L'utente può poi cliccare liberamente sugli altri nodi.

### Slide F3.7.4 — Step-by-step con rientro visivo

Il rientro visivo (freccia curva dal blocco 5 al blocco 1) si implementa con un elemento SVG assoluto posizionato sopra la colonna sinistra: una curva `<path>` con `stroke: var(--color-accent)` e `fill: none`, con un `marker-end` freccia. L'elemento è mostrato solo dopo che il blocco 5 è diventato visibile.

Il chip `D1 → D2 → D3 → D4` nel blocco 3 (ORIENTA) è implementato come quattro badge piccoli `<span class="badge badge--d">D1</span>` con frecce `→` in `--color-text-muted` tra di loro. Non usare icone SVG: frecce in testo ASCII `→` sono sufficienti e più facili da gestire nell'inline HTML.

### Slide F3.7.6 — ComparisonPanel con nota di tono

La colonna sinistra ("esecutore di protocolli") segue la regola di tono di F3 (da `tono.md`): non è un approccio sbagliato ma diverso, con logica propria. La nota in corsivo sotto la colonna sinistra deve essere presente — è il segnale che F3 non è polemico con gli approcci protocollorizzati, ma li descrive come metodologicamente distinti.

### Colore accent rosso

L'accent di M7 è `#c0392b` — rosso scuro. Questo colore richiama la decisionalità, la responsabilità, il peso del giudizio professionale. I guardrail di M7 (C-F3-70 e C-F3-71) usano il verde standard `--color-guardrail` — non il rosso del modulo — per mantenere la distinzione semantica tra "vincolo metodologico" e "colore del modulo".
