---
azione: "002"
nome: "Sottosezione HCAIRE - Protocolli"
stato: "pronto per Claude Code"
priorità: "alta"
dipendenze: "nessuna"
data: "2026-04-19"
---

# Azione 002 — Sottosezione HCAIRE: Protocolli

## Contesto

HCAIRE adotta protocolli metodologici per guidare l'interazione con gli LLM
nei processi di ricerca e produzione dei contenuti. Questa azione crea la
sottosezione `/hcaire/protocolli/` con una landing index e la prima pagina
dedicata a un protocollo specifico.

I protocolli sono progettati per **doppio utilizzo**: possono essere eseguiti
da agenti AI in workflow automatizzati, oppure da operatori del comitato
scientifico-editoriale tramite interazione diretta con un modello linguistico
via chat.

---

## Intervento 1 — Nuova landing `/hcaire/protocolli/`

### Fonte del contenuto

```
HCAIRE Site/TODO/Sezione HCAIRE/Protocolli - landing.md
```

Il testo va trasferito **letteralmente**, senza riscritture.

### Front-matter da aggiungere

```yaml
---
title: "Protocolli"
subtitle: "Strumenti metodologici per la ricerca assistita da AI"
section: "hcaire"
type: "index"
slug: "protocolli"
order: 6
excerpt: "I protocolli metodologici che guidano l'interazione con gli LLM nei processi di ricerca e produzione dei contenuti di HCAIRE."
---
```

### URL

```
/hcaire/protocolli/
```

### Breadcrumb

```
Home > HCAIRE > Protocolli
```

### Contenuto della pagina

1. Hero con titolo + sottotitolo
2. Corpo del testo da `Protocolli - landing.md` (le tre sezioni: intro,
   "A chi sono destinati", "Come crescerà questa sezione")
3. Griglia di card — per ora una sola card:
   - Titolo: **Ricerca Assistita da AI: il metodo "Framework & Deep Dive"**
   - Excerpt: "Un protocollo strutturato in 5 fasi per condurre ricerche
     interdisciplinari con LLM, con strumenti di controllo critico integrati."
   - Link: `/hcaire/protocolli/ricerca-assistita-ai/`

### Navigazione interna alla sezione `/hcaire/`

Aggiungere la voce **"Protocolli"** al sotto-menu della sezione HCAIRE,
in sesta posizione (`order: 6`, dopo `agentic-shift`).

### Card nella landing `/hcaire/`

Aggiungere una card nella griglia della landing `/hcaire/`:
- Titolo: "Protocolli"
- Excerpt: dal campo `excerpt` del front-matter sopra
- Link: `/hcaire/protocolli/`

### Footer di pagina

```
← Torna a HCAIRE
```

---

## Intervento 2 — Nuova pagina `/hcaire/protocolli/ricerca-assistita-ai/`

### Fonte del contenuto

```
HCAIRE Site/TODO/Sezione HCAIRE/Protocollo ricerca assistita AI.md
```

Il file è già normalizzato (nessuna ancora Google Docs, nessun carattere
di escape). Il testo va trasferito **letteralmente**.

### Front-matter da aggiungere

```yaml
---
title: "Ricerca Assistita da AI: il metodo \"Framework & Deep Dive\""
section: "hcaire"
type: "page"
slug: "ricerca-assistita-ai"
parent: "protocolli"
order: 1
version: "2"
excerpt: "Un protocollo strutturato in 5 fasi per condurre ricerche interdisciplinari con LLM, con strumenti di controllo critico integrati."
---
```

### URL

```
/hcaire/protocolli/ricerca-assistita-ai/
```

### Breadcrumb

```
Home > HCAIRE > Protocolli > Ricerca Assistita da AI
```

### Layout della pagina — indicazioni specifiche

Questa pagina è lunga (10 sezioni principali). Applicare le seguenti
scelte di layout:

