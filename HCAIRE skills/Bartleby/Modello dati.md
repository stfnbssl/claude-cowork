# Modello dati di Bartleby - Entità e relazioni

> **Nota di allineamento (2026-05-24).** Gli esempi di ConceptNode e DomainArea in questo documento sono aggiornati ai 7 Nodi Trasversali canonici N1–N7 e ai 4 contesti canonici. Il modello delle entità resta valido; per la ridefinizione complessiva di Bartleby vedi `Bartleby/Ipotesi di ridefinizione.md`.

Ogni entità è organizzata così:

* **Tipo di dato**
* **Che cos’è**
* **Dati elementari principali**
* **Descrizione dei dati elementari**
* **Chi lo crea**
* **Chi lo usa**
* **Relazioni principali**

Sommario

1. dati fondativi HCAIRE
  1.1 FoundationDocument
  1.2 ConceptNode
  1.3 DomainArea
2. dati di traduzione e operatività
  2.1 AreaSheet
  2.2 TranslationRule
  2.3 Skill
  2.4 OutputTemplate
3. dati di input e generazione
  3.1 InputTrace
  3.2 TraceInterpretation
  3.3 GenerationPlan
  3.4 OutputDocument
  3.5 OutputRevision
  3.6 SourceDocument
4. dati di governance e personalizzazione
  4.1 UserCustomizationProfile
  4.2 GovernanceDecision
  4.3 User

---

# 1. DATI FONDATIVI HCAIRE

## 1.1 FoundationDocument

**Che cos’è**
Documento fondativo prodotto da HCAIRE. Rappresenta un testo-madre che definisce una parte del modello.

**Esempi**

* Carta fondativa
* Pipeline di traducibilità (canonica) — rinvio
* Atlante dei nodi trasversali (v2.0)

| Dato elementare | Descrizione                                          |
| --------------- | ---------------------------------------------------- |
| `id`            | Identificatore univoco del documento                 |
| `type`          | Tipo del documento fondativo                         |
| `title`         | Titolo leggibile del documento                       |
| `slug`          | Nome breve usato negli URL o nei riferimenti interni |
| `summary`       | Sintesi breve del contenuto                          |
| `body`          | Testo completo del documento                         |
| `status`        | Stato del documento: bozza, approvato, archiviato    |
| `version`       | Numero o codice di versione                          |
| `created_by`    | Identificativo dell’autore o gruppo autore           |
| `approved_by`   | Identificativo di chi ha approvato il documento      |
| `created_at`    | Data di creazione                                    |
| `updated_at`    | Data ultimo aggiornamento                            |

**Chi lo crea**
HCAIRE / comitato scientifico

**Chi lo usa**

* HCAIRE
* motore di generazione
* eventualmente utenti in consultazione

**Relazioni principali**

* genera nodi
* genera regole
* genera skill
* può essere collegato a schede di ambito

---

## 1.2 ConceptNode

**Che cos’è**
Nodo concettuale trasversale del modello.

**Esempi**

* N1 — Regolazione / Integrazione dell'esperienza
* N2 — Campo relazionale / Co-regolazione
* N3 — Accesso al mondo condiviso simbolico

| Dato elementare      | Descrizione                                      |
| -------------------- | ------------------------------------------------ |
| `id`                 | Identificatore univoco del nodo                  |
| `name`               | Nome del nodo                                    |
| `slug`               | Nome tecnico breve                               |
| `definition`         | Definizione del nodo                             |
| `why_transversal`    | Spiegazione del perché attraversa più ambiti     |
| `priority_level`     | Livello di priorità del nodo nel sistema         |
| `status`             | Stato: bozza, approvato, archiviato              |
| `version`            | Versione del nodo                                |
| `source_document_id` | Documento fondativo da cui deriva principalmente |

**Chi lo crea**
HCAIRE

**Chi lo usa**

* motore di interpretazione
* schede di ambito
* generazione output
* utenti in consultazione

**Relazioni principali**

* deriva da documenti fondativi
* si collega a più ambiti
* si collega a più skill
* può essere attivato da una traccia

---

## 1.3 DomainArea

**Che cos’è**
Ambito generale di applicazione del modello.

**Esempi**

* genitoriale
* clinico
* pedagogico
* istituzionale/servizi

