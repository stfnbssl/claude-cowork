# F2 STEP 2a — Verifica e mappatura sui Nodi Trasversali canonici

---

## A. Ruolo e contesto

Sei un assistente che lavora su un progetto di modellizzazione dello sviluppo umano basato su sei assi strutturali e sette Nodi Trasversali canonici (N1–N7). Questo è lo **STEP 2a** della pipeline F2 — si esegue subito dopo lo STEP 2 (Rilevanza strutturale) e prima della verifica.

Il tuo compito è verificare se i nodi candidati prodotti in STEP 2 corrispondono, anche parzialmente, ai **Nodi Trasversali canonici** del modello HCAIRE (N1–N7). La corrispondenza non è obbligatoria: un nodo derivato può non mappare su nessun nodo canonico. Ma la mappatura — dove esiste — deve essere dichiarata esplicitamente, perché garantisce la tracciabilità metodologica tra il tema specifico e l'architettura strutturale del modello.

> **Principio guida**
>
> I Nodi Trasversali canonici (N1–N7) sono **invarianti strutturali** del modello HCAIRE.
> Ogni tema specifico porta nodi propri (dal vocabolario degli assi) ma può — e spesso deve — attivare alcune di queste invarianti.
> Questo step non produce nuovi nodi: verifica la relazione tra i nodi già candidati e il sistema canonico.

---

## I sette Nodi Trasversali canonici

| ID | Nome | Struttura | Assi coinvolti |
|---|---|---|---|
| N1 | Regolazione / Integrazione dell'esperienza | capacità del sistema di mantenere coerenza interna durante l'azione | 1 — 4 — 6 |
| N2 | Campo relazionale / Co-regolazione | struttura della reciprocità affettiva e corporea | 1 — 2 — 4 |
| N3 | Accesso al mondo condiviso simbolico | apertura verso la condivisione intersoggettiva | 1 — 3 — 6 |
| N4 | Apertura / Esplorabilità del mondo | disponibilità all'esplorazione e alla novità | 1 — 4 — 5 |
| N5 | Separazione / Limite reale | tolleranza della frustrazione e del confine | 2 — 5 — 6 |
| N6 | Continuità temporale del Sé nascente | coerenza diacronica dell'esperienza soggettiva | 1 — 3 — 5 |
| N7 | Desiderio / Direzione dell'esperienza | orientamento attivo verso possibilità significative | 1 — 5 — 6 |

---

## B. Input

### STEP 2 — Nodi candidati (per il tema scelto)
`C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\theme-relevance-v2.json`

Usa esclusivamente i nodi presenti in `candidate_nodes` per il tema che stai analizzando. Non aggiungere nodi non presenti in STEP 2.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Aggiungere nodi non presenti in STEP 2 | Questo step verifica, non produce |
| Forzare una mappatura dove non esiste | Una corrispondenza assente è informazione strutturale, non un fallimento |
| Modificare la denominazione dei nodi candidati | I nodi restano quelli prodotti in STEP 2 |
| Introdurre nuovi Nodi Trasversali canonici | N1–N7 sono fissi per definizione del modello |
| Classificare un nodo come attivazione di N canonico se la sovrapposizione è marginale | Soglia minima: il nodo candidato deve condividere almeno due assi con il Nodo canonico corrispondente **e** avere funzione strutturale affine |
| Forzare ogni nodo candidato su un canonico | Il campo `canonical_mapping` può essere `null` per i nodi correttamente derivati |

---

## D. Operazioni da svolgere

### D.1 Per ogni nodo candidato di STEP 2 (per il tema selezionato):

**Verifica di mappatura su N1–N7:**

1. Confronta gli assi del nodo candidato con gli assi di ciascun nodo canonico.
2. Verifica se la funzione strutturale è affine.
3. Determina il tipo di relazione:
   - `"identico"` — il nodo candidato corrisponde direttamente al nodo canonico (stesso nome o sinonimo riconoscibile, stessa funzione, stessi assi)
   - `"istanza"` — il nodo candidato è una specifica manifestazione del nodo canonico nel tema (es. "co-regolazione nel campo diadico del pointing" come istanza di N2)
   - `"parziale"` — condivisione di alcuni assi e funzione affine, ma non coincidenza piena
   - `null` — nessuna relazione identificabile con i canonici (nodo genuinamente derivato)

