# 🔹 1. DOVE SERVONO INPUT

> **Aggiornamento r3 (2026-05)**: con la riduzione della pipeline F3 da 10 a 5 step (vedi `webapp-hcaire/specifiche/D7-pipeline-f3-redesign.md`), i punti di input esterno F3 si riposizionano. Lo step di scelta del tema (atto/fenomeno) si sposta interamente nell'archivio temi (la pipeline F2 inizia da step 2 lavorando su un tema *già selezionato*).

Non tutti gli step richiedono input.
Il metodo funziona perché **pochi punti sono vincolati dall'esterno**, il resto è trasformazione.

## ✔ PUNTI DI INPUT OBBLIGATI

### 🔸 ARCHIVIO TEMI — promozione del tema

```text
Scelta del tema (atto / fenomeno) e promozione
```

Esempio:

* pointing precoce
* richiesta di aiuto

👉 Questo definisce **l'oggetto ontologico**.
Avviene **fuori dalla pipeline** (nell'archivio temi). La pipeline F2 inizia da step 2 lavorando su un tema *già selezionato e promosso*.

---

### 🔸 F3 — STEP 1 (Nodo dominante e funzione)

```text
Scelta del dominio / contesto
```

Esempio:

* clinico (neurosviluppo, ambulatoriale 9-24 mesi)
* educativo (nido, scuola dell'infanzia)
* formazione (aula formativa pediatri)
* politiche

👉 Questo definisce **il vincolo di realtà** del dispositivo.
Per ciascun dominio si esegue una pipeline F3 dedicata, producendo un dispositivo contestualizzato.

---

## 🔹 PUNTI DI INPUT FACOLTATIVI (ma strategici)

### 🔸 F3 — STEP 3 (Stress test)

```text
Casi reali del dominio forniti dal ricercatore
```

I casi forniti dal ricercatore che conosce il dominio sono più forti dei casi costruiti dall'agente in autonomia: riflettono varianti limite osservate nella pratica e costruiscono ambiguità reali. Se non forniti, l'agente costruisce 5 casi in autonomia (test plausibile ma generico).

Questo è input perché:

```text
la qualità del test dipende da quanto "forzi" il modello
```

---

## 🔹 TUTTO IL RESTO

```text
NON richiede input esterno
```

Perché:

* deve emergere dalla struttura
* se lo guidi troppo → rompi il metodo

Gli step F3 step 2 (Micro-dispositivo), step 4 (Verifica di coerenza F3), step 5 (Audit metodologico opzionale) non richiedono input esterni: lavorano su output già prodotti dalla pipeline.
Gli step F2 step 2a (Nodi trasversali), 4b (CE Prototipica), 6 (Output-tipo vuoto) non richiedono input esterni.

---

# 🔹 RIASSUNTO OPERATIVO

```text
INPUT OBBLIGATI:
1. ARCHIVIO TEMI → tema (promozione, fuori pipeline)
2. F3 STEP 1     → dominio/contesto (uno per ciascun dispositivo F3)

INPUT FACOLTATIVI MA RACCOMANDATI:
3. F3 STEP 3 → casi reali del dominio per stress test ancorato

STEP SENZA INPUT ESTERNO (automatici):
• F2 STEP 2 → rilevanza strutturale (lavora sul tema selezionato)
• F2 STEP 2a → verifica nodi canonici N1-N7
• F2 STEP 3 → verifica strutturale
• F2 STEP 4 → micro-matrice
• F2 STEP 4b → CE Prototipica
• F2 STEP 5 → output family
• F2 STEP 6 → output-tipo vuoto / passaporto del tema
• F3 STEP 2 → micro-dispositivo
• F3 STEP 4 → verifica di coerenza F3
• F3 STEP 5 → audit metodologico (opzionale)
```

👉 Questo è un punto forte del metodo:

```text
pochi input, alta generatività
```

**r3 vs r2**: gli input obbligatori passano da 3 a 2; i facoltativi da 2 a 1. La rimozione degli step F3 sul "trasferimento a un nuovo tema" (vecchi step 7-9) ha eliminato i loro input esterni (contesto target, livello di specificità). La logica di trasferimento è ora distribuita: ogni nuovo tema ha una sua pipeline F2+F3 dedicata, ogni nuovo contesto ha la sua pipeline F3 sul tema già verificato.

