# f3-modulo-05 — Il micro-dispositivo
**Numero slide**: 8
**Colore accent**: `#2d6a4f`
**Tipo prevalente**: interactive + standard + narrative

---

## Dati globali del modulo

Definire in `m05.js` le seguenti costanti. `TEMPLATE_F3_CAMPI` è la sorgente strutturale del modulo e viene usata nel F3Builder e nella slide del template compilato.

```javascript
// Struttura descrittiva dei 7 campi del Template F3
const TEMPLATE_F3_CAMPI = [
  {
    numero: 1,
    id: 'ceOrigine',
    label: 'CE di origine',
    domanda: 'Qual è la configurazione del campo da cui partiamo?',
    descrizione: `La sintesi grammaticale della CE prodotta in F2.
                  Non una lista di nodi: una frase che descrive il campo
                  come configurazione relazionale dinamica.`,
    formato: 'Frase descrittiva — es. "Campo relazionale forte che sostiene accesso al mondo condiviso simbolico, con esplorazione ridotta ma in espansione."',
    esempio: window.CASO_GUIDA_F3.ce.grammaticale,
    errore: 'Non copiare i nodi uno per uno: serve la lettura d\'insieme, non l\'elenco.'
  },
  {
    numero: 2,
    id: 'nodoDominante',
    label: 'Nodo dominante',
    domanda: 'Quale nodo, se attivato, muove di più il campo nella direzione evolutiva indicata?',
    descrizione: `Il nodo la cui apertura produce la variazione più rilevante per l'abitabilità
                  complessiva del campo. Non è necessariamente il nodo con lo stato più basso.
                  Identificato nella F3 tramite i quattro criteri (M3).`,
    formato: 'Codice + nome — es. "N3 — Accesso al mondo condiviso simbolico"',
    esempio: `${window.CASO_GUIDA_F3.f3.nodoDominante.codice} — ${window.CASO_GUIDA_F3.f3.nodoDominante.nome}`,
    errore: 'Non confondere con il nodo di sostegno (N2) o con il nodo in tensione (N4): ognuno ha un ruolo distinto nel template.'
  },
  {
    numero: 3,
    id: 'funzione',
    label: 'Funzione',
    domanda: 'Cosa deve fare il dispositivo sul campo?',
    descrizione: `Una delle quattro funzioni F3: Stabilizzare / Ampliare / Mediare / Proteggere.
                  Scelta attraverso la sequenza decisionale (M4) a partire da T, A, R, D nella CE.
                  Non si sceglie la tecnica: si sceglie la funzione.`,
    formato: 'Enum: STABILIZZARE · AMPLIARE · MEDIARE · PROTEGGERE',
    esempio: window.CASO_GUIDA_F3.f3.funzione,
    errore: 'Non nominare una tecnica (es. "lettura dialogica"): la funzione è categoriale, non tecnica.'
  },
  {
    numero: 4,
    id: 'campoBersaglio',
    label: 'Campo bersaglio',
    domanda: 'Quale aspetto del campo deve cambiare?',
    descrizione: `La condizione relazionale che il dispositivo mira a modificare.
                  Descrive il campo come dovrebbe essere dopo il dispositivo, non
                  come si descrive il bambino o il comportamento atteso.
                  Il soggetto grammaticale è il campo, non il bambino.`,
    formato: 'Frase nominale — es. "Stabilità e durata dello scambio condiviso simbolico"',
    esempio: window.CASO_GUIDA_F3.f3.campoBersaglio,
    errore: '"Far sì che il bambino indichi di più" — no: il soggetto non può essere il bambino. "Ampliamento del repertorio verbale" — no: descrive una competenza, non una condizione relazionale.'
  },
  {
    numero: 5,
    id: 'microAzioni',
    label: 'Micro-azioni',
    domanda: 'Quali azioni concrete, osservabili e minime modificano il campo verso il campo bersaglio?',
    descrizione: `Lista ordinata di 3–5 azioni. Ogni azione deve essere:
                  breve (realizzabile nella situazione senza ristrutturarla),
                  integrabile (coerente con ciò che il professionista sta già facendo),
                  osservabile (il suo effetto è rilevabile nel campo in tempo reale).
                  Il soggetto è l'adulto o il setting — mai il bambino.`,
    formato: 'Lista ordinata, 3–5 voci. Ogni voce: verbo + oggetto relazionale.',
    esempio: window.CASO_GUIDA_F3.f3.microAzioni,
    errore: '"Guidare il bambino a indicare con il dito" → azione sul bambino. "Fare una sessione di 30 minuti di scaffolding" → non è integrabile in un bilancio. Le micro-azioni modificano il comportamento adulto o le condizioni ambientali, non le competenze del bambino.'
  },
  {
    numero: 6,
    id: 'tempoReale',
    label: 'Tempo reale',
    domanda: 'In quanto tempo il dispositivo si realizza nel contesto specifico?',
    descrizione: `Non il tempo ideale: il tempo effettivamente disponibile nel contesto professionale
                  in cui il dispositivo si inserisce. Il principio del minimo intervento sufficiente
                  si applica anche al tempo: meno è meglio, se produce lo stesso effetto sul campo.`,
    formato: 'Stima in minuti o range — es. "5 minuti durante il bilancio pediatrico"',
    esempio: window.CASO_GUIDA_F3.f3.tempoReale,
    errore: 'Non sovrastimare il tempo disponibile nel contesto reale. Un dispositivo di 45 minuti non è un micro-dispositivo: è una sessione.'
  },
  {
    numero: 7,
    id: 'indicatoreRisonanza',
    label: 'Indicatore di risonanza',
    domanda: 'Come si riconosce che il campo ha risposto al dispositivo?',
    descrizione: `L'indicatore di risonanza è un segnale osservabile nel campo
                  — non nel bambino isolato — che indica che il dispositivo ha
                  prodotto un cambiamento nell'esperienza relazionale.
                  Permette di aggiornare la CE dopo l'azione e, se assente,
                  segnala che la funzione o il dispositivo vanno rivalutati.`,
    formato: 'Descrizione comportamentale osservabile nel campo (bambino + adulto + contesto)',
    esempio: window.CASO_GUIDA_F3.f3.indicatoreRisonanza,
    errore: '"Il bambino sorride" → segnale del bambino, non del campo. "Il bambino impara a condividere" → obiettivo di sviluppo, non indicatore di risonanza. L\'indicatore di risonanza riguarda la qualità dello scambio relazionale, non il progresso del bambino.'
  }
];

