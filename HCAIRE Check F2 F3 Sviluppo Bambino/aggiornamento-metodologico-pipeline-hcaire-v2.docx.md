**HCAIRE — Aggiornamento Metodologico Pipeline**

Guida Tecnica per Claude Code

*Data: 2026-05-04  |  Versione pipeline: 2.0*

**Destinatario:** Claude Code (implementazione webapp HCAIRE)

**Scopo:** Documentare le modifiche apportate alla pipeline F2 per allinearla alla metodologia HCAIRE. Descrivere esattamente cosa cambia negli schemi JSON, nel grafo di dipendenze, nella webapp e nel motore di esecuzione.

# **1\. Riepilogo delle modifiche**

Sono stati introdotti tre nuovi step nella Fase F2 della pipeline. Queste modifiche correggono il principale scostamento metodologico: il salto strutturale tra F2 e F3 senza mediazione esplicita attraverso il linguaggio formale del modello HCAIRE.

## **1.1 Tre nuovi step F2**

| Step ID | Label | Posizione | Funzione |
| :---- | :---- | :---- | :---- |
| f2\_step\_2a | Verifica Nodi Trasversali | Dopo f2\_step\_2 | Mappa nodi candidati sui 7 Nodi Trasversali canonici N1–N7 |
| f2\_step\_4b | CE Prototipica | Dopo f2\_step\_4 | Traduce micro-matrice in Grammatica CE (S, R, D, T, A) |
| f2\_step\_6 | Output-Tipo Vuoto | Dopo f2\_step\_5✓ | Produce il passaporto del tema — input primario di f3\_step\_1 |

## **1.2 Modifiche ai file esistenti**

* f2\_step\_2/CLAUDE.md — aggiunta sezione «Step successivo obbligatorio: STEP 2a»

* f2\_step\_4/CLAUDE.md — aggiunta sezione «Step successivo obbligatorio: STEP 4b»

* f2\_step\_5/CLAUDE.md — aggiunta sezione «Step successivo obbligatorio: STEP 6»

* f3\_step\_1/CLAUDE.md — input primario aggiornato: output-tipo-vuoto-v1.json (passaporto del tema)

* CLAUDE.md root pipeline — architettura F2 aggiornata con i tre nuovi step

* Pipeline-inputs.md — riepilogo operativo aggiornato

* **webapp-hcaire/pipeline-step-config.json — CREATO ex novo (v2.0):** 

  * contiene tutti gli step (esistenti \+ 3 nuovi) con dipendenze aggiornate

## **1.3 Cosa NON cambia**

* Grafo F3 (f3\_step\_1 → f3\_step\_10): invariato

* Schemi JSON degli step F3 esistenti: invariati

* MongoDB collections: nessuna migrazione schema necessaria

* Protocollo Redis (D3): invariato

* API Express (D4): nessun nuovo endpoint — i nuovi step usano POST .../steps/:stepId/run

# **2\. Nuovi file della pipeline**

## **2.1  f2-step-2a — Verifica Nodi Trasversali canonici**

**CLAUDE.md:** input/produzioni/f2-step-2a-verifica-nodi-trasversali/CLAUDE.md

**Schema JSON:** input/produzioni/f2-step-2a-verifica-nodi-trasversali/node-verification-schema.json

**Output path:** ricerche/{ricerca\_id}/node-verification-v{N}.json

**Output root:** { "step": "f2\_step\_2a", "results": \[ ThemeNodeVerification \] }

| Campo | Tipo | Descrizione |
| :---- | :---- | :---- |
| theme\_id | string | Identificatore del tema (stesso di STEP 2\) |
| node\_mappings\[\] | array | Ogni nodo candidato mappato su canonici N1-N7 |
| → node\_id | string | ID del nodo candidato da STEP 2 |
| → canonical\_mapping.canonical\_node\_id | string | null | N1…N7 oppure null |
| → canonical\_mapping.type | string | null | "identico" | "istanza" | "parziale" |
| activated\_canonical\_nodes\[\] | array | N1-N7 coperti con coverage\_type: 'piena'|'parziale' |
| absent\_canonical\_nodes\[\] | array | N1-N7 non attivati con structural\_reason |
| pure\_derived\_nodes\[\] | array | Nodi candidati senza mapping canonico (null) |
| canonical\_configuration\_assessment | object | Plausibility \+ missing\_relations\_notes \+ coverage\_adequacy |

