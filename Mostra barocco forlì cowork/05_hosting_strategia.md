# Strategia di pubblicazione online
*Come mettere online i materiali della mostra per i tuoi amici*

## Requisiti del progetto

Prima di scegliere, fissiamo cosa ti serve:

1. Sito **statico**: contenuti che non cambiano (checklist PDF + 4 approfondimenti + pagina di presentazione)
2. **Nessuna esigenza di aggiornamento** frequente (lo pubblichi e basta)
3. **Gratis**
4. Tu hai già un **account GitHub**
5. Traffico molto basso (qualche amico, forse una ventina di visite)

In queste condizioni le opzioni principali sono: GitHub Pages, Cloudflare Pages, Netlify. Le escludo tutte le altre (Vercel è overkill, Surge.sh è ok ma meno diffuso, i cPanel classici non servono per uno statico).

## Confronto sintetico

| Caratteristica | GitHub Pages | Cloudflare Pages | Netlify |
|---|---|---|---|
| **Setup** | Semplicissimo se usi già GitHub | Semplice ma devi creare un account Cloudflare | Semplice (drag & drop o GitHub) |
| **Costo** | Gratis | Gratis | Gratis |
| **Dominio personalizzato** | Sì, HTTPS automatico | Sì, HTTPS automatico | Sì, HTTPS automatico |
| **Limiti gratuiti** | 1 GB di spazio, 100 GB/mese di banda | **Banda illimitata**, 500 build/mese | 100 GB/mese di banda, 100 minuti di build/mese |
| **Repository pubblico richiesto** | Sì (nella versione gratuita) | No | No |
| **Workflow** | Push su repo → pubblicato | Collega repo o upload cartella | Collega repo o upload cartella |

## Raccomandazione

**→ GitHub Pages.**

Motivo: tu hai già un account GitHub, i contenuti sono pubblici per natura (vuoi condividerli con gli amici), lo spazio necessario è ridicolo rispetto al limite (un PDF di 200 KB e quattro file HTML di pochi KB ciascuno pesano in totale meno di 1 MB), e la banda di 100 GB/mese è comunque enormemente più di quanto servirà. Soprattutto: **il flusso è il più semplice possibile**. Crei un repository, carichi i file, attivi GitHub Pages, e il sito è online all'indirizzo `https://<tuo-username>.github.io/<nome-repo>/`.

**Cloudflare Pages** sarebbe preferibile solo se prevedessi traffico altissimo o volessi condividere più siti: non è il tuo caso.

**Netlify** funziona bene ma aggiunge un account in più e, dal 2025, ha ridotto i minuti di build gratuiti: per un sito statico semplice non c'è nessun vantaggio rispetto a GitHub Pages.

## Come procederemo

1. Ti preparo un **prompt di istruzioni per Claude Code** (file `06_istruzioni_per_claude_code.md`) che gli dice come costruire il sito statico a partire dai nostri materiali.
2. Tu avvii Claude Code nella cartella di progetto e gli dai quel prompt.
3. Claude Code genera la cartella `site/` con HTML, CSS, PDF copiato, tutto pronto.
4. Tu crei un repository pubblico su GitHub (es. `mostra-barocco-forli`).
5. Carichi il contenuto di `site/` sulla branch `main` del repo.
6. Nelle impostazioni del repo → **Pages**, scegli "Deploy from a branch" → `main` → `/ (root)`.
7. In pochi minuti il sito è online all'indirizzo `https://<tuo-username>.github.io/mostra-barocco-forli/` da condividere con gli amici.

## Note sulla licenza e l'attribuzione

Trattandosi di testi originali che abbiamo elaborato a partire da fonti pubbliche (comunicati di stampa, Treccani, articoli divulgativi), il sito è perfettamente condivisibile. Conviene comunque:

- Includere nel footer una **nota** del tipo: "Materiali preparati per un uso personale di visita alla mostra. Le opere citate e le immagini eventuali sono di proprietà dei rispettivi detentori."
- Inserire i **link alle fonti** consultate (le abbiamo già nei documenti).
- **Non includere immagini** delle opere senza averne verificato i diritti. Il sito che generiamo sarà solo testuale + un PDF nostro — niente immagini di opere d'arte — per evitare problemi.

## Fonti consultate

- [GitHub Docs — What is GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Docs — Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [HowToGeek — Why GitHub Pages is the best option for most free websites](https://www.howtogeek.com/heres-why-github-pages-is-the-best-option-for-most-free-websites/)
- [DanubeData — Cloudflare Pages vs Netlify vs Vercel 2026](https://danubedata.ro/blog/cloudflare-pages-vs-netlify-vs-vercel-static-hosting-2026)
- [Hosted.md — GitHub Pages vs Netlify vs Cloudflare Pages for Markdown Sites](https://hosted.md/blog/github-pages-vs-netlify-vs-cloudflare-pages-which-is-best-for-markdown-sites)
