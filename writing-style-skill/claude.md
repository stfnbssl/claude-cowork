# Claude come operatore degli script — Istruzioni operative

Questo file documenta cosa può fare Claude (l'IA in questa sessione Cowork) per gestire il ciclo di apprendimento della writing-style-skill senza che tu debba aprire un terminale.

---

## Gli stili disponibili

Il sistema è organizzato su due livelli: uno **stile base** con le regole universali della tua voce, e tre **stili specifici** per contesto. Claude legge sempre entrambi i livelli.

| Stile | Cartella | Usato per |
|---|---|---|
| Base | `base/` | Regole valide in ogni contesto — letto sempre |
| Saggio scientifico-filosofico | `saggio-filosofico/` | Articoli, saggi, testi argomentativi |
| Critica culturale | `critica-culturale/` | Recensioni e analisi di film e testi narrativi |
| Pagine web | `pagine-web/` | Testi per il sito su sviluppo umano e del bambino |

---

## Come attivare uno stile

Basta dirlo nella richiesta:

> "Scrivi una recensione del film X **usando lo stile critica culturale**"
> "Scrivi la pagina di presentazione della funzionalità Y **seguendo lo stile pagine web**"
> "Scrivi un saggio su Z **con lo stile saggio filosofico**"

Claude leggerà `base/SKILL.md` + il `SKILL.md` dello stile indicato prima di iniziare a scrivere.

---

## Cosa può fare Claude

### ✅ observe.py — completamente delegabile

Claude può eseguire tutti i comandi di `observe.py` direttamente dalla chat:

| Operazione | Come chiederla |
|---|---|
| Registrare una bozza | "registra la bozza `testi/articolo.md` come saggio filosofico" |
| Registrare la versione finale | "registra la versione finale `testi/articolo.md`" |
| Vedere le bozze in attesa | "mostrami le bozze in attesa di abbinamento" |
| Vedere le statistiche di uno stile | "mostrami le statistiche del saggio filosofico" |

### ✅ Analisi e aggiornamento SKILL.md — gestito direttamente da Claude

Claude può leggere i log di uno stile, analizzare le differenze sistematiche tra bozze e versioni finali, e aggiornare il `SKILL.md` corrispondente — senza script esterni.

> "Analizza i log della critica culturale e aggiorna il suo SKILL.md"
> "Aggiorna lo stile base con le regole comuni che emergono dai log"

---

## Convenzione fondamentale sui log

Ogni stile ha la propria cartella `logs/` **dentro la sua directory**. Questo garantisce la separazione tra i cicli di apprendimento e la persistenza tra le sessioni.

| Stile | Directory dei log |
|---|---|
| Base | `base/logs/` |
| Saggio filosofico | `saggio-filosofico/logs/` |
| Critica culturale | `critica-culturale/logs/` |
| Pagine web | `pagine-web/logs/` |

Internamente Claude usa sempre `--log-dir ./<stile>/logs` quando esegue gli script.

---

## Flusso di lavoro completo

### 1. Chiedi la bozza specificando lo stile

> "Scrivi una recensione di *Tre colori — Film Blu* di Kieślowski usando lo stile critica culturale e salvala in `testi/kielowski-blu.md`"

Claude legge `base/SKILL.md` + `critica-culturale/SKILL.md` e produce il testo.

### 2. Chiedi a Claude di registrare la bozza

> "Registra la bozza `testi/kielowski-blu.md` come critica culturale"

Claude esegue:
```bash
python3 scripts/observe.py record-original testi/kielowski-blu.md \
  --log-dir ./critica-culturale/logs \
  --content-type critica-cinema
```
e ti restituisce l'hash (es. `a3f7c2b1`).

### 3. Correggi il testo

Modifica il file come preferisci — direttamente, su un editor esterno, come vuoi. Salva la versione definitiva nello stesso file o in uno nuovo.

### 4. Chiedi a Claude di registrare la versione finale

> "Registra la versione finale `testi/kielowski-blu.md`"

Claude abbina automaticamente all'ultima bozza in attesa per quello stile.

### 5. Aggiorna lo SKILL.md (periodicamente)

Dopo 2-3 sessioni accumulate su uno stile:

> "Analizza i log della critica culturale e aggiorna il suo SKILL.md con le nuove regole"

Claude legge i log, estrae le differenze sistematiche, fa un backup del `SKILL.md` attuale e lo aggiorna.

Per aggiornare anche le regole comuni:

> "Analizza tutti i log e aggiorna base/SKILL.md con le regole che si ripetono in tutti gli stili"

---

## Note pratiche

**Non serve ricordare gli hash.** Finché hai una sola bozza in attesa per quello stile, Claude la abbina automaticamente.

**I log sono separati per stile.** Le correzioni su un saggio filosofico non influenzano l'apprendimento della critica culturale.

**Backup automatici.** Prima di ogni aggiornamento, Claude salva una copia del `SKILL.md` che sta per modificare in `<stile>/logs/backups/`. Per tornare indietro: "ripristina la versione precedente di critica-culturale/SKILL.md".

**Lo stile base si aggiorna raramente.** Conviene aggiornarlo solo dopo aver accumulato molte sessioni su più stili, cercando le regole che emergono ovunque.

---

## Frasi di riferimento rapido

```
"Scrivi [testo] usando lo stile [saggio-filosofico | critica-culturale | pagine-web]"
"Registra la bozza [nomefile] come [stile]"
"Registra la versione finale [nomefile]"
"Mostrami le bozze in attesa"
"Mostrami le statistiche di [stile]"
"Analizza i log di [stile] e aggiorna il suo SKILL.md"
"Analizza tutti i log e aggiorna base/SKILL.md"
"Ripristina la versione precedente di [stile]/SKILL.md"
```