**Documentazione obbligatoria per ogni mapping non-null:**
- quale Nodo canonico (`N1`–`N7`)
- tipo di relazione (`identico` | `istanza` | `parziale`)
- motivazione strutturale della corrispondenza (max 2 frasi)

---

### D.2 Verifica della copertura complessiva

Dopo aver processato tutti i nodi candidati, produci:

**Nodi canonici attivati**: lista degli N1–N7 che risultano coperti da almeno un nodo candidato (con tipo di copertura dominante).

**Nodi canonici assenti**: lista degli N1–N7 che nessun nodo candidato attiva. **Non sono lacune da colmare**: la loro assenza è parte della configurazione tematica specifica. Documentare perché la struttura del tema non li richiede.

**Nodi derivati puri** (mapping null): lista dei nodi candidati che non mappano su nessun canonico. Verificare che siano giustificati (criterio di derivazione: soddisfano i requisiti di nodo di STEP 2, e la loro specificità non è catturabile da nessun canonico).

---

### D.3 Valutazione della coerenza configurazionale

Produci `canonical_configuration_assessment`:

- I Nodi canonici attivati formano una configurazione strutturalmente plausibile per il tema? (sì / no / parzialmente — con motivazione)
- Esistono relazioni attese tra Nodi canonici che nel tema risultano assenti? Questo è un segnale di specificità tematica o una lacuna?
- La combinazione di nodi canonici attivati + nodi derivati puri copre adeguatamente la struttura del tema?

---

## E. Output

### Schema
`C:/my/claude/claude-cowork\Sviluppo Bambino\input\produzioni\f2-step-2a-verifica-nodi-trasversali\node-verification-schema.json`

### Wrapper
```json
{
  "step": "f2_step_2a",
  "results": [ { ... } ]
}
```

### Salvataggio
- **Nome file**: `node-verification-v1.json`
- **Cartella**: `C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `canonical_mapping.type`
`"identico"` | `"istanza"` | `"parziale"` | `null`

### `canonical_node_id`
`"N1"` | `"N2"` | `"N3"` | `"N4"` | `"N5"` | `"N6"` | `"N7"` | `null`

### `coverage_type` (in `activated_canonical_nodes`)
`"piena"` (almeno un nodo identico o istanza) | `"parziale"` (solo mappature parziali)

---

## G. Posizione nella pipeline

1. **Dopo**: STEP 2 (`theme-relevance-v2.json`)
2. **Prima**: verifica di STEP 2 (il verificatore può usare questo output per valutare la coerenza tematica)
3. **Dipendenza forte**: STEP 3 (Verifica strutturale) deve tenere conto delle mappature canoniche per validare definitivamente i nodi confermati
4. **Non iterativo**: se STEP 2 viene revisionato, rieseguire STEP 2a

---

## I. Criteri di skip (skip_reason ammesse)

Questo step può essere saltato con `skip_reason` solo se il `skip_reason` corrisponde a uno dei due criteri seguenti. Nessun altro motivo è metodologicamente ammesso.

| Codice | Condizione | Descrizione |
|---|---|---|
| `input_canonico_fornito` | Il ricercatore fornisce direttamente la mappatura N1–N7 | Il ricercatore ha già prodotto o dispone della mappatura canonica (es. da una precedente elaborazione del tema). Deve essere fornita come input strutturato, non solo dichiarata. |
| `tema_canonicamente_noto` | Il tema è già formalizzato nel modello con mappatura stabilita | Il tema è stato già portato in F2 in ricerche precedenti e la mappatura canonica è documentata nel sistema (es. un tema di una ricerca precedente verificata). |

**Conseguenza dello skip**: STEP 3 dovrà ricavare i Nodi canonici direttamente dagli assi confermati di STEP 2, senza la mappatura esplicita. STEP 4b dovrà fare altrettanto per la CE Prototipica. Il rischio è una minore tracciabilità della catena F2→F3.

---

## H. Perché questo step esiste

Senza la mappatura esplicita sui Nodi canonici, la pipeline produce nodi tematici che restano locali al tema. La metodologia HCAIRE richiede che i dispositivi F3 siano costruiti su **invarianti strutturali** (N1–N7), non su vocaboli tematici arbitrari. Questo step garantisce che la catena di traducibilità F2→F3 sia ancorata al sistema canonico del modello, rendendo i dispositivi comparabili tra temi diversi e coerenti con la grammatica delle configurazioni.
