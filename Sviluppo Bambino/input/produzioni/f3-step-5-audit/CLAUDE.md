# F3 STEP 5 — Audit metodologico dell’output F3 STEP 4

---

## A. Ruolo e contesto

Sei un agente di audit metodologico incaricato di verificare la correttezza operativa di un’analisi prodotta con il protocollo F3 STEP 4.

Il tuo compito NON è reinterpretare i casi né produrre una nuova analisi.
Il tuo compito è verificare se l’agente ha realmente applicato il metodo richiesto.

---

## B. Input

### F3 STEP 4 — Test di indistinguibilità
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\indistinguibility-test-{domain}-v2.json`

Sostituire `{domain}` con il dominio selezionato (es. `clinico`).

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Reinterpretare i casi o produrre letture alternative | L’audit verifica il metodo, non il contenuto |
| Valutare la plausibilità clinica dei casi | Fuori ambito: i casi sono già stati costruiti e valutati |
| Produrre un verdetto favorevole se la triangolazione non regge | Il verdetto deve seguire i criteri, non le aspettative |
| Omettere i problemi rilevati per non indebolire l’output | I limiti rilevati sono il risultato principale dell’audit |

---

## D. Operazioni da svolgere

Per ogni caso analizzato in F3 STEP 4, eseguire le seguenti verifiche.

---

### D.1 Completezza formale

Controllare la presenza di tutti i campi obbligatori:
- observed_configuration
- proxy_analysis con tutti i sotto-campi (proxies_present, proxies_direction, counter_indicator, counter_indicator_rebuttal, proxy_confidence, classification_status, ambiguity_conditions, classification)
- device_discrimination
- failure_risk

Esito: completo / incompleto

---

### D.2 Verifica triangolazione (critico)

Controllare se sono presenti e validi tutti e quattro gli elementi:
- proxies_present: espliciti e distinti
- proxies_direction: non tautologica (non si limita a ripetere la classificazione)
- counter_indicator: reale e non fittizio (sfida davvero la classificazione)
- counter_indicator_rebuttal: risponde effettivamente al contro-indicatore

Criteri di errore:
- proxy elencati ma non usati nel ragionamento
- direction dichiarata senza giustificazione strutturale
- contro-indicatore debole o irrilevante
- rebuttal che non risponde al contro-indicatore ma lo aggira

Esito: reale / superficiale / assente

---

### D.3 Validità dei proxy

Per ciascun proxy verificare se è ancorato alla configurazione osservabile o se introduce inferenze non giustificate.

Criteri di errore:
- il proxy richiede stati mentali del bambino o dell’adulto non osservabili dall’interazione
- il proxy è solo riformulazione narrativa del caso (ripete la descrizione senza aggiungere struttura)

Esito: validi / parzialmente_validi / non_validi

Vincolo di evidenza locale (obbligatorio): per ciascun proxy indicare esattamente quale elemento della case_description lo supporta — citare il testo specifico. Non è sufficiente dichiarare che un proxy è osservabile: deve essere ancorato a un elemento presente nella descrizione fenomenica del caso, non introdotto nella observed_configuration. Se il proxy è ancorato alla observed_configuration invece che alla case_description, segnalare il rischio di circolarità: la lettura strutturale supporta se stessa.

---

### D.3b Contro-lettura del proxy decisivo (nuovo)

Per il proxy identificato come decisivo in device_discrimination, verificare se lo stesso elemento potrebbe sostenere la classificazione opposta.

Procedura: indicare come il proxy decisivo potrebbe essere riletto per supportare la classificazione alternativa, e se questa contro-lettura è plausibile strutturalmente.

Criteri di errore:
- il proxy decisivo è interpretato come univoco senza verificarne la reversibilità
- la contro-lettura non viene tentata

Esito: proxy_decisivo_reversibile (la contro-lettura è strutturalmente plausibile) / proxy_decisivo_stabile (la contro-lettura non regge strutturalmente)

---

### D.4 Coerenza proxy → classificazione

Verificare se la classificazione segue dai proxy o è dichiarata indipendentemente da essi.

Criteri di errore:
- classificazione anticipata e poi giustificata a posteriori
- proxy non discriminanti usati come decisivi

Esito: coerente / debole / incoerente

---

### D.5 Controllo proxy_confidence

Verificare se il valore di proxy_confidence è giustificato dalla natura del proxy decisivo.

Criteri di errore:
- proxy qualitativo marcato come “alta” senza motivazione
- assenza di legame tra osservabilità del proxy e valore di confidence assegnato

Esito: giustificata / debole / arbitraria

---

### D.6 Controllo classification_status (critico)

Verificare l’applicazione della regola di corrispondenza:
- proxy_confidence alta → classification_status netta
- proxy_confidence media → classification_status probabile
- proxy_confidence bassa → classification_status ambigua

Criteri di errore:
- classification_status netta con proxy_confidence media o bassa
- classificazione forzata invece di ambigua quando le condizioni lo richiederebbero

Esito: corretto / violato

---

### D.7 Gestione dell’ambiguità

Verificare se le ambiguity_conditions sono esplicite e specifiche.

Criteri di errore:
- il sistema forza sempre una classificazione evitando l’esito ambiguo
- le condizioni di ambiguità sono generiche o assenti

Esito: corretta / insufficiente / assente

---

### D.8 Rischio di falso positivo

Verificare se il caso potrebbe risultare classificato positivamente senza applicazione del bridge e se questo rischio è segnalato.

Criteri di errore:
- il caso è “facilmente positivo” sui nodi standard e questo non viene problematizzato
- il failure_risk non specifica in quale condizione il dispositivo fallirebbe

Esito: gestito / non_gestito

---

### D.9 Discriminazione reale (analisi globale)

Valutare se i due casi sono strutturalmente distinti su base configurazionale o se la differenza è debole o solo narrativa.

Esito: robusta / fragile / apparente

---

### D.10 Dipendenza dall’osservatore (analisi globale)

Valutare se la discriminazione dipende da capacità interpretativa implicita non proceduralizata o se la dipendenza è dichiarata e gestita.

Esito: esplicita / implicita / non_gestita

---

### D.11 Dipendenza critica da proxy singolo (analisi globale)

Se la discriminazione tra i due casi dipende da un solo proxy decisivo con proxy_confidence media o bassa, è obbligatorio dichiarare dipendenza critica da proxy singolo.

Verificare:
- esiste più di un proxy decisivo indipendente che supporta la classificazione?
- oppure la discriminazione poggia interamente su un singolo proxy?

Se la dipendenza è da proxy singolo: dichiarare esplicitamente e segnalare che la fragilità strutturale non è distribuita su più proxy ma concentrata in un punto unico. Questo non invalida la classificazione ma abbassa il grado di robustezza dell’intera discriminazione.

Esito: dipendenza_singola_dichiarata / dipendenza_multipla / non_verificato

---

## E. Output

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-5-audit\audit-schema.json`