// Criteri per le micro-azioni: cosa le rende valide nel perimetro F3
const MICRO_AZIONI_CRITERI = [
  {
    id: 'breve',
    label: 'Breve e integrabile',
    colore: 'var(--color-accent)',
    descrizione: `Realizzabile nella situazione senza ristrutturarla.
                  Il professionista non ha bisogno di interrompere quello che sta facendo:
                  il dispositivo si inserisce nel flusso già in corso.`,
    test: 'Posso farlo adesso, qui, con quello che ho?',
    esempio_ok: 'Rallentare il ritmo del commento e aspettare la risposta del bambino.',
    esempio_no: 'Organizzare una sessione separata di lettura condivisa di 20 minuti.'
  },
  {
    id: 'non-specialistico',
    label: 'Non specialistico e reversibile',
    colore: 'var(--color-accent)',
    descrizione: `Non richiede formazione specifica per essere eseguito,
                  e può essere interrotto senza conseguenze negative se il campo
                  non risponde. Non produce dipendenza o effetti collaterali strutturali.`,
    test: 'Se smetto, il campo torna alla sua condizione precedente senza danni?',
    esempio_ok: 'Il genitore segue l\'iniziativa del bambino invece di dirigerla.',
    esempio_no: 'Prescrivere una terapia logopedica bi-settimanale di 12 sessioni.'
  },
  {
    id: 'osservabile',
    label: 'Osservabile nei suoi effetti',
    colore: 'var(--color-accent)',
    descrizione: `L'effetto del dispositivo è rilevabile nel campo in tempo reale.
                  Non si tratta di valutare il bambino: si tratta di leggere
                  come il campo risponde all'azione. L'indicatore di risonanza
                  permette di decidere se continuare o rivalutare.`,
    test: 'Sono in grado di vedere se il campo sta rispondendo?',
    esempio_ok: 'La sequenza bambino-adulto si allunga: il bambino non interrompe lo scambio.',
    esempio_no: '"Il bambino migliorerà nel tempo" — non osservabile in tempo reale.'
  }
];

