# Modulo 8 — L'Output-tipo vuoto

**Accent color**: `#27ae60`  
**Slides**: 5  
**Obiettivo**: Far comprendere la funzione e la struttura dell'output-tipo vuoto come passo finale di F2 — l'ultimo operatore della pipeline prima della soglia verso F3. Il modulo chiarisce cosa il template fa e, soprattutto, cosa si rifiuta deliberatamente di fare.

---

## JS Data (costanti del modulo)

```javascript
// --- DEFINIZIONE_OUTPUT_TIPO ---
// Usato nella slide 8.1
const DEFINIZIONE_OUTPUT_TIPO = {
  testo: 'L\'output-tipo vuoto è uno stampo riusabile. Non è ancora lo strumento contestualizzato. Non contiene criteri diagnostici, prescrizioni, soglie o punteggi.',
  funzione: 'Verificare che la catena di traducibilità sia completa prima della costruzione dello strumento reale.',
  regola: 'Il template vuoto organizza la lettura, non decide l\'intervento.',
  regola_alternativa: 'Il template vuoto non è uno strumento debole: è uno strumento trattenuto.',
  regola_tecnica: 'L\'output-tipo vuoto è la prova che la traduzione è completa, non la prova che l\'intervento è già definito.'
};

// --- CRITERI_VALIDITA_TEMPLATE ---
// I 10 criteri di validità di un output-tipo vuoto (§7.2 degli esempi)
// Usato nella slide 8.2
const CRITERI_VALIDITA_TEMPLATE = [
  { id: 1, testo: 'È compilabile',                     tipo: 'strutturale', check: 'Il template ha sezioni reali, con domande guide e spazio per le risposte.' },
  { id: 2, testo: 'Resta neutro',                      tipo: 'strutturale', check: 'Nessuna sezione porta implicita una valutazione positiva o negativa.' },
  { id: 3, testo: 'Non assegna punteggi',              tipo: 'limite',      check: 'Nessuna scala, nessun valore numerico, nessun 0-1-2.' },
  { id: 4, testo: 'Non contiene soglie',               tipo: 'limite',      check: 'Non dice "se X allora Y". Non definisce né normali né patologici.' },
  { id: 5, testo: 'Non formula diagnosi',              tipo: 'limite',      check: 'Non usa categorie diagnostiche; non orienta verso etichette cliniche.' },
  { id: 6, testo: 'Non prescrive azioni',              tipo: 'limite',      check: 'Non dice cosa fare. Non orienta l\'intervento. Non consiglia.' },
  { id: 7, testo: 'Non giudica bambino, adulto o servizio', tipo: 'limite', check: 'Nessuna valutazione implicita sulla famiglia, sul professionista o sul contesto.' },
  { id: 8, testo: 'Distingue osservazione e interpretazione', tipo: 'metodologico', check: 'Sezioni separate: "cosa si vede" e "come si legge". Non mischiate.' },
  { id: 9, testo: 'Lascia spazio a domande aperte',   tipo: 'metodologico', check: 'Include una sezione esplicita "cosa non è ancora leggibile".' },
  { id: 10, testo: 'Può essere adattato in Fase 3',   tipo: 'strutturale',  check: 'La struttura è abbastanza generica da reggere contesti diversi senza essere riscritta da zero.' }
];

// --- TEMPLATE_CASO_GUIDA ---
// Output-tipo vuoto del caso-guida: "Lettura di una situazione di mondo condiviso"
// Usato nella slide 8.3 — versione pre-compilata con dati del caso-guida
const TEMPLATE_CASO_GUIDA = {
  titolo: 'Scheda vuota di leggibilità del mondo condiviso',
  nodoRiferimento: 'N3 — Accesso al mondo condiviso simbolico',
  concettoPonte: 'Accesso al mondo condiviso',
  sezioni: [
    {
      numero: 1,
      sezione: 'Situazione',
      domanda: 'In quale contesto avviene la sequenza?',
      campoVuoto: 'Contesto, attori, oggetto, durata',
      compilazioneCasoGuida: 'Bilancio pediatrico. Bambino 18-24 mesi, genitore presente, libro illustrato. Durata: 3-5 minuti.'
    },
    {
      numero: 2,
      sezione: 'Oggetto mediatore',
      domanda: 'Che cosa sta tra adulto e bambino?',
      campoVuoto: 'Libro, gioco, immagine, evento, altro',
      compilazioneCasoGuida: 'Libro illustrato con immagini semplici (animali, oggetti familiari, figure umane).'
    },
    {
      numero: 3,
      sezione: 'Campo condiviso',
      domanda: 'L\'oggetto diventa comune? Si costruisce un orientamento reciproco?',
      campoVuoto: 'Descrizione osservativa — non valutativa',
      compilazioneCasoGuida: 'Presente. Il bambino indica una figura e guarda l\'adulto; il genitore nomina, sorride, attende. Alternanza di sguardo verso libro e adulto.'
    },
    {
      numero: 4,
      sezione: 'Iniziativa del bambino',
      domanda: 'Il bambino introduce qualcosa di proprio nell\'interazione?',
      campoVuoto: 'Gesti, sguardi, vocalizzi, scelte, rifiuti',
      compilazioneCasoGuida: 'Sì: indica una figura, vocalizza, gira pagina autonomamente, mostra un\'altra figura all\'adulto.'
    },
    {
      numero: 5,
      sezione: 'Risposta adulta',
      domanda: 'L\'adulto sostiene, segue, anticipa o dirige?',
      campoVuoto: 'Descrizione neutrale del comportamento adulto',
      compilazioneCasoGuida: 'L\'adulto nomina l\'immagine indicata, sorride, aspetta la risposta del bambino prima di procedere.'
    },
    {
      numero: 6,
      sezione: 'Continuità',
      domanda: 'Lo scambio si mantiene, si interrompe, si riprende?',
      campoVuoto: 'Sequenze di mantenimento / interruzione / ripresa',
      compilazioneCasoGuida: 'Sequenza breve ma stabile. Il bambino gira pagina (interruzione) e introduce nuova figura (ripresa).'
    },
    {
      numero: 7,
      sezione: 'Rapporto con il limite',
      domanda: 'Come vengono vissute attese, cambi di pagina, proposte adulte?',
      campoVuoto: 'Descrizione — integrabile / destabilizzante',
      compilazioneCasoGuida: 'Il bambino accetta di condividere il controllo del libro; la sequenza si interrompe e riprende. Limite integrabile.'
    },
    {
      numero: 8,
      sezione: 'Configurazione leggibile',
      domanda: 'Che forma assume complessivamente il campo?',
      campoVuoto: 'Sintesi non diagnostica — CE o descrizione strutturale',
      compilazioneCasoGuida: 'Campo condiviso presente ma fragile. Accesso al mondo condiviso sostenuto dalla relazione, non ancora autonomamente stabile. CE: N2↑ N3~ N4↓ | D: ↗ | A: A±'
    },
    {
      numero: 9,
      sezione: 'Domande aperte',
      domanda: 'Che cosa resta da osservare meglio?',
      campoVuoto: 'Questioni non risolte — per osservazioni successive',
      compilazioneCasoGuida: 'Come si comporta il campo con un adulto meno responsivo? Cosa accade quando il bambino è più stanco o meno regolato?'
    },
    {
      numero: 10,
      sezione: 'Possibili destinazioni',
      domanda: 'A quale famiglia di output può servire questo template compilato?',
      campoVuoto: 'Osservativa · Formativa · Restitutiva · Ricerca · Organizzativa · AI-assistita',
      compilazioneCasoGuida: 'Osservativa (scheda bilancio) + Formativa (micro-modulo pediatri/DBS) + Organizzativa (protocollo leggero).'
    }
  ],
  formulaSintesi: 'In questa situazione, il campo condiviso appare _______; l\'iniziativa del bambino si manifesta attraverso _______; la risposta adulta tende a _______; la continuità dello scambio è _______; il rapporto con il limite appare _______. La configurazione complessiva suggerisce _______.',
  formulaCompilata: 'In questa situazione, il campo condiviso appare presente ma discontinuo; l\'iniziativa del bambino si manifesta attraverso indicazione e alternanza di sguardo; la risposta adulta tende a sostenere quando attende, ma a interrompere quando anticipa; la continuità dello scambio è fragile ma recuperabile; il rapporto con il limite appare tollerabile se mediato dall\'adulto. La configurazione complessiva suggerisce un accesso al mondo condiviso sostenuto dalla relazione ma non ancora autonomamente stabile.'
};

// --- CONFRONTO_F2_F3 ---
// Tabella di confronto template vuoto (F2) vs strumento contestualizzato (F3)
// Usato nella slide 8.4
const CONFRONTO_F2_F3 = [
  { aspetto: 'Funzione',       f2: 'Organizzare la leggibilità',      f3: 'Guidare un uso concreto' },
  { aspetto: 'Contesto',       f2: 'Generico o semi-generico',         f3: 'Specifico e definito' },
  { aspetto: 'Destinatario',   f2: 'Non ancora definitivo',            f3: 'Definito' },
  { aspetto: 'Indicatori',     f2: 'Aperti',                           f3: 'Stabilizzati' },
  { aspetto: 'Punteggi',       f2: 'Assenti',                          f3: 'Possibili, se giustificati' },
  { aspetto: 'Istruzioni',     f2: 'Assenti',                          f3: 'Presenti' },
  { aspetto: 'Validazione',    f2: 'Non richiesta come strumento',     f3: 'Necessaria se usato formalmente' },
  { aspetto: 'Responsabilità', f2: 'Metodologica',                     f3: 'Professionale / istituzionale' },
  { aspetto: 'Output',         f2: 'Configurazione leggibile',         f3: 'Scheda, protocollo, guida, modulo' }
];

// --- FAMIGLIE_OUTPUT ---
// Le 7 famiglie di output possibili + strumenti F3 per ogni contesto
// Usato nella slide 8.5
const FAMIGLIE_OUTPUT = [
  { famiglia: 'Osservativa',   forma: 'Scheda di osservazione della lettura condivisa',          colore: '#2980b9' },
  { famiglia: 'Formativa',     forma: 'Micro-modulo per pediatri o educatori',                    colore: '#16a085' },
  { famiglia: 'Restitutiva',   forma: 'Traccia di colloquio con il genitore',                     colore: '#8e44ad' },
  { famiglia: 'Riflessiva',    forma: 'Domande guida per l\'adulto di riferimento',               colore: '#d35400' },
  { famiglia: 'Ricerca',       forma: 'Griglia per confrontare sequenze video',                    colore: '#27ae60' },
  { famiglia: 'Organizzativa', forma: 'Protocollo per inserire la lettura nei bilanci di salute', colore: '#c0392b' },
  { famiglia: 'AI-assistita',  forma: 'Prompt per analizzare trascrizioni o descrizioni di sequenze', colore: '#7f8c8d' }
];

const STRUMENTI_F3 = [
  { contesto: 'Clinico',       strumento: 'Scheda breve per osservare la lettura condivisa nei bilanci di salute' },
  { contesto: 'Pedagogico',    strumento: 'Traccia per educatori del nido su libro e campo condiviso' },
  { contesto: 'Genitoriale',   strumento: 'Scheda semplice per aiutare il genitore a riconoscere i momenti di condivisione' },
  { contesto: 'Ricerca',       strumento: 'Griglia per codifica qualitativa di brevi video' },
  { contesto: 'Formativo',     strumento: 'Micro-caso per formazione di pediatri o volontari NPL/DBS' },
  { contesto: 'AI-assistito',  strumento: 'Prompt per trasformare descrizioni narrative in configurazioni leggibili' }
];
```

