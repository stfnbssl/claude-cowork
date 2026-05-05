# f3-modulo-03 — Il nodo dominante
**Numero slide**: 6
**Colore accent**: `#e67e22`
**Tipo prevalente**: standard + interactive

---

## Dati globali del modulo

Definire in `m03.js` le seguenti costanti. Sono la sorgente di dati per tutte le slide del modulo.

```javascript
const TRE_CATEGORIE_NODI = [
  {
    id: 'sostenuto',
    stato: '↑',
    colore: 'var(--color-valid)',
    nome: 'Nodo sostenuto',
    ruolo_f2: 'Il campo regge bene su questa dimensione.',
    ruolo_f3: `Risorsa disponibile. Non è il punto di lavoro:
               è il terreno su cui si costruisce il dispositivo.
               Lavorare su un nodo sostenuto è spreco di energia
               e può destabilizzare ciò che già funziona.`,
    domanda: 'Come posso usare questa risorsa per sostenere il nodo dominante?',
    esempio_caso: `N2↑ nel caso-guida: il campo relazionale è solido.
                   Non si lavora su N2 — si usa N2 come leva per aprire N3.`
  },
  {
    id: 'neutro',
    stato: '~',
    colore: 'var(--color-warning)',
    nome: 'Nodo neutro',
    ruolo_f2: 'Il campo non è né rinforzato né limitato su questa dimensione.',
    ruolo_f3: `Zona di possibile movimento. È il candidato principale
               per il nodo dominante: ha lo spazio per muoversi
               e non è già in tensione. Con un intervento lieve,
               può passare da ~ a una configurazione più aperta.`,
    domanda: 'Questo nodo neutro può muoversi? Ci sono risorse che lo sostengono?',
    esempio_caso: `N3~ nel caso-guida: l'accesso al mondo condiviso è presente
                   ma discontinuo. C'è spazio di movimento — e N2↑ come risorsa.`
  },
  {
    id: 'limitante',
    stato: '↓',
    colore: 'var(--color-invalid)',
    nome: 'Nodo limitante',
    ruolo_f2: 'Il campo è in tensione su questa dimensione.',
    ruolo_f3: `Tensione da rispettare. Non è automaticamente il punto di lavoro.
               Va considerata per non esacerbarla: il dispositivo
               non deve aumentare il carico su un nodo già in difficoltà.
               In certi casi può essere il nodo dominante — ma solo se
               soddisfa anche gli altri criteri.`,
    domanda: 'Il dispositivo che costruisco aggrava questa tensione?',
    esempio_caso: `N4↓ nel caso-guida: l'esplorazione è ridotta.
                   Non è il punto di lavoro: è un vincolo. Il dispositivo
                   non deve aumentare il carico percettivo del campo.`
  }
];

const CRITERI_NODO_DOMINANTE = [
  {
    id: 'c1',
    numero: '①',
    colore: 'var(--color-n2)',
    criterio: 'Il campo si sta già muovendo verso di lui',
    spiegazione: `La relazione dominante (R) nella CE indica il verso
                  dell'energia del campo: quale nodo sostiene quale altro.
                  Se R punta verso un nodo ~, quel nodo è il candidato
                  privilegiato: il campo ha già iniziato la transizione.`,
    segnale: 'R: Nodo↑ → questo nodo',
    caso_guida: `R: N2→N3. Il campo si sta già muovendo verso N3.
                 La risorsa (N2↑) sta "spingendo" nella direzione giusta.
                 Il dispositivo non deve creare il movimento: deve sostenerlo.`
  },
  {
    id: 'c2',
    numero: '②',
    colore: 'var(--color-n3)',
    criterio: 'Una risorsa attiva può sostenerlo',
    spiegazione: `Il nodo dominante funziona come punto di lavoro
                  solo se c'è almeno un nodo ↑ disponibile che può
                  sostenerne l'attivazione. Un nodo ~ senza risorse
                  di sostegno richiede un intervento più pesante —
                  fuori dal perimetro del micro-dispositivo.`,
    segnale: 'Esiste almeno un nodo ↑ collegato tramite R',
    caso_guida: `N2↑ è la risorsa che sostiene N3~.
                 Il campo relazionale attivo è la condizione che rende
                 possibile l'accesso al mondo condiviso.
                 Senza N2↑, N3 non avrebbe terreno su cui muoversi.`
  },
  {
    id: 'c3',
    numero: '③',
    colore: 'var(--color-f3)',
    criterio: 'La sua attivazione è coerente con la direzione D',
    spiegazione: `La direzione evolutiva (D) indica dove il campo
                  si sta muovendo. Il nodo dominante deve essere
                  coerente con quella direzione: la sua attivazione
                  deve accompagnare o accelerare il movimento,
                  non contradirlo.`,
    segnale: 'D punta nella direzione in cui questo nodo può aprirsi',
    caso_guida: `D↗ (espansione in corso). N3 in espansione è coerente con D↗.
                 Lavorare su N4↓ (che è in contrazione) contrasterebbe
                 la direzione evolutiva: si spingerebbe in senso opposto
                 a dove il campo si sta muovendo.`
  },
  {
    id: 'c4',
    numero: '④',
    colore: 'var(--color-n5)',
    criterio: 'La sua attivazione non esacerba i nodi in tensione',
    spiegazione: `Il dispositivo che attiva il nodo dominante
                  non deve aumentare il carico su nodi già limitanti (↓).
                  Se l'attivazione del candidato produce sovraccarico
                  su un nodo ↓, quel candidato va riconsiderato.
                  Principio: non aggiungere tensione dove c'è già tensione.`,
    segnale: 'Nessun nodo ↓ risulta ulteriormente compromesso',
    caso_guida: `Attivare N3 (aumentando la stabilità dello scambio condiviso)
                 non esacerba N4↓. Uno scambio più stabile e guidato
                 riduce il carico percettivo dell'ambiente — e questo
                 favorisce marginalmente, non ostacola, l'esplorazione.`
  }
];

