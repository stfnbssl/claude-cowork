# OUTPUT BARTLEBY — FONDAMENTI E SCELTE

*Versione 1.0 · Prodotta: 2026-05-25*

> **Scopo.** Documentare le basi fondative e le scelte di progetto che stanno dietro a `Bartleby/data/output_templates.json` (i 7 template canonici di output) e a `Bartleby/data/output_documents.json` (le simulazioni che dimostrano il funzionamento del motore). Risponde alla domanda «perché questi output e non altri, in questa forma e con questi vincoli».
>
> **Riferimenti canonici.** `04 Memorie di contesto fondamentali/Metodo-fasi-concetti.md` (Fase 2 §3, operatore «Famiglie di output»); `Documenti fondativi/Pipeline di traducibilità (canonica).md`; `Documenti fondativi/Carta fondativa.md`. **Riferimenti operativi.** `Bartleby/Motore di lettura della traccia.md`; `Schede di ambito/` v2.0; `Documenti fondativi/Atlante nodi trasversali.md` v2.0.

---

## 1. Cos'è un output Bartleby

Questo documento riguarda specificamente gli output prodotti da **Bartleby**. Il progetto HCAIRE ha altri tipi di output a livelli diversi — gli strumenti contestualizzati della Pipeline canonica (Fase 2–3), i micro-materiali situazionali del modulo F3-SIT della pipeline Produzioni — che hanno propri fondamenti e proprie scelte (vedi §9).

Un output Bartleby non è un «testo prodotto a partire da una traccia». È il **passaggio finale del Motore di lettura della traccia**, che traduce una **struttura interpretativa intermedia** — la lettura ricondotta a nodi, assi, contesto e configurazione — in un testo che rende leggibile *quella lettura* a un destinatario specifico. Il distintivo, rispetto a un testo qualsiasi prodotto su una domanda, è triplice:

- è **subordinato al fondamento** (Carta + Atlante v2.0): rispetta i divieti metodologici (non diagnosticare, non rassicurare in modo vuoto, non prescrivere in modo rigido);
- è **non riducibile alla risposta standard** che la traccia rischierebbe di evocare (rassicurazione banale, allarmismo, neuroriduzionismo, economicismo, ecc.);
- è **genealogicamente trasparente**: porta con sé i campi che mostrano *come è stato letto* (`activated_nodes`, `activated_axes`, `skills_used`). La trasparenza non è ornamento: è il tratto distintivo del sistema.

Il body dell'output è testo fluente per il destinatario; la genealogia è esposta come metadato strutturato dell'OutputDocument.

---

## 2. Le sette tipologie canoniche — e perché sette

I 7 `output_template` di `output_templates.json` non sono un elenco arbitrario: rispondono a una logica precisa, che attraversa due assi.

**Primo asse — il destinatario** (mappato sui 4 contesti canonici). Per ciascun contesto serve almeno un template che parli con il suo linguaggio:

| Contesto canonico | Template dedicato |
|---|---|
| Genitoriale (`da-001`) | `guida-genitoriale` |
| Clinico (`da-002`) | `nota-clinico-riflessiva` |
| Pedagogico (`da-003`) | `guida-educativa` |
| Istituzionale/servizi (`da-004`) | `policy-brief` |

Quattro contesti, quattro template dedicati: la copertura del livello «un testo per quel destinatario» è completa.

**Secondo asse — la funzione del testo.** I rimanenti tre template coprono *funzioni operative* che attraversano più contesti:

| Funzione | Template | Contesti applicabili |
|---|---|---|
| Strumento di osservazione strutturato | `griglia-osservazionale` | Clinico + Pedagogico |
| Lettura sistemica integrata di un caso | `analisi-di-caso` | Clinico + Istituzionale/servizi |
| Riflessione di servizio per un pubblico professionale allargato | `articolo-riflessione` | tutti e quattro i contesti |

Le `applicable_areas` di ciascun template (campo del JSON) codificano esattamente questa logica: monocontesto per i quattro destinatari principali; trasversale per le tre funzioni operative.

**Numero non arbitrario.** Sette = 4 (destinatari) + 3 (funzioni trasversali). Aggiungere un template significa o un nuovo contesto canonico (cosa che impone una decisione di livello fondativo, fuori scope di un template), o una nuova funzione operativa non riducibile alle tre esistenti. Togliere un template significa rinunciare a un destinatario o a una funzione: anche questa è una decisione di livello superiore.

---

## 3. Mappatura sulle «famiglie di output» canoniche

La Pipeline di traducibilità canonica (Fase 2, operatore 6) identifica quattro **famiglie di output**: *osservativi*, *formativi*, *accompagnamento*, *ricerca*. I sette template di Bartleby si distribuiscono coerentemente:

