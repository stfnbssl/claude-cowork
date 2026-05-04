# F3 STEP 4 — Stress test di indistinguibilità apparente

---

## A. Ruolo e contesto

Sei un agente analitico che opera nella Fase 3 (F3) del sistema. Questo è il quarto step della Fase 3.

Il tuo compito è verificare la capacità discriminativa del dispositivo corretto (F3 STEP 3) su casi che sono comportamentalmente quasi identici ma strutturalmente distinti. Non è un test di funzionamento del dispositivo — è un test del suo limite critico: riesce a distinguere forma da struttura quando la forma è la stessa?

> Principio guida
>
> Se i due casi risultano distinguibili solo attraverso inferenze non ancorate alla configurazione (interpretazioni psicologiche del bambino o del caregiver, giudizi di qualità, informazioni contestuali esterne all'interazione), il test è fallito.

---

## B. Input

### F3 STEP 3 — Dispositivo corretto
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\correzione-strutturale-clinico-v2.json`

---

## C. Vincoli — cosa NON fare

| Divieto | Perché |
|---|---|
| Introdurre differenze esplicite tra i due casi (bambino più attivo, caregiver più freddo) | La differenza deve emergere solo dalla struttura del processo, non dal contenuto |
| Usare indicatori comportamentali diretti per distinguere i casi (durata, frequenza, latenza) | La distinzione deve essere strutturale, non metrica |
| Costruire casi in cui la differenza è immediatamente ovvia a lettura fenomenica | I casi devono sfidare la discriminazione, non facilitarla |
| Produrre un verdetto favorevole se la triangolazione non regge | Se il dispositivo non discrimina su base strutturale, il risultato deve essere dichiarato negativo |

---

## D. Operazioni da svolgere

### D.1 Generazione dei due casi

Genera due casi clinici di pointing precoce (età 14–24 mesi) che siano comportamentalmente quasi identici: stessi gesti, stessa sequenza osservabile, stessa qualità apparente dell'interazione.

I due casi devono differire SOLO a livello strutturale nella dimensione del passaggio trasformativo (bridge):

- Caso A: configurazione_reale — passaggio aperto (co-produzione genuina)
- Caso B: configurazione_apparente — passaggio predeterminato (script o chiusura anticipata)

Vincoli di costruzione dei casi:

- I comportamenti osservabili devono essere il più possibile sovrapponibili
- Non introdurre differenze esplicite nel contenuto (età, setting, tipo di oggetto, tono dell'adulto)
- La differenza deve essere strutturale e non immediatamente visibile a lettura fenomenica

---

### D.2 Lettura configurazionale di ciascun caso

Per ogni caso, produrre:

a) observed_configuration — stato di ciascun nodo: corporeità-vissuta, campo-intenzionale, co-regolazione, mediazione-simbolica, e stato del passaggio trasformativo (bridge)

b) proxy_analysis — applicazione esplicita della triangolazione obbligatoria del bridge:
- quali proxy strutturali sono presenti nel caso
- perché questi proxy indicano apertura o predeterminazione
- almeno un contro-indicatore con spiegazione del perché viene scartato
- classificazione finale: aperto / predeterminato / ambiguo

Regola stabile per ogni classificazione strutturale: è obbligatorio indicare tutti e quattro gli elementi seguenti.
1. il proxy decisivo (quello su cui poggia la classificazione)
2. il grado di osservabilità del proxy: alta (direttamente leggibile), media (richiede attenzione qualitativa specifica), bassa (inferenziale, non direttamente osservabile)
3. se la classificazione risultante è netta (la triangolazione è robusta), probabile (la triangolazione regge ma dipende dalla qualità dell'osservazione del proxy decisivo) o ambigua (i proxy non producono lettura netta)
4. le condizioni in cui la classificazione deve diventare ambigua: in quale circostanza il proxy decisivo perde osservabilità e la classificazione non deve essere forzata

Il principio che questa regola fissa è: il dispositivo discrimina tra configurazione reale e configurazione apparente quando il bridge è triangolabile attraverso proxy qualitativi sufficientemente osservabili. Se il proxy decisivo non è osservabile o ha bassa affidabilità, l'esito corretto non è una classificazione forzata, ma una classificazione ambigua.

Questi quattro elementi vanno nei campi proxy_confidence, classification_status e ambiguity_conditions della proxy_analysis.

c) alternative_interpretation — perché il caso potrebbe essere letto nell'altro modo

d) device_discrimination — il dispositivo corretto distingue questo caso? su quali basi? quale dimensione è discriminante?

e) failure_risk — in quali condizioni il dispositivo fallirebbe su questo caso specifico

---

### D.3 Analisi comparativa

Produce un'analisi che mette a confronto i due casi:

- somiglianza comportamentale: cosa li rende indistinguibili a lettura fenomenica
- differenza strutturale: dove e perché differiscono a livello di configurazione
- fattore discriminante: quale elemento del dispositivo corretto rende la differenza leggibile

---

### D.4 Verdetto del test

Produce un verdetto strutturale:

- il dispositivo discrimina i due casi su base strutturale?
- su quali basi specifiche?
- quale ambiguità residua rimane anche con il dispositivo corretto?

Se i due casi sono distinguibili solo attraverso inferenze esterne alla configurazione, il verdetto deve essere dichiarato negativo: il dispositivo non ha superato il test.

---

## E. Output

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-4-indistinguibilità\indistinguibility-test-schema.json`

### Salvataggio
- **Nome file**: `indistinguibility-test-{domain}-v2.json` (es. `indistinguibility-test-clinico-v2.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## F. Definizioni dei valori ammessi

### `case_type`
`"configurazione_reale"` — passaggio aperto, co-produzione genuina
`"configurazione_apparente"` — passaggio predeterminato, script

### `proxy_analysis.classification`
`"aperto"` — la triangolazione indica passaggio aperto con contro-indicatore scartato
`"predeterminato"` — la triangolazione indica script con contro-indicatore scartato
`"ambiguo"` — la triangolazione non produce lettura netta: i proxy sono insufficienti o contraddittori

### `test_verdict.device_discriminates`
`true` — il dispositivo discrimina i due casi su base strutturale ancorata alla configurazione
`false` — la distinzione richiede inferenze esterne alla configurazione: il test è fallito

---

## G. Differenza chiave con F3 STEP 2

| F3 STEP 2 | F3 STEP 4 |
|---|---|
| Testa il dispositivo su casi strutturalmente diversi | Testa il dispositivo su casi strutturalmente quasi identici |
| Verifica dove il dispositivo si rompe | Verifica se il dispositivo distingue quando la forma è la stessa |
| Cerca breaking points su tipi diversi di configurazione | Cerca l'unico punto discriminante tra casi quasi identici |
| Genera 5 casi di tipo diverso | Genera 2 casi costruiti per essere indistinguibili |

---

## H. Posizione nella pipeline

1. Dopo: F3 STEP 3 approvato (`correzione-strutturale-clinico-v2.json`)
2. Prima: eventuale ulteriore revisione del dispositivo o passaggio alla costruzione degli strumenti operativi
3. Funzione: test critico della capacità discriminativa del dispositivo corretto — verifica che la correzione del bridge sia sufficiente a distinguere configurazione reale da configurazione apparente quando la forma comportamentale è la stessa
