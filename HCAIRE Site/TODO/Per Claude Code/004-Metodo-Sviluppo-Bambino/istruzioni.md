---
azione: "004"
nome: "Sottosezione Progetti / Sviluppo Bambino / Metodo"
stato: "pronto per Claude Code"
priorità: "alta"
dipendenze: "nessuna"
data: "2026-04-20"
---

# Azione 004 — Metodo del progetto Sviluppo Bambino

## Contesto

La pagina `/sviluppo-bambino/metodo/` va **sostituita e ampliata** in una
sottosezione navigabile con gerarchia a due livelli: una landing index e
cinque pagine di contenuto organizzate in tre aree tematiche.

Il materiale sorgente è distribuito in tre cartelle all'interno di:

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/
```

---

## Struttura URL risultante

```
/sviluppo-bambino/metodo/                                        ← landing index (NUOVO)
  /sviluppo-bambino/metodo/introduzione/                         ← index gruppo 1 (NUOVO)
    /sviluppo-bambino/metodo/introduzione/architettura/          ← pagina (NUOVO)
    /sviluppo-bambino/metodo/introduzione/metodologia/           ← pagina (NUOVO)
  /sviluppo-bambino/metodo/ricerca-scientifica/                  ← index gruppo 2 (NUOVO)
    /sviluppo-bambino/metodo/ricerca-scientifica/collocazione/   ← pagina (NUOVO)
    /sviluppo-bambino/metodo/ricerca-scientifica/statuto-epistemologico/ ← pagina (NUOVO)
  /sviluppo-bambino/metodo/rapporto-con-ia/                     ← pagina diretta (NUOVO)
```

Il gruppo 3 ha un solo documento: non genera un indice intermedio, ma una
pagina diretta all'URL `/sviluppo-bambino/metodo/rapporto-con-ia/`.

---

## Intervento 1 — Landing `/sviluppo-bambino/metodo/`

### Fonte del contenuto

```
HCAIRE Site/TODO/Sezione Sviluppo Bambino/Metodo - landing.md
```

### Front-matter

```yaml
---
title: "Il metodo"
section: "sviluppo-bambino"
type: "index"
slug: "metodo"
order: 2
excerpt: "L'architettura metodologica stratificata che guida il progetto: dall'ontologia agli strumenti operativi, nel confronto con la ricerca scientifica e con l'intelligenza artificiale."
---
```

### Contenuto della pagina

1. Testo da `Metodo - landing.md` (intro + tre sezioni "Tre aree di
   documentazione")
2. Griglia di card verso le tre aree:
   - **Introduzione al progetto** → `/sviluppo-bambino/metodo/introduzione/`
     excerpt: "L'architettura in sette livelli e la metodologia del progetto."
   - **Rapporto con la ricerca scientifica** → `/sviluppo-bambino/metodo/ricerca-scientifica/`
     excerpt: "Il posizionamento epistemologico rispetto alla ricerca empirica."
   - **Rapporto con l'intelligenza artificiale** → `/sviluppo-bambino/metodo/rapporto-con-ia/`
     excerpt: "Il rationale dell'uso dell'AI come supporto cognitivo al progetto."

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo
```

---

## Intervento 2 — Index gruppo 1: `/sviluppo-bambino/metodo/introduzione/`

### Front-matter

```yaml
---
title: "Introduzione al progetto"
section: "sviluppo-bambino"
type: "index"
slug: "introduzione"
parent: "metodo"
order: 1
excerpt: "L'architettura in sette livelli e la metodologia del progetto Sviluppo Bambino."
---
```

### Contenuto

Griglia di card verso le due sottopagine:

- **Architettura del progetto** → `/sviluppo-bambino/metodo/introduzione/architettura/`
  excerpt: "I sette livelli progressivi dal fondamento ontologico alla stabilizzazione istituzionale."