**TOC laterale (sidebar)**
Il TOC sidebar è essenziale su questa pagina. Deve includere tutte le
voci `##` e `###` del documento. Su desktop deve essere sticky; su
mobile collassabile.

**Riquadro "Utilizzo"**
Subito dopo il titolo e prima del corpo del testo, inserire un riquadro
informativo (componente `<InfoBox />` o equivalente, classe CSS
`infobox-usage`) con il seguente testo:

> *Questo protocollo è progettato per essere eseguito da agenti AI in
> workflow automatizzati, oppure da operatori del comitato
> scientifico-editoriale tramite interazione diretta con un modello
> linguistico.*

Stile: riquadro discreto, bordo sottile o sfondo lievemente differenziato,
corpo in corsivo. Non deve essere invasivo.

**Sezione §9 in evidenza**
La sezione `## 9. Workflow operativo sintetico` contiene la lista dei
9 passi operativi del protocollo. Renderla visivamente più prominente
rispetto alle altre sezioni: ad esempio con un leggero sfondo differenziato
o un bordo laterale, in modo che sia riconoscibile come riferimento rapido
per chi vuole usare il protocollo senza rileggere tutto il documento.
Classe CSS consigliata: `protocol-workflow`.

**Nota versione**
In fondo alla pagina, prima del link "← Torna ai Protocolli", inserire
una riga discreta con la versione del documento:

> *Versione 2 — ultima revisione: 2026-04-19*

Stile: corpo ridotto, colore attenuato.

### Navigazione

In fondo alla pagina:

```
← Torna ai Protocolli
```

(link a `/hcaire/protocolli/`)

Non sono previsti link Prev/Next per ora (è l'unico protocollo disponibile).

### Label AgenticLabel

Applicare il componente `<AgenticLabel />` (introdotto nell'Azione 001)
anche a questa pagina, in quanto contenuto generato tramite Agentic Workflow.

---

## Struttura URL risultante

```
/hcaire/
    └── /hcaire/protocolli/                          ← landing index (NUOVO)
            └── /hcaire/protocolli/ricerca-assistita-ai/   ← primo protocollo (NUOVO)
```

---

## Checklist di verifica per questa azione

- [ ] Pagina `/hcaire/protocolli/` accessibile con il testo di landing integrale
- [ ] Card del protocollo "Framework & Deep Dive" visibile nella landing
      `/hcaire/protocolli/` con link funzionante
- [ ] Voce "Protocolli" presente nel sotto-menu della sezione HCAIRE
- [ ] Card "Protocolli" visibile nella landing `/hcaire/`
- [ ] Breadcrumb corretto su `/hcaire/protocolli/` e su
      `/hcaire/protocolli/ricerca-assistita-ai/`
- [ ] Pagina `/hcaire/protocolli/ricerca-assistita-ai/` accessibile con
      contenuto integrale (10 sezioni presenti)
- [ ] TOC sidebar funzionante sulla pagina del protocollo (voci `##` e `###`)
- [ ] Riquadro "Utilizzo" visibile subito dopo il titolo
- [ ] Sezione §9 "Workflow operativo sintetico" visivamente in evidenza
- [ ] Nota versione presente in fondo alla pagina
- [ ] Link "← Torna ai Protocolli" funzionante
- [ ] `<AgenticLabel />` presente sulla pagina del protocollo
- [ ] Nessun testo del file sorgente è stato riscritto o parafrasato

---

## Note operative

- Il file sorgente `Protocollo ricerca assistita AI.md` è già pulito:
  nessuna ancora `{#...}` da rimuovere, nessun carattere di escape da
  correggere.
- La heading hierarchy del sorgente presenta alcune `##` usate sia per
  le fasi (A, B, C…) sia per le sezioni numerate (1, 2, 3…): mantenerla
  così com'è, senza riorganizzare.
- Non aggiungere immagini, icone decorative o elementi grafici non richiesti.
- Il tono di tutti gli elementi di UI (riquadro, nota versione) deve
  essere sobrio e coerente con la linea editoriale del sito.
