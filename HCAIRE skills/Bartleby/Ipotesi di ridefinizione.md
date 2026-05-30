# Bartleby — Ipotesi di ridefinizione

> **Statuto.** Documento di indirizzo: un'**ipotesi strategica** per riprendere lo strumento Bartleby, rimasto in sospeso. Contiene una diagnosi dello stato attuale e una ridefinizione del ruolo e dell'architettura concettuale. **Non** contiene roadmap, fasi di sviluppo o specifica tecnica: si ferma al livello concettuale, come punto di partenza per le decisioni successive.
>
> **Data**: 2026-05-24 · **Oggetto**: `HCAIRE skills/Bartleby/` · **Contesto**: ripresa dopo il completamento della pipeline di produzione "Produzioni" (F2/F3/F3-SIT) del progetto Sviluppo Bambino.

---

## 1. Perché ridefinire Bartleby ora

Bartleby è stato abbozzato come il sistema applicativo che trasforma i contenuti fondativi di HCAIRE in output, a partire da una traccia fornita dall'utente. L'idea originaria era netta: dalla semplice indicazione di una traccia, il sistema avrebbe dovuto *individuare le skill di indagine e di scrittura pertinenti* e con esse *produrre l'output*.

Da allora il progetto HCAIRE ha sviluppato, su un altro fronte, la pipeline di produzione "Produzioni": un percorso semi-automatico e verificato che costruisce dispositivi di lettura configurazionale e strumenti operativi contestualizzati. Quel lavoro ha prodotto qualcosa che Bartleby, nel suo abbozzo, non aveva: una grammatica strutturale matura e disciplinata.

Riprendere Bartleby oggi non significa continuarlo dov'era rimasto, ma **riposizionarlo** alla luce di questa maturazione. Due rischi vanno evitati. Il primo è che Bartleby resti un sistema concettualmente più povero e parallelo, con una propria grammatica che lentamente diverge da quella della pipeline. Il secondo, opposto, è che Bartleby venga assorbito nella pipeline e perda la propria ragione d'essere — che è diversa e legittima. Questa ipotesi cerca la terza via: Bartleby **autonomo nel funzionamento, allineato nel fondamento**.

---

## 2. Diagnosi dello stato attuale

### 2.1 Cosa esiste

L'abbozzo di Bartleby è oggi stratificato in tre livelli, prodotti in momenti diversi e non del tutto coerenti tra loro.

Il primo è un **abbozzo concettuale**: `Modello app.md` e `Modello dati.md` descrivono un'architettura reticolare con quattordici entità, tre famiglie di dati (fondativi, di esecuzione, di governance) e un modello relazionale a grafo. È un'analisi lucida, ma redatta in forma esplorativa e discorsiva, non ancora normativa.

Il secondo è un **dataset seed**: tredici file JSON in `Bartleby/data/`, 302 record, che popolano la base di conoscenza (documenti fondativi, nodi concettuali, ambiti, schede di ambito, skill, template di output) più tracce di esempio e ponti relazionali. È materiale solido e validato.

Il terzo è un **prototipo funzionante a trigger**: il `CLAUDE.md` di root, attivato dal file `input_bartleby.md`, esegue il Motore di Traducibilità nei suoi sei moduli A–F e produce un output JSON. Le due simulazioni eseguite (T-G03, T-PI01; valutazioni 7,5 e 8 su 10) mostrano che il metodo, quando gira, produce davvero output non riduttivi.

### 2.2 Cosa funziona

Tre elementi sono solidi e vanno conservati. Il **fondamento** — Carta fondativa, Motore di traducibilità, Atlante dei nodi trasversali — è coerente e ben costruito. Il **principio di trasparenza** — l'idea che ogni output esponga la propria genealogia ("questo documento è stato generato usando…") — è il tratto più distintivo del progetto e non va perso. E il **prototipo dimostra la tesi di fondo**: una procedura di lettura strutturata, interposta tra la traccia e il testo, produce un output qualitativamente diverso da una risposta diretta.

### 2.3 Cosa è incompleto o critico

Cinque punti meritano attenzione, perché sono esattamente ciò che la ridefinizione deve affrontare.

**Le skill non sono ancora ciò che il modello dichiara.** Il `Modello app.md` insiste su un punto: «non modellare le skill come semplici prompt testuali sparsi». Ma nei fatti le skill di fondamento *sono* documenti markdown discorsivi, e il Motore A–F è un prompt monolitico nel `CLAUDE.md` di root. La skill, che dovrebbe essere l'oggetto centrale e composabile del sistema, è oggi un testo. C'è uno scarto tra l'ambizione dichiarata e la realtà dell'abbozzo.