| Dato elementare  | Descrizione                                           |
| ---------------- | ----------------------------------------------------- |
| `id`             | Identificatore univoco dell’ambito                    |
| `name`           | Nome dell’ambito                                      |
| `slug`           | Nome tecnico breve                                    |
| `description`    | Descrizione sintetica dell’ambito                     |
| `purpose`        | Finalità generale dell’ambito                         |
| `language_style` | Stile linguistico prevalente richiesto                |
| `risk_profile`   | Tipologia di rischi interpretativi tipici dell’ambito |
| `status`         | Stato dell’ambito                                     |
| `version`        | Versione dell’ambito                                  |

**Chi lo crea**
HCAIRE

**Chi lo usa**

* motore di selezione
* generazione output
* utenti in navigazione

**Relazioni principali**

* ha una o più schede di ambito
* si collega a più nodi
* si collega a più skill
* viene attivato da interpretazioni di traccia

---

# 2. DATI DI TRADUZIONE E OPERATIVITÀ

## 2.1 AreaSheet

**Che cos’è**
Scheda operativa completa di un ambito.

| Dato elementare          | Descrizione                                                |
| ------------------------ | ---------------------------------------------------------- |
| `id`                     | Identificatore della scheda                                |
| `domain_area_id`         | Ambito a cui la scheda appartiene                          |
| `title`                  | Titolo della scheda                                        |
| `scope`                  | Scopo operativo della scheda                               |
| `main_focus`             | Oggetto principale di attenzione                           |
| `translation_of_model`   | Descrizione di come il modello si traduce in questo ambito |
| `priority_dimensions`    | Elenco delle dimensioni del modello prioritarie            |
| `typical_configurations` | Configurazioni tipiche osservabili                         |
| `reduction_risks`        | Rischi tipici di riduzione                                 |
| `guiding_questions`      | Domande guida da usare nell’ambito                         |
| `allowed_output_types`   | Tipi di output appropriati                                 |
| `language_rules`         | Regole linguistiche per questo ambito                      |
| `operational_cautions`   | Cautele specifiche                                         |
| `quality_indicators`     | Indicatori per valutare la qualità dell’output             |
| `status`                 | Stato della scheda                                         |
| `version`                | Versione della scheda                                      |

**Chi lo crea**
HCAIRE

**Chi lo usa**

* motore di generazione
* revisione
* consultazione interna o pubblica

**Relazioni principali**

* appartiene a un ambito
* si collega a nodi
* alimenta skill di ambito
* guida output specifici

---

## 2.2 TranslationRule

**Che cos’è**
Regola di traducibilità o di comportamento interpretativo.

| Dato elementare    | Descrizione                                                     |
| ------------------ | --------------------------------------------------------------- |
| `id`               | Identificatore della regola                                     |
| `title`            | Titolo breve della regola                                       |
| `rule_type`        | Tipo di regola: interpretativa, linguistica, sicurezza, qualità |
| `rule_text`        | Testo completo della regola                                     |
| `applies_to_scope` | Ambito di applicazione: fondamento, nodo, ambito, output        |
| `scope_id`         | Identificatore dell’oggetto a cui si applica                    |
| `priority`         | Importanza della regola nel sistema                             |
| `status`           | Stato della regola                                              |
| `version`          | Versione della regola                                           |

**Chi lo crea**
HCAIRE

**Chi lo usa**

* motore di traducibilità
* generazione output
* modulo di revisione

**Relazioni principali**

* deriva da fondamenti o schede
* si applica a nodi, ambiti o output

---

## 2.3 Skill

**Che cos’è**
Unità operativa usata dal sistema per applicare regole, fondamenti e traduzioni.

| Dato elementare       | Descrizione                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| `id`                  | Identificatore della skill                                              |
| `name`                | Nome della skill                                                        |
| `slug`                | Nome tecnico breve                                                      |
| `skill_type`          | Tipo: fondativa, di ambito, di nodo, di personalizzazione, di output    |
| `description`         | Descrizione della funzione della skill                                  |
| `instruction_payload` | Contenuto operativo della skill, preferibilmente in formato strutturato |
| `status`              | Stato della skill                                                       |
| `version`             | Versione della skill                                                    |
| `owner_type`          | Origine: HCAIRE o utente                                                |
| `owner_id`            | Identificativo del proprietario della skill                             |

**Chi lo crea**
HCAIRE o utente, a seconda del tipo

**Chi lo usa**

* motore di generazione
* motore di selezione
* revisione

**Relazioni principali**

* può derivare da fondamenti
* può essere collegata a nodi
* può essere collegata ad ambiti
* può essere inclusa in un piano di generazione

---

## 2.4 OutputTemplate