---

## Slide 8.1 — Che cos'è l'output-tipo vuoto
**Tipo**: `standard`  
**Titolo**: "L'output-tipo vuoto"  
**Sottotitolo**: "Ultimo passo di F2 — prova di completezza della traduzione"

### Contenuto

**Piccola intestazione di contesto** (breadcrumb-style, grigio, sopra il titolo):
`Pipeline F2 · Passo 7 di 7 · Guardrail C6`

Paragrafo di apertura:

> La traduzione interdisciplinare è completa quando è possibile costruire un template riutilizzabile — una forma che organizza la leggibilità senza ancora diventare strumento operativo. Questo è l'output-tipo vuoto: lo stampo da cui nasce l'azione di Fase 3.

**Card definitoria** (bordo sinistro `#27ae60`):

> L'output-tipo vuoto è uno stampo riusabile. Non è ancora lo strumento contestualizzato.  
> Non contiene criteri diagnostici, prescrizioni, soglie o punteggi.

**Tre label-funzione** in riga sotto la card (chip):
1. **Verifica** la completezza della catena di traducibilità
2. **Organizza** la leggibilità del campo osservato
3. **Prepara** la struttura per i riempimenti di F3

**Separatore sottile**

**Posizione nella pipeline** — una barra orizzontale compatta (mini-pipeline):
```
[F1] → [1. Campo] → [2. Concetto-ponte] → [3. Nodo] → [4. Domande] → [5. Operatore] → [6. Famiglie] → [7. Output-tipo ◀] → [F3]
```
Il passo 7 è evidenziato con sfondo `#27ae60` + testo bianco. Gli altri passi sono grigio chiaro.

