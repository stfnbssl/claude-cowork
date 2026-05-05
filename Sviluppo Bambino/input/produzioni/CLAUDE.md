# Pipeline di produzione — laboratorio HCAIRE

Questo documento descrive la pipeline completa per la costruzione di dispositivi configurazionali a partire dalla ricerca tematica. È il punto di ingresso operativo per eseguire la pipeline in una sessione di lavoro.

---

## Architettura generale

La pipeline è articolata in due fasi:

**F2 — Ricerca e modellizzazione tematica**
Produce un array di temi strutturalmente fondati, ciascuno con una configurazione di assi, nodi, concetti-ponte, tensioni e famiglie di output.
Input: fonti esterne + JSON degli assi strutturali.
Output: array di temi in `output/produzioni/ricerche/[nome-ricerca]/`.
Ogni run di F2 prende il nome assegnato in f2-step-1 e diventa una cartella autonoma in `ricerche/`.

**F3 — Costruzione del dispositivo configurazionale**
A partire da un singolo tema (o da un tema dell'array F2), costruisce e valida un dispositivo di lettura configurazionale operativamente utilizzabile.
Input: un tema + dispositivo sorgente validato.
Output: tutti i file F3 del tema in `output/produzioni/temi/[nome-tema]/`.
Ogni tema ha la propria cartella che contiene tutti gli step F3 più il file `revisioni.md` con la storia delle decisioni episodiche.

**Connessione tra le fasi**: F2 produce l'array tematico più l'output-tipo vuoto del tema scelto ("passaporto del tema"); F3 prende un tema per volta. Il passaggio da array a tema singolo è una decisione umana (quale tema portare in F3 e con quale priorità). Il passaporto del tema (`output-tipo-vuoto-v1.json`) è l'input primario di F3 STEP 1.

---

## Punti di input esterno

La pipeline è progettata con pochi punti di ingresso esterni — il resto è trasformazione strutturale che deve emergere dai dati, non essere guidata. Intervenire fuori dai punti indicati rischia di rompere la generatività del metodo.

### Input obbligatori

| Step | Input richiesto | Cosa definisce |
|---|---|---|
| **f2-step-2** | Scelta del tema (atto / fenomeno) | L'oggetto ontologico della pipeline |
| **f3-step-7** | Scelta del contesto / ambito | Il vincolo di realtà del dispositivo |
| **f3-step-10** | Costruzione dei casi di stress test | La qualità e profondità del test finale |

### Input facoltativi

| Step | Input possibile | Quando usarlo |
|---|---|---|
| **f3-step-6** | Livello di severità del test di non-reversibilità | Se si vuole un test forte vs. test di plausibilità |
| **f3-step-8** | Livello di specificità del dispositivo finale | Raramente — meglio non intervenire |

**Principio**: più l'input è precoce e preciso (f2-step-2), più la generatività della pipeline è alta. Fornire tema sbagliato o contesto ambiguo produce dispositivi strutturalmente fragili anche con esecuzione perfetta degli step.

---

## Esecuzione della pipeline

Ogni step è definito da un file `CLAUDE.md` nella cartella dello step. Per eseguire uno step:

1. Verificare se lo step richiede un input esterno (vedi tabella sopra) e prepararlo.
2. Leggere il `CLAUDE.md` dello step (contiene ruolo, input, vincoli, istruzioni, schema output).
3. Eseguire lo step secondo le istruzioni.
4. Se nella cartella è presente un `verifica.md`, applicarlo **prima di procedere allo step successivo**.
5. Alcuni step hanno varianti (es. `CLAUDE-B.md`): leggerle nell'ordine indicato.

**La pipeline è semi-automatica.** I passaggi di verifica richiedono valutazione umana: il verifica non approva automaticamente — produce una diagnosi che orienta la decisione di procedere, correggere o ripetere.

---

## F2 — Step per step

Tutti gli step F2 possono lavorare su un singolo tema o sull'intero array prodotto dallo step precedente. Lo schema di output prevede sempre un wrapper `{ "step": "f2_step_N", "results": [ ... ] }` che supporta entrambe le modalità.

### f2-step-1 — Ricerca temi
**Cartella**: `f2-step-1-ricerca-temi/`
**Funzione**: ricerca e formulazione di temi candidati strutturalmente significativi.
**Input**: fonti esterne (web) + JSON assi strutturali.
**Output**: `output/produzioni/temi/theme-discovery-vN.json`
**Verifica**: non presente — la selezione dei temi è validata dal ricercatore.
**Note metodologiche**: `f2-step-1-ricerca-temi/METODOLOGIA-TEMI.md`

### f2-step-2 — Rilevanza strutturale
**Cartella**: `f2-step-2-rilevanza-strutturale/`
**Funzione**: prima mappa esplorativa di assi, nodi e concetti-ponte per ciascun tema.
**Input**: `theme-discovery-vN.json` + JSON assi strutturali.
**Output**: `output/produzioni/ricerche/[nome-ricerca]/theme-relevance-vN.json`
**Verifica**: `verifica.md` presente — applica prima di procedere a f2-step-3.
**→ Dopo**: eseguire **f2-step-2a** per mappare i nodi candidati sui Nodi Trasversali canonici N1–N7.

### f2-step-2a — Verifica Nodi Trasversali *(nuovo)*
**Cartella**: `f2-step-2a-verifica-nodi-trasversali/`
**Funzione**: verifica e mappatura dei nodi candidati di STEP 2 sui Nodi Trasversali canonici N1–N7 del modello HCAIRE.
**Input**: `theme-relevance-vN.json`
**Output**: `output/produzioni/ricerche/[nome-ricerca]/node-verification-v1.json`
**Verifica**: non presente (output usato da STEP 3 per validazione dei nodi).
**Schema**: `f2-step-2a-verifica-nodi-trasversali/node-verification-schema.json`

### f2-step-3 — Verifica strutturale
**Cartella**: `f2-step-3-verifica-strutturale/`
**Funzione**: riduzione e selezione della configurazione strutturale (da ipotesi a vincolo).
**Input**: `theme-discovery-vN.json` + `theme-relevance-vN.json` + JSON assi strutturali.
**Output**: `output/produzioni/temi/theme-verification-vN.json`
**Verifica**: non presente — la verifica è incorporata nello step stesso.

### f2-step-4 — Micro-matrice
**Cartella**: `f2-step-4-micro-matrice/`
**Funzione**: articolazione della configurazione strutturale in micro-matrice interrogabile (assi, tensioni, domande strutturali).
**Input**: `theme-discovery-vN.json` + `theme-verification-vN.json` + JSON assi strutturali.
**Output**: `output/produzioni/ricerche/[nome-ricerca]/theme-matrix-vN.json`
**Verifica**: non presente.
**→ Dopo**: eseguire **f2-step-4b** per produrre la Configurazione Evolutiva Prototipica (CE Prototipica) nella Grammatica delle Configurazioni.

### f2-step-4b — CE Prototipica *(nuovo)*
**Cartella**: `f2-step-4b-ce-prototipica/`
**Funzione**: traduzione della micro-matrice nella Grammatica delle Configurazioni (CE Prototipica con dimensioni S, R, D, T, A). Produce la "firma strutturale" del tema nel linguaggio formale del modello.
**Input**: `theme-matrix-vN.json` + `node-verification-v1.json` (se disponibile)
**Output**: `output/produzioni/ricerche/[nome-ricerca]/ce-prototipica-v1.json`
**Verifica**: non presente.
**Schema**: `f2-step-4b-ce-prototipica/ce-prototipica-schema.json`

### f2-step-5 — Famiglia di output
**Cartella**: `f2-step-5-output-family/`
**Funzione**: identificazione delle possibilità strutturate di uso del modello per dominio.
**Input**: `theme-discovery-vN.json` + `theme-verification-vN.json` + `theme-matrix-vN.json` + JSON assi strutturali.
**Output**: `output/produzioni/ricerche/[nome-ricerca]/output-family-vN.json`
**Verifica**: `verifica.md` presente — applica prima di passare a F3.

### f2-step-6 — Output-Tipo Vuoto (Passaporto del tema) *(nuovo)*
**Cartella**: `f2-step-6-output-tipo-vuoto/`
**Funzione**: produzione dell'output-tipo vuoto — struttura compilabile che formalizza il passaggio dall'Operatore Triadico di Lettura (F2) allo strumento contestualizzato (F3). Questo file è il "passaporto del tema" e diventa l'input primario di F3 STEP 1.
**Input**: `output-family-vN.json` (approvato) + `ce-prototipica-v1.json` + `theme-matrix-vN.json` + `theme-verification-vN.json`
**Output**: `output/produzioni/ricerche/[nome-ricerca]/output-tipo-vuoto-v1.json`
**Verifica**: non presente — validato implicitamente dalla coerenza con F2 già approvato.
**Schema**: `f2-step-6-output-tipo-vuoto/output-tipo-vuoto-schema.json`

---

## F3 — Step per step

F3 lavora su **un tema per volta**. Ogni step produce un file JSON dedicato al tema in lavorazione. Il dispositivo sorgente di riferimento per F3 è il dispositivo del pointing validato (nei file di output/produzioni/temi/).

### f3-step-1 — Dispositivo di lettura
**Cartella**: `f3-step-1-dispositivo-lettura/`
**Funzione**: costruzione del dispositivo di lettura configurazionale per il tema nel dominio selezionato.
**Input primario**: `output-tipo-vuoto-v1.json` (passaporto del tema, da f2-step-6) — è la struttura triadica che orienta la costruzione del dispositivo.
**Input secondario**: `output-family-vN.json` (per il dominio selezionato) + schema del dispositivo.
**Output**: `output/produzioni/temi/[nome-tema]/lettura-configurazionale-{domain}-vN.json`
**Verifica**: `verifica.md` presente.
**Schema**: `f3-step-1-dispositivo-lettura/reading-device-schema.json`

### f3-step-2 — Stress test
**Cartella**: `f3-step-2-stress-test/`
**Funzione**: test di tenuta del dispositivo su casi critici (configurazioni assenti, parziali, ambigue).
**Input**: dispositivo f3-step-1.
**Output**: `output/produzioni/temi/[tema]-stress-test-vN.json`
**Verifica**: non presente.
**Schema**: `f3-step-2-stress-test/stress-test-schema.json`

### f3-step-3 — Correzione strutturale
**Cartella**: `f3-step-3-correzione-strutturale/`
**Funzione**: correzione del dispositivo sulla base delle fratture emerse nello stress test.
**Input**: dispositivo f3-step-1 + risultati f3-step-2.
**Output**: `output/produzioni/temi/[tema]-correzione-strutturale-vN.json`
**Verifica**: non presente.
**Schema**: `f3-step-3-correzione-strutturale/structural-correction-schema.json`

### f3-step-4 — Test di indistinguibilità
**Cartella**: `f3-step-4-indistinguibilità/`
**Funzione**: costruzione di coppie di casi quasi indistinguibili per verificare la tenuta del proxy.
**Input**: dispositivo corretto f3-step-3.
**Output**: `output/produzioni/temi/[tema]-indistinguibilità-vN.json`
**Verifica**: `verifica.md` presente.
**Schema**: `f3-step-4-indistinguibilità/indistinguibility-test-schema.json`

### f3-step-5 — Audit
**Cartella**: `f3-step-5-audit/`
**Funzione**: audit epistemico completo del dispositivo (inferenze, circolarità, normatività).
**Input**: dispositivo corretto f3-step-3 + risultati f3-step-4.
**Output**: `output/produzioni/temi/[tema]-audit-vN.json`
**Verifica**: `verifica.md` presente.
**Schema**: `f3-step-5-audit/audit-schema.json`

### f3-step-6 — Stabilizzazione proxy
**Cartella**: `f3-step-6-stabilizzazione-proxy/`
**Funzione**: stabilizzazione del proxy (sostituzione di proxy fragili con proxy strutturalmente non reversibili).
**Variante**: `CLAUDE-B.md` — forma operativa completa del proxy (condizioni di applicabilità, regole di non classificabilità). Eseguire dopo CLAUDE.md, prima della verifica.
**Input**: dispositivo corretto f3-step-3 + risultati f3-step-4 e f3-step-5.
**Output**: `output/produzioni/temi/[tema]-stabilizzazione-proxy-vN.json` (step 6) + `[tema]-stabilizzazione-proxy-vNb.json` (step 6-B)
**Verifica**: `verifica.md` presente — applica dopo aver completato sia 6 che 6-B.
**Nota**: dopo la verifica può essere necessario un 6-C (integrazione del proxy stabilizzato nel dispositivo corretto).

### f3-step-7 — Trasferibilità del dispositivo
**Cartella**: `f3-step-7-trasferibilità-dispositivo/`
**Funzione**: valutazione della trasferibilità del dispositivo validato a un nuovo tema.
**Input**: dispositivo validato (con proxy stabilizzato) + tema target.
**Output**: `output/produzioni/temi/[tema]-trasferibilità-vN.json`
**Verifica**: non presente — il verdetto di trasferibilità orienta la decisione di procedere a f3-step-8.

### f3-step-8 — Adattamento strutturale
**Cartella**: `f3-step-8-adattamento-strutturale/`
**Funzione**: costruzione dei quattro blocchi strutturali del nuovo dispositivo (corporeità, bridge, proxy, requisiti di osservabilità).
**Input**: dispositivo sorgente + risultati f3-step-7 + micro-casi del nuovo tema.
**Output**: `output/produzioni/temi/[tema]-adattamento-strutturale-vN.json`
**Verifica**: `verifica.md` presente — il proxy v1 può essere rifiutato e richiedere una versione v2.

### f3-step-9 — Dispositivo completo
**Cartella**: `f3-step-9-dispositivo-completo/`
**Funzione**: sintesi operativa del dispositivo completo per il nuovo tema. Integra tutti gli elementi stabilizzati negli step precedenti senza innovazione libera.
**Input**: dispositivo sorgente (f3-step-3 corretto) + tutti gli output di f3-step-8.
**Output**: `output/produzioni/temi/[tema]-dispositivo-completo-vN.json`
**Verifica**: non presente di default (può essere aggiunta).

### f3-step-10 — Stress test del dispositivo
**Cartella**: `f3-step-10-stress-test-dispositivo/`
**Funzione**: stress test finale del dispositivo completo su 5 casi critici (assente, parziale, chiudente, apparente/scripted, quasi indistinguibile).
**Input**: dispositivo completo f3-step-9.
**Output**: `output/produzioni/temi/[tema]-stress-test-dispositivo-vN.json`
**Verifica**: non presente — il global_assessment orienta eventuali correzioni residue.

---

## Struttura degli output

```
output/produzioni/
  ricerche/
    [nome-ricerca]/          ← una cartella per ogni run di f2-step-1
      theme-discovery-vN.json
      theme-relevance-vN.json
      node-verification-v1.json     ← f2-step-2a (Nodi Trasversali canonici)
      theme-verification-vN.json
      theme-matrix-vN.json
      ce-prototipica-v1.json        ← f2-step-4b (CE Prototipica)
      output-family-vN.json
      output-tipo-vuoto-v1.json     ← f2-step-6 (Passaporto del tema → input F3)
  temi/
    [nome-tema]/             ← una cartella per ogni tema portato in F3
      [file f3-step-1..10]-vN.json
      revisioni.md           ← feedback epis