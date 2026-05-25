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

| Punto | Input richiesto | Cosa definisce |
|---|---|---|
| **archivio temi** (fuori pipeline) | Scelta del tema (atto / fenomeno) e promozione | L'oggetto ontologico della pipeline |
| **f3-step-1** | Scelta del dominio / contesto | Il vincolo di realtà del dispositivo |

### Input facoltativi

| Step | Input possibile | Quando usarlo |
|---|---|---|
| **f3-step-3** | Casi reali del dominio per lo stress test | Sempre raccomandato: l'agente in autonomia produce casi plausibili ma generici |

**Principio**: più l'input è precoce e preciso (scelta del tema), più la generatività della pipeline è alta. Fornire tema sbagliato o dominio ambiguo produce dispositivi strutturalmente fragili anche con esecuzione perfetta degli step.

> **Aggiornamento r3 (2026-05)**: con la riduzione della pipeline F3 a 5 step e la separazione dell'archivio temi dalla pipeline, gli input obbligatori passano da 3 a 2 e i facoltativi da 2 a 1. I vecchi step F3 di "trasferimento a un nuovo tema" (7, 8, 9, 10) sono stati eliminati. Vedi `webapp-hcaire/specifiche/D7-pipeline-f3-redesign.md`.

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

F2 lavora su **un tema per volta**: il tema è scelto nell'Archivio Temi prima di avviare la run e non cambia nel corso di essa. Lo schema di output usa il wrapper `{ "step": "f2_step_N", "results": [ ... ] }` dove `results` contiene sempre esattamente un elemento.

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

## F3 — Step per step (r3 — pipeline ridotta a 5 step)

> **Modifica r3 (2026-05)**: la pipeline F3 è stata ridotta da 10 step a 5 step per allinearla alla metodologia in `HCAIRE Slides/context/metodo/f3-strumenti-operativi.md` e per rimuovere stratificazioni di controllo non previste dal metodo. Vedi `webapp-hcaire/specifiche/D7-pipeline-f3-redesign.md` per la migrazione completa.

F3 lavora su **un tema per volta**, **per dominio**: una pipeline F3 = un dispositivo contestualizzato. Ogni step produce un file JSON dedicato al tema in lavorazione. L'input primario è l'output-tipo vuoto di F2 step 6 (passaporto del tema).

### f3-step-1 — Nodo dominante e funzione
**Cartella**: `f3-step-1-nodo-funzione/`
**Funzione**: identificare il nodo dominante della CE per il dominio scelto e determinare la funzione dell'intervento (1 di 4 categorie chiuse: stabilizzare, ampliare, mediare, proteggere).
**Input primario**: `output-tipo-vuoto-v1.json` (F2 step 6).
**Input esterno obbligatorio**: dominio + context_label + note opzionali del ricercatore.
**Output**: `output/produzioni/temi/<context_id>/nodo-funzione-v{N}.json`
**Verifica**: presente.
**Schema**: `f3-step-1-nodo-funzione/nodo-funzione-schema.json`

### f3-step-2 — Micro-dispositivo di campo
**Cartella**: `f3-step-2-micro-dispositivo/`
**Funzione**: costruzione del micro-dispositivo nel template a 7 campi della metodologia (CE di origine, nodo dominante, funzione, campo bersaglio, 3-5 micro-azioni, tempo reale, indicatore di risonanza), classificato secondo la tipologia universale U1-U6 e dotato di condizioni di non-applicabilità.
**Input primario**: `nodo-funzione-v{N}.json` + `output-tipo-vuoto-v{N}.json`.
**Output**: `output/produzioni/temi/<context_id>/micro-dispositivo-v{N}.json`
**Verifica**: presente.
**Schema**: `f3-step-2-micro-dispositivo/micro-dispositivo-schema.json`

### f3-step-3 — Stress test e correzione
**Cartella**: `f3-step-3-stress-test/`
**Funzione**: stress test integrato del dispositivo su 5 casi tipologici (assenza, parziale, distorta-chiudente, oscillante, apparente-indistinguibile) + eventuale correzione condizionale del dispositivo se i breaking point sono strutturali.
**Input primario**: `micro-dispositivo-v{N}.json` + `nodo-funzione-v{N}.json`.
**Input esterno facoltativo**: casi reali del dominio forniti dal ricercatore (raccomandati).
**Output**: `output/produzioni/temi/<context_id>/stress-test-v{N}.json`
**Verifica**: presente.
**Schema**: `f3-step-3-stress-test/stress-test-schema.json`

### f3-step-4 — Verifica di coerenza F3
**Cartella**: `f3-step-4-coerenza/`
**Funzione**: verifica obbligatoria del dispositivo finale tramite checklist di 10 controlli (5 di coerenza F3 dalla sez. 2.7 della metodologia + 4 di logica decisionale dalla sez. 5.4 + 1 di auto-limitazione dalla sez. 5.6). Verdetto: `valido` / `richiede_revisione` / `fuori_modello`.
**Input primario**: dispositivo finale (da step 2 o, se corretto, da step 3) + esito stress test.
**Output**: `output/produzioni/temi/<context_id>/coerenza-v{N}.json`
**Verifica**: non presente — la verifica *è* lo step.
**Schema**: `f3-step-4-coerenza/coerenza-schema.json`

### f3-step-5 — Output-tipo contestualizzato
**Cartella**: `f3-step-5-output-tipo-contestualizzato/`
**Funzione**: tradurre la struttura triadica astratta dell'output-tipo vuoto (F2 step 6) in uno strumento operativo contestualizzato — il prodotto finale della pipeline F3. Le cinque sezioni A–E vengono "riempite" con il contesto del dominio scelto (esempi orientativi contestuali, cornice linguistica condivisa, snodi decisionali esterni), più sintesi narrativa contestuale, direzione orientativa e riferimento al dispositivo.
**Input primario**: dispositivo finale (`micro-dispositivo-v{N}.json` o, se corretto, la versione corretta da step 3) + `output-tipo-vuoto-v{N}.json` (F2 step 6) + `coerenza-v{N}.json`.
**Output**: `output/produzioni/temi/<context_id>/output-tipo-{dominio}-v{N}.json` *(unico step F3 che mantiene `{dominio}` nel filename — convenzione editoriale per il sito HCAIRE)*
**Verifica**: non presente — è il passo conclusivo della pipeline F3.
**Schema**: `f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json`

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
    <context_id>/            ← <theme_id>--<ambito_id>, una cartella per (tema × ambito)
      nodo-funzione-v{N}.json             ← f3-step-1
      micro-dispositivo-v{N}.json         ← f3-step-2
      stress-test-v{N}.json               ← f3-step-3
      coerenza-v{N}.json                  ← f3-step-4
      output-tipo-{dominio}-v{N}.json     ← f3-step-5 (mantiene {dominio} nel filename)
      revisioni.md                        ← feedback epis