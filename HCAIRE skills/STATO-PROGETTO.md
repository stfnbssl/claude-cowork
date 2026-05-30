# STATO DEL PROGETTO HCAIRE
*Aggiornato: 16 aprile 2026 — terza sessione di lavoro*

---

## Contesto per riprendere la sessione

Questo file è un handoff tra sessioni di lavoro. Chi legge (umano o IA) può ripartire da qui senza rileggere tutta la conversazione precedente.

---

## Cos'è HCAIRE

Progetto per sviluppare strumenti IA a supporto di chi lavora per il miglioramento dello sviluppo del bambino (ambito clinico, pedagogico, genitoriale, sociale, politico). Il sistema funziona attraverso una catena: fondamenti filosofici → skill operative → lettura delle tracce → produzione di output.

Il documento di riferimento è `CLAUDE.md` nella root della cartella.

---

## Cosa è stato fatto il 15 aprile 2026

### 1. Carta fondativa — Sezione 5 completata
`Documenti fondativi/Carta fondativa.md`

La sezione 5 ("Concetti strutturali del modello") era vuota. È stata completata con 9 voci operative. Il punto 5.5 (Simbolico e linguaggio) è volutamente incompleto — Stefano deve ancora lavorare su questo fondamento.

### 2. Sei schede-skill di fondamento create
`Skill di fondamento/` — Skill-Asse1 → Skill-Asse6

### 3. Corpus di tracce v1 costruito
`Repertorio tracce di esempio/Corpus-tracce-v1.md` — 18 tracce, 5 ambiti operativi

### 4. Prima simulazione completa eseguita
`Simulazioni/Simulazione-01-T-G03.md` — Traccia T-G03 (bambino 14 mesi). Valutazione 7.5/10.

---

## Cosa è stato fatto il 16 aprile 2026

### 1. Verifica di coerenza schede di ambito ↔ skill di fondamento (v1.0)
`Verifica-coerenza-schede-ambito.md`

Prima analisi sistematica: identificati 5 gap trasversali. La scheda Clinico risultava la più lacunosa.

### 2. Ciclo di interventi su 5 priorità — completato

#### Priorità 1 — Integrazione Asse 4 nelle schede Clinico, Pedagogico, Politico, Sociologico ✅
Aggiunto "Limite reale / Perdita" in §4, §5, §6, §7, §8 di ciascuna scheda con calibrazione specifica per ambito. Calibrazione: onnipotenza clinica/educativa/politica, dolore come risposta adeguata, situazioni che resistono agli interventi.

#### Priorità 2 — Nodo Integrazione/disorganizzazione nella Skill-Asse1 ✅
Skill-Asse1 aggiornata a v1.1. Aggiunti: Integrazione come coerenza multidimensionale, Disorganizzazione come segnale di configurazione, distinzione contestuale/pervasiva — in §1, §2, §3, §4, §5, §7.

#### Priorità 3 — Riformulazione Affettività in tutte le schede (Asse 2) ✅
"Affettività" espansa in tutte e 5 le schede con nucleo operativo dell'Asse 2 (ciclo legame/rottura/riparazione, colpa integrativa, riparazione, distinzione conformismo/responsabilità). Calibrazione per ambito. Nel Politico e Sociologico aggiunta come "infrastruttura affettiva" e "condizioni per il legame".

#### Priorità 4 — Asse 6 nelle schede Genitoriale e Clinico ✅
Aggiunto contesto storico-culturale in §4, §5, §6, §7, §8 di entrambe. Genitoriale: pressioni culturali, tecnologie, disuguaglianze. Clinico: condizioni socio-economiche, norme culturali non universali, decontestualizzazione come rischio clinico specifico.

#### Priorità 5 — Mappa di corrispondenza terminologica ✅
`Mappa-corrispondenza-terminologica.md`
35 termini mappati da schede di ambito verso assi/concetti fondativi. Indice inverso per asse. Identificati 3 termini non ancora mappati su un asse: Simbolico-linguaggio, Prevenzione, Integrazione tra sistemi.

#### Priorità 6 — Verifica di coerenza aggiornata (v2.0) ✅
`Verifica-coerenza-schede-ambito-v2.md`
Tutti i gap critici risolti. Identificati gap residui B (importanti) e C (strutturali).