**La distinzione indagine / scrittura è andata perduta.** L'intenzione originaria — individuare skill di indagine e skill di scrittura — non è formalizzata da nessuna parte. Il Motore di Traducibilità concentra in un unico processo lineare sia la lettura della traccia sia la produzione del testo. Le due operazioni, di natura diversa, non sono separate né rese governabili distintamente.

**La tassonomia delle skill è dichiarata ma non istanziata.** Il modello dati prevede cinque tipi di skill (fondativa, di ambito, di nodo, di personalizzazione, di output), ma il seed contiene solo le prime due. "Di nodo", "di output" e "di personalizzazione" sono caselle vuote. Il sistema, allo stato, non sa fare ciò che la sua stessa tassonomia promette.

**Il prototipo e il seed divergono già.** Il `CLAUDE.md` di root elenca cinque valori ammessi per il tipo di output (`guida-genitoriale`, `policy-brief`, `nota-clinico-riflessiva`, `risposta-istituzionale`, `report-educativo`); il file `output_templates.json` ne contiene sette, in parte diversi (`guida-educativa`, `griglia-osservazionale`, `analisi-di-caso`, `articolo-riflessione`). Il prototipo hard-codifica liste che dovrebbero vivere nei dati. È un piccolo sintomo di un problema più generale: la logica è incollata nel prompt invece di essere letta dalla base di conoscenza.

