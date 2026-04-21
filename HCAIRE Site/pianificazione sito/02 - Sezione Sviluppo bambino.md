---
title: "Sezione Sviluppo bambino — piano dettagliato"
versione: "0.1"
---

# Sezione Sviluppo bambino — piano dettagliato

Questo documento dettaglia la sezione `/sviluppo-bambino/` del sito,
prevista nel piano generale (`00 — Piano generale per il sito HCAIRE.md`).
È la sezione più ricca del sito: espone l'intero modello strutturale dello
sviluppo del bambino 0–12 anni.

## 1. Obiettivo della sezione

`/sviluppo-bambino/` deve, nell'ordine:

1. **introdurre** il progetto: di cosa si tratta, a chi è rivolto, con
   quale posizionamento teorico;
2. **illustrare il metodo** di lavoro (filosofico-concettuale, non
   operativo);
3. **esporre integralmente i documenti fondativi** — il Modello a sei
   assi nella sua versione sintetica, e i 44 capitoli integrali;
4. **predisporre spazi** per i materiali in arrivo (interlocuzioni
   disciplinari, riflessioni, eventuali strumenti derivati).

Il tono è **accademico accessibile**: denso nei contenuti, lineare nella
struttura, senza divulgazione semplificatrice.

## 2. Mappa dei contenuti sorgente → pagine

### 2.1 Dai materiali esistenti alle pagine web

| Pagina web                                               | File sorgente                                                                 | Estratto / operazione                                          |
| -------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `/sviluppo-bambino/`                                     | `01 Modello assi…` § Premessa (prime 8 righe)                                 | breve intro + CTA verso finalita/metodo/assi                   |
| `/sviluppo-bambino/finalita/`                            | `01 Modello assi…` § Premessa (integrale)                                     | testo tal quale                                                |
| `/sviluppo-bambino/metodo/`                              | `01 Modello assi…` § Premessa (parte "percorso per stratificazioni")          | testo tal quale + collegamenti                                 |
|                                                          | + § "Ambiti di traducibilità"                                                 |                                                                |
| `/sviluppo-bambino/modello/`                             | `01 Modello assi…` titoli "1. Asse …" … "6. Asse …"                           | panoramica/indice con card per i 6 assi                        |
| `/sviluppo-bambino/modello/asse-N-<slug>/`               | `01 Modello assi…` § "N. Asse …" (una per asse, testo integrale)              | pagina di sintesi per ogni asse                                |
| `/sviluppo-bambino/concetti/`                            | `01 Modello assi…` § "Concetti strutturali del modello" (tutti e 12)          | una sola pagina con i 12 concetti in sequenza                  |
| `/sviluppo-bambino/nota-metodologica/`                   | `01 Modello assi…` § "Nota metodologico-lessicale…" (integrale)               | testo tal quale                                                |
| `/sviluppo-bambino/assi/`                                | `normalized/` (lettura della struttura cartelle)                              | indice dei 6 assi + conteggi capitoli                          |
| `/sviluppo-bambino/assi/asse-N-<slug>/`                  | `normalized/Asse N - …/` (listing dei capitoli)                               | indice dei capitoli dell'asse                                  |
| `/sviluppo-bambino/assi/asse-N-<slug>/<capitolo-slug>/`  | singolo `.md` in `normalized/`                                                | pagina capitolo integrale                                      |
| `/sviluppo-bambino/riflessioni/`                         | cartella `metodo/riflessioni/` (escluso il 01 già usato)                      | indice dei documenti metodologici                              |
| `/sviluppo-bambino/riflessioni/<slug>/`                  | singoli `02…md`, `03…md` e futuri                                             | pagina con `StubNotice` finché vuoti                           |
| `/sviluppo-bambino/interlocuzioni/`                      | cartella `interlocuzioni disciplinari/`                                       | indice per ambito disciplinare                                 |
| `/sviluppo-bambino/interlocuzioni/neuroscienze/`         | cartella `interlocuzioni disciplinari/neuroscienze/`                          | indice dei documenti dell'ambito                               |
| `/sviluppo-bambino/interlocuzioni/<ambito>/<slug>/`      | singoli `.md` dell'ambito                                                     | pagina con `StubNotice` finché vuoti                           |

