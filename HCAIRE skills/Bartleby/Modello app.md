# 1. Principio architetturale di base

Io distinguerei subito tre grandi famiglie di dati:

## A. Dati fondativi

Sono i contenuti prodotti e governati da HCAIRE.

Esempi:

* carta fondativa;
* concetti strutturali;
* nodi trasversali;
* matrici di traduzione interdisciplinare;
* schede di ambito;
* regole di traducibilità;
* criteri di qualità;
* skill di base.

Questi dati sono il **patrimonio epistemico** del sistema Bartleby.

## B. Dati di esecuzione

Sono i dati usati quando Bartleby lavora su una richiesta concreta.

Esempi:

* traccia utente;
* classificazione della traccia;
* nodi attivati;
* ambiti attivati;
* skill selezionate;
* piano di generazione;
* bozze;
* revisioni;
* output finale.

Questi dati sono il **processo operativo**.

## C. Dati di personalizzazione e governance

Sono i dati che modulano il comportamento del sistema e ne governano l’evoluzione.

Esempi:

* profili utente;
* skill di personalizzazione;
* ruoli e permessi;
* versioni dei documenti HCAIRE;
* approvazioni del comitato;
* log di utilizzo;
* valutazioni di qualità.

Questi dati sono il **livello gestionale e istituzionale**.

---

# 2. Il modello dati: entità principali

Qui conviene pensare in termini di oggetti chiari.
Ti propongo un primo modello logico.

## 2.1 FoundationDocument

Rappresenta un documento fondativo HCAIRE.

Esempi:

* Carta fondativa
* Motore di traducibilità
* Matrice interdisciplinare
* Atlante dei nodi trasversali

### Campi principali

* `id`
* `type`
  esempio: `foundational_charter`, `translation_engine`, `interdisciplinary_matrix`
* `title`
* `slug`
* `summary`
* `body`
* `status`
  draft, approved, archived
* `version`
* `created_by`
* `approved_by`
* `created_at`
* `updated_at`

Questo oggetto è importante perché ti permette di avere documenti “madre”.

---

## 2.2 ConceptNode

Rappresenta un concetto o nodo strutturale del modello.

Esempi:

* relazione adulto-bambino
* regolazione/co-regolazione
* linguaggio e significato condiviso

### Campi

* `id`
* `name`
* `slug`
* `definition`
* `why_transversal`
* `priority_level`
* `status`
* `version`
* `source_document_id`

### Relazioni

* collegato a più ambiti
* collegato a più documenti fondativi
* collegato a più skill
* collegato a più output generati

Questo è uno degli oggetti più importanti dell’intero sistema.

---

## 2.3 DomainArea

Rappresenta un ambito.

Esempi:

* genitoriale
* pedagogico
* clinico
* sociale
* politico

### Campi

* `id`
* `name`
* `slug`
* `description`
* `purpose`
* `language_style`
* `risk_profile`
* `status`
* `version`

---

## 2.4 AreaSheet

Rappresenta la scheda di ambito completa.

### Campi

* `id`
* `domain_area_id`
* `title`
* `scope`
* `main_focus`
* `translation_of_model`
* `priority_dimensions`
* `typical_configurations`
* `reduction_risks`
* `guiding_questions`
* `allowed_output_types`
* `language_rules`
* `operational_cautions`
* `quality_indicators`
* `version`
* `status`

### Nota

`DomainArea` può essere l’identità sintetica dell’ambito, mentre `AreaSheet` è la sua formalizzazione operativa versionata.

---

## 2.5 TranslationRule

Rappresenta una regola di traducibilità.

Esempi:

* “non ridurre il linguaggio a numero di parole”
* “in ambito clinico distinguere osservazione e ipotesi”
* “in ambito genitoriale evitare tono colpevolizzante”

### Campi

* `id`
* `title`
* `rule_type`
  interpretive, linguistic, safety, quality
* `rule_text`
* `applies_to_scope`
  foundation, area, node, output_type
* `scope_id`
* `priority`
* `status`
* `version`

---

## 2.6 Skill

Qui è importante definire bene cosa intendi.

Io la modellerei come **unità operativa derivata**.

### Tipi di skill

* fondativa
* di ambito
* di nodo
* di personalizzazione
* di output

### Campi

* `id`
* `name`
* `slug`
* `skill_type`
* `description`
* `instruction_payload`
* `status`
* `version`
* `owner_type`
  hcaire, user
* `owner_id`

### Relazioni

* può derivare da più documenti
* può essere collegata a più nodi
* può essere collegata a più ambiti

`instruction_payload` può contenere JSON strutturato anziché solo testo libero.

---

## 2.7 UserCustomizationProfile

Rappresenta la personalizzazione utente.

### Campi

* `id`
* `user_id`
* `name`
* `target_audience`
* `tone`
* `technical_level`
* `preferred_output_types`
* `depth_level`
* `explicit_theory_level`
* `constraints`
* `status`