// Struttura dell'Output-tipo vuoto: cinque sezioni A–E
const OUTPUT_TIPO_STRUTTURA = [
  {
    sezione: 'A',
    titolo: 'Campo condiviso',
    domanda: 'Cosa è condiviso tra bambino e adulto in questa situazione? Come funziona l\'incontro?',
    descrizione: `Descrive la qualità dello spazio relazionale in atto:
                  cosa è percepito insieme, come è organizzata la presenza reciproca.
                  Non descrive il bambino, ma il campo nella sua struttura presente.`,
    focus: 'La configurazione attuale dello scambio — cos\'è attivo, cos\'è assente.',
    esempio: window.CASO_GUIDA_F3.f3.outputTipo.A,
    nota: 'Il campo condiviso non è "buono" o "cattivo": è strutturato in un certo modo. La sezione descrive quella struttura senza valutarla.'
  },
  {
    sezione: 'B',
    titolo: 'Posizione soggettiva',
    domanda: 'Qual è la posizione del bambino in questa configurazione? Come si situa rispetto all\'altro e all\'oggetto?',
    descrizione: `Descrive la posizione che il bambino occupa nel campo relazionale:
                  come si orienta verso l'adulto, verso l'oggetto, verso l'esperienza.
                  Non è una descrizione di competenze o deficit: è la lettura di
                  come il soggetto è presente in quel campo specifico.`,
    focus: 'Iniziativa, orientamento, risposta — nel campo, non isolati.',
    esempio: window.CASO_GUIDA_F3.f3.outputTipo.B,
    nota: 'Non confondere la posizione soggettiva con il profilo evolutivo. Non si valuta il bambino: si descrive come è situato in quel campo adesso.'
  },
  {
    sezione: 'C',
    titolo: 'Rapporto con il limite',
    domanda: 'Come il bambino si confronta con i limiti della situazione (fine dello scambio, transizione, no, attesa)?',
    descrizione: `Descrive come il bambino si rapporta alle discontinuità del campo:
                  l'interruzione dello scambio, il ritardo della risposta, la fine
                  dell'attività. Non è un giudizio sulla tolleranza alla frustrazione:
                  è la lettura di come il limite è vissuto nel campo relazionale.`,
    focus: 'La discontinuità: come si affronta, come si riprende, cosa succede nel campo.',
    esempio: window.CASO_GUIDA_F3.f3.outputTipo.C,
    nota: 'Il "limite" in F3 è strutturale, non normativo: non si valuta se il bambino sa "gestire la frustrazione" — si descrive come il limite è presente o assente nel campo osservato.'
  },
  {
    sezione: 'D',
    titolo: 'Configurazione complessiva',
    domanda: 'Come si può descrivere sinteticamente il campo nella sua configurazione d\'insieme?',
    descrizione: `La descrizione sintetica del campo come totalità: quali forze sono attive,
                  qual è la struttura dominante dell'esperienza relazionale,
                  come si colloca rispetto alla direzione evolutiva.
                  È la sezione che integra le tre precedenti in un'immagine complessiva.`,
    focus: 'La sintesi configurazionale — non la lista dei problemi.',
    esempio: window.CASO_GUIDA_F3.f3.outputTipo.D,
    nota: 'La sezione D deve poter essere letta da sola: deve dare un\'immagine del campo comprensibile anche senza le sezioni precedenti. È il "riassunto esecutivo" dell\'output-tipo.'
  },
  {
    sezione: 'E',
    titolo: 'Ipotesi di sostegno',
    domanda: 'Cosa può essere sostenuto? Qual è l\'azione minima che aumenta l\'abitabilità del campo?',
    descrizione: `La proposta operativa che emerge dalla lettura del campo:
                  non una prescrizione, ma un'ipotesi di intervento coerente
                  con la configurazione descritta nelle sezioni A–D.
                  Prende la forma di micro-azioni contestualizzate nel perimetro F3.`,
    focus: 'La proposta minima — funzione + campo bersaglio + micro-azioni essenziali.',
    esempio: window.CASO_GUIDA_F3.f3.outputTipo.E,
    nota: 'La sezione E è un\'ipotesi, non una prescrizione. Deve rimanere coerente con ciò che è stato descritto in A–D: non introduce elementi nuovi che non siano stati osservati nel campo.'
  }
];

// Domande di verifica di coerenza del Template F3
const VERIFICA_COERENZA_DOMANDE = [
  {
    numero: 1,
    id: 'vc1',
    domanda: 'Il campo bersaglio e le micro-azioni hanno come soggetto il campo relazionale, non il bambino isolato?',
    indicatore: 'Le micro-azioni modificano comportamenti adulti o condizioni ambientali — non prescrivono al bambino cosa fare.',
    errore_tipico: '"Il bambino deve imparare a..." · "Stimolare il bambino a..."',
    check_caso: window.CASO_GUIDA_F3.f3.verificaCoerenza[0]
  },
  {
    numero: 2,
    id: 'vc2',
    domanda: 'Il dispositivo è applicabile senza diagnosi clinica?',
    indicatore: 'Il template non fa riferimento a etichette diagnostiche né le richiede per essere applicato. È valido per qualsiasi configurazione relazionale con quei segnali CE.',
    errore_tipico: '"Applicabile a bambini con..." · "In presenza di diagnosi di..."',
    check_caso: window.CASO_GUIDA_F3.f3.verificaCoerenza[1]
  },
  {
    numero: 3,
    id: 'vc3',
    domanda: 'Ogni micro-azione è osservabile nel campo in tempo reale?',
    indicatore: 'Posso vedere mentre accade se l\'azione è in corso e se il campo sta rispondendo. Non richiede strumenti di valutazione differita.',
    errore_tipico: '"Nel lungo periodo si vedrà..." · "Alla fine del percorso..."',
    check_caso: window.CASO_GUIDA_F3.f3.verificaCoerenza[2]
  },
  {
    numero: 4,
    id: 'vc4',
    domanda: 'L\'indicatore di risonanza è leggibile come risposta del campo — non come progresso del bambino?',
    indicatore: 'L\'indicatore descrive la qualità dello scambio relazionale: durata, qualità, struttura dell\'incontro. Non misura competenze.',
    errore_tipico: '"Il bambino sa ora..." · "Ha migliorato la sua capacità di..."',
    check_caso: window.CASO_GUIDA_F3.f3.verificaCoerenza[3]
  },
  {
    numero: 5,
    id: 'vc5',
    domanda: 'Se l\'indicatore di risonanza è assente, il template permette di rivalutare la CE?',
    indicatore: 'Un dispositivo F3 non si insiste: se il campo non risponde, si torna alla CE e si rivaluta la lettura. Il template non presuppone che il campo debba rispondere in un certo modo.',
    errore_tipico: '"Se non funziona, aumentare la frequenza del dispositivo." · "Insistere per almeno X sessioni."',
    check_caso: window.CASO_GUIDA_F3.f3.verificaCoerenza[4]
  }
];

