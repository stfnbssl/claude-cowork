# Specifiche delle schede-concetti

**Progetto:** Sviluppo Bambino — laboratorio HCAIRE  
**Versione:** 2.0  
**Data:** 2026-05-13  
**Stato:** definitivo

---

## 1. Scopo del documento

Questo file descrive i criteri adottati per la strutturazione delle schede-concetti in `output/schede-concetti/` e costituisce la legenda di riferimento per il campo `related:` del front matter YAML.

Serve a quattro scopi:

1. Garantire coerenza tra tutte le schede, anche quando vengono redatte o modificate in momenti diversi.
2. Fornire la documentazione necessaria per trasformare le schede in un grafo (Neo4J, JSON statico, o altro) senza doverle reinterpretare.
3. Rendere esplicite le scelte che altrimenti resterebbero implicite nel testo delle schede.
4. Guidare la manutenzione del grafo quando le schede vengono create, modificate o rimosse.

### Stato attuale del corpus

| Indicatore | Valore |
|---|---|
| Schede totali | 50 |
| Schede con campo `related` | 50 (100%) |
| Relazioni totali annotate | 215 |
| Tipi di relazione usati | 14 (su 15 canonici) |
| Tipi non canonici residui | 0 |

---

## 2. Struttura del front matter

Ogni scheda-concetto è un file Markdown con front matter YAML nella seguente forma:

```yaml
---
id:               # slug univoco in kebab-case, es. concetto-ponte
titolo:           # titolo leggibile del concetto
alias: []         # sinonimi e abbreviazioni in uso nel progetto
area:             # area tematica (vocabolario controllato, vedi § 3)
fase_principale:  # fase metodologica di appartenenza primaria (F1–F7 o "trasversale")
stato:            # bozza | in-revisione | finale
related:          # elenco delle relazioni strutturate (vedi § 5)
  - id: …
    rel: …
    dir: …
    obbligatoria: …
    nota: "…"
---
```

### Campi obbligatori

| Campo | Tipo | Note |
|---|---|---|
| `id` | stringa kebab-case | univoco nell'intero corpus |
| `titolo` | stringa | titolo leggibile, può differire dall'id |
| `alias` | lista di stringhe | può essere vuota `[]` |
| `area` | stringa (vocabolario controllato) | vedi § 3 |
| `stato` | stringa (vocabolario controllato) | `bozza` \| `in-revisione` \| `finale` |

### Campi raccomandati

| Campo | Tipo | Note |
|---|---|---|
| `fase_principale` | stringa | `F1`–`F7` oppure `trasversale` |
| `related` | lista di oggetti | obbligatorio per le schede centrali; può mancare nelle periferiche |

---

## 3. Vocabolario controllato: `area`

Il campo `area` classifica ogni concetto nell'area tematica in cui svolge la propria funzione primaria. Un concetto può essere rilevante per più aree, ma viene assegnato a una sola — quella in cui il suo statuto è fondativo.

| Valore | Descrizione |
|---|---|
| `fondamento` | Concetti della Fase 1 — presupposti ontologici e antropologici dello sviluppo |
| `metodo` | Principi e dispositivi metodologici trasversali (pipeline, traduzione, regolazione) |
| `configurazione` | Concetti relativi alla lettura e descrizione degli stati di sviluppo |
| `operativo` | Concetti relativi all'azione professionale nei contesti reali |
| `progetto` | Concetti che descrivono il progetto stesso come infrastruttura (statuto metateorico, sistema cognitivo di supporto) |

---

## 4. Vocabolario controllato: `fase_principale`

La fase principale indica dove il concetto viene introdotto o dove svolge la funzione più significativa. Non implica che sia usato esclusivamente in quella fase.

| Valore | Fase |
|---|---|
| `F1` | Fondazione ontologica |
| `F2` | Traduzione interdisciplinare |
| `F3` | Strumenti operativi |
| `F4` | Formazione e trasformazione sistemica |
| `F5` | Valutazione configurazionale |
| `F6` | Posizionamento e adozione istituzionale |
| `F7` | Architettura integrata |
| `trasversale` | Rilevante per più fasi senza appartenenza primaria |

---

## 5. Il campo `related`: struttura e legenda

