# Revisioni — gioco-libero-come-incontro-del-bambino-con-il-possibile × clinico-pediatrico

Storia delle decisioni episodiche per questo tema × dominio.

---

## 2026-05-23 — Pilota del modulo F3-SIT (Fase 4)

Prima esecuzione completa del modulo **F3-SIT** (Repertorio Situazionale di Micro-mediazioni) su un dispositivo F3 reale. Scopo: validare la tassonomia delle 9 famiglie e gli schemi prima di considerarli stabili. Riferimenti: `Piano di attuazione F3-SIT.md` (Fase 4), `D9-pipeline-f3-sit.md`.

### Input

Dispositivo F3 r3 completo: `nodo-funzione-v1.json`, `micro-dispositivo-v1.json`, `stress-test-v1.json`, `output-tipo-clinico-v2.json`. **`coerenza-v1.json` (F3 step 4) assente** nella cartella del tema: lo step 4 di F3-SIT ha registrato `f3_coherence_status: null`.

### Esecuzione

| Step | Output | Esito |
|---|---|---|
| f3_sit_step_1 | `sit/sit-famiglie-v1.json` | 5 famiglie selezionate (F3-SIT-1, 2, 4 alta; 6, 8 media), 4 escluse. Verifica umana: **approvato** dal ricercatore. |
| f3_sit_step_2 | `sit/sit-micro-mediazioni-v1.json` | 14 item (F3-SIT-1: 5; F3-SIT-2: 5; F3-SIT-4: 4). |
| f3_sit_step_3 | `sit/sit-formati-v1.json` | 5 training_outputs (3 vignette F3-SIT-6; 2 linee guida F3-SIT-8). |
| f3_sit_step_4 | `sit/sit-repertorio-v1.json` | 19 item verificati C1–C8; `methodological_status: validato`. |

Tutti gli output sono validati contro i rispettivi JSON Schema Draft-07.

### Valutazione della tassonomia — la tassonomia regge

Le 9 famiglie sono risultate workable; la pipeline ha prodotto materiale coerente, tracciabile e non prescrittivo. Osservazioni puntuali:

1. **Connessione B confermata come punto di forza.** I 5 casi tipologici dello stress test si sono convertiti 1:1 nelle 5 casistiche F3-SIT-1, senza inventarne di nuovi. È il meccanismo più solido del modulo.
2. **F3-SIT-4 (schede di atteggiamento) è la famiglia più pertinente** per un dispositivo a funzione `proteggere`: i marcatori di qualità performativa introdotti dalla correzione dello stress test (ma1/ma3) sono confluiti direttamente nelle schede.
3. **Distinzione F3-SIT-2 vs F3-SIT-4 netta.** Lo schema dello step 2 ha retto: gli item di atteggiamento hanno `possible_phrase: null`, quelli di frase la valorizzano. La flessibilità del campo `micro_mediation` è adeguata.
4. **Selezione fortemente domino-dipendente.** In un dominio clinico-professionale sono state escluse 4 famiglie su 9 (F3-SIT-3 caregiver, 5 micro-scenari, 7 storyboard, 9 prompt AI). Conferma che la tassonomia è ampia e che il meccanismo di selezione dello step 1 è essenziale.

### Candidati di revisione per la v2 (non applicati ora)

- **F3-SIT-1 (casistiche) calza lo schema dello step 2 in modo forzato.** Una casistica descrive una configurazione da riconoscere, non una mediazione che l'adulto compie: i campi `possible_phrase` / `alternative_phrase` / `gesture_or_timing` risultano sempre `null`. Valutare per la v2 una sotto-forma dedicata per F3-SIT-1, oppure rendere `micro_mediation` opzionale per quella famiglia.
- **Confine sottile F3-SIT-1 ↔ F3-SIT-6.** La vignetta formativa è, di fatto, una casistica arricchita di lettura ingenua e domande di discussione. Chiarire la distinzione nelle descrizioni di `f3-sit-famiglie.json`.
- **`configurational_basis` ripetuto identico in ogni item.** Per un singolo dispositivo i campi di tracciabilità sono costanti. Valutare di issarli a livello di `results[0]` con riferimento per-item (ottimizzazione di schema).
- **F3-SIT-5 confermata come la famiglia più ridondante** (sovrapposizione con micro-dispositivo e con F3-SIT-1): in fase pilota la sua esclusione non ha prodotto lacune.
- **Il percorso negativo della checklist non è stato esercitato:** tutti i 19 item sono `validato`. La capacità discriminante di C1–C8 (`richiede_revisione` / `non_pubblicabile`) andrà testata su un caso che la solleciti.

### Pubblicabilità

`sit-repertorio-v1.json` → `public_site: false`, `professional_training: true`. La pubblicazione sul sito è sospesa perché manca la verifica di coerenza F3 (`coerenza-v1.json` assente) e il dispositivo sorgente ha verdetto stress test `fragile` poi corretto. Il repertorio è raccomandato per formazione e supervisione professionale.

### Pendenza segnalata

`coerenza-v1.json` (F3 step 4) non è presente nella cartella del tema: o lo step 4 di F3 non è stato eseguito, o l'output non è stato salvato. Da chiarire prima di un eventuale uso pubblicabile del repertorio.
