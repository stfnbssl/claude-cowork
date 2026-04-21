---
azione: "001"
nome: "Adozione Agentic Shift"
stato: "pronto per Claude Code"
priorità: "alta"
dipendenze: "nessuna"
data: "2026-04-19"
---

# Azione 001 — Adozione Agentic Shift

## Contesto

HCAIRE è sviluppato tramite un processo di AI Orchestration (Agentic Workflow).
Questa azione rende esplicita e trasparente questa scelta all'interno del sito,
attraverso due interventi distinti:

1. **una nuova pagina** nella sezione `/hcaire/` che illustra il paradigma
2. **elementi di trasparenza globali** (footer, badge, label) che compaiono
   in tutto il sito con link alla nuova pagina

---

## Intervento 1 — Nuova pagina `/hcaire/agentic-shift/`

### Fonte del contenuto

Il testo della pagina si trova nel file:

```
HCAIRE Site/TODO/Sezione HCAIRE/Agentic shift.md
```

Il contenuto va trasferito **letteralmente**, senza riscritture né aggiunte
di paragrafi. Rispetta le heading esistenti (`##`, `###`) del file sorgente.

### Front-matter da aggiungere

```yaml
---
title: "HCAIRE adotta l'Agentic Shift"
section: "hcaire"
type: "page"
slug: "agentic-shift"
order: 5
excerpt: "Il sito è realizzato tramite un sistema di AI Orchestration. Cos'è l'Agentic Shift e come orienta il lavoro di HCAIRE."
---
```

### URL

```
/hcaire/agentic-shift/
```

### Breadcrumb

```
Home > HCAIRE > HCAIRE adotta l'Agentic Shift
```

### Navigazione interna alla sezione `/hcaire/`

Aggiungere la voce **"Sviluppo Agentico"** (o "Agentic Shift") al sotto-menu
della sezione HCAIRE, in quinta posizione (dopo `ia-centrata-sull-umano`,
`order: 5`).

### Link dalla landing `/hcaire/`

Aggiungere una card nella griglia delle sottopagine della landing `/hcaire/`,
con:
- titolo: "HCAIRE adotta l'Agentic Shift"
- excerpt: estratto dal campo `excerpt` del front-matter sopra
- link: `/hcaire/agentic-shift/`

### Footer di pagina

In calce alla pagina, aggiungere:

```
← Torna a HCAIRE
```

---

## Intervento 2 — Elementi di trasparenza globali

Tutti e tre gli elementi sotto **linkano** alla pagina `/hcaire/agentic-shift/`
con il testo `[Scopri di più]` o equivalente.

### 2.1 Footer fisso (site-wide)

Aggiungere nel footer globale del sito (presente su **tutte** le pagine)
una riga dedicata alla trasparenza agentica:

> Sviluppo Agentico: Questo sito è realizzato tramite processi di AI Orchestration. [Scopri di più →](/hcaire/agentic-shift/)

**Specifiche tecniche:**
- Posizione: nell'area footer globale, separata dagli altri elementi footer.
- Stile: tono sobrio, corpo più piccolo rispetto al testo principale, coerente
  con le convenzioni tipografiche già definite.
- Classe CSS consigliata: `footer-agentic-notice` (per permettere styling
  mirato in futuro).
- Il link `[Scopri di più]` deve essere un anchor tag standard, non un bottone.

### 2.2 Label accanto ai contenuti generati (page-level)

Per le pagine che contengono contenuto generato tramite Agentic Workflow
(inizialmente: tutte le pagine della sezione `/sviluppo-bambino/` e quelle
di `/hcaire/`), aggiungere un'etichetta discreta in fondo al corpo della
pagina, prima del footer di navigazione:

> *Contenuto generato tramite Agentic Workflow e revisionato da un operatore umano.*

**Specifiche tecniche:**
- Posizione: dopo il corpo testo, prima di elementi Prev/Next o "← Torna a".
- Stile: corsivo, corpo ridotto, colore attenuato (es. `text-muted` o
  equivalente nel tema scelto). Nessun bordo o box evidente: deve essere
  presente ma non invadente.
- Classe CSS consigliata: `agentic-label`.
- Il rendering può avvenire tramite un componente `<AgenticLabel />` (o
  equivalente nel template engine scelto) inserito nel layout base dei
  tipi `page` e `chapter`.
- **Non** aggiungere sulle pagine `type: "stub"` (che già hanno il
  componente `StubNotice`).

### 2.3 Badge informativo (site-wide, discreto)

Aggiungere un badge testuale discreto in una zona visibile ma non
invasiva del sito (suggerimento: angolo in alto a destra del menu bar,
oppure subito sotto l'header su mobile):

> Contenuti generati da Agenti AI [Scopri di più →](/hcaire/agentic-shift/)

**Specifiche tecniche:**
- Stile: piccolo, senza elementi visivi pesanti (no icone colorate, no
  animazioni). Coerente con la linea grafica sobria definita nel piano generale.
- Classe CSS consigliata: `agentic-badge`.
- Su mobile: può comparire nel footer invece che nell'header, per non
  congestionare lo spazio limitato.
- **Non** deve sovrapporsi né confondersi con le voci di navigazione del
  menu bar.

---

## Checklist di verifica per questa azione

- [ ] Pagina `/hcaire/agentic-shift/` accessibile e con contenuto integrale
      tratto da `TODO/Sezione HCAIRE/Agentic shift.md`
- [ ] Front-matter corretto sulla nuova pagina
- [ ] Voce "Agentic Shift" presente nel sotto-menu della sezione HCAIRE
- [ ] Card della nuova pagina visibile nella landing `/hcaire/`
- [ ] Breadcrumb corretto su `/hcaire/agentic-shift/`
- [ ] Footer globale mostra la riga di trasparenza con link funzionante
- [ ] Label `AgenticLabel` presente sulle pagine `type: "page"` e `type: "chapter"`
- [ ] Badge informativo visibile e non invasivo nell'header (o footer su mobile)
- [ ] Tutti i link `[Scopri di più]` puntano correttamente a `/hcaire/agentic-shift/`
- [ ] Nessun testo del file sorgente è stato riscritto o parafrasato

---

## Note operative

- Non aggiungere immagini, icone decorative o elementi grafici non richiesti.
- Non riscrivere né parafrasare il testo sorgente di `Agentic shift.md`.
- Il tono degli elementi di trasparenza (footer, badge, label) deve essere
  informativo e sobrio, coerente con la linea editoriale del sito.
- Qualunque dubbio su posizionamento o stile va risolto preferendo la
  soluzione più discreta e non invasiva.
