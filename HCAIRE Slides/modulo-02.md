# Modulo 2 — La Pipeline di Traducibilità
**Numero slide**: 9
**Colore accent**: `#2d6a4f`
**Tipo prevalente**: diagram + standard

---

## Dati globali del modulo

I dati della pipeline sono il cuore di questo modulo. Definirli come costante in `m02.js`:

```javascript
const PIPELINE_STEPS = [
  {
    id: 'f1',
    label: 'F1 — Fondazione ontologica',
    sublabel: 'Assi strutturali + tesi + criteri',
    type: 'foundation',
    color: '#6c63ff',
    control: null,
    glossario: null,
    casoGuida: 'Il bambino è un soggetto incarnato, relazionale, temporale. Il libro non è un oggetto di prestazione: è un mediatore di mondo.'
  },
  {
    id: 'op1',
    label: '① Campo di lavoro',
    sublabel: 'Contesto reale / dispositivo / popolazione',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C0', label: 'Vincolo di contesto', domanda: 'Cosa è osservabile? Cosa è decidibile?' },
    glossario: 'Definisce oggetto reale, vincoli, tempi, attori. Delimita cosa si può osservare e cosa non è direttamente accessibile.',
    casoGuida: 'Bilancio pediatrico · bambino 18-24 mesi · genitore presente · libro illustrato · 3-5 minuti. Osservabili: corpo, sguardo, gesto, vocalizzazione. Non osservabili: motivazione interna, competenza stabile.'
  },
  {
    id: 'op2',
    label: '② Concetto-ponte',
    sublabel: 'Linguaggio del progetto ↔ linguaggio disciplinare',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C1', label: 'Non-riduzionismo', domanda: 'Mantiene la funzione strutturale? È osservabile senza ridursi a variabile?' },
    glossario: 'Rende compatibili linguaggi disciplinari senza appiattire il concetto originario. Non è una semplificazione: è una traduzione che conserva la struttura.',
    casoGuida: 'Concetto-ponte: "Accesso al mondo condiviso". Non "attenzione condivisa" (troppo specifico) né "sviluppo simbolico" (troppo astratto). Mantiene insieme corpo, gesto, relazione e significato.'
  },
  {
    id: 'op3',
    label: '③ Nodo trasversale',
    sublabel: 'Formulazione strutturale multi-asse',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C2', label: 'Attraversamento', domanda: 'Collega più assi? Integra corpo, relazione e senso?' },
    glossario: 'È il "motore" strutturale che attraversa assi e discipline. Non è un caso clinico, non è una variabile. È la configurazione teorica che rende intelligibili le dinamiche trasformative.',
    casoGuida: 'Nodo attivo: N3 — Accesso al mondo condiviso simbolico (Assi 1, 2, 5, 6). Nodo di supporto: N2 — Campo relazionale / Co-regolazione (Assi 1, 2, 3).'
  },
  {
    id: 'op4',
    label: '④ Domande professionali',
    sublabel: 'Interrogabili in contesti reali · non diagnostiche',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C3', label: 'Non-diagnostico', domanda: 'Leggibilità senza classificazione o prescrizione?' },
    glossario: 'Trasformano il Nodo in interrogazioni usabili da pediatra, educatore, genitore. Devono essere osservabili, condivisibili tra discipline, prive di giudizio.',
    casoGuida: '• Il bambino usa l\'oggetto come occasione di scambio con l\'adulto?\n• C\'è alternanza di sguardo tra libro e adulto?\n• Il gesto apre una relazione o rimane azione solitaria?\nNon: "Il bambino ha deficit di attenzione?" o "Il genitore stimola adeguatamente?"'
  },
  {
    id: 'op5',
    label: '⑤ Operatore di lettura',
    sublabel: 'Dati osservativi → configurazione di sviluppo',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C4', label: 'Separazione', domanda: 'Descrive configurazioni senza imporre decisioni?' },
    glossario: 'La struttura mentale attraverso cui il professionista organizza ciò che vede. Non è una griglia. È la forma applicativa del Nodo. Tre domande simultanee: Campo condiviso / Posizione soggettiva / Rapporto con il limite.',
    casoGuida: 'Campo: adulto e bambino si orientano verso un oggetto comune con gesto, sguardo, parola. Posizione: il bambino indica e mostra — c\'è iniziativa soggettiva. Limite: il bambino accetta di condividere il controllo del libro.'
  },
  {
    id: 'op6',
    label: '⑥ Famiglie di output',
    sublabel: 'Osservativi / Formativi / Accompagnamento / Ricerca',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C5', label: 'Scalabilità', domanda: 'Più destinatari, stessa grammatica?' },
    glossario: 'Classi di prodotti possibili senza costruire ancora strumenti specifici. Ogni famiglia ha destinatari, funzione e forma diversi — ma tutti derivano dalla stessa configurazione evolutiva.',
    casoGuida: 'Osservativo: scheda di lettura per il pediatra. Formativo: modulo per educatori su lettura condivisa. Accompagnamento: restituzione ai genitori. Ricerca: protocollo longitudinale. Stessa grammatica, quattro usi.'
  },
  {
    id: 'op7',
    label: '⑦ Output-tipo vuoto',
    sublabel: 'Template riusabile · prova di completezza',
    type: 'operator',
    color: '#2d6a4f',
    control: { code: 'C6', label: 'Completezza', domanda: 'Template riusabile? Campi minimi? Linguaggio neutro?' },
    glossario: 'Struttura compilabile che deriva dall\'operatore di lettura ma non è ancora uno strumento. Non contiene indicatori prefissati, criteri valutativi, prescrizioni. Serve a verificare che la catena regge prima di costruire lo strumento reale.',
    casoGuida: 'Template: "Lettura di una situazione di mondo condiviso". Sezioni: campo osservato · domande triadiche · configurazione risultante · note per F3. Nessuna età, tecnica o giudizio.'
  },
  {
    id: 'f3',
    label: 'F3 — Strumento contestualizzato',
    sublabel: 'Workflow e artefatti · responsabilità disciplinare esplicita',
    type: 'output',
    color: '#2d9cdb',
    control: { code: 'C7', label: 'Responsabilità', domanda: 'La decisione clinica/educativa è fuori dal metodo?' },
    glossario: null,
    casoGuida: 'In ambulatorio: protocollo osservativo per bilancio 18 mesi. In educazione: griglia per l\'educatrice al nido. Per i genitori: scheda narrativa di restituzione. La decisione su cosa fare spetta alla disciplina, non al metodo.'
  }
];
```