const ERRORI_IDENTIFICAZIONE = [
  {
    id: 'e1',
    titolo: 'Il nodo dominante è il nodo ↓ più basso',
    esempio_errato: `"N4↓ è il nodo con lo stato più basso.
                     Quindi lavoro su N4."`,
    problema: `Il nodo ↓ indica una tensione nel campo — non il luogo
               in cui il campo può muoversi con un intervento leggero.
               N4↓ dice: l'esplorazione è sotto pressione. Non dice:
               è qui che devi intervenire.`,
    conseguenza: `Un dispositivo centrato su N4 (es. introdurre
                  nuovi stimoli esplorativi) aumenterebbe il carico
                  su un campo già fragile (T2). Risultato probabile:
                  disorganizzazione, non apertura.`,
    corretto: `N3~ con R: N2→N3 soddisfa tutti e quattro i criteri.
               N4↓ è un vincolo da rispettare — non il punto di lavoro.`
  },
  {
    id: 'e2',
    titolo: 'Il nodo dominante si sceglie dal sintomo',
    esempio_errato: `"Il bambino non parla ancora abbastanza.
                     Lavoro su N3 perché c'è un problema linguistico."`,
    problema: `Il nodo dominante non si sceglie dal sintomo osservato:
               emerge dalla lettura della CE. Il risultato può coincidere —
               ma il percorso è diverso, e la coincidenza non è garantita.
               Partire dal sintomo bypassa la lettura configurazionale.`,
    conseguenza: `Se il ritardo linguistico fosse prodotto da N1↓
                  (regolazione fragile che impedisce l'accesso allo scambio)
                  anziché da N3~, un dispositivo centrato su N3
                  sarebbe fuori bersaglio: lavora sull'effetto, non sulla causa.`,
    corretto: `La CE prima. Sempre. Il nodo dominante emerge
               dalla struttura configurazionale — non dall'osservazione del sintomo.`
  },
  {
    id: 'e3',
    titolo: 'Si lavora su più nodi contemporaneamente',
    esempio_errato: `"Ho tre nodi da migliorare: N3, N4 e N1.
                     Creo un dispositivo che li lavora tutti."`,
    problema: `Un micro-dispositivo che cerca di attivare più nodi
               contemporaneamente perde precisione, diventa incoerente
               e smette di soddisfare le tre proprietà: non è più breve,
               non è più reversibile, non produce un indicatore
               di risonanza osservabile e distinto.`,
    conseguenza: `Multi-nodo → programma d'intervento.
                  Non è un micro-dispositivo di campo: è un piano terapeutico.
                  Fuori dal perimetro metodologico di F3.`,
    corretto: `Un nodo dominante. Una funzione. Un dispositivo. Una rivalutazione.
               Se serve un secondo ciclo, si rivaluta la CE e si sceglie il prossimo.`
  }
];