**Guardrail C6** (footer della slide):
`GuardrailBadge('C6', 'Completezza', 'Il template è completo se può essere usato come base per futuri strumenti, ma resta ancora vuoto: non prescrive, non valuta, non assegna punteggi.')`

### Note implementative
- La mini-pipeline è `display: flex; gap: 0.3rem; flex-wrap: wrap` con ogni passo come piccolo chip
- Il passo corrente (7) ha `background: #27ae60; color: white; font-weight: 600`
- I passi già visti (1-6) hanno `background: var(--surface-2); color: var(--text-secondary); opacity: 0.8`
- F1 e F3 sono etichette di fase, non passi — stile diverso (bordo pieno, sfondo var(--surface-3))

---

## Slide 8.2 — I 10 criteri di validità
**Tipo**: `interactive`  
**Titolo**: "Quando un template è valido?"  
**Sottotitolo**: "10 criteri di completezza e neutralità"

### Layout
Griglia 2 colonne × 5 righe su desktop, colonna singola su mobile. Ogni cella è una card cliccabile con numero + testo del criterio.

Al click sulla card → espande un pannello sotto (accordion `multiOpen: true`) con:
1. Il testo del `check` (verifica operativa — da `CRITERI_VALIDITA_TEMPLATE[i].check`)
2. Una chip che indica il tipo di criterio: `strutturale` (verde), `limite` (rosso/arancio), `metodologico` (blu)

