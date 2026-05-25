# D11 — Area pubblica di visualizzazione degli strumenti finali

> **Scopo del documento.** Specificare la **nuova area pubblica** del sito HCAIRE che mostra al pubblico gli strumenti finali prodotti dalla pipeline "Produzioni". Definisce: cosa è uno "strumento finale" pubblicabile, come si compone, come si organizza la navigazione, come il dato JSON tecnico diventa contenuto leggibile, il criterio di pubblicabilità e il workflow editoriale, il rapporto con l'area riservata, il modello di accesso e ruoli, gli endpoint API, e il vincolo metodologico non-prescrittivo come requisito verificabile.
>
> **Statuto.** Documento di **progettazione**, non di implementazione. È la sorgente di verità per una successiva fase di costruzione (a carico di Claude Code per backend/frontend). Dove tocca documenti esistenti, lo segnala esplicitamente (§11).
>
> **Destinatario**: il ricercatore (validazione delle scelte di progetto) e Claude Code (implementazione successiva).
>
> **Data**: 2026-05-24 · **Stato**: specifica iniziale (v1).
>
> **Leggere prima**: `D4` (API e modello di autenticazione), `D5` (frontend, `useIsAdmin`), `D5b` (area riservata — laboratorio workbench), `D8` (output-tipo contestualizzato — F3 step 5), `D9` (modulo F3-SIT). Contesto: `Storage dati e schemi pipeline.md`, `Ripartenza — area pubblica strumenti finali.md`.

---

## 1. Sintesi e scopo

La pipeline "Produzioni" costruisce dispositivi di lettura configurazionale a partire da fenomeni dello sviluppo infantile. Oggi **tutti** i suoi output — strutturali, intermedi, tecnici — sono esposti pubblicamente: `D4` §1.1 stabilisce che ogni endpoint `GET` è `public`, e `D5` §0 che l'interfaccia read-only è visibile a chiunque. Questo è inadeguato: gli output intermedi (assi, nodi, CE, stress test, JSON di metodo) sono **strumenti di lavoro del progettista**, non contenuti per il pubblico.

D11 separa la fruizione in due aree distinte:

**Area riservata (progettisti / ricercatori).** L'esecuzione della pipeline e la visualizzazione di tutti gli output intermedi (F2, F3, F3-SIT, JSON, verifiche, stress test). È il **Laboratorio** già specificato in `D5b`, più le attuali pagine read-only della pipeline. Riservata: per ora accessibile al solo ruolo `admin`.

**Area pubblica (strumenti finali approvati).** Una visualizzazione **leggibile e non tecnica** degli strumenti contestualizzati approvati. È la nuova area che questo documento progetta. Per ora visibile a tutti gli utenti; il modello prevede un livello futuro riservato agli abbonati senza implementarlo subito.

Le sette decisioni di progetto della §4 del documento di ripartenza sono state risolte (sintesi in §13.1) e sono incorporate nelle sezioni che seguono.

---

## 2. Le due aree

### 2.1 Stato attuale e cosa cambia

| Aspetto | Stato attuale (D4/D5) | Stato D11 |
|---|---|---|
| Output intermedi pipeline (F2, F3 step 1–4, F3-SIT step 1–3) | Pubblici (`GET` public) | **Riservati ad admin** |
| Output finali (output-tipo F3 step 5, repertorio F3-SIT step 4) | Pubblici, in forma JSON/tecnica | **Pubblici solo se approvati**, in forma leggibile non tecnica |
| Pagine read-only pipeline (`/produzioni`, `/sviluppo-bambino`) | Visibili a tutti | **Riservate ad admin** (vedi §2.2) |
| Laboratorio workbench (`/laboratorio`) | Già admin-only (`D5b`) | Invariato |
| Area pubblica leggibile | Non esiste | **Nuova** (questo documento) |

> **Modifica a `D4`.** D11 rovescia il principio di `D4` §1.1: gli endpoint `GET /api/pipeline/*` passano da `public` ad `admin`. La nuova area pubblica non legge da quegli endpoint, ma da un namespace dedicato `/api/sviluppo-bambino/strumenti/*` (§9). Dettaglio in §11.

### 2.2 Area riservata

L'area riservata è la controparte dell'area pubblica e **non** viene riprogettata qui: è il Laboratorio di `D5b` (route `/laboratorio/...`, condizionate a `useIsAdmin()`). D11 aggiunge solo una conseguenza: anche le **pagine read-only esistenti della pipeline** — quelle che oggi mostrano gli output intermedi a chiunque — vanno riservate ad admin, perché espongono materia del progettista. Concretamente, le route `/produzioni/...` e `/sviluppo-bambino/...` che renderizzano artefatti di pipeline passano dietro al check `useIsAdmin()`, come già fa il Laboratorio. Un utente non admin che vi accede riceve un redirect all'area pubblica o una pagina "contenuto riservato".

