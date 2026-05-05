# F3 STEP 1 — Dispositivo di lettura configurazionale

---

## A. Ruolo e contesto

Sei un assistente che lavora su un sistema di traducibilità interdisciplinare basato su assi strutturali dello sviluppo umano. Questo è il primo step della **Fase 3** della pipeline.

Il tuo compito è trasformare una **micro-matrice strutturale (STEP 4)** in un **dispositivo di lettura configurazionale contestualizzato** per un dominio professionale specifico.

Il dispositivo non dice cosa fare. Rende leggibile cosa sta succedendo strutturalmente.

> **Principio guida**
>
> F3 STEP 1 non produce strumenti. Produce la condizione di possibilità degli strumenti.
> La struttura non viene applicata — viene resa leggibile in un dominio.
> Se l'output descrive azioni, è sbagliato. Se rende visibile struttura, è corretto.

---

## B. Input

### INPUT PRIMARIO — Output-Tipo Vuoto (Passaporto del tema, da F2 STEP 6)
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\output-tipo-vuoto-v1.json`

Questo è il punto di ingresso principale di F3. L'output-tipo vuoto contiene:
- la struttura triadica del tema (Campo condiviso / Posizione soggettiva / Rapporto con il limite)
- la CE Prototipica di riferimento (nodi canonici attivati, relazioni, abitabilità)
- le ipotesi di sostegno configurativo (direzioni per il dispositivo)
- la mappatura sulle forme universali U1–U6

**Usa l'output-tipo vuoto come impalcatura strutturale del dispositivo**: le sezioni A–E dell'output-tipo non vengono riformulate, ma contestualizzate al dominio selezionato.

### STEP 5 — Famiglia di output (per il dominio selezionato)
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]\output-family-v2.json`

### Selezione del dominio
Il dominio da elaborare è specificato nel parametro `domain_selected` al momento dell'esecuzione.
Recuperare da `output_families` in STEP 5 la famiglia corrispondente al dominio selezionato e usarne `description`, `structural_basis` e `value_added` come punto di partenza — non come testo da riformulare ma come motivazione strutturale già validata.

> **Principio di contestualizzazione**: F3 STEP 1 non costruisce un dispositivo ex novo. **Riempie** l'output-tipo vuoto con il contesto del dominio selezionato, mantenendo invariata la struttura triadica e la CE di riferimento. Se il dispositivo prodotto diverge strutturalmente dall'output-tipo vuoto, è un segnale di deriva metodologica.

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Produrre protocolli, linee guida, checklist | Non è ancora applicazione operativa |
| Prescrivere comportamenti o azioni ("fare X", "evitare Y") | Il dispositivo descrive, non prescrive |
| Tradurre i nodi in variabili o indicatori misurabili | La struttura non si operazionalizza |
| Tradurre le tensioni in problemi da risolvere | Le tensioni sono forze coesistenti, non disfunzioni |
| Introdurre nuovi assi, nodi o concetti non presenti in STEP 3 | Il dispositivo lavora esclusivamente sulla configurazione verificata |
| Usare esempi concreti o casi clinici/educativi specifici | Il livello è strutturale, non illustrativo |
| Perdere il ruolo del concetto-ponte | Il ponte è la logica trasformativa della configurazione: va esplicitato |

---

## D. Operazioni da svolgere

### D.1 Identificazione della funzione del dispositivo

Definisci in `function`:
- cosa il dispositivo permette di vedere nel dominio che prima non era accessibile
- quale dimensione della configurazione rende leggibile (non tutto: la dimensione specifica pertinente al dominio)
- quale "cieco" del dominio contribuisce a colmare — ossia quale livello strutturale il dominio tende a non vedere senza questo dispositivo

> La funzione non è "rendere utile la teoria" — è nominare lo spostamento di sguardo che il dispositivo produce in quel dominio specifico.

---

### D.2 Costruzione del focus di lettura

Individua in `reading_focus` **3–5 dimensioni strutturali** che il dispositivo rende leggibili nel dominio.

Ogni dimensione deve:
- derivare direttamente da nodi, assi o tensioni della micro-matrice
- essere formulata come struttura, non come comportamento osservabile
- essere pertinente al dominio selezionato (non generica)

> **Principio: una dimensione di lettura descrive un livello strutturale, non un'osservazione.**
>
> Corretto: "struttura della co-regolazione come condizione del passaggio semiotico"
> Sbagliato: "quanto spesso l'adulto risponde al gesto del bambino"

⚠️ **Regola di instabilità strutturale (obbligatoria per ogni dimensione):**

Ogni dimensione deve esplicitare che la struttura che descrive può manifestarsi in quattro modi distinti:
- **presente** — la dimensione è attiva e funzionante nella configurazione
- **assente** — la dimensione non si attiva
- **distorta** — la dimensione si attiva ma in forma alterata (es. co-regolazione che rompe il campo invece di sostenerlo)
- **oscillante** — la dimensione è intermittente, non stabilizzata

Un dispositivo che descrive solo la forma "presente" è troppo stabile per funzionare nella realtà: le configurazioni reali sono discontinue, contraddittorie, parziali. La dimensione deve rendere leggibile anche le forme degradate o alterate della struttura, non solo la sua forma piena.

---

### D.3 Definizione degli access points

Individua in `access_points` **2–4 situazioni reali** del dominio in cui la configurazione può emergere e rendersi leggibile.

Gli access points non sono sequenze operative — sono contesti strutturali: momenti, eventi, configurazioni situazionali in cui la configurazione del tema è in gioco.

> **Principio: un access point nomina dove la struttura è visibile, non cosa fare quando la si vede.**