### Differenziazione visiva per tipo
- **Strutturale** (criteri 1, 2, 10) — bordo left `#27ae60` — riguarda la forma del template
- **Limite** (criteri 3, 4, 5, 6, 7) — bordo left `#e74c3c` — ciò che il template si rifiuta di fare
- **Metodologico** (criteri 8, 9) — bordo left `#2980b9` — distinzioni operative

### Box formula sistetica
Dopo la griglia, un box centrato (sfondo `#eafaf1`, bordo `#27ae60`):
> **"Il template vuoto organizza la lettura, non decide l'intervento."**

### Dati
Usa `CRITERI_VALIDITA_TEMPLATE` — array di 10 oggetti definito sopra.

### Note implementative
- Le cards hanno altezza fissa ~70px (chiuse): numero in grassetto a sinistra, testo a destra
- Al click → `max-height` espande per mostrare check + chip tipo
- La chip tipo usa stile small badge: `font-size: 0.7rem; padding: 0.15rem 0.5rem; border-radius: 3px; text-transform: uppercase`

---

## Slide 8.3 — Il template del caso-guida
**Tipo**: `interactive`  
**Titolo**: "Scheda vuota di leggibilità del mondo condiviso"  
**Sottotitolo**: "Template applicato al caso-guida — sezioni compilabili"

### Layout
Due zone:
- **Zona superiore** (always visible): titolo del template + nodo di riferimento + concetto-ponte
- **Zona centrale**: tabella delle 10 sezioni con toggle interattivo
- **Zona inferiore**: formula di sintesi (prima vuota, poi compilata al click)

### Zona superiore — header template
Tre badge in riga:
- `Template`: "Scheda vuota di leggibilità del mondo condiviso"
- `Nodo`: "N3 — Accesso al mondo condiviso simbolico"
- `Concetto-ponte`: "Accesso al mondo condiviso"

### Zona centrale — tabella 10 sezioni

Ogni riga della tabella ha:
- **Numero** (1–10, monospace)
- **Sezione** (nome della sezione in grassetto)
- **Domanda guida** (corsivo, grigio)
- **Campo** — alterna tra due stati con un toggle/click:
  - Stato **VUOTO**: mostra `campoVuoto` (descrizione del tipo di informazione da inserire) — sfondo `var(--surface-2)`, testo tenue, placeholder-style
  - Stato **COMPILATO**: mostra `compilazioneCasoGuida` — sfondo `#eafaf1`, testo normale, bordo sinistro `#27ae60`

**Bottone sopra la tabella**: "Mostra compilazione caso-guida" (toggle globale) — al click passa TUTTI i campi da VUOTO a COMPILATO in un'unica transizione. Testo del bottone: "Mostra compilazione" / "Nascondi compilazione" (toggle).

