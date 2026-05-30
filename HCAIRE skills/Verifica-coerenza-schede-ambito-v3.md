# VERIFICA DI COERENZA — Schede di Ambito ↔ Skill di Fondamento
## Versione 3.0 — sul nuovo apparato (7 nodi canonici, 4 contesti)
*Prodotta: 2026-05-24*

> Questa verifica sostituisce la v2.0 (pre-migrazione). È condotta sul nuovo apparato: i **4 contesti canonici** (Genitoriale, Clinico, Pedagogico, Istituzionale/servizi), le 4 schede di ambito riviste alla v2.0, i **7 Nodi Trasversali canonici N1–N7** e le 6 skill di fondamento (Assi 1–6). Riferimenti: `Documenti fondativi/Atlante nodi trasversali.md` v2.0, `Migrazione-nodi-trasversali.md`.

---

## 1. Oggetto della verifica

Si verificano tre coerenze:

- **copertura degli Assi** — quali dei 6 assi strutturali sono trattati in ciascuna scheda di ambito;
- **copertura dei Nodi** — quali dei 7 nodi trasversali sono prioritari in ciascuna scheda (§8 delle schede);
- **coerenza schede ↔ dati seed** — corrispondenza tra il §8 delle schede e le tabelle `area_sheet_nodes.json` / `skill_nodes.json`.

Legenda: ● presente/prioritario · ◑ parziale/secondario · ○ assente.

---

## 2. Mappa di copertura degli Assi

| Asse | Genitoriale | Clinico | Pedagogico | Istituzionale/servizi |
|------|-------------|---------|------------|------------------------|
| **A1** Ontologico-fenomenologico | ● | ● | ● | ○ |
| **A2** Affettivo-morale | ● | ● | ● | ◑ |
| **A3** Normativo-educativo | ○ | ○ | ● | ● |
| **A4** Separazione e limite reale | ● | ● | ● | ◑ |
| **A5** Desiderio | ◑ | ● | ● | ◑ |
| **A6** Rapporto con il mondo storico-culturale | ● | ● | ● | ● |

Lettura: il quadro è migliorato rispetto alla v2.0 — la fusione di Politico e Sociologico in Istituzionale/servizi ha consolidato la copertura di A2, A4 e A5 al livello sistemico (prima frammentata tra due schede). Restano i gap della §5.

---

## 3. Mappa di copertura dei Nodi

Dal §8 delle schede riviste, coerente con `area_sheet_nodes.json`.

| Nodo | Genitoriale | Clinico | Pedagogico | Istituzionale/servizi |
|------|-------------|---------|------------|------------------------|
| **N1** Regolazione / Integrazione | ● primario | ● primario | ◑ secondario | ● primario |
| **N2** Campo relazionale / Co-regolazione | ● primario | ● primario | ● primario | ● primario |
| **N3** Accesso al mondo condiviso simbolico | ● primario | ◑ secondario | ● primario | ◑ secondario |
| **N4** Apertura / Esplorabilità del mondo | ○ | ○ | ○ | ◑ secondario |
| **N5** Separazione / Limite reale | ◑ secondario | ◑ secondario | ◑ secondario | ◑ secondario |
| **N6** Continuità temporale del Sé nascente | ○ | ○ | ○ | ● primario |
| **N7** Desiderio / Direzione dell'esperienza | ◑ secondario | ◑ secondario | ● primario | ◑ secondario |

N2 è prioritario in tutti i contesti (è il nodo più trasversale); N5 è secondario ovunque ma sempre presente. N4 e N6 sono i nodi meno coperti (vedi §5).

---

## 4. Coerenza schede ↔ dati seed

- **§8 schede ↔ `area_sheet_nodes.json`** — coerente per costruzione: nella migrazione v2.0 le righe di `area_sheet_nodes.json` sono state ricostruite a partire dal §8 delle schede riviste. Le 22 righe corrispondono esattamente alla mappa della §3.
- **skill di ambito ↔ `skill_nodes.json`** — coerente: le righe `operativo` delle skill di ambito (sk-007…sk-010) rispecchiano i nodi prioritari del rispettivo contesto.
- **skill di fondamento ↔ nodi** — le righe `fondamento-diretto` di `skill_nodes.json` derivano dal campo `axes_involved` dei 7 nodi: ogni nodo è collegato alle skill degli assi che lo costituiscono. Nessuna incoerenza.

---

## 5. Gap identificati

**Gap di asse (confermati dalla v2.0, non ancora chiusi)**

- **A3 — Normatività in Genitoriale e Clinico.** La distinzione norma/normatività/giudizio e l'autorità educativa legittima non sono trattate esplicitamente nelle schede Genitoriale e Clinico. È il gap più rilevante: tocca il cuore di molte domande genitoriali e la lettura clinica delle dinamiche educative familiari.
- **A5 — Desiderio in Genitoriale.** Presente solo come traccia («iniziativa del bambino»): manca la trattazione del desiderio come struttura di orientamento, con la distinzione desiderio/bisogno/motivazione/capriccio.
- **A1 in Istituzionale/servizi.** Marcato assente: è un gap *strutturale atteso* — la scala sistemica astrae dal soggetto incarnato. Va presidiato (l'ambito non deve perdere il soggetto), non necessariamente «colmato».

**Gap di nodo (nuovi, emersi dalla mappa §3)**

- **N4 — Apertura / Esplorabilità** è prioritario solo in Istituzionale (come secondario). È un nodo centrale per la lettura di curiosità, ritiro ed esplorazione: andrebbe esplicitato almeno nelle schede Clinico e Pedagogico, dove la qualità del campo esplorativo è osservativamente rilevante.
- **N6 — Continuità temporale del Sé nascente** compare solo in Istituzionale/servizi. È il nodo introdotto dalla migrazione (non aveva predecessori nella v1): la sua assenza dagli altri tre §8 è coerente con il fatto che le schede sono state riviste prima che N6 fosse elaborato in profondità. Va integrato in Clinico (recuperabilità delle regressioni), Pedagogico (apprendimento cumulativo) e Genitoriale (ripresa dopo le difficoltà).

---

## 6. Verdetto

Il nuovo apparato è **internamente coerente**: schede, dati seed e skill non presentano incoerenze di riferimento; la fusione a 4 contesti ha consolidato la copertura degli assi al livello sistemico. Restano **aperti tre gap di asse** (A3 in Genitoriale e Clinico, A5 in Genitoriale; A1 in Istituzionale come gap strutturale da presidiare) e **due gap di nodo** (N4 e N6 poco coperti). Nessuno è bloccante; tutti sono affrontabili come cicli di intervento mirati sulle schede, da accompagnare con il corrispondente aggiornamento di `area_sheet_nodes.json`.

Priorità suggerita per il prossimo ciclo: **N6 nelle tre schede non istituzionali** (è il nodo nuovo, oggi il meno coperto) e **A3 in Genitoriale e Clinico** (il gap di asse più rilevante).

---

*Verifica di coerenza v3.0 — sul nuovo apparato a 7 nodi canonici e 4 contesti — 2026-05-24.*