### 5.1 Struttura di ogni voce

```yaml
related:
  - id: nome-scheda-correlata     # id della scheda correlata (deve corrispondere a un id esistente)
    rel: TIPO_RELAZIONE           # tipo di relazione (vocabolario canonico, vedi § 6)
    dir: source                   # direzione: source = questo nodo origina la relazione
                                  #            target = questo nodo riceve la relazione
    obbligatoria: true            # true = la relazione è costitutiva del concetto
                                  # false = la relazione è accessoria o contestuale
    nota: "spiegazione testuale"  # perché esiste questa relazione (in linguaggio naturale)
```

### 5.2 Il campo `dir`: come leggere la direzione

Il campo `dir` indica il ruolo di **questa scheda** nella relazione:

- `source` — questa scheda è il punto di partenza: *questa_scheda → REL → scheda_correlata*
- `target` — questa scheda è il punto di arrivo: *scheda_correlata → REL → questa_scheda*

**Esempio:** nella scheda `operatore-di-lettura`, la voce:
```yaml
  - id: configurazione-evolutiva
    rel: PRODUCE
    dir: source
```
si legge: *operatore-di-lettura → PRODUCE → configurazione-evolutiva*

Nella scheda `configurazione-evolutiva`, la stessa relazione appare come:
```yaml
  - id: operatore-di-lettura
    rel: PRODUCE
    dir: target
```
che si legge ugualmente: *operatore-di-lettura → PRODUCE → configurazione-evolutiva* (stessa freccia, vista dal lato opposto).

Questa ridondanza è intenzionale: permette di leggere tutte le relazioni di un concetto guardando solo la sua scheda.

### 5.3 Il campo `obbligatoria`

- `true` — la relazione è costitutiva: rimuoverla cambierebbe il significato del concetto o violerebbe la coerenza dell'architettura metodologica.
- `false` — la relazione è contestuale, comparativa o accessoria: utile per la navigazione, ma non indispensabile per la comprensione.

---

## 6. Vocabolario canonico delle relazioni

Le relazioni sono organizzate in cinque famiglie. Il corpus attuale usa 14 dei 15 tipi canonici definiti (TRADUCE_IN non è ancora usato; è riservato per future schede sui concetti-ponte disciplinari specifici).

### Famiglia A — SEQUENZA
*Ordine obbligatorio tra concetti. Non saltabile senza perdita di coerenza metodologica.*

| Tipo | Direzione | Significato |
|---|---|---|
| `PRECEDE_IN_PIPELINE` | source → target | Posizione ordinata nella pipeline di traducibilità |
| `PRECEDE_IN_CICLO` | source → target | Posizione ordinata nel ciclo decisionale |

### Famiglia B — FONDAZIONE
*Dipendenze logiche. Il concetto source è condizione di possibilità del concetto target.*

| Tipo | Direzione | Significato |
|---|---|---|
| `FONDA` | source → target | Condizione di possibilità logica: senza il source, il target non ha base concettuale |
| `HA_STATUTO` | source → target | Il source ha lo statuto ontologico definito dal target |

### Famiglia C — TRASFORMAZIONE
*Movimenti dal più astratto al più concreto, o da un livello all'altro del sistema.*

| Tipo | Direzione | Significato |
|---|---|---|
| `PRODUCE` | source → target | Il source genera il target come output diretto |
| `TRADUCE_IN` | source → target | Traduzione disciplinare controllata: il source mantiene la propria funzione strutturale cambiando linguaggio |
| `REALIZZA` | source → target | Il source è la realizzazione contestuale e situata del target (astratto → concreto) |
| `RENDE_OPERATIVO` | source → target | Il source porta il target dall'astratto all'operativo, rendendolo usabile in pratica |

### Famiglia D — COMPOSIZIONE E MEMBERSHIP
*Relazioni parte-tutto, appartenenza, istanziazione.*

| Tipo | Direzione | Significato |
|---|---|---|
| `COMPONE` | source → target | Il source è parte costitutiva del target |
| `ISTANZA_DI` | source → target | Il source è un caso particolare o esemplare del tipo generale target |

### Famiglia E — REGOLAZIONE
*Principi che governano processi, distinzioni, vincoli.*

