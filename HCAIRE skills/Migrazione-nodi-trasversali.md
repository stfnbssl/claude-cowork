# Migrazione dei Nodi Trasversali — da 10 nodi (v1) ai 7 canonici (N1–N7)

> **Scopo.** Registrare la decisione di adottare l'enumerazione canonica dei Nodi Trasversali e tracciare la mappatura dai 10 nodi della prima versione dell'Atlante ai 7 nodi canonici. È il documento di riferimento per la revisione, demandata a un passaggio successivo, dei dati seed di Bartleby e dei testi derivati.
>
> **Data:** 2026-05-24 · **Stato:** decisione registrata; livello fondativo eseguito, livelli dati e testi derivati da eseguire.

---

## 1. La decisione

Il progetto HCAIRE skills adotta come **base fondativa ufficiale** il documento `04 Memorie di contesto fondamentali/Metodo-fasi-concetti.md` e, in particolare, l'enumerazione canonica dei **7 Nodi Trasversali (N1–N7)** e dei **6 Assi Strutturali (A1–A6)** definita nella sua Fase 2.

Questa decisione scioglie la prima questione aperta lasciata da `Bartleby/Ipotesi di ridefinizione.md` (§5): *quale sia l'enumerazione canonica dei nodi trasversali*. La risposta è: quella della pipeline Produzioni di Sviluppo Bambino, già sviluppata. Per coerenza e semplicità, HCAIRE adotta un'unica grammatica dei nodi.

## 2. Perché non è una semplice rinumerazione

La prima versione dell'Atlante proponeva **10 nodi**. Confrontata con il modello canonico, quella lista **confondeva due livelli che il modello tiene distinti**:

- alcuni dei 10 erano effettivamente nodi-configurazione (configurazioni multi-asse);
- altri — *Affettività*, *Corpo e esperienza incarnata*, *Contesto storico-culturale* — sono in realtà **Assi**, non nodi. Nel modello canonico un Nodo richiede la co-attivazione costitutiva di **almeno tre assi** (`Metodo-fasi-concetti.md`, Fase 2 §4.2): un elemento che coincide con un solo asse non può essere un nodo;
- uno — *Integrazione / disorganizzazione* — non è un nodo autonomo ma una componente di N1 e, sul versante grammaticale, la dimensione **A (Abitabilità)** della Configurazione Evolutiva.

La migrazione è quindi una **ri-stratificazione**: si separa il livello degli Assi (6) dal livello dei Nodi (7). Non si perde contenuto — i nodi della v1 che erano assi rientrano nel livello, già esistente, delle `Skill di fondamento/` (una per asse).

## 3. Tabella di mappatura — dai 10 nodi v1 ai 7 canonici

| ID v1 | Nodo v1 | Destinazione canonica | Tipo di transizione |
|---|---|---|---|
| cn-001 | Relazione adulto-bambino | **N2** — Campo relazionale / Co-regolazione | confluenza diretta |
| cn-002 | Regolazione e co-regolazione | **N1** — Regolazione / Integrazione (componente regolativa); concorre a **N2** per l'aspetto co-regolativo-relazionale | confluenza con scissione |
| cn-003 | Linguaggio e significato condiviso | **N3** — Accesso al mondo condiviso simbolico | confluenza diretta |
| cn-004 | Affettività | **Asse A2** — Affettivo-morale | riassorbito nel livello Assi (non è un nodo) |
| cn-005 | Corpo e esperienza incarnata | **Asse A1** — Ontologico-fenomenologico (dimensione corporea) | riassorbito nel livello Assi (non è un nodo) |
| cn-006 | Limite reale e separazione | **N5** — Separazione / Limite reale | confluenza diretta |
| cn-007 | Desiderio e iniziativa del soggetto | **N7** — Desiderio / Direzione dell'esperienza | confluenza diretta |
| cn-008 | Contesto storico-culturale | **Asse A6** — Rapporto con il mondo storico e culturale | riassorbito nel livello Assi (non è un nodo) |
| cn-009 | Integrazione / disorganizzazione | **N1** (componente di integrazione) + dimensione **A (Abitabilità)** della grammatica CE | riassorbito (non è un nodo autonomo) |
| cn-010 | Apertura / chiusura al mondo | **N4** — Apertura / Esplorabilità del mondo | confluenza diretta |

### 3.1 Lettura inversa — origine dei 7 nodi canonici

