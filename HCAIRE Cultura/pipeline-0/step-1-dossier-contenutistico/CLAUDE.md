# STEP 1 — Dossier contenutistico

## Obiettivo
Raccogliere informazioni affidabili e verificate sull'opera senza interpretarla. Questo step produce la base fattuale su cui si costruiranno tutti gli step successivi. Nessuna applicazione degli assi strutturali. Nessuna critica compiuta.

---

## Input atteso

L'utente fornirà:
- **Titolo** dell'opera
- **Autore / Regista / Creatore**
- **Macrotipologia** (romanzo, film, opera teatrale, racconto, saggio narrativo, serie televisiva, fumetto, ecc.)
- **Materiali disponibili** (testo completo, trascrizione, sinossi, accesso diretto, ecc.)
- **Fonti opzionali** (articoli critici già forniti, link, note)

---

## Istruzioni operative per Cowork

1. **Raccogli i dati essenziali dell'opera** tramite ricerca web e/o analisi dei materiali forniti:
   - Titolo completo, autore, anno di prima pubblicazione/uscita, editore/produttore, genere, eventuale serie o ciclo di appartenenza.

2. **Scrivi una sintesi contenutistica neutra**: riassumi il contenuto dell'opera (trama, argomento, struttura) in modo descrittivo, senza interpretare né valutare. Usa il condizionale per elementi incerti o controversi.

3. **Descrivi la struttura formale**: come è organizzata l'opera (capitoli, atti, sequenze, episodi, parti, movimenti). Numero di unità, eventuali irregolarità o scelte formali rilevanti.

4. **Mappa i personaggi / figure / gruppi**: per ogni entità principale, indica nome, ruolo nell'opera, relazioni con le altre entità. Non interpretare caratteri psicologici: descrivi ruoli e funzioni narrative.

5. **Individua le scene, episodi, immagini o momenti chiave**: i momenti dell'opera che sembrano strutturalmente più significativi (snodi narrativi, scene ad alta intensità, passaggi formali rilevanti). Descrivili senza interpretarli.

6. **Elenca i temi espliciti**: i temi dichiarati o facilmente riconoscibili nell'opera (es. la guerra, la famiglia, la perdita, l'identità). Basati su quanto è manifesto nel testo/immagini, non su inferenze.

7. **Segnala le tensioni emergenti**: elementi che sembrano in conflitto, irrisolti o problematici all'interno dell'opera, che potrebbero richiedere interpretazione. Non interpretarle: limitati a nominarle come aree di potenziale interesse critico.

8. **Descrivi il contesto storico-culturale**: anno e luogo di produzione, clima culturale, eventuali riferimenti storici rilevanti, tradizione letteraria/cinematografica/teatrale di appartenenza, ricezione critica principale.

9. **Aggiungi le avvertenze anti-confabulazione**: segnala esplicitamente quali informazioni sono certe (basate su fonti verificabili), quali probabili (inferite con buona base) e quali incerte o non reperibili. Se non hai accesso all'opera completa, indicalo chiaramente.

---

## Regola fondamentale

> **Non applicare gli assi strutturali in questo step. Non avanzare tesi interpretative. Non valutare l'opera. Descrivere, non interpretare.**

---

## Generazione dello slug

Lo slug identifica l'opera in modo univoco e determina il nome della cartella in cui saranno salvati tutti gli output della pipeline. Va generato in questo step e usato in modo coerente in tutti gli step successivi.

**Regole di formazione:**
- Formato: `{cognome-autore}_{titolo-opera}`
- Tutto in minuscolo
- Spazi sostituiti da trattini (`-`)
- Caratteri accentati sostituiti dalla versione non accentata (è → e, à → a, ecc.)
- Punteggiatura e caratteri speciali rimossi
- Per opere con titolo molto lungo: usare le prime 4-5 parole significative

**Esempi:**
- *Il Gattopardo* di Giuseppe Tomasi di Lampedusa → `lampedusa_il-gattopardo`
- *La cognizione del dolore* di Carlo Emilio Gadda → `gadda_la-cognizione-del-dolore`
- *Apocalypse Now* di Francis Ford Coppola → `coppola_apocalypse-now`
- *Aspettando Godot* di Samuel Beckett → `beckett_aspettando-godot`

---

## Percorso di output

Crea la cartella dell'opera e salva il file di output nel percorso:

```
C:\my\claude\claude-cowork\HCAIRE Cultura\letture\{slug}\step-1-dossier-contenutistico.json
```

Se la cartella `letture\{slug}\` non esiste, creala prima di salvare il file.

Produce un documento JSON conforme allo schema `schema.json` presente in questa cartella.
