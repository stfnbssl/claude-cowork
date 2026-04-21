# Come usare le Skill di Claude Cowork per costruire un sistema automatico di generazione articoli

**Generare articoli con l'AI non significa semplicemente chiedere a Claude di "scrivere qualcosa". Significa costruire un sistema: istruzioni strutturate, workflow ripetibili, output coerenti. Le skill di Claude Cowork sono esattamente lo strumento giusto per farlo.**

---

## Cosa sono le Skill di Claude Cowork

Le Skill sono la funzionalità che trasforma Claude da assistente reattivo a sistema attivo. In termini tecnici, una Skill è un file markdown con frontmatter strutturato che Claude Code carica su richiesta e invoca tramite uno slash command — ad esempio `/genera-articolo`. In termini pratici, è un pacchetto di istruzioni persistente e riutilizzabile che definisce come Claude deve comportarsi in un determinato contesto.

Le Skill vivono nella directory `.claude/skills/` del progetto (o nella home per quelle globali) e vengono attivate con linguaggio naturale oppure tramite comando esplicito. Ogni Skill ha una logica di trigger, istruzioni operative, e può orchestrare strumenti esterni, subagent, e altri workflow.

Come sintetizza la [documentazione ufficiale di Claude Code](https://code.claude.com/docs/en/skills): le Skill permettono di "pacchettizzare prompt riutilizzabili come slash command", passando dall'improvvisazione all'automazione strutturata.

---

## Perché usarle per la generazione di contenuti

La generazione di articoli, guide o documentazione è uno dei workflow più adatti a essere skillizzato. I motivi sono precisi:

**Ripetibilità.** Ogni articolo segue sempre le stesse fasi: ricerca fonti, strutturazione outline, scrittura, revisione, metadati SEO. Codificare queste fasi in una Skill significa non doverle rispiegare ogni volta a Claude.

**Consistenza di tono e stile.** Uno dei problemi più comuni nella generazione AI è l'incoerenza stilistica tra articoli diversi. Una Skill con istruzioni esplicite su tono, pubblico target, struttura delle sezioni e lunghezza elimina questa variabilità alla radice.

**Pipeline multi-step.** Come spiega [alexop.dev nella sua guida](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/), le Skill possono orchestrare sequenze di operazioni complesse: "research → scansione codebase → scrittura documento". Per la generazione di articoli, la pipeline diventa: **ricerca → analisi fonti → scrittura → metadata → pubblicazione**.

**Scalabilità.** Una Skill scritta bene funziona ugualmente bene per un articolo o per venti articoli in batch. L'investimento iniziale nella definizione delle istruzioni si ammortizza rapidamente.

---

## Struttura di un sistema basato su Skill

Un sistema di generazione articoli con Claude Cowork si compone di tre elementi che si integrano tra loro.

### 1. Il file CLAUDE.md — il cervello del sistema

Il file `CLAUDE.md` è la memoria contestuale del progetto. Non è una Skill nel senso tecnico, ma è il luogo dove definire le regole generali che Claude applica in ogni sessione: la struttura delle cartelle di output, il formato dei file, i criteri di qualità, le checklist di validazione, le istruzioni per la pubblicazione.

In un sistema di generazione articoli, il `CLAUDE.md` dovrebbe contenere:
- La struttura del file di input (`input_articoli.md`) e i marcatori di separazione tra articoli
- I template di output per `fonti.md`, `articolo.md` e `metadata.json`
- Le regole SEO da applicare (slug, descrizione, tag)
- Le istruzioni di post-generazione (archiviazione, svuotamento del file input)

### 2. Le Skill — i moduli operativi

Le Skill sono i moduli che eseguono le singole fasi del workflow. Per un sistema di generazione articoli, si possono definire Skill specializzate:

- **`/ricerca-fonti`** — dato un topic, esegue query di ricerca web, valuta l'autorevolezza delle fonti e produce il file `fonti.md` nel formato standard
- **`/scrivi-articolo`** — data la lista fonti e i requisiti, scrive l'articolo rispettando tono, struttura e lunghezza specificati
- **`/genera-metadata`** — estrae dall'articolo scritto gli elementi SEO e produce il `metadata.json`
- **`/pubblica`** — legge il `metadata.json` e l'articolo e chiama l'endpoint di pubblicazione del CMS via HTTP

Oppure — soluzione più comune — una singola Skill `/genera-articolo` che orchestra tutte le fasi in sequenza, come una pipeline unica.

### 3. Il file di input strutturato

Il file di input è l'interfaccia utente del sistema. Segue un formato fisso con marcatori come `===== NUOVO ARTICOLO =====` e sezioni standardizzate per contenuti richiesti, tono, pubblico e indicazioni aggiuntive. Questo formato è ciò che la Skill legge come input e trasforma in output strutturato.

---

## Come costruire la Skill di generazione

Una Skill efficace per la generazione di articoli ha questa struttura di base:

```markdown
---
name: genera-articolo
description: Genera un articolo completo da un briefing strutturato in input_articoli.md
triggers:
  - "genera articolo"
  - "scrivi articolo"
  - "/genera-articolo"
---

## Istruzioni

1. Leggi `input_articoli.md` e identifica tutti gli articoli separati dal marcatore
2. Per ogni articolo:
   a. Esegui 3-4 ricerche web sui temi principali
   b. Seleziona almeno 5 fonti autorevoli (di cui 2 primarie)
   c. Salva le fonti in `work/[nome-articolo]/fonti.md`
   d. Scrivi l'articolo rispettando tono, lunghezza e struttura richiesti
   e. Salva l'articolo in `work/[nome-articolo]/articolo.md`
   f. Genera i metadata SEO in `work/[nome-articolo]/metadata.json`
3. Al termine, archivia l'input e svuota `input_articoli.md`
```

Come sottolinea [Castaldo Solutions](https://www.castaldosolutions.it/articles/blog/come-creare-skill-claude-code), la regola d'oro è: **se ti ritrovi a dare le stesse istruzioni tre o più volte, è il momento di farne una Skill**. Le Skill devono essere focalizzate e componibili — meglio tre Skill separate che si integrano bene piuttosto che un'unica Skill monolitica che prova a fare tutto.

---

## Estendere il sistema: subagent e automazioni avanzate

Il sistema può essere potenziato ulteriormente. Con la funzionalità di subagent di Claude Code, è possibile parallelizzare il lavoro: un agente ricerca le fonti mentre un altro abbozza la struttura, riducendo i tempi su batch di articoli.

Il [repository awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) documenta un caso d'uso analogo, il "Book Factory", che replica un'intera pipeline editoriale usando Skill specializzate per ricerca, strutturazione, scrittura, revisione e formattazione — dimostrando che la logica è applicabile ben oltre la dimensione del singolo articolo.

Per la pubblicazione automatica, la Skill può integrarsi con l'API del CMS tramite `curl` o tool MCP dedicati, in modo che il ciclo si chiuda senza intervento manuale: dall'input testuale all'articolo pubblicato.

---

## Il vantaggio concreto rispetto alla generazione one-shot

L'approccio tradizionale — chiedere di volta in volta a Claude di scrivere un articolo — produce risultati variabili e richiede supervisione continua. Il sistema basato su Skill produce risultati prevedibili, documentati e migliorabili iterativamente.

Secondo [Sight AI](https://www.trysight.ai/blog/content-generation-workflow-automation), i sistemi di content automation maturi del 2026 si distinguono per tre caratteristiche: **multi-agent architecture**, **CMS integration** e **autopilot mode**. Le Skill di Claude Cowork permettono di replicare esattamente questo schema a costo quasi zero, senza dipendere da piattaforme proprietarie.

Il formato strutturato dell'input garantisce che ogni articolo riceva lo stesso livello di attenzione. Le Skill garantiscono che il processo venga eseguito sempre nello stesso modo. Il risultato è un sistema editoriale AI che si comporta come un collaboratore affidabile, non come uno strumento imprevedibile.

---

## Conclusione

Le Skill di Claude Cowork non sono solo una funzionalità tecnica: sono il modo in cui si passa dall'uso occasionale dell'AI all'integrazione sistematica nei processi editoriali. Costruire una Skill per la generazione di articoli richiede un investimento iniziale di alcune ore — definire il workflow, scrivere le istruzioni, testare l'output. Il ritorno è un sistema che produce articoli completi, coerenti e ottimizzati per la pubblicazione in modo automatico, ripetibile e scalabile.

Il punto di partenza è semplice: identifica le fasi che ripeti ogni volta che generi un articolo, scrivile in un file markdown strutturato, e invocale con un solo comando.

---

*Fonti: [Claude Code Docs](https://code.claude.com/docs/en/skills) · [Castaldo Solutions](https://www.castaldosolutions.it/articles/blog/come-creare-skill-claude-code) · [alexop.dev](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/) · [Sight AI](https://www.trysight.ai/blog/content-generation-workflow-automation) · [DEV Community](https://dev.to/whoffagents/how-to-build-claude-code-skills-custom-slash-commands-that-actually-work-1nje) · [Martes AI](https://www.martes-ai.com/blog/claude-cowork-guida-completa-automazione-aziendale/) · [BrightCoding](https://blog.brightcoding.dev/2026/04/02/claude-skills-51-ai-skills-that-actually-build-things)*