const ANALISI_CASO_GUIDA_M3 = {
  ce_display: {
    // Da richiamare con CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N3', 'N2', 'N4'] })
    highlights: ['N3', 'N2', 'N4'],
    note: {
      N2: 'Risorsa di sostegno (↑)',
      N3: 'Nodo dominante candidato (~)',
      N4: 'Tensione da rispettare (↓)'
    }
  },
  passi: [
    {
      criterio: '① Il campo si sta muovendo verso quale nodo?',
      risposta: `R: N2→N3. L'energia del campo si muove già verso N3.
                 Non verso N4, non verso N1. Verso N3.`,
      esito: 'N3 candidato: ✓'
    },
    {
      criterio: '② C\'è una risorsa che può sostenerlo?',
      risposta: `N2↑ è la risorsa di sostegno. È N2 che R indica
                 come nodo sostenente per N3. Il campo relazionale
                 attivo è la condizione per l'accesso al simbolico.`,
      esito: 'N3 candidato: ✓'
    },
    {
      criterio: '③ La sua attivazione è coerente con D?',
      risposta: `D↗: il campo è in espansione. Attivare N3
                 (accesso al mondo condiviso) è espansione.
                 Lavorare su N4↓ (che è in contrazione) contraddirebbe D↗.`,
      esito: 'N3 candidato: ✓ — N4 escluso'
    },
    {
      criterio: '④ La sua attivazione esacerba N4↓?',
      risposta: `Un dispositivo che aumenta la stabilità dello scambio
                 condiviso non aumenta il carico esplorativo del campo.
                 Anzi: uno scambio guidato e contenuto riduce la dispersione.`,
      esito: 'N3 candidato: ✓'
    },
    {
      criterio: 'Conclusione',
      risposta: `N3 soddisfa tutti e quattro i criteri.
                 N4↓ non soddisfa ③ (contraddice D↗) né ④ (rischio di esacerbazione).
                 N3 è il nodo dominante.`,
      esito: 'N3 — Nodo dominante confermato'
    }
  ]
};
```

---

## SLIDE F3.3.1 — Una distinzione anti-intuitiva

**Tipo**: `standard`
**Titolo**: Il nodo su cui intervenire non è il nodo più critico
**Sottotitolo**: La distinzione che cambia tutto

**Contenuto principale**:

Layout a due colonne. La slide entra subito nel paradosso — senza preamboli.

**Colonna sinistra** (45%) — "Il ragionamento naturale" (card sfondo `--color-bg`, bordo `--color-border`):

**Il ragionamento naturale**

Il professionista guarda la CE. Vede uno stato così:

```
N1 ~   N2 ↑   N3 ~
N4 ↓   N5 ~   N6 ~   N7 ~
```

La conclusione spontanea:

> *"N4 è il nodo più basso. Il problema è lì. Intervengo su N4."*

Questo ragionamento è intuitivo, lineare, familiare. È il ragionamento della diagnostica: si individua il deficit, si interviene sul deficit.

**Colonna destra** (55%) — "Il ragionamento F3" (card sfondo `--color-primary-light`, bordo sinistro `--color-f3`):

**Il ragionamento F3**

Il nodo dominante non è necessariamente il nodo con lo stato più basso.

È il nodo la cui **attivazione produce il cambiamento più rilevante** per l'abitabilità del campo nella direzione evolutiva indicata (D).

In questa CE, il nodo dominante è **N3** — non N4.

Perché? Quattro criteri lo determinano:
- Il campo si sta già muovendo verso N3 (R: N2→N3)
- C'è una risorsa attiva che può sostenerlo (N2↑)
- La sua attivazione è coerente con D↗
- Non esacerba N4↓

N4↓ è una tensione da rispettare, non il punto di lavoro.

**Elemento visivo sotto le colonne** — freccia bidirezionale con domanda:

```
[Nodo più basso]  ≠  [Nodo dominante]
```

Testo centrato sotto: *"Questa distinzione è il cuore del Modulo 3."*

**Nota in footer**:
*Confondere il nodo più basso con il nodo dominante è l'errore più frequente nell'applicazione di F3. Questo modulo costruisce i criteri per evitarlo.*

---

## SLIDE F3.3.2 — Tre categorie di nodi in F3

**Tipo**: `interactive`
**Titolo**: Cosa legge F3 nella CE
**Sottotitolo**: Tre ruoli, non tre stati

**Contenuto principale**:

Layout a due aree: sinistra la CE del caso-guida, destra le tre categorie espandibili.

**Area sinistra** (40%) — visualizzazione CE:

Titolo `--text-sm`, `--color-text-muted`: *"CE del caso-guida"*

Componente `CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N2', 'N3', 'N4'] })` — versione standard, con le tre righe N2, N3, N4 evidenziate (sfondo tenue nel colore del nodo, bordo sinistro).

