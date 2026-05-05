# Modulo 0 — Orientamento nell'architettura
**Numero slide**: 5
**Colore accent**: `#1a6b8a`
**Tipo prevalente**: narrative + diagram

---

## SLIDE 0.1 — Il problema di partenza

**Tipo**: `narrative`
**Titolo**: Il problema di partenza
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Testo centrato, layout a colonna singola, abbondante spazio bianco. Font grande (--text-2xl per la frase principale).

> Un bambino di 20 mesi guarda un libro illustrato insieme alla madre.
> Indica una figura, vocalizza, poi guarda la madre.
> Lei nomina la figura e sorride.
>
> **Come leggiamo questa scena?**

Sotto la domanda, tre chip/tag affiancati che mostrano prospettive diverse:
- `🩺 Il pediatra` → "Competenza linguistica nella norma?"
- `📚 L'educatore` → "Attenzione sostenuta?"
- `👨‍👩‍👧 Il genitore` → "Capisce già le immagini?"

Sotto i chip, in testo secondario (--color-text-secondary, --text-lg):
*Tre osservatori, tre linguaggi, tre domande diverse — sulla stessa scena.*

**Footer / nota**:
*Questo caso attraverserà tutto il corso. Lo ritroveremo in ogni modulo.*

---

## SLIDE 0.2 — L'architettura del metodo

**Tipo**: `diagram`
**Titolo**: Un metodo in tre fasi
**Sottotitolo**: *(nessuno)*

**Contenuto principale**:

Diagramma verticale interattivo con tre blocchi collegati da frecce. Ogni blocco è cliccabile e mostra un pannello espanso a destra.

```
┌─────────────────────────────┐
│  F1 — Fondazione ontologica │  ← colore: --color-f1 (#6c63ff)
│  "Cosa è lo sviluppo"       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  F2 — Traduzione            │  ← colore: --color-f2 (#1a6b8a) + bordo più spesso
│  Interdisciplinare          │     (siamo qui)
│  "Come si rende leggibile"  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  F3 — Strumenti operativi   │  ← colore: --color-f3 (#2d9cdb)
│  "Come si agisce"           │
└─────────────────────────────┘
```

**Pannello espanso cliccando F1** (appare a destra del diagramma):
- Titolo: "Fase 1 — Fondazione ontologica"
- Funzione: Stabilisce *che tipo di realtà è* lo sviluppo infantile e *che tipo di soggetto è* il bambino.
- Output verso F2: I sei assi strutturali come condizioni di possibilità.
- Non produce strumenti. Fonda i vincoli.

