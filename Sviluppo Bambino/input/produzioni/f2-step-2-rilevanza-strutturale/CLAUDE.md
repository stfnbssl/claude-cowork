# STEP 2 — Ipotesi iniziale di rilevanza strutturale

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali. Questo è lo **STEP 2** di una pipeline.

Il tuo compito è costruire una **prima mappa plausibile** di:
- assi coinvolti
- nodi strutturali candidati
- concetti-ponte rilevanti

senza ancora stabilire nulla in modo definitivo.

> **Principio guida**
>
> Lo STEP 2 non dimostra. Lo STEP 2 esplora.
> Se tutto è certo, è sbagliato. Se tutto è possibile, è inutile.

---

## ⬥ INPUT ESTERNO — OBBLIGATORIO

**Scelta del tema (atto / fenomeno)**

Questo step richiede che il ricercatore abbia già scelto quale tema (o quali temi) portare in analisi strutturale. La scelta non è delegabile all'agente: definisce l'**oggetto ontologico** della pipeline — il fenomeno specifico su cui viene costruito tutto il dispositivo a valle.

Esempi validi:
- pointing precoce
- richiesta di aiuto
- offerta spontanea

Se f2-step-1 ha prodotto più candidati (array), il ricercatore seleziona qui quale/i portare avanti. Se f2-step-1 è stato eseguito già in modalità focalizzata su un fenomeno specifico, la scelta è già implicita nel file di discovery.