Sotto la tabella, in `--text-sm` centrato: *"La stessa CE. Ma F3 non vede stati: vede ruoli."*

**Area destra** (60%) — tre card espandibili (componente `ExpandableCards`, `multiOpen: true`), una per categoria, con i dati da `TRE_CATEGORIE_NODI`:

**Card fronte** (stato compatto):
```
[Chip stato: ↑ verde / ~ arancione / ↓ rosso]  [Nome categoria]
[ruolo_f3 — prima frase]
[Domanda in corsivo, sfondo tenue]              [↓ Espandi]
```

**Card espansa** (aggiunge tre sezioni):
- `ruolo_f2` in `--text-sm`, `--color-text-secondary`, con etichetta *"In F2:"*
- `ruolo_f3` completo, testo normale
- Box tenue (`--color-bg`) con etichetta *"Nel caso-guida:"* e testo `esempio_caso`

**Elemento visivo importante** — sopra le tre card, intestazione in `--text-sm` corsivo:
*"Stessa notazione (↑ ↓ ~). Lettura diversa."*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-30`
- Label: Inversione del ruolo
- Testo: *Un nodo ↓ letto come "punto di lavoro" anziché come "tensione da rispettare" è l'inversione più comune. Un nodo ↑ lavorato come se fosse fragile spreca la risorsa disponibile.*

---

## SLIDE F3.3.3 — Quattro criteri per identificare il nodo dominante

**Tipo**: `interactive`
**Titolo**: Come si identifica il nodo dominante
**Sottotitolo**: Quattro criteri da soddisfare tutti

**Contenuto principale**:

Layout a colonna singola. Quattro blocchi step-by-step verticali, numerati, con i dati da `CRITERI_NODO_DOMINANTE`.

**Struttura di ogni blocco** (non card espandibili — tutti visibili):

```
[Numero grande in --color-accent]  [criterio in --text-lg grassetto]
[spiegazione in testo normale]
[Segnale visivo: chip con testo "segnale" in --text-sm]
[Box tenue con etichetta "Nel caso-guida:" e testo caso_guida]
```

I quattro blocchi sono separati da un divisore sottile (`--color-border`). L'ultimo blocco (④) ha un bordo inferiore leggermente più spesso per segnalare la fine della sequenza.

**Elemento visivo aggiuntivo** — tra ③ e ④, una nota in `--text-sm`, `--color-text-muted`, corsivo, centrata:

*I criteri non sono una checklist da compilare in ordine: sono condizioni simultanee. Un nodo che soddisfa ① e ② ma viola ③ o ④ non è il nodo dominante.*

**Sezione inferiore — la regola sintetica** (box sfondo `--color-primary-light`, bordo `--color-f3`):

**Il nodo dominante è:**
Il nodo ~ verso cui il campo si sta già muovendo (R), sostenuto da una risorsa disponibile (↑), coerente con la direzione evolutiva (D), la cui attivazione non esacerba le tensioni esistenti (↓).

**Non è:**
- Il nodo con lo stato più basso
- Il nodo scelto dal sintomo osservato
- Il nodo che il professionista vuole migliorare

**Nota in footer**:
*Nella maggior parte delle CE ben formate, il nodo dominante è un nodo ~. Se tutti i nodi ~ soddisfano i criteri, scegliere quello indicato da R. Se nessun nodo ~ li soddisfa, è possibile che la CE necessiti di rivalutazione.*

---

## SLIDE F3.3.4 — Tre errori nell'identificazione

**Tipo**: `interactive`
**Titolo**: Gli errori più frequenti
**Sottotitolo**: Cosa succede quando l'identificazione va storta

**Contenuto principale**:

Tre card espandibili verticali (componente `ExpandableCards`, `multiOpen: false` — una alla volta) con i dati da `ERRORI_IDENTIFICAZIONE`.

**Card fronte** (stato compatto):
```
[Numero grande in --color-invalid]  [titolo in --text-lg]
[esempio_errato in corsivo, virgolettato, --color-text-secondary]
[↓ Espandi per vedere conseguenze e correzione]
```

**Card espansa** (aggiunge tre sezioni con label distinte):

Sezione 1 — *"Problema:"* (testo `problema`, bordo sinistro `--color-warning`)

Sezione 2 — *"Conseguenza:"* (testo `conseguenza`, sfondo rosso tenuissimo, `--color-invalid` testo)

Sezione 3 — *"Lettura corretta:"* (testo `corretto`, sfondo verde tenuissimo, `--color-valid` testo, con chip `✓`)

**Nota di tono** — tra le card e il guardrail, in `--text-sm`, `--color-text-muted`, corsivo, centrato:

*Questi errori non indicano incompetenza professionale: riflettono abitudini di pensiero consolidate (deficit-based, multitasking, pattern-matching rapido) che il metodo chiede di sospendere temporaneamente per costruire la lettura configurazionale.*

**Guardrail** (`GuardrailBadge`):
- Codice: `C-F3-31`
- Label: Il ciclo che si chiude
- Testo: *Se il dispositivo F3 costruito non produce l'indicatore di risonanza atteso, la prima domanda non è "il dispositivo era sbagliato?" ma "il nodo dominante era corretto?". L'errore di identificazione si manifesta sempre come assenza di risonanza.*

---

## SLIDE F3.3.5 — Il caso-guida: perché N3 e non N4

**Tipo**: `interactive`
**Titolo**: Applicare i quattro criteri
**Sottotitolo**: La scelta del nodo dominante nel caso-guida — passo per passo

**Contenuto principale**:

Layout a due aree: sinistra CE visualizzata, destra i passi dell'analisi.

**Area sinistra** (38%) — CE con highlights:

`CEDisplay(window.CASO_GUIDA_F3.ce, container, { highlights: ['N2', 'N3', 'N4'] })`

Sotto la CE, tre chip colorati fissi (non interattivi) che etichettano i tre nodi rilevanti:
- Chip `N2↑` colore `var(--color-n2)` con etichetta: *"Risorsa"*
- Chip `N3~` colore `var(--color-n3)` con etichetta: *"Candidato dominante"*
- Chip `N4↓` colore `var(--color-n4)` con etichetta: *"Tensione"*

**Area destra** (62%) — analisi step-by-step con i dati da `ANALISI_CASO_GUIDA_M3.passi`:

Titolo `--text-sm`, `--color-text-muted`: *"Quattro criteri applicati"*

Cinque blocchi verticali (i quattro criteri + la conclusione), ognuno con:

```
[Chip numerato: ①②③④ o "✓"] [criterio in --text-sm grassetto]
[risposta in testo normale --text-base]
[Chip esito: verde "N3 candidato: ✓" o rosso "N4 escluso"]
```

I blocchi ①②③④ mostrano il campo `criterio` e il campo `risposta`. Il blocco conclusione ha uno sfondo tenue (`--color-primary-light`) e il chip esito in `--text-lg`, grassetto: *"N3 — Nodo dominante confermato"*.

**Comportamento interattivo**: i cinque blocchi appaiono in sequenza con un click su "→ Passo successivo" (pulsante piccolo, discreto, in basso a destra dell'area destra). All'entrata nella slide, solo il titolo dell'area destra e il pulsante sono visibili. I blocchi appaiono uno alla volta (animazione slide-down, 200ms).

Un pulsante alternativo "Mostra tutto" fa comparire tutti i blocchi contemporaneamente senza animazione.

**Nota in footer**:
*In contesto reale, questa analisi non viene eseguita per iscritto: il professionista la interiorizza come habitus di lettura. Il corso la rende esplicita per permettere di costruirla consapevolmente.*

---

## SLIDE F3.3.6 — Il nodo dominante come apertura

**Tipo**: `standard`
**Titolo**: Non un problema da risolvere. Un'apertura da sostenere.
**Sottotitolo**: Una riformulazione che cambia il dispositivo

**Contenuto principale**:

Layout a colonna singola. Slide concettualmente densa ma visivamente ariosa.

**Sezione superiore — la riformulazione centrale**:

Due blockquote affiancati:

**Blockquote sinistro** (bordo `--color-invalid`, sfondo rosso tenuissimo):
> *"N3 è il nodo su cui c'è un problema. Lo devo migliorare."*

**Freccia → tra i due blockquote**

**Blockquote destro** (bordo `--color-f3`, sfondo `--color-primary-light`):
> *"N3 è l'apertura attraverso cui il campo può muoversi. La sostengo."*

Sotto i due blockquote, in `--text-base`, centrato:
*La differenza non è semantica. Cambia il dispositivo.*

**Sezione centrale — perché la riformulazione cambia il dispositivo**:

Due colonne:

**Colonna sinistra** — "Se N3 è un problema":
- L'obiettivo del dispositivo è far migliorare N3
- Si misura il successo su N3 ("ora il bambino indica di più?")
- Il dispositivo tende a lavorare direttamente su N3 (stimolazione)
- Si perde di vista il campo (N2 come risorsa, N4 come vincolo)

**Colonna destra** — "Se N3 è un'apertura":
- L'obiettivo è sostenere le condizioni in cui N3 si muove
- Si misura il successo sul campo ("lo scambio si allunga? l'adulto risponde meglio?")
- Il dispositivo agisce su N2 (risorsa) e sul contesto (ritmo, modalità)
- N4 viene rispettato: non si aggiunge carico

**Sezione inferiore — sintesi operativa**:

Box sfondo `--color-primary-light`, bordo `--color-f3`:

Il nodo dominante indica:
- **Dove** il campo ha uno spazio di movimento
- **Verso cosa** il dispositivo orienta l'energia disponibile
- **Quali risorse** il dispositivo può usare
- **Quali tensioni** il dispositivo deve rispettare

Non indica: *cosa il bambino deve imparare* né *cosa manca al campo*.

**Chiusura** — testo centrato, spazio bianco sopra, `--text-lg`, corsivo:

*Il nodo dominante è identificato. Il passo successivo è scegliere la funzione dell'azione: cosa fa il dispositivo su quel nodo, con quelle risorse, in quella direzione.*

Badge modulo successivo: `→ Modulo 4 — Le quattro funzioni`

---

## Note per l'implementazione

### Slide F3.3.2 — Layout a due aree

La slide usa un layout a due aree affiancate (CEDisplay + ExpandableCards) non presente negli altri moduli. Implementare come `<div class="slide__two-col">` con larghezze fisse in CSS: `40%` per l'area CE, `60%` per le card. Su schermi stretti (< 1100px), impilare verticalmente (CE sopra, card sotto).

La `CEDisplay` in questa slide usa `{ highlights: ['N2', 'N3', 'N4'] }`: le tre righe hanno sfondo tenue nel colore del nodo (opacity 0.12) e bordo sinistro solido (2px). Le righe non evidenziate (N1, N5, N6, N7) hanno opacity 0.5 su tutto il testo — visibili ma deemphasize.

### Slide F3.3.3 — Blocchi non espandibili

I quattro blocchi dei criteri non usano ExpandableCards: sono tutti visibili dall'inizio. La scelta è deliberata — i criteri devono poter essere confrontati tra loro visivamente. La struttura è `<div class="criterion-block">` con una classe `criterion-block--last` sull'ultimo per il bordo inferiore più spesso.

### Slide F3.3.5 — Animazione step-by-step

L'animazione step-by-step usa un pattern semplice:

```javascript
let currentStep = 0;
const steps = container.querySelectorAll('.analysis-step');