| Tipo | Direzione | Significato |
|---|---|---|
| `GOVERNA` | source → target | Il source (principio o vincolo) regola il funzionamento del target |
| `DISTINGUE_DA` | source → target | Il source si distingue esplicitamente dal target per funzione o statuto metodologico. Relazione simmetrica: va dichiarata in entrambe le schede |
| `RISPONDE_A` | source → target | Il source risponde a un problema strutturale o a un rischio identificato dal target |

### Famiglia F — AZIONE
*Come e dove operano i dispositivi nel campo reale.*

| Tipo | Direzione | Significato |
|---|---|---|
| `AGISCE_SU` | source → target | Il source (dispositivo) opera direttamente sul target |
| `ORIENTA` | source → target | Il source guida il target senza prescriverlo: apre possibilità senza determinare l'azione |

---

## 7. Criteri di annotazione

### Quali relazioni includere

Includere una voce `related:` quando la relazione:

- è **costitutiva** del significato del concetto (obbligatoria: true), oppure
- è una **distinzione metodologica esplicita** nel testo della scheda, oppure
- è necessaria per ricostruire una **sequenza** (pipeline, ciclo decisionale).

Evitare di includere relazioni:

- già deducibili dal solo campo `area` o `fase_principale`,
- di pura co-presenza tematica senza funzione strutturale,
- già espresse dalla collocazione del concetto nell'architettura a fasi.

### Ridondanza controllata

La stessa relazione può apparire in entrambe le schede coinvolte, con `dir` opposto. Questa ridondanza è **raccomandata** per le relazioni obbligatorie e **facoltativa** per quelle accessorie (obbligatoria: false).

---

## 8. Tipi di relazione da non usare

I seguenti tipi erano stati usati in bozza e sono stati soppressi perché sostituiti. Usarli in nuove schede è un errore da correggere.

| Tipo soppresso | Sostituito da | Motivo |
|---|---|---|
| `PRECEDE_IN_CICLO_DECISIONALE` | `PRECEDE_IN_CICLO` | troppo verboso |
| `PRODOTTO_DA` | `PRODUCE` con `dir: target` | inverso esplicito inutile se si usa `dir` |
| `PRODOTTA_DA` | `PRODUCE` con `dir: target` | variante di genere da evitare |
| `GENERATO_DA` | `PRODUCE` con `dir: target` | sinonimo |
| `STATUTO_DI` | `HA_STATUTO` con `dir` appropriato | forma inversa non canonica |
| `RESO_OPERATIVO_DA` | `RENDE_OPERATIVO` con `dir: target` | inverso esplicito inutile |
| `OPERAZIONALIZZA` | `RENDE_OPERATIVO` | sinonimo |
| `OPERAZIONALIZZATO_IN` | `RENDE_OPERATIVO` con `dir: target` | inverso + sinonimo |
| `FORMALIZZATO_IN` | `RENDE_OPERATIVO` | sinonimo |
| `FORMALIZZATA_IN` | `RENDE_OPERATIVO` | variante di genere da evitare |
| `STRUMENTO_DI` | `RENDE_OPERATIVO` | sinonimo |
| `COMPOSTA_DA` | `COMPONE` con `dir: target` | inverso esplicito inutile |
| `COMPONENTE_DI` | `COMPONE` con `dir: target` | sinonimo dell'inverso |
| `APPARTIENE_A_PROCESSO` | `COMPONE` | sinonimo |
| `PROPRIETÀ_DI` | `COMPONE` con nota | relazione descritta meglio in prosa |
| `INCARNA` | `GOVERNA` con nota | troppo specifico e ambiguo |
| `PRECEDE` | `PRECEDE_IN_PIPELINE` o `PRECEDE_IN_CICLO` | troppo generico |
| `ASSUME_FORMA_DI` | `PRODUCE` con nota | sinonimo contestuale |
| `MISURA` | `PRODUCE` con nota | relazione descritta meglio in nota |
| `OGGETTO_DI` | `AGISCE_SU` o `ISTANZA_DI` | ambiguo |
| `UNITA_DI` | `COMPONE` con nota | troppo specifico |
| `DESCRIVE` | `ORIENTA` o `PRODUCE` con nota | ambiguo: la CE orienta/produce, non descrive in senso passivo |

