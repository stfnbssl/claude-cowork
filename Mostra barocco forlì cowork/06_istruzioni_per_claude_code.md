# Istruzioni per Claude Code
*Brief per generare il sito statico "Bird-watching artistico — Barocco a Forlì 2026"*

> **Come usare questo file:** apri Claude Code nella cartella `C:\Users\nnmrd\Documents\Claude\Projects\Mostra barocco forlì\` e incolla nel prompt l'intero contenuto sotto la riga "INIZIO PROMPT". Claude Code si occuperà di leggere i file di partenza e generare la cartella `site/`. Poi seguirai le istruzioni di pubblicazione in fondo a questo documento.

---

## INIZIO PROMPT (incolla questo a Claude Code)

Sei nella cartella di un progetto che contiene materiali pronti su una mostra d'arte. Il tuo compito è costruire un **sito statico semplice, elegante e leggibile** da pubblicare su GitHub Pages, a partire dai file già presenti.

### File di partenza (già nella cartella)

- `00_pianificazione.md` — documento interno di lavoro (NON pubblicarlo nel sito)
- `01_approfondimento_committenza.md` — testo da convertire in pagina HTML
- `02_approfondimento_mitologia.md` — testo da convertire in pagina HTML
- `03_approfondimento_tecniche_espressive.md` — testo da convertire in pagina HTML
- `04_approfondimento_iconografia_sacra.md` — testo da convertire in pagina HTML
- `05_hosting_strategia.md` — documento interno di lavoro (NON pubblicarlo)
- `06_istruzioni_per_claude_code.md` — questo file (NON pubblicarlo)
- `Checklist Barocco Forli - bird-watching artistico.pdf` — PDF da copiare nel sito e linkare per il download
- `Checklist Barocco Forli - bird-watching artistico.docx` — versione Word, NON pubblicarla

### Struttura del sito da generare

Crea una sottocartella `site/` con questa struttura:

```
site/
├── index.html              ← home page
├── committenza.html        ← da 01_approfondimento_committenza.md
├── mitologia.html          ← da 02_approfondimento_mitologia.md
├── tecniche.html           ← da 03_approfondimento_tecniche_espressive.md
├── iconografia-sacra.html  ← da 04_approfondimento_iconografia_sacra.md
├── checklist.pdf           ← copia del PDF (rinominato senza spazi)
├── style.css               ← unico foglio di stile per tutte le pagine
└── README.md               ← brevi istruzioni per chi guarda il repo
```

### Requisiti del sito

**Tecnologie:** HTML5 statico + un singolo file CSS. Niente JavaScript, niente build tools, niente framework. Deve funzionare da semplice apertura di file nel browser e da GitHub Pages senza configurazioni speciali.

**Compatibilità:** mobile-first, responsive. Deve essere leggibile bene su telefono, tablet e desktop. Niente font esterni che richiedano connessione (usa stack di sistema): l'utente potrebbe consultarlo in mostra con segnale debole.

**Lingua:** italiano. Imposta `<html lang="it">`.

**Encoding:** UTF-8 ovunque (i file di partenza contengono accentate e caratteri speciali).

### Design e tono

Il sito deve riflettere il tono "elegante, sobrio, da quaderno di campo" della checklist. Riferimenti cromatici (allineati al PDF):

- Colore primario (titoli, accenti): `#5A2A00` (marrone barocco scuro)
- Colore secondario (sopratitoli, righe sottili): `#8A6A4A` (oro spento)
- Sfondo riquadri "chiave": `#FBF1E4` (avorio caldo)
- Bordi riquadri: `#D8B48C` (cuoio chiaro)
- Testo: nero su sfondo bianco/avorio chiaro
- Link: stesso marrone primario, sottolineati al hover

**Font:** stack di sistema serif per i titoli (`'Iowan Old Style', 'Palatino Linotype', Georgia, serif`) e sans-serif per il corpo (`-apple-system, 'Segoe UI', system-ui, sans-serif`). Niente Google Fonts.

**Larghezza massima della colonna di lettura:** circa 720px, centrata. Sui mobili occupa tutta la larghezza con 16px di padding laterale. Riga di lettura comoda (interlinea ~1.6).

### Contenuto delle pagine

#### `index.html` — Home page