### 3. Gap urgenti residui risolti

#### A5 (Desiderio) → Scheda Clinico ✅
Aggiunto: distinzione ritiro del desiderio vs. difficoltà di regolazione; prestazionalismo come patologia strutturale; ambiente che sostiene o soffoca il campo desiderante; domande guida operative. In §4, §5, §6, §7, §8.

#### A6 (Storico-culturale) → Scheda Pedagogico ✅
Aggiunto: scuola come istituzione che organizza il campo di esperienza; tecnologie vs. tempo scolastico; pressioni culturali sulla prestazione; disuguaglianze nelle condizioni di partenza; bambino "inadeguato al contesto" come configurazione. In §4, §5, §6, §7, §8.

---

## Struttura attuale della cartella

```
HCAIRE skills/
├── CLAUDE.md
├── STATO-PROGETTO.md                         ← questo file
├── Migrazione-nodi-trasversali.md            ← ✅ mappa migrazione 10→N1-N7 (v2.0)
├── Verifica-coerenza-schede-ambito.md        ← v1.0 (archivio, pre-v2.0)
├── Verifica-coerenza-schede-ambito-v2.md     ← v2.0 (archivio, pre-migrazione)
├── Verifica-coerenza-schede-ambito-v3.md     ← ✅ v3.0 — sul nuovo apparato (7 nodi, 4 contesti)
├── Mappa-corrispondenza-terminologica.md     ← ✅ v2.0 (4 contesti, 7 nodi)
├── Documenti fondativi/
│   ├── Carta fondativa.md
│   ├── Pipeline di traducibilità (canonica).md   ← ✅ rinvio canonico (v2.0)
│   ├── Atlante nodi trasversali.md               ← ✅ v2.0 — 7 nodi canonici N1-N7
│   ├── Output Bartleby — fondamenti e scelte.md  ← ✅ basi fondative degli output Bartleby (v1.0)
│   └── Scheda di ambito HCAIRE.md
├── Skill di fondamento/
│   ├── Skill-Asse1-Ontologico-fenomenologico.md
│   ├── Skill-Asse2-Affettivo-morale.md
│   ├── Skill-Asse3-Normativo-educativo.md
│   ├── Skill-Asse4-Separazione-e-Limite.md
│   ├── Skill-Asse5-Desiderio.md
│   └── Skill-Asse6-Storico-culturale.md
├── Schede di ambito/                         ← ✅ 4 contesti canonici
│   ├── Genitoriale.md
│   ├── Clinico.md
│   ├── Pedagogico.md
│   └── Istituzionale.md                      ← ✅ v2.0 — fonde Politico + Sociologico
├── Repertorio tracce di esempio/
│   ├── CLAUDE.md
│   └── Corpus-tracce-v1.md
├── Simulazioni/
│   ├── README.md
│   ├── Simulazione-01-T-G03.md
│   └── Simulazione-02-T-PI01.md
└── Bartleby/
    ├── CLAUDE.md
    ├── CLAUDE_webapp.md
    ├── Modello app.md
    ├── Modello dati.md
    ├── Motore di lettura della traccia.md    ← ✅ v2.0 — motore operativo Bartleby
    ├── Ipotesi di ridefinizione.md           ← ✅ ipotesi di ridefinizione (verso v2)
    └── data/                                 ← ✅ migrato alla v2.0
        ├── foundation_documents.json   (4)
        ├── concept_nodes.json          (7)
        ├── domain_areas.json           (4)
        ├── area_sheets.json            (4)
        ├── skills.json                 (10)
        ├── output_templates.json       (7)
        ├── input_traces.json           (17)
        ├── output_documents.json       (2)
        ├── users.json                  (2)
        ├── foundation_document_nodes.json (23)
        ├── area_sheet_nodes.json       (22)
        ├── skill_nodes.json            (44)
        └── skill_areas.json            (28)
```

---

## Stato della copertura assi — post interventi