Le singole sezioni possono anche essere cliccate individualmente (click sulla riga = toggle di quella sola sezione).

### Zona inferiore — formula di sintesi

Header: "Formula di sintesi prevista dal template"

Prima: mostra `formulaSintesi` con gli spazi bianchi visibili come underscore — `font-family: monospace; color: var(--text-secondary)`

Bottone sotto: "Mostra formula compilata"

Al click: la formula `formulaSintesi` viene sostituita da `formulaCompilata` con fade-in. Sfondo `#eafaf1`.

### Dati
Usa `TEMPLATE_CASO_GUIDA` definito sopra.  
Legge anche `window.CASO_GUIDA` per i riferimenti al nodo e al contesto.

### Note implementative
- La tabella usa `<table>` o `<div>` a 4 colonne; le righe sono cliccabili (cursor: pointer)
- Transizione stato VUOTO → COMPILATO: `background-color` transition 200ms + fade del testo
- Il bottone "Mostra compilazione caso-guida" è il CTA principale della slide: `background: #27ae60; color: white; border-radius: 6px; padding: 0.5rem 1.25rem`
- Su mobile: ridurre le 4 colonne a 2 (numero+sezione / domanda+campo stacked)

---

## Slide 8.4 — Template vuoto vs strumento contestualizzato
**Tipo**: `comparison`  
**Titolo**: "Due forme, due funzioni"  
**Sottotitolo**: "Template F2 e strumento F3 a confronto"

### Layout
**Tabella di confronto** a 3 colonne: Aspetto · Template vuoto F2 · Strumento contestualizzato F3.

Header colonne:
- "Aspetto" (neutro)
- "Template vuoto — F2" → sfondo `#eafaf1`, header `#27ae60`
- "Strumento contestualizzato — F3" → sfondo `#fef9e7`, header `#f39c12`

Le 9 righe della tabella (da `CONFRONTO_F2_F3`) vengono rese con:
- Colonna F2: testo verde scuro `#1e8449`, indicando "ancora aperto"
- Colonna F3: testo arancio scuro `#d35400`, indicando "già definito"

### Box regola — tre formulazioni sovrapposte
Sotto la tabella, un box `#eafaf1` con le tre formulazioni in ordine crescente di tecnicità:

> "Il template vuoto organizza la lettura, non decide l'intervento."  
> "Il template vuoto non è uno strumento debole: è uno strumento trattenuto."  
> "L'output-tipo vuoto è la prova che la traduzione è completa, non la prova che l'intervento è già definito."

Le tre frasi appaiono in sequenza (non insieme): click / tap avanza alla frase successiva. Questo mantiene il peso di ciascuna formulazione.

### Guardrail C6 + C7
Due GuardrailBadge affiancati nel footer:
- `GuardrailBadge('C6', 'Completezza', 'Il template è riusabile, resta vuoto, non prescrive, non valuta, non assegna punteggi.')`
- `GuardrailBadge('C7', 'Responsabilità', 'La decisione operativa appartiene a F3 e alle responsabilità disciplinari specifiche. F2 produce solo la grammatica di traducibilità.')`

Se lo spazio è limitato, i due badge si impilano verticalmente.

### Dati
Usa `CONFRONTO_F2_F3` — array di 9 oggetti definito sopra.

### Note implementative
- La tabella ha righe alternate `background: var(--surface-1)` / `var(--surface-2)` per leggibilità
- Le tre formulazioni usano `position: relative` con il testo corrente visibile e `opacity: 0` per i nascosti; il click incrementa un contatore `formulaIndex` (0→1→2→loop)
- I due GuardrailBadge hanno display `flex; gap: 1rem` e si impilano su mobile (`flex-direction: column`)

---

## Slide 8.5 — Famiglie di output e soglia F3
**Tipo**: `narrative`  
**Titolo**: "Da qui, si costruisce"  
**Sottotitolo**: "Le famiglie di output e la soglia verso Fase 3"

### Contenuto

**Paragrafo di apertura**:
> Il template vuoto mostra che la traduzione è riuscita. Ora è possibile costruire. Ogni famiglia di output è una classe di prodotti possibili — non ancora uno strumento definitivo, ma la direzione che lo strumento prenderà in Fase 3.

**Tabella famiglie di output** — 7 righe (da `FAMIGLIE_OUTPUT`):