Da generare ex-novo (non c'è un md sorgente specifico). Contenuti:

1. **Hero** in cima: titolo grande "BAROCCO. Il Gran Teatro delle Idee", sottotitolo "Una guida tematica per la visita alla mostra di Forlì (21 febbraio – 28 giugno 2026)". Riga sotto: "preparato per gli amici curiosi".
2. **Paragrafo introduttivo** (~150 parole) di tono familiare. Spiega cosa è la mostra (Musei San Domenico di Forlì, oltre 200 opere divise in 10 sezioni, dialogo Seicento-Novecento) e cosa è questo materiale (una checklist da bird-watching artistico + 4 approfondimenti tematici per leggere meglio i quadri durante la visita).
3. **Box prominente** con titolo "📋 La checklist da portarsi appresso" e un grosso pulsante/link "Scarica il PDF (15 pagine, A4)" che linka a `checklist.pdf`. Aggiungi una riga di descrizione: "Mini-glossario tecnico e iconografico, chiavi di lettura trasversali, e una scheda per ciascuna delle 10 sezioni della mostra. Da stampare e piegare come quaderno di campo."
4. **Sezione "Approfondimenti tematici"** con 4 card o blocchi linkati:
   - "La committenza barocca" → `committenza.html` (con riga sintetica: "Chi ordinava i quadri, e perché contavano tanto i temi")
   - "La mitologia nella pittura barocca" → `mitologia.html` ("Miti, allegorie, e come riconoscerli")
   - "Le modalità espressive del Barocco" → `tecniche.html` ("Come riconoscere lo stile di un'epoca e dei singoli autori")
   - "L'iconografia sacra barocca" → `iconografia-sacra.html` ("Santi, Madonne, estasi, martiri: come riconoscerli")
5. **Footer** con: "Testi originali a cura di Stefano (con l'aiuto di Claude di Anthropic), aprile 2026 · Materiali per uso personale di visita · Le opere citate e i loro detentori restano dei rispettivi proprietari." Includi un piccolo link "Codice sorgente del sito" che punta al repository GitHub (lascia un placeholder `<URL_REPOSITORY>` che Stefano sostituirà dopo aver creato il repo).

#### Pagine di approfondimento (`committenza.html`, `mitologia.html`, `tecniche.html`, `iconografia-sacra.html`)

Per ognuna:

1. **Header del sito** con logo testuale "Barocco a Forlì" che linka a `index.html`, e una piccola nav con i 4 approfondimenti.
2. **Titolo e sottotitolo della pagina** presi dal markdown sorgente (le righe `# Titolo` e `*Sottotitolo*` iniziali).
3. **Il contenuto del markdown convertito in HTML semantico:**
   - `#` → `<h1>` (uno solo per pagina, è già stato gestito dal titolo)
   - `##` → `<h2>`
   - `###` → `<h3>`
   - `####` → `<h4>`
   - Liste puntate `-` → `<ul><li>`
   - Liste numerate → `<ol><li>`
   - **Grassetto** → `<strong>`
   - *Italic* → `<em>`
   - I paragrafi normali → `<p>`
   - I separatori `---` → `<hr>`
   - I `> blockquote` (se ce ne sono) → `<blockquote>`
4. **Box "Cosa cercare nella mostra di Forlì"**: nei file `01_…`, `02_…`, `03_…`, `04_…` c'è una sezione finale con questo titolo (o simile). Mettila in un riquadro evidenziato (sfondo `#FBF1E4`, bordo `#D8B48C`, padding 1.5em, margine verticale 2em).
5. **Footer con navigazione**: link "← Torna all'indice" + link agli altri 3 approfondimenti.

> **Importante sulla conversione markdown→HTML:** non usare un modulo npm/pip; processa i file in modo programmatico (uno script Python o Node monouso che lanci tu, oppure scrittura diretta dell'HTML leggendo il markdown). I markdown sono puliti — non hanno tabelle né immagini — quindi il parser non deve essere sofisticato. L'importante è che l'HTML sia ben formato e validi.

#### `style.css`

Un singolo foglio. Includi: reset minimo, tipografia (font, line-height, font-size responsive), layout della colonna centrale, header/nav, hero della home, box "chiave" (con bordo cuoio e sfondo avorio), card degli approfondimenti, blockquote, hr stile barocco, link sottolineati con colore primario, footer attenuato, media query mobile. Mantieni il file sotto le 200 righe — deve restare leggibile.

#### `README.md`

Un README breve nel repo con: titolo del progetto, una riga di descrizione, link al sito pubblicato (placeholder `<URL_SITO>` che Stefano sostituirà), nota sulla licenza ("Testi originali, uso personale; le opere d'arte citate restano dei rispettivi detentori").

### Checklist di qualità (verifica prima di consegnare)

- [ ] La cartella `site/` esiste con tutti i file elencati sopra
- [ ] Ho copiato il PDF originale rinominato come `checklist.pdf` in `site/`
- [ ] L'HTML è ben formato (passa una validazione W3C, anche manuale)
- [ ] Ho impostato `<html lang="it">` su tutte le pagine
- [ ] Ho impostato `<meta charset="UTF-8">` su tutte le pagine
- [ ] Ho impostato `<meta name="viewport" content="width=device-width, initial-scale=1">` per il mobile
- [ ] I link interni (es. `committenza.html`) sono **relativi** e funzionano sia in apertura locale sia da sottocartella di GitHub Pages
- [ ] Ho aggiunto un favicon o un placeholder `<link rel="icon" href="data:,">` per evitare il warning 404 dei browser
- [ ] Ho controllato un paio di pagine renderizzate aprendo l'HTML nel browser
- [ ] Tutto il testo italiano si vede correttamente (accenti, virgolette tipografiche)
- [ ] I file `00_…`, `05_…`, `06_…` e il `.docx` NON sono finiti nella cartella `site/`

### Output finale

Quando hai finito, mostrami:

1. La struttura della cartella `site/` (tipo `tree site/`)
2. Una riga di sintesi: "Sito generato. N pagine HTML, M KB totali, pronto per essere caricato su GitHub Pages."
3. Eventuali warning o decisioni di design che hai dovuto prendere.

## FINE PROMPT

---

## Cosa fare dopo che Claude Code ha generato il sito

### 1. Verifica locale

Apri `site/index.html` con un doppio click nel browser. Controlla che:
- la home si veda bene
- i link agli approfondimenti funzionino
- il pulsante "Scarica il PDF" scarichi/apra il PDF
- una pagina di approfondimento (es. mitologia) sia leggibile e impaginata bene

Se qualcosa non va, fai una nuova chiamata a Claude Code con il problema specifico.

### 2. Crea il repository su GitHub

1. Vai su [github.com/new](https://github.com/new)
2. Nome del repository: `mostra-barocco-forli` (o quello che preferisci)
3. **Public** (necessario per GitHub Pages gratuito)
4. Non aggiungere README/license/.gitignore (non servono)
5. Click su "Create repository"

### 3. Carica i file

Modo più semplice (drag & drop nel browser):
1. Nella pagina del repo appena creato, click su "uploading an existing file"
2. Trascina nella pagina **il contenuto della cartella `site/`** (i singoli file, non la cartella stessa)
3. Scrivi un commit message tipo "Pubblicazione iniziale del sito"
4. Click "Commit changes"

(In alternativa, se preferisci la riga di comando: `git init`, `git add .`, `git commit -m "..."`, `git remote add origin ...`, `git push`.)

### 4. Attiva GitHub Pages

1. Nel repo, vai su **Settings** (ingranaggio in alto a destra)
2. Sezione **Pages** nel menu di sinistra
3. Sotto "Source", scegli **"Deploy from a branch"**
4. Branch: **`main`**, folder: **`/ (root)`**
5. Click **Save**

### 5. Aspetta 1–2 minuti

In alto comparirà un riquadro verde con il link al tuo sito, del tipo:

`https://<tuo-username>.github.io/mostra-barocco-forli/`

Aprilo. Se vedi la home page, sei online! 🎉

### 6. Aggiorna i due placeholder

Nel sito che Claude Code ha generato ci sono due placeholder:
- `<URL_REPOSITORY>` nel footer del sito (link al codice sorgente)
- `<URL_SITO>` nel README del repo

Vai sul tuo repo su GitHub, trova i file `index.html` e `README.md`, click sull'icona della matita per modificarli, sostituisci i placeholder con gli URL reali, salva.

### 7. Condividi il link

Ora puoi mandare il link `https://<tuo-username>.github.io/mostra-barocco-forli/` ai tuoi amici via mail o messaggio.

---

## Cosa fare se vuoi un dominio personalizzato (opzionale)

Se hai un tuo dominio (es. `cognome.it`):

1. Nelle Pages settings del repo, sotto "Custom domain", inserisci `barocco.cognome.it` (o quello che vuoi)
2. Vai dal tuo registrar DNS e aggiungi un record CNAME `barocco` → `<tuo-username>.github.io`
3. Aspetta 5–60 minuti
4. Riattiva nel pannello di GitHub Pages la voce "Enforce HTTPS"

Fine.