**Pannello espanso cliccando F2** (default aperto all'entrata nella slide):
- Titolo: "Fase 2 — Traduzione Interdisciplinare ← *Siamo qui*"
- Funzione: Rende lo sviluppo **leggibile** nei contesti professionali senza perderne la complessità.
- Input: gli assi strutturali della F1.
- Output: condizioni di traducibilità (Nodi, Matrice, Grammatica).
- Regola fondamentale: **F2 produce leggibilità, non azione.**

**Pannello espanso cliccando F3**:
- Titolo: "Fase 3 — Strumenti operativi"
- Funzione: Trasforma la leggibilità in micro-azioni coerenti senza produrre protocolli, diagnosi o prescrizioni.
- Richiede F2 come prerequisito. La decisione disciplinare resta fuori dal metodo.

**Elemento visivo aggiuntivo**: sotto il diagramma, una riga con tre parole chiave in grassetto:
`DEFINISCE` → `RENDE LEGGIBILE` → `RENDE POSSIBILE L'AZIONE`

---

## SLIDE 0.3 — Fase 1 in sintesi: gli assi strutturali

**Tipo**: `standard`
**Titolo**: Da dove veniamo: la Fase 1
**Sottotitolo**: Gli assi strutturali di sviluppo

**Contenuto principale**:

Due colonne:

**Colonna sinistra** (40% larghezza) — testo introduttivo:

Il metodo assume un'ontologia specifica: il bambino non è un organismo che accumula competenze, né un insieme di funzioni che maturano in sequenza.

È un **soggetto incarnato, temporale e relazionale**.

Gli assi strutturali non sono fasi da attraversare né competenze da misurare. Sono le **dimensioni sempre attive** dell'esperienza in sviluppo.

**Colonna destra** (60% larghezza) — tabella dei sei assi:

Tabella a 3 colonne: `#` | `Asse` | `Domanda guida`

| # | Asse | Domanda guida |
|---|------|--------------|
| 1 | Ontologico-fenomenologico | Come abita il bambino l'esperienza? |
| 2 | Affettivo-morale | Come riconosce l'altro come portatore di esperienza propria? |
| 3 | Normativo-educativo | Come emerge la capacità di orientare l'azione secondo criteri condivisi? |
| 4 | Separazione e limite reale | Come incontra la resistenza del reale? |
| 5 | Desiderio | Come si orienta verso possibilità che eccedono il presente? |
| 6 | Rapporto con il mondo storico-culturale | Come entra nella partecipazione al mondo condiviso? |

La riga dell'asse 1 ha un bordo o sfondo leggermente evidenziato (è fondativo rispetto agli altri).

**Nota in footer**:
*Gli assi sono strutture interpretative, non variabili empiriche. Non si misurano: orientano la costruzione degli strumenti.*

---

## SLIDE 0.4 — Il cuore del corso: la Fase 2

**Tipo**: `standard`
**Titolo**: Cosa fa la Fase 2
**Sottotitolo**: Il cuore metodologico

**Contenuto principale**:

Layout a due sezioni verticali separate da un divisore orizzontale sottile.

**Sezione superiore** — La funzione:

Grande citazione testuale (blockquote stilizzato, bordo sinistro colorato --color-f2):

> *"Costruire condizioni di traducibilità tra livelli disciplinari differenti senza perdita dello statuto teorico originario."*

Sotto, in testo normale:
La F2 occupa il **cuore metodologico** dell'intero progetto. Non produce ancora strumenti operativi. Il suo scopo è uno solo: rendere lo sviluppo **leggibile** ai professionisti di discipline diverse.

**Sezione inferiore** — La regola fondamentale:

Due box affiancati:

Box verde (--color-valid bg molto chiaro, bordo verde):
**✓ F2 produce**
- Leggibilità strutturale
- Domande professionali condivisibili
- Configurazioni osservative
- Condizioni per costruire strumenti

Box rosso (--color-invalid bg molto chiaro, bordo rosso):
**✗ F2 non produce**
- Strumenti operativi
- Protocolli d'intervento
- Diagnosi
- Prescrizioni educative

**Elemento aggiuntivo** — sotto i box, in testo enfatizzato:
*La F2 separa esplicitamente osservazione e decisione operativa.*

---

## SLIDE 0.5 — Il caso che useremo

**Tipo**: `narrative`
**Titolo**: Il nostro caso-guida
**Sottotitolo**: Una lettura condivisa in ambulatorio

**Contenuto principale**:

Layout a colonna singola, narrativo.

**Sezione 1 — La scena** (card con sfondo --color-primary-light, bordo sinistro --color-primary):

Testo narrativo in corsivo, font leggermente più grande (--text-lg):

*Durante un bilancio di salute, il pediatra propone per alcuni minuti una breve situazione di lettura condivisa. Il bambino ha circa 18-24 mesi. È presente un genitore. Sul tavolo c'è un piccolo libro illustrato con immagini semplici: animali, oggetti familiari, figure umane.*

*Il bambino prende il libro, lo apre, guarda alcune immagini, indica una figura, vocalizza qualcosa e guarda l'adulto. Il genitore nomina l'immagine, sorride, aspetta. Il bambino torna a guardare il libro, gira pagina, poi mostra un'altra figura all'adulto.*

**Sezione 2 — Come la leggono le discipline** (tre chip/tag in riga):

Chip colorati con icona + disciplina + lettura riduttiva:

| Disciplina | Lettura comune | Problema |
|------------|---------------|---------|
| 🩺 Pediatria | "Competenza linguistica nella norma" | Riduce a prestazione |
| 📚 Pedagogia | "Buona attenzione sostenuta" | Riduce a funzione cognitiva |
| 🧠 NPI | "Assenza di segnali di allerta" | Riduce a esclusione del deficit |

**Sezione 3 — La domanda della F2** (testo grande, centrato):

*Come leggiamo questa scena senza ridurla?*

Sotto, in testo secondario:
*Questo è il problema che la Fase 2 risolve. Torneremo su questa scena in ogni modulo.*

**Elemento visivo**: piccola icona/illustration di un libro aperto o di due sagome (adulto + bambino) affiancate — stile lineare minimalista.

---

## Note per l'implementazione

- All'entrata nel **Modulo 0**, mostrare una breve transizione di benvenuto (fade-in del titolo del modulo per 400ms).
- La **Slide 0.2** deve avere il pannello F2 già aperto al caricamento; gli altri pannelli si aprono al clic.
- La **Slide 0.5** è volutamente narrativa e lenta — nessuna animazione, solo testo che respira.
- Il **testo del caso-guida** nella Slide 0.5 deve essere esattamente quello definito in `window.CASO_GUIDA.scena` in `app.js` (non duplicarlo nel modulo).