### 2.2 Importante: splittare `01 Modello assi…` senza riscritturalo

Il file `01 Modello assi di sviluppo del bambino (0-13 anni).md` è **un
documento unico di 33 KB**. Claude Code lo processa **senza modificarlo**:
legge i suoi heading e genera le pagine web splittando il contenuto in
base ai `##` di primo livello.

Schema:

```
# Modello assi strutturali di sviluppo del bambino (0-12 anni)    ← H1 principale
##  Premessa                                                     ← finalita/ + metodo/ base
##  1. Asse ontologico-fenomenologico                            ← modello/asse-1
##  2. Asse affettivo-morale                                     ← modello/asse-2
##  3. Asse normativo-educativo                                  ← modello/asse-3
##  4. L'asse della separazione e del limite reale               ← modello/asse-4
##  5. Asse del rapporto con il desiderio                        ← modello/asse-5
##  6. Asse del rapporto con il mondo storico e culturale…       ← modello/asse-6
# Concetti strutturali del modello                               ← concetti/ (ha H1 autonomo)
  ## 1. Soggetto … ## 12. Responsabilità
# Nota metodologico-lessicale sul modello a sei assi             ← nota-metodologica/
```

Claude Code, quando split-ta, **preserva le note metodologiche interne**
(es. "Nota metodologica e di controllo lessicale") che ogni Asse contiene
a chiusura, renderizzandole come box/riquadro distintivo a fondo pagina.

## 3. Pagine — template e front-matter

### 3.1 `/sviluppo-bambino/` (landing)

```yaml
---
title: "Sviluppo bambino"
subtitle: "Un modello strutturale per lo sviluppo umano 0–12 anni"
section: "sviluppo-bambino"
type: "landing"
slug: ""
order: 0
---
```

Contenuto (indicativo):

1. hero con titolo + sottotitolo
2. 2–3 paragrafi di apertura, estratti dall'incipit della Premessa
3. griglia di 4 card prominenti:
   - "Finalità del progetto" → `/sviluppo-bambino/finalita/`
   - "Il metodo" → `/sviluppo-bambino/metodo/`
   - "Il modello a sei assi" → `/sviluppo-bambino/modello/`
   - "Gli assi strutturali (44 capitoli)" → `/sviluppo-bambino/assi/`
4. riga secondaria di card per "Concetti strutturali", "Nota
   metodologica", "Riflessioni", "Interlocuzioni disciplinari"

### 3.2 `/sviluppo-bambino/finalita/`

```yaml
---
title: "Finalità del progetto"
section: "sviluppo-bambino"
type: "page"
slug: "finalita"
order: 1
excerpt: "Il modello si colloca su un piano filosofico-concettuale. Non fornisce indicazioni operative dirette: costruisce il campo concettuale che le rende possibili."
---
```

Contenuto: intera **Premessa** del Modello (~ 40 righe).

### 3.3 `/sviluppo-bambino/metodo/`

```yaml
---
title: "Il metodo"
section: "sviluppo-bambino"
type: "page"
slug: "metodo"
order: 2
excerpt: "Percorso per stratificazioni successive: fondazione, traduzione interdisciplinare, strumenti, verifica."
---
```

Contenuto:

1. dalla Premessa, i paragrafi che descrivono il percorso per
   stratificazioni successive (4 fasi)
2. § "Ambiti di traducibilità del modello" (dalla Nota metodologica)
3. link in calce a "Concetti strutturali" e "Nota metodologica"
   per approfondire

### 3.4 `/sviluppo-bambino/modello/` (indice dei 6 assi)

```yaml
---
title: "Il modello a sei assi"
section: "sviluppo-bambino"
type: "index"
slug: "modello"
order: 3
excerpt: "Sei dimensioni strutturali, sempre compresenti, dello sviluppo del soggetto."
---
```