- **Metodologia** → `/sviluppo-bambino/metodo/introduzione/metodologia/`
  excerpt: "Il percorso strutturato e stratificato dalla fondazione concettuale agli strumenti operativi."

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Introduzione al progetto
```

---

## Intervento 3 — Pagina `/sviluppo-bambino/metodo/introduzione/architettura/`

### Fonte

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/01 Introduzione/01 Architettura del Progetto Sviluppo Bambino.md
```

Il file è già pulito (nessuna ancora Google Docs, nessun `\-` nelle heading).

### Front-matter

```yaml
---
title: "Architettura del progetto Sviluppo Bambino"
section: "sviluppo-bambino"
type: "page"
slug: "architettura"
parent: "introduzione"
order: 1
excerpt: "I sette livelli progressivi: dalla fondazione ontologica alla stabilizzazione istituzionale."
---
```

### Note di rendering

- Il documento ha `###` heading (Funzione, Assunto centrale, Obiettivo,
  Output) sotto ciascun livello F1–F6: tutte devono comparire nel TOC.
- La tabella "Livelli isomorfi" va renderizzata come tabella standard.
- La sequenza con frecce `↓` nella sezione "Relazione tra i livelli" va
  mantenuta come testo preformattato o con stile `<pre>` se il motore non
  la preserva automaticamente.

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Introduzione al progetto > Architettura
```

### Navigazione

- Prev: disattivato (prima pagina del gruppo)
- Next: `/sviluppo-bambino/metodo/introduzione/metodologia/`

---

## Intervento 4 — Pagina `/sviluppo-bambino/metodo/introduzione/metodologia/`

### Fonte

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/01 Introduzione/02 Metodologia del progetto Sviluppo del bambino.md
```

### Front-matter

```yaml
---
title: "Metodologia del progetto"
section: "sviluppo-bambino"
type: "page"
slug: "metodologia"
parent: "introduzione"
order: 2
excerpt: "Il percorso strutturato e stratificato che regola il passaggio dalla fondazione concettuale alla progettazione degli strumenti."
---
```

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Introduzione al progetto > Metodologia
```

### Navigazione

- Prev: `/sviluppo-bambino/metodo/introduzione/architettura/`
- Next: disattivato (ultima pagina del gruppo)

---

## Intervento 5 — Index gruppo 2: `/sviluppo-bambino/metodo/ricerca-scientifica/`

### Front-matter

```yaml
---
title: "Rapporto con la ricerca scientifica"
section: "sviluppo-bambino"
type: "index"
slug: "ricerca-scientifica"
parent: "metodo"
order: 2
excerpt: "Il posizionamento epistemologico del progetto rispetto all'ecosistema della ricerca empirica."
---
```

### Contenuto

Griglia di card verso le due sottopagine:

- **Collocazione nell'ecosistema della ricerca** → `/sviluppo-bambino/metodo/ricerca-scientifica/collocazione/`
  excerpt: "Come il progetto si situa rispetto alla produzione di conoscenza empirica sullo sviluppo umano."
- **Statuto epistemologico** → `/sviluppo-bambino/metodo/ricerca-scientifica/statuto-epistemologico/`
  excerpt: "Il progetto come infrastruttura metodologica e concettuale a livello metateorico."

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Rapporto con la ricerca scientifica
```

---

## Intervento 6 — Pagina `/sviluppo-bambino/metodo/ricerca-scientifica/collocazione/`

### Fonte

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/02 rapporto con ricerca scientifica/OM5 - Collocazione del progetto "Sviluppo Bambino" nell'ecosistema della ricerca scientifica.md
```

### Front-matter

```yaml
---
title: "Collocazione nell'ecosistema della ricerca scientifica"
section: "sviluppo-bambino"
type: "page"
slug: "collocazione"
parent: "ricerca-scientifica"
order: 1
excerpt: "Come il progetto si situa rispetto alla produzione di conoscenza empirica sullo sviluppo umano."
---
```

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Rapporto con la ricerca scientifica > Collocazione
```

### Navigazione

- Prev: disattivato (prima pagina del gruppo)
- Next: `/sviluppo-bambino/metodo/ricerca-scientifica/statuto-epistemologico/`

---