---

## SLIDE 2.1 — La pipeline: panoramica

**Tipo**: `diagram`
**Titolo**: La pipeline di traducibilità
**Sottotitolo**: Sette operatori tra F1 e F3

**Contenuto principale**:

Visualizzazione completa della pipeline usando `PipelineAnimator`. Tutti i nodi sono visibili ma con diversa opacità: F1 e F3 ben visibili, i 7 operatori a opacità ridotta (0.4). Quando l'utente clicca su un operatore, il pannello destro mostra nome + glossario. **Non c'è ancora animazione step-by-step: questa slide è la mappa d'insieme.**

A destra della pipeline, pannello fisso con il testo:

**Principio della pipeline**:
La traduzione interdisciplinare non è libera: avviene attraverso una **sequenza stabile di sette operatori**, ognuno con un vincolo di coerenza che ne protegge l'integrità.

Ogni operatore:
- Ha una funzione precisa
- Ha un controllo (guard-rail) che verifica l'integrità del passaggio
- Si applica allo stesso modo in tutti i contesti professionali

**Nota in footer**:
*La pipeline completa applicata al caso-guida è nel Modulo 9. Qui impariamo i singoli operatori.*

---

## SLIDE 2.2 — La logica dei guard-rail

**Tipo**: `standard`
**Titolo**: Ogni passaggio ha un vincolo
**Sottotitolo**: I controlli di coerenza C0–C7

**Contenuto principale**:

Due sezioni verticali:

**Sezione superiore** — spiegazione del principio:

La pipeline non è un elenco di suggerimenti. È una struttura vincolata: ogni passaggio tra un operatore e il successivo è protetto da un **controllo di coerenza** che previene un errore specifico.

Blockquote (bordo sinistro, sfondo chiaro):
*"Se il controllo non passa, la catena non avanza. Non si salta un operatore per arrivare prima al risultato."*