| Famiglia canonica | Template Bartleby |
|---|---|
| Osservativi | `griglia-osservazionale` |
| Formativi | `guida-educativa`, `articolo-riflessione` |
| Accompagnamento | `guida-genitoriale`, `nota-clinico-riflessiva` |
| Ricerca / Policy | `analisi-di-caso`, `policy-brief` |

Bartleby non opera *sulla* Pipeline canonica (la Pipeline produce strumenti dal modello; Bartleby produce output da tracce — cfr. `Pipeline di traducibilità (canonica).md` §4), ma riconosce le sue famiglie come spazio strutturale dove collocare i propri template. La mappatura è leggibilità del sistema, non vincolo operativo.

---

## 4. Struttura canonica di un OutputDocument

Ogni output prodotto è un record con quattro famiglie di campi.

### 4.1 Identità

- `id` — identificativo univoco (es. `od-001`).
- `input_trace_id` — la traccia da cui l'output discende.
- `output_type` — uno dei 7 valori canonici (vedi §2).
- `audience` — uno dei 4 valori 1:1 con i contesti: `genitore` / `clinico` / `educatore` / `decisore-istituzionale`.
- `area_id` — uno dei 4 contesti canonici (`da-001`…`da-004`).
- `title` — titolo del documento.

### 4.2 Contenuto

- `body` — testo completo in Markdown. **Deve essere fluente** (non un elenco di moduli del Motore). Lunghezza orientativa secondo il template (vedi §6).
- `body_summary` — riassunto operativo in 2-3 frasi (max ~300 caratteri).
- `file_path` — opzionale; quando il body è grande o lavorato in markdown esterno, può vivere in un file (es. le due simulazioni in `Simulazioni/`).

### 4.3 Genealogia (vincolo distintivo)

Non opzionali. Sono i campi che fanno di un output Bartleby qualcosa di diverso da un testo qualsiasi:

- `activated_nodes` — i Nodi Trasversali canonici (`N1`…`N7`) attivati dalla traccia.
- `activated_axes` — gli Assi salienti (`A1`…`A6`), distinti dai nodi. Aggiunto con la migrazione v2.0 per concretizzare la distinzione assi/nodi nel dato di runtime. È vuoto se nessun asse è particolarmente saliente.
- `skills_used` — le skill effettivamente usate (`sk-001`…`sk-010`). Include le skill di fondamento attivate (gli assi), le skill di ambito del contesto, e le skill di personalizzazione utente se presenti.

La trasparenza che questi tre campi rendono possibile (il pannello «come è stato generato questo output» nella webapp Bartleby — `CLAUDE_webapp.md` §3) è il tratto distintivo del sistema. Senza genealogia, un output HCAIRE non è un output HCAIRE.

### 4.4 Governance

- `evaluation` — oggetto con `score` (0-10 o null), `notes` (punti di forza, limiti, riserve), `status` (`aperta a revisione`, `validata`, ecc.).
- `status` — stato editoriale dell'output (`bozza`, `revisionato`, `pubblicato`, `archiviato`).
- `version`, `created_at` — versionamento e tracciabilità.
- `generation_plan_id` — riferimento al piano di generazione (concettualmente; oggi `null` perché il motore opera senza un GenerationPlan esplicito materializzato).

---

## 5. I principi fondativi che ogni output deve rispettare

Sono gli invarianti, validi *trasversalmente* a tutti i 7 template. Codificati esplicitamente nel `CLAUDE.md` di root come «Principi da rispettare sempre» e ripresi nelle `language_constraints.negative` di ciascun template.

1. **Non diagnosticare** — non formulare etichette diagnostiche, anche se la traccia le sollecita.
2. **Non rassicurare in modo vuoto** — la rassicurazione che chiude la domanda è una forma di riduzione.
3. **Non prescrivere in modo rigido** — orientamento sì, prescrizione no.
4. **Soggetto incarnato in relazione** — il bambino è soggetto, non oggetto di valutazione.
5. **Profondità anche per il pubblico non specialistico** — semplificare senza banalizzare.
6. **Body fluente, non elenco di moduli** — il motore A–F è processo interno, non struttura del testo.
7. **Distinguere Assi e Nodi** — A1–A6 sono dimensioni strutturali permanenti; N1–N7 sono configurazioni multi-asse. Affettività, Corpo, Contesto storico-culturale sono Assi, non Nodi.
8. **Genealogia obbligatoria** — i tre campi della §4.3 non sono opzionali.

Questi otto principi sono il «livello di vincolo» più alto: in caso di conflitto fra template e principio, prevale il principio.

---

## 6. Le scelte dentro `structure_schema` e `language_constraints`