// Template F3 del caso-guida compilato (sintesi per la slide narrativa)
const CASO_GUIDA_M5 = {
  template: {
    ceOrigine: window.CASO_GUIDA_F3.ce.grammaticale,
    nodoDominante: `${window.CASO_GUIDA_F3.f3.nodoDominante.codice} — ${window.CASO_GUIDA_F3.f3.nodoDominante.nome}`,
    funzione: window.CASO_GUIDA_F3.f3.funzione,
    funzioneColore: window.CASO_GUIDA_F3.f3.funzioneColore,
    campoBersaglio: window.CASO_GUIDA_F3.f3.campoBersaglio,
    microAzioni: window.CASO_GUIDA_F3.f3.microAzioni,
    tempoReale: window.CASO_GUIDA_F3.f3.tempoReale,
    indicatoreRisonanza: window.CASO_GUIDA_F3.f3.indicatoreRisonanza
  },
  outputTipo: window.CASO_GUIDA_F3.f3.outputTipo,
  verificaCoerenza: window.CASO_GUIDA_F3.f3.verificaCoerenza
};
```

---

## SLIDE F3.5.1 — Dalla funzione al dispositivo

**Tipo**: `standard`
**Titolo**: La funzione non è ancora il dispositivo
**Sottotitolo**: Cosa manca per passare da "Mediare" a cinque micro-azioni in cinque minuti

**Contenuto principale**:

Layout a colonna singola. Slide di apertura — stabilisce il nodo concettuale del modulo senza anticipare i contenuti tecnici.

**Sezione superiore — il punto di arrivo di M4**:

Box sfondo `--color-primary-light`, bordo sinistro `var(--color-fn-mediare)`:

*Nel Modulo 4 abbiamo scelto la funzione: MEDIAZIONE. Sappiamo cosa deve fare il dispositivo: sostenere la transizione N2→N3, rallentando il ritmo adulto e lasciando spazio alla sequenza del bambino.*

*Non sappiamo ancora come.*

**Sezione centrale — la domanda di M5**:

Testo `--text-2xl`, centrato, `--color-text`, con ampio spazio verticale sopra e sotto:

*"Come si costruisce un dispositivo F3?"*

Sotto, due righe `--text-base`, `--color-text-secondary`, centrate:

*Dall'orientamento funzionale al template.*
*Dal template alle micro-azioni contestualizzate nel campo reale.*

**Sezione inferiore — la struttura del modulo**:

Schema orizzontale a quattro blocchi con frecce tra loro:

```
[Template F3]  →  [Micro-azioni]  →  [Output-tipo]  →  [Verifica di coerenza]
  7 campi          3–5 azioni         5 sezioni         5 domande
```

Ogni blocco è un chip arrotondato con bordo `--color-accent` e sfondo `--color-guardrail-bg` (leggero). La numerazione mostra che si tratta di una sequenza costruttiva, non parallela.

Sotto lo schema, testo `--text-sm`, `--color-text-muted`, centrato:

*Questi quattro strumenti formano insieme il micro-dispositivo di campo. Non sono liste da compilare: sono domande da porre al campo.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-50`
- Label: Il dispositivo nasce dal campo
- Testo: *Il Template F3 non si compila a partire da un manuale di tecniche. Si compila a partire dalla CE. Ogni campo diverso produce un template diverso — anche con la stessa funzione.*

---

## SLIDE F3.5.2 — Il Template F3: i sette campi

**Tipo**: `interactive`
**Titolo**: Sette campi, una struttura
**Sottotitolo**: La grammatica del micro-dispositivo di campo

**Contenuto principale**:

Layout a due colonne: sinistra elenco verticale di 7 tab/chip cliccabili (numerati 1–7), destra pannello con i dettagli del campo selezionato.

I dati vengono da `TEMPLATE_F3_CAMPI`.

**Colonna sinistra** (30%) — lista numerata di campi:

Sette chip verticali cliccabili, numerati, con il `label` del campo. Il chip attivo ha bordo `--color-accent` e sfondo `--color-guardrail-bg`. I campi 1–3 (CE di origine, Nodo dominante, Funzione) hanno un'indicazione visiva sottile: *"← già definito in F2/F3"* — sono campi che arrivano dall'upstream del processo; non li si inventa al momento del template.

**Colonna destra** (70%) — pannello del campo selezionato:

Per ogni campo:
- Numero grande (`--text-4xl`, `--color-text-muted`) in alto a sinistra
- `label` in `--text-xl`, grassetto
- `domanda` in corsivo, `--color-accent`, bordo sinistro `--color-accent`
- `descrizione` in `--text-base`
- Riga **Formato atteso**: `--text-sm`, sfondo `--color-bg`, bordo `--color-border`, `font-mono`
- Box **Esempio caso-guida** (sfondo `--color-primary-light`, bordo `--color-primary`): testo da `esempio`, preceduto da chip `Caso-guida DBS`
- Box **Errore tipico** (sfondo rosso tenuissimo, bordo `--color-invalid`): testo da `errore`, `--text-sm`

**Navigazione**: pulsanti `← Campo precedente` / `Campo successivo →` in basso alla colonna destra. La progressione suggerisce l'ordine di compilazione.

**Nota in footer**:
*I campi 1–3 (CE, nodo dominante, funzione) sono già stati prodotti dai passaggi precedenti di F3. La compilazione del template inizia di fatto dai campi 4–7.*

---

## SLIDE F3.5.3 — Le micro-azioni: cosa le rende valide

