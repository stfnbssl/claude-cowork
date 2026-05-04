Nel primo step io prevedrei **due agenti leggeri**, non uno solo.

Non perché sia impossibile farlo con un agente unico, ma perché nello scouting iniziale conviene separare:

* **raccolta/estrazione**
* **normalizzazione/filtraggio**

Se metti tutto in un solo agente, tende a fare confusione tra ciò che trova, ciò che deduce e ciò che scarta. Nel tuo caso, dove poi vuoi far passare dati strutturati agli step successivi, questa separazione è utile fin dall’inizio.

# Step 1 — Scouting iniziale

## Obiettivo

Costruire un insieme di **evidenze grezze ma già classificate**, senza ancora fare vera valutazione comparativa.

Lo step 1 deve rispondere a domande come:

* quali aziende compaiono?
* in quali settori?
* su quali processi aziendali si parla di AI?
* quali fonti parlano di implementazioni reali e quali solo di intenzioni?
* quali segnali meritano approfondimento allo step 2?

---

# Proposta: 2 agenti nello step 1

## Agente 1A — Source Scout

Compito: cercare e raccogliere evidenze elementari dalle fonti.

Lavora su:

* siti investor relations
* relazioni annuali
* earnings call
* comunicati stampa
* case study vendor
* job posting
* engineering blog
* news economiche
* database brevetti o paper, se inclusi nel perimetro

### Che cosa produce

Produce una lista di **raw evidence items**.
Non deve unificare troppo. Deve essere generoso nel raccogliere, ma disciplinato nel classificare.

### Regola chiave

Non deve dire:
“questa azienda è matura nell’AI”.

Deve dire:
“questa fonte contiene un segnale che suggerisce AI in questo processo”.

---

## Agente 1B — Signal Normalizer

Compito: prendere le evidenze raccolte dal primo agente e renderle uniformi, deduplicate e ordinabili.

Fa:

* deduplicazione
* normalizzazione nomi azienda
* classificazione del tipo di processo
* classificazione del tipo di caso d’uso
* prima stima della forza del segnale
* prima distinzione tra claimed / inferred / observed
* raggruppamento preliminare per azienda

### Che cosa produce

Produce un output già pronto per lo step 2:

* evidenze pulite
* cluster preliminari per azienda
* candidati use case da approfondire

---

# Perché 2 agenti e non 1

Per una ragione metodologica importante.

Il primo agente deve avere **alta recall**: trovare tanto.

Il secondo deve avere **ordine epistemico**: non lasciarti entrare nel passo successivo con materiale caotico.

Se il medesimo agente fa entrambe le cose, spesso:

* o raccoglie troppo poco
* o struttura male
* o introduce giudizi prematuri

---

# Unità minima prodotta dallo step 1

L’unità fondamentale non è ancora il “caso aziendale”, ma la:

## Evidence Item

cioè un singolo fatto o segnale documentato.

Esempi:

* una frase in una earnings call
* una job posting su AI governance
* un case study AWS con un cliente nominato
* una news Reuters su partnership AI
* una pagina prodotto che annuncia un assistant interno
* un report annuale che cita automazione AI di un workflow

Lo step 2 poi userà questi evidence item per costruire schede aziendali.

---

# Schema JSON di output dello Step 1

Ti propongo una struttura a tre livelli:

1. **run metadata**
2. **evidence items**
3. **preliminary company clusters**

Così hai già sia il livello granulare sia quello aggregato.