---

## 9. Esempio completo di scheda annotata

```yaml
---
id: operatore-di-lettura
titolo: Operatore di lettura
alias: []
area: metodo
fase_principale: F2
stato: bozza
related:
  - id: domanda-professionale
    rel: PRECEDE_IN_PIPELINE
    dir: target
    obbligatoria: true
    nota: "quinto passaggio della pipeline di traducibilità"
  - id: famiglia-di-output
    rel: PRECEDE_IN_PIPELINE
    dir: source
    obbligatoria: true
    nota: "l'operatore produce la CE, che orienta le famiglie di output"
  - id: configurazione-evolutiva
    rel: PRODUCE
    dir: source
    obbligatoria: true
    nota: "l'operatore trasforma osservazioni in configurazioni evolutive"
  - id: lettura-configurazionale
    rel: DISTINGUE_DA
    dir: source
    obbligatoria: false
    nota: "strumento formalizzato vs competenza professionale acquisita"
  - id: separazione-tra-osservazione-e-decisione
    rel: GOVERNA
    dir: target
    obbligatoria: true
    nota: "l'operatore produce leggibilità, non azione: la decisione resta al professionista"
---
```

---

## 10. Procedure di manutenzione delle relazioni (CRUD)

Questa sezione descrive le operazioni da eseguire sul campo `related:` ogni volta che le schede vengono create, lette, modificate o eliminate.

---

### 10.1 CREATE — Aggiungere una nuova scheda

Quando si crea una nuova scheda, le relazioni vanno costruite in due passaggi:

**Passaggio 1 — Compilare il `related:` della nuova scheda**

Per ogni concetto del corpus con cui la nuova scheda ha una relazione strutturale:
1. Scegliere il tipo canonico corretto dalla tabella § 6.
2. Determinare `dir:` rispetto alla nuova scheda (source = la nuova scheda origina la relazione).
3. Valutare se la relazione è obbligatoria o accessoria.
4. Scrivere una `nota:` che motivi la relazione in linguaggio naturale.

**Passaggio 2 — Aggiornare le schede già esistenti correlate**

Per ogni relazione obbligatoria dichiarata nella nuova scheda, aggiungere la voce speculare (`dir` invertito) anche nella scheda correlata. Questo è il principio di ridondanza controllata.

Esempio: se la nuova scheda `X` dichiara `id: Y, rel: FONDA, dir: source` (X fonda Y), aggiungere in `Y.md` la voce `id: X, rel: FONDA, dir: target`.

**Checklist CREATE:**