### Come arriva nel prompt

  Il sistema HCAIRE inserisce la scelta del tema come blocco JSON inline
  nella sezione **`INPUT FORNITI DAL RICERCATORE`** del prompt:

  scelta_tema:
  {
    "tema_scelto": "<id del tema scelto, es. tema_03_co_regolazione_diadica>",
    "descrizione": "...",
    "motivazione_selezione": "...",
    "ricerca_id": "..."
  }

  Usa `tema_scelto` come identificatore canonico del tema da analizzare.
  **Non cercare un file `scelta_tema.json` o simile su disco** — l'input è
  inline nel prompt che stai leggendo.

  Se il blocco è assente o ha `tema_scelto` vuoto/null, **fermati e segnala
  al ricercatore** che la scelta manca: NON scegliere autonomamente fra
  i candidati di step 1 (la scelta è metodologicamente non delegabile
  all'agente).

> **Attenzione**: un tema troppo generico ("comunicazione precoce") o troppo operativo ("training al pointing") non è un oggetto ontologico valido. Deve essere un atto o fenomeno specifico, osservabile, strutturalmente leggibile.


---

## B. Input

### Temi (STEP 1 già approvato)
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-discovery-vN.json`

### JSON precompilati dei sei assi
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\assi-strutturali\precompiled\`

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Confermare definitivamente gli assi | Questo step è esplorativo |
| Costruire una micro-matrice | Riservato a STEP 3+ |
| Produrre sintesi finali o configurazioni evolutive | Riservato a Fase 2–3 |
| Proporre strumenti, interventi o operatività | Nessuna applicazione |
| Inserire un asse solo per completezza | Solo se strutturalmente motivato |
| Usare linguaggio disciplinare chiuso | Mantenere apertura interdisciplinare |

---

## D. Operazioni da svolgere

### D.1 Assi candidati

Per ogni asse dei sei, valuta se è **forte** | **plausibile** | **da_verificare** | (escludi se non rilevante).

Per ogni asse incluso: fornisci una motivazione strutturale senza esempi pratici e senza linguaggio operativo.

> **Principio: un asse è plausibile solo se il fenomeno non è pienamente spiegabile senza di esso.**
>
> Test per ogni asse incluso:
> 1. Il tema perde la sua identità strutturale senza questo asse?
> 2. L'asse aggiunge un livello che nessun altro asse già incluso presidia?
> Se la risposta a entrambe è "no" → escludere l'asse.

⚠️ **Verifiche obbligatorie:**
- **Asse 2** (Affettivo–morale): tende a essere escluso prematuramente. Includere se il tema implica riconoscimento reciproco, interiorizzazione di una presenza, o alterità interiorizzata. **Attenzione però**: plausibile solo se il fenomeno non è spiegabile senza interiorizzazione — non basta che l'interiorizzazione sia possibile come esito.
- **Asse 3** (Normativo–educativo): prudenza per fascia 0–3 anni. Preferire "strutturazione di primi orizzonti di significato" a "trasmissione normativa implicita". Segnalare incertezza in `notes_for_review`.

⚠️ **Soglia di attivazione differenziata per temi micro:**

I temi micro — gesti, atti puntuali, configurazioni circoscritte (es. pointing, sguardo, proto-segni) — richiedono una soglia di attivazione **più alta** per gli assi "alti" (Asse 2, Asse 3, Asse 5). Un atto piccolo e puntuale può essere strutturalmente vicino alla soglia Asse 1 ↔ Asse 6 senza raggiungere i livelli di interiorizzazione, normatività o campo desiderabile. Non forzare una configurazione elementare verso una struttura più densa di quanto il fenomeno richieda.

---

### D.2 Nodi strutturali candidati

**Target: 5–10 nodi per tema.**

**Criteri di inclusione** — un nodo è ammesso solo se soddisfa **almeno 2 di questi 3 criteri**:

1. È direttamente attivato dalla definizione del tema
2. Ha ruolo strutturale (non descrittivo)
3. È centrale nell'asse di origine

> **Test di discriminanza (obbligatorio per ogni nodo candidato):**
>
> 1. Il tema è pensabile senza questo nodo?
> 2. Questo nodo distingue il tema da altri fenomeni simili?
>
> Se la risposta è "sì" alla prima e "no" alla seconda → il nodo è troppo generale → rimuoverlo o sostituirlo con qualcosa di più specifico per il tema.

**Provenienza:**
- 80–90% dei nodi devono provenire dai JSON degli assi (usare l'`id` originale del nodo)
- Massimo 1–2 nodi derivati ex novo → marcarli obbligatoriamente con `"is_derived": true`

**Livello di astrazione corretto:**

| Livello | Esempio | Valido? |
|---|---|---|
| Troppo astratto | "esperienza" | ❌ |
| Troppo concreto | "guardare il libro" | ❌ |
| Corretto | "mediazione simbolica" | ✅ |

---

### D.3 Concetti-ponte

**Target: 2–4 concetti-ponte per tema.**

I concetti-ponte sono strutturalmente più rari dei nodi: devono collegare effettivamente più assi. Un concetto che appartiene a un solo asse non è un concetto-ponte — è un nodo.

Per ogni concetto-ponte incluso:
- collega almeno 2 assi
- aggiunge una relazione nuova (non riformula una relazione già espressa da un altro concetto-ponte)
- non duplica un nodo esistente

> **Principio: ogni ponte deve descrivere una trasformazione, non solo una co-presenza.**
>
> Un concetto-ponte valido risponde alla domanda: "Chi trasforma cosa, attraverso quale processo, con quale esito?" Un ponte che si limita a nominare la connessione tra due assi senza descrivere il movimento strutturale tra essi è descrittivo, non trasformativo — non soddisfa la funzione di ponte.
>
> Esempio: non "corpo e simbolo si intrecciano nel pointing" (co-presenza), ma "il gesto corporeo co-regolato (Asse 1) diventa atto semiotico (Asse 6) solo attraverso la risposta dell'altro" (trasformazione).

---

### D.4 Struttura del tema

Determina se il tema è:
- **`asse_dominante`** — un asse è chiaramente prevalente
- **`multi_assiale`** — distribuito su più assi con peso comparabile
- **`soglia_tra_assi`** — si colloca al confine tra due assi specifici

⚠️ Se multi_assiale con assi co-dominanti: non limitarti a nominarli. Specifica in `notes` la **funzione diversa** di ciascun asse co-dominante (es. "Asse 1 → dimensione esperienziale; Asse 6 → dimensione simbolica e culturale").

---

### D.5 Razionale complessivo

Spiega sinteticamente in `selection_rationale`:
- perché questi assi sono stati selezionati
- come il tema si distribuisce strutturalmente
- quali sono i punti di incertezza

---

## E. Regole di qualità strutturale

Queste regole derivano dalla revisione critica del sistema. Applicarle sistematicamente prima di produrre l'output.

---

### Regola 1 — Nodo ≠ Concetto-ponte

Un elemento non può comparire contemporaneamente in `candidate_nodes` e in `candidate_bridge_concepts`.

- Se è specifico di un asse → **nodo**
- Se connette più assi → **concetto-ponte**

Se un elemento è stato inserito in entrambe le liste, rimuoverlo dalla lista meno appropriata.

---

### Regola 2 — Nodo discriminante

Un nodo deve essere non solo **corretto** per il tema, ma anche **discriminante**: deve essere specificamente attivato da questo tema, non essere applicabile a qualsiasi tema senza modifiche.

Se lo stesso nodo potrebbe comparire identico in molti temi diversi → è troppo generale → eliminarlo o sostituirlo con qualcosa di più specifico.

---

### Regola 3 — Concetto-ponte non ridondante

Un concetto-ponte deve aggiungere una **relazione nuova tra assi**, non riformulare una relazione già presente in un altro concetto-ponte.

Se due concetti-ponte della stessa lista descrivono sostanzialmente la stessa connessione → eliminarne uno.

---

### Regola 4 — Validità del concetto derivato

Un nodo o concetto-ponte con `is_derived: true` è valido solo se soddisfa **tutti e tre** i criteri:

1. Non è ridondante rispetto ai nodi o ai ponti esistenti
2. È necessario per descrivere il tema (senza di esso il tema non è leggibile nella sua specificità)
3. Collega almeno due assi (per i concetti-ponte) o ha un ruolo strutturale chiaro (per i nodi)

Se non soddisfa anche uno solo dei tre → rimuoverlo.

---

### Regola 5 — Densità di configurazione

Gli assi non si attivano allo stesso livello in tutti i fenomeni. Esistono configurazioni **più dense** (tema ampio, molti assi ad alta intensità) e configurazioni **meno dense** (tema circoscritto, pochi assi a livello elementare). Non forzare una configurazione meno densa verso livelli strutturali più alti di quanto il fenomeno richieda.

Un tema micro può essere strutturalmente ricco con soli Asse 1 e Asse 6: non è una limitazione, è la sua configurazione corretta. La densità inferiore non è un difetto — è informazione strutturale.

---

### Regola 6 — Ponte trasformativo

Un concetto-ponte non è valido se si limita a nominare la co-presenza di due assi. Deve descrivere una **trasformazione strutturale**: un passaggio, un processo, un cambiamento di livello che avviene nella relazione tra i due assi.

Per ogni ponte incluso, verificare che risponda a: *chi trasforma cosa, attraverso quale processo, con quale esito sul piano strutturale*. Se il ponte non risponde a questa domanda è descrittivo, non trasformativo — va riformulato o eliminato.

---

---

## F. Output

### Schema
Lo schema completo dei campi è in:
`C:/my/claude/claude-cowork\Sviluppo Bambino\input\produzioni\f2-step-2-rilevanza-strutturale\theme-relevance-schema.json`

### Wrapper output
```json
{
  "step": "step_2",
  "results": [ { ... } ]
}
```

> **F2 è single-tema**: `results` contiene sempre esattamente un elemento — il tema fornito dall'Archivio Temi. Il wrapper è mantenuto per compatibilità tecnica con il backend.

### Salvataggio
- **Nome file**: `theme-relevance-v2.json`
- **Cartella**: `C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## G. Definizioni dei valori ammessi

### `relevance_level` (assi e nodi)
`"forte"` | `"plausibile"` | `"da_verificare"`

### `theme_structure_assessment.type`
`"asse_dominante"` | `"multi_assiale"` | `"soglia_tra_assi"`

---

## H. Posizione nella pipeline

1. **Dopo**: STEP 1 approvato (`theme-discovery-v2.json`)
2. **Prima**: verifica strutturale (STEP 3)
3. **Iterativo**: può essere revisionato prima di passare a STEP 3

---

## I. Step successivo obbligatorio — STEP 2a

Dopo aver prodotto e salvato l'output di questo step, eseguire **f2-step-2a (Verifica Nodi Trasversali)** prima della verifica di STEP 2.

STEP 2a verifica se i `candidate_nodes` prodotti qui corrispondono ai **Nodi Trasversali canonici N1–N7** del modello HCAIRE. La mappatura canonica è metodologicamente necessaria per garantire la tracciabilità tra il tema specifico e l'architettura strutturale del modello — e per consentire a F3 di operare sulla grammatica CE.

**STEP 2a non richiede input aggiuntivi**: legge solo l'output di questo step. Può essere eseguito in sequenza immediata.

**Cartella**: `f2-step-2a-verifica-nodi-trasversali/`
**Output**: `output/produzioni/ricerche/[nome-ricerca]/node-verification-v1.json`