**Tipo**: `comparison`
**Titolo**: La grammatica delle micro-azioni
**Sottotitolo**: Tre proprietà, tre test, tre distinzioni

**Contenuto principale**:

Layout misto: sezione superiore con tre blocchi orizzontali (le proprietà), sezione inferiore con `ComparisonPanel` (azione sul bambino vs. azione sul campo).

**Sezione superiore — tre proprietà** (dati da `MICRO_AZIONI_CRITERI`):

Tre blocchi affiancati, bordo superiore spesso `--color-accent`:

Ogni blocco contiene:
- `label` in grassetto `--text-base`
- `descrizione` in `--text-sm`
- Test formattato come domanda in corsivo, sfondo `--color-bg`: `test`
- Due righe compatte: ✓ `esempio_ok` (verde) / ✗ `esempio_no` (rosso tenue)

**Sezione inferiore** — `ComparisonPanel`:

**Colonna sinistra** — "Azione sul bambino" (bordo `--color-invalid`):

Titolo: *"Il bambino come soggetto dell'azione"*

Quattro esempi invalidi:
- *"Guidare il bambino a indicare con il dito"*
- *"Insegnare al bambino a nominare le immagini"*
- *"Stimolare il bambino a vocalizzare"*
- *"Far fare al bambino una sequenza di tre gesti"*

Sotto, corsivo `--color-text-secondary`:
*Queste azioni non sono sbagliate come azioni — ma non sono micro-azioni F3: non modificano il campo, modificano il bambino.*

**Colonna destra** — "Azione sul campo" (bordo `--color-accent`):

Titolo: *"Il campo come soggetto dell'azione"*

Quattro esempi validi (dal caso-guida):
- *"Il genitore segue l'interesse del bambino senza anticiparlo"*
- *"Nomina ciò che il bambino indica, con voce calma e ritmo lento"*
- *"Attende la risposta del bambino senza riempire il silenzio"*
- *"Il pediatra osserva senza interrompere la sequenza bambino-genitore"*

Sotto, corsivo `--color-accent`:
*Ogni azione ha come soggetto l'adulto o il contesto: modifica le condizioni in cui il bambino è presente, non il bambino stesso.*

**Footer** a piena larghezza:

*Il test grammaticale per ogni micro-azione: "il soggetto è un adulto o una condizione ambientale — non il bambino"? Se il bambino è soggetto, l'azione è fuori perimetro F3.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-51`
- Label: Il soggetto delle micro-azioni
- Testo: *Se una micro-azione descrive ciò che deve fare il bambino, non è una micro-azione F3. Il soggetto dell'azione è sempre l'adulto, il setting, le condizioni relazionali.*

---

## SLIDE F3.5.4 — L'output-tipo vuoto: cinque sezioni

**Tipo**: `interactive`
**Titolo**: L'output-tipo: leggere il campo per sostenerlo
**Sottotitolo**: Cinque sezioni, una struttura di lettura condivisa

**Contenuto principale**:

Componente tab orizzontale con cinque sezioni A–E (dati da `OUTPUT_TIPO_STRUTTURA`). Il nome "output-tipo vuoto" indica che la struttura è invariante — il contenuto cambia per ogni campo osservato.

**Intestazione sopra i tab**:

Testo `--text-base`, `--color-text-secondary`:
*L'output-tipo vuoto è una pre-struttura di lettura: non prescrive cosa scrivere, ma orienta l'attenzione verso le dimensioni rilevanti del campo. È condivisibile con altri professionisti perché usa un vocabolario comune.*

**Tab navigation**: cinque tab orizzontali, ognuno con la lettera della sezione in grassetto + il `titolo`. Il tab attivo ha bordo inferiore spesso `--color-accent` e `label` colorato.

**Pannello per ogni sezione** (al clic sul tab):

Layout verticale:
- Lettera grande (`--text-4xl`, `--color-text-muted`) in alto a sinistra, affiancata da `titolo` in `--text-xl` grassetto
- `domanda` in corsivo, sfondo `--color-bg`, bordo sinistro `--color-accent`
- `descrizione` in `--text-base`
- Riga **Cosa descrive**: `focus` in `--text-sm`, bordo `--color-border`
- Box **Esempio — caso-guida DBS** (sfondo `--color-primary-light`): testo da `esempio`, corsivo
- Box **Nota metodologica** (sfondo `--color-guardrail-bg`, bordo `--color-guardrail`): testo da `nota`, `--text-sm`

**Sezione inferiore — relazione tra le sezioni**:

Box sfondo `--color-bg`, bordo `--color-border`, presentato sotto i tab:

*Le cinque sezioni non sono indipendenti:*
*A descrive il campo → B descrive il bambino nel campo → C descrive come il campo si confronta con la discontinuità → D integra A–C in una configurazione complessiva → E propone l'ipotesi di sostegno coerente con D.*

Schema lineare orizzontale: `A → B → C → D → E` con frecce e etichette minime. La freccia tra D ed E è più spessa: E dipende da D più delle altre relazioni.

**Nota in footer**:
*L'output-tipo non è un formulario da consegnare: è uno strumento di lettura condivisa. La sezione E è un'ipotesi — non una prescrizione. Se il campo cambia, l'ipotesi va aggiornata.*

---

## SLIDE F3.5.5 — La verifica di coerenza

**Tipo**: `standard`
**Titolo**: Prima di applicare il dispositivo: cinque domande
**Sottotitolo**: La verifica di coerenza metodologica del Template F3

**Contenuto principale**:

Layout a colonna singola. Cinque domande di verifica come checklist interattiva: ogni domanda ha una casella di spunta visiva (non funzionale come form, ma visiva come elenco strutturato). Dati da `VERIFICA_COERENZA_DOMANDE`.

**Intestazione**:

Testo `--text-base`:
*Prima che un Template F3 sia pronto per essere applicato, cinque domande verificano che il dispositivo sia coerente con il perimetro metodologico di F3.*

*Non sono criteri formali: sono domande di lettura. Un "no" a qualsiasi domanda non invalida il lavoro — indica dove rileggere la CE o riformulare il campo bersaglio.*

**Checklist** (cinque blocchi verticali, bordo sinistro `--color-accent`, sfondo `--color-surface`):

Ogni blocco:
```
┌─────────────────────────────────────────────────────────────────┐
│  [✓ in --color-valid]  [numero]  [domanda in --text-base grassetto]
│
│  Indicatore: [indicatore in --text-sm, --color-text-secondary]
│
│  Errore tipico: [errore_tipico in --text-sm, --color-invalid, corsivo]
│
│  [chip piccolo: ✓ Nel caso-guida] [nota breve dal check_caso.nota]
└─────────────────────────────────────────────────────────────────┘
```

I chip `✓ Nel caso-guida` usano `check_caso.ok` (tutti `true` nel caso-guida): colore `--color-valid` quando `true`, `--color-invalid` quando `false`. La nota del chip viene da `check_caso.nota`.

**Sezione inferiore — il principio che unifica**:

Blockquote centrato, bordo sinistro `--color-guardrail`:

> *"Un dispositivo F3 è coerente quando non parla del bambino ma del campo;
> quando non prescrive ma propone; quando, se il campo non risponde,
> permette di rivalutare invece di insistere."*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-52`
- Label: Indicatore di risonanza assente → rivalutare, non insistere
- Testo: *Se il campo non risponde al dispositivo, il passo corretto è tornare alla CE e rivalutare la lettura — non aumentare l'intensità o la frequenza dello stesso dispositivo. Il dispositivo F3 è un'ipotesi di campo, non un protocollo.*

---

## SLIDE F3.5.6 — Il caso-guida: template compilato

**Tipo**: `narrative`
**Titolo**: Il Template F3 del caso-guida: dalla CE al dispositivo
**Sottotitolo**: Dialogic Book Sharing durante il bilancio pediatrico — micro-dispositivo MEDIAZIONE

**Contenuto principale**:

Layout a due colonne: sinistra il Template F3 compilato (7 campi), destra l'output-tipo compilato (5 sezioni A–E). Sotto, a piena larghezza, la verifica di coerenza sintetica.

Tutti i dati da `CASO_GUIDA_M5`.

**Colonna sinistra** (48%) — "Template F3 compilato":

Titolo colonna: *"Template F3"* con chip `MED` colore `var(--color-fn-mediare)`.

Sette righe verticali, ognuna con:
- Numero piccolo `--color-text-muted`
- Label in `--text-sm` grassetto
- Valore in `--text-sm`, sfondo `--color-bg`, padding `--space-2`

Campo 5 (micro-azioni): lista ordinata 1–5, ogni voce `--text-sm`.

**Colonna destra** (52%) — "Output-tipo compilato":

Titolo colonna: *"Output-tipo"* con chip `A B C D E` colorati `--color-accent`.

Cinque blocchi verticali con label lettera + contenuto in `--text-sm`. Le sezioni sono compatte: testo non troncato, ma layout denso. Il blocco E ha bordo sinistro più spesso `--color-accent` a indicare che è l'ipotesi operativa.

**Sezione inferiore a piena larghezza** — "Verifica di coerenza":

Cinque chip orizzontali affiancati, ognuno con:
- ✓ colore `--color-valid`
- Numero + sintesi brevissima del check (da `check_caso.nota`, max 6 parole)

Sotto i chip, in `--text-sm` `--color-text-muted` centrato:
*Tutte e cinque le domande di verifica ricevono risposta affermativa. Il dispositivo è pronto per essere applicato.*

**Sezione conclusiva**:

Box sfondo `--color-primary-light`, bordo `--color-primary`:

*Questo template è il prodotto della pipeline F3 applicata al caso-guida: partendo dalla CE prodotta in F2, identificando N3 come nodo dominante, scegliendo MEDIAZIONE come funzione, costruendo cinque micro-azioni osservabili nel bilancio pediatrico.*

*Il dispositivo non prescrive: orienta. Il pediatra e il genitore rimangono i protagonisti della scena.*

**Nota in footer**:
*Nel Modulo 6 vedremo come lo stesso template si ricollega alla Tipologia Universale: le micro-azioni del caso-guida esprimono U2 (Sintonizzazione) e U4 (Mediazione Simbolica).*

---

## SLIDE F3.5.7 — F3Builder: costruisci il tuo dispositivo