**Che cos’è**
Modello strutturale di output.

**Esempi**

* articolo
* guida
* scheda osservazionale
* policy brief
* case study

| Dato elementare        | Descrizione                                 |
| ---------------------- | ------------------------------------------- |
| `id`                   | Identificatore del template                 |
| `name`                 | Nome del tipo di output                     |
| `description`          | Descrizione sintetica                       |
| `structure_schema`     | Schema della struttura prevista dell’output |
| `audience_type`        | Destinatario tipico                         |
| `language_constraints` | Vincoli di linguaggio                       |
| `status`               | Stato del template                          |
| `version`              | Versione del template                       |

**Chi lo crea**
HCAIRE

**Chi lo usa**

* piano di generazione
* generatore di output

**Relazioni principali**

* usato nei piani di generazione
* collegato ad ambiti e skill

---

# 3. DATI DI INPUT E GENERAZIONE

## 3.1 InputTrace

**Che cos’è**
Traccia iniziale fornita da un utente o da HCAIRE per avviare la generazione.

| Dato elementare      | Descrizione                           |
| -------------------- | ------------------------------------- |
| `id`                 | Identificatore della traccia          |
| `user_id`            | Utente che ha inserito la traccia     |
| `title`              | Titolo breve assegnato alla traccia   |
| `raw_text`           | Testo originale della traccia         |
| `context_notes`      | Eventuali note aggiuntive di contesto |
| `target_output_type` | Tipo di output richiesto              |
| `requested_area_id`  | Ambito richiesto, se indicato         |
| `status`             | Stato della traccia                   |
| `created_at`         | Data di inserimento                   |

**Chi lo crea**
Utente o HCAIRE

**Chi lo usa**

* motore di interpretazione
* piano di generazione

**Relazioni principali**

* genera una interpretazione
* può generare più output

---

## 3.2 TraceInterpretation

**Che cos’è**
Risultato dell’analisi della traccia secondo il modello HCAIRE.

| Dato elementare        | Descrizione                                  |
| ---------------------- | -------------------------------------------- |
| `id`                   | Identificatore dell’interpretazione          |
| `input_trace_id`       | Traccia di origine                           |
| `reformulated_trace`   | Traccia riformulata dal sistema              |
| `detected_nodes`       | Elenco dei nodi attivati                     |
| `detected_areas`       | Elenco degli ambiti attivati                 |
| `detected_risks`       | Rischi di riduzione o errore individuati     |
| `interpretation_notes` | Note descrittive dell’interpretazione        |
| `confidence_level`     | Livello di affidabilità dell’interpretazione |
| `generated_at`         | Data di generazione                          |

**Chi lo crea**
Sistema HCAIRE

**Chi lo usa**

* piano di generazione
* revisione
* spiegazione del processo all’utente

**Relazioni principali**

* deriva da una traccia
* seleziona nodi e ambiti
* alimenta il piano di generazione

---

## 3.3 GenerationPlan

**Che cos’è**
Piano strutturato che decide quali oggetti usare per generare un output.

| Dato elementare                 | Descrizione                           |
| ------------------------------- | ------------------------------------- |
| `id`                            | Identificatore del piano              |
| `input_trace_id`                | Traccia di partenza                   |
| `trace_interpretation_id`       | Interpretazione usata                 |
| `selected_foundation_documents` | Documenti fondativi selezionati       |
| `selected_area_sheets`          | Schede di ambito selezionate          |
| `selected_nodes`                | Nodi selezionati                      |
| `selected_skills`               | Skill selezionate                     |
| `selected_translation_rules`    | Regole selezionate                    |
| `selected_customizations`       | Personalizzazioni utente applicate    |
| `selected_sources`              | Fonti esterne da integrare            |
| `generation_strategy`           | Strategia adottata per la generazione |
| `status`                        | Stato del piano                       |

**Chi lo crea**
Sistema HCAIRE

**Chi lo usa**

* generatore di output
* revisori
* eventuale interfaccia di trasparenza

**Relazioni principali**

* deriva da traccia e interpretazione
* seleziona tutti gli oggetti necessari
* genera uno o più output

---

## 3.4 OutputDocument

**Che cos’è**
Documento finale o bozza prodotta dal sistema.