Contenuto:

1. paragrafo di inquadramento (estratto dalla Nota metodologica,
   § "Gerarchia implicita tra gli assi")
2. griglia di 6 card con:
   - numero e titolo dell'Asse
   - sottotitolo (dal Modello, es. "La costituzione del soggetto nel
     tempo, nel corpo e nella relazione")
   - domanda guida dell'asse
   - link a `/sviluppo-bambino/modello/asse-N-…/`
   - link secondario "Leggi i capitoli →" a `/sviluppo-bambino/assi/asse-N-…/`

### 3.5 `/sviluppo-bambino/modello/asse-N-<slug>/` (sintesi del singolo asse)

```yaml
---
title: "Asse <N> — <titolo>"
section: "sviluppo-bambino"
type: "asse-overview"
slug: "asse-N-<slug>"
asse_number: N
parent: "modello"
order: N
excerpt: "<sottotitolo dell'asse>"
---
```

Contenuto: testo integrale del blocco `## N. Asse …` del Modello,
compresa la "Nota metodologica e di controllo lessicale" finale resa
come riquadro secondario.

In calce:

- riquadro "Leggi i capitoli di questo asse →" con link all'indice
  dei capitoli (`/sviluppo-bambino/assi/asse-N-…/`)
- prev/next per navigare tra assi (Asse 1 ← → Asse 2 ← → … ← → Asse 6)

### 3.6 `/sviluppo-bambino/concetti/`

```yaml
---
title: "Concetti strutturali del modello"
section: "sviluppo-bambino"
type: "page"
slug: "concetti"
order: 4
excerpt: "Dodici operatori concettuali: soggetto, corporeità, regolazione, relazione, altro, norma, giudizio, limite, reale, desiderio, simbolico, responsabilità."
---
```

Contenuto: pagina unica con tutti e 12 i concetti in sequenza, ciascuno
con un `##` che ne apre la scheda.

Rendering consigliato:

- TOC a sinistra con i 12 concetti, sticky su desktop
- ogni concetto è una sezione `##` con sotto-struttura "Funzione
  strutturale / Asse fondativo / Circolazione"
- icona link a `#concetto-N` per condividere l'ancora

Si è scelto **una pagina sola** (contro 12 sottopagine) perché ogni
concetto è breve (~ 10-15 righe) e la comparazione tra concetti è più
utile della lettura isolata. Se Stefano vuole pagine singole, si ricava
automaticamente: ogni `##` diventa una pagina indipendente con slug
`<concetto>`.

### 3.7 `/sviluppo-bambino/nota-metodologica/`

```yaml
---
title: "Nota metodologico-lessicale"
section: "sviluppo-bambino"
type: "page"
slug: "nota-metodologica"
order: 5
excerpt: "Statuto del modello, principio di armonizzazione lessicale, gerarchia degli assi, principio di non-riduzionismo, transizioni."
---
```

Contenuto: testo integrale della "Nota metodologico-lessicale sul modello
a sei assi di sviluppo", splittato con i suoi `##` interni come
sotto-sezioni navigabili via TOC.

### 3.8 `/sviluppo-bambino/assi/`

```yaml
---
title: "Gli assi strutturali — 44 capitoli"
section: "sviluppo-bambino"
type: "index"
slug: "assi"
order: 6
excerpt: "La versione integrale, capitolo per capitolo, del modello a sei assi."
---
```

Contenuto:

1. paragrafo introduttivo che distingue *questa* pagina da
   `/sviluppo-bambino/modello/` ("qui trovi i capitoli integrali — lì
   trovi la sintesi del modello")
2. 6 blocchi, uno per asse, ciascuno con:
   - titolo dell'asse
   - breve domanda guida (una riga, dal Modello)
   - elenco numerato degli 8 capitoli (6 per Asse 3, 7 per Assi 5 e 6)
   - ogni voce è un link a `/sviluppo-bambino/assi/asse-N-…/capitolo-N-…/`

### 3.9 `/sviluppo-bambino/assi/asse-N-<slug>/` (indice di un asse)

```yaml
---
title: "Asse <N> — <titolo>"
section: "sviluppo-bambino"
type: "index"
slug: "asse-N-<slug>"
parent: "assi"
asse_number: N
order: N
---
```

Contenuto:

1. titolo dell'asse + sottotitolo
2. link "↑ Leggi la sintesi di questo asse" a
   `/sviluppo-bambino/modello/asse-N-…/`
3. lista ordinata dei capitoli dell'asse (ottenuta leggendo i `.md`
   di `normalized/Asse N - …/` e ordinandoli per `chapter`)
4. per ogni capitolo: titolo, numero, eventuale excerpt (prime 1–2
   righe del corpo)
5. breadcrumb: Home > Sviluppo bambino > Assi strutturali > Asse N

### 3.10 Pagina capitolo `/sviluppo-bambino/assi/asse-N-<slug>/<capitolo-slug>/`

Template **cruciale**. Qui si trovano i 44 capitoli dei documenti
fondativi.

Front-matter: **già presente** nei file di `normalized/`. Claude Code
legge direttamente.

Layout (dall'alto):

1. menu bar globale
2. breadcrumb: Home > Sviluppo bambino > Assi strutturali > Asse N > Capitolo N
3. intestazione con:
   - numero capitolo (piccolo, sopra)
   - titolo `H1`
   - nome e numero dell'Asse (piccolo, link a `/sviluppo-bambino/assi/asse-N-…/`)
4. due colonne su desktop (stack verticale su mobile):
   - **sinistra**, contenuto markdown renderizzato (corpo)
   - **destra**, TOC sticky (dagli `##` e `###`) + link "↑ Torna in cima"
5. sezione **Note** a piè del corpo, con le definizioni Pandoc `[^n]: …`
   rese in stile footnote.
6. navigazione prev/next in fondo: "← Capitolo N-1" e "Capitolo N+1 →"
   (disabilitati se `null` nel front-matter)
7. in chiusura, link "Tutti i capitoli di questo Asse" →
   `/sviluppo-bambino/assi/asse-N-…/`

Stile **tipografico**:

- corpo serif, misura generosa (~ 18px)
- massima larghezza ~ 70 caratteri
- note a piè di pagina in corpo più piccolo, separate da hairline

### 3.11 `/sviluppo-bambino/riflessioni/`

```yaml
---
title: "Riflessioni"
section: "sviluppo-bambino"
type: "index"
slug: "riflessioni"
order: 7
excerpt: "Materiali metodologici che accompagnano il modello."
---
```

Contenuto: lista dei documenti in `metodo/riflessioni/` (escluso il
`01 Modello…` che è già esposto nelle pagine precedenti).

Attualmente **vuoti** `02` e `03`: appaiono come stub.

### 3.12 `/sviluppo-bambino/interlocuzioni/`

```yaml
---
title: "Interlocuzioni disciplinari"
section: "sviluppo-bambino"
type: "index"
slug: "interlocuzioni"
order: 8
excerpt: "Traduzione interdisciplinare del modello — neuroscienze, psicologia, pedagogia, sociologia e altro."
---
```

Contenuto:

1. paragrafo introduttivo (breve, da scrivere; proposta: riprendere
   dalla Nota metodologica "Ambiti di traducibilità del modello")
2. lista degli ambiti disciplinari (ciascuno è una cartella sotto
   `interlocuzioni disciplinari/`), con conteggio documenti

Le pagine figlie (`/<ambito>/<slug>/`) seguono la logica standard pagina
/ stub.

## 4. Navigazione interna alla sezione

Sotto il menu bar principale, `/sviluppo-bambino/` espone un sotto-menu
sempre visibile con queste voci in ordine:

- Finalità
- Metodo
- Il modello
- Concetti strutturali
- Nota metodologica
- Assi strutturali (44 capitoli)
- Riflessioni
- Interlocuzioni disciplinari

Su mobile collassa.

All'interno di `/assi/` (cioè nelle pagine capitolo e nelle pagine di
asse), un secondo livello di navigazione è disponibile: breadcrumb +
TOC + prev/next.

## 5. Relazioni tra pagine (link impliciti)

Claude Code deve generare link incrociati automaticamente:

- da ogni pagina `/modello/asse-N-…/` → al primo capitolo dell'asse
  corrispondente in `/assi/asse-N-…/`
- da ogni pagina `/assi/asse-N-…/capitolo-M/` → alla sintesi
  `/modello/asse-N-…/` (linkare "Vai alla sintesi di questo asse" in
  head o footer del capitolo)
- dalla pagina `/concetti/` → quando cita un asse, linkare a
  `/modello/asse-N-…/`
- dalla pagina `/nota-metodologica/` → linkare agli assi citati

Questo crea un grafo interno coerente: il visitatore può entrare dalla
panoramica o dal capitolo e muoversi tra i due livelli senza perdersi.

## 6. Regole di ordinamento

- Assi: ordinati per `asse_number` (1→6)
- Capitoli all'interno di un asse: ordinati per `chapter` (da
  front-matter)