## **2.2  f2-step-4b — CE Prototipica (Grammatica delle Configurazioni)**

**CLAUDE.md:** input/produzioni/f2-step-4b-ce-prototipica/CLAUDE.md

**Schema JSON:** input/produzioni/f2-step-4b-ce-prototipica/ce-prototipica-schema.json

**Output path:** ricerche/{ricerca\_id}/ce-prototipica-v{N}.json

**Output root:** { "step": "f2\_step\_4b", "results": \[ ThemeCEPrototica \] }

| Campo / Dimensione CE | Tipo | Valori ammessi |
| :---- | :---- | :---- |
| theme\_id | string | Identificatore del tema |
| ce\_prototipica.S\[\] | array\<NodeState\> | node\_id: N1-N7; state: ↑ \~ ↓ \! ? |
| ce\_prototipica.R\[\] | array\<NodeRelation\> | relation\_type: CPL | VIN | MED | CMP |
| ce\_prototipica.D | string | ↗ | → | ↘ |
| ce\_prototipica.T | string | T1 | T2 | T3 |
| ce\_prototipica.A | string | A+ | A± | A- |
| ce\_notation | string | Notazione formale CE \= S: … R: … D: … T: … A: … |
| ce\_natural\_language | string | Descrizione non tecnica (2-4 frasi) |
| ce\_variants\[\] | array (2-3) | variant\_name, modified\_dimension, modification\_description, structural\_description |
| derivation\_notes | string | Come i valori derivano dalla micro-matrice di STEP 4 |

## **2.3  f2-step-6 — Output-Tipo Vuoto (Passaporto del tema)**

**CLAUDE.md:** input/produzioni/f2-step-6-output-tipo-vuoto/CLAUDE.md

**Schema JSON:** input/produzioni/f2-step-6-output-tipo-vuoto/output-tipo-vuoto-schema.json

**Output path:** ricerche/{ricerca\_id}/output-tipo-vuoto-v{N}.json

**Output root:** { "step": "f2\_step\_6", "results": \[ OutputTipoVuoto \] }

**⚠ NOTA:** *Questo file è l'input primario di f3\_step\_1. Il Blocco 1 del prompt composito (D3 §12.2) per f3\_step\_1 deve includere output-tipo-vuoto (role: 'output-tipo-vuoto') come primo file.*

| Campo (sezione) | Tipo | Valori ammessi / Struttura |
| :---- | :---- | :---- |
| theme\_id | string | Identificatore del tema |
| structural\_reference.confirmed\_nodes\[\] | array\<string\> | node\_id confermati da STEP 3 |
| structural\_reference.canonical\_nodes\_active\[\] | array\<string\> | N1…N7 attivati nel tema |
| structural\_reference.ce\_reference | string | Notazione CE da STEP 4b |
| campo\_condiviso.forma\_prevalente | string | "condiviso" | "parallelo" | "frammentato" |
| campo\_condiviso.elementi\_sostenenti\[\] | array\<string\> | Componenti strutturali che sostengono il campo |
| campo\_condiviso.segnali\_accesso\[\] | array\<string\> (2-3) | Segnali osservabili elementari |
| posizione\_soggettiva.modalita\_prototipica | string | "emergenza\_di\_posizione" | "reattività" | "evitamento" | "oscillazione" |
| posizione\_soggettiva.funzione\_adulto | string | Sostiene / sostituisce / interrompe la posizione |
| posizione\_soggettiva.forme\_degradate\[\] | array\<string\> (2-4) | Configurazioni assenti/distorte/oscillanti |
| rapporto\_con\_limite.presenza | string | "sì" | "no" | "condizionalmente" |
| rapporto\_con\_limite.reazione\_strutturale | string | "A+" | "A±" | "A-" |
| configurazione\_complessiva | string | Frase sintetica (max 3 frasi) — Sez. D |
| ipotesi\_sostegno\[\].direzione | string | "campo\_condiviso" | "posizione\_soggettiva" | "limite\_nominabile" |
| ipotesi\_sostegno\[\].nodo\_principale | string | N1…N7 |
| tipologia\_universale\[\].id | string | "U1" | "U2" | "U3" | "U4" | "U5" | "U6" |

# **3\. Aggiornamenti richiesti alla webapp**

## **3.1  pipeline-step-config.json — Versione 2.0**

**File prodotto:** input/produzioni/webapp-hcaire/pipeline-step-config.json

**Destinazione webapp:** client/public/pipeline/pipeline-step-config.json

