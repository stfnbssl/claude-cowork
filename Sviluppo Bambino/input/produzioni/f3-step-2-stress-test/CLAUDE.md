# F3 STEP 2 — Stress test strutturale del dispositivo

---

## A. Ruolo e contesto

Sei un assistente che lavora su un sistema di traducibilità interdisciplinare basato su assi strutturali dello sviluppo umano. Questo è il secondo step della **Fase 3** della pipeline.

Il tuo compito è sottoporre il dispositivo di lettura configurazionale (F3 STEP 1) a una serie di **casi limite controllati**, al fine di verificare dove mantiene capacità descrittiva, dove produce ambiguità e dove smette di funzionare.

Il compito NON è dimostrare che il dispositivo funziona. È metterlo in difficoltà.

> **Principio guida**
>
> Un buon stress test non cerca i casi in cui il dispositivo è utile.
> Cerca i casi in cui il dispositivo è in difficoltà, produce ambiguità o collassa.
> Se tutti i casi risultano leggibili con bassa ambiguità, lo stress test non è abbastanza severo.

---

## B. Input

### F3 STEP 1 — Dispositivo di lettura configurazionale
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\lettura-configurazionale-{domain}-v2.json`

Sostituire `{domain}` con il dominio selezionato (es. `clinico`).

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Trasformare il dispositivo in checklist per valutare i casi | Lo stress test legge con il dispositivo, non applica scale |
| Introdurre valutazioni normative (corretto / scorretto, adeguato / inadeguato) | Il dispositivo descrive struttura, non giudica |
| Introdurre diagnosi o categorie diagnostiche | Fuori ambito del dispositivo |
| Semplificare i casi per far "funzionare" il dispositivo | I casi devono essere plausibili e sfidanti, non costruiti per dimostrare |
| Omettere i punti di rottura quando il dispositivo è in difficoltà | I limiti del dispositivo sono il risultato principale dello stress test |
| Descrivere casi astratti o puramente teorici | Ogni caso deve essere osservabile e plausibile in contesto reale |

---

## D. Operazioni da svolgere

### D.1 Generazione dei casi strutturali

Produci **almeno 5 casi**, uno per ciascuna tipologia obbligatoria:

| Tipologia | Descrizione |
|---|---|
| `assenza_configurazione` | Nessun livello della configurazione si attiva: il gesto ha la forma esterna del pointing ma non la struttura |
| `configurazione_parziale` | Alcuni livelli sono presenti, altri assenti: la configurazione si attiva parzialmente e si arresta |
| `configurazione_distorta` | I livelli si attivano ma in forma alterata: la co-regolazione rompe il campo invece di sostenerlo, o il passaggio semiotico si produce in modo unilaterale |
| `configurazione_oscillante` | La configurazione si costituisce in modo intermittente: presente in alcuni scambi, assente in altri, senza stabilizzarsi |
| `configurazione_apparente` | Falso positivo strutturale: la configurazione ha forma piena in superficie (tutti i comportamenti attesi sono presenti) ma non struttura genuina — il passaggio è riproduzione di uno script, non co-produzione |

Ogni caso deve essere:
- **concreto**: descrive una situazione specifica e osservabile, non una categoria astratta
- **plausibile**: potrebbe accadere realmente nel dominio selezionato
- **sfidante**: costruito per mettere il dispositivo in difficoltà, non per dimostrarne la funzionalità

⚠️ **Il caso `configurazione_apparente` è il più importante**: è il caso in cui il dispositivo è maggiormente a rischio di fallire silenziosamente — producendo una lettura apparentemente coerente su una configurazione che non è tale.

---

### D.2 Applicazione del dispositivo a ogni caso

Per ogni caso, descrivere:

**a) La configurazione osservata** — cosa accade a livello di ciascun nodo:
- corporeità vissuta
- campo intenzionale
- co-regolazione
- mediazione simbolica

La descrizione è strutturale, non valutativa: descrive lo stato del nodo nel caso, non se è "buono" o "cattivo".

**b) Il comportamento del dispositivo** — il dispositivo:
- riesce a leggere il caso? (cosa legge e cosa rimane opaco)
- quale livello di ambiguità produce su questo caso?

---

### D.3 Identificazione del punto di rottura

Se il dispositivo non funziona pienamente su un caso:
- dove si localizza la rottura (quale dimensione, quale passaggio strutturale)
- perché si rompe (limite strutturale del dispositivo, ambiguità concettuale, nodo insufficiente)

Se il dispositivo funziona senza rotture evidenti, indicare comunque la zona di maggiore fragilità — il punto in cui un uso approssimativo del dispositivo potrebbe produrre mislettura.

---

### D.4 Valore discriminante

Per ogni caso: cosa rende questo caso strutturalmente diverso da altri simili in superficie? Il dispositivo riesce a cogliere questa differenza o tende a uniformare casi che sono strutturalmente distinti?

---

### D.5 Rischi di mislettura

Per ogni caso, identificare due livelli di rischio:
- **senza dispositivo**: quale errore farebbe un operatore che legge il caso con le categorie abituali del dominio
- **con dispositivo usato male**: quale errore specifico questo caso facilita quando il dispositivo viene applicato in modo scorretto (come checklist, in modo normativo, senza tenere presente il bridge)

---

## E. Output

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-2-stress-test\stress-test-schema.json`

### Salvataggio
- **Nome file**: `stress-test-{domain}-v2.json` (es. `stress-test-clinico-v2.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `case_type`
`"assenza_configurazione"` | `"configurazione_parziale"` | `"configurazione_distorta"` | `"configurazione_oscillante"` | `"configurazione_apparente"`

### `device_performance.ambiguity_level`
`"basso"` — il dispositivo legge il caso con chiarezza strutturale
`"medio"` — il dispositivo legge ma produce zone di opacità significative
`"alto"` — il dispositivo è in seria difficoltà: la lettura è parziale o ambigua in modo rilevante

### `breaking_point.present`
Se `false`: i campi `where` e `why` sono omessi. Indicare comunque in `device_performance.what_becomes_unclear` la zona di fragilità.

---

## G. Differenza chiave con F3 STEP 1

| F3 STEP 1 | F3 STEP 2 |
|---|---|
| costruisce il dispositivo | lo mette sotto pressione |
| descrive cosa rende leggibile | verifica su cosa smette di farlo |
| formula le dimensioni di lettura | le testa su casi limite |
| identifica i rischi in astratto | li rende concreti su casi specifici |

---

## H. Posizione nella pipeline

1. **Dopo**: F3 STEP 1 approvato (`lettura-configurazionale-{domain}-v2.json`)
2. **Prima**: revisione del dispositivo (F3 STEP 1 eventualmente aggiornato) o costruzione degli strumenti operativi
3. **Funzione**: i punti di rottura identificati qui orientano la revisione del dispositivo prima di passare alla costruzione degli strumenti