### 2.3 Area pubblica nuova

L'area pubblica è un **nuovo set di route e componenti**, distinto dal Laboratorio admin, sotto il prefisso `/sviluppo-bambino/strumenti`. Legge dalla **stessa sorgente dati** (MongoDB, source-of-truth della pipeline — cfr. `Storage dati e schemi pipeline.md`) ma **solo il sottoinsieme pubblicato**, attraverso endpoint pubblici dedicati che non espongono mai output intermedi. Non è un'app separata con deploy proprio: vive nella stessa webapp, con separazione a livello di route, componenti, endpoint e proiezione dei dati.

```
WEBAPP HCAIRE
├── Area pubblica            /sviluppo-bambino/strumenti/...        visibilità: pubblico (+abbonato futuro)
│   └── legge da             GET /api/sviluppo-bambino/strumenti/*  → solo strumenti pubblicati, resi leggibili
├── Area riservata
│   ├── Laboratorio          /laboratorio/...      visibilità: admin           (D5b)
│   └── Read-only pipeline   /produzioni, /sviluppo-bambino   visibilità: admin (era pubblica)
│       └── legge da         GET /api/pipeline/*   → admin (era public)
```

---

## 3. L'unità di contenuto: la Scheda Strumento

### 3.1 Definizione e composizione