---

## 2.8 InputTrace

Rappresenta la traccia fornita dall’utente.

### Campi

* `id`
* `user_id`
* `title`
* `raw_text`
* `context_notes`
* `target_output_type`
* `requested_area_id` nullable
* `status`
* `created_at`

---

## 2.9 TraceInterpretation

È il cuore del processo intermedio.

### Campi

* `id`
* `input_trace_id`
* `reformulated_trace`
* `detected_nodes`
* `detected_areas`
* `detected_risks`
* `interpretation_notes`
* `confidence_level`
* `generated_at`

Questo oggetto è fondamentale perché rende visibile il passaggio dalla traccia al modello.

---

## 2.10 GenerationPlan

Rappresenta il piano con cui Bartleby decide cosa usare.

### Campi

* `id`
* `input_trace_id`
* `trace_interpretation_id`
* `selected_foundation_documents`
* `selected_area_sheets`
* `selected_nodes`
* `selected_skills`
* `selected_translation_rules`
* `selected_customizations`
* `selected_sources`
* `generation_strategy`
* `status`

---

## 2.11 OutputDocument

Rappresenta il documento prodotto.

### Campi

* `id`
* `input_trace_id`
* `generation_plan_id`
* `output_type`
* `title`
* `body`
* `audience`
* `area_id`
* `status`
* `version`
* `created_at`

---

## 2.12 OutputRevision

Serve a tenere traccia delle revisioni.

### Campi

* `id`
* `output_document_id`
* `revision_type`
* `revision_notes`
* `body`
* `reviewed_by`
* `created_at`

---

## 2.13 SourceDocument

Se prevedi ricerca fonti, va separato dai documenti HCAIRE.

### Campi

* `id`
* `title`
* `source_type`
  article, paper, guideline, uploaded_doc, internal_note
* `citation`
* `url`
* `summary`
* `status`
* `metadata_json`

---

## 2.14 GovernanceDecision

Perché hai un comitato di direzione.

### Campi

* `id`
* `entity_type`
* `entity_id`
* `decision_type`
* `decision_notes`
* `approved_by`
* `created_at`

Questo rende visibile che i contenuti HCAIRE non sono “emersi automaticamente”, ma sono governati.

---

# 3. Relazioni tra i dati

Qui il punto decisivo è che Bartleby non è lineare, ma reticolare.

## Relazioni chiave

### Un FoundationDocument

può generare molti ConceptNode, molte TranslationRule, molte Skill.

### Un ConceptNode

può appartenere a molti DomainArea.

### Un DomainArea

può avere una o più AreaSheet versionate.

### Una Skill

può derivare da:

* un documento fondativo,
* un nodo,
* un ambito,
* oppure da un profilo utente.

### Una InputTrace

genera una TraceInterpretation.

### Una TraceInterpretation

attiva:

* nodi,
* ambiti,
* skill,
* regole di traducibilità.

### Un GenerationPlan

usa questi elementi per produrre uno o più OutputDocument.

Questa struttura è più simile a un **grafo semantico con versioning** che a un semplice archivio di pagine.

---

# 4. Schema concettuale del flusso

Ti propongo il flusso principale in forma semplice.

## Flusso A — Produzione dei contenuti base HCAIRE

1. HCAIRE redige o aggiorna documenti fondativi.
2. Dai documenti si estraggono o si definiscono:

   * nodi,
   * ambiti,
   * regole,
   * skill.
3. Il comitato approva.
4. Questi contenuti diventano “pubblicati” e utilizzabili dal motore.

## Flusso B — Produzione di output su traccia utente

1. L’utente inserisce una traccia.
2. Bartleby interpreta la traccia.
3. Identifica nodi e ambiti rilevanti.
4. Seleziona skill e regole.
5. Costruisce un piano di generazione.
6. Produce una bozza.
7. Applica eventuale revisione.
8. Rende visibile output + albero dei legami usati.

## Flusso C — Evoluzione del sistema

1. HCAIRE osserva gli output prodotti.
2. Valuta criticità e lacune.
3. Aggiorna documenti, nodi, ambiti, skill.
4. Nuove versioni entrano in produzione.

Questo è molto importante: la webapp non deve essere solo generativa, ma **riflessiva e migliorabile**.

---

# 5. Come renderlo visibile nella webapp “in modo naturale”

Qui c’è un punto molto bello del tuo progetto: i dati fondativi devono essere visibili e il loro collegamento deve apparire naturale.

Io eviterei una presentazione solo archivistica.
Meglio mostrare i contenuti come **mappa navigabile**.

## 5.1 Vista “Mappa del modello”

Una pagina dove l’utente vede:

* Fondamenti
* Nodi trasversali
* Ambiti
* Skill
* Tipi di output

Con collegamenti cliccabili.

