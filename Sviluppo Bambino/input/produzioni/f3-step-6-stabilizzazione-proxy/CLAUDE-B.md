**CONTESTO**

Hai costruito un proxy strutturalmente più robusto:

> “Co-orientamento finale bilaterale vs. chiusura unilaterale”

Lo STEP 6 ha mostrato che:

* il proxy è meno reversibile del precedente
* ma NON è sempre applicabile
* richiede informazioni fenomeniche specifiche (non sempre presenti)

Questo introduce un problema strutturale:

> Il dispositivo può essere corretto ma **non applicabile senza vincoli espliciti di osservazione**

---

## 🎯 OBIETTIVO

Trasformare il proxy in una forma completa:

> **Proxy + Condizioni di osservabilità + Regole di applicazione**

Il risultato deve impedire:

* applicazioni forzate
* inferenze non controllate
* uso su dati insufficienti

---

## 🔴 VINCOLI METODOLOGICI

1. **Divieto di completamento implicito**

   * Non puoi “assumere” dati mancanti
   * Se un’informazione non è osservata → deve essere dichiarata come assente

2. **Obbligo di non-classificabilità**

   * Devi esplicitare quando il proxy NON può essere usato
   * “Ambiguo” o “non classificabile” è un esito valido

3. **Separazione netta**
   Devi distinguere chiaramente:

   * ciò che è osservato
   * ciò che è inferito
   * ciò che è necessario ma assente

4. **No recupero tramite competenza**

   * Non è valido: “un osservatore esperto capirebbe”
   * Il dispositivo deve funzionare per vincoli, non per intuizione

---

## 🧩 OPERAZIONI DA SVOLGERE

---

### 1. IDENTIFICAZIONE DELLE VARIABILI OSSERVATIVE NECESSARIE

Per il proxy definito, elenca **tutte le informazioni necessarie** per applicarlo correttamente.

Esempio di forma (non contenuto):

* orientamento dello sguardo dell’adulto in fase finale
* durata del co-orientamento
* sequenza temporale degli eventi
* ecc.

---

### 2. CLASSIFICAZIONE DELLE VARIABILI

Per ogni variabile indica:

* **tipo**:

  * direttamente osservabile
  * osservabile con mediazione (es. video)
  * non osservabile

* **livello di dipendenza dall’osservatore**:

  * basso / medio / alto

---

### 3. DEFINIZIONE DELLE CONDIZIONI DI APPLICABILITÀ

Costruisci una sezione:

## “Il proxy è applicabile solo se:”

* elenco minimo di condizioni necessarie
* tutte devono essere soddisfatte

---

### 4. DEFINIZIONE DELLE CONDIZIONI DI NON APPLICABILITÀ

Costruisci una sezione:

## “Il proxy NON è applicabile se:”

* anche una sola condizione mancante
* oppure presenza di ambiguità strutturale

---

### 5. DEFINIZIONE DELL’ESITO CORRETTO IN CASO DI DATI INSUFFICIENTI

Devi specificare:

* cosa deve restituire il dispositivo:

  * non classificabile
  * ambiguo
  * sospeso

* e perché NON deve classificare

---

### 6. RISCRITTURA DEL PROXY IN VERSIONE OPERATIVA

## OUTPUT

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-6-stabilizzazione-proxy\proxy-operativo-schema.json`

### Salvataggio
- **Nome file**: `stabilizzazione-proxy-{domain}-v1b.json` (es. `stabilizzazione-proxy-clinico-v1b.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## ⚠️ CRITERIO DI SUCCESSO

Il risultato è valido solo se:

* impedisce applicazioni su dati incompleti
* non introduce nuove inferenze
* rende esplicito quando NON decidere
* è utilizzabile senza accesso alla observed_configuration

---

## 🔚 NOTA FINALE

Non stai migliorando la precisione del proxy.

Stai introducendo una proprietà fondamentale del dispositivo:

> **la capacità di non funzionare quando non deve funzionare**

Se questa proprietà manca:

👉 il dispositivo produrrà inevitabilmente falsi positivi.