**La grammatica di Bartleby diverge da quella della pipeline.** Bartleby ha dieci nodi concettuali (l'Atlante) e sei assi (le skill di fondamento). La pipeline Produzioni, nel frattempo, ha consolidato un proprio apparato: Nodi Trasversali canonici, Configurazioni Evolutive, dimensioni e tipologie formalizzate. I due sistemi nascono dallo stesso fondamento ma usano enumerazioni e lessici diversi. Finché restano scollegati, lo stesso progetto HCAIRE parla due lingue.

---

## 3. Ridefinizione del ruolo di Bartleby

### 3.1 Due motori, un fondamento

Bartleby e la pipeline Produzioni non sono lo stesso strumento e non vanno fusi. Hanno tempi, granularità e prodotti diversi.

La pipeline **produce strumenti**: a partire da un tema e da un dominio, costruisce — lentamente, in più passi, con verifica umana — dispositivi e strumenti contestualizzati riusabili. È produzione editoriale interna; il suo esito è un patrimonio stabile.

Bartleby **genera output**: a partire da una traccia libera dell'utente, produce — rapidamente, su singola richiesta — un testo significativo per quella situazione. È il punto di contatto diretto tra l'utente e il modello; il suo esito è un documento per un caso.

La pipeline lavora *per tipi* (un tema vale per molti casi); Bartleby lavora *per istanze* (una traccia, un caso). La pipeline è lenta e verificata; Bartleby è veloce e si autovaluta. Sono due motori distinti. Ma poggiano sullo stesso fondamento: la Carta fondativa, gli assi, i nodi trasversali sono patrimonio di HCAIRE, non di uno dei due sistemi. **Un fondamento, due motori**: è questa la formula della ridefinizione.

### 3.2 Autonomia operativa, allineamento concettuale

Bartleby resta **autonomo nel funzionamento**. Mantiene la propria base di conoscenza, il proprio modello dati, il proprio motore. Non dipende, a runtime, dai prodotti della pipeline: non li consuma, non li attende, non si ferma se mancano. Un utente può sottoporre una traccia su un tema che la pipeline non ha mai trattato, e Bartleby deve poter rispondere lo stesso, attingendo al solo fondamento. Questa autonomia è una qualità, non un limite: è ciò che rende Bartleby il volto reattivo del modello.

Ma Bartleby deve essere **allineato nel fondamento**. Allineamento non significa dipendenza: significa che le due grammatiche non possono contraddirsi. Un interlocutore scientifico, o un utente attento, che incontri sia un output di Bartleby sia uno strumento della pipeline non deve trovare due modelli HCAIRE diversi. L'allineamento è un requisito di coerenza del metodo, e si ottiene a livello del fondamento condiviso, non accoppiando i due sistemi. In concreto (§4.1) significa una sola enumerazione dei nodi trasversali e un lessico strutturale riconciliato — non una fusione delle pipeline.

---

## 4. Ridefinizione dell'architettura concettuale

### 4.1 Il fondamento unico e la riconciliazione delle grammatiche

Il primo atto della ridefinizione è riconoscere che il fondamento è uno solo. La Carta fondativa, i sei assi e i nodi trasversali non appartengono a Bartleby né alla pipeline: sono il patrimonio epistemico di HCAIRE, e i due motori lo *operazionalizzano* in modi diversi.

Da qui discende una correzione necessaria: la **doppia enumerazione dei nodi va risolta**. Oggi Bartleby ne ha dieci (l'Atlante), la pipeline ne ha un proprio insieme canonico. Non possono restare due liste diverse della stessa cosa. La riconciliazione non richiede di accoppiare i sistemi: richiede una decisione di fondamento — quale sia l'enumerazione canonica dei nodi trasversali di HCAIRE — e una **mappa di corrispondenza** che traduca l'una nell'altra dove le due restano operativamente distinte. Lo strumento esiste già in forma embrionale: `Mappa-corrispondenza-terminologica.md`. Va esteso fino a coprire esplicitamente la corrispondenza Bartleby ↔ pipeline. Lo stesso vale per termini che Bartleby usa in modo informale (per esempio "configurazione", "apertura/chiusura") e che nella pipeline hanno una definizione formale: vanno mappati, non lasciati a significare cose vicine ma non identiche.

### 4.2 La tassonomia delle skill, rivista

La skill è l'oggetto operativo di Bartleby. La tassonomia attuale (cinque tipi, due soli istanziati) va rivista per intero e resa coerente con il flusso reale del sistema. Si propongono **sei tipi di skill**, ciascuno con una funzione propria.

| Tipo di skill | Funzione | Origine |
|---|---|---|
| **di fondamento** | Codifica un asse del modello (Assi 1–6). È una lente di lettura sempre potenzialmente attiva, che orienta tutta l'interpretazione. | HCAIRE |
| **di nodo** | Codifica un nodo trasversale: come riconoscerlo in una traccia, come leggerlo, quali rischi di riduzione gli sono propri. Una per nodo. *Tipo oggi dichiarato ma vuoto.* | HCAIRE |
| **di ambito** | Codifica un dominio operativo: lessico, configurazioni tipiche, rischi di riduzione specifici, vincoli di linguaggio. Una per ambito. | HCAIRE |
| **di output** | Codifica un tipo di output: struttura attesa, vincoli di formato. Una per template. *Tipo oggi dichiarato ma vuoto.* | HCAIRE |
| **di personalizzazione** | Modula la scrittura secondo il profilo dell'utente: tono, livello tecnico, profondità, esplicitazione della teoria. | Utente |
| **di verifica** | Codifica il controllo di qualità: indicatori positivi e negativi, coerenza con il fondamento. Rende la verifica un oggetto, non un passaggio implicito nel prompt. *Tipo nuovo.* | HCAIRE |

Rispetto alla tassonomia attuale, la revisione conferma fondamento, nodo, ambito, output e personalizzazione; **aggiunge il tipo "di verifica"**, perché il controllo di qualità (il Modulo F del Motore) merita di essere una skill esplicita e non logica nascosta nel prompt; e soprattutto **chiede che i tipi oggi vuoti vengano istanziati**: senza skill di nodo e skill di output, il sistema non può selezionare e comporre nulla — può solo eseguire un prompt unico.

Un punto vale per tutti i tipi: una skill deve essere un **oggetto strutturato**, non un documento in prosa. I documenti markdown delle skill di fondamento sono la *fonte*; la skill operativa è ciò che se ne deriva — condizioni di attivazione, operatori di lettura, rischi, indicatori — in forma interrogabile (`instruction_payload` strutturato). È la condizione perché le skill siano selezionabili e componibili, che è esattamente ciò che il `Modello app.md` chiedeva e che l'abbozzo non ha ancora realizzato.

### 4.3 Indagine e scrittura: le due fasi del flusso

I sei tipi di skill classificano gli oggetti. Ma c'è una seconda classificazione, ortogonale, che riguarda il *momento del flusso* in cui una skill opera. È qui che rientra, riformulata, l'intuizione originaria delle "skill di indagine e di scrittura": non come due tipi, ma come due **fasi**.

Il flusso di Bartleby si articola in quattro momenti. Una **selezione** iniziale: dalla traccia si decide quali skill attivare — quali nodi sembrano in gioco, quale ambito, quale tipo di output. Una fase di **indagine**: le skill di fondamento, di nodo e di ambito leggono la traccia e producono un'interpretazione strutturata (la traccia riformulata, i nodi attivati, i rischi di riduzione rilevati). Una fase di **scrittura**: le skill di output e di personalizzazione traducono l'interpretazione in un testo per il destinatario. Una **verifica** finale: la skill di verifica controlla la coerenza dell'output con il fondamento.

Questo non sostituisce il Motore di Traducibilità: lo *rilegge*. I moduli A–D del Motore sono la fase di indagine; il modulo E è la scrittura; il modulo F è la verifica. La differenza rispetto all'abbozzo è che indagine e scrittura cessano di essere segmenti di un unico prompt e diventano fasi distinte, ciascuna servita da skill proprie e selezionate. Ogni skill, quindi, oltre al suo tipo (§4.2), porta un attributo di fase — *indagine*, *scrittura*, *verifica* o *trasversale* (le skill di fondamento, che orientano l'intero processo). Indagine e scrittura non sono l'ossatura unica della tassonomia: sono l'asse temporale lungo cui gli oggetti della tassonomia entrano in funzione.

Perché la separazione conta: un sistema che tiene distinte indagine e scrittura può sbagliare la scrittura senza aver sbagliato la lettura, e viceversa — e quindi può correggere l'una senza rifare l'altra. È la stessa ragione per cui la pipeline Produzioni separa i suoi step. Rende il sistema diagnosticabile.

### 4.4 Un corollario sulla trasparenza

La separazione in fasi rafforza il tratto più forte di Bartleby — l'esposizione della genealogia dell'output. Se indagine e scrittura sono distinte, il pannello "come è stato generato" può mostrare due cose diverse e ugualmente importanti: *come la traccia è stata letta* (quali nodi, quale ambito, quali rischi) e *come la lettura è stata tradotta in testo* (quale template, quale registro, quali personalizzazioni). La trasparenza smette di essere un elenco di oggetti usati e diventa il racconto di un percorso. È coerente con la stessa idea — maturata nella pipeline — che il valore non sta solo nell'output ma nella leggibilità del processo che lo ha prodotto.

---

## 5. Questioni aperte

La ridefinizione lascia aperte alcune decisioni, che vanno prese prima di qualunque sviluppo.

La prima riguardava l'**enumerazione canonica dei nodi trasversali**: i dieci dell'Atlante, l'insieme della pipeline, o un terzo insieme riconciliato. **Risolta (2026-05-24)**: il progetto ha adottato i 7 Nodi Trasversali canonici N1–N7 del fondamento ufficiale; l'Atlante è stato riscritto (v2.0) e i dati seed e i testi derivati migrati. Vedi `Migrazione-nodi-trasversali.md`.

La seconda riguarda il **rapporto tra prototipo e webapp**. Oggi coesistono un prototipo a trigger (`input_bartleby.md`) e un progetto di webapp (il modello dati, il seed). Vanno chiariti i ruoli: il prototipo come ambiente di sviluppo e collaudo del motore, la webapp come destinazione — oppure un'altra ipotesi. Finché i due convivono senza gerarchia, le incoerenze come quella tra le liste di output (§2.3) si moltiplicheranno.

La terza riguarda la **verifica umana**. La pipeline Produzioni ha verifiche umane in ogni passo; Bartleby, allo stato, si autovaluta soltanto (Modulo F). Va deciso se gli output di Bartleby debbano poter passare per una revisione umana prima di essere mostrati, almeno in alcuni casi — e questo si lega al modello di governance già previsto (`GovernanceDecision`, `OutputRevision`).

La quarta riguarda le **tracce che Bartleby non sa coprire bene**. Quando una traccia ricade su un fenomeno che il fondamento copre solo genericamente, Bartleby produce comunque un output, ma più debole. Quelle tracce sono un'informazione preziosa: sono candidati naturali a diventare temi di lavoro. Anche restando i due motori autonomi, vale la pena decidere se e come Bartleby segnali le proprie lacune ricorrenti — non come dipendenza dalla pipeline, ma come contributo all'agenda di HCAIRE.

---

## 6. In sintesi

Bartleby va ripreso non come si era lasciato, ma riposizionato. Resta un motore **autonomo** di generazione di output su traccia, distinto dalla pipeline Produzioni per tempo, granularità e prodotto. Ma va **allineato** a essa nel fondamento: un solo apparato di nodi trasversali, un lessico strutturale riconciliato. La sua architettura concettuale va rifondata su tre correzioni: la skill come oggetto strutturato e componibile, non come prompt; una tassonomia delle skill rivista e finalmente completa nei suoi sei tipi; la separazione esplicita tra la fase di indagine e la fase di scrittura — che recupera, in forma più rigorosa, l'intuizione originaria del progetto. Su questa base si potrà poi decidere il percorso di sviluppo, che questo documento, per scelta, non anticipa.

---

*Fine documento — ipotesi di ridefinizione di Bartleby, 2026-05-24.*