| Famiglia | Possibile forma |
|---|---|
| Osservativa | Scheda di osservazione della lettura condivisa |
| Formativa | Micro-modulo per pediatri o educatori |
| Restitutiva | Traccia di colloquio con il genitore |
| Riflessiva | Domande guida per l'adulto di riferimento |
| Ricerca | Griglia per confrontare sequenze video |
| Organizzativa | Protocollo per inserire la lettura nei bilanci di salute |
| AI-assistita | Prompt per analizzare trascrizioni o descrizioni di sequenze |

La colonna "Famiglia" ha un pallino colorato (da `FAMIGLIE_OUTPUT[i].colore`) prima del testo.

**Separatore "Soglia F3"** (stessa grafica di slide 6.7 — linea tratteggiata con label centrata)

**Tabella strumenti possibili in F3** (da `STRUMENTI_F3`) — 6 righe, 2 colonne: Contesto · Strumento possibile:

| Contesto | Strumento possibile |
|---|---|
| Clinico | Scheda breve per osservare la lettura condivisa nei bilanci di salute |
| Pedagogico | Traccia per educatori del nido su libro e campo condiviso |
| Genitoriale | Scheda semplice per aiutare il genitore a riconoscere i momenti di condivisione |
| Ricerca | Griglia per codifica qualitativa di brevi video |
| Formativo | Micro-caso per formazione di pediatri o volontari DBS/NPL |
| AI-assistito | Prompt per trasformare descrizioni narrative in configurazioni leggibili |

Nota sotto la tabella (piccola, corsiva, grigio):
> F2 si ferma qui. La costruzione degli strumenti, la definizione dei protocolli, la validazione: tutto questo appartiene alla responsabilità disciplinare di F3.

**Box conclusivo** (sfondo `#eafaf1`, bordo `#27ae60`, testo centrato):
> La Fase 2 ha prodotto leggibilità.  
> F3 produce azione.  
> Il template vuoto è il punto di passaggio.

### Note implementative
- Il pallino colorato prima del nome famiglia: `display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: [colore]; margin-right: 0.5rem`
- Le due tabelle hanno stili omogenei — stesse dimensioni di font, stesso padding — per coerenza visiva
- Il separatore "Soglia F3" riutilizza il componente già specificato in modulo 6 slide 6.7
- Il box conclusivo è l'ultimo elemento della slide — padding generoso, font leggermente più grande della norma, `line-height: 2`

---

## Note generali del modulo

### Tensione pedagogica centrale
Il modulo deve comunicare una tensione: il template vuoto è la fine di F2 e l'inizio di F3. Non è un prodotto debole o provvisorio — è deliberatamente trattenuto. La difficoltà per i professionisti non è costruire il template, ma resistere alla tentazione di riempirlo con prescrizioni prima che sia il momento. Questa tensione è il cuore pedagogico del modulo.

### Progressione delle slide
**8.1** (cos'è) → **8.2** (cosa deve rispettare) → **8.3** (come si presenta concretamente) → **8.4** (differenza da F3) → **8.5** (cosa apre). Le slide 8.2 e 8.3 possono sembrare ridondanti ma hanno funzioni diverse: 8.2 è il controllo formale, 8.3 è la pratica applicata al caso-guida.

### Guardrail C6 e C7
- C6 (Completezza): compare in slide 8.1 (contesto) e 8.4 (confronto)
- C7 (Responsabilità): compare solo in 8.4, abbinato a C6 — sono i due guardrail di soglia
- C5 (Scalabilità) è già stato introdotto in modulo 2 e non va ripetuto qui

### Connessione con il modulo 9
Il template del caso-guida compilato in slide 8.3 (soprattutto la sezione 8 — Configurazione leggibile) sarà il punto di partenza della pipeline completa in modulo 9. È opportuno che Claude Code mantenga coerenza tra `TEMPLATE_CASO_GUIDA.sezioni[7].compilazioneCasoGuida` e la CE del caso-guida in `window.CASO_GUIDA.pipeline.ce`.

### Design
- Accent `#27ae60` (verde medio) — il verde è il colore dell'apertura e della crescita; appropriato per un modulo che "apre" verso F3
- Le due tabelle di slide 8.5 devono essere leggibili anche su schermi più piccoli: nessun testo che va a capo stranamente
- Evitare troppe animazioni in questo modulo: la concentrazione deve essere sui contenuti, non sugli effetti visivi
