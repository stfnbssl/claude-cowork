---
title: "Piano generale per il sito HCAIRE"
author: "Cowork (Stefano + Claude)"
versione: "0.2"
status: "concordato con Stefano, pronto per Claude Code"
---

# Piano generale per il sito HCAIRE

Questo documento è pensato per essere consegnato a **Claude Code**, che si
occupa dello sviluppo tecnico del sito. Descrive, a partire dai materiali
presenti nel progetto Cowork `HCAIRE Site`, l'architettura informativa, i
template di pagina, le convenzioni di frontmatter e le regole operative che
Claude Code dovrà applicare per generare le due sezioni principali del sito:
**HCAIRE** e **Sviluppo bambino**.

Per i dettagli specifici delle singole sezioni si rimanda ai documenti
complementari `01 — Sezione HCAIRE.md` e `02 — Sezione Sviluppo bambino.md`.

---

## 1. Contesto e materiali disponibili

### 1.1 Cosa è HCAIRE

HCAIRE (Human Centred Artificial Intelligence Research Environment) è un
laboratorio di ricerca che lavora all'incrocio tra filosofia, scienze umane
e intelligenza artificiale generativa, con l'obiettivo di elaborare modelli
concettuali rigorosi su temi complessi dello sviluppo umano, della
relazione, della formazione e della cura.

Il primo progetto fondativo di HCAIRE è **Sviluppo bambino**, un modello
strutturale dello sviluppo umano nella fascia 0–12 anni articolato in sei
assi.

### 1.2 Cartelle e materiali attualmente presenti

```
HCAIRE Site/
├── sezioni/
│   ├── hcaire/
│   │   └── index.md                      ← testo identitario HCAIRE (~2 KB)
│   ├── bartleby/                         ← vuota, placeholder
│   └── progetti/
│       └── sviluppo bambino/
│           ├── assi strutturali/
│           │   ├── md/                   ← 44 capitoli .md (sorgente GDocs)
│           │   │                           SOLO LETTURA per Claude Code
│           │   └── normalized/           ← 44 capitoli .md normalizzati
│           │                               con front-matter, H1/H2/H3 coerenti,
│           │                               note Pandoc [^n] preservate
│           │                               → QUESTA è la sorgente per il rendering
│           ├── metodo/
│           │   └── riflessioni/
│           │       ├── 01 Modello assi strutturali di sviluppo del bambino (0-13 anni).md
│           │       │                       ← panoramica + 12 concetti + nota
│           │       │                         metodologica (33 KB, documento chiave)
│           │       ├── 02 Interlocuzione disciplinare.md      ← stub, 0 KB
│           │       └── 03 Scheda tipo interlocuzione disciplinare.md ← stub, 0 KB
│           └── interlocuzioni disciplinari/
│               └── neuroscienze/
│                   └── Free Energy Principle.md               ← stub, 0 KB
└── pianificazione sito/                                       ← piano per Claude Code
```

### 1.3 Cosa deve produrre Claude Code

Un sito statico (tecnologia a scelta: Astro, Next, Hugo, 11ty — l'importante
è che supporti MDX/remark-gfm o un motore equivalente per note Pandoc)
strutturato attorno a:

- **home page** con menu bar
- due sezioni navigabili dal menu bar: **HCAIRE** e **Sviluppo bambino**
- rendering integrale dei 44 capitoli degli assi strutturali con note a
  piè di pagina, TOC per capitolo, navigazione prev/next
- rendering delle pagine metodologiche (panoramica assi, concetti
  strutturali, nota metodologica)
- un'impalcatura estensibile, pensata per accogliere nel tempo nuovi
  capitoli, nuove interlocuzioni disciplinari e nuovi progetti.

---

## 2. Architettura informativa complessiva

### 2.1 Menu bar della home page

Il menu bar della home page espone più voci di primo livello. Le **prime
due**, coperte da questo piano, sono:

1. **HCAIRE** → `/hcaire/`
2. **Sviluppo bambino** → `/sviluppo-bambino/`

Claude Code gestisce autonomamente le ulteriori voci del menu (ad esempio
**Bartleby**, attualmente in sviluppo), a partire da propri sorgenti e
con proprie convenzioni. Questo piano **non** le dettaglia; si limita a
riservare loro lo spazio tecnico nel menu e nella sitemap.

Il logo/titolo del sito (sinistra del menu) rimanda sempre a `/`.

### 2.2 Home page (`/`)

Pagina di ingresso breve, visivamente identitaria, con:

- hero con il nome HCAIRE e il sottotitolo esteso
  (*Human Centred Artificial Intelligence Research Environment*)
- 2–3 righe di posizionamento (estratte dall'incipit di `sezioni/hcaire/index.md`)
- call-to-action ben visibili verso le sezioni principali:
  `Scopri HCAIRE` → `/hcaire/`,
  `Entra in Sviluppo bambino` → `/sviluppo-bambino/`,
  `Prova Bartleby` → `/bartleby/` (se/quando Claude Code la espone)
- eventuale sezione "novità / ultime pubblicazioni" lasciata come placeholder
  (si popolerà quando ci sarà il blog editoriale menzionato in `index.md`).

### 2.3 Sitemap complessiva

Questa sitemap copre le due sezioni del piano. Le ulteriori sezioni di
primo livello gestite da Claude Code (es. `/bartleby/`) non sono
dettagliate qui: compaiono nel menu e nella home ma hanno sorgenti e
struttura propri.

```
/                                          Home
├── /hcaire/                                Sezione HCAIRE
│   ├── /hcaire/metodo/                     Il metodo HCAIRE
│   ├── /hcaire/ambiente-editoriale/        Blog, comitato, editoriale
│   ├── /hcaire/progetti/                   Indice dei progetti
│   └── /hcaire/ia-centrata-sull-umano/     Posizionamento sull'uso dell'IA
│
├── /bartleby/                              (gestita da Claude Code — fuori piano)
│
└── /sviluppo-bambino/                      Sezione Sviluppo bambino
    ├── /sviluppo-bambino/finalita/         Finalità del progetto
    ├── /sviluppo-bambino/metodo/           Metodo (premessa del Modello + stratificazioni)
    ├── /sviluppo-bambino/modello/          Il modello a sei assi (panoramica)
    │   ├── /sviluppo-bambino/modello/asse-1-ontologico-fenomenologico/
    │   ├── /sviluppo-bambino/modello/asse-2-affettivo-morale/
    │   ├── /sviluppo-bambino/modello/asse-3-normativo-educativo/
    │   ├── /sviluppo-bambino/modello/asse-4-separazione-e-limite/
    │   ├── /sviluppo-bambino/modello/asse-5-desiderio/
    │   └── /sviluppo-bambino/modello/asse-6-storico-culturale/
    ├── /sviluppo-bambino/concetti/         12 concetti strutturali
    ├── /sviluppo-bambino/nota-metodologica/  Nota metodologico-lessicale
    ├── /sviluppo-bambino/assi/             Indice dei 44 capitoli
    │   ├── /sviluppo-bambino/assi/asse-1-ontologico-fenomenologico/
    │   │   ├── .../capitolo-1-.../
    │   │   ├── .../capitolo-2-.../
    │   │   └── … (8 capitoli)
    │   ├── … (asse-2 … asse-6, 44 capitoli totali)
    │   └── …
    ├── /sviluppo-bambino/riflessioni/       Riflessioni di metodo (02, 03 + futuri)
    └── /sviluppo-bambino/interlocuzioni/    Interlocuzioni disciplinari
        └── /sviluppo-bambino/interlocuzioni/neuroscienze/
            └── .../free-energy-principle/
```

Nota: `/sviluppo-bambino/modello/` espone le **sintesi** dei sei assi
(tratte da `01 Modello assi strutturali …`), mentre `/sviluppo-bambino/assi/`
espone i **44 capitoli integrali** (da `normalized/`). Sono due viste
complementari dello stesso materiale: panoramica leggibile in una sola
visita, vs. approfondimento integrale.

### 2.4 Breadcrumb

Ogni pagina sotto `/sviluppo-bambino/assi/` espone un breadcrumb del tipo:

```
Home > Sviluppo bambino > Assi strutturali > Asse N - … > Capitolo N - …
```

In `/hcaire/` breadcrumb semplificato: `Home > HCAIRE > [sottopagina]`.

---

## 3. Contenuti per sezione (sintesi)

### 3.1 Sezione HCAIRE

Fonte unica attuale: `sezioni/hcaire/index.md` (~ 44 righe, 7 sezioni
tematiche). Il documento viene **splittato** in sottopagine tematiche,
preservando il testo integralmente. Dettaglio in
`01 — Sezione HCAIRE.md`.

Mappa base:

| Pagina                                | Fonte (estratto da index.md)                 |
| ------------------------------------- | -------------------------------------------- |
| `/hcaire/` (landing)                  | definizione + "Un ambiente aperto"           |
| `/hcaire/metodo/`                     | "Un metodo"                                  |
| `/hcaire/ambiente-editoriale/`        | "Un ambiente editoriale"                     |
| `/hcaire/progetti/`                   | "Un progetto fondativo" + link               |
| `/hcaire/ia-centrata-sull-umano/`     | "Una intelligenza artificiale…"              |

Il paragrafo "Bartleby" di `index.md` resta nel testo della landing
come presentazione dello strumento, con CTA "Scopri Bartleby →" che
rimanda alla sezione top-level `/bartleby/` (gestita da Claude Code).

### 3.2 Sezione Sviluppo bambino

Fonti:

- `sezioni/progetti/sviluppo bambino/metodo/riflessioni/01 Modello …`
  → sorgente di `finalita/`, `metodo/`, `modello/`, `concetti/`,
  `nota-metodologica/`
- `sezioni/progetti/sviluppo bambino/assi strutturali/normalized/`
  → sorgente di `assi/` (44 capitoli integrali)
- `sezioni/progetti/sviluppo bambino/metodo/riflessioni/02-03`
  → sorgente di `riflessioni/` (attualmente stub)
- `sezioni/progetti/sviluppo bambino/interlocuzioni disciplinari/…`
  → sorgente di `interlocuzioni/` (attualmente stub)

Dettaglio in `02 — Sezione Sviluppo bambino.md`.

---

## 4. Convenzioni tecniche

### 4.1 Frontmatter site-wide

Ogni file `.md` destinato al rendering web riceve (o ha già) un front-matter
YAML con **almeno** questi campi:

```yaml
title: "…"              # obbligatorio, titolo della pagina
section: "…"            # "hcaire" | "sviluppo-bambino"
type: "…"               # "landing" | "page" | "chapter" |
                        # "asse-overview" | "concept" | "stub"
slug: "…"               # segmento URL (kebab-case ASCII)
order: N                # ordinamento dentro il proprio indice
```

Front-matter aggiuntivo **già presente** sui 44 capitoli in `normalized/`:
`asse`, `asse_number`, `asse_slug`, `chapter`, `prev`, `next`. Claude Code
li usa direttamente per generare le pagine di `/sviluppo-bambino/assi/`.

Claude Code, se un file sorgente non ha front-matter (es. i nuovi
`riflessioni/02-03.md`), lo **aggiunge** seguendo questo schema prima di
generare le pagine.

### 4.2 URL e slug

- Tutti gli slug sono **kebab-case ASCII** (no accenti, no apostrofi, no
  spazi).
- Gli slug dei capitoli sono quelli già calcolati nel front-matter
  (`normalized/`).
- Gli slug delle sottopagine di HCAIRE e Sviluppo bambino sono definiti
  nella sitemap (§ 2.3).

### 4.3 Componenti di pagina condivisi

Claude Code costruisce questi componenti riutilizzabili:

- **Sidebar / TOC** — generata a runtime dagli heading `##` e `###` del
  contenuto. Sticky a destra su desktop, collassabile su mobile.
- **Breadcrumb** — visibile in alto su ogni pagina sotto il primo livello.
- **Prev/Next** — in fondo alle pagine capitolo, usa `prev`/`next` dal
  front-matter. `null` = pulsante disattivato.
- **Footnote render** — note Pandoc `[^n]` rese con ancora cliccabile a
  fondo pagina + back-reference. Le librerie standard
  (remark-gfm + remark-footnotes, `remark-pandoc`, rehype-mdx-footnotes
  a seconda dello stack) gestiscono nativamente il formato.
- **ChapterCard / AsseCard** — card riutilizzabile per le pagine indice.
- **Heading anchor** — ogni `h2`/`h3` ha un link-ancora (hover icon).

### 4.4 Heading hierarchy dentro le pagine capitolo

Grazie alla normalizzazione già eseguita (vedi
`pianificazione sito/` script), **ogni capitolo rispetta**:

- `#` = titolo del capitolo (sempre uno, all'inizio)
- `##` = sezioni principali (numerate `1.`, `2.` oppure `N.M`)
- `###` = sottosezioni (presenti solo se il contenuto le prevede)

Claude Code può quindi assumere uniformemente:
`h1 = titolo pagina, h2 = voci TOC, h3 = voci TOC annidate`.

### 4.5 Rendering di "index" pages

Per le pagine indice (sitemap node con figli), Claude Code deve generare
automaticamente una griglia/lista di card con:

- titolo (da `title`)
- descrizione breve (presa dal primo paragrafo del contenuto, oppure da un
  campo `excerpt` opzionale in front-matter — preferibile introdurlo)
- conteggio figli se index-di-indici (es. "8 capitoli")
- link al figlio

### 4.6 Stile tipografico (raccomandazioni, non prescrizioni)

- Font serif per il corpo dei capitoli (leggibilità testo lungo).
- Font sans per navigazione, UI, menu.
- Note a piè di pagina: corpo più piccolo, spaziatura maggiore.
- Massima larghezza misura di lettura ~ 70 caratteri.
- Dark mode opzionale.
- Nessuna gallery di immagini (attualmente i sorgenti non ne prevedono).

---

## 5. Regole operative per Claude Code

### 5.1 Sorgenti di lettura

| Sezione del sito                           | Sorgente                                                   |
| ------------------------------------------ | ---------------------------------------------------------- |
| `/` (home)                                 | vedi § 2.2                                                 |
| `/hcaire/*`                                | `sezioni/hcaire/index.md` (split)                          |
| `/sviluppo-bambino/finalita/`              | premessa di `01 Modello assi…`                             |
| `/sviluppo-bambino/metodo/`                | premessa + § "Ambiti di traducibilità" di `01 Modello…`    |
| `/sviluppo-bambino/modello/` + figli       | §§ 1–6 di `01 Modello…` (uno per asse)                     |
| `/sviluppo-bambino/concetti/`              | § "Concetti strutturali del modello" di `01 Modello…`      |
| `/sviluppo-bambino/nota-metodologica/`     | § "Nota metodologico-lessicale…" di `01 Modello…`          |
| `/sviluppo-bambino/assi/*`                 | 44 file in `normalized/`                                   |
| `/sviluppo-bambino/riflessioni/*`          | `riflessioni/02…`, `riflessioni/03…`                       |
| `/sviluppo-bambino/interlocuzioni/*`       | `interlocuzioni disciplinari/*`                            |

### 5.2 Cosa NON toccare

- `sezioni/progetti/sviluppo bambino/assi strutturali/md/`
  → è la copia sorgente "cruda" da Google Docs. Claude Code **non** la
  legge né la modifica. Rimane come backup.
- I file già presenti in `sezioni/**` devono essere trattati come fonte:
  Claude Code ne genera pagine a partire dal loro contenuto, ma
  **non li riscrive**. Eccezione: può aggiungere front-matter mancante se
  necessario per la pipeline.

### 5.3 Gestione degli stub

I file a 0 byte (`02 Interlocuzione disciplinare.md`,
`03 Scheda tipo interlocuzione disciplinare.md`, `Free Energy Principle.md`)
e la cartella `bartleby/` vuota:

- generano comunque una pagina con titolo derivato dal nome file
- il corpo è sostituito da un componente `StubNotice` che dice
  "Contenuto in elaborazione. Torna a trovarci." e propone un link al
  nodo padre
- il componente `StubNotice` è semanticamente identificabile (classe CSS
  `is-stub`, `<meta name="robots" content="noindex">` per non indicizzarli
  finché vuoti)

Claude Code deve comportarsi automaticamente così quando incontra file con
front-matter `type: "stub"` oppure con corpo vuoto.

### 5.4 Aggiornamenti incrementali

Il flusso tipico dell'utente sarà: aggiungo un file `.md` sorgente in una
delle cartelle di `sezioni/`, oppure aggiungo capitoli in `normalized/`.
Claude Code deve:

1. leggere la struttura di `sezioni/` a ogni build
2. se trova un file nuovo, crea la pagina corrispondente secondo la
   sitemap di § 2.3
3. se trova un file nuovo che non rientra nella sitemap esplicita
   (es. un nuovo asse, o una nuova interlocuzione), segue la regola
   convenzionale: `type: "chapter"` o `type: "page"` + inserimento
   nell'indice del nodo padre, ordinato per `order` del front-matter

### 5.5 Pipeline di conversione markdown → HTML

Stack consigliato (Claude Code è libero di scegliere):

- **Astro** o **Next.js** con plugin `remark-gfm` + `remark-footnotes`
  (o `remark-pandoc-attr` se vuole attributi ai titoli)
- o **Hugo** con Goldmark (supporto note nativo in Hugo ≥ 0.32)

Requisiti minimi del motore scelto:

- supporto note Pandoc `[^n]` native con back-ref
- supporto heading anchor
- supporto front-matter YAML
- possibilità di generare pagine indice programmaticamente a partire da
  collection di file

---

## 6. Checklist di verifica post-build

Prima di considerare il sito pronto:

- [ ] Home page accessibile in `/` con menu a 2 voci
- [ ] Entrambe le voci del menu raggiungibili e funzionanti
- [ ] 44 pagine capitolo generate e raggiungibili via
      `/sviluppo-bambino/assi/asse-N-…/capitolo-N-…/`
- [ ] Note a piè di pagina funzionanti (click sul riferimento porta alla
      nota, click sulla back-ref torna al riferimento) su un campione di
      ≥ 3 capitoli che ne contengono molte
- [ ] Prev/Next corretti all'interno di ciascun asse (primo capitolo ha
      `prev` disattivato, ultimo ha `next` disattivato)
- [ ] TOC automatica per-capitolo mostra tutte le voci `##` e `###`
- [ ] Pagina `/sviluppo-bambino/modello/` ha 6 sottopagine-asse, ciascuna
      con il summary preso da `01 Modello…`
- [ ] Pagina `/sviluppo-bambino/concetti/` mostra i 12 concetti
- [ ] Stub pages mostrano `StubNotice` e sono `noindex`
- [ ] Breadcrumb corretto su tutte le pagine di profondità ≥ 2
- [ ] Link interni tra pagine (es. da un Asse overview al primo capitolo
      di quell'asse) funzionanti
- [ ] Test accessibilità basilari (heading hierarchy, alt text — non
      applicabile qui per assenza immagini —, contrasto colori)
- [ ] Build riproducibile: `npm run build` (o equivalente) produce lo
      stesso output su due macchine diverse a parità di sorgenti

---

## 7. Decisioni prese e punti lasciati aperti

**Decisioni confermate da Stefano:**

- La scelta della **tecnologia** del sito è demandata a Claude Code.
- Il **menu bar** espone in prima e seconda posizione HCAIRE e
  Sviluppo bambino; le altre voci (es. Bartleby) sono gestite
  autonomamente da Claude Code.
- **Lingua** del sito: italiano per tutti i testi UI. Versione EN
  eventualmente in v2.

**Punti ancora aperti, da rifinire in corso d'opera (non bloccanti):**

1. **Il corpo della home `/`**: quanto testo mettere? Una hero
   minimalista con CTA oppure un estratto più lungo dall'`index.md`?
2. **Blog editoriale**: `index.md` lo menziona ma non ci sono ancora
   contenuti. Nascosta dal menu o placeholder in footer fino al
   lancio?
3. **Comitato scientifico-editoriale**: pagina dedicata dentro
   `/hcaire/ambiente-editoriale/` oppure sotto-sezione autonoma?
4. **Tema chiaro/scuro**, **font**, **palette**: lasciati aperti.
   Claude Code può proporre un primo tema e Stefano decide.
5. **Indice dei `concetti/`**: pagina unica con 12 sezioni vs pagina
   indice con 12 sottopagine. Consigliata: pagina unica, perché ogni
   concetto è breve e il confronto è più utile della lettura isolata.

---

## 8. Documenti correlati di questo piano

In questa stessa cartella `pianificazione sito/`:

- `00 - Piano generale per il sito HCAIRE.md` — (questo documento)
- `01 - Sezione HCAIRE.md` — split dell'index.md, template pagine HCAIRE
- `02 - Sezione Sviluppo bambino.md` — mappatura dettagliata dei
  contenuti della sezione Sviluppo bambino, con gli estratti del
  Modello e il template per le pagine capitolo

---

## 9. Nota sullo stato del materiale

**Pronto per il rendering senza ulteriore lavoro:**
- i 44 capitoli in `normalized/` (front-matter, heading, note — tutto
  verificato)
- il testo `01 Modello assi…` (basta splittare in sezioni secondo la
  struttura dei suoi heading esistenti)
- il testo `sezioni/hcaire/index.md` (idem, splittabile per `##`)

**Da produrre prima di passare a Claude Code** (decisione di Stefano):
- completare, se si vuole, `02`, `03` di `riflessioni/`
- completare, se si vuole, il file `Free Energy Principle.md` in
  `interlocuzioni disciplinari/neuroscienze/`
- un testo introduttivo per la home page (`/`) — può essere estratto
  dall'`index.md` HCAIRE
- un testo landing per `/sviluppo-bambino/` (1–2 paragrafi di
  orientamento), se si vuole distinguerlo dal `finalita/`

**Non bloccanti**: gli stub possono restare vuoti; il sito si costruisce
e si espande nel tempo.