Per ogni template, tre blocchi di scelte. Le riprendiamo evidenziando *perché* sono fatte così.

### 6.1 `sections` — l'ossatura del testo

Le sezioni di ciascun template non sono titoli di paragrafo da copiare: sono i **passaggi argomentativi** che il body deve attraversare. Ad esempio per `guida-genitoriale`:

> lettura del comportamento o della situazione (senza categorizzare) → cosa può significare dal punto di vista dello sviluppo → come orientarsi nella quotidianità (strumenti osservativi) → quando è utile un approfondimento professionale.

Il senso editoriale: aprire dalla situazione (non da una categoria), articolare il significato evolutivo, dare strumenti osservativi (non istruzioni), chiudere indicando quando è opportuno un approfondimento (apertura, non chiusura).

La logica è analoga per gli altri sei template: la sequenza di sezioni codifica una **forma argomentativa** coerente con il contesto.

### 6.2 `length` e `tone`

La lunghezza è un'indicazione operativa, calibrata sul livello di approfondimento atteso:

- testi brevi-medi (600-1200 parole): `nota-clinico-riflessiva`, `policy-brief` — destinatari professionali che lavorano in tempi serrati;
- testi medi (800-1500 parole): `guida-genitoriale`, `guida-educativa` — destinatari che hanno bisogno di una lettura sufficientemente articolata;
- testi medio-lunghi (1000-2000 parole): `analisi-di-caso`, `articolo-riflessione` — quando l'oggetto richiede sviluppo;
- griglia con sezione note (200-500 parole): `griglia-osservazionale` — strumento, non testo.

Il `tone` è la traduzione del linguaggio del contesto (cfr. §10 di ciascuna scheda di ambito) nel template.

### 6.3 `language_constraints` — il livello operativo dei divieti

Ogni template ha due liste: `positive` (cosa fare) e `negative` (cosa evitare). I `negative` sono la traduzione **operativa** dei principi fondativi della §5 nel registro del template:

- in `guida-genitoriale`: «tecnicismi clinici», «tono colpevolizzante», «rassicurazioni vuote», «prescrizioni rigide», «confronti normativi decontestualizzati»;
- in `nota-clinico-riflessiva`: «diagnosi implicite o prematuri», «tono allarmistico», «causalità lineare», «medicalizzazione precoce», «separazione del bambino dal suo contesto»;
- in `policy-brief`: «over-promise», «neuroriduzionismo come unico argomento», «economicismo esclusivo (bambino come ROI futuro)», «perdita del soggetto», «vaghezza non traducibile»;
- e così via per gli altri quattro.

Sono i **bordi negativi** che impediscono al template di deviare verso la forma standard non-HCAIRE che il contesto naturalmente solleciterebbe. Per questo sono enumerati con cura: non sono indicazioni di stile, sono presidi del modello.

I `positive` non sono il complemento dei `negative`: sono le qualità che caratterizzano un output ben riuscito in quel template (es. nel policy-brief la combinazione «argomento fondativo + equità + economico»; nella nota clinico-riflessiva la «distinzione esplicita dato/interpretazione/ipotesi»).

---

## 7. Le simulazioni — statuto e ruolo

`output_documents.json` contiene oggi due simulazioni — `od-001` (T-G03, guida-genitoriale) e `od-002` (T-PI01, policy-brief). Non sono «esempi» nel senso generico: hanno uno statuto preciso.

**Sono prove operative del motore.** Ciascuna è la dimostrazione che, su una traccia reale del corpus, il motore produce un output qualitativamente diverso dalle risposte standard che la traccia sollecita. Il `body_summary` di entrambe rende esplicito il contrasto: per T-G03, contro rassicurazione (tipo A) e allarmismo diagnostico (tipo B); per T-PI01, contro neuroriduzionismo (tipo A), economicismo (tipo B), genericismo antropologico (tipo C). La simulazione vale in quanto **distinguibile** dalla risposta standard.

**Sono validate e riusabili.** Hanno `status: "revisionato"` (sono state riviste) e `evaluation` con `notes` esplicite. La T-PI01 ha un punteggio 8/10 e nota un punto debole (mancanza di contestualizzazione locale); la T-G03 ha auto-valutazione qualitativa positiva con riserva (più strumenti osservativi pratici). Entrambe sono `aperta a revisione`: il sistema le tratta come *output validi e perfettibili*, non come modelli rigidi.

**Body esterno.** Per scelta editoriale, il `body` Markdown vive in `Simulazioni/Simulazione-*.md` (campo `file_path`), non dentro il JSON. È una conseguenza pragmatica della lunghezza dei body e della loro lavorabilità in editor markdown.