| Asse | Genitoriale | Clinico | Pedagogico | Politico | Sociologico |
|------|-------------|---------|------------|----------|-------------|
| A1 Ontologico-fenomenologico | ◑ | ◑ | ◑ | ○ | ○ |
| A2 Affettivo-morale | ● | ● | ● | ◑ | ◑ |
| A3 Normativo-educativo | ○ | ○ | ● | ● | ● |
| A4 Separazione e Limite | ● | ● | ● | ● | ● |
| A5 Desiderio | △ | ● | ● | △ | △ |
| A6 Storico-culturale | ● | ● | ● | ● | ● |

**Legenda:** ● presente | ◑ parziale/indiretto | △ traccia | ○ assente

---

## Gap residui (da affrontare in cicli futuri)

### Gap B — Importanti
- **A3 in Genitoriale**: distinzione norma/giudizio, autorità educativa legittima — cuore delle domande genitoriali
- **A3 in Clinico**: lettura delle dinamiche educative familiari come variabile clinica
- **A5 in Genitoriale**: "Desiderio" ancora a livello di traccia ("iniziativa del bambino")

### Gap C — Strutturali (in parte attesi)
- **A1 parziale in Politico e Sociologico**: la scala sistemica astrae dal soggetto incarnato
- **A2 indiretto in Politico e Sociologico**: opera al livello delle condizioni strutturali per il legame

---

## Cosa è stato fatto (continuazione del 16 aprile 2026 — seconda sessione)

### 1. Skill-Asse5-Desiderio.md aggiornata a v1.1 ✅
Completamento dell'espansione con creatività ed espressività artistica:
- §2 già completato nella sessione precedente (4 nuovi concetti: Desiderio e creatività, Inibizione creativa come indicatore, Prestazionalismo creativo, Gioco simbolico come primo atto creativo)
- §3: aggiunti 3 trigger (inibizione creativa, gioco simbolico, prestazionalismo creativo)
- §4: aggiunto operatore #6 sulla creatività (atto creativo abitato vs. ridotto a prestazione; resistenza del materiale)
- §5: aggiunta riga "Riduzione della creatività a talento" → correzione verso lettura del campo
- §7: aggiunti 2 indicatori positivi (inibizione creativa come segnale del campo; gioco simbolico ricco vs. contratto) e 2 negativi (interpretare inibizione come carenza; leggere prestazionalismo senza dimensione strutturale)

### 2. Skill-Asse6-Storico-culturale.md aggiornata a v1.1 ✅
Espansione con dimensione culturale del linguaggio e nota di delimitazione:
- §2: "Mediazione simbolica e linguaggio" riformulata come "Mediazione linguistica e culturale" con paragrafo sulla dimensione culturale del linguaggio (lingua concreta, tradizione narrativa, lingua di casa vs. lingua della scuola, contesti migratori) + nota di delimitazione esplicita che distingue il territorio di A6 (linguaggio come pratica culturale: *in quale mondo linguistico vive questo bambino?*) dall'Asse Simbolico-linguaggio futuro (funzione simbolica come trasformazione strutturale dell'esperienza)
- §3: aggiunti 3 trigger (differenze lingua di casa/scuola, contesti plurilingui, valutazione decontestualizzata dello sviluppo linguistico)
- §4: aggiunto operatore #6 sul linguaggio come pratica culturale
- §5: aggiunta riga "Universalismo linguistico" → correzione verso contestualizzazione
- §7: aggiunto 1 indicatore positivo (contesto linguistico come variabile strutturale) e 1 negativo (valutazione senza contesto)

### 3. Mappa-corrispondenza-terminologica.md aggiornata a v1.1 ✅
- Aggiunte 7 nuove voci nella tavola principale (Creatività ed espressività artistica, Gioco simbolico, Inibizione creativa, Prestazionalismo creativo, Linguaggio e simbolico, Lingua di casa/scuola — tutte con assi e note operative)
- Indice inverso Asse 5 espanso con termini di creatività
- Indice inverso Asse 6 espanso con termini di linguaggio culturale
- Sezione §2.1 "Simbolico e linguaggio" aggiornata per riflettere la nota di delimitazione in A6 v1.1
- Tabella architettura aggiornata: A5 v1.1, A6 v1.1; creatività integrata in A5 (non nuovo asse); Simbolico-linguaggio in costruzione con territorio delimitato

---

## Prossimi passi (in ordine stabilito oggi)

### 1 — Gap residui importanti (prossimo ciclo operativo)
- Aggiungere A3 alla Scheda Genitoriale
- Aggiungere A3 alla Scheda Clinico
- Espandere A5 nella Scheda Genitoriale

### 2 — Riflessione sui nuovi assi
Due assi candidati emersi nel corso del lavoro:
- **Asse Simbolico-linguaggio**: già pianificato come 5.5 nella Carta fondativa. Urgente per Genitoriale e Pedagogico dove "Linguaggio e simbolico" è dimensione primaria senza fondamento nell'asse. Dipende da materiale che Stefano deve elaborare.
- **Asse Creatività ed Espressività Artistica**: segnalato da Stefano come dimensione rilevante nello sviluppo del bambino. Da valutare strategicamente: nuovo asse autonomo o integrazione in asse esistente?

### 3 — Seconda simulazione ✅
`Simulazioni/Simulazione-02-T-PI01.md` — Traccia T-PI01 (Comune, primi 1000 giorni). Valutazione 8/10.

L'argomento fondativo (regolazione, sicurezza relazionale, apertura al possibile) sostituisce il neuroriduzionismo standard. Combinazione: argomento fondativo + argomento economico (Heckman) + argomento di equità. Output in forma di nota orientativa per decisore istituzionale. Punto debole identificato: assenza di contestualizzazione locale.

**Candidato per Simulazione 03:**
- **T-C03** (bambino 5 anni con aggressività, genitori in separazione) → lettura sistemica clinica

---

## Cosa è stato fatto (continuazione del 16 aprile 2026 — terza sessione)

### Bartleby — Batch 1 JSON completato ✅

Prodotti tutti i file JSON seed per avviare la programmazione di Bartleby (Claude Code).

**Localizzazione:** `Bartleby/data/`

#### File prodotti — Batch 1

| File | Record | Descrizione |
|------|--------|-------------|
| `foundation_documents.json` | 4 | Documenti fondativi HCAIRE (fd-001..fd-004) — Option B (file_path, no body) |
| `concept_nodes.json` | 10 | Nodi concettuali trasversali (cn-001..cn-010) — tutti con payload completo |
| `domain_areas.json` | 5 | Ambiti operativi (da-001..da-005) |
| `area_sheets.json` | 5 | Schede di ambito operative complete (as-001..as-005) |
| `skills.json` | 11 | Skill fondative (sk-001..sk-006) + skill di ambito (sk-007..sk-011) |
| `output_templates.json` | 7 | Template di output (guida-genitoriale, nota-clinico-riflessiva, guida-educativa, griglia-osservazionale, analisi-di-caso, policy-brief, articolo-riflessione) |
| `input_traces.json` | 17 | Tracce dal Corpus-tracce-v1.md (T-G01..06, T-C01..04, T-P01..03, T-S01..02, T-PI01..02) |
| `output_documents.json` | 2 | Simulazioni 01 (T-G03) e 02 (T-PI01) |
| `users.json` | 2 | Admin HCAIRE (user-001) + utente standard (user-002) |
| `foundation_document_nodes.json` | 36 | Bridge: FoundationDocument ↔ ConceptNode (origine, supporto, attivazione, traduzione-interdisciplinare) |
| `area_sheet_nodes.json` | 34 | Bridge: AreaSheet ↔ ConceptNode (con priorità per ambito) |
| `skill_nodes.json` | 54 | Bridge: Skill ↔ ConceptNode (fondamento-diretto, fondamento-indiretto, operativo) |
| `skill_areas.json` | 35 | Bridge: Skill ↔ DomainArea (fondamento, fondamento-principale, principale) |

**Totale: 13 file, 302 record**

#### Note architetturali

- **Option B mantenuta**: FoundationDocuments usano `file_path` + `summary`, nessun campo `body`. I documenti originali sono su Google Drive. Il passaggio a PostgreSQL con ingestione del body è deferred.
- **Skill di fondamento ≠ FoundationDocuments**: Le 6 skill (sk-001..sk-006) sono entità di tipo `Skill` derivate dai 4 FoundationDocuments, non documenti fondativi essi stessi.
- **Bridge `bridge/` vuota**: La directory era un placeholder. Le tabelle di relazione sono direttamente in `data/`.
- **`activated_nodes` in InputTrace**: campo aggiunto come annotazione operativa (deriva dal Corpus-tracce). Nella logica del sistema questo dato emerge dalla TraceInterpretation, ma il Corpus lo fornisce già come annotazione.

#### Batch 2 — deferred

Da produrre in fase successiva:
- `translation_rules.json` — richiede lettura completa della Pipeline di traducibilità (rinvio canonico) e del Motore di lettura della traccia (Bartleby)
- `user_customization_profiles.json` — quando ci sono utenti reali
- `governance_decisions.json` — quando il comitato HCAIRE approva formalmente
- `source_documents.json` — fonti bibliografiche esterne (Heckman, ricerche citate)

---

## Sessione 2026-05-24 — Migrazione v2.0: 7 nodi canonici e 4 contesti

Allineamento dell'intero progetto al fondamento ufficiale (`04 Memorie di contesto fondamentali/Metodo-fasi-concetti.md`): adozione dei **7 Nodi Trasversali canonici N1–N7** (al posto dei 10 nodi della v1) e dei **4 contesti canonici** (al posto dei 5 ambiti — Politico e Sociologico fusi in Istituzionale/servizi).

**Livello fondativo.** `Documenti fondativi/Atlante nodi trasversali.md` riscritto alla v2.0 sui 7 nodi. Creato `Migrazione-nodi-trasversali.md` con la mappa di migrazione 10→N1-N7.

**Dati seed Bartleby** (`Bartleby/data/`). `concept_nodes.json` 10→7 record (N1-N7); `domain_areas.json` e `area_sheets.json` 5→4; `skills.json` 11→10 (skill di ambito Politico+Sociologico fuse in Istituzionale/servizi). Tabelle ponte rimappate: `foundation_document_nodes` 36→23, `area_sheet_nodes` 34→22, `skill_nodes` 54→44, `skill_areas` 35→28. `input_traces.json`: `activated_nodes` rimappati + nuovo campo `activated_axes`. Tutti i riferimenti incrociati validati. Totale: 13 file, 174 record.

**Contenuto del modello.** Schede di ambito 5→4 (creata `Istituzionale.md`; eliminate `Politico.md` e `Sociologico.md`); §8 di ogni scheda riscritto sui 7 nodi. `Skill-Asse1` e `Mappa-corrispondenza-terminologica.md` (v2.0) aggiornate.

**Documenti di sistema e di tracciamento.** `Bartleby/CLAUDE_webapp.md`, `CLAUDE.md` di root, `Bartleby/Modello dati.md`, `Bartleby/Modello app.md` aggiornati ai 7 nodi e 4 contesti; verifiche di coerenza e corpus tracce annotati per l'allineamento.

**Completamento (2026-05-24).** Re-annotazione del corpus tracce ai 7 nodi canonici (`Repertorio tracce di esempio/Corpus-tracce-v1.md`) e ri-verifica di coerenza schede↔skill sul nuovo apparato (`Verifica-coerenza-schede-ambito-v3.md`) eseguite.

**Pendenze residue.** Chiusura dei gap rilevati dalla v3 (A3 in Genitoriale e Clinico, A5 in Genitoriale, nodi N4 e N6 poco coperti); evoluzione dei documenti di sistema e del prototipo verso Bartleby v2 (vedi `Bartleby/Ipotesi di ridefinizione.md`).

---

## Materiali su Google Drive

Cartella: *Assi strutturali — sviluppo bambino*
Link: https://drive.google.com/drive/folders/1myRQk3sBvR23oej8xjrw0G9NPpW0NBDU

Contenuto: 6 cartelle (una per asse), ognuna con capitoli discorsivi e traduzioni interdisciplinari vs. Embodied Cognition. Materiale filosofico di base da cui sono state derivate le skill di fondamento.

---

## Come riprendere

1. Apri Cowork
2. Seleziona la cartella `HCAIRE skills`
3. Di': *"Riprendo il lavoro sul progetto HCAIRE. Leggi STATO-PROGETTO.md per il contesto e dimmi se hai domande prima di procedere."*
4. Indica quale priorità vuoi affrontare