**Sezione inferiore** — tabella dei controlli:

Tabella scrollabile (8 righe), con header sticky. Sfondo alternato chiaro/bianco per leggibilità.

| Passo | Controllo | Errore prevenuto |
|-------|-----------|-----------------|
| Campo di lavoro | C0 — Vincolo di contesto | Osservazioni vaghe o non delimitabili |
| Concetto-ponte | C1 — Non-riduzionismo | Concetti appiattiti a variabili disciplinari |
| Nodo trasversale | C2 — Attraversamento | Nodi mono-asse, senza emergenza |
| Domande professionali | C3 — Non-diagnostico | Domande classificatorie o prescrittive |
| Operatore di lettura | C4 — Separazione | Lettura che impone decisioni operative |
| Famiglie di output | C5 — Scalabilità | Output valido solo per una disciplina |
| Output-tipo vuoto | C6 — Completezza | Template incompleto o con giudizi impliciti |
| Strumento contestualizzato | C7 — Responsabilità | Il metodo che decide al posto della disciplina |

Il badge `GuardrailBadge` appare come icona nella colonna "Controllo" — cliccandola mostra la domanda di controllo completa.

---

## SLIDE 2.3 — Operatore ① Campo di lavoro

**Tipo**: `standard`
**Titolo**: ① Campo di lavoro
**Sottotitolo**: Cosa osserviamo, dove, con chi, per quanto tempo

**Contenuto principale**:

Layout a due colonne.

**Colonna sinistra** — definizione:

**Funzione**: il campo di lavoro delimita il contesto concreto entro cui il concetto fondativo viene osservato e reso interrogabile.

Il campo di lavoro risponde a quattro domande:
- **Dove?** — il contesto fisico e istituzionale
- **Chi?** — gli attori (bambino, adulto, osservatore)
- **Cosa?** — l'oggetto mediatore o il dispositivo
- **Quanto?** — il tempo disponibile e i vincoli

**Regola fondamentale**: il campo deve essere delimitato. "Sviluppo simbolico del bambino" non è un campo di lavoro — è un tema. Un campo di lavoro specifica cosa si vede, quando, in quale contesto.

**Colonna destra** — applicazione al caso-guida:

Card con sfondo --color-primary-light:

**Caso: Lettura condivisa**

| Elemento | Specificazione |
|----------|---------------|
| Contesto | Ambulatorio pediatrico / casa / nido |
| Età | 18-24 mesi |
| Attori | Bambino · genitore · eventualmente pediatra |
| Oggetto | Libro illustrato con immagini semplici |
| Tempo | 3-5 minuti |
| Osservabili | Corpo, sguardo, gesto, vocalizzazione, alternanza adulto-oggetto, iniziativa |
| Non osservabili | Motivazione interna, intenzione psicologica, competenza stabile |

**GuardrailBadge in footer**:
`C0 — Vincolo di contesto` | *La situazione è valida perché è delimitata. Non "sviluppo simbolico" in genere, ma questa situazione, con questi attori, in questo tempo.*

---

## SLIDE 2.4 — Operatore ② Concetto-ponte

**Tipo**: `comparison`
**Titolo**: ② Concetto-ponte
**Sottotitolo**: Tradurre senza appiattire

**Contenuto principale**:

**Sezione superiore** — definizione:

Il concetto-ponte rende compatibili linguaggi disciplinari senza ridurre il concetto originario a una categoria tecnica troppo stretta. Non è una semplificazione: è una traduzione che **conserva la funzione strutturale** del concetto.

**Sezione inferiore** — componente `ComparisonPanel`:

**Colonna sinistra (verde) — Formulazione valida**:
"Accesso al mondo condiviso"

