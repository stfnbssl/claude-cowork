STEP 9 non è più analisi o correzione — è **sintesi operativa del dispositivo**.

Ti propongo un **prompt completo**, coerente con tutta la pipeline che hai costruito (STEP 3 → STEP 8), ma con un vincolo forte:
👉 **non deve reinventare nulla**, deve solo integrare ciò che è già stato stabilizzato.

---

# 🔷 PROMPT — F3 STEP 9

**Costruzione del dispositivo completo (nuovo tema)**

---

## 🧭 RUOLO

Agisci come **costruttore di dispositivi configurazionali**.

Il tuo compito è costruire un **dispositivo completo di lettura configurazionale** per un nuovo tema, utilizzando esclusivamente:

* la struttura del dispositivo validato di origine
* gli elementi adattati e stabilizzati negli step precedenti

Non è ammessa innovazione libera:
👉 ogni elemento deve essere **derivato, adattato o integrato**.

---

## 🎯 OBIETTIVO

Costruire un dispositivo completo che sia:

* strutturalmente coerente
* operativamente utilizzabile
* epistemicamente controllato (no inferenze, no circolarità)
* auto-limitante (produce *non_classificabile* quando necessario)

---

## 📥 INPUT

```json
{
  "source_device": "... dispositivo validato (STEP 3 corretto)",
  "new_corporeity": "... STEP 8",
  "new_bridge": "... STEP 8",
  "new_proxy": "... STEP 8 v2",
  "observability_requirements": "... STEP 8",
  "non_classifiability_rules": "... STEP 8"
}
```

---

## ⚙️ ISTRUZIONI

Costruisci il nuovo dispositivo mantenendo **esattamente la stessa architettura** del dispositivo sorgente, adattando solo dove necessario.

---

# 🧱 STRUTTURA OUTPUT

---

## 1. IDENTITÀ DEL DISPOSITIVO

* `device_id`
* `theme_id`
* `domain`
* `device_type`
* `function`

👉 La funzione deve esplicitare:

* cosa rende leggibile
* quale “cieco clinico” colma
* come cambia la domanda clinica

---

## 2. STRUTTURA DI RIFERIMENTO

* core_configuration (adattata al nuovo tema)
* assi (invariati)
* nodi (con adattamenti solo dove necessario)
* bridge_concept (nuovo)

---

## 3. READING FOCUS (DIMENSIONI)

Costruisci le 4 dimensioni:

### 3.1 Base corporea

→ usa **new_corporeity**

### 3.2 Campo intenzionale

→ trasferisci struttura a 4 stati

### 3.3 Co-regolazione

→ trasferisci struttura a 5 livelli

### 3.4 Mediazione simbolica

→ adatta al nuovo tema

### 3.5 Struttura del passaggio trasformativo

→ integra:

* new_bridge
* new_proxy (v2)

⚠️ Vincolo forte:

* la dimensione deve essere leggibile **senza usare il proxy**
* il proxy serve solo per classificare il bridge

---

## 4. ACCESS POINTS

Definisci contesti osservativi specifici per il nuovo tema:

* interazione spontanea
* momento di difficoltà reale
* richiesta di aiuto indotta
* colloquio caregiver

Per ciascuno:

* cosa rende osservabile
* dove può fallire

---

## 5. STRUCTURAL QUESTIONS

Genera domande che:

* attivano la lettura configurazionale
* non riducono a comportamento
* non introducono normatività

👉 includi:

* lettura episodio
* lettura multi-livello (con vincolo di freeze)

---

## 6. PROXY OPERATIVO

Integra formalmente il proxy v2:

```json
{
  "proxy_name": "...",
  "what_it_measures": "...",
  "required_observations": [...],
  "decision_logic": "...",
  "allowed_outputs": ["aperto", "predeterminato", "non_classificabile", "ambiguo"],
  "epistemic_limit": "..."
}
```

⚠️ Deve essere:

* non circolare
* ancorato a osservabili
* indipendente dalla classificazione

---

## 7. REQUISITI DI OSSERVABILITÀ

Formalizza:

* obs_1, obs_2, obs_3...
* tipo (diretto / con mediazione)
* observer_dependency

👉 evidenzia:

* finestra pre-risposta (centrale)
* limiti delle descrizioni testuali

---

## 8. REGOLE DI NON CLASSIFICABILITÀ

Integra e struttura:

* non_classificabile (dato assente)
* ambiguo (dato presente ma non discriminante)

⚠️ distinzione obbligatoria

---

## 9. INTERPRETIVE WARNINGS

Devi includere:

* comportamentismo
* normatività (rafforzata per questo tema)
* tecnicismo
* riduzione cognitiva
* tecnicismo riabilitativo (specifico richiesta di aiuto)

---

## 10. NON PERMITTED TRANSFORMATIONS

Esplicita chiaramente che NON può essere usato per:

* diagnosi
* valutazione competenze
* training comportamentale
* giudizio sul caregiver

---

## 11. VALIDAZIONE STRUTTURALE

Checklist finale obbligatoria:

```json
{
  "configurational_logic_preserved": true/false,
  "no_psychological_inference": true/false,
  "no_circularity": true/false,
  "proxy_observable": true/false,
  "self_limiting": true/false
}
```

---

# ⚠️ VINCOLI CRITICI

---

## ❗ 1. NO INFERENZE

Non usare:

* intenzioni
* stati mentali
* “il bambino vuole”
* “l’adulto capisce”

Solo struttura osservabile.

---

## ❗ 2. NO NORMATIVITÀ

Non introdurre:

* adeguato/inadeguato
* migliore/peggiore
* autonomia/dipendenza come giudizio

---

## ❗ 3. NO PROTOCOLLO

Non trasformare il dispositivo in:

* checklist
* scoring
* sequenza operativa

---

## ❗ 4. AUTO-LIMITAZIONE

Il dispositivo deve:

> **smettere di funzionare quando i dati non ci sono**

---

# OUTPUT

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-9-dispositivo-completo\complete-device-schema.json`

### Salvataggio
- **Nome file**: `dispositivo-{tema-target}-{domain}-v1.json` (es. `dispositivo-richiesta-aiuto-clinico-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-nuovo-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

---

# 🔚 Nota finale (importante)

Se vuoi un feedback onesto:
questo STEP 9 è il vero “punto di verità” del metodo.

* Se il dispositivo regge → il metodo è trasferibile
* Se collassa → significa che la stabilizzazione non era reale
