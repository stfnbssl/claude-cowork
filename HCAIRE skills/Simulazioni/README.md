# CARTELLA SIMULAZIONI HCAIRE

Questa cartella raccoglie le simulazioni del processo HCAIRE completo:
dalla traccia all'output finale, passando per il Motore di lettura della traccia (Bartleby).

---

## Struttura di ogni simulazione

Ogni file documenta:

1. **Traccia originale** — input grezzo così com'è
2. **Confronto preventivo** — cosa produrrebbe un sistema standard (per evidenziare la differenza)
3. **Motore A→F** — il processo completo:
   - A: Riformulazione della traccia
   - B: Analisi multidimensionale
   - C: Nodi critici
   - D: Integrazione con il modello
   - E: Traduzione verso l'output
   - F: Verifica qualità
4. **Output finale** — il testo destinato all'utente
5. **Note per l'evoluzione** — varianti da testare, domande aperte, margini di miglioramento

---

## Simulazioni presenti

| File | Traccia | Ambito | Nodi principali | Stato |
|------|---------|--------|-----------------|-------|
| Simulazione-01-T-G03.md | Bambino 14m che gioca da solo | Genitoriale | Relazione, Apertura/chiusura, Campo intenzionale | Prima versione |

---

## Come usare questa cartella

- **Per testare nuove tracce:** aggiungere un file seguendo la struttura standard
- **Per migliorare le simulazioni esistenti:** annotare direttamente nel file i punti da rivedere nella sezione "Note per l'evoluzione"
- **Per validare con esperti:** le simulazioni sono pensate per essere mostrate a pediatri, educatori, clinici e raccolti i loro feedback
- **Per addestrare il sistema:** le simulazioni sono esempi di come il Motore dovrebbe ragionare — possono essere usate come few-shot examples

---

## Criteri per scegliere le prossime tracce da simulare

Priorità a tracce che:
- Testano domini diversi (prossima: clinica o pedagogica)
- Testano il limite del modello (tracce con dati molto scarsi o ambigui)
- Testano il passaggio a output diversi (policy brief, nota clinica, guida per operatori)
- Sono state suggerite da professionisti del campo