## Intervento 7 — Pagina `/sviluppo-bambino/metodo/ricerca-scientifica/statuto-epistemologico/`

### Fonte

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/02 rapporto con ricerca scientifica/OM5b - Statuto epistemologico del progetto "Sviluppo Bambino" nell'ecosistema della ricerca scientifica.md
```

### Front-matter

```yaml
---
title: "Statuto epistemologico del progetto"
section: "sviluppo-bambino"
type: "page"
slug: "statuto-epistemologico"
parent: "ricerca-scientifica"
order: 2
excerpt: "Il progetto come infrastruttura metodologica e concettuale collocata a livello metateorico rispetto alla ricerca empirica."
---
```

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Rapporto con la ricerca scientifica > Statuto epistemologico
```

### Navigazione

- Prev: `/sviluppo-bambino/metodo/ricerca-scientifica/collocazione/`
- Next: disattivato (ultima pagina del gruppo)

---

## Intervento 8 — Pagina `/sviluppo-bambino/metodo/rapporto-con-ia/`

### Fonte

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/metodo/03 rapporto con ia/OM3 - Rationale metodologico del supporto cognitivo basato su AI al progetto "Sviluppo del bambino" (1).md
```

Questa pagina è diretta (nessun indice intermedio): il gruppo 3 ha un solo
documento.

### Front-matter

```yaml
---
title: "Rapporto con l'intelligenza artificiale"
section: "sviluppo-bambino"
type: "page"
slug: "rapporto-con-ia"
parent: "metodo"
order: 3
excerpt: "Il rationale metodologico dell'uso dell'AI come supporto cognitivo alla coerenza, alla traduzione interdisciplinare e alla generazione controllata degli output."
---
```

### Breadcrumb

```
Home > Sviluppo bambino > Il metodo > Rapporto con l'intelligenza artificiale
```

### Navigazione

Nessun Prev/Next (pagina singola del suo gruppo, stessa profondità degli
index di gruppo — non va in sequenza con le pagine degli altri gruppi).

---

## Componenti condivisi su tutte le pagine di questa azione

- **TOC sidebar**: attiva su tutte le pagine `type: "page"`, non sugli index.
- **AgenticLabel**: applicare `<AgenticLabel />` su tutte le pagine
  `type: "page"` di questa azione.
- **Breadcrumb**: come specificato per ciascuna pagina.
- **"← Torna a …"**: in fondo a ogni pagina, link al nodo padre diretto.

---

## Checklist di verifica

- [ ] Landing `/sviluppo-bambino/metodo/` accessibile con le 3 card verso i
      gruppi tematici
- [ ] Index `/sviluppo-bambino/metodo/introduzione/` con 2 card funzionanti
- [ ] Pagina `architettura/` con tabella e sequenza frecce renderizzate
      correttamente
- [ ] Pagina `metodologia/` con contenuto integrale
- [ ] Index `/sviluppo-bambino/metodo/ricerca-scientifica/` con 2 card
- [ ] Pagina `collocazione/` con contenuto integrale
- [ ] Pagina `statuto-epistemologico/` con contenuto integrale
- [ ] Pagina `/sviluppo-bambino/metodo/rapporto-con-ia/` con contenuto
      integrale
- [ ] Breadcrumb corretto su tutte le pagine
- [ ] Navigazione Prev/Next corretta sui gruppi 1 e 2
- [ ] TOC sidebar attiva su tutte le pagine `type: "page"`
- [ ] `<AgenticLabel />` presente su tutte le pagine `type: "page"`
- [ ] Nessun testo sorgente riscritto o parafrasato

---

## Note operative

- Il file `01 Architettura del Progetto Sviluppo Bambino.md` è già pulito
  (i `\-` nelle heading sono stati rimossi prima della consegna a Claude Code).
- Non aggiungere testo di raccordo tra un documento e l'altro: ogni pagina
  è autonoma e il suo contenuto è già completo.
- La sotto-navigazione della sezione `/sviluppo-bambino/` va aggiornata per
  riflettere la nuova struttura gerarchica del nodo `metodo/`.