| Dato elementare      | Descrizione                                       |
| -------------------- | ------------------------------------------------- |
| `id`                 | Identificatore dell’output                        |
| `input_trace_id`     | Traccia da cui deriva                             |
| `generation_plan_id` | Piano usato per produrlo                          |
| `output_type`        | Tipo di output                                    |
| `title`              | Titolo del documento                              |
| `body`               | Contenuto completo                                |
| `audience`           | Destinatario principale                           |
| `area_id`            | Ambito prevalente                                 |
| `status`             | Stato: bozza, revisionato, pubblicato, archiviato |
| `version`            | Versione dell’output                              |
| `created_at`         | Data di creazione                                 |

**Chi lo crea**
Sistema HCAIRE, eventualmente con revisione umana

**Chi lo usa**

* utente finale
* HCAIRE
* sistema di validazione

**Relazioni principali**

* deriva da un piano
* è collegato a nodi, skill, ambiti e fonti
* può avere revisioni

---

## 3.5 OutputRevision

**Che cos’è**
Versione revisionata o annotata di un output.

| Dato elementare      | Descrizione                                                     |
| -------------------- | --------------------------------------------------------------- |
| `id`                 | Identificatore della revisione                                  |
| `output_document_id` | Output a cui la revisione si riferisce                          |
| `revision_type`      | Tipo di revisione: stilistica, concettuale, scientifica, utente |
| `revision_notes`     | Note sul motivo della revisione                                 |
| `body`               | Testo della versione revisionata                                |
| `reviewed_by`        | Identificativo del revisore                                     |
| `created_at`         | Data della revisione                                            |

**Chi lo crea**
HCAIRE, utente autorizzato o sistema

**Chi lo usa**

* HCAIRE
* utente
* storico del documento

**Relazioni principali**

* appartiene a un output

---

## 3.6 SourceDocument

**Che cos’è**
Fonte esterna o interna non fondativa, usata per supportare la generazione.

| Dato elementare | Descrizione                                                     |
| --------------- | --------------------------------------------------------------- |
| `id`            | Identificatore della fonte                                      |
| `title`         | Titolo della fonte                                              |
| `source_type`   | Tipo: articolo, paper, linea guida, file caricato, nota interna |
| `citation`      | Riferimento bibliografico o descrittivo                         |
| `url`           | Collegamento esterno, se esiste                                 |
| `summary`       | Sintesi della fonte                                             |
| `status`        | Stato della fonte nel sistema                                   |
| `metadata_json` | Metadati aggiuntivi strutturati                                 |

**Chi lo crea**
Sistema o HCAIRE; talvolta utente tramite upload

**Chi lo usa**

* motore di ricerca
* piano di generazione
* output

**Relazioni principali**

* può essere selezionata nel piano di generazione
* può essere citata negli output

---

# 4. DATI DI GOVERNANCE E PERSONALIZZAZIONE

## 4.1 UserCustomizationProfile

**Che cos’è**
Profilo di personalizzazione creato dall’utente.

| Dato elementare          | Descrizione                               |
| ------------------------ | ----------------------------------------- |
| `id`                     | Identificatore del profilo                |
| `user_id`                | Utente proprietario                       |
| `name`                   | Nome del profilo                          |
| `target_audience`        | Destinatario desiderato dei testi         |
| `tone`                   | Tono preferito                            |
| `technical_level`        | Livello di tecnicità richiesto            |
| `preferred_output_types` | Tipi di output preferiti                  |
| `depth_level`            | Livello di approfondimento desiderato     |
| `explicit_theory_level`  | Quanto rendere visibile il quadro teorico |
| `constraints`            | Vincoli aggiuntivi                        |
| `status`                 | Stato del profilo                         |

**Chi lo crea**
Utente

**Chi lo usa**

* piano di generazione
* selezione skill
* output

**Relazioni principali**

* può essere collegato a skill di personalizzazione
* viene applicato nei piani di generazione

---

## 4.2 GovernanceDecision

**Che cos’è**
Decisione formale del comitato HCAIRE relativa a un oggetto del sistema.

| Dato elementare  | Descrizione                                                       |
| ---------------- | ----------------------------------------------------------------- |
| `id`             | Identificatore della decisione                                    |
| `entity_type`    | Tipo di oggetto interessato                                       |
| `entity_id`      | Identificativo dell’oggetto interessato                           |
| `decision_type`  | Tipo di decisione: approvazione, revisione, ritiro, pubblicazione |
| `decision_notes` | Motivazione della decisione                                       |
| `approved_by`    | Identificativo del decisore                                       |
| `created_at`     | Data della decisione                                              |

**Chi lo crea**
Comitato HCAIRE

**Chi lo usa**

* governance interna
* log di trasparenza
* workflow approvativi