Esempio naturale di navigazione:

* clicco su “Relazione adulto-bambino”
* vedo definizione
* vedo in quali ambiti entra
* vedo quali skill usa
* vedo esempi di output collegati

Questa è una visualizzazione molto coerente con il tuo progetto.

---

## 5.2 Vista “Scheda oggetto”

Ogni entità importante ha una pagina propria.

Per esempio, la pagina di un nodo mostra:

* definizione;
* motivo della trasversalità;
* documenti fondativi di origine;
* ambiti in cui è prioritario;
* skill derivate;
* output esemplificativi.

Così il legame appare naturale perché è esposto come genealogia e rete.

---

## 5.3 Vista “Come è stato generato questo output”

Questa, secondo me, è una funzione decisiva.

Ogni output dovrebbe avere una sezione tipo:

**Questo documento è stato generato usando:**

* 2 fondamenti HCAIRE
* 1 scheda di ambito
* 3 nodi trasversali
* 1 skill di personalizzazione utente

Questa trasparenza è molto forte.

---

## 5.4 Vista “Percorsi”

Potresti offrire percorsi di lettura:

* dai fondamenti agli ambiti
* dai nodi agli output
* dalla traccia al documento finale

Questo aiuta sia utenti normali sia interlocutori scientifici.

---

# 6. Modello logico minimo delle tabelle

A livello pratico, per una prima versione, io farei così:

## Tabelle principali

* `foundation_documents`
* `concept_nodes`
* `domain_areas`
* `area_sheets`
* `translation_rules`
* `skills`
* `user_customization_profiles`
* `input_traces`
* `trace_interpretations`
* `generation_plans`
* `output_documents`
* `output_revisions`
* `source_documents`
* `governance_decisions`

## Tabelle ponte

Perché le relazioni sono molte-a-molte:

* `foundation_document_nodes`
* `foundation_document_skills`
* `area_sheet_nodes`
* `skills_nodes`
* `skills_areas`
* `trace_interpretation_nodes`
* `trace_interpretation_areas`
* `generation_plan_skills`
* `generation_plan_rules`
* `output_document_nodes`

Questa struttura relazionale va benissimo per una prima implementazione in MongoDB o PostgreSQL.
Se vuoi forte navigabilità semantica, nel tempo potresti anche affiancare un grafo.

---

# 7. Scelta tecnica consigliata

Dato il tuo contesto progettuale, farei così:

## Primo stadio

**PostgreSQL**
per i dati strutturati e versionati.

Perché:

* relazioni solide;
* versioning gestibile;
* query chiare;
* ottimo per app serie.

## Secondo stadio

Aggiungere:

* `pgvector` per retrieval semantico;
* eventualmente un livello grafo logico applicativo.

Non partirei subito con Neo4j o sistemi troppo sofisticati. Prima serve chiarezza del modello.

---

# 8. Punto molto importante: distinguere contenuto e derivazione

Ogni oggetto dovrebbe avere campi come:

* `source_type`: `hcaire`, `user`, `system`
* `derived_from`
* `version`
* `approval_status`

Per esempio:

* un nodo è prodotto da HCAIRE;
* una skill utente è prodotta da utente;
* un piano di generazione è prodotto dal sistema.

Questo ti permette di spiegare bene l’origine dei dati.

---

# 9. Un primo diagramma concettuale in parole

Te lo scrivo in forma compatta:

**Fondamenti HCAIRE**
→ generano **nodi**, **regole**, **schede di ambito**, **skill di base**
→ questi formano il **motore di conoscenza**

**Traccia utente** + **profilo utente**
→ vengono interpretati dal motore
→ producono **piano di generazione**

**Piano di generazione** + **fonti esterne**
→ producono **output**

**Output**
→ possono essere revisionati
→ e alimentano miglioramento del motore

Questa è già una buona architettura da mostrare.

---

# 10. Cosa ti consiglierei di fare subito

Per non disperderti, partirei da tre artefatti progettuali:

## A. Dizionario delle entità

Una pagina per ogni tipo di dato:

* nome
* funzione
* campi essenziali
* relazioni

## B. Diagramma dei flussi

Tre flussi:

* produzione HCAIRE
* generazione output
* revisione/evoluzione

## C. Regole di visibilità

Per ogni oggetto decidere:

* è interno o pubblico?
* è modificabile da chi?
* è approvato o solo bozza?
* compare nella webapp pubblica o solo in area di lavoro?

---

# 11. Il punto più delicato da non sbagliare

Secondo me è questo:

**non modellare le skill come semplici prompt testuali sparsi.**

Perché se fai così:

* perdi trasparenza,
* perdi riuso,
* perdi governabilità.

Le skill devono essere oggetti collegati a:

* fondamenti,
* nodi,
* ambiti,
* personalizzazioni.

Solo così Bartleby rimane leggibile.

