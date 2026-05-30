# Motore di lettura della traccia (Bartleby)

*Versione 2.0 · Operativo di Bartleby · 2026-05-25*

> **Statuto.** Documento operativo del motore di Bartleby. Sostituisce e ribattezza il precedente *Motore di traducibilità* (eliminato), che collideva nominalmente con la Pipeline di traducibilità canonica del fondamento ufficiale e ne descriveva un'operazione diversa.
>
> **Relazione con la Pipeline canonica.** Il motore di Bartleby **non è** la Pipeline di traducibilità canonica (Metodo-fasi-concetti, Fase 2). Sono due manufatti distinti: la Pipeline canonica processa il *modello* per produrre uno *strumento contestualizzato*; questo motore processa una *traccia dell'utente* per produrre un *output testuale*. Entrambi presuppongono lo stesso fondamento canonico (6 assi, 7 Nodi Trasversali N1–N7, 4 contesti). Cfr. `Documenti fondativi/Pipeline di traducibilità (canonica).md`.
>
> **Riferimenti.** `Documenti fondativi/Atlante nodi trasversali.md` v2.0; `Documenti fondativi/Carta fondativa.md`; `Schede di ambito/` v2.0; `Bartleby/Ipotesi di ridefinizione.md`.

---

## 1. Scopo

Trasformare una **traccia** dell'utente — una domanda, un caso, una situazione descritta — in un **output testuale** coerente con il modello HCAIRE: non riduttivo, attento alla configurazione, contestualizzato, non prescrittivo. Il motore non produce direttamente il testo finale: produce una **struttura interpretativa intermedia** (cfr. §6), dalla quale il testo viene poi composto.

---

## 2. Logica generale: due fasi più verifica

Il motore articola tre momenti operativamente distinti, in coerenza con l'**Ipotesi di ridefinizione** di Bartleby (vedi `Bartleby/Ipotesi di ridefinizione.md`):

```
TRACCIA
   │
   ▼
[Selezione]   quali skill attivare per questa traccia
   │
   ▼
[Indagine]    leggere la traccia e ricondurla al modello (skill di fondamento + di nodo + di ambito)
   │            → TraceInterpretation
   ▼
[Scrittura]   tradurre la lettura in output per il destinatario (skill di output + di personalizzazione)
   │            → OutputDocument
   ▼
[Verifica]    controllare la coerenza dell'output con il fondamento (skill di verifica)
```

Indagine e scrittura sono fasi separate, non un unico processo. La separazione è un requisito di **diagnosticabilità**: un output può sbagliare la scrittura senza aver sbagliato la lettura, o viceversa, e si può correggere l'una senza rifare l'altra.

---

## 3. Selezione

Dalla traccia il motore decide quali skill attivare. La selezione è guidata da:

- **Indizi nodali**: quali Nodi Trasversali (N1–N7) sembrano in gioco (parole, situazioni, segnali);
- **Indizio di ambito**: a quale dei 4 contesti canonici è destinato l'output (Genitoriale, Clinico, Pedagogico, Istituzionale/servizi);
- **Tipo di output richiesto**: dal `target_output_type` dell'InputTrace, fra gli `OutputTemplate` disponibili;
- **Profilo di personalizzazione utente** (se presente).

La selezione attiva, in modo coerente, le corrispondenti **skill di nodo**, **skill di ambito**, **skill di fondamento** (gli assi sempre presenti come lente), **skill di output** e **skill di personalizzazione**. La tassonomia delle skill e la loro relazione con assi e nodi è definita nell'`Ipotesi di ridefinizione`, §4.2.

---

## 4. Indagine — leggere la traccia

L'indagine ha cinque operazioni, da eseguire come *struttura di lettura* non come sequenza meccanica.

### 4.1 Riformulazione della traccia

Identificare il problema reale implicito nella traccia. Chi sono i soggetti coinvolti? Quali presupposizioni la traccia contiene? Quale immagine dello sviluppo è già attiva nella formulazione? Che livello e che destinatario richiede? La riformulazione **esplicita** ciò che la traccia lascia implicito; non lo corregge.