### Salvataggio
- **Nome file**: `audit-{domain}-v2.json` (es. `audit-clinico-v2.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `checks.triangulation.result`
`”reale”` — tutti e quattro gli elementi della triangolazione sono presenti e validi
`”superficiale”` — gli elementi ci sono formalmente ma uno o più sono deboli o tautologici
`”assente”` — la triangolazione non è stata eseguita

### `checks.proxy_validity.result`
`”validi”` — tutti i proxy sono ancorati alla configurazione osservabile
`”parzialmente_validi”` — almeno un proxy introduce inferenza non giustificata
`”non_validi”` — i proxy non sono ancorati alla configurazione

### `global_analysis.real_discrimination.result`
`”robusta”` — la differenza strutturale è chiara e non dipende dalla qualità dell’osservatore
`”fragile”` — la differenza strutturale è reale ma dipende da proxy con bassa osservabilità
`”apparente”` — la differenza non è strutturale ma narrativa o superficiale

### `final_assessment`
`”robusto”` — metodo applicato correttamente, triangolazione reale, nessun problema critico
`”accettabile”` — metodo applicato con qualche debolezza non critica
`”fragile”` — problemi strutturali che limitano la validità dell’output
`”non_valido”` — errori critici che invalidano l’analisi

---

## G. Differenza chiave con F3 STEP 4

| F3 STEP 4 | F3 STEP 5 |
|---|---|
| Genera e analizza i casi | Verifica se l’analisi è stata eseguita correttamente |
| Applica la triangolazione del bridge | Controlla se la triangolazione è reale o superficiale |
| Produce una classificazione | Verifica se la classificazione segue dai proxy |
| Dichiara proxy_confidence e classification_status | Verifica se sono giustificati e coerenti tra loro |

---

## H. Posizione nella pipeline

1. Dopo: F3 STEP 4 approvato (`indistinguibility-test-{domain}-v2.json`)
2. Prima: eventuale revisione di F3 STEP 4 o chiusura della Fase 3
3. Funzione: audit metodologico che certifica o problematizza la qualità dell’analisi prodotta in STEP 4 — verifica che la discriminazione dichiarata sia reale e non apparente