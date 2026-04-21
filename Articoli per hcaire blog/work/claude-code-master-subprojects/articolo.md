# Claude Code e i Portali Complessi: la Strategia Master + Sotto-Progetti

**Sviluppare un portale web con Claude Code può diventare rapidamente dispendioso: troppe funzionalità, troppi file, troppo contesto da gestire in un'unica sessione. Esiste però una strategia documentata — e sempre più adottata nel 2026 — che permette di tenere tutto sotto controllo: un progetto master come punto d'ingresso e tanti sotto-progetti dedicati alle singole funzionalità.**

---

## Il problema: il contesto è la risorsa più preziosa

Chi ha lavorato a lungo con Claude Code su un portale reale lo sa bene: la qualità delle risposte degrada man mano che la sessione avanza. La causa non è il modello, ma la finestra di contesto. Ogni file letto, ogni comando eseguito, ogni correzione apportata occupa spazio. Quando la finestra si riempie, Claude inizia a "dimenticare" istruzioni impartite in precedenza o a commettere errori su codice che aveva già gestito correttamente.

La documentazione ufficiale di Anthropic lo dice esplicitamente: **"The context window is the most important resource to manage."** Questo vale ancora di più per un portale, dove coesistono autenticazione, dashboard, API, notifiche, pannelli di amministrazione e decine di componenti UI.

---

## La soluzione: un'architettura gerarchica di progetti

La risposta non è lavorare su tutto in una volta, ma strutturare il lavoro come farebbe un team di sviluppo umano: un **progetto master** che definisce le regole globali e coordina l'ingresso, più **sotto-progetti separati** per ogni macro-funzionalità.

Questa struttura si implementa in modo nativo in Claude Code grazie al sistema gerarchico dei file `CLAUDE.md`.

---

## Come funziona la gerarchia dei CLAUDE.md

`CLAUDE.md` è il file che Claude legge automaticamente all'avvio di ogni sessione. Quello che molti non sanno è che **possono esistere più CLAUDE.md annidati**, e Claude li carica in modo intelligente:

- **Root del progetto** (`./CLAUDE.md`): caricato sempre, contiene le regole universali che si applicano a tutto il portale — stack tecnologico, convenzioni di naming, workflow di commit, variabili d'ambiente richieste.
- **Sotto-directory** (`./features/auth/CLAUDE.md`, `./features/dashboard/CLAUDE.md`): caricati *on demand*, solo quando Claude lavora con file in quella directory. Contengono il contesto specifico della funzionalità.
- **Home folder** (`~/.claude/CLAUDE.md`): regole personali che si applicano a tutti i progetti sulla macchina.

Questa logica di **lazy loading** è fondamentale: Claude non carica tutto in memoria fin dall'inizio, ma si porta dietro solo il contesto rilevante per il task corrente. Il risultato è una finestra di contesto più pulita e performante.