- Concetti: ordinati per il numero nel testo sorgente (1→12)

## 7. Comportamento stub

I file vuoti o con solo titolo vengono comunque renderizzati come pagina,
ma con:

- componente `StubNotice` al posto del corpo
- `<meta name="robots" content="noindex">`
- nessun link da pagine di indice principali (`/sviluppo-bambino/` e
  `/sviluppo-bambino/assi/`); sì invece dai loro specifici indici
  (`/riflessioni/`, `/interlocuzioni/ambito/`).

## 8. Non fare

- Non riscrivere, riassumere o "divulgare" il testo dei capitoli.
- Non aggiungere glossari se l'utente non li fornisce: il modello è già
  autoesplicito attraverso la sezione Concetti.
- Non raggruppare i 44 capitoli in modo diverso da quello stabilito dagli
  Assi (es. per tema trasversale): si perde la struttura del modello.
- Non modificare il testo dei file `normalized/`: se serve una variante
  editoriale per il web, si discute prima con Stefano.

## 9. Estensibilità

### 9.1 Nuovi capitoli

Quando Stefano aggiunge un nuovo `.md` in una cartella di `normalized/`
(ad es. `Asse 2 - …/Capitolo 9 – …md`):

- Claude Code lo rileva, legge il front-matter, lo inserisce in ordine
  `chapter` nell'indice dell'asse