L'unità di contenuto dell'area pubblica è la **Scheda Strumento**: una pagina leggibile per ogni coppia **tema × dominio** (l'identità `context_id = <theme_id>--<ambito_id>` della pipeline F3). Una scheda non è un singolo file JSON: è la **composizione** di due output finali della pipeline, con ruoli distinti.

**Cornice (introduzione e quadro di lettura) — dall'output-tipo contestualizzato (F3 step 5).** L'output-tipo è descritto da `D8` come "pre-struttura di senso che il professionista usa per orientarsi nel campo". È scritto per un professionista del dominio, quindi **non** viene esposto integralmente: se ne usano i campi che funzionano come cornice leggibile — `narrative_synthesis`, `orientative_direction`, le sezioni A–E con il loro `linguistic_frame` ed esempi. Forniscono al lettore il "di cosa si tratta" e il "quadro di senso" prima dei materiali concreti.

**Corpo (i materiali mostrabili) — dal repertorio F3-SIT (step 4).** `D9` §1 definisce F3-SIT come ciò che "rende il metodo visibile, comunicabile e trasferibile": casistiche, frasi, schede di atteggiamento, vignette, linee guida. È il livello concretamente mostrabile. Il corpo della scheda è il repertorio F3-SIT validato, reso in forma narrativa e organizzato per famiglia.

```
SCHEDA STRUMENTO  (tema × dominio)
┌─────────────────────────────────────────────────────────────┐
│  CORNICE   ← output-tipo contestualizzato (F3 step 5)         │
│  · titolo del fenomeno + contesto (context_label)            │
│  · introduzione narrativa (narrative_synthesis)              │
│  · a cosa serve (orientative_direction)                      │
│  · quadro di lettura: sezioni A–E (linguistic_frame, esempi) │
├─────────────────────────────────────────────────────────────┤
│  CORPO     ← repertorio F3-SIT (step 4 + 2 + 3)              │
│  · materiali raggruppati per famiglia                        │
│    (casistiche, frasi operatori, schede atteggiamento, …)   │
│  · ogni materiale in forma narrativa non-prescrittiva        │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Il caso "F3-SIT assente" e la soglia di pubblicabilità pubblica

F3-SIT è un **modulo opzionale** (`D9` §1.1): non tutti i dispositivi F3 lo eseguono. Una scheda può quindi trovarsi in due stati di completezza:

- **Tema × dominio con repertorio F3-SIT.** Ha corpo e cornice: è una scheda completa, candidabile alla pubblicazione pubblica.
- **Tema × dominio con solo output-tipo (F3 step 5), senza F3-SIT.** Ha solo la cornice. L'output-tipo da solo è scritto per un professionista del dominio: **non** è materiale per il pubblico generico. Una scheda così **non** è pubblicabile al livello `pubblico`; al più potrà essere esposta al livello `abbonato`/professionale (futuro, §8) o restare `riservato`.

**Regola di soglia.** La pubblicazione al pubblico generale (`visibility: pubblico`) **richiede** un repertorio F3-SIT con `methodological_status = validato` e `publication_recommendation.public_site = true`. L'output-tipo fornisce la cornice ma non è, da solo, una condizione sufficiente di pubblicabilità pubblica. Questo lega §3, §4 e §8 in un criterio unico (vedi gating in §7.2).

---

## 4. Modello dati della pubblicazione

### 4.1 Collezione `published_tools`

La pubblicazione introduce una nuova collezione MongoDB, `published_tools` (uno **strato editoriale** sopra i dati di pipeline; non duplica la pipeline). Un documento per ogni Scheda Strumento candidata o pubblicata.

```jsonc
{
  "_id": "ObjectId",
  "context_id": "gioco-libero-…--clinico-pediatrico",   // identità pipeline F3
  "theme_id": "gioco-libero-come-incontro-…",
  "theme_label": "Il gioco libero come incontro del bambino con il possibile",
  "ambito_id": "clinico-pediatrico",
  "domain_selected": "clinico",                          // clinico|educativo|formazione|politiche
  "context_label": "Ambulatorio pediatrico, bambini 3-5 anni, osservazione del pediatra",
  "slug": "gioco-libero-clinico",                        // slug URL pubblico, editabile

  "source_refs": {
    "output_tipo_execution_id": "ObjectId|null",         // f3_step_5
    "sit_repertorio_execution_id": "ObjectId|null",      // f3_sit_step_4
    "sit_micro_mediazioni_execution_id": "ObjectId|null", // f3_sit_step_2
    "sit_formati_execution_id": "ObjectId|null"          // f3_sit_step_3 (può mancare se saltato)
  },

  "data_gate": {                                         // valutazione automatica (§7.2, gate 1)
    "methodological_status": "validato|richiede_revisione|non_pubblicabile|null",
    "public_site_recommended": true,                     // da publication_recommendation.public_site
    "professional_training_recommended": true,
    "f3_coherence_status": "valido|richiede_revisione|fuori_modello|null",
    "passes_data_gate": false,                           // calcolato, vedi §7.2
    "evaluated_at": "ISO8601"
  },

  "publication": {                                       // strato editoriale (§7.1, gate 2)
    "status": "bozza",                                   // bozza|in_revisione|pubblicato|ritirato
    "visibility": "riservato",                           // pubblico|abbonato|riservato
    "published_at": "ISO8601|null",
    "published_by": "userId|null",
    "last_editorial_review_at": "ISO8601|null",
    "editorial_notes": "string"
  },

  "content_snapshot": { /* proiezione leggibile congelata — §5.5 */ },
  "created_at": "ISO8601",
  "updated_at": "ISO8601"
}
```

Indici: univoco su `context_id`; univoco su `slug`; su `publication.status` + `publication.visibility` + `domain_selected` per l'index pubblico.

### 4.2 Perché uno strato separato e non un flag sui dati di pipeline

La pubblicazione **non** è un campo dentro `pipeline_step_executions` per tre ragioni: (a) è una decisione editoriale, di natura diversa dallo stato di esecuzione di uno step; (b) deve sopravvivere a ri-esecuzioni della pipeline — ri-lanciare F3-SIT non deve cambiare silenziosamente cosa è pubblico; (c) compone più output (output-tipo + repertorio) in una sola unità, che nessun singolo execution rappresenta. Lo strato `published_tools` referenzia gli output di pipeline ma vive di vita propria.

---

## 5. Resa pubblica: dal JSON tecnico al contenuto leggibile

Gli output di pipeline sono JSON in linguaggio del metodo. La resa pubblica è una **proiezione narrativa selettiva**: mostra i campi leggibili, nasconde i campi di metodo, non semplifica fino a impoverire. Questa sezione è la mappa campo-per-campo della trasformazione.

### 5.1 Dalla cornice — output-tipo contestualizzato (`output-tipo-schema.json`)

| Campo sorgente | Resa pubblica | Note |
|---|---|---|
| `context_label` | Sottotitolo della scheda | Es. "Ambulatorio pediatrico, bambini 3-5 anni" |
| `narrative_synthesis` | Paragrafo introduttivo "Di cosa si tratta" | È la voce del ricercatore; si mostra integrale |
| `orientative_direction` | Riquadro "A cosa serve" | Etichettato come *orientamento*, mai come istruzione |
| `sections[].section_label` | Titolo di ciascuna delle 5 aree di lettura | A–E rinominate con il loro `section_label` leggibile |
| `sections[].linguistic_frame` | Testo dell'area di lettura | Già scritto in registro divulgativo: si mostra |
| `sections[].domain_examples` | Esempi concreti, in elenco | Si mostrano |
| `sections[].decisional_nodes` | "Domande che l'adulto/il professionista si pone" | **Resi come domande aperte**, mai come passi da eseguire (§10) |
| `dispositivo_ref.device_synthesis` | Riquadro sintetico "Come funziona, in breve" | Mostrabile in forma breve |
| `dispositivo_ref.real_time` | Indicazione di durata | Mostrabile (es. "5-10 minuti") |
| `dispositivo_ref.function_type` | — | **Nascosto**: gergo (stabilizzare/ampliare/mediare/proteggere) |
| `dispositivo_ref.resonance_indicator` | "Come accorgersene" (opzionale) | Mostrabile se riformulato in registro non tecnico |
| `step`, `tema_id`, `domain_selected` | — | Metadati di indicizzazione, non mostrati come testo |
| `operator_note` | — | **Nascosto**: nota interna |

### 5.2 Dal corpo — repertorio F3-SIT

Il file `sit-repertorio-v{N}.json` (step 4) **non contiene** il testo dei materiali: contiene la validazione (`item_checks` C1–C8), gli aggregati `repertoire[]` per famiglia con i soli `item_refs` validati, e `publication_recommendation`. Il testo dei materiali è in `sit-micro-mediazioni-v{N}.json` (famiglie 1–5) e `sit-formati-v{N}.json` (famiglie 6–9). La proiezione del corpo è quindi una **giunzione**: per ogni `family_id` in `repertoire[]`, si prendono solo gli `item_refs` con `item_verdict = validato` e si recupera il contenuto completo dai file a monte.

**Materiali micro-mediazioni (famiglie F3-SIT-1…5):**

| Campo sorgente | Resa pubblica | Note |
|---|---|---|
| `family_id` | Nome leggibile della famiglia (intestazione di gruppo) | Mappa da `f3-sit-famiglie.json` (es. "Casistiche situazionali", "Frasi per operatori") |
| `title` | Titolo del materiale | Si mostra |
| `context.setting`, `context.age_window` | Riga di contesto | Si mostrano |
| `context.situation` | Descrizione della situazione | Si rimuove il prefisso tecnico `case_type: …`; il resto si mostra |
| `context.actors` | — | Nascosto o reso implicito nel testo |
| `configurational_basis` (tutto) | — | **Nascosto**: `dominant_node`, `function`, `target_field`, `universal_device_type`, `source_device_id` sono metodo puro |
| `micro_mediation.adult_attitude` | "L'atteggiamento dell'adulto" | Si mostra in prosa |
| `micro_mediation.possible_phrase` / `alternative_phrase` | "Una formulazione possibile" | Si mostrano se non `null`; etichettate come *esempio*, mai come copione |
| `micro_mediation.gesture_or_timing` | "Il gesto, il tempo" | Si mostra |
| `micro_mediation.avoid` | "Cosa evitare" | Si mostra: è un campo anti-prescrittivo (§10) |
| `expected_field_effect` | "Cosa rende osservabile" | Si mostra |
| `non_prescriptive_note` | Riquadro evidenziato "Non è una ricetta" | **Sempre mostrato**: è il presidio anti-prescrittivo (§10) |
| `methodological_warnings` | — | **Nascosto di default**: spesso tecnico ("breaking point strutturale…"). Se editorialmente rilevante, va riformulato a mano |

**Materiali formati formativi e narrativi (famiglie F3-SIT-6…9):** vignette, storyboard, linee guida, prompt AI. Sono già in forma narrativa; si mostrano i campi di testo (titolo, scena/contrapposizione lettura ingenua–configurazionale, domande di discussione, corpo della linea guida) e si nasconde la struttura di tracciabilità. I prompt per AI generativa (F3-SIT-9), se presenti, **non** si mostrano al pubblico generale: sono materiale di produzione, non di fruizione (livello `riservato` o `abbonato`).

### 5.3 Campi sempre nascosti al pubblico

Mai esposti, su qualunque scheda: i Nodi Trasversali N1–N7; la Configurazione Evolutiva e le dimensioni S/R/D/T/A; la Tipologia Universale U1–U6; la checklist di coerenza C1–C8 e gli `item_checks`; `source_device_id` e la catena di tracciabilità; i `breaking point` e i `methodological_warnings` tecnici; `methodological_status`, `source_validations`, `item_verdict`, `critical_failures`; l'intero contenuto degli step intermedi F2/F3/F3-SIT. Questi campi restano visibili solo nell'area riservata.

### 5.4 Registro linguistico

La resa pubblica non usa il vocabolario del metodo. "Nodo dominante", "configurazione evolutiva", "dispositivo", "campo configurazionale" non compaiono. Si privilegiano i termini già presenti nei campi `linguistic_frame` e `narrative_synthesis`, che sono scritti in registro divulgativo dalla pipeline stessa. La scheda parla di *situazioni*, *atteggiamenti dell'adulto*, *cosa diventa osservabile*, *domande da tenere aperte* — non di grammatica del modello.

### 5.5 `content_snapshot`: proiezione congelata alla pubblicazione

La proiezione descritta in §5.1–5.4 è prodotta da una funzione server-side `buildPublicSchedaProjection(context_id)` che giunge output-tipo + repertorio + micro-mediazioni + formati e applica la mappa dei campi. Il risultato viene **congelato** in `published_tools.content_snapshot` al momento della pubblicazione (transizione a `pubblicato`, §7). Ragione: una ri-esecuzione della pipeline non deve cambiare silenziosamente una pagina già pubblica. Per aggiornare una scheda pubblicata si ri-esegue esplicitamente la pubblicazione, che rigenera lo snapshot e lo sottopone di nuovo a revisione editoriale. L'area pubblica serve sempre `content_snapshot`, mai i dati di pipeline live.

---

## 6. Organizzazione e navigazione

### 6.0 Collocazione nel progetto

L'area pubblica **non** è una sezione autonoma del sito: appartiene al progetto **"Sviluppo Bambino"**, sotto-sezione **"Produzioni"**. Questo deve essere evidente sia nelle URL sia nella navigazione. Le route e gli endpoint portano il prefisso di progetto `/sviluppo-bambino/strumenti` (la sotto-sezione `produzioni` non viene riportata nell'URL, per brevità). Nelle barre di navigazione la voce "Strumenti" va collocata **dentro il raggruppamento "Sviluppo Bambino"**, accanto a "Produzioni", non come voce di primo livello del sito. Il dettaglio di implementazione della collocazione dei pulsanti è in `D12`.

### 6.1 Assi di navigazione

Il pubblico non conosce la grammatica del metodo: l'organizzazione deve essere navigabile senza di essa. Due assi:

**Asse primario — ambito.** L'index pubblico è organizzato per ambito/dominio: `clinico`, `educativo`, `formazione`, `politiche` (i valori di `domain_selected`). Etichette divulgative ("Ambito clinico e pediatrico", "Ambito educativo", …). È l'asse con cui un visitatore arriva: cerca per il proprio campo, non per il nome di un fenomeno che non conosce.

**Filtro secondario — destinatario.** Dentro un ambito (o trasversalmente), un filtro per destinatario: genitori e caregiver, operatori, formatori. Si calcola dai `typical_target_user` delle famiglie F3-SIT presenti nella scheda (valori in `f3-sit-famiglie.json`: pediatra, educatore, insegnante, bibliotecario, genitore, caregiver, formatore), raggruppati in tre categorie pubbliche.

**Titolo della scheda — il fenomeno.** Ogni scheda è titolata dal fenomeno dello sviluppo (`theme_label`). Il fenomeno **non** è un asse di navigazione primario (il pubblico non lo cerca per nome) ma è ciò che identifica e intesta la scheda.

**La famiglia F3-SIT** (casistiche, frasi, vignette, …) **non** è un asse di navigazione: è un raggruppamento *interno* alla scheda, usato per dare struttura al corpo (§5.2).

### 6.2 Route

| Route | Pagina | Contenuto |
|---|---|---|
| `/sviluppo-bambino/strumenti` | `StrumentiIndexPage` | Index: schede pubblicate, raggruppate per ambito, con filtro destinatario |
| `/sviluppo-bambino/strumenti/:slug` | `SchedaStrumentoPage` | Una Scheda Strumento completa (cornice + corpo) |

Le route `/sviluppo-bambino/strumenti/...` sono pubbliche (nessun `useIsAdmin()`). Restano distinte dalle route `/laboratorio/...` (admin, `D5b`) e dalle route read-only di pipeline (che D11 riserva ad admin, §2.2).

### 6.3 Struttura delle pagine

`StrumentiIndexPage`: intestazione divulgativa dell'area; sezioni per ambito; dentro ogni ambito, le schede come card (titolo del fenomeno, contesto, destinatari, una riga dall'`orientative_direction`); filtro destinatario applicato lato client. Mostra solo `published_tools` con `publication.status = pubblicato` e `visibility` compatibile con il ruolo del visitatore.

`SchedaStrumentoPage`: in alto la **cornice** (§5.1) — titolo, introduzione, "a cosa serve", le 5 aree di lettura; sotto il **corpo** (§5.2) — i materiali per famiglia; in chiusura la **cornice di lettura non-prescrittiva** (§10). Nessun viewer JSON, nessun campo di metodo.

---

## 7. Workflow di approvazione editoriale

`publication_recommendation.public_site` prodotto da F3-SIT step 4 è una **raccomandazione dell'agente**, non una decisione di pubblicazione. La pubblicazione effettiva passa per un **doppio gate**.

### 7.1 Stati della pubblicazione

`published_tools.publication.status` attraversa:

```
[bozza] ──▶ [in_revisione] ──▶ [pubblicato] ──▶ [ritirato]
   ▲              │                  │              │
   └──────────────┴──────────────────┴──────────────┘
        (un admin può sempre riportare a uno stato precedente)
```

- **`bozza`** — esiste un record `published_tools` (creato automaticamente o da admin) ma non è in lavorazione editoriale.
- **`in_revisione`** — un admin ha preso in carico la scheda; sta rivedendo la proiezione leggibile e applicando la checklist non-prescrittiva (§10).
- **`pubblicato`** — la scheda è visibile nell'area pubblica, secondo la sua `visibility`. La transizione a `pubblicato` congela `content_snapshot` (§5.5).
- **`ritirato`** — scheda rimossa dalla vista pubblica (es. dopo una revisione metodologica della pipeline). Il record resta, per storico e ri-pubblicazione.

### 7.2 I due gate

**Gate 1 — gate-dati (automatico).** Calcola `data_gate.passes_data_gate`. È `true` quando, per il livello `pubblico`: il repertorio F3-SIT esiste con `methodological_status = validato`; `publication_recommendation.public_site = true`; `f3_coherence_status` ∈ {`valido`} (non `null`, non `fuori_modello`). Il gate-dati è **necessario ma non sufficiente**: una scheda che non lo supera non può essere pubblicata `pubblico`; una che lo supera è solo *candidabile*.

> Sul pilota `gioco-libero × clinico`: il repertorio ha `methodological_status = validato` e 21 item validati, ma `public_site = false`, `internal_only = true` e `f3_coherence_status = null` (manca `coerenza-v1.json`). Non supera il gate-dati per il livello `pubblico`. È coerente con la pendenza segnalata in `revisioni.md`: l'area pubblica **gestisce** il gating, non lo assume. Una scheda così resta `riservato` finché la verifica di coerenza F3 non è recuperata; le note del repertorio indicano che, recuperato `coerenza-v1.json` con stato `valido`, diventerebbe idonea a sito pubblico e formazione professionale.

**Gate 2 — gate editoriale (umano).** Un admin porta la scheda da `in_revisione` a `pubblicato`. È qui che si applica la checklist non-prescrittiva (§10) e si decide la `visibility`. Nessuna scheda diventa `pubblicato` senza questo passaggio: la raccomandazione dell'agente non pubblica nulla da sola.

### 7.3 Chi fa cosa

Per ora tutti gli atti editoriali sono compiuti dal ruolo `admin` (non esiste un ruolo "editore" distinto). Il modello dati (`published_by`, `last_editorial_review_at`) è predisposto per un eventuale ruolo editoriale separato in futuro, ma D11 non lo introduce.

---

## 8. Modello di accesso e ruoli

### 8.1 Stato attuale

L'autenticazione è gestita da Clerk (`D5` §1.2): `useIsAdmin()` legge `user.publicMetadata.role === 'admin'`. Oggi esistono di fatto due condizioni: `admin` e "tutti gli altri" (autenticati o no).

### 8.2 Modello a tre livelli, due attivi

Ogni scheda pubblicata porta `publication.visibility` con tre valori:

| `visibility` | Chi vede la scheda | Stato in D11 |
|---|---|---|
| `pubblico` | Chiunque, anche non autenticato | **Attivo** |
| `abbonato` | Utenti con ruolo `subscriber` + `admin` | **Previsto, non attivato** |
| `riservato` | Solo `admin` | **Attivo** |

Il livello `abbonato` è progettato fin d'ora — è un valore legittimo dello schema e un ruolo Clerk previsto (`role: 'subscriber'`) — ma l'implementazione iniziale espone solo `pubblico` e `riservato`. Una scheda marcata `abbonato` in questa fase si comporta come `riservato` (visibile solo agli admin) finché il livello non viene attivato. Questo permette di progettare la struttura senza implementare ora la logica di abbonamento.

### 8.3 Mappatura raccomandazione → visibilità

La `publication_recommendation` di F3-SIT orienta (non vincola) la `visibility` proposta in fase di revisione:

| `public_site` | `professional_training` | `internal_only` | `visibility` proposta |
|---|---|---|---|
| true | — | — | `pubblico` |
| false | true | — | `abbonato` (oggi: di fatto `riservato`) |
| false | false | true | `riservato` |

L'admin in gate 2 può confermare o modificare la proposta. La `visibility` finale è una decisione editoriale, non automatica.

### 8.4 Helper di ruolo

Coerente con `useIsAdmin()`, si prevede un `useUserTier()` che restituisce `'public' | 'subscriber' | 'admin'`. L'area pubblica filtra le schede per `visibility` compatibile con il tier. In questa fase `useUserTier()` restituisce solo `'public'` o `'admin'`.

---

## 9. API — endpoint pubblici

Nuovo namespace `/api/sviluppo-bambino/strumenti/*`, separato da `/api/pipeline/*`. Envelope e codici HTTP come `D4` §1.2–1.3.

### 9.1 Endpoint pubblici (lettura)

| Metodo | Path | Auth | Scopo |
|---|---|---|---|
| GET | `/api/sviluppo-bambino/strumenti` | public | Index delle schede pubblicate, filtrabile per `ambito` e `destinatario` (query string). Restituisce solo schede con `status = pubblicato` e `visibility` compatibile con il tier del richiedente. |
| GET | `/api/sviluppo-bambino/strumenti/:slug` | public | Una Scheda Strumento: serve `content_snapshot`. 404 se non esiste o non è pubblicata/visibile al tier. |

Questi endpoint **non** restituiscono mai output di pipeline grezzi né campi di metodo: servono solo la proiezione `content_snapshot` (§5.5).

### 9.2 Endpoint editoriali (admin)

| Metodo | Path | Auth | Scopo |
|---|---|---|---|
| GET | `/api/sviluppo-bambino/strumenti/admin/candidati` | admin | Elenco dei tema × dominio con un output finale (F3 step 5 e/o F3-SIT step 4), con l'esito del gate-dati calcolato. Materiale di lavoro della revisione editoriale. |
| POST | `/api/sviluppo-bambino/strumenti/:contextId/build` | admin | Crea o aggiorna il record `published_tools`, esegue `buildPublicSchedaProjection`, ricalcola `data_gate`. Non pubblica. |
| GET | `/api/sviluppo-bambino/strumenti/admin/:contextId` | admin | Record completo `published_tools` + anteprima della proiezione, per la revisione. |
| POST | `/api/sviluppo-bambino/strumenti/:contextId/transition` | admin | Cambia `publication.status` (`in_revisione`/`pubblicato`/`ritirato`) e/o `visibility`. La transizione a `pubblicato` congela `content_snapshot`. Rifiuta `pubblicato` con `visibility: pubblico` se il gate-dati non è superato. |
| PATCH | `/api/sviluppo-bambino/strumenti/:contextId/slug` | admin | Modifica lo slug pubblico. |

### 9.3 Modifica agli endpoint esistenti

Gli endpoint `GET /api/pipeline/*` di `D4` §2 passano da `public` ad `admin` (vedi §11). Il frontend read-only che li consuma viene di conseguenza riservato ad admin (§2.2).

---

## 10. Vincolo metodologico non-prescrittivo — requisiti verificabili

Gli strumenti HCAIRE **non sono protocolli né consigli prescrittivi**. `D9` insiste che F3-SIT non deve diventare "manualistica educativa" (cosa dire / cosa fare): ogni materiale è una *micro-mediazione*, non una ricetta. Nella resa pubblica questo è un **requisito di design verificabile**, non una linea guida generica.

### 10.1 Requisiti strutturali sulla resa

1. **I campi anti-prescrittivi sono sempre mostrati.** Per ogni materiale del corpo, `non_prescriptive_note` compare in un riquadro evidenziato e `avoid` ("Cosa evitare") è sempre reso. Non sono opzionali né comprimibili.
2. **Le formulazioni sono etichettate come esempi.** `possible_phrase` / `alternative_phrase` compaiono sotto un'etichetta esplicita ("Una formulazione possibile, non un copione"). Mai presentate come frasi da pronunciare.
3. **Gli snodi decisionali restano domande.** I `decisional_nodes` dell'output-tipo sono resi come domande aperte che l'adulto si pone, mai come passi da eseguire o checklist.
4. **La direzione orientativa è etichettata.** `orientative_direction` compare sotto "A cosa serve / orientamento", mai come obiettivo da raggiungere o risultato garantito.
5. **Cornice di lettura su ogni scheda.** Ogni Scheda Strumento porta, in apertura o chiusura, una nota di cornice che dichiara la natura non-prescrittiva del materiale: descrive configurazioni e atteggiamenti possibili, non istruzioni; non sostituisce il giudizio del professionista né la relazione con il bambino.
6. **Niente forma-protocollo.** La resa evita liste numerate di passi, "step 1/2/3", checklist operative. I materiali della famiglia "linee guida narrative" (F3-SIT-8) — che `revisioni.md` segnala lambire la forma-protocollo — vanno resi in prosa, non in struttura a punti operativi.

### 10.2 Checklist di verifica editoriale

Il gate editoriale (§7.2, gate 2) include una checklist che l'admin applica a ogni scheda prima di `pubblicato`. Riprende lo spirito della checklist C1–C8 di `D9`, applicata alla *resa* anziché all'item:

- [ ] Nessun campo di metodo è trapelato nella resa (§5.3).
- [ ] Ogni materiale mostra la sua nota non-prescrittiva e il "cosa evitare".
- [ ] Nessuna formulazione è presentata come copione; tutte sono etichettate come esempi.
- [ ] Gli snodi decisionali sono domande, non istruzioni.
- [ ] Nessuna lista di passi operativi; nessuna forma-checklist.
- [ ] La scheda non etichetta il bambino, non colpevolizza il genitore, non moralizza (C1–C3 di `D9` sulla resa complessiva).
- [ ] La cornice di lettura non-prescrittiva è presente e visibile.
- [ ] Il linguaggio è divulgativo: nessun termine del metodo non spiegato (§5.4).

Una scheda che non supera la checklist non passa a `pubblicato`.

---

## 11. Impatto su altri documenti

D11 è di progettazione; l'implementazione comporterà modifiche a:

| Documento / artefatto | Modifica |
|---|---|
| `D4` §1.1 | Gli endpoint `GET /api/pipeline/*` passano da `public` ad `admin`. Aggiungere il namespace `/api/sviluppo-bambino/strumenti/*` (§9). |
| `D5` §1.1 | Le pagine read-only della pipeline (`/produzioni`, `/sviluppo-bambino`) passano dietro `useIsAdmin()`. Aggiungere `useUserTier()` (§8.4). |
| `D5b` | Nessuna modifica sostanziale: il Laboratorio resta l'area riservata. Eventuale nota di rinvio a D11 per l'area pubblica. |
| MongoDB | Nuova collezione `published_tools` (§4.1) con i suoi indici. Nessuna modifica alle collezioni di pipeline. |
| Ruoli Clerk | Previsto (non attivato) il ruolo `subscriber` (§8.2). |
| Routing webapp | Nuove route `/sviluppo-bambino/strumenti` e `/sviluppo-bambino/strumenti/:slug` (§6.2). |

Nessuna modifica alla pipeline F2/F3/F3-SIT, ai suoi schemi, agli step o ai loro output: l'area pubblica è puramente a valle e additiva.

---

## 12. Fuori scope e pendenze

**Fuori scope di D11:** l'implementazione (backend, frontend, componenti React); il design grafico dell'area pubblica; l'attivazione del livello `abbonato` e la logica di abbonamento/pagamento; un ruolo editoriale distinto da `admin`; la gestione dell'Archivio Temi (`D5b` §1.4) e dell'area riservata, già coperti altrove.

**Pendenze da risolvere prima o durante l'implementazione:**

1. **`coerenza-v1.json` mancante nel pilota.** Il gate-dati richiede `f3_coherence_status` valorizzato. È una pendenza della pipeline F3 (segnalata in `D10` §9 domanda 5 e in `revisioni.md`), non di D11, ma blocca la pubblicabilità pubblica di qualsiasi scheda finché non è risolta.
2. **Schede a sola cornice.** Finché il livello `abbonato`/professionale non è attivo, i tema × dominio con solo output-tipo e senza F3-SIT non hanno una collocazione pubblica: restano `riservato`. Da valutare se anticipare l'attivazione del livello professionale.
3. **Famiglia F3-SIT-9 (prompt AI).** Esclusa dalla resa pubblica generale (§5.2); va deciso se mostrarla al livello `abbonato` o tenerla sempre `riservato`.
4. **Slug e identità pubblica.** La derivazione automatica dello `slug` da `theme_id` + `ambito_id` va definita (collisioni, leggibilità, stabilità nel tempo).

## 13. Appendici

### 13.1 Le sette decisioni di progetto

Sintesi delle decisioni prese (§4 del documento di ripartenza), tutte risolte con il ricercatore il 2026-05-24:

1. **Cosa è lo strumento finale** → Scheda composita tema × dominio: corpo = repertorio F3-SIT, cornice = output-tipo F3 (§3).
2. **Organizzazione** → Asse primario ambito, filtro destinatario; titolo per fenomeno (§6.1).
3. **Forma di presentazione** → Resa narrativa selettiva, con mappa campo-per-campo (§5).
4. **Criterio di pubblicabilità** → Doppio gate: gate-dati automatico + gate editoriale umano; stato di pubblicazione persistente (§7).
5. **Rapporto con l'area riservata** → Route e componenti separati (`/sviluppo-bambino/strumenti` vs `/laboratorio`); pagine read-only attuali riservate ad admin; stessa sorgente dati, endpoint pubblici filtrati (§2, §9).
6. **Modello di accesso** → Tre livelli (`pubblico`/`abbonato`/`riservato`) nello schema, due attivi; livello abbonato previsto, non implementato (§8).
7. **Vincolo non-prescrittivo** → Requisito di design verificabile: campi anti-prescrittivi sempre mostrati, cornice di lettura, checklist editoriale (§10).

### 13.2 Riferimenti

- `Ripartenza — area pubblica strumenti finali.md` — documento di ripartenza della sessione.
- `D4-api-spec-express.md` — API e modello di autenticazione (modificato da D11, §11).
- `D5-frontend-spec-orchestrazione.md` — frontend, `useIsAdmin`.
- `D5b-laboratorio-workbench.md` — area riservata (Laboratorio).
- `D8-f3-step-5-output-tipo-contestualizzato.md` + `f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json` — la cornice.
- `D9-pipeline-f3-sit.md` + `D10-f3-sit-integrazione-webapp.md` — il modulo F3-SIT (il corpo).
- `f3-sit-step-4-repertorio/sit-repertorio-schema.json`, `f3-sit-famiglie.json` — struttura del repertorio e tassonomia.
- `Storage dati e schemi pipeline.md` — persistenza e sorgente dati.
- Pilota: `output/produzioni/temi/gioco-libero-…--clinico-pediatrico/` (`output-tipo-clinico-v2.json`, `sit/sit-repertorio-v1.json`, `revisioni.md`).

---

*Fine documento — D11, area pubblica di visualizzazione degli strumenti finali, 2026-05-24.*