oppure

**Destinazione alternativa:** server/src/config/pipeline-step-config.json

**⚠ NOTA:** *Questo file SOSTITUISCE la versione precedente. Contiene tutti gli step esistenti \+ i 3 nuovi. Claude Code deve copiarlo nella webapp e aggiornare il servizio che lo legge (stepConfigService).*

Aggiunte al grafo di dipendenze (adjacency list F2 aggiornata):

| Step nuovo | Dipende da (required) | Dipende da (facoltativo) | Blocca |
| :---- | :---- | :---- | :---- |
| f2\_step\_2a | f2\_step\_2 | — | f2\_step\_3, f2\_step\_4b |
| f2\_step\_4b | f2\_step\_4 | f2\_step\_2a | f2\_step\_5, f2\_step\_6 |
| f2\_step\_6 | f2\_step\_5✓, f2\_step\_4, f2\_step\_3 | f2\_step\_4b | \[human\_decision\] → f3\_step\_1 |

## **3.2  pipeline\_contexts — step\_states**

La collection MongoDB pipeline\_contexts usa step\_states come Record\<string, StepState\>. Per i contesti di tipo ricerca, aggiungere i tre nuovi step\_id con stato iniziale non\_avviato.

| step\_id nuovo | Stato iniziale | context\_type |
| :---- | :---- | :---- |
| f2\_step\_2a | non\_avviato | ricerca |
| f2\_step\_4b | non\_avviato | ricerca |
| f2\_step\_6 | non\_avviato | ricerca |

**⚠ NOTA:** *Non è necessaria una migrazione schema MongoDB: step\_states è un Record dinamico. I nuovi step\_id appariranno naturalmente nei nuovi contesti creati dopo l'aggiornamento.*

Migration script facoltativo (per contesti ricerca già esistenti):

db.pipeline\_contexts.updateMany(

  { context\_type: 'ricerca', 'step\_states.f2\_step\_2a': { $exists: false } },

  { $set: {

      'step\_states.f2\_step\_2a': { status: 'non\_avviato', last\_execution\_id: null },

      'step\_states.f2\_step\_4b': { status: 'non\_avviato', last\_execution\_id: null },

      'step\_states.f2\_step\_6': { status: 'non\_avviato', last\_execution\_id: null }

  }}

)

## **3.3  f3\_step\_1 — Input primario aggiornato**

|  | Versione 1.x | Versione 2.0 |
| :---- | :---- | :---- |
| Input primario | output-family-v{N}.json (da f2\_step\_5) | output-tipo-vuoto-v{N}.json (da f2\_step\_6) |
| Input secondario | — | output-family-v{N}.json (per dominio selezionato) |
| Cartella sorgente | ricerche/{ricerca\_id}/ | ricerche/{ricerca\_id}/ (entrambi) |

Modifiche al backend (pipelineService.ts):

1. resolveInputFiles() per f3\_step\_1 deve risolvere output-tipo-vuoto-v{N}.json dalla cartella della ricerca associata al tema.

2. Il Blocco 1 del prompt composito (D3 §12.2) per f3\_step\_1 deve includere: output-tipo-vuoto (role: 'output-tipo-vuoto') come primo file, poi output-family (role: 'output-family').

3. La dipendenza di f3\_step\_1 include ora f2\_step\_6 come prerequisito (oltre a f2\_step\_5). Entrambi devono essere in stato completato/verificato.

## **3.4  Verifica e stato dei nuovi step**

| Step | verifica | can\_skip | Stato dopo completamento |
| :---- | :---- | :---- | :---- |
| f2\_step\_2a | false | false | completato → abilita f2\_step\_3 e f2\_step\_4b |
| f2\_step\_4b | false | false | completato → abilita f2\_step\_5 e f2\_step\_6 |
| f2\_step\_6 | false | false | completato → \[human\_decision\] → f3\_step\_1 |

# **4\. Server locale Cowork — Blocco 1 dei prompt compositi**

Non sono necessarie modifiche al protocollo Redis né al loop BRPOP. Le uniche modifiche riguardano la costruzione del Blocco 1 (D3 §12.2) per i nuovi step.

## **4.1  Blocco 1 per i tre nuovi step**

