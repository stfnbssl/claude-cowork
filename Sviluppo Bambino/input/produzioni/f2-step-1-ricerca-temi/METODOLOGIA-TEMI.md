# Linee guida metodologiche per la ricerca e formulazione dei temi

Questo documento raccoglie regole, criteri e avvertenze metodologiche derivate dalla revisione critica delle prime elaborazioni. Va letto in combinazione con `CLAUDE.md`.

Versione: 1.0 — Aprile 2026

---

## 1. Separazione rigorosa tra STEP 1 e STEP 2

Il JSON di theme discovery include campi che appartengono a fasi logicamente distinte:

**STEP 1 — Definizione del tema** (deve essere completato prima):
- `theme_label_provisional`
- `starting_point`
- `structural_focus`
- `what_it_is`
- `what_it_is_not`
- `why_it_matters`
- `source_signals`
- `definition_draft`
- `definition_risks`

**STEP 2 — Lettura strutturale preliminare** (dipende da STEP 1):
- `possible_axes_involved`
- `possible_structural_nodes`
- `possible_bridge_concepts`
- `exploratory_priority`
- `pilot_suitability`
- `human_review_notes`

**Regola operativa**: il testo dei campi STEP 1 non deve già presupporre la lettura strutturale. Se nella formulazione di `what_it_is` o `definition_draft` compaiono riferimenti a nodi strutturali specifici degli assi, è un segnale che c'è stata contaminazione tra le due fasi. STEP 1 deve reggere da solo, come fuoco strutturale provvisorio formulato sulla base delle fonti, prima di qualsiasi confronto con i JSON degli assi.

**Test di coerenza**: rileggere `what_it_is` e `definition_draft` immaginando di non avere i JSON degli assi disponibili. Se il testo perde senso o sembra incompleto, la formulazione ha sconfinato in STEP 2.

---

## 2. Formulazione dell'etichetta provvisoria

L'etichetta (`theme_label_provisional`) deve:

- catturare il **fuoco strutturale** del tema, non solo la sua forma esteriore o il contesto in cui si manifesta
- essere abbastanza specifica da distinguere il tema da fenomeni adiacenti
- non ridursi a un sintagma puramente descrittivo o contestuale (es. "lettura precoce con i bambini" è descrittivo; "mediazione simbolica condivisa nella diade precoce" è strutturale)

**Errori tipici da evitare**:
- Etichette troppo operative: nominano uno strumento o una tecnica invece di un fenomeno strutturale
- Etichette che sottopesano una dimensione chiave: es. nominare solo la relazione senza la dimensione simbolica, o solo la pratica senza la dimensione regolativa
- Etichette che riducono fenomeni poliadici a fenomeni diadici (vedi sezione 4)

**Procedura suggerita**: formulare almeno due etichette candidate, identificare cosa si perde in ciascuna, scegliere quella che preserva più dimensioni strutturali rilevanti.

---

## 3. Selezione degli assi coinvolti

### 3.1 Non escludere prematuramente Asse 2

L'Asse 2 (Affettivo–morale) tende a essere sottorappresentato nelle prime elaborazioni perché le sue manifestazioni più visibili (riconoscimento reciproco, interiorizzazione della presenza condivisa attorno a un oggetto comune) sono meno immediatamente ovvie rispetto agli altri assi. Prima di escluderlo, verificare esplicitamente:

- il tema implica una forma di riconoscimento reciproco tra soggetti?
- il tema coinvolge l'interiorizzazione di una presenza o di una relazione?
- il tema ha a che fare con la nascita di una forma di alterità interiorizzata?

Se la risposta è sì a una o più di queste domande, Asse 2 va incluso.

### 3.2 Prudenza su Asse 3 per le età precoci (0–3 anni)

L'Asse 3 (Normativo–educativo) ha formulazioni che presuppongono un grado di sviluppo del giudizio e della normatività che non è ancora presente nei bambini sotto i 3 anni. Per questa fascia d'età:

- evitare formulazioni come "trasmissione normativa implicita" o "orientamento normativo" senza qualificarle
- preferire formulazioni come: "selezione implicita di senso", "strutturazione di primi orizzonti di significato", "orientamenti impliciti del campo di esperienza"
- indicare esplicitamente in `human_review_notes` l'incertezza sull'applicabilità dell'Asse 3 alla fascia d'età target

### 3.3 Verifica sistematica della copertura

Prima di chiudere il campo `possible_axes_involved`, verificare tutti e sei gli assi con una domanda strutturale per ciascuno:

| Asse | Domanda di verifica |
|---|---|
| Asse 1 — Ontologico–fenomenologico | Il tema coinvolge corporeità, campo intenzionale, temporalità vissuta? |
| Asse 2 — Affettivo–morale | Il tema coinvolge riconoscimento reciproco, alterità interiorizzata, dimensione morale precoce? |
| Asse 3 — Normativo–educativo | Il tema coinvolge orientamento normativo, trasmissione di senso, giudizio? (con prudenza per 0–3 anni) |
| Asse 4 — Separazione e Limite | Il tema coinvolge incontro con la realtà, frustrazione, separazione, limite strutturale? |
| Asse 5 — Desiderio | Il tema coinvolge orientamento verso il possibile, campo desiderabile, motivazione vs. desiderio? |
| Asse 6 — Storico–culturale | Il tema coinvolge mediazioni storiche, istituzioni, tecnica, configurazioni culturali contemporanee? |

---

## 4. Riconoscimento delle strutture poliadiche

Alcuni fenomeni hanno una struttura triadica o poliadica che non va ridotta alla diade caregiver–bambino.

**Criterio diagnostico**: se il fenomeno cambia qualitativamente quando si rimuove uno degli elementi (non solo si impoverisce, ma diventa un fenomeno diverso), la struttura è poliadica e va esplicitata.

**Esempio paradigmatico**: nella lettura condivisa precoce, il libro non è un semplice supporto: è un mediatore simbolico costitutivo. La triade caregiver–bambino–libro non è riducibile alla diade caregiver–bambino + un oggetto. Rimuovere il libro trasforma la relazione in qualcosa di strutturalmente diverso.

**Regola operativa**:
- identificare tutti gli elementi della struttura
- per ciascuno, chiedersi: se lo rimuovo, il fenomeno rimane strutturalmente lo stesso o cambia?
- se cambia, l'elemento è costitutivo e va nominato nell'etichetta o nella definizione
- segnalare la struttura poliadica in `structural_focus` e in `what_it_is`

---

## 5. Livello di astrazione nella definizione del tema

Il tema è un **fuoco strutturale provvisorio**, non una descrizione di una pratica né un concetto già elaborato dalla letteratura.

**Regola del livello**: la definizione in `definition_draft` deve essere:
- più astratta di una descrizione empirica (non "cosa fanno i caregiver quando leggono con il bambino")
- meno astratta di un concetto strutturale già elaborato (non "mediazione simbolica vygotskijana")
- formulata come interrogazione aperta su un fenomeno strutturalmente rilevante

**Test di livello**: se la definizione potrebbe comparire direttamente in un manuale di prassi professionale senza modifiche, è troppo concreta (scivola in STEP 2 o nell'operativo). Se potrebbe comparire direttamente in un testo di filosofia dello sviluppo senza modifiche, è troppo astratta.

---

## 6. Trattamento dell'incertezza

Quando l'attribuzione di un asse o di un nodo è incerta:

- **non omettere**: segnalare con `"confidence": "bassa"` o equivalente nel campo `possible_axes_involved`
- **motivare brevemente** l'incertezza in `human_review_notes`
- **non risolvere artificialmente** l'incertezza scegliendo l'opzione più plausibile senza segnalare il dubbio

I nodi strutturali e i concetti-ponte in STEP 2 sono **candidati**, non assegnazioni definitive. La formulazione deve riflettere questo carattere provvisorio.

---

## 7. Rischi di definizione da segnalare sistematicamente

Per ogni tema, verificare e segnalare esplicitamente in `definition_risks` i seguenti rischi:

1. **Riduzione operativa**: il tema viene identificato con uno strumento, un protocollo o una tecnica professionale
2. **Riduzione mono-disciplinare**: il tema viene catturato interamente da una disciplina (es. tutto clinico, tutto pedagogico, tutto neurologico)
3. **Genericità**: il tema è troppo ampio per avere densità strutturale propria
4. **Contemporaneizzazione**: il tema viene letto esclusivamente attraverso le categorie del contesto storico contemporaneo perdendo la struttura fondativa
5. **Collasso diadico**: per i temi con struttura poliadica, il rischio di ridurli a sola diade caregiver–bambino
6. **Anticipazione normativa**: per le età precoci (0–3), il rischio di attribuire funzioni normative o giudicative prematuramente

Non tutti i rischi si applicano a ogni tema: selezionare quelli pertinenti e motivarli brevemente.