```json
{
  "run_metadata": {
    "run_id": "step1_2026_04_23_001",
    "generated_at": "2026-04-23T11:30:00+02:00",
    "scope": {
      "geography": ["global"],
      "languages": ["it", "en"],
      "target_sectors": [],
      "target_functions": [],
      "time_window": {
        "start": "2025-01-01",
        "end": "2026-04-23"
      }
    },
    "agent_versions": {
      "source_scout": "v1.0",
      "signal_normalizer": "v1.0"
    }
  },
  "evidence_items": [
    {
      "evidence_id": "ev_0001",
      "company_name_raw": "Example Corp.",
      "company_name_normalized": "Example Corp",
      "sector": "software",
      "source_type": "earnings_call",
      "source_title": "Q1 2026 Earnings Call Transcript",
      "source_url": "https://example.com/q1-2026-call",
      "publisher": "Example Corp Investor Relations",
      "publication_date": "2026-03-18",
      "retrieval_date": "2026-04-23",
      "claim_excerpt": "We are deploying generative AI across customer support and internal engineering workflows.",
      "claim_summary": "L'azienda dichiara implementazioni di AI generativa nel supporto clienti e nei workflow di engineering interni.",
      "ai_capability_tags": [
        "generative_ai",
        "copilot",
        "workflow_automation"
      ],
      "business_function_tags": [
        "customer_service",
        "software_engineering",
        "internal_operations"
      ],
      "use_case_tags": [
        "agent_assistance",
        "knowledge_retrieval",
        "developer_productivity"
      ],
      "implementation_stage_hint": "rollout_claimed",
      "evidence_type": "claimed",
      "evidence_strength_preliminary": 4,
      "quant_metrics_present": false,
      "metrics": [],
      "vendor_partners": [],
      "region_tags": [],
      "notes": "Dichiarazione aziendale in fonte primaria ma senza metriche.",
      "dedup_group_key": "examplecorp_support_engineering_genai_q12026",
      "confidence_preliminary": 0.74
    }
  ],
  "preliminary_company_clusters": [
    {
      "cluster_id": "cl_0001",
      "company_name_normalized": "Example Corp",
      "sector": "software",
      "evidence_ids": ["ev_0001", "ev_0004", "ev_0007"],
      "suspected_use_cases": [
        {
          "label": "AI per customer support",
          "business_function_tags": ["customer_service"],
          "use_case_tags": [
            "agent_assistance",
            "knowledge_retrieval",
            "case_summarization"
          ]
        },
        {
          "label": "AI per engineering interno",
          "business_function_tags": ["software_engineering"],
          "use_case_tags": [
            "developer_productivity",
            "code_assistance",
            "documentation_generation"
          ]
        }
      ],
      "source_mix": {
        "primary_sources": 2,
        "secondary_sources": 1,
        "vendor_case_studies": 0,
        "jobs": 1,
        "news": 0
      },
      "signal_density": "medium",
      "next_step_priority": "high",
      "normalizer_notes": "C'è convergenza tra fonti aziendali e assunzioni, ma mancano metriche operative."
    }
  ],
  "step1_summary": {
    "companies_detected": 18,
    "evidence_items_count": 74,
    "high_priority_clusters": 6,
    "dominant_business_functions": [
      "customer_service",
      "software_engineering",
      "marketing",
      "internal_operations"
    ],
    "dominant_ai_capabilities": [
      "generative_ai",
      "agent_assistance",
      "knowledge_retrieval",
      "workflow_automation"
    ],
    "notes": "Dataset di scouting preliminare, non ancora validato comparativamente."
  }
}
```

---

# Osservazioni sul JSON

## 1. `evidence_type`

Io inserirei già qui una tripartizione forte:

* `claimed`
* `observed`
* `inferred`

Dove:

* **claimed** = la fonte dichiara esplicitamente qualcosa
* **observed** = il contenuto mostra un fatto operativo abbastanza diretto
* **inferred** = il segnale è dedotto indirettamente, per esempio da assunzioni o partnership

Questa distinzione è preziosa.

---

## 2. `implementation_stage_hint`

Non farei ancora una classificazione troppo sofisticata, ma almeno:

* `research_or_exploration`
* `pilot_claimed`
* `rollout_claimed`
* `production_indicated`
* `unclear`

Serve solo a guidare lo step 2.

---

## 3. `evidence_strength_preliminary`

Può essere una scala semplice 1–5.

Per esempio:

* 1 = segnale debole
* 2 = segnale plausibile ma indiretto
* 3 = dichiarazione esplicita ma poco concreta
* 4 = dichiarazione esplicita in fonte primaria o evidenza convergente
* 5 = fonte primaria con metriche o prova operativa forte

---

## 4. `dedup_group_key`

È utile perché nello scouting troverai dieci versioni quasi uguali dello stesso annuncio.

---

# Output minimo alternativo, più semplice

Se vuoi partire ancora più leggero, puoi ridurre lo step 1 a due soli blocchi:

```json
{
  "evidence_items": [],
  "company_candidates": []
}
```

Ma secondo me perdi troppo presto informazione utile. La versione sopra è un buon compromesso.

---

# Prompt per l’Agente 1A — Source Scout

Ti propongo una prima versione già abbastanza pulita.

Sei un agente di scouting documentale.
Il tuo compito è raccogliere evidenze elementari su come le aziende stanno implementando tecniche di intelligenza artificiale per ottimizzare i propri processi.

Obiettivo:

* trovare segnali documentati relativi a uso dell’AI in processi aziendali
* estrarre evidenze puntuali senza fare ancora una valutazione comparativa complessiva
* produrre un output JSON conforme allo schema richiesto

Regole:

* lavora a livello di singola evidenza
* non sintetizzare prematuramente un intero profilo aziendale
* non dedurre maturità complessiva dell’azienda
* distingui ciò che è esplicitamente dichiarato da ciò che è soltanto suggerito
* privilegia fonti primarie quando disponibili
* conserva la formulazione più concreta possibile del claim
* se una fonte è vaga, registrala come vaga, non colmare i vuoti
* se non trovi metriche, indica esplicitamente che mancano