Secondo [ClaudeArchitect](https://claudearchitect.com/docs/claude-code/claude-code-monorepo/), un file CLAUDE.md sano ha tra le 200 e le 300 righe. Oltre le 500, è il momento di spostare il contenuto nelle sotto-directory o di usare la sintassi `@path/to/file` per importare documentazione esterna in modo condizionale.

---

## La struttura consigliata per un portale

Ecco un esempio concreto di come organizzare un portale con questa strategia:

```
portale/
├── CLAUDE.md                    # Regole globali, stack, workflow
├── .claude/
│   ├── agents/
│   │   ├── security-reviewer.md # Subagente per code review sicurezza
│   │   └── api-designer.md      # Subagente per design delle API
│   └── skills/
│       ├── new-feature.md       # Workflow per aggiungere nuove funzionalità
│       └── deploy-check.md      # Checklist pre-deploy
├── features/
│   ├── auth/
│   │   ├── CLAUDE.md            # Contesto specifico: OAuth, sessioni, token
│   │   └── ...
│   ├── dashboard/
│   │   ├── CLAUDE.md            # Contesto: widget, layout, dati real-time
│   │   └── ...
│   ├── admin/
│   │   ├── CLAUDE.md            # Contesto: permessi, ruoli, audit log
│   │   └── ...
│   └── notifications/
│       ├── CLAUDE.md            # Contesto: WebSocket, push, preferenze
│       └── ...
└── docs/
    ├── architettura.md
    └── api-reference.md
```

Il file `CLAUDE.md` alla root conterrà solo ciò che è universale:

```markdown
# Portale - Regole Globali

## Stack
- Frontend: React 19 + TypeScript strict
- Backend: Node.js + Express
- DB: PostgreSQL con Prisma ORM

## Workflow
- Sempre eseguire `npm run typecheck` dopo modifiche ai tipi
- Branch naming: feature/NOME, fix/NOME
- Test: `npm run test:unit` per test unitari, `npm run test:e2e` per end-to-end

## Architettura
- Ogni funzionalità vive in features/NOME/
- Le API pubbliche di ogni modulo sono esportate da features/NOME/index.ts
- Vietate le dipendenze circolari tra moduli
```

---

## Il "Virtual Monorepo Pattern" per repository separati

Se invece le funzionalità risiedono in **repository Git separati** (scenario comune nei team più strutturati), esiste una strategia documentata da Owen Zanzal su Medium: il **Virtual Monorepo Pattern**.

L'idea è creare un repository "ombrello" che non contiene codice ma solo:
- Un `CLAUDE.md` master con il contesto cross-repo
- Link simbolici o riferimenti ai repository figli
- Documentazione architetturale condivisa
- Script di orchestrazione

Zanzal ha applicato questo pattern a 35 repository, ottenendo a Claude Code un contesto unificato sull'intero sistema — senza dover aprire e chiudere sessioni diverse per ogni repo. Il "progetto master" diventa il punto d'ingresso unico da cui Claude comprende il big picture, per poi immergersi nel dettaglio di ogni sotto-progetto quando necessario.

---

## Subagenti e Agent Teams: sviluppare in parallelo

Una volta strutturato il progetto, Claude Code offre due meccanismi potenti per lavorare su più funzionalità in contemporanea.

### Subagenti

Un **subagente** è un'istanza di Claude che gira in una finestra di contesto separata, esplora file o risponde a domande, e riporta solo i risultati al contesto principale. Ideale per investigazioni:

```
Usa un subagente per analizzare come il modulo auth gestisce il refresh 
dei token, e dimmi se esistono utility OAuth riutilizzabili.
```

Il subagente legge decine di file senza sporcare la sessione principale. Il contesto master rimane pulito per le decisioni architetturali.

### Agent Teams

Per task più ambiziosi, Claude Code introduce gli **Agent Teams** — ancora sperimentali ma sempre più usati nel 2026. Un agente "team lead" coordina più agenti "teammate", ognuno con il proprio contesto e i propri tool. I teammate possono:

- Lavorare in parallelo su funzionalità indipendenti
- Condividere una task list con dependency tracking
- Comunicare tra loro via messaggistica peer-to-peer
- Usare il file locking per evitare conflitti sugli stessi file

Un esempio pratico: mentre un agente implementa il modulo di autenticazione, un secondo costruisce i componenti della dashboard, e un terzo scrive i test di integrazione. Il team lead coordina, gestisce le dipendenze e mergia i risultati.

---

## Esiste documentazione ufficiale su questa strategia?

Sì. Anthropic ha pubblicato documentazione diretta su diversi aspetti di questa architettura:

- **[Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)**: copre la gestione della finestra di contesto, la gerarchia dei CLAUDE.md, l'uso di subagenti e le sessioni parallele.
- **[Agent Teams](https://code.claude.com/docs/en/agent-teams)**: guida ufficiale all'orchestrazione multi-agente.
- **[Extend Claude Code](https://code.claude.com/docs/en/features-overview)**: panoramica su skills, subagents, hooks e plugin — tutti strumenti utili per la gestione di un portale complesso.

Esistono inoltre risorse della community che documentano pattern specifici per monorepo e multi-repo, come le guide su [ClaudeArchitect](https://claudearchitect.com/docs/claude-code/claude-code-monorepo/) e [ClaudeLab](https://claudelab.net/en/articles/claude-code/claude-code-monorepo-turborepo-workspace-guide).

---

## Checklist per iniziare

Se stai iniziando a strutturare un portale con questa strategia, ecco un punto di partenza pratico:

1. **Crea un CLAUDE.md alla root** con stack, workflow e regole universali (max 300 righe). Usa `/init` in Claude Code per generare una bozza automatica.
2. **Organizza il codice per funzionalità**, non per tipo di file — `features/auth/` invece di `routes/`, `services/`, `types/` separati.
3. **Aggiungi un CLAUDE.md per ogni macro-funzionalità**, con il contesto specifico (pattern usati, librerie, gotcha da evitare).
4. **Definisci subagenti** in `.claude/agents/` per task specializzati (security review, API design, testing).
5. **Crea skill per i workflow ricorrenti** in `.claude/skills/` — ad esempio un workflow `new-feature.md` che descrive passo per passo come aggiungere una nuova funzionalità al portale.
6. **Usa `/clear` aggressivamente** tra task non correlati. Una sessione lunga con contesto sporco è il nemico principale della qualità.

---

## Conclusione

Sviluppare un portale con Claude Code non richiede di rinunciare alla complessità: richiede di gestirla con la stessa disciplina archittetturale che si applicherebbe a un team distribuito. Un progetto master come punto d'ingresso, sotto-progetti per le singole funzionalità, CLAUDE.md gerarchici per il contesto, subagenti per le investigazioni e Agent Teams per il lavoro parallelo — questi sono gli strumenti che trasformano Claude Code da assistente reattivo a co-sviluppatore strutturato.

La documentazione ufficiale esiste, è pubblica, e viene aggiornata regolarmente. Il punto di partenza migliore rimane sempre la [pagina delle best practice ufficiali](https://code.claude.com/docs/en/best-practices).
