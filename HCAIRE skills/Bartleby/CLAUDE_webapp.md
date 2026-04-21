# CLAUDE.md — Bartleby

## Cos'è Bartleby

Bartleby è il sottosistema della webapp HCAIRE che gestisce la base di conoscenza strutturata del modello e la produzione di output su tracce utente. Il modello concettuale e il modello dati completo si trovano in questo folder: `Modello app.md` e `Modello dati.md`. Leggerli prima di procedere.

Il patrimonio di conoscenza HCAIRE è organizzato in tre famiglie:
- **A — Fondativi**: documenti madre, nodi concettuali trasversali, ambiti operativi, schede di ambito, skill. Prodotti e governati da HCAIRE. Immutabili lato utente.
- **B — Esecuzione**: tracce utente, interpretazioni, piani di generazione, output, revisioni.
- **C — Governance e personalizzazione**: profili utente, skill utente, decisioni del comitato.

---

## Dati disponibili: file JSON in `./data/`

I 13 file JSON in questa cartella sono il seed data del sistema. Vanno usati per:
1. popolare il database (MongoDB) al primo avvio
2. alimentare la visualizzazione della knowledge base nella UI
3. costruire il contesto passato a Claude Cowork per la generazione degli output

Per la specifica completa di ogni entità (campi, tipi, relazioni M:M) consultare `Modello dati.md`.

### File presenti e contenuto sintetico

**Famiglia A — Fondativi**

| File | Record | Contenuto |
|------|--------|-----------|
| `foundation_documents.json` | 4 | Documenti fondativi HCAIRE. Campi principali: id, type, title, summary, file_path. Nessun campo body (testi originali su Google Drive). |
| `concept_nodes.json` | 10 | Nodi concettuali trasversali. Payload completo: definition, why_transversal, typical_manifestations, area_lexicons, guiding_questions, presence_indicators, impoverishment_indicators. |
| `domain_areas.json` | 5 | Ambiti operativi (Genitoriale, Clinico, Pedagogico, Politico, Sociologico). Campi: name, purpose, language_style, risk_profile. |
| `area_sheets.json` | 5 | Schede di ambito operative, una per dominio. Campi: scope, priority_dimensions, typical_configurations, reduction_risks, guiding_questions, allowed_output_types, language_rules, quality_indicators. |
| `skills.json` | 11 | 6 skill fondative (Asse 1–6) + 5 skill di ambito (una per dominio). Ogni skill ha instruction_payload strutturato. `owner_type: "hcaire"` per tutte le skill di questo batch. |
| `output_templates.json` | 7 | Template di output: guida-genitoriale, nota-clinico-riflessiva, guida-educativa, griglia-osservazionale, analisi-di-caso, policy-brief, articolo-riflessione. Campi: structure_schema, audience_type, language_constraints, applicable_areas. |

**Famiglia B — Dati di esempio e test**

| File | Record | Contenuto |
|------|--------|-----------|
| `input_traces.json` | 17 | Corpus di tracce di riferimento HCAIRE (T-G01..06, T-C01..04, T-P01..03, T-S01..02, T-PI01..02). Campi: corpus_id, raw_text, context_notes, target_output_type, requested_area_id, activated_nodes, trace_type. |
| `output_documents.json` | 2 | Simulazioni già prodotte (T-G03, T-PI01). Il body completo è nei file .md indicati in file_path. |

**Famiglia C — Utenti stub**

| File | Record | Contenuto |
|------|--------|-----------|
| `users.json` | 2 | user-001 (admin HCAIRE) e user-002 (utente standard). |

**Tabelle bridge M:M**

| File | Record | Relazione |
|------|--------|-----------|
| `foundation_document_nodes.json` | 36 | FoundationDocument ↔ ConceptNode (relation_type: origine / supporto / attivazione / traduzione-interdisciplinare) |
| `area_sheet_nodes.json` | 34 | AreaSheet ↔ ConceptNode (con priority_in_area: primario / secondario) |
| `skill_nodes.json` | 54 | Skill ↔ ConceptNode (relation_type: fondamento-diretto / fondamento-indiretto / operativo) |
| `skill_areas.json` | 35 | Skill ↔ DomainArea (relation_type: fondamento / fondamento-principale / principale) |

---

## Architettura di generazione output

Gli output sono prodotti tramite **child process che chiama Claude Cowork sul desktop locale**.