**Tipo**: `interactive`
**Titolo**: Il tuo Template F3
**Sottotitolo**: Costruisci passo per passo un micro-dispositivo di campo

**Contenuto principale**:

Componente `F3Builder(container)` come descritto in `ISTRUZIONI_CLAUDE_CODE_F3.md` §6.5. Questa slide occupa tutta l'area slide disponibile con il builder.

**Intestazione sopra il builder** (rimane visibile durante tutti i 7 step):

Barra compatta con:
- A sinistra: step indicator `[● ○ ○ ○ ○ ○ ○]` che si aggiorna al passo corrente
- A destra: pulsante `↺ Ripristina caso-guida` (grigio tenue, non prominente)

**Struttura dei 7 step** (implementata nel componente, descritta qui per il contenuto):

**Step 1 — CE di origine**:
Area di testo pre-compilata con `window.CASO_GUIDA_F3.ce.grammaticale`. Etichetta: *"Descrivi la CE di partenza in una frase:"*. Testo di aiuto sotto: *"Non è una lista di nodi: è la lettura del campo come configurazione relazionale."*

**Step 2 — Nodo dominante**:
Campo testo pre-compilato con `"N3 — Accesso al mondo condiviso simbolico"`. Etichetta: *"Quale nodo, se attivato, muove il campo nella direzione evolutiva?"*. Testo di aiuto: *"Ricorda: non è necessariamente il nodo più basso. È quello la cui attivazione fa la differenza."*

**Step 3 — Funzione**:
Quattro card selezionabili visivamente, ognuna con badge colorato `--color-fn-X`, nome funzione, e la `azione_sul_campo` da `QUATTRO_FUNZIONI`. La card MEDIAZIONE è pre-selezionata. Etichetta: *"Cosa deve fare il dispositivo sul campo?"*

**Step 4 — Campo bersaglio**:
Campo testo pre-compilato con `window.CASO_GUIDA_F3.f3.campoBersaglio`. Etichetta: *"Quale condizione relazionale deve cambiare?"*. Testo di aiuto: *"Il soggetto è il campo — non il bambino. Es.: 'Stabilità dello scambio condiviso' → sì. 'Il bambino condivide di più' → no."*

**Step 5 — Micro-azioni**:
Lista dinamica pre-compilata con `window.CASO_GUIDA_F3.f3.microAzioni` (5 voci). Pulsante `+ Aggiungi azione` (attivo fino a max 5), `✕` per rimuovere ogni voce (attivo fino a min 3). Etichetta: *"Quali azioni concrete modificano il campo? (3–5)"*. Testo di aiuto: *"Ogni azione ha come soggetto un adulto o una condizione — non il bambino."*

**Step 6 — Tempo reale**:
Campo testo pre-compilato con `window.CASO_GUIDA_F3.f3.tempoReale`. Etichetta: *"In quanto tempo il dispositivo si realizza nel contesto reale?"*. Testo di aiuto: *"Non il tempo ideale: il tempo che il contesto effettivamente permette."*

**Step 7 — Indicatore di risonanza**:
Area di testo pre-compilata con `window.CASO_GUIDA_F3.f3.indicatoreRisonanza`. Etichetta: *"Come si riconosce che il campo ha risposto?"*. Testo di aiuto: *"Non un progresso del bambino: una qualità dello scambio relazionale osservabile in tempo reale."*

**Dopo il completamento di tutti e 7 gli step**:

Area risultato con transizione `slide-down` (200ms):

Titolo: *"Descrizione naturale del dispositivo"*

Testo generato dalla funzione template string del componente (compone i 7 campi in un paragrafo descrittivo):

*"In questa configurazione — [ceOrigine] — l'azione si orienta verso [nodoDominante], con funzione [funzione]. Il campo bersaglio è: [campoBersaglio]. Le micro-azioni contestualizzate sono: [microAzioni come lista]. Il dispositivo si realizza in [tempoReale]. Il campo ha risposto quando: [indicatoreRisonanza]."*

Pulsante `Copia descrizione` (copia il testo negli appunti).

**Nota in footer**:
*Il builder è pre-compilato con i dati del caso-guida. Puoi modificare ogni campo per sperimentare configurazioni diverse — il pulsante "Ripristina caso-guida" riporta ai valori originali.*

---

## SLIDE F3.5.8 — Il dispositivo come ipotesi di campo

**Tipo**: `standard`
**Titolo**: Non una soluzione: un'ipotesi
**Sottotitolo**: Cosa resta aperto dopo aver costruito il dispositivo

**Contenuto principale**:

Layout a colonna singola. Slide di chiusura concettuale — ariosa, poche parole, molto respiro visivo.

**Sezione superiore — la distinzione fondamentale**:

Due box affiancati, dimensione uguale, sfondo `--color-bg`, bordo `--color-border`:

**Box sinistra** — "Il protocollo":
*Prescrive una sequenza di azioni da seguire.*
*Ha una logica interna indipendente dal campo specifico.*
*Se il campo non risponde, si insiste o si aumenta la dose.*
*Valuta il bambino alla fine del percorso.*

**Box destra** — "Il micro-dispositivo F3":
*Propone un'ipotesi di intervento coerente con questa CE.*
*Nasce dal campo specifico e per quel campo.*
*Se il campo non risponde, si rivaluta la CE — non si insiste.*
*Aggiorna la lettura del campo dopo ogni azione.*