Il concetto-ponte mantiene insieme:
- il corpo (orientamento fisico verso l'oggetto)
- la relazione (l'altro come partecipe)
- il gesto (come apertura verso il comune)
- il significato (il libro come mediatore culturale)

Può essere usato da pediatra, educatore e genitore senza che nessuno debba rinunciare al proprio quadro.

**Colonna destra (rosso) — Formulazioni riduttive**:

Tabella con tre colonne: Formulazione | Disciplina | Problema

| Formulazione | Disciplina | Problema |
|-------------|------------|---------|
| "Il bambino presta attenzione al libro" | Neuropsicologia | Riduce a funzione attentiva |
| "Il bambino sa indicare" | Sviluppo | Riduce a comportamento isolato |
| "Il bambino conosce le figure" | Cognitiva | Riduce a riconoscimento |
| "Il genitore stimola adeguatamente" | Educativa | Sposta su giudizio dell'adulto |
| "Sviluppo simbolico nella norma" | Clinica | Anticipa classificazione |

**GuardrailBadge in footer**:
`C1 — Non-riduzionismo` | *Il concetto-ponte è valido se mantiene insieme corpo, relazione, oggetto, gesto, parola e significato. Non deve diventare una singola variabile.*

---

## SLIDE 2.5 — Operatore ③ Nodo Trasversale

**Tipo**: `standard`
**Titolo**: ③ Nodo Trasversale
**Sottotitolo**: Il motore strutturale della traduzione

**Contenuto principale**:

**Sezione superiore** — definizione rapida (rimandare al Modulo 3 per l'approfondimento):

Il Nodo Trasversale è la **configurazione teorica** che rende intelligibili le dinamiche trasformative generate dalla co-attivazione di più assi strutturali.

Non è un nuovo asse. Non è un meccanismo causale. È il **punto di trasformazione** nella pipeline: è dove si passa da coerenza teorica a interrogabilità professionale.

*(Il Modulo 3 è dedicato interamente ai Nodi. Qui ne vediamo la funzione nella pipeline.)*

**Sezione inferiore** — applicazione al caso con visualizzazione assi:

Card per N3:

**N3 — Accesso al mondo condiviso simbolico** *(nodo principale)*

Struttura: transizione da azione individuale a significato condiviso.

Assi coinvolti (visualizzati come badge colorati): `Asse 1` `Asse 2` `Asse 5` `Asse 6`

Perché questo Nodo?
- Il libro non è solo un oggetto: è un mediatore di mondo
- Il bambino non "presta attenzione": *entra in un campo condiviso*
- Coinvolge corpo (A1), relazione (A2), desiderio (A5) e mondo culturale (A6)

Card per N2 (secondario, più piccola):

**N2 — Campo relazionale / Co-regolazione** *(nodo di supporto)*

Il N3 non si attiva senza un campo relazionale funzionante. N2 lo sostiene: senza co-regolazione tra adulto e bambino, l'accesso al mondo condiviso non è possibile.

**GuardrailBadge in footer**:
`C2 — Attraversamento` | *Il Nodo è valido se collega più assi contemporaneamente e produce una configurazione non riducibile alla somma dei singoli assi.*

---

## SLIDE 2.6 — Operatore ④ Domande professionali

**Tipo**: `standard`
**Titolo**: ④ Domande professionali
**Sottotitolo**: Rendere il Nodo interrogabile nei contesti reali

**Contenuto principale**:

**Sezione superiore** — principio:

Le domande professionali trasformano il Nodo in interrogazioni **usabili da qualsiasi professionista** nel proprio contesto, senza che diventi uno strumento diagnostico. Devono essere:
- osservabili (si risponde guardando, non testando)
- condivisibili tra discipline diverse
- prive di giudizio (non implicano una risposta "giusta")
- non classificatorie (non portano a un'etichetta)

**Sezione centrale** — due colonne:

**Colonna sinistra (verde) — Domande valide per il caso**:

Dalla scena della lettura condivisa, il professionista si chiede:
- Il bambino usa il libro come **occasione di scambio** con l'adulto?
- C'è **alternanza di sguardo** tra libro e adulto?
- Il gesto di indicare **apre una relazione** o rimane azione solitaria?
- L'adulto **aspetta** o anticipa sempre la risposta del bambino?
- Il bambino **riprende il contatto** dopo una breve interruzione?

**Colonna destra (rosso) — Formulazioni da evitare**:

| Formulazione scorretta | Problema |
|----------------------|---------|
| "Il bambino ha deficit di attenzione?" | Classificatorio |
| "Il genitore stimola adeguatamente?" | Giudicante |
| "Il bambino è nella norma per questa età?" | Normativo |
| "Serve una valutazione neuropsichiatrica?" | Anticipa F3 |
| "Il bambino capisce quello che diciamo?" | Non osservabile nella scena |

**GuardrailBadge in footer**:
`C3 — Non-diagnostico` | *Una domanda professionale valida può essere posta da un pediatra, un educatore e un genitore — e nessuno dei tre deve sentirsi fuori posto nell'ascoltare la risposta.*

---

## SLIDE 2.7 — Operatore ⑤ Operatore di lettura

**Tipo**: `standard`
**Titolo**: ⑤ Operatore di lettura
**Sottotitolo**: La struttura mentale che organizza l'osservazione

**Contenuto principale**:

**Sezione superiore** — definizione:

L'operatore di lettura non è una griglia, non è un modulo, non è una checklist. È la **forma applicativa del Nodo** nella mente del professionista che osserva: come organizza ciò che vede prima ancora di scrivere qualcosa.

La forma più stabile è l'**Operatore Triadico**: ogni situazione viene letta attraverso tre domande strutturali simultanee.

**Sezione centrale** — tre card orizzontali (o verticali su mobile):

Card 1 — **Campo condiviso**
*Qui si sta costruendo un mondo comune o solo esecuzione parallela?*

Applicazione: *il bambino e l'adulto si orientano insieme verso il libro — c'è un "noi" che guarda qualcosa di comune.*

Card 2 — **Posizione soggettiva**
*C'è emergenza di posizione nel valore o solo reazione/adattamento?*

Applicazione: *il bambino indica, mostra, vocalizza — c'è iniziativa e non solo risposta agli stimoli dell'adulto.*

Card 3 — **Rapporto con il limite**
*Il limite è abitabile o distrugge il campo?*

Applicazione: *il bambino accetta di condividere il controllo del libro; la sequenza si interrompe e riprende senza disorganizzazione.*

**Sezione inferiore** — lettura sintetica risultante:

Blockquote:
*"Il campo si organizza: c'è orientamento comune verso un oggetto mediatore, iniziativa del bambino nel mostrare, e capacità di riprendere dopo brevi interruzioni. La configurazione è fragile (uso discontinuo) ma evolutivamente aperta."*

**GuardrailBadge in footer**:
`C4 — Separazione` | *L'operatore descrive configurazioni. Non dice cosa fare. Non prescrive. Non diagnostica.*

---

## SLIDE 2.8 — Operatori ⑥ e ⑦: Famiglie di output e Output-tipo vuoto

**Tipo**: `standard`
**Titolo**: ⑥ Famiglie di output · ⑦ Output-tipo vuoto
**Sottotitolo**: Dalla configurazione al template

**Contenuto principale**:

Questa slide presenta due operatori nella stessa slide perché sono strettamente collegati: le famiglie di output definiscono *per chi*, l'output-tipo vuoto definisce *in quale forma*.

**Sezione ⑥ — Famiglie di output**:

Le famiglie di output sono classi di prodotti possibili — non ancora strumenti. La stessa configurazione evolutiva può generare output diversi per destinatari diversi, ma con **la stessa grammatica**.

Quattro card mini affiancate:

| Famiglia | Destinatario | Funzione |
|---------|-------------|---------|
| **Osservativa** | Professionista (pediatra, educatore) | Struttura ciò che vede |
| **Formativa** | Team / équipe | Trasferisce la lettura |
| **Accompagnamento** | Genitore | Restituisce in linguaggio accessibile |
| **Ricerca** | Ricercatore | Standardizza per comparazioni |

Sotto: *Stessa struttura. Quattro usi. Zero prescrizioni.*

`C5 — Scalabilità`: badge ridotto, inline.

**Sezione ⑦ — Output-tipo vuoto**:

Divisore orizzontale tra le due sezioni.

Il template "Lettura di una situazione di mondo condiviso":

```
Titolo del template:  Lettura di una situazione di mondo condiviso
Scopo:                Descrivere come si organizza il campo di esperienza
                      condivisa senza classificare né prescrivere.
─────────────────────────────────────────────────────────
Sezione 1 — Campo osservato        [testo libero]
Sezione 2 — Campo condiviso        [testo libero]
Sezione 3 — Posizione soggettiva   [testo libero]
Sezione 4 — Rapporto con il limite [testo libero]
Sezione 5 — Configurazione (CE)    [codifica strutturale]
Sezione 6 — Note per F3            [solo annotazioni, no prescrizioni]
─────────────────────────────────────────────────────────
Non compilare: età standard · soglie · diagnosi · indicazioni terapeutiche
```

`C6 — Completezza`: *Se un campo non si riesce a compilare in modo neutro, la catena ha un problema. Il template è la prova che la traduzione è riuscita.*

---

## SLIDE 2.9 — La soglia verso F3

**Tipo**: `standard`
**Titolo**: La soglia verso la Fase 3
**Sottotitolo**: Dove finisce F2 e dove inizia la responsabilità disciplinare

**Contenuto principale**:

**Sezione superiore** — riassunto della pipeline completata:

Mini-visualizzazione della pipeline completa (tutti i nodi attivi, nessuno in evidenza — "completata"). Testo breve: *La catena è completa. Il professionista dispone di una Configurazione Evolutiva e di un template pronto. La F2 ha fatto il suo lavoro.*

**Sezione centrale** — tabella delle responsabilità:

Tabella a tre colonne, senza bordo esterno, più leggera:

| Livello | Chi | Funzione |
|---------|-----|---------|
| **F2 — Metodo** | Il framework | Rende leggibile |
| **F3 — Professionista** | Pediatra / educatore / équipe | Valuta e produce il dispositivo |
| **Disciplina** | La professione specifica | Assume la decisione finale |

In grassetto sotto: *Il metodo orienta. Non decide.*

**Sezione destra** — cosa diventa possibile in F3 (dal caso-guida):

Card con sfondo --color-f3 molto chiaro:

**Dal caso lettura condivisa, in F3 potrebbero nascere:**
- Protocollo osservativo per il bilancio dei 18 mesi
- Griglia per l'educatrice al nido (lettura condivisa come attività osservativa)
- Scheda narrativa per i genitori (restituzione accessibile)
- Protocollo di ricerca longitudinale

*Nessuno di questi strumenti è ancora la F2. La F2 ha reso possibile costruirli in modo coerente.*

**GuardrailBadge in footer**:
`C7 — Responsabilità` | *La decisione clinica o educativa è sempre fuori dal metodo. Il professionista usa la leggibilità prodotta dalla F2 per decidere — con la propria responsabilità disciplinare.*

**Chiusura del modulo** — testo in basso, centrato, leggero:

*Nel Modulo 3 approfondiremo i Nodi Trasversali — il cuore della pipeline.*

---

## Note per l'implementazione

### Animazione della pipeline

Nelle slide 2.3–2.8, la pipeline è mostrata come **barra di avanzamento laterale**: una versione compatta della pipeline verticale sul lato sinistro della slide, con il passo corrente evidenziato in --color-accent e i passi precedenti in verde tenue (completati), quelli successivi in grigio (non ancora raggiunti).

Quando si entra nella **slide 2.3** (Campo di lavoro), il passo ① si evidenzia. Quando si avanza alla **slide 2.4** (Concetto-ponte), il passo ① diventa "completato" (verde) e il ② si evidenzia. E così via fino alla slide 2.9.

### Struttura visiva delle slide degli operatori (2.3–2.8)

Ogni slide di operatore ha una struttura fissa riconoscibile:
```
[Header: numero + nome operatore]
[Barra pipeline laterale sinistra con passo evidenziato]
[Area contenuto principale: definizione + caso-guida]
[Footer: GuardrailBadge con codice e testo]
```

Questa struttura fissa crea ritmo e riconoscibilità. Il professionista sa sempre dove si trova nella catena.

### Dati da `PIPELINE_STEPS`

Per ogni slide di operatore, non duplicare il testo: usare `PIPELINE_STEPS[index].glossario` e `PIPELINE_STEPS[index].casoGuida` come sorgente dati. Il testo nelle slide è derivato da questi dati, non scritto due volte.

### Slide 2.8 — doppio operatore

La slide 2.8 copre gli operatori ⑥ e ⑦ nella stessa slide per non frammentare eccessivamente. I due badge della pipeline si evidenziano **entrambi** all'entrata nella slide, con un breve ritardo sequenziale (200ms) per indicare che si tratta di due operatori distinti.