// Stato iniziale: tutti nascosti
steps.forEach(s => s.style.display = 'none');

// Click "→ Passo successivo"
nextBtn.addEventListener('click', () => {
  if (currentStep < steps.length) {
    steps[currentStep].style.display = 'block';
    steps[currentStep].classList.add('slide-in');
    currentStep++;
  }
  if (currentStep === steps.length) {
    nextBtn.textContent = 'Tutto mostrato';
    nextBtn.disabled = true;
  }
});

// Click "Mostra tutto"
showAllBtn.addEventListener('click', () => {
  steps.forEach(s => { s.style.display = 'block'; });
  currentStep = steps.length;
  nextBtn.textContent = 'Tutto mostrato';
  nextBtn.disabled = true;
});
```

Il blocco "Conclusione" (quinto step) ha uno stile distinto rispetto agli altri quattro — deve essere chiaramente riconoscibile come punto di arrivo dell'analisi.

### Slide F3.3.6 — I due blockquote

I due blockquote affiancati sono collegati da una freccia SVG semplice (→) centrata verticalmente. Su schermi stretti, impilare verticalmente con la freccia che diventa ↓.

### Scelta cromatica del modulo

Il colore accent di M3 è `#e67e22` — lo stesso di N1 in F2. La scelta non è casuale: N1 (Regolazione) è il nodo che in F2 era trattato per primo e con più attenzione al "come si vede". M3 richiama quella stessa attenzione al "come si legge" — ma applicata all'intera CE in chiave F3. Il colore crea un ponte visivo riconoscibile.