- il capitolo precedente (prima ultimo) vede il suo `next` aggiornato:
  **questo richiede che Claude Code rigeneri il front-matter prev/next
  al build, non si basi sulla versione committata**. In alternativa, si
  può rieseguire lo script `normalize_assi.py` prima di ogni build.

### 9.2 Nuovi assi

Struttura identica: cartella `Asse 7 - …/` in `normalized/`, con i suoi
capitoli. Lo split del Modello (`01 Modello …`) dovrebbe però essere
aggiornato da Stefano perché contenga la sintesi dell'asse 7.

### 9.3 Nuovi ambiti interdisciplinari

Nuova cartella sotto `interlocuzioni disciplinari/`. Appare come nuova
card nell'indice `/sviluppo-bambino/interlocuzioni/`.

## 10. Sintesi operativa

Al momento del lancio del sito, per la sezione Sviluppo bambino, Claude
Code genera **circa 70 pagine**:

- 1 landing
- 2 pagine "finalità" e "metodo"
- 1 indice modello + 6 sintesi asse = 7 pagine
- 1 pagina concetti
- 1 pagina nota metodologica
- 1 indice assi + 6 indici di asse + 44 capitoli = 51 pagine
- 1 indice riflessioni + N stub
- 1 indice interlocuzioni + M stub (con neuroscienze come primo ambito)

Tutte leggono sorgenti già presenti nel progetto, senza necessità di
contenuti aggiuntivi per la v1.
