---
title: "Sezione HCAIRE — piano dettagliato"
versione: "0.2"
---

# Sezione HCAIRE — piano dettagliato

Questo documento dettaglia la sezione `/hcaire/` del sito, prevista nel
piano generale (`00 — Piano generale per il sito HCAIRE.md`). Descrive
come trasformare il file `sezioni/hcaire/index.md` in un piccolo
sotto-sito organizzato, mantenendo il testo dell'utente **integralmente**
e senza riscritture.

## 1. Obiettivo della sezione

`/hcaire/` ha il compito di **presentare HCAIRE come ambiente di ricerca**
al visitatore. Quando un utente clicca "HCAIRE" nel menu bar, deve trovare:

1. **che cos'è** HCAIRE (finalità, identità)
2. **come lavora** HCAIRE (il metodo)
3. **che cosa produce** (progetti, ambiente editoriale, strumenti come
   Bartleby)
4. **quale visione di IA** orienta il lavoro

Il tono è istituzionale-editoriale: pulito, sobrio, con hierarchy
tipografica chiara.

## 2. Sorgente unica: `sezioni/hcaire/index.md`

Il file è composto da un H1 ("HCAIRE"), un H2 sottotitolo
("Human Centred Artificial Intelligence Research Environment") e **7 blocchi
tematici** introdotti da un `##`:

| #  | Titolo in index.md                                 | Destinazione                           |
| -- | -------------------------------------------------- | -------------------------------------- |
| 0  | *(H1 + H2 + paragrafi identitari iniziali)*        | `/hcaire/` landing                     |
| 1  | Un metodo                                          | `/hcaire/metodo/`                      |
| 2  | Un progetto fondativo                              | `/hcaire/progetti/` (con link)         |
| 3  | Un ambiente editoriale                             | `/hcaire/ambiente-editoriale/`         |
| 4  | Bartleby                                           | `/hcaire/` landing + CTA → `/bartleby/` |
| 5  | Una intelligenza artificiale orientata alla compr. | `/hcaire/ia-centrata-sull-umano/`      |
| 6  | Un ambiente aperto                                 | landing (coda)                         |

Il testo di ogni blocco viene trasferito **letteralmente** nella pagina
di destinazione, con l'aggiunta di:

- front-matter (vedi § 3)
- breadcrumb automatico
- link "← Torna a HCAIRE" in calce

**Nota sul blocco "Bartleby"**: non genera una sottopagina in
`/hcaire/`. Il paragrafo descrittivo resta nella landing come
presentazione dello strumento, con un CTA "Scopri Bartleby →" verso
la sezione top-level `/bartleby/`, gestita direttamente da Claude Code.


## 3. Pagine della sezione — struttura e front-matter

### 3.1 `/hcaire/` (landing)

```yaml
---
title: "HCAIRE"
subtitle: "Human Centred Artificial Intelligence Research Environment"
section: "hcaire"
type: "landing"
slug: ""
order: 0
---
```

Contenuto:

1. hero con titolo + sottotitolo
2. i due paragrafi iniziali di `index.md` (quelli sotto "HCAIRE")
3. griglia di card verso le sottopagine (`metodo`, `ambiente-editoriale`,
   `progetti`, `ia-centrata-sull-umano`)
4. blocco testuale "Bartleby" (paragrafo integrale di `index.md`) con
   CTA "Scopri Bartleby →" che punta a `/bartleby/` (sezione
   top-level, fuori piano)
