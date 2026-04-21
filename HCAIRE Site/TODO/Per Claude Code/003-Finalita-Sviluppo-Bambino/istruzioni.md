---
azione: "003"
nome: "Sottosezione Progetti / Sviluppo Bambino / Finalità"
stato: "pronto per Claude Code"
priorità: "alta"
dipendenze: "nessuna"
data: "2026-04-20"
---

# Azione 003 — Finalità del progetto Sviluppo Bambino

## Contesto

La pagina `/sviluppo-bambino/finalita/` del sito va **sostituita** con un
nuovo contenuto, più ricco e articolato rispetto a quello attualmente
pubblicato. Il testo sorgente è pronto nel repository.

---

## Intervento — Sostituzione pagina `/sviluppo-bambino/finalita/`

### Fonte del contenuto

```
HCAIRE Site/sezioni/progetti/sviluppo bambino/finalità/01 - Natura e finalità del progetto "Sviluppo del bambino".md
```

Il testo va trasferito **letteralmente**, senza riscritture. Le sezioni in
grassetto (`**Obiettivo N – …**`) sono i sottotitoli della pagina: trattarle
come `###` heading nel rendering, in modo che compaiano nel TOC sidebar.

### Front-matter da applicare

Aggiungere (o sostituire l'esistente) il seguente front-matter:

```yaml
---
title: "Natura e finalità del progetto"
section: "sviluppo-bambino"
type: "page"
slug: "finalita"
order: 1
excerpt: "Il progetto costruisce un impianto teorico capace di sostenere la comprensione dello sviluppo, il dialogo interdisciplinare e la progettazione di strumenti professionali non riduzionisti."
---
```

### URL

```
/sviluppo-bambino/finalita/
```

L'URL non cambia rispetto all'esistente.

### Breadcrumb

```
Home > Sviluppo bambino > Finalità
```

### Heading della pagina

Il file sorgente ha un H1 (`# **Natura e finalità…**`) e cinque blocchi
con sottotitolo in grassetto inline. Claude Code deve convertire quei
grassetti in `###` heading proper, così:

```
# Natura e finalità del progetto "Sviluppo del bambino"

[paragrafo introduttivo]

### Obiettivo 1 – Costruire una grammatica concettuale dello sviluppo
[testo]

### Obiettivo 2 – Rendere possibile un dialogo interdisciplinare controllato
[testo]

### Obiettivo 3 – Fondare la progettazione di strumenti professionali contestualizzati
[testo]

### Obiettivo 4 – Costruire un sistema cognitivo di supporto alla produzione di output basato su AI
[testo]

### Obiettivo 5 – Garantire coerenza e responsabilità nel tempo
[testo]
```

### Componenti di pagina

- **TOC sidebar**: attiva, deve mostrare i 5 obiettivi come voci `###`
- **Breadcrumb**: come sopra
- **AgenticLabel**: applicare il componente `<AgenticLabel />` in fondo al
  corpo della pagina
- **Prev/Next**: mantenere la logica già in uso per la sezione
  `/sviluppo-bambino/`

---

## Checklist di verifica

- [ ] Pagina `/sviluppo-bambino/finalita/` accessibile e aggiornata
- [ ] Testo integrale dei 5 obiettivi presente e non riscritto
- [ ] I 5 sottotitoli "Obiettivo N" sono heading `###` e compaiono nel TOC
- [ ] Front-matter aggiornato
- [ ] Breadcrumb corretto
- [ ] `<AgenticLabel />` presente

---

## Note operative

- Non riscrivere né parafrasare il testo sorgente.
- La conversione da grassetto inline a heading `###` riguarda solo le
  righe `**Obiettivo N – …**`: il resto del testo in grassetto nel corpo
  dei paragrafi va mantenuto come grassetto inline.
