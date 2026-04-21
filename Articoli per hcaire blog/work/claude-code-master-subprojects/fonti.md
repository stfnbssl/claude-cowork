# Fonti - Claude Code: Gestire un Portale con Strategia Master/Sotto-Progetti

## Fonte 1
- **Titolo**: Best Practices for Claude Code
- **URL**: https://code.claude.com/docs/en/best-practices
- **Tipo**: Documentazione ufficiale
- **Autore/Fonte**: Anthropic
- **Data**: 2026
- **Rilevanza**: Fonte primaria ufficiale di Anthropic. Descrive in dettaglio la gestione del contesto, la struttura gerarchica dei file CLAUDE.md, l'uso di subagenti per isolare task, e le strategie per progetti complessi con molti file. Fondamentale per il concetto di "master project" con sottocontesti.

## Fonte 2
- **Titolo**: Claude Code × Monorepo Development — Streamlining Large-Scale Projects with Turborepo and pnpm Workspaces
- **URL**: https://claudelab.net/en/articles/claude-code/claude-code-monorepo-turborepo-workspace-guide
- **Tipo**: Articolo tecnico
- **Autore/Fonte**: Claude Lab
- **Data**: 2026
- **Rilevanza**: Fonte primaria tecnica che descrive la strategia di layering dei CLAUDE.md in un monorepo: root-level per regole globali, package-level per contesti specifici. Copre Turborepo, pnpm workspaces e cross-package refactoring — architettura direttamente applicabile a un portale con funzionalità multiple.

## Fonte 3
- **Titolo**: Orchestrate teams of Claude Code sessions - Claude Code Docs
- **URL**: https://code.claude.com/docs/en/agent-teams
- **Tipo**: Documentazione ufficiale
- **Autore/Fonte**: Anthropic
- **Data**: 2026
- **Rilevanza**: Fonte primaria ufficiale che descrive Agent Teams — il sistema di orchestrazione multi-agente di Claude Code. Spiega come un "team lead" coordina agenti paralleli su sotto-task indipendenti, con task list condivisa, messaggistica peer-to-peer e file locking. Perfetto per lo sviluppo parallelo di funzionalità di un portale.

## Fonte 4
- **Titolo**: The "Virtual Monorepo" Pattern: How I Gave Claude Code Full-System Context Across 35 Repos
- **URL**: https://medium.com/devops-ai/the-virtual-monorepo-pattern-how-i-gave-claude-code-full-system-context-across-35-repos-43b310c97db8
- **Tipo**: Articolo / case study
- **Autore/Fonte**: Owen Zanzal (Medium - DevOps<>AI)
- **Data**: Marzo 2026
- **Rilevanza**: Case study pratico su come gestire 35 repository separati dando a Claude Code un contesto unificato tramite il "Virtual Monorepo Pattern". Dimostra che la strategia multi-repo con un progetto master è fattibile e scalabile anche in contesti reali complessi.

## Fonte 5
- **Titolo**: Claude Code in Monorepos — Configuration Guide
- **URL**: https://claudearchitect.com/docs/claude-code/claude-code-monorepo/
- **Tipo**: Guida tecnica
- **Autore/Fonte**: ClaudeArchitect
- **Data**: 2026
- **Rilevanza**: Guida dettagliata sulla configurazione di Claude Code in monorepo. Spiega il lazy loading dei CLAUDE.md nelle subdirectory, il dimensionamento ottimale dei file (200-300 righe), e l'uso di @ references per suddividere la documentazione — direttamente applicabile alla gestione di un portale con più sotto-progetti.

## Fonte 6
- **Titolo**: Shipyard — Multi-agent orchestration for Claude Code in 2026
- **URL**: https://shipyard.build/blog/claude-code-multi-agent/
- **Tipo**: Articolo tecnico / blog
- **Autore/Fonte**: Shipyard
- **Data**: 2026
- **Rilevanza**: Analisi dell'ecosistema di orchestrazione multi-agente per Claude Code nel 2026. Utile per il confronto tra approcci (subagents vs agent teams) e per capire quali strumenti esistono per gestire workflow complessi come lo sviluppo di un portale web a più funzionalità.