5. chiusura con il testo della sezione "Un ambiente aperto"
   (invito a seguire l'evoluzione del laboratorio)

### 3.2 `/hcaire/metodo/`

```yaml
---
title: "Il metodo HCAIRE"
section: "hcaire"
type: "page"
slug: "metodo"
order: 1
excerpt: "Tre livelli di lavoro: fondazione concettuale, traduzione interdisciplinare, sviluppo di strumenti."
---
```

Contenuto: testo integrale del blocco `## Un metodo` di `index.md`.

In calce, se valorizzato, un riquadro "Vedi anche" che linka:
`/sviluppo-bambino/metodo/` (il metodo operativo del primo progetto).

### 3.3 `/hcaire/progetti/`

```yaml
---
title: "Progetti"
section: "hcaire"
type: "index"
slug: "progetti"
order: 2
excerpt: "I progetti di ricerca di HCAIRE."
---
```

Contenuto:

1. testo integrale del blocco `## Un progetto fondativo` di `index.md`
2. card/lista dei progetti noti. Per ora: un'unica card
   **Sviluppo bambino** che linka a `/sviluppo-bambino/`
3. placeholder "Altri progetti in arrivo" (stub, non renderizzato come
   pagina ma come nota testuale).

### 3.4 `/hcaire/ambiente-editoriale/`

```yaml
---
title: "Ambiente editoriale"
section: "hcaire"
type: "page"
slug: "ambiente-editoriale"
order: 3
excerpt: "Blog editoriale, materiali fondativi e comitato scientifico-editoriale."
---
```

Contenuto: blocco `## Un ambiente editoriale` di `index.md`.

Nota: il blog editoriale è **menzionato ma non ancora presente**. La
pagina può chiudere con un piccolo componente
`<ComingSoon feature="blog" />` che informa il visitatore.

### 3.5 `/hcaire/ia-centrata-sull-umano/`

```yaml
---
title: "Una IA orientata alla comprensione"
section: "hcaire"
type: "page"
slug: "ia-centrata-sull-umano"
order: 4
excerpt: "L'IA in HCAIRE come supporto al pensiero, non come sostituto del giudizio."
---
```

Contenuto: blocco `## Una intelligenza artificiale orientata alla
comprensione` di `index.md`.

Questa pagina è **posizionamento**, ha valore identitario forte. Può
essere linkata da vari punti del sito quando si menziona il ruolo dell'IA
nel progetto.

### 3.6 `/hcaire/identita/` *(opzionale)*

Se Stefano preferisce un'entrata "Chi siamo" più esplicita nel menu
secondario della sezione, si può creare una pagina che aggrega i
paragrafi identitari della landing. Altrimenti, la landing stessa svolge
già questa funzione. **Proposta**: non crearla nella v1, valutarla dopo
una passata di review editoriale.

## 4. Navigazione interna alla sezione

Sotto il menu bar principale, `/hcaire/` espone un sotto-menu laterale
(o in alto, sotto l'hero) con le voci in ordine `order`:

- Identità/Landing (`/hcaire/`)
- Il metodo
- Progetti
- Ambiente editoriale
- IA orientata alla comprensione

Su mobile, il sotto-menu collassa in un selector a tendina o in una
bottom-sheet.

Bartleby **non** fa parte del sotto-menu di `/hcaire/`: è una voce
di primo livello del menu bar, gestita da Claude Code. Il riferimento a
Bartleby dentro `/hcaire/` (landing) è solo testuale, con CTA verso
`/bartleby/`.

## 5. Template di pagina condiviso per `/hcaire/*`

Layout suggerito (dall'alto):

1. Menu bar globale (comune a tutto il sito)
2. Breadcrumb: `Home > HCAIRE > [titolo pagina]`
3. Hero compatto con `title` + `subtitle` (se presente)
4. Contenuto `.md` renderizzato
5. Footer di pagina con:
   - "← Torna a HCAIRE" (se pagina interna)
   - tag `section: hcaire` per eventuale footer comune
6. Sidebar di navigazione laterale (solo desktop) con sotto-menu di
   `/hcaire/`

## 6. Non fare

- Non spezzare il testo dell'utente in sotto-paragrafi diversi da come
  è scritto. Le H2 del file sorgente restano H2 delle pagine.
- Non aggiungere paragrafi descrittivi di "riempimento" tra un blocco e
  l'altro: se serve una transizione, va concordata con Stefano.
- Non usare emoji, icone decorative o immagini stock: la linea grafica è
  **sobria**.

## 7. Estensibilità futura

Quando HCAIRE acquisirà altri progetti oltre Sviluppo bambino:

- un nuovo folder `sezioni/progetti/<nome>/` genera automaticamente una
  nuova card in `/hcaire/progetti/`
- la card richiede almeno un file `index.md` con `title` + `excerpt` nel
  front-matter

Quando partirà il blog editoriale:

- nuova cartella `sezioni/blog/` con post in markdown
- aggiunta di `/hcaire/ambiente-editoriale/blog/` come feed
- eventuale promozione del blog nella home page

Questi scenari non sono nel perimetro della v1 ma vanno tenuti presenti
nell'architettura: la sitemap e le cartelle devono essere predisposte per
accoglierli senza rifattorizzazioni.
