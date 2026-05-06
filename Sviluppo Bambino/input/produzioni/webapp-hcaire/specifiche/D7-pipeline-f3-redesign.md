# D7 — Pipeline F3 redesign — migrazione per Claude Code

> **Destinatario**: Claude Code — leggere D1, D2, D4 (per il contesto orchestrazione/persistenza). Questo documento istruisce la migrazione della **pipeline F3** da 10 step (+ sub-step 6B/6C) a **5 step** (+ 1 opzionale).
>
> **Stato della pipeline F2**: invariata. Solo `f2_step_1` riceve un'annotazione informativa (vedi §4.4).
>
> **Cosa sostituisce/modifica**:
> - sostituisce integralmente i CLAUDE.md degli step F3 in `produzioni/`
> - aggiorna `pipeline-step-config.json` (rimossi 11 step F3 vecchi, aggiunti 5 nuovi)
> - aggiorna `produzioni/CLAUDE.md` (sezione F3) e `Pipeline-inputs.md`
> - tocca D5b in alcuni punti (mapping step UI → nuova lista; valore di alcune route)
> - **non** richiede modifiche al data layer di D5 (hook, service, polling/SSE)
>
> **Migrazione dati esistenti**: nessuna. Le esecuzioni precedenti F3 erano prove tecniche e vanno abbandonate (conferma del ricercatore). Nessuna conversione di output JSON storici è richiesta.

---

## 1. Sintesi della modifica

### 1.1 Perché ridurre la pipeline F3

Il confronto tra la pipeline F3 attuale e la metodologia di riferimento (`HCAIRE Slides/context/metodo/f3-strumenti-operativi.md`) ha evidenziato tre problemi:

1. **Dimensione sproporzionata**: 10 step (+ 6B/6C) contro i 3 nominati dalla metodologia (Nodo dominante → Funzione → Micro-dispositivo).
2. **Mancanza dei passaggi metodologici espliciti**: nessuno step F3 della pipeline tecnica identificava il **nodo dominante** né la **funzione dell'intervento** (4 categorie chiuse: stabilizzare/ampliare/mediare/proteggere).
3. **Stratificazioni di controllo non previste dal metodo**: 3 stress test paralleli, audit di un audit, frammentazione del proxy in 3 step, 4 step dedicati al "trasferimento a un nuovo tema" (caso d'uso non previsto dalla metodologia).

Decisioni del ricercatore (2026-05):

- ✅ Audit metodologico mantenuto come **ultimo step opzionale**.
- ❌ Step di trasferimento (7-9 vecchi) **abbandonati**.
- ❌ Nodo dominante e quattro funzioni vanno **gestiti esplicitamente** (era un'assenza, non una scelta).
- ❌ Esecuzioni precedenti **abbandonate** (erano prove tecniche).

### 1.2 La nuova pipeline F3 a 5 step

| ID | Label | Funzione | Verifica | Skip |
|---|---|---|---|---|
| `f3_step_1` | Nodo dominante e funzione | Identifica nodo dominante della CE per il dominio scelto + sceglie 1 di 4 funzioni | sì | no |
| `f3_step_2` | Micro-dispositivo di campo | Costruisce il dispositivo nel template a 7 campi della metodologia + classificazione U1-U6 + condizioni di non-applicabilità | sì | no |
| `f3_step_3` | Stress test e correzione | 5 casi tipologici integrati (incl. quasi indistinguibile) + correzione condizionale del dispositivo | sì | no |
| `f3_step_4` | Verifica di coerenza F3 | Checklist 10 controlli (5 di sez. 2.7 + 4 di sez. 5.4 + 1 di sez. 5.6) — verdetto: valido / richiede_revisione / fuori_modello | no¹ | no |
| `f3_step_5` | Audit metodologico (opzionale) | 8 controlli sulla qualità di esecuzione della pipeline F3 da parte degli agenti AI | no | **sì** |

¹ Lo step 4 *è* la verifica: non ha senso applicargli un altro layer di verifica.

---

## 2. Mapping vecchio → nuovo

### 2.1 Dove finisce ogni vecchio step F3

| Vecchio | Cosa diventa | Note |
|---|---|---|
| `f3_step_1` (Lettura configurazionale) | parzialmente assorbito in **nuovo `f3_step_1`** (Nodo+Funzione) e **nuovo `f3_step_2`** (Micro-dispositivo) | Il nuovo step 1 esplicita le scelte decisionali (nodo, funzione) che il vecchio mascherava in una costruzione monolitica |
| `f3_step_2` (Stress test) | assorbito in **nuovo `f3_step_3`** | I 5 casi tipologici sono identici come funzione |
| `f3_step_3` (Correzione strutturale) | assorbito in **nuovo `f3_step_3`** come correzione condizionale | La correzione si esegue solo se i breaking point sono strutturali |
| `f3_step_4` (Test di indistinguibilità) | assorbito in **nuovo `f3_step_3`** come tipologia `configurazione_apparente_indistinguibile` (caso 5/5) | Niente più step dedicato |
| `f3_step_5` (Audit) | assorbito in **nuovo `f3_step_5`** ma generalizzato a tutta la pipeline F3 (non solo step 4) e reso opzionale | I controlli D1-D11 sono stati rifusi in 8 controlli (A1-A8) |
| `f3_step_6` (Stabilizzazione proxy) | assorbito in **nuovo `f3_step_2`** (il proxy è proprietà del dispositivo) | Non più entità con pipeline propria |
| `f3_step_6b` (Proxy forma operativa) | assorbito in **nuovo `f3_step_2`** come `non_applicability` + in **nuovo `f3_step_4`** come C10 | Auto-limitazione è criterio di coerenza, non sub-step |
| `f3_step_6c` (Integrazione proxy) | rimosso | Non c'è più separazione tra "proxy" e "dispositivo" |
| `f3_step_7` (Trasferibilità) | **rimosso** | Il "trasferimento" non è step F3 secondo metodo |
| `f3_step_8` (Adattamento strutturale) | **rimosso** | Idem — nuovo tema = nuova pipeline F2+F3 |
| `f3_step_9` (Dispositivo completo) | **rimosso** | Il dispositivo *è già* prodotto da nuovo `f3_step_2` |
| `f3_step_10` (Stress test dispositivo) | assorbito in **nuovo `f3_step_3`** | Era duplicato di `f3_step_2` vecchio |

### 2.2 Da dove viene ogni nuovo step F3

| Nuovo | Deriva da | Aggiunto |
|---|---|---|
| `f3_step_1` (Nodo+Funzione) | nessun analogo vecchio (era un'assenza nel metodo) | nuovo |
| `f3_step_2` (Micro-dispositivo) | parti riformulate del vecchio step 1 + assorbe step 6/6B nelle proprietà del dispositivo | template a 7 campi + U1-U6 + non_applicability |
| `f3_step_3` (Stress test) | accorpa vecchi step 2, 3, 4, 10 | unica esecuzione |
| `f3_step_4` (Coerenza F3) | nessun analogo vecchio | nuovo: 10 controlli normativi del metodo |
| `f3_step_5` (Audit) | versione generalizzata e opzionale del vecchio step 5 | resa opzionale, applicata a tutta la pipeline |

---

## 3. Modifiche ai file del filesystem `produzioni/`

### 3.1 Cartelle da rimuovere

⚠ Le cartelle che contengono i CLAUDE.md, gli schemi e i `verifica.md` dei vecchi step F3 vanno **rimosse fisicamente**. Claude Code può eseguire la rimozione tramite `mcp__workspace__bash` (comando `rm -rf`).

```
input/produzioni/f3-step-1-dispositivo-lettura/
input/produzioni/f3-step-2-stress-test/                 ← attenzione: non confondere con la NUOVA cartella f3-step-3-stress-test/
input/produzioni/f3-step-3-correzione-strutturale/
input/produzioni/f3-step-4-indistinguibilità/
input/produzioni/f3-step-5-audit/                       ← attenzione: non confondere con la NUOVA cartella f3-step-5-audit-metodologico/
input/produzioni/f3-step-6-stabilizzazione-proxy/
input/produzioni/f3-step-7-trasferibilità-dispositivo/
input/produzioni/f3-step-8-adattamento-strutturale/
input/produzioni/f3-step-9-dispositivo-completo/
input/produzioni/f3-step-10-stress-test-dispositivo/
```

### 3.2 Cartelle nuove (già create)

Già presenti dopo questa migrazione:

```
input/produzioni/f3-step-1-nodo-funzione/
  CLAUDE.md
  nodo-funzione-schema.json

input/produzioni/f3-step-2-micro-dispositivo/
  CLAUDE.md
  micro-dispositivo-schema.json

input/produzioni/f3-step-3-stress-test/
  CLAUDE.md
  stress-test-schema.json

input/produzioni/f3-step-4-coerenza/
  CLAUDE.md
  coerenza-schema.json

input/produzioni/f3-step-5-audit-metodologico/
  CLAUDE.md
  audit-schema.json
```

### 3.3 File aggiornati

```
input/produzioni/CLAUDE.md                          ← sezione "F3 — Step per step" riscritta
input/produzioni/Pipeline-inputs.md                 ← input esterni F3 aggiornati
input/produzioni/webapp-hcaire/pipeline-step-config.json ← rimossi 11 vecchi step F3, aggiunti 5 nuovi
```

### 3.4 Output di sessioni precedenti

I file in `output/produzioni/temi/[nome-tema]/` prodotti dalle vecchie esecuzioni F3 sono **prove tecniche da abbandonare**. Possono essere:

- Cancellati (raccomandato per mantenere pulizia).
- Spostati in una cartella `output/produzioni/temi/_archivio-prove-tecniche-pre-r3/` se si vuole conservarli per riferimento storico.

Non sono richieste conversioni o migrazioni di dati.

---

## 4. Modifiche al codice — backend orchestrazione

### 4.1 `pipeline-step-config.json`

✅ **Già aggiornato** in questa migrazione. Ora contiene:

- `f2_step_1` con `excluded_from_pipeline_ui: true` e `_note` esplicativa (rinviato all'archivio temi — vedi D5b r2 §1.4)
- F2 step 2 → step 6: invariati (a parte `f2_step_6.blocks` che ora punta direttamente a `f3_step_1` senza decisione umana intermedia)
- F3: 5 nuovi step (`f3_step_1` … `f3_step_5`)
- Nessuna entry residua per i vecchi step F3 (`f3_step_6/6b/6c/7/8/9/10`) né `f3_step_3_or_6c` né overrides di `f3_step_6b`
- `_version` bumped a `"3.0"`

### 4.2 `evaluateStepEnablement` (D4 §9)

La funzione `evaluateStepEnablement` aveva una logica speciale per il caso `f3_step_3_or_6c` (biforcazione del grafo: step 6c se presente, altrimenti step 3). **Questa logica va rimossa** dato che `f3_step_6c` non esiste più nel modello r3.

Codice attuale (da rimuovere):
```typescript
// Esempio della logica condizionale che NON è più necessaria
if (stepId === 'f3_step_7' || stepId === 'f3_step_9') {
  const f3_step_6c = context.step_states['f3_step_6c'];
  const sourceStep = f3_step_6c?.status === 'verificato' ? 'f3_step_6c' : 'f3_step_3';
  // ...
}
```

Sostituire con il modello lineare semplice: ogni step F3 dipende solo dai propri predecessori dichiarati in `inputs_pipeline`. Nessuna biforcazione.

### 4.3 Override di `f3_step_6b`

L'overload `overrides: ["operative_proxies", "observability_requirements", "non_classifiability_rules"]` di `f3_step_6b` (D4 §9, "punto critico — override step 6b") **non è più applicabile**. Rimuovere il branch di codice che, alla verifica di `f3_step_6b`, aggiornava `canonical_device` del context con i nuovi proxy.

Nel modello r3, il dispositivo è prodotto e corretto entro `f3_step_3` e non subisce più sostituzioni ex post. La nozione di `canonical_device` resta ma viene aggiornata con un'unica scrittura alla verifica di `f3_step_4`.

### 4.4 Endpoint che fanno riferimento esplicito a vecchi step

Cercare nei controllori pipeline (`server/src/controllers/pipelineController.ts`, `server/src/services/pipelineService.ts`) ogni riferimento a:

- `f3_step_6`, `f3_step_6b`, `f3_step_6c`
- `f3_step_7`, `f3_step_8`, `f3_step_9`, `f3_step_10`
- `f3_step_3_or_6c`
- `lettura-configurazionale` (vecchio output_prefix di step 1)
- `correzione-strutturale` (vecchio output_prefix di step 3)
- `stabilizzazione-proxy` (vecchi step 6/6b/6c)
- `trasferibilità` (vecchio step 7)
- `adattamento-strutturale` (vecchio step 8)
- `dispositivo` (vecchio step 9 — attenzione: termine generico, contestualizzare)
- `stress-test-dispositivo` (vecchio step 10)

Tutti vanno aggiornati o rimossi.

### 4.5 `PromptComposer` (D6 §3) — server locale Cowork

Il `PromptComposer` carica il `CLAUDE.md` dello step da una mappa `STEP_CLAUDE_FILE_MAP` (D6 §1). **La mappa va aggiornata**:

| Step ID | Path nuovo (relativo a `input/produzioni/`) |
|---|---|
| `f3_step_1` | `f3-step-1-nodo-funzione/CLAUDE.md` |
| `f3_step_2` | `f3-step-2-micro-dispositivo/CLAUDE.md` |
| `f3_step_3` | `f3-step-3-stress-test/CLAUDE.md` |
| `f3_step_4` | `f3-step-4-coerenza/CLAUDE.md` |
| `f3_step_5` | `f3-step-5-audit-metodologico/CLAUDE.md` |

Rimuovere dalla mappa tutti i path dei vecchi step F3.

Inoltre il `PromptComposer` aveva una gestione speciale del `MICRO CASI` per `f3_step_10` (D6 §7) e una gestione del `CLAUDE-B.md` per `f3_step_6` (variante da concatenare). **Entrambe le gestioni speciali vanno rimosse**: il modello r3 non ha più step con CLAUDE alternativo né il blocco MICRO CASI separato.

Lo step `f3_step_3` ha un input esterno facoltativo `casi_dominio` (casi reali del dominio forniti dal ricercatore). Quando presenti, vanno passati al prompt come blocco di input strutturato (sezione `[Blocco 2 — input dati]` di D3 §12). Nessuna gestione speciale: pattern uniforme con gli altri input esterni.

### 4.6 Schemi MongoDB (D2)

Nessuna modifica strutturale richiesta. La collezione `pipeline_step_executions` continua a indicizzare per `step_id`. I documenti delle vecchie esecuzioni con `step_id` ∈ {`f3_step_6`, `f3_step_6b`, `f3_step_6c`, `f3_step_7`, `f3_step_8`, `f3_step_9`, `f3_step_10`} possono essere lasciati in stato terminale (non saranno più referenziati) oppure rimossi con uno script di pulizia.

Per il context dei temi/dispositivi attivi (collezioni `temi`/`dispositivi_f3` nel modello r2 di D5b), le entry `step_states` per i vecchi step F3 vanno rimosse al primo refresh, oppure ignorate dal frontend (filtrate sull'array `stepConfig.steps` aggiornato).

---

## 5. Modifiche al frontend (D5b r2)

### 5.1 Sezioni di D5b da aggiornare

In `webapp-hcaire/specifiche/D5b-laboratorio-workbench.md`:

**§5.2 — TimelineRail vista Dispositivo (mockup F3)**

Il mockup attuale elenca:
```
●  f3_step_1 — Lettura
●  f3_step_2 — Stress test
●  f3_step_3 — Correzione        ▶ ◎
○  f3_step_4 — Indistinguibilità
○  f3_step_5 — Audit
●  f3_step_6 — Stabilizzazione
│  ●  f3_step_6b — Forma operativa
│  ●  f3_step_6c — Integrazione
○  f3_step_7 — Trasferibilità    ✎
○  f3_step_8 — Adattamento
○  f3_step_9 — Dispositivo completo
○  f3_step_10 — Stress test disp. ✎
```

**Va sostituito con**:
```
●  f3_step_1 — Nodo dominante e funzione   ✎
●  f3_step_2 — Micro-dispositivo
●  f3_step_3 — Stress test e correzione    ✎
●  f3_step_4 — Verifica di coerenza F3
○  f3_step_5 — Audit metodologico (opz.)
```

(I glifi `✎` indicano gli step con input esterni: step 1 obbligatorio, step 3 facoltativo.)

**§5.3 sub-step annidati**

Rimuovere il riferimento a `2a, 4b in F2; 6b, 6c in F3`. Lasciare solo `2a, 4b in F2`. La timeline F3 non ha più sub-step annidati.

**§5.7 Props `TimelineRailProps`**

Nessuna modifica strutturale ma aggiornare il commento/example dei `steps: StepConfig[]` per chiarire che ora sono 5 in F3.

**§9.2 `HumanDecisionDialog` — varianti attive**

Già aggiornato in D5b r2 a sola variante `step7_context_selection`. Tuttavia: **questa variante non esiste più** nel modello r3 della pipeline F3 (lo step 7 vecchio è eliminato; il contesto è raccolto come input esterno standard di `f3_step_1` nuovo).

Riformulare D5b §9.2 come:

> **Nessuna variante attiva nel modello r3+pipeline-r3.**
>
> Tutte le decisioni umane nominate da D5 originale (`f2_to_f3_tema_selection`, `step7_context_selection`) sono state assorbite altrove:
> - selezione tema → archivio temi (atto di promozione)
> - scelta del contesto/dominio → input esterno obbligatorio di `f3_step_1` (tramite `ExternalInputPanel` inline, non modale)
>
> Il componente `HumanDecisionDialog` può essere **rimosso** dall'implementazione, insieme al `PendingDecisionBanner` (§9.3) — non c'è più nessun caso d'uso nella pipeline F2+F3 corrente. Mantenerli solo come scaffolding se si prevede l'introduzione futura di altre decisioni strutturali.

> **Conseguenza per D5b §3.3 e §3.5**: l'algoritmo del fronte attivo aveva `attende_decisione` come priorità #1. Con la rimozione di `HumanDecisionDialog`, questo stato non sarà più valorizzato. Il branch resta nel codice come no-op futuro, ma non si attiverà nei flussi attuali.

**§5.5 mapping stato → glifo + badge**

Lo stato `attende_decisione` resta nello schema MongoDB ma in pratica non sarà attivato dal modello r3+pipeline-r3. Mantenere il rendering per coerenza, eventualmente marcandolo `legacy`.

**§9.3 `PendingDecisionBanner`**

Rendere conditional su `pendingDecision !== null`. Nel modello r3+pipeline-r3 sarà sempre `null` per default. Stesso suggerimento di §9.2: mantenere come scaffolding, rimuovibile.

**§13 struttura file**

Rimuovere dal piano di implementazione:
- `HumanDecisionDialog.tsx` (commentare come *non più necessario, mantenere come scaffolding*)
- `PendingDecisionBanner.tsx` (idem)

**§19.7 criteri di accettazione**

I criteri su `HumanDecisionDialog` e `PendingDecisionBanner` decadono nei test funzionali ma rimangono come test di scaffolding (i componenti devono essere montabili, non eseguibili nel flusso reale).

### 5.2 `ExternalInputPanel` — renderer aggiornati

In D5b §13 (componenti `external-input-renderers/`):

| Renderer | Stato |
|---|---|
| `F3Step7InputRenderer.tsx` | **rinominare** in `F3Step1InputRenderer.tsx` (il form contesto/ambito ora è raccolto al primo step della pipeline F3) |
| `F3Step10InputRenderer.tsx` | **rinominare** in `F3Step3InputRenderer.tsx` (i casi reali del dominio sono raccolti allo step 3) |
| `GenericEnumInputRenderer` | rimuove i due usi (`severita_test` di vecchio step 6, `specificita_dispositivo` di vecchio step 8). Resta come componente generico riusabile (potrebbe non essere più usato nessuno step) |

Il payload del form `F3Step1InputRenderer`:

```typescript
{
  domain: 'clinico' | 'educativo' | 'formazione' | 'politiche';
  context_label: string;       // es. "ambulatoriale 9-24 mesi"
  researcher_notes?: string;   // opzionale
}
```

Il payload del form `F3Step3InputRenderer`:

```typescript
{
  // 5 casi narrativi (uno per case_type), tutti opzionali individualmente
  cases?: Array<{
    case_type: 'assenza_configurazione' | 'configurazione_parziale'
              | 'configurazione_distorta_chiudente' | 'configurazione_oscillante'
              | 'configurazione_apparente_indistinguibile';
    description: string;
  }>;
}
```

Il form mostra 5 sezioni espandibili (una per `case_type`). Il ricercatore può lasciare alcune sezioni vuote: l'agente integrerà i casi mancanti in autonomia. Contatore "N/5 casi forniti" in cima.

### 5.3 Mapping `EnrichedStepState.action` (D5 §2)

Resta invariato. La pipeline F3 ridotta usa lo stesso vocabolario di azioni.

### 5.4 `WorkbenchOutputPanel` — preview per tipo di step

In D5b §6.5, la tabella di mapping output → componente di preview va aggiornata:

| Step | Componente di preview |
|---|---|
| `f3_step_1` | JSON pretty-printed (no componente specifico) |
| `f3_step_2` | `MicroDispositivoViewer` (NUOVO — da implementare; mostra il template a 7 campi + U1-U6 + non_applicability) |
| `f3_step_3` | `StressTestDashboard` (riusato, ma riconfigurato sui 5 nuovi `case_type`) |
| `f3_step_4` | `CoerenzaChecklistViewer` (NUOVO — mostra i 10 controlli con esiti, evidenzia i critici falliti) |
| `f3_step_5` | `AuditViewer` (NUOVO — mostra gli 8 controlli e l'esito globale) |

I componenti `DeviceViewer`, `CorrectionsLog`, `DeviceLineage` esistenti **non sono più riusati** dalla pipeline F3 r3 perché non c'è più un "dispositivo configurazionale" a struttura ramificata. Restano in vita per le pagine read-only esistenti che mostrano produzioni storiche.

**Per la prima implementazione**: si può accettare il fallback "JSON pretty-printed" per tutti gli step F3 e introdurre i viewer specifici in una tappa successiva.

---

## 6. Cosa NON cambia

Per evitare malintesi:

- **Pipeline F2**: invariata. Tutti gli step F2 (1, 2, 2a, 3, 4, 4b, 5, 6) restano come da modello attuale, salvo l'annotazione `excluded_from_pipeline_ui` su `f2_step_1` (che era già prevista da D5b r2 per il modello a tre entità).
- **Output-tipo vuoto** (`f2_step_6`): è e resta l'input primario di F3. Nessuna modifica al suo schema.
- **Modello a tre entità (D5b r2)**: invariato. La pipeline F3 ridotta vive perfettamente dentro la nozione di *dispositivo F3 contestualizzato* del modello r2. Anzi, la riduzione la rinforza: una pipeline F3 = un dispositivo, fine. Nessuna ambiguità.
- **Hook, service, polling, SSE**: tutti invariati.
- **Schema MongoDB delle collezioni** `pipeline_contexts`, `pipeline_step_executions`, `pipeline_external_inputs`: nessuna modifica strutturale.
- **Protocollo Redis (D3)**: invariato. Cambia il contenuto dei prompt (perché cambiano i CLAUDE.md), non il protocollo.

---

## 7. Sequenza di rilascio consigliata

Per evitare di rompere ambienti che potrebbero essere stati esercitati con la pipeline vecchia.

**Tappa 1 — Backend e config (atomica)**

1. Aggiornare `pipeline-step-config.json` (✅ già fatto).
2. Aggiornare `evaluateStepEnablement` rimuovendo la biforcazione `f3_step_3_or_6c` e l'override `f3_step_6b`.
3. Aggiornare `STEP_CLAUDE_FILE_MAP` nel `PromptComposer` (server locale Cowork) con i 5 nuovi path.
4. Rimuovere logica speciale per `MICRO CASI` di vecchio `f3_step_10` e `CLAUDE-B.md` di vecchio `f3_step_6`.
5. Pulire script `scripts/sync-pipeline.mjs` se ha riferimenti hardcoded ai vecchi step F3.

**Tappa 2 — Filesystem (atomica)**

6. Eseguire `rm -rf` sulle 10 cartelle vecchie F3 in `input/produzioni/`.
7. Verificare che le 5 nuove cartelle in `input/produzioni/f3-step-*-*/` esistano e siano popolate (✅ già create).
8. Spostare/cancellare gli output di esecuzioni precedenti in `output/produzioni/temi/`.

**Tappa 3 — MongoDB (idempotente)**

9. Script di pulizia (opzionale) per rimuovere documenti `pipeline_step_executions` con `step_id` ∈ insieme dei vecchi F3 in stato non terminale (segnarli come `cancellato` con motivazione "migrazione r3"). I documenti in stato terminale possono essere lasciati.
10. Per i `pipeline_contexts` attivi, rimuovere le entry di `step_states` per i vecchi step F3.

**Tappa 4 — Frontend D5b**

11. Aggiornare il mockup di `TimelineRail` variante Dispositivo (§5.2 di D5b).
12. Riformulare/rimuovere `HumanDecisionDialog` e `PendingDecisionBanner` come da §5.1 di questo documento.
13. Rinominare i renderer external input (`F3Step7` → `F3Step1`; `F3Step10` → `F3Step3`).
14. Aggiornare il mapping output → preview component (§6.5 di D5b) — viewer specifici opzionali, fallback JSON sempre disponibile.

**Tappa 5 — Smoke test end-to-end**

15. Su un tema di prova: eseguire la pipeline completa F2 (step 2 → step 6) + F3 (step 1 → step 4), verificando che ogni step accetti e produca output validati dai nuovi schemi JSON.
16. Eseguire opzionalmente lo step 5 (audit) per verificare la pipeline integrale.
17. Su un tema con F2 verificata e dominio diverso: lanciare una seconda pipeline F3 (nuovo dispositivo contestualizzato) per verificare la relazione 1-N tema → dispositivi del modello r2.

---

## 8. Criteri di accettazione

### 8.1 Configurazione e backend

- [ ] `pipeline-step-config.json._version === "3.0"`
- [ ] `f2_step_1` ha `excluded_from_pipeline_ui: true`
- [ ] `f2_step_6.blocks === ["f3_step_1"]` (senza `[human_decision] →`)
- [ ] La sezione F3 contiene esattamente 5 step: `f3_step_1` … `f3_step_5`
- [ ] Nessun `f3_step_6/6b/6c/7/8/9/10` né `f3_step_3_or_6c` nel file
- [ ] `f3_step_5.can_skip === true` e `skip_condition` è valorizzato
- [ ] `evaluateStepEnablement` non ha più branch per `f3_step_3_or_6c`
- [ ] `STEP_CLAUDE_FILE_MAP` punta ai nuovi path

### 8.2 Filesystem `produzioni/`

- [ ] Le 5 nuove cartelle esistono e contengono `CLAUDE.md` + `*-schema.json`
- [ ] Le 10 vecchie cartelle F3 sono state rimosse
- [ ] `produzioni/CLAUDE.md` riflette la nuova lista F3
- [ ] `Pipeline-inputs.md` descrive i nuovi input esterni F3 (step 1 obbligatorio, step 3 facoltativo)

### 8.3 Esecuzione

- [ ] Lanciando `f3_step_1` da pipeline orchestrator, l'agente riceve il nuovo CLAUDE.md `f3-step-1-nodo-funzione/CLAUDE.md`
- [ ] L'output di `f3_step_1` è validato da `nodo-funzione-schema.json`
- [ ] L'input esterno obbligatorio di `f3_step_1` (dominio + context_label) è raccolto via `ExternalInputPanel` con renderer `F3Step1InputRenderer` (rinominato da `F3Step7InputRenderer`)
- [ ] La pipeline procede linearmente da step 1 a step 4 senza decisioni umane modali
- [ ] Lo step 5 può essere eseguito o saltato; se saltato, il dispositivo è considerato comunque finalizzato dopo lo step 4 verificato
- [ ] Una seconda pipeline F3 sullo stesso tema, con `domain` diverso, parte da step 1 con un'identità di dispositivo distinta (`(tema_id, contesto_id)` come da modello r2)

### 8.4 D5b allineato

- [ ] `TimelineRail` vista Dispositivo mostra 5 voci
- [ ] Il blocco "Pre-requisiti F2 ✓" funziona come specificato (collassabile, link a output F2)
- [ ] `HumanDecisionDialog` e `PendingDecisionBanner` non si attivano in nessun flusso normale
- [ ] La sezione `ContestualizzazioniSection` in `LaboratorioTemaPage` (D5b §6.7) mostra le card dei dispositivi F3 figli con avanzamento N/5 (non più N/10)

### 8.5 No-regressioni

- [ ] La pipeline F2 esegue identicamente come prima
- [ ] Le pagine read-only esistenti (`PipelineMap`, `DeviceOverview`) non sono toccate
- [ ] Gli utenti non admin non vedono cambiamenti

---

## 9. Domande aperte da chiarire prima dell'implementazione

Punti che potrebbero richiedere conferma del ricercatore o decisioni implementative:

1. **Componenti di preview per gli output F3 (D5b §6.5)**: la tabella in §5.4 di questo documento elenca componenti nuovi (`MicroDispositivoViewer`, `CoerenzaChecklistViewer`, `AuditViewer`). Possono essere posticipati a una tappa successiva? Per la prima migrazione il fallback "JSON pretty-printed" è sufficiente?

2. **Pulizia output di esecuzioni precedenti**: cancellazione completa o spostamento in `_archivio-prove-tecniche-pre-r3/`? La scelta è cosmetica ma vale la pena rendere esplicito.

3. **`HumanDecisionDialog` come scaffolding**: rimuovere completamente i componenti dalla codebase o tenerli come placeholder per future decisioni umane non ancora previste? Preferenza implementativa: tenerli **commentati nel piano** ma non implementarli, come zone di estensione futura.

4. **Versioning degli output F3 r3**: per i temi nuovi, gli output partiranno da `v1`. Per i temi che eventualmente vengono ri-eseguiti dopo aver visto le esecuzioni precedenti, mantenere il convenzione `v1` (nessuna eredità) o partire da una versione che indichi "post-migration" (es. `v3.0`)? Consiglio: `v1`, riflette il fatto che si tratta di una pipeline diversa.

---

## 10. Riferimenti

- **Metodologia**: `HCAIRE Slides/context/metodo/f3-strumenti-operativi.md`
- **CLAUDE.md nuovi step F3**: `input/produzioni/f3-step-{1..5}-{nome}/CLAUDE.md`
- **Schemi JSON nuovi step F3**: `input/produzioni/f3-step-{1..5}-{nome}/{nome}-schema.json`
- **Configurazione orchestrazione**: `input/produzioni/webapp-hcaire/pipeline-step-config.json` (v3.0)
- **Documenti correlati**:
  - `D1-pipeline-step-graph.md` (grafo dichiarativo step)
  - `D2-execution-state-model.md` (schema MongoDB)
  - `D3-redis-message-protocol.md` (protocollo Redis)
  - `D4-api-spec-express.md` (endpoint Express, **§9 evaluateStepEnablement va aggiornato**)
  - `D5b-laboratorio-workbench.md` (frontend, **§5.2, §9.2, §9.3, §13, §19.7 vanno aggiornati**)
  - `D6-server-locale-cowork.md` (server locale, **§1 STEP_CLAUDE_FILE_MAP, §3 PromptComposer, §7 MICRO CASI vanno aggiornati**)
  - `Pipeline-inputs.md` (input esterni — già aggiornato)

---

**Fine documento.**

Per ogni punto in cui questo documento contraddice un documento precedente (D1-D6, D5b), **prevale questo documento** per ciò che riguarda la pipeline F3. Per F2 e per il modello a tre entità prevalgono i documenti precedenti.
