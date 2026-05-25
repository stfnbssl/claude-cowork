# Verifica — F3-SIT Step 1 (Selezione delle famiglie situazionali)

Questa verifica produce una **diagnosi**, non un'approvazione automatica. Orienta la decisione del ricercatore: `approvato` / `richiede_correzione`. È l'unico punto di verifica umana obbligatoria del modulo F3-SIT — qui si decide la destinazione comunicativa di tutto il materiale che verrà prodotto.

Applicare prima di procedere a `f3_sit_step_2`.

---

## Controlli

### V1 — Ancoraggio al dispositivo validato

Il `device_reference` riporta nodo dominante, funzione, campo bersaglio e forme U1–U6 effettivamente presi dagli output F3 (`nodo-funzione`, `micro-dispositivo`)? La selezione è motivata a partire dalla configurazione letta, non dal tema in generale?

→ Se la selezione sembra dedotta dall'argomento e non dal dispositivo: `richiede_correzione`.

### V2 — Pertinenza reale delle famiglie selezionate

Ogni famiglia in `selected_families` ha un destinatario reale nel dominio scelto e una `reason` che spiega la pertinenza *in questo dominio*? Una motivazione generica ("è utile per la formazione") non basta.

→ Verificare in particolare che non siano state selezionate famiglie narrative (vignette, storyboard, prompt AI) per domini che non producono materiali comunicativi (es. supervisione, politiche), se non con una ragione esplicita.

### V3 — Selezione che è una scelta

Il numero di famiglie selezionate riflette una scelta? Selezionare 8–9 famiglie su 9 è quasi sempre un segnale che la selezione non ha discriminato. Selezionarne 0 contraddice l'attivazione del modulo.

→ Atteso, in genere: 2–5 famiglie selezionate.

### V4 — Coerenza con la funzione del dispositivo

Le famiglie selezionate sono coerenti con la funzione del dispositivo (`stabilizzare` / `ampliare` / `mediare` / `proteggere`)? Esempio: una funzione `proteggere` raramente ha come priorità alta un repertorio ampio di prompt per AI generativa.

### V5 — Famiglie escluse tracciate

Le famiglie non selezionate sono in `excluded_families` con motivazione? L'esclusione deve essere esplicita e ragionata, non silenziosa.

### V6 — Flag narrativo corretto

`narrative_families_selected` è coerente con le famiglie effettivamente selezionate (true se e solo se è presente almeno una tra F3-SIT-6, 7, 8, 9)? Da questo flag dipende l'esecuzione o lo skip di `f3_sit_step_3`.

### V7 — Destinazione d'uso

Se il ricercatore ha fornito `destinazione_uso`, la selezione ne tiene conto (priorità e destinatari allineati)? Se non l'ha fornito, la selezione resta difendibile sulla sola base degli input pipeline?

---

## Esito

| Esito | Quando |
|---|---|
| `approvato` | V1–V7 soddisfatti; eventuali riserve minori annotate per gli step successivi |
| `richiede_correzione` | Fallisce V1, V2 o V3 (ancoraggio, pertinenza, o assenza di scelta), oppure V6 (flag incoerente) |

In caso di `richiede_correzione`, indicare quali famiglie rivedere e perché. La correzione rilancia `f3_sit_step_1` con il feedback, non prosegue al passo successivo.