Per ogni evidenza, cerca di identificare:

* azienda
* settore
* tipo di fonte
* titolo della fonte
* URL
* data
* estratto o claim rilevante
* sintesi del claim
* funzione aziendale coinvolta
* caso d’uso AI
* indizio di stadio di implementazione
* presenza o assenza di metriche
* eventuali partner o vendor citati
* tipo di evidenza: claimed, observed, inferred
* forza preliminare del segnale

Criteri di classificazione:

* "claimed" = la fonte dichiara esplicitamente un uso o un progetto AI
* "observed" = la fonte documenta in modo abbastanza diretto un fatto operativo, una funzionalità, una demo concreta, una testimonianza tecnica o un rollout verificabile
* "inferred" = l’uso AI è soltanto dedotto da segnali indiretti, come job posting, partnership, linguaggio di prodotto, riorganizzazioni, competenze cercate

Non introdurre informazioni non presenti o non ragionevolmente deducibili dalla fonte.
Non unire evidenze diverse nello stesso record.
Meglio due record distinti che uno troppo sintetico.

Output:
restituisci solo JSON valido, senza commenti fuori dal JSON.

---

# Prompt per l’Agente 1B — Signal Normalizer

Sei un agente di normalizzazione e filtraggio.
Ricevi in input un insieme di evidence items raccolti da uno scout documentale.
Il tuo compito è pulire, uniformare, deduplicare e raggruppare preliminarmente queste evidenze per prepararle allo step successivo.

Obiettivi:

* normalizzare i nomi aziendali
* correggere incoerenze tassonomiche
* deduplicare record quasi identici
* uniformare i tag relativi a funzioni aziendali e casi d’uso
* stimare la priorità di approfondimento
* costruire cluster preliminari per azienda

Regole:

* non inventare nuove evidenze
* non rimuovere in modo aggressivo segnali deboli: segnali deboli possono restare, ma devono essere marcati come tali
* non trasformare evidenze deboli in evidenze forti
* non attribuire maturità finale all’azienda
* usa i campi già presenti e correggili solo quando l’incoerenza è evidente
* conserva traccia delle evidenze originali tramite evidence_id

Operazioni richieste:

1. normalizza company_name_raw in company_name_normalized
2. uniforma sector, business_function_tags, use_case_tags, ai_capability_tags
3. individua duplicati o quasi duplicati
4. assegna o correggi dedup_group_key
5. crea preliminary_company_clusters
6. assegna next_step_priority ai cluster
7. produci un breve step1_summary

Criteri per next_step_priority:

* high = più fonti convergenti o almeno una fonte primaria forte
* medium = segnali plausibili ma ancora incompleti
* low = segnali isolati, vaghi o scarsamente utilizzabili

Output:
restituisci solo JSON valido conforme allo schema di step 1 arricchito e normalizzato.

---

# Tassonomie minime da fissare subito

Ti consiglio di fissarne poche, altrimenti esplodono.

## `source_type`

Esempio:

* annual_report
* earnings_call
* investor_presentation
* press_release
* company_blog
* engineering_blog
* vendor_case_study
* job_posting
* news_article
* patent
* research_paper
* product_page

## `business_function_tags`

Esempio:

* customer_service
* marketing
* sales
* software_engineering
* finance
* hr
* procurement
* operations
* manufacturing
* supply_chain
* legal
* compliance
* cybersecurity
* r_and_d
* it_internal

## `use_case_tags`

Esempio:

* agent_assistance
* knowledge_retrieval
* document_processing
* forecasting
* anomaly_detection
* predictive_maintenance
* code_assistance
* customer_chatbot
* personalization
* content_generation
* decision_support
* workflow_automation
* fraud_detection
* quality_inspection
* search_and_discovery

---

# Mia raccomandazione pratica

Per partire davvero, non complicherei ancora il primo step con troppi agenti specializzati per fonte.
Farei così:

* **1A scout generale**
* **1B normalizer**

Poi, se funziona, potresti specializzare il primo agente in sottotipi:

* scout financial sources
* scout vendor case studies
* scout job signals
* scout press/news

Ma come prima versione, due agenti bastano.

---

# Giudizio netto

Quindi: **sì, nello step 1 prevederei più di un agente**, ma resterei su **due**.

Uno solo è troppo confuso.
Tre o quattro, all’inizio, sono probabilmente troppi.

La soluzione a due agenti ti dà già:

* buona recall
* ordine nei dati
* passaggio pulito allo step 2

Nel prossimo passaggio possiamo fare due cose molto utili: scrivere un **JSON schema formale**, con tipi e campi obbligatori/facoltativi, oppure affinare i prompt del primo agente distinguendo fra **ricerca larga** e **ricerca mirata per azienda/settore**.