**Cosa rappresentano i due output insieme.** Coprono i due estremi operativi della gamma di Bartleby: il caso quotidiano-genitoriale (con un bambino reale come soggetto, una madre come destinataria della guida) e il caso istituzionale-strategico (un Comune, una decisione di policy, un argomento da costruire). Tra questi due estremi vivono tutte le altre tipologie. Le due simulazioni sono il test del fatto che il sistema regge agli estremi.

---

## 8. Il sistema di valutazione

Lo `score` (0-10) e le `notes` non sono punteggi accademici: sono **auto-valutazione del motore** (Modulo F del Motore di lettura), confermata o corretta dalla revisione editoriale. Le scelte fondative:

- **scala 0-10**: discreta, leggibile, comparabile fra output diversi;
- **`null` ammesso**: quando lo score numerico non è significativo si esprime la valutazione solo in `notes` (è il caso di T-G03);
- **`notes` come parte integrante**: il punteggio da solo è muto; la nota esplicita punti di forza, limiti, riserve;
- **`status: "aperta a revisione"`** come default per le simulazioni: nessun output è chiuso definitivamente; la revisione editoriale può tornarvi.

---

## 9. Relazione con altri livelli di output del progetto HCAIRE

I 7 output_type di Bartleby sono **output a livello di documento**: un testo intero per un destinatario. Non vanno confusi con due altri livelli, presenti altrove nel progetto HCAIRE:

- **Le famiglie di output della Pipeline canonica** (Fase 2, operatore 6): osservativi/formativi/accompagnamento/ricerca. Sono **classi strutturali** che la Pipeline canonica considera; i 7 template di Bartleby vi si mappano (§3).
- **Le 9 famiglie F3-SIT del modulo situazionale** della pipeline Produzioni (Sviluppo Bambino): casistiche situazionali, frasi per operatori, frasi per caregiver, schede di atteggiamento, micro-scenari, vignette formative, storyboard, linee guida narrative, prompt per AI generativa. Sono **micro-materiali situazionali** — unità interne di un output, non output autonomi. Possono entrare *dentro* un output Bartleby (es. una frase per caregiver dentro una guida-genitoriale), ma non lo sostituiscono.

Bartleby produce documenti; F3-SIT produce micro-materiali; la Pipeline canonica produce strumenti. Tre livelli distinti, articolati attorno allo stesso fondamento.

---

## 10. Aperture e questioni di sviluppo

Quattro punti meritano una riflessione prima di un'eventuale revisione futura dei template.

1. **`articolo-riflessione` è il template più ampio** (4 contesti applicabili). Funziona bene come «testo riflessivo trasversale», ma per scelte editoriali specifiche (es. articoli orientati al clinico vs articoli per il sociale) potrebbe richiedere una *variante per contesto* o restare l'unico template generalista con calibrazione del tono per ambito. Decisione editoriale, non strutturale.

2. **Versionamento dei template.** Oggi tutti i 7 sono `v1.0`. Quando un template viene rivisto (sezioni, lunghezza, vincoli), serve un versionamento esplicito e una compatibilità con gli output già prodotti.

3. **Templates personalizzati / di personalizzazione utente.** Il modello prevede `UserCustomizationProfile` per modulare tono, profondità, esplicitazione teorica. Oggi non c'è ancora un meccanismo che istanzi un template come *variante* di un canonico per un utente specifico. Lo si potrà introdurre quando ci saranno utenti reali.

4. **Output `articolo-riflessione` ↔ `analisi-di-caso`.** I due template di media-lunghezza più simili. Distinzione: l'analisi di caso parte da una situazione concreta e produce lettura sistemica; l'articolo di riflessione parte da un tema e produce una riflessione situata. La distinzione è chiara nei `sections` di ciascuno e nelle `applicable_areas`, ma va presidiata editorialmente per evitare drift.

---

## 11. Sintesi

I 7 template di output di Bartleby non sono un elenco di tipi: sono una **mappa strutturale** che incrocia destinatari (4 contesti) e funzioni (3 operazioni trasversali). Le scelte dentro ogni template (`sections`, `length`, `tone`, `language_constraints`) traducono in vincoli operativi gli otto principi fondativi del modello HCAIRE. La genealogia (`activated_nodes`, `activated_axes`, `skills_used`) è il tratto distintivo non opzionale che separa un output Bartleby da un testo qualsiasi. Le due simulazioni in `output_documents.json` sono prove operative agli estremi della gamma (quotidiano-genitoriale, istituzionale-strategico) e dimostrano che il sistema regge.

Questo è ciò che il seed `output_templates.json` codifica, e che `output_documents.json` esemplifica: la forma canonica entro cui Bartleby produce testi che restano coerenti con il fondamento.

---

*Output Bartleby — fondamenti e scelte — 2026-05-25.*