| Nodo canonico | Origine dalla v1 |
|---|---|
| **N1** Regolazione / Integrazione | cn-002 (regolazione) + cn-009 (integrazione) |
| **N2** Campo relazionale / Co-regolazione | cn-001 (+ aspetto co-regolativo di cn-002) |
| **N3** Accesso al mondo condiviso simbolico | cn-003 |
| **N4** Apertura / Esplorabilità | cn-010 |
| **N5** Separazione / Limite reale | cn-006 |
| **N6** Continuità temporale del Sé nascente | **nessun predecessore — nodo nuovo** |
| **N7** Desiderio / Direzione | cn-007 |

### 3.2 Il caso N6

**N6 — Continuità temporale del Sé nascente** non ha alcun corrispettivo nella v1. È un nodo canonico che la prima versione dell'Atlante semplicemente non prevedeva: la persistenza dell'esperienza attraverso le discontinuità (riprendersi dopo una frattura, una regressione, un'interruzione). Va costruito ex novo in tutti i livelli — scheda di nodo (già fatto, Atlante v2), skill di nodo, dati seed, riferimenti nelle schede di ambito.

## 4. Conseguenze sul livello degli Assi

I tre nodi v1 riassorbiti (cn-004 Affettività → A2; cn-005 Corpo → A1; cn-008 Contesto storico-culturale → A6) non perdono contenuto: la loro trattazione è già coperta dalle `Skill di fondamento/` corrispondenti (Skill-Asse2, Skill-Asse1, Skill-Asse6). Nella revisione dei dati seed andrà deciso se introdurre un'entità esplicita *Asse* nel modello dati di Bartleby — oggi assente: gli assi vivono solo come skill di fondamento — o se mantenere gli assi rappresentati unicamente dalle skill di fondamento. È una decisione del passaggio sui dati (§5).

## 5. Cosa resta da rivedere — passaggio successivo

Il livello fondativo è stato eseguito: `Documenti fondativi/Atlante nodi trasversali.md` è stato riscritto alla v2.0 sui 7 nodi canonici. Restano da rivedere, in un passaggio successivo e coordinato, i seguenti file.

**Dati seed di Bartleby** (`Bartleby/data/`)
- `concept_nodes.json` — da 10 record a 7 (uno per N1–N7); rimozione dei 3 record-asse; costruzione ex novo di N6. Si raccomanda di adottare come identificatori i codici canonici (N1–N7) al posto di cn-001…cn-010.
- `foundation_document_nodes.json`, `area_sheet_nodes.json`, `skill_nodes.json` — tabelle ponte: rimappare ogni riferimento di nodo secondo la tabella §3; ricostruire i legami per N6.
- `input_traces.json` — campo `activated_nodes`: rimappare i nodi annotati nelle 17 tracce.

**Testi derivati**
- `Schede di ambito/` (5 schede) — riferimenti ai nodi e ai loro lessici.
- `Skill di fondamento/` (6 skill) — in particolare i rimandi al nodo "Integrazione/disorganizzazione" (esplicito in Skill-Asse1).
- `Mappa-corrispondenza-terminologica.md` — la voce sui nodi e l'indice.
- `CLAUDE.md` (root, prototipo trigger) e `Bartleby/CLAUDE.MD`, `Bartleby/CLAUDE_webapp.md` — riferimenti ai nodi e ai conteggi.
- `Bartleby/Modello dati.md`, `Bartleby/Modello app.md` — gli esempi di `ConceptNode`.
- `STATO-PROGETTO.md` — i conteggi (10 concept_nodes → 7) e le note di batch.
- `Verifica-coerenza-schede-ambito.md` / `-v2.md` — riferimenti ai nodi.
- `Repertorio tracce di esempio/Corpus-tracce-v1.md` — annotazioni `activated_nodes`.
- `Bartleby/Ipotesi di ridefinizione.md` — la questione aperta §5 sull'enumerazione dei nodi risulta ora sciolta: andrà aggiornata di conseguenza.

## 6. Principio della migrazione

La rimappatura non è un'operazione meccanica di sostituzione di codici. Per ogni file derivato vale il criterio: un riferimento a un nodo v1 che era *davvero un nodo* si rimappa sul nodo canonico corrispondente (§3); un riferimento a un nodo v1 che era *un asse* va riformulato come riferimento all'asse, non forzato dentro un nodo. Dove un testo derivato attribuiva a un "nodo" v1 contenuti che il modello canonico colloca a livello di asse o di dimensione grammaticale (Abitabilità), la revisione è anche un'occasione di correzione concettuale, non solo di rietichettatura.

---

*Documento di migrazione dei Nodi Trasversali — 2026-05-24.*