- [ ] `id` univoco verificato (nessun'altra scheda con lo stesso slug)
- [ ] `area` e `fase_principale` assegnati dal vocabolario controllato
- [ ] `related:` compilato con almeno le relazioni obbligatorie
- [ ] Solo tipi canonici usati (nessun tipo dalla lista § 8)
- [ ] Schede correlate aggiornate con la voce speculare per le relazioni obbligatorie

---

### 10.2 READ — Navigare le relazioni

Il campo `related:` consente due tipi di navigazione:

**Navigazione diretta (relazioni in uscita dalla scheda corrente)**

Tutte le voci con `dir: source` sono relazioni che partono da questa scheda. Leggono come: *questa_scheda → REL → id_correlato*.

**Navigazione inversa (relazioni in entrata nella scheda corrente)**

Tutte le voci con `dir: target` sono relazioni che arrivano a questa scheda. Leggono come: *id_correlato → REL → questa_scheda*.

**Per ricostruire l'intero grafo di un concetto** basta leggere il suo `related:` senza cercare in altri file, grazie alla ridondanza controllata.

**Per rispondere a domande traversali** (es. "quali concetti precedono X nella pipeline?") cercare in tutto il corpus le voci `rel: PRECEDE_IN_PIPELINE, dir: source` che puntano a X — o, equivalentemente, cercare in X.md le voci `rel: PRECEDE_IN_PIPELINE, dir: target`.

---

### 10.3 UPDATE — Modificare una scheda esistente

Le modifiche si distinguono in tre categorie con impatti diversi sulle relazioni:

**A. Modifica del solo corpo testuale (non tocca il front matter)**

Nessuna azione richiesta sulle relazioni, salvo che il testo modificato non introduca o elimini relazioni strutturali esplicite. In quel caso aggiornare il `related:` di conseguenza.

**B. Modifica dei metadati di classificazione (`area`, `fase_principale`, `stato`, `alias`)**

Nessuna azione richiesta sulle relazioni. Questi campi non hanno effetti sul grafo.

**C. Modifica dell'`id` (rinominare una scheda)**

È l'operazione più delicata. Richiede di aggiornare **ogni voce `id:`** che punta alla scheda rinominata in tutto il corpus.

Procedura:
1. Rinominare il file (es. `vecchio-id.md` → `nuovo-id.md`).
2. Cambiare il campo `id:` nel front matter della scheda rinominata.
3. Cercare in tutti i file del corpus il valore `id: vecchio-id` all'interno di blocchi `related:`.
4. Sostituire con `id: nuovo-id` in ogni occorrenza trovata.

**D. Modifica del contenuto concettuale (il concetto cambia significato o funzione)**

Se il cambiamento modifica le relazioni strutturali:
1. Aggiornare le voci `related:` della scheda modificata.
2. Per ogni relazione rimossa che era obbligatoria, rimuovere la voce speculare dalla scheda correlata.
3. Per ogni relazione aggiunta che è obbligatoria, aggiungere la voce speculare nella scheda correlata.

**Checklist UPDATE:**

- [ ] Identificata la categoria della modifica (A, B, C o D)
- [ ] Se C: cercato e aggiornato `id: vecchio-id` in tutto il corpus
- [ ] Se D: `related:` della scheda aggiornato
- [ ] Se D: schede correlate aggiornate per le relazioni obbligatorie aggiunte o rimosse
- [ ] Nessun tipo non canonico introdotto

---

### 10.4 DELETE — Eliminare una scheda

Eliminare una scheda crea riferimenti pendenti (`dangling references`) in tutte le schede che la citano nel loro `related:`. Prima di eliminare:

**Passaggio 1 — Identificare tutte le schede che la citano**

Cercare nel corpus: `id: <slug-da-eliminare>` all'interno di blocchi `related:`. Questo restituisce la lista completa delle schede da aggiornare.

**Passaggio 2 — Valutare l'impatto**

Per ogni scheda che cita quella da eliminare, chiedersi:
- La relazione era obbligatoria? In quel caso eliminare la scheda può rompere la coerenza del modello. Valutare se sia più opportuno fare un `merge` (incorporare il contenuto in un'altra scheda) anziché una cancellazione secca.
- La relazione era accessoria? Può essere rimossa senza impatti sulla coerenza.

**Passaggio 3 — Aggiornare le schede correlate**

Rimuovere da ciascuna scheda identificata al passaggio 1 la voce `related:` che puntava alla scheda eliminata.

**Passaggio 4 — Eliminare il file**

Solo dopo aver completato i passaggi 1–3.

**Alternativa consigliata: deprecazione anziché cancellazione**

Invece di eliminare, cambiare `stato: deprecata` e aggiungere una nota nel corpo della scheda che indica a quale scheda il concetto è stato incorporato. Questo preserva la tracciabilità storica e non spezza i link esistenti finché il corpus non viene aggiornato sistematicamente.

**Checklist DELETE:**

- [ ] Identificate tutte le schede che citano questa scheda nel loro `related:`
- [ ] Valutato l'impatto per le relazioni obbligatorie
- [ ] Schede correlate aggiornate (voci `related:` rimosse)
- [ ] Considerata la deprecazione come alternativa alla cancellazione secca

---

## 11. Punti aperti

- [ ] Definire se `fase_principale` può avere valori multipli (es. `output-tipo-vuoto` appartiene sia a F1 che a F3). Soluzione provvisoria: usare il valore della fase in cui il concetto svolge la funzione più fondativa.
- [ ] Verificare sistematicamente la simmetria delle ridondanze per le relazioni obbligatorie (ogni relazione obbligatoria dovrebbe apparire in entrambe le schede coinvolte con `dir` opposto).
- [ ] Decidere se aggiungere `TRADUCE_IN` al corpus quando verranno create schede per i concetti-ponte disciplinari specifici (es. "regolazione in contesto clinico", "norma in contesto educativo").
