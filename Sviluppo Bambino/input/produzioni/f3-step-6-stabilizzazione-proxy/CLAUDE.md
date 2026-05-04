**CONTESTO**

Stai lavorando sul dispositivo di lettura configurazionale del pointing precoce (F3 STEP 3 già corretto).
Gli stress test (STEP 4) e il meta-audit (STEP 5) hanno evidenziato una fragilità strutturale:

* Il proxy decisivo (“registrazione come partecipazione” / qualità della vocalizzazione finale)
  è:

  * reversibile
  * non ancorato direttamente alla case_description
  * dipendente dalla observed_configuration
  * quindi potenzialmente circolare

Il tuo compito è **stabilizzare un singolo proxy**, rendendolo:

* ancorato a dati osservabili
* indipendente dalla classificazione
* non reversibile (o significativamente meno reversibile)
* utilizzabile senza inferenze sugli stati mentali

---

## ⬦ INPUT ESTERNO — FACOLTATIVO

**Livello di severità del test di non-reversibilità**

Il test di non-reversibilità (operazione 4) può essere eseguito con intensità variabile:

- **Test debole** (default): verifica la plausibilità del proxy — costruisce una contro-lettura ragionevole e valuta se il proxy regge
- **Test forte**: il ricercatore fornisce contro-letture sofisticate basate su casistica reale del dominio — scenari borderline, casi clinici osservati, varianti che la teoria non anticipa facilmente

Per attivare il test forte, il ricercatore fornisce esplicitamente nella richiesta le contro-letture da testare. Se non fornite, l'agente costruisce le contro-letture in autonomia (test debole).

> La differenza non è di rigore logico ma di ancoraggio empirico: un test forte portato da chi conosce il dominio può smontare proxy che sembrano robusti sulla carta.

---

## 🎯 OBIETTIVO

Trasformare il proxy:

> “Registrazione come partecipazione (qualità ascendente-interrogativa della vocalizzazione finale)”

in una forma **epistemicamente robusta**.

---

## 🔴 VINCOLI METODOLOGICI (OBBLIGATORI)

1. **Divieto di inferenze mentali**

   * Non puoi usare formulazioni tipo:

     * “il bambino non sa…”
     * “il bambino intende…”
     * “il bambino si aspetta…”
   * Devi restare sul piano della configurazione osservabile

2. **Divieto di ancoraggio circolare**

   * Il proxy NON può essere supportato da:

     * observed_configuration
     * classificazione finale
   * Deve essere ancorato SOLO a:

     * case_description
     * oppure elementi osservabili esplicitabili

3. **Divieto di proxy singolo ambiguo**

   * Se il proxy rimane reversibile:
     → devi costruire almeno un proxy aggiuntivo indipendente

4. **Divieto di comportamento isolato**

   * Il proxy non può essere un singolo evento (es. “una vocalizzazione”)
   * Deve descrivere una **struttura temporale o relazionale**

---

## 🧩 OPERAZIONI DA SVOLGERE

### 1. DIAGNOSI DEL PROXY ATTUALE

Analizza il proxy originale e specifica:

* perché è reversibile
* dove introduce inferenze
* dove perde ancoraggio fenomenico

---

### 2. SCOMPOSIZIONE STRUTTURALE

Scomponi il proxy in componenti osservabili:

Esempio (solo come forma, non contenuto):

* evento A (prima della risposta)
* evento B (risposta dell’adulto)
* evento C (dopo la risposta)
* relazione temporale tra A–B–C

---

### 3. COSTRUZIONE NUOVO PROXY

Costruisci una nuova versione del proxy che:

* sia descrivibile come sequenza osservabile
* sia verificabile senza sapere la classificazione
* distingua struttura aperta vs chiusa

---

### 4. TEST DI NON REVERSIBILITÀ (OBBLIGATORIO)

Per il nuovo proxy devi:

#### a. Costruire una contro-lettura forte

* mostrare come potrebbe essere letto al contrario

#### b. Rispondere alla contro-lettura

* dimostrare perché il proxy resiste

Se il proxy NON resiste:

👉 devi modificarlo o affiancarne un secondo

---

### 5. VERIFICA DI ANCORAGGIO

Per ogni elemento del proxy, specifica:

* da dove viene osservato (case_description o osservabile esplicito)
* se richiede competenza alta / media / bassa

---

### 6. OUTPUT FINALE

## OUTPUT

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-6-stabilizzazione-proxy\proxy-stabilization-schema.json`

### Salvataggio
- **Nome file**: `stabilizzazione-proxy-{domain}-v1.json` (es. `stabilizzazione-proxy-clinico-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

## ⚠️ CRITERIO DI SUCCESSO

Il proxy è accettabile solo se:

* NON dipende dalla classificazione
* NON richiede inferenze mentali
* NON può essere invertito facilmente
* È leggibile come **struttura dell’interazione**, non come comportamento isolato

Se queste condizioni non sono soddisfatte:

👉 devi dichiarare FALLIMENTO e spiegare perché

---

## 🔚 NOTA

Non stai migliorando una descrizione.

Stai rendendo il dispositivo **ancorato al reale**.

Se il proxy rimane ambiguo ma lo segnali correttamente → è valido.

Se sembra preciso ma è circolare → è da scartare.