```
Utente (webapp)
  → inserisce traccia
  → backend salva InputTrace in MongoDB
  → backend pubblica job su Redis

Server locale (desktop)
  → ascolta Redis
  → riceve il job
  → legge dal DB: traccia + skill HCAIRE rilevanti + skill utente
  → avvia child process Claude Cowork con questo contesto
  → Claude Cowork elabora (Moduli A–F del Motore di traducibilità)
  → salva in MongoDB: TraceInterpretation + GenerationPlan + OutputDocument

Webapp
  → recupera OutputDocument da MongoDB
  → visualizza output + provenienza completa
```

**Contesto passato al child process Cowork:**
- La traccia utente (raw_text + context_notes)
- Le skill fondative pertinenti (da `skills.json`, skill_type: "fondativa")
- La skill di ambito rilevante (da `skills.json`, skill_type: "di_ambito")
- Il template di output selezionato (da `output_templates.json`)
- Le skill di personalizzazione utente, se presenti (da MongoDB, owner_type: "user")

Le skill HCAIRE (fondative e di ambito) non cambiano tra una generazione e l'altra: sono lette dai JSON o dal DB al momento della costruzione del contesto.

---

## Cosa costruire: sezione Bartleby della webapp

### 1. Knowledge Base Browser

Visualizzazione navigabile della base di conoscenza HCAIRE. Non una lista piatta: una rete navigabile.

**Vista nodo trasversale** — mostra: definition, why_transversal, ambiti in cui è prioritario (da area_sheet_nodes), skill collegate (da skill_nodes), output esemplificativi se disponibili.

**Vista ambito** — mostra: DomainArea (purpose, language_style, risk_profile) + AreaSheet completa (priority_dimensions, typical_configurations, guiding_questions, allowed_output_types).

**Vista skill** — mostra: name, skill_type, description, instruction_payload in forma leggibile, nodi collegati, ambiti in cui opera.

**Vista documento fondativo** — mostra: title, type, summary, link al file originale.

**Vista template di output** — mostra: name, description, structure_schema, audience_type, language_constraints.

La navigazione deve essere bidirezionale: da un nodo si arriva alle skill, da una skill si arriva ai nodi e agli ambiti, da un ambito si arriva ai nodi prioritari.

---

### 2. Sottomissione traccia

Form per l'inserimento di una nuova traccia con:
- Testo libero (raw_text) — obbligatorio
- Note di contesto (context_notes) — opzionale
- Ambito richiesto (requested_area_id) — opzionale, select dai 5 DomainArea
- Tipo di output desiderato (target_output_type) — select dai 7 OutputTemplate
- Profilo di personalizzazione (se l'utente ne ha uno) — opzionale

Al submit: salva InputTrace in MongoDB, pubblica job su Redis, mostra stato (in attesa / in elaborazione / completato).

---

### 3. Visualizzazione output con provenienza

Per ogni OutputDocument prodotto, la UI deve mostrare due sezioni distinte:

**Sezione A — Il documento**
Il testo dell'output formattato (body), con titolo, tipo, ambito, data.

**Sezione B — Come è stato generato**
Pannello di trasparenza che espone l'intera catena decisionale:
- Traccia originale
- Traccia riformulata (da TraceInterpretation.reformulated_trace)
- Nodi trasversali attivati (da TraceInterpretation.detected_nodes) — con link alle schede nodo
- Ambito rilevato (da TraceInterpretation.detected_areas) — con link alla scheda di ambito
- Rischi di riduzione rilevati (da TraceInterpretation.detected_risks)
- Skill utilizzate (da GenerationPlan.selected_skills) — con link alle schede skill
- Template di output applicato (da GenerationPlan) — con link
- Skill di personalizzazione utente applicate, se presenti

Questa sezione di trasparenza è il tratto distintivo del sistema HCAIRE. Non è opzionale.

---

### 4. Storico tracce e output

- Lista delle tracce dell'utente con stato (pending / processing / completed / failed)
- Accesso all'output con provenienza completa per ogni traccia completata
- Filtro per ambito e tipo di output

---

### 5. Area admin (user-001 soltanto)

- Visualizzazione dei JSON di seed data caricati nel DB
- Indicatore di versione per ogni entità fondativa
- Log delle generazioni (chi ha generato cosa, quando, con quali skill)
- Accesso alle GovernanceDecision (deferred: entità non ancora popolata nel Batch 1)

---

## Stato del seed data

Il Batch 1 è completo e validato (13 file JSON, 302 record). Tutti i file sono JSON valido.

Entità del Batch 2, non ancora prodotte (deferred):
- `translation_rules.json` — regole di traducibilità dal Motore di traducibilità
- `user_customization_profiles.json` — profili utente (quando ci sono utenti reali)
- `governance_decisions.json` — decisioni formali del comitato HCAIRE
- `source_documents.json` — fonti bibliografiche esterne citate negli output

La sezione admin può già prevedere placeholder per queste entità.