Sotto i due box, testo centrato `--text-sm` `--color-text-muted`:
*Questa differenza non è terminologica: è strutturale. Un dispositivo F3 che si comporta come un protocollo ha perso il suo principio costitutivo.*

**Sezione centrale — il ciclo dell'ipotesi**:

Schema circolare semplice (non `DecisionCycle` — quello è per M7): tre nodi in sequenza circolare con frecce:

```
[Osserva il campo]  →  [Applica il dispositivo]  →  [Rileva la risposta]
        ↑                                                      │
        └──────────────── [Aggiorna la CE] ────────────────────┘
```

I quattro nodi sono chip con testo centrato. Le frecce sono frecce CSS semplici. Il nodo `[Aggiorna la CE]` ha bordo `--color-f2` (torna alla F2): il ciclo porta alla CE aggiornata, non a un punto fisso di arrivo.

Sotto lo schema, testo `--text-sm` `--color-text-muted` centrato:
*Il dispositivo non chiude il processo: lo rilancia. Ogni applicazione produce nuova osservabilità. La CE dopo il dispositivo è diversa dalla CE prima.*

**Sezione inferiore — la prospettiva verso M6**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

*Abbiamo costruito il template. Abbiamo compilato l'output-tipo. Abbiamo verificato la coerenza.*

*Il dispositivo del caso-guida si può descrivere in modo diverso: non solo come MEDIAZIONE per N3, ma come espressione di due forme universali di sostegno del campo — U2 (Sintonizzazione) e U4 (Mediazione Simbolica).*

*Nel Modulo 6 vedremo la Tipologia Universale: sei forme che ritornano in qualsiasi campo, con qualsiasi funzione, in qualsiasi contesto professionale.*

Badge modulo successivo: `→ Modulo 6 — La tipologia U1–U6`

---

## Note per l'implementazione

### Slide F3.5.2 — Navigazione tra i campi

I sette chip cliccabili nella colonna sinistra e i pulsanti di navigazione nel pannello destro condividono lo stesso stato `currentField` (indice 0–6). Al cambio di campo, il pannello destro aggiorna il contenuto con una transizione fade (100ms opacity). Al primo caricamento della slide, il campo 1 (CE di origine) è selezionato — anche se concettualmente è già noto, questo posiziona il participante all'inizio della sequenza.

### Slide F3.5.4 — Tab per l'output-tipo

I cinque tab A–E usano lo stesso pattern dei chip dell'indice rapido in M4: cliccando su un tab si aggiorna il pannello centrale. Il tab attivo ha background `--color-guardrail-bg` e bordo inferiore `3px solid var(--color-accent)`. La transizione tra pannelli è fade (100ms). Al caricamento della slide, la sezione A è aperta di default.

### Slide F3.5.5 — Checklist visiva

La checklist non è un form funzionale: le cinque voci hanno il check `✓` pre-impostato (case del caso-guida: tutti true). In un uso reale del builder, la verifica potrebbe essere integrata nell'ultimo step del F3Builder — ma questa slide la presenta come concetto separato, non come tab del builder. Mantenere la distinzione.

### Slide F3.5.6 — Layout bicolonna denso

La slide del template compilato è intenzionalmente densa: mostra tutto in una pagina. Usare `--text-sm` per il contenuto (non `--text-base`), padding ridotto (`--space-2`) nei blocchi. Il font-size per i valori del template è `0.825rem` — leggermente sotto `--text-sm` — per adattarsi alla densità. Se la slide supera l'altezza disponibile, rendere la colonna sinistra e la destra scorrevoli indipendentemente (overflow-y: auto).

### Slide F3.5.7 — F3Builder: gestione stato

Il builder usa un oggetto stato locale `templateState` (non `window`). Al click su `↺ Ripristina caso-guida`, `templateState` viene reimpostato su `DEFAULT_TEMPLATE` (definito in `ISTRUZIONI_CLAUDE_CODE_F3.md` §6.5) e tutti i campi si aggiornano senza ricaricare la slide. La descrizione in linguaggio naturale viene generata dalla funzione:

```javascript
function generaDescrizioneNaturale(state) {
  const microAzioniTesto = state.microAzioni
    .map((a, i) => `${i + 1}. ${a}`)
    .join('\n');
  return `In questa configurazione — ${state.ceOrigine} — ` +
    `l'azione si orienta verso ${state.nodoDominante}, ` +
    `con funzione ${state.funzione.toUpperCase()}. ` +
    `Il campo bersaglio è: ${state.campoBersaglio}. ` +
    `Le micro-azioni contestualizzate sono:\n${microAzioniTesto}\n` +
    `Il dispositivo si realizza in ${state.tempoReale}. ` +
    `Il campo ha risposto quando: ${state.indicatoreRisonanza}.`;
}
```

### Colori accent

L'accent di M5 è `#2d6a4f` — lo stesso usato per `--color-guardrail`. Questo è intenzionale: M5 è il modulo della coerenza metodologica e il verde guardrail è il suo colore semantico. Nelle slide che mostrano la verifica di coerenza, il verde è dominante; nelle slide che mostrano il template e il builder, il verde si accoppia con il viola `--color-fn-mediare` del caso-guida.