**Relazioni principali**

* si applica a documenti, nodi, schede, skill, output

---

## 4.3 User

**Che cos’è**
Soggetto che usa la webapp.

| Dato elementare | Descrizione                                               |
| --------------- | --------------------------------------------------------- |
| `id`            | Identificatore dell’utente                                |
| `name`          | Nome visualizzato                                         |
| `email`         | Indirizzo email                                           |
| `role`          | Ruolo: admin HCAIRE, redattore, revisore, utente standard |
| `status`        | Stato account                                             |
| `created_at`    | Data di creazione account                                 |

**Chi lo crea**
Sistema / HCAIRE / utente stesso

**Chi lo usa**

* autenticazione
* workflow
* tracciamento azioni

**Relazioni principali**

* crea tracce
* può avere profili di personalizzazione
* può approvare o revisionare oggetti

---

# 5. TABELLE DI RELAZIONE MOLTI-A-MOLTI

Questi non sono “contenuti” ma legami strutturali molto importanti.

## 5.1 FoundationDocument ↔ ConceptNode

Un documento fondativo può collegarsi a molti nodi, e un nodo può essere sostenuto da più documenti.

| Dato elementare          | Descrizione                                           |
| ------------------------ | ----------------------------------------------------- |
| `foundation_document_id` | Documento fondativo                                   |
| `concept_node_id`        | Nodo collegato                                        |
| `relation_type`          | Tipo di relazione: origine, supporto, approfondimento |

---

## 5.2 AreaSheet ↔ ConceptNode

Una scheda di ambito usa molti nodi, e ogni nodo entra in molte schede.

| Dato elementare    | Descrizione                       |
| ------------------ | --------------------------------- |
| `area_sheet_id`    | Scheda di ambito                  |
| `concept_node_id`  | Nodo collegato                    |
| `priority_in_area` | Priorità del nodo in quell’ambito |

---

## 5.3 Skill ↔ ConceptNode

| Dato elementare   | Descrizione                      |
| ----------------- | -------------------------------- |
| `skill_id`        | Skill collegata                  |
| `concept_node_id` | Nodo collegato                   |
| `relation_type`   | Tipo di uso del nodo nella skill |

---

## 5.4 Skill ↔ DomainArea

| Dato elementare  | Descrizione          |
| ---------------- | -------------------- |
| `skill_id`       | Skill collegata      |
| `domain_area_id` | Ambito collegato     |
| `relation_type`  | Tipo di collegamento |

---

## 5.5 TraceInterpretation ↔ ConceptNode

| Dato elementare           | Descrizione                            |
| ------------------------- | -------------------------------------- |
| `trace_interpretation_id` | Interpretazione della traccia          |
| `concept_node_id`         | Nodo attivato                          |
| `confidence`              | Livello di confidenza dell’attivazione |

---

## 5.6 TraceInterpretation ↔ DomainArea

| Dato elementare           | Descrizione                            |
| ------------------------- | -------------------------------------- |
| `trace_interpretation_id` | Interpretazione della traccia          |
| `domain_area_id`          | Ambito attivato                        |
| `confidence`              | Livello di confidenza dell’attivazione |

---

# 6. LETTURA SEMPLICE DEL FLUSSO DATI

Te lo sintetizzo in forma lineare.

## Flusso 1 — Costruzione del patrimonio HCAIRE

`FoundationDocument`
→ genera `ConceptNode`, `TranslationRule`, `AreaSheet`, `Skill`

## Flusso 2 — Arrivo della richiesta

`InputTrace` + `UserCustomizationProfile`
→ genera `TraceInterpretation`

## Flusso 3 — Preparazione della risposta

`TraceInterpretation`
→ genera `GenerationPlan`

## Flusso 4 — Produzione

`GenerationPlan` + eventuali `SourceDocument`
→ genera `OutputDocument`

## Flusso 5 — Controllo ed evoluzione

`OutputDocument`
→ può generare `OutputRevision`
→ può portare a nuove `GovernanceDecision`

---

# 7. OSSERVAZIONE IMPORTANTE SUL LIVELLO DI GRANULARITÀ

Per partire bene, ti consiglierei di distinguere da subito due livelli:

## Livello 1 — Oggetti editoriali

Documenti, nodi, schede, output

## Livello 2 — Oggetti di processo

Interpretazioni, piani di generazione, revisioni, decisioni

Questa distinzione ti evita di confondere:

* ciò che Bartleby “sa”
  con
* ciò che Bartleby “fa”

---