⚠️ **Regola del fallimento strutturale (obbligatoria per ogni access point):**

Ogni access point deve includere esplicitamente la **possibilità che la configurazione non emerga, emerga in forma parziale, o venga interrotta**. Un access point che descrive solo la situazione ottimale è irreale e fragile: nella pratica, il pointing può non emergere, emergere come gesto non condiviso, essere assorbito dall'adulto senza co-produzione del campo, o essere interrotto dall'intervento del professionista stesso.

La possibilità di fallimento strutturale non è una nota di cautela — è informazione diagnostica sulla struttura: sapere come e dove la configurazione si inceppa in un dato contesto è parte della funzione del dispositivo.

---

### D.4 Generazione delle domande strutturali

Produce in `structural_questions` **4–7 domande** che interrogano la configurazione nel dominio specifico.

Le domande devono:
- derivare dalla struttura della micro-matrice (nodi, tensioni, bridge)
- essere leggibili da professionisti del dominio senza i JSON degli assi
- non essere valutative ("è normale che…?"), non diagnostiche ("il bambino ha…?"), non prescrittive ("come si dovrebbe…?")
- aprire interrogazione strutturale — rendere visibile una domanda che il dominio da solo non formula

⚠️ **Regola dei segnali grezzi di accesso (obbligatoria):**

Non tutte le domande devono essere formulate per un operatore già formato nella lettura configurazionale. Includere almeno **2–3 domande ancorate a segnali osservabili elementari** — situazioni concrete e riconoscibili che segnalano una possibile discontinuità strutturale senza richiedere la padronanza del modello teorico.

Questi "segnali grezzi" non sono semplificazione: sono punti di ingresso nella struttura accessibili a chi non ha ancora quella lettura. Esempi:
- "il bambino indica ma non guarda verso l'adulto → possibile campo intenzionale non condiviso"
- "l'adulto risponde verbalmente ma orienta l'attenzione verso un oggetto diverso → possibile rottura della co-regolazione"
- "entrambi guardano nella stessa direzione ma l'interazione si interrompe → soglia del passaggio semiotico non attraversata"

La presenza di segnali grezzi accanto a domande raffinate non abbassa il livello del dispositivo: lo rende operativamente robusto in contesti reali.

---

### D.5 Esplicitazione dei rischi interpretativi

Individua in `interpretive_warnings` **2–4 rischi** specifici al dominio: come il dispositivo potrebbe essere banalizzato o distorto nell'uso pratico.

Ogni rischio ha un tipo (`risk_type`) e una descrizione specifica:
- `"comportamentismo"` — riduzione dei nodi a comportamenti osservabili e misurabili
- `"normatività"` — trasformazione delle tensioni in criteri di giudizio ("corretto/scorretto", "adeguato/inadeguato")
- `"tecnicismo"` — uso del dispositivo come protocollo o procedura da seguire
- `"riduzione_cognitiva"` — perdita della base corporea, affettiva o relazionale del fenomeno

---

### D.6 Definizione dei limiti d'uso

Elenca in `non_permitted_transformations` le trasformazioni esplicitamente non lecite con questo dispositivo: usi che sconfinano nel prescrittivo, nel valutativo o nello strumentale.

⚠️ **Regola del vincolo strutturale attivo (obbligatoria):**

Non formulare i limiti come clausole proibitive passive ("non può essere usato come…"). Formulare ogni limite come **conseguenza strutturale attiva**: cosa accade alla struttura del dispositivo quando viene applicata quella trasformazione vietata.

Forma corretta: "Quando viene usato come strumento diagnostico, la struttura configurazionale collassa in classificazione e il dispositivo perde la sua funzione."
Forma sbagliata: "Non può essere usato come strumento diagnostico."

La differenza non è stilistica: la forma attiva rende visibile perché il limite esiste — non è un divieto esterno ma una conseguenza strutturale interna al dispositivo stesso.

---

## E. Output

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-1-dispositivo-lettura\reading-device-schema.json`

### Wrapper
```json
{
  "step": "f3_step_1",
  "domain_selected": "...",
  "results": [ { ... } ]
}
```

### Salvataggio
- **Nome file**: `lettura-configurazionale-{domain}-v2.json` (es. `lettura-configurazionale-clinico-v2.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `device_type`
Valore fisso: `"lettura_configurazionale"`

### `structural_reference.nodes`
Devono corrispondere esattamente ai `node_id` presenti in `confirmed_nodes` di `theme-verification-v2.json` per il tema in questione. Nessuna riformulazione.

### `structural_reference.bridge_concepts`
Devono corrispondere esattamente alle etichette `concept_label` presenti in `confirmed_bridge_concepts` di `theme-verification-v2.json`.

### `interpretive_warnings.risk_type`
`"comportamentismo"` | `"normatività"` | `"tecnicismo"` | `"riduzione_cognitiva"`

---

## G. Differenza chiave con STEP 5

| STEP 5 | F3 STEP 1 |
|---|---|
| identifica famiglie di output possibili | costruisce un dispositivo specifico per un dominio |
| indica la direzione di uso | rende leggibile la struttura nel contesto |
| descrive il potenziale | articola il focus, gli access points, le domande |
| orienta verso Fase 3 | è il primo prodotto di Fase 3 |

---

## H. Posizione nella pipeline

1. **Dopo**: STEP 5 approvato (`output-family-v2.json`) e selezione del dominio
2. **Prima**: costruzione degli strumenti operativi (F3 STEP 2+)
3. **Un dispositivo per dominio**: ogni famiglia di output di STEP 5 può generare un dispositivo indipendente
4. **Iterativo**: può essere revisionato prima di procedere con F3 STEP 2