### 4.2 Mappatura sui Nodi Trasversali

Per ciascuno dei 7 nodi canonici (N1–N7) il motore valuta se è **attivato** dalla traccia, e in quale stato (per le tracce dove ne ha senso, in coerenza con la grammatica CE):

- **N1** Regolazione / Integrazione dell'esperienza
- **N2** Campo relazionale / Co-regolazione
- **N3** Accesso al mondo condiviso simbolico
- **N4** Apertura / Esplorabilità del mondo
- **N5** Separazione / Limite reale
- **N6** Continuità temporale del Sé nascente
- **N7** Desiderio / Direzione dell'esperienza

I criteri di attivazione, presenza, impoverimento di ciascun nodo sono nelle schede dell'`Atlante nodi trasversali.md` v2.0.

### 4.3 Mappatura sugli Assi salienti

Indipendentemente dai nodi, il motore individua quali **assi strutturali** (A1–A6) la traccia attiva in modo saliente. I 6 assi sono sempre compresenti (Carta fondativa §5); qui si segnala la salienza relativa per questa traccia. La distinzione assi/nodi è canonica: gli assi sono dimensioni strutturali permanenti, i nodi sono configurazioni multi-asse (Atlante v2.0 §2).

### 4.4 Identificazione dell'ambito

Il motore conferma o identifica il **contesto canonico** di destinazione fra i 4: Clinico, Pedagogico, Genitoriale, Istituzionale/servizi. La scheda di ambito corrispondente (`Schede di ambito/<X>.md`) attiva il proprio lessico, i propri rischi tipici, le proprie domande guida (§7 della scheda) e i propri vincoli di output (§9–§10–§13 della scheda).

### 4.5 Rilevamento dei rischi di riduzione

Quali riduzioni tipiche la traccia rischia di indurre nell'output? Le forme principali, riprese dalla Carta fondativa §6 e dalle schede di ambito:

- riduzionismo (una dimensione domina le altre);
- frammentazione (le dimensioni non sono integrate);
- causalità lineare (processi complessi → cause semplici);
- invisibilità del soggetto (il bambino come oggetto di valutazione);
- decontestualizzazione (contesto storico-culturale ignorato);
- prescrittività (orientamento → istruzione);
- psicologizzazione del sociale (problemi strutturali attribuiti all'individuo).

Ogni nodo e ogni scheda di ambito porta in più i propri *rischi specifici* (campi `reduction_risks`): vanno attivati di conseguenza.

### 4.6 Integrazione: la configurazione emergente

L'esito dell'indagine non è un elenco di nodi e rischi ma una **configurazione** coerente: come, in questa traccia, i nodi attivati si tengono insieme (sostegno, vincolo, mediazione, compensazione — `Atlante` §7) e cosa rende la situazione abitabile o ne segnala la fatica. È la struttura interpretativa intermedia di cui parla la §6 — il «modulo D» del vecchio Motore, ora ricondotto alla grammatica delle Configurazioni Evolutive (Metodo-fasi-concetti, Fase 2 §7) anziché a pattern paralleli sciolti.

---

## 5. Scrittura — tradurre verso l'output

La scrittura traduce la struttura interpretativa in un testo per il destinatario. Modula:

- **Linguaggio e tono** secondo la scheda di ambito (§10) e il profilo di personalizzazione utente.
- **Tipo di output** secondo il template selezionato (`output_templates.json`): guida-genitoriale, nota-clinico-riflessiva, guida-educativa, griglia-osservazionale, analisi-di-caso, policy-brief, articolo-riflessione.
- **Profondità** secondo il destinatario: per output divulgativi semplificare senza banalizzare; per output clinici mantenere precisione e linguaggio probabilistico; per il livello istituzionale combinare argomento fondativo, di equità ed economico.

La scrittura **rispetta sempre i campi anti-prescrittivi**: il testo descrive configurazioni e atteggiamenti possibili, non istruzioni; non sostituisce il giudizio del professionista né la relazione con il bambino.

---

## 6. Punto decisivo — la struttura interpretativa intermedia

Il motore **non** produce direttamente il testo finale: produce una struttura intermedia, che la scrittura trasforma in testo. È questo passaggio che evita gli output superficiali. La struttura intermedia è leggibile e ispezionabile: nodi attivati, assi salienti, rischi rilevati, configurazione emergente. È anche la base della **trasparenza** che caratterizza Bartleby — il pannello «come è stato generato questo output» che espone la genealogia decisionale (`CLAUDE_webapp.md` §3, sezione di provenienza).

---

## 7. Verifica della qualità

La verifica controlla che l'output sia coerente con il fondamento canonico. Indicatori positivi:

- più dimensioni integrate, attenzione alla relazione, riconoscimento della complessità;
- linguaggio non meccanicistico, non solo prestazionale;
- distinzione assi/nodi rispettata (non si trattano le dimensioni come nodi e viceversa);
- assenza di diagnosi implicite, prescrizioni rigide, rassicurazioni vuote;
- genealogia leggibile della lettura (quali nodi, quali assi, quali rischi).

Indicatori negativi: causalità semplicistiche, assenza del soggetto, prescrizioni rigide non contestualizzate, riduzione del bambino a sintomi o prestazioni.

---

## 8. Criticità da gestire

Quattro rischi strutturali del motore stesso, ereditati dal vecchio Motore e ancora pertinenti:

- **Rigidità** — se la struttura interpretativa diventa meccanica, l'output è freddo e formulaico.
- **Vaghezza** — se la struttura resta troppo aperta, perde potere operativo.
- **Uniformità** — il rischio che tutti i testi «suonino uguali» perché ricondotti meccanicamente alla stessa grammatica.
- **Sovrainterpretazione** — forzare il modello su contenuti che non lo sollecitano.

Si gestiscono in fase di revisione editoriale e calibrazione delle skill, non con regole più dettagliate.

---

## 9. Relazione con i moduli A–F del precedente Motore

Il vecchio *Motore di traducibilità* articolava il processo in sei moduli A–F. Il nuovo motore li ricomprende così:

| Moduli A–F (precedente) | Collocazione attuale |
|---|---|
| A — Riformulazione della traccia | §4.1 Riformulazione |
| B — Analisi multidimensionale | §4.2 Mappatura sui nodi + §4.3 Mappatura sugli assi (resa rigorosa: assi e nodi distinti) |
| C — Identificazione dei nodi critici (riduzionismi) | §4.5 Rilevamento dei rischi di riduzione (chiarito: «nodi critici» qui non sono Nodi Trasversali ma rischi) |
| D — Integrazione con il modello | §4.6 Configurazione emergente (ricondotta alla grammatica CE) |
| E — Traduzione verso l'output | §5 Scrittura |
| F — Indicatori di qualità del testo | §7 Verifica |

La differenza non è di sostanza ma di **disciplina** dell'apparato: assi e nodi tenuti distinti, configurazione formalizzata, 4 contesti canonici, riferimenti al fondamento ufficiale.

---

## 10. Pendenze

Due punti aperti che riguardano l'implementazione, non la concezione del motore:

- **Il prototipo trigger** (`CLAUDE.md` di root con `input_bartleby.md`) hard-codifica ancora alcuni elenchi (output_type, audience) che diverggono dai dati seed. Un'evoluzione completa verso Bartleby v2 — con skill di nodo, skill di indagine/scrittura come oggetti strutturati, motore di selezione esplicito — è descritta nell'`Ipotesi di ridefinizione`.
- **La propagazione dell'apparato v2.0 al repo webapp e a MongoDB** (oggi a 10 nodi / 5 ambiti) resta priorità immediata, indipendente dal motore (cfr. `11 Bartleby/Revisione/Fonti dei dati di seed e source of truth.md`).

---

*Motore di lettura della traccia — operativo di Bartleby — v2.0 — 2026-05-25.*