| Step | Input files da includere nel Blocco 1 |
| :---- | :---- |
| f2\_step\_2a | theme-relevance-v{N}.json  (role: 'theme-relevance') |
| f2\_step\_4b | theme-matrix-v{N}.json (role: 'theme-matrix')  \+  node-verification-v{N}.json se disponibile (role: 'node-verification') |
| f2\_step\_6 | output-family-v{N}.json (role: 'output-family')  \+  ce-prototipica-v{N}.json se disponibile (role: 'ce-prototipica')  \+  theme-matrix-v{N}.json  \+  theme-verification-v{N}.json |

## **4.2  Blocco 1 per f3\_step\_1 (aggiornato)**

| Role | File | Note |
| :---- | :---- | :---- |
| output-tipo-vuoto | ricerche/{ricerca\_id}/output-tipo-vuoto-v{N}.json | INPUT PRIMARIO — sempre required |
| output-family | ricerche/{ricerca\_id}/output-family-v{N}.json | Required — per il dominio selezionato |

**⚠ NOTA:** *Il path di output-tipo-vuoto è in ricerche/, non in temi/. Il backend deve risolvere il ricerca\_id associato al tema per costruire il path corretto.*

# **5\. Checklist di implementazione**

| \# | Attività | File | Priorità |
| :---- | :---- | :---- | :---- |
| 1 | Copiare pipeline-step-config.json v2.0 nella webapp | client/public/pipeline/ o server/src/config/ | ALTA |
| 2 | Aggiornare stepConfigService per leggere i 3 nuovi step\_id | server/src/services/stepConfigService.ts | ALTA |
| 3 | Aggiornare evaluateStepEnablement per f2\_step\_2a, f2\_step\_4b, f2\_step\_6 | server/src/services/pipelineService.ts | ALTA |
| 4 | Aggiornare resolveInputFiles per f3\_step\_1 (aggiungere output-tipo-vuoto) | server/src/services/pipelineService.ts | ALTA |
| 5 | Aggiornare createPipelineContext per includere 3 nuovi step\_id in step\_states | server/src/controllers/pipelineController.ts | ALTA |
| 6 | Migration script MongoDB per contesti ricerca esistenti (facoltativo) | MongoDB Atlas | MEDIA |
| 7 | Aggiornare DeviceLineage per mostrare i 3 nuovi step nel grafo F2 | client/src/components/DeviceLineage.tsx | MEDIA |
| 8 | Aggiornare pipeline overview per F2 (3 nuovi step) | client/src/pages/PipelinePage.tsx | MEDIA |

## **5.1  Verifica di correttezza post-implementazione**

* Creare un nuovo contesto ricerca: verificare step\_states con f2\_step\_2a, f2\_step\_4b, f2\_step\_6 in non\_avviato

* Eseguire f2\_step\_2 e verificare che f2\_step\_2a sia abilitato dopo il completamento

* Eseguire f2\_step\_4 e verificare che f2\_step\_4b sia abilitato dopo il completamento

* Eseguire f2\_step\_5 (verificato) e verificare che SOLO f2\_step\_6 sia abilitato — non f3\_step\_1 direttamente

* Eseguire f2\_step\_6 e verificare che output-tipo-vuoto-v1.json venga prodotto in ricerche/{ricerca\_id}/

* Eseguire f3\_step\_1 e verificare che il Blocco 1 del prompt includa output-tipo-vuoto e output-family

# **6\. Appendice — Grafo F2 aggiornato**

Grafo di dipendenze F2 completo (versione 2.0):

f2\_step\_1  →  f2\_step\_2, f2\_step\_3, f2\_step\_4, f2\_step\_5

f2\_step\_2\* →  f2\_step\_2a, f2\_step\_3           (\* dopo verifica)

f2\_step\_2a →  f2\_step\_3 (facoltativo), f2\_step\_4b

f2\_step\_3  →  f2\_step\_4, f2\_step\_5

f2\_step\_4  →  f2\_step\_4b, f2\_step\_5

f2\_step\_4b →  f2\_step\_5 (facoltativo), f2\_step\_6

f2\_step\_5\* →  f2\_step\_6                       (\* dopo verifica)

f2\_step\_6  →  \[human\_decision\] → f3\_step\_1

**⚠ NOTA:** *f2\_step\_2a e f2\_step\_4b sono 'facoltative' per f2\_step\_3 e f2\_step\_5 (nel senso che non bloccano le dipendenze di step successivi), ma obbligatorie per f2\_step\_6. Di fatto la catena è sequenziale nella direzione principale.*

*— Fine documento — Pipeline HCAIRE v2.0*

File sorgente: input/produzioni/webapp-hcaire/pipeline-step-config.json