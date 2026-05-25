# D12 — Area pubblica strumenti — implementazione webapp — istruzioni per Claude Code

> **Destinatario**: Claude Code. Questo documento istruisce l'**implementazione webapp** della nuova **area pubblica di visualizzazione degli strumenti finali** della pipeline "Produzioni" del progetto "Sviluppo Bambino".
>
> **Leggere prima**: `D11-area-pubblica-strumenti.md` — è la **specifica autoritativa di progettazione** (cosa è una Scheda Strumento, composizione, organizzazione, resa campo-per-campo, doppio gate, modello di accesso, vincolo non-prescrittivo). D12 non duplica D11: lo presuppone e lo traduce in istruzioni di codice. Per il contesto: `D4` (API e auth), `D5` (frontend, `useIsAdmin`), `D5b` (area riservata — Laboratorio), `D9` (modulo F3-SIT), `Storage dati e schemi pipeline.md` (persistenza).
>
> **Cosa aggiunge**:
> - una collezione MongoDB `published_tools` + modello Mongoose
> - un namespace API `/api/sviluppo-bambino/strumenti/*` (endpoint pubblici + editoriali admin)
> - una funzione di proiezione `buildPublicSchedaProjection` e una di gating `evaluatePublicationDataGate`
> - route, pagine e componenti frontend dell'area pubblica, sotto `/sviluppo-bambino/strumenti`
> - un pannello editoriale admin per il workflow di pubblicazione
> - un hook `useUserTier` e il ruolo Clerk `subscriber` (previsto, non attivato)
>
> **Cosa modifica**:
> - gli endpoint `GET /api/pipeline/*` passano da `public` ad `admin` (era `D4` §1.1)
> - le pagine read-only della pipeline (`/produzioni`, `/sviluppo-bambino/...` che renderizzano artefatti di pipeline) passano dietro `useIsAdmin()`
>
> **Cosa NON modifica**: la pipeline F2/F3/F3-SIT, i suoi step, schemi e output; le collezioni `pipeline_contexts`, `pipeline_step_executions`, `pipeline_external_inputs`; il protocollo Redis (`D3`); il Laboratorio (`D5b`).
>
> **Migrazione dati**: nessuna. La collezione `published_tools` nasce vuota; i record si creano on-demand dal pannello editoriale.
>
> **Stato**: specifica di implementazione v1 · **Data**: 2026-05-24.

---

## 1. Sintesi della modifica

Oggi l'intera pipeline è esposta pubblicamente (`D4` §1.1: ogni `GET` è `public`). D12 implementa la separazione progettata da `D11`:

- **Area riservata** — pipeline, output intermedi, Laboratorio: solo `admin`.
- **Area pubblica** — strumenti finali approvati, in forma leggibile: tutti gli utenti (con un livello `abbonato` previsto e non attivato).

L'unità di contenuto pubblica è la **Scheda Strumento** (`D11` §3): una pagina per `context_id` (`<theme_id>--<ambito_id>`) che compone la **cornice** (output-tipo F3 step 5) e il **corpo** (repertorio F3-SIT). La pubblicazione passa per un **doppio gate** (`D11` §7): gate-dati automatico + gate editoriale umano.

L'area appartiene al progetto **Sviluppo Bambino → Produzioni**: URL e navigazione devono renderlo evidente (§8).

---

## 2. Modello dati — collezione `published_tools`

Nuova collezione MongoDB. Schema Mongoose in `server/src/models/PublishedTool.ts`. La struttura del documento è definita in `D11` §4.1; qui la traduzione in modello.

```typescript
// server/src/models/PublishedTool.ts

type PublicationStatus = 'bozza' | 'in_revisione' | 'pubblicato' | 'ritirato';
type Visibility = 'pubblico' | 'abbonato' | 'riservato';
type MethodologicalStatus = 'validato' | 'richiede_revisione' | 'non_pubblicabile';
type CoherenceStatus = 'valido' | 'richiede_revisione' | 'fuori_modello';

interface PublishedTool {
  context_id: string;            // univoco — identità pipeline F3
  theme_id: string;
  theme_label: string;
  ambito_id: string;
  domain_selected: 'clinico' | 'educativo' | 'formazione' | 'politiche';
  context_label: string;
  slug: string;                  // univoco — slug URL pubblico

  source_refs: {
    output_tipo_execution_id: ObjectId | null;        // f3_step_5
    sit_repertorio_execution_id: ObjectId | null;     // f3_sit_step_4
    sit_micro_mediazioni_execution_id: ObjectId | null; // f3_sit_step_2
    sit_formati_execution_id: ObjectId | null;        // f3_sit_step_3 (può mancare)
  };

  data_gate: {
    methodological_status: MethodologicalStatus | null;
    public_site_recommended: boolean;
    professional_training_recommended: boolean;
    f3_coherence_status: CoherenceStatus | null;
    passes_data_gate: boolean;     // calcolato — §4
    evaluated_at: Date | null;
  };

  publication: {
    status: PublicationStatus;     // default 'bozza'
    visibility: Visibility;        // default 'riservato'
    published_at: Date | null;
    published_by: string | null;   // Clerk userId
    last_editorial_review_at: Date | null;
    editorial_notes: string;       // default ''
  };

  content_snapshot: SchedaProjection | null;   // §3 — congelato alla pubblicazione
  created_at: Date;
  updated_at: Date;
}
```

**Indici**: `context_id` univoco; `slug` univoco; indice composto `{ 'publication.status': 1, 'publication.visibility': 1, domain_selected: 1 }` per l'index pubblico.

**Vincoli applicativi** (non a livello di schema): un documento non può passare a `publication.status = 'pubblicato'` con `visibility = 'pubblico'` se `data_gate.passes_data_gate === false` (§5, endpoint `transition`).

---

## 3. Backend — funzione di proiezione `buildPublicSchedaProjection`

In `server/src/services/strumentiService.ts`. Trasforma gli output di pipeline nella struttura leggibile `SchedaProjection`, applicando la mappa campo-per-campo di `D11` §5. È invocata dall'endpoint `build` (§5.2) e il risultato viene congelato in `content_snapshot` alla pubblicazione (`D11` §5.5).

### 3.1 Input

`buildPublicSchedaProjection(contextId)` legge da `pipeline_step_executions` (campo `output_data` mirrorato — `D9` §8 punto 6) l'ultima run verificata/completata di:

- `f3_step_5` → output-tipo contestualizzato (la cornice)
- `f3_sit_step_4` → `sit-repertorio` (la lista degli item validati per famiglia)
- `f3_sit_step_2` → `sit-micro-mediazioni` (contenuto item famiglie 1–5)
- `f3_sit_step_3` → `sit-formati` (contenuto item famiglie 6–9; può mancare se lo step è stato saltato)

Il file `sit-repertorio` **non contiene** il testo dei materiali: contiene `repertoire[]` (aggregati per famiglia, con i soli `item_refs` validati) e `item_checks[]`. La proiezione è una **giunzione**: per ogni `family_id` in `repertoire[]`, prende i `item_refs` con `item_verdict = validato` e recupera il contenuto completo da `sit-micro-mediazioni` / `sit-formati`.

### 3.2 Output — struttura `SchedaProjection`

```typescript
interface SchedaProjection {
  schema_version: '1';
  titolo: string;                 // theme_label
  sottotitolo: string;            // context_label
  ambito: string;                 // domain_selected
  introduzione: string;           // output-tipo.narrative_synthesis
  a_cosa_serve: string;           // output-tipo.orientative_direction
  come_funziona: {                // da output-tipo.dispositivo_ref
    sintesi: string;              // device_synthesis
    durata: string;               // real_time
    come_accorgersene: string | null;  // resonance_indicator, riformulato
  };
  aree_di_lettura: Array<{        // 5 — da output-tipo.sections[]
    etichetta: string;            // section_label
    testo: string;                // linguistic_frame
    esempi: string[];             // domain_examples
    domande: string[];            // decisional_nodes — resi come domande (D11 §10)
  }>;
  destinatari: Array<'genitori' | 'operatori' | 'formatori'>;  // §3.3
  materiali_per_famiglia: Array<{
    famiglia_id: string;          // F3-SIT-1..9
    famiglia_nome: string;        // da f3-sit-famiglie.json (name)
    materiali: MaterialeProiettato[];
  }>;
  cornice_non_prescrittiva: string;  // testo di cornice standard (D11 §10)
}

interface MaterialeProiettato {
  tipo: string;                   // nome leggibile della famiglia
  titolo: string;                 // item.title
  contesto: { setting: string; eta: string; situazione: string } | null;
  atteggiamento_adulto: string | null;     // micro_mediation.adult_attitude
  formulazioni: string[];         // possible_phrase + alternative_phrase, non-null
  gesto_tempo: string | null;     // micro_mediation.gesture_or_timing
  cosa_evitare: string[];         // micro_mediation.avoid
  cosa_rende_osservabile: string | null;   // expected_field_effect
  non_e_una_ricetta: string;      // non_prescriptive_note — SEMPRE valorizzato
}
```

### 3.3 Regole di trasformazione (vincolanti)

1. **Campi nascosti.** Non devono comparire in `SchedaProjection`, mai: nodi N1–N7, `configurational_basis` (`dominant_node`, `function`, `target_field`, `universal_device_type`, `source_device_id`), tipi U1–U6, checklist C1–C8 e `item_checks`, `methodological_status`, `source_validations`, `item_verdict`, `critical_failures`, CE / dimensioni S-R-D-T-A, `dispositivo_ref.function_type`, `operator_note`. Riferimento: `D11` §5.3.
2. **`situazione`.** Da `context.situation` rimuovere il prefisso tecnico `case_type: …` (regex sul prefisso) e mantenere il resto.
3. **`item_checks` come filtro.** Solo gli item con `item_verdict = validato` entrano nella proiezione. Gli item in `items_to_revise` sono esclusi.
4. **Famiglia F3-SIT-9 (prompt AI)** esclusa dalla proiezione pubblica (`D11` §5.2): se presente in `repertoire[]`, non proiettarne i materiali per `visibility: pubblico`.
5. **`non_e_una_ricetta` obbligatorio.** Se un item non ha `non_prescriptive_note`, è un errore di dato: l'item va escluso e segnalato nei log della proiezione (non deve mai mancare il presidio anti-prescrittivo).
6. **`destinatari`.** Calcolati dall'unione dei `typical_target_user` delle famiglie presenti (`f3-sit-famiglie.json`), mappati in 3 categorie: `genitori` ← {genitore, caregiver}; `operatori` ← {pediatra, educatore, insegnante, bibliotecario}; `formatori` ← {formatore}.
7. **`cornice_non_prescrittiva`.** Testo standard, costante, definito una sola volta lato server (vedi §12).
8. **Caso "solo cornice".** Se non esiste `sit-repertorio` (modulo F3-SIT non eseguito), `materiali_per_famiglia` è `[]`. Una scheda così **non** è pubblicabile `pubblico` (gate-dati, §4): la proiezione si costruisce comunque ma resta utilizzabile solo per livelli `abbonato`/`riservato`.

---

## 4. Backend — gating dei dati

In `strumentiService.ts`. `evaluatePublicationDataGate(record)` calcola `data_gate.passes_data_gate` e popola `data_gate`.

```typescript
function evaluatePublicationDataGate(repertoire, coherence): {
  passes: boolean; reasons: string[];
} {
  // Per il livello 'pubblico' servono TUTTE:
  //  - methodological_status === 'validato'
  //  - publication_recommendation.public_site === true
  //  - f3_coherence_status === 'valido'   (non null, non 'fuori_modello', non 'richiede_revisione')
  // passes === false → la scheda NON può essere pubblicata 'pubblico'.
}
```

Il gate-dati è **necessario ma non sufficiente** (`D11` §7.2): superarlo rende la scheda *candidabile*, non pubblicata. La pubblicazione effettiva richiede il gate editoriale (§5.2, endpoint `transition`).

> Caso noto (pilota `gioco-libero × clinico`): `methodological_status = validato` ma `public_site = false` e `f3_coherence_status = null` → `passes_data_gate = false`. Atteso e corretto: la scheda resta `riservato`. Vedi `D11` §7.2 e §12 pendenza 1.

---

## 5. Backend — endpoint API

Namespace nuovo `/api/sviluppo-bambino/strumenti/*`. Envelope e codici HTTP come `D4` §1.2–1.3. File: `server/src/routes/strumenti.ts`, `server/src/controllers/strumentiController.ts`. Registrazione in `server/src/index.ts`:

```typescript
import strumentiRoutes from './routes/strumenti';
app.use('/api/sviluppo-bambino/strumenti', strumentiRoutes);
```

### 5.1 Endpoint pubblici (lettura)

| Metodo | Path | Auth | Scopo |
|---|---|---|---|
| GET | `/api/sviluppo-bambino/strumenti` | public | Index: schede con `status = pubblicato` e `visibility` compatibile col tier del richiedente. Query opzionali: `?ambito=`, `?destinatario=`. Restituisce metadati di card (titolo, sottotitolo, ambito, destinatari, una riga da `a_cosa_serve`), **non** il `content_snapshot` completo. |
| GET | `/api/sviluppo-bambino/strumenti/:slug` | public | Una scheda: restituisce `content_snapshot`. 404 se inesistente, non `pubblicato`, o `visibility` non compatibile col tier. |

Questi endpoint servono **solo** `content_snapshot`. Non devono mai leggere `pipeline_step_executions` né esporre campi nascosti (§3.3).

### 5.2 Endpoint editoriali (admin)

Tutti con middleware `requireAdmin` (`D4` §1.1).

| Metodo | Path | Scopo |
|---|---|---|
| GET | `/api/sviluppo-bambino/strumenti/admin/candidati` | Elenco dei `context_id` con un output finale (`f3_step_5` e/o `f3_sit_step_4` completati), con l'esito del gate-dati. Materiale di lavoro della revisione. |
| GET | `/api/sviluppo-bambino/strumenti/admin/:contextId` | Record `published_tools` completo + anteprima della proiezione, per la revisione. |
| POST | `/api/sviluppo-bambino/strumenti/:contextId/build` | Crea/aggiorna il record, esegue `buildPublicSchedaProjection` + `evaluatePublicationDataGate`. Non pubblica. 201 se creato, 200 se aggiornato. |
| POST | `/api/sviluppo-bambino/strumenti/:contextId/transition` | Cambia `publication.status` e/o `visibility`. Body: `{ status?, visibility?, editorial_notes? }`. Su transizione a `pubblicato`: congela `content_snapshot`, set `published_at`/`published_by`. **422** se `status=pubblicato` + `visibility=pubblico` + `data_gate.passes_data_gate=false`. |
| PATCH | `/api/sviluppo-bambino/strumenti/:contextId/slug` | Modifica lo slug. **409** se lo slug è già in uso. |

Codici errore applicativi nuovi (stile `D4` §1.4): `TOOL_NOT_FOUND`, `TOOL_DATA_GATE_FAILED`, `SLUG_ALREADY_IN_USE`, `INVALID_STATUS_TRANSITION`.

### 5.3 Migrazione — `GET /api/pipeline/*` da `public` ad `admin`

In `server/src/routes/pipeline.ts`: applicare il middleware `requireAdmin` a **tutti** gli endpoint `GET` oggi `public` (`D4` §11: `index`, `step-config`, `temi/:id`, `ricerche/:id`, `.../history`, `.../inputs`, `pending-decision`, `executions/:id/logs`). Dopo la modifica nessun endpoint di pipeline è pubblico. Aggiornare la tabella di `D4` §11 di conseguenza (annotazione di revisione in testa a `D4`, vedi §15).

---

## 6. Ruoli Clerk e tier utente

### 6.1 Ruolo `subscriber` (previsto, non attivato)

Il modello prevede tre tier (`D11` §8.2): `public`, `subscriber`, `admin`. Clerk gestisce i ruoli via `user.publicMetadata.role`. In questa fase si usano solo `admin` e l'assenza di ruolo; il valore `'subscriber'` è documentato come legittimo ma **non** assegnato ad alcun utente e **non** sbloccante.

### 6.2 Hook `useUserTier`

```typescript
// client/src/hooks/useUserTier.ts
import { useUser } from '@clerk/clerk-react';

export type UserTier = 'public' | 'subscriber' | 'admin';

export function useUserTier(): UserTier {
  const { user } = useUser();
  const role = user?.publicMetadata?.role;
  if (role === 'admin') return 'admin';
  if (role === 'subscriber') return 'subscriber';   // previsto, oggi nessun utente lo ha
  return 'public';
}
```

`useIsAdmin()` (`D5` §1.2) resta invariato. La compatibilità di visibilità: `pubblico` → visibile a tutti; `abbonato` → `subscriber` + `admin`; `riservato` → solo `admin`. In questa fase, non esistendo utenti `subscriber`, una scheda `abbonato` è di fatto visibile solo agli admin (comportamento atteso, `D11` §8.2).

---

## 7. Frontend — service e routing

### 7.1 Service

`client/src/services/strumentiService.ts`: `fetchStrumentiIndex(filtri)`, `fetchSchedaBySlug(slug)`, e — per il pannello admin — `fetchCandidati()`, `fetchAdminScheda(contextId)`, `buildScheda(contextId)`, `transitionScheda(contextId, body)`, `updateSlug(contextId, slug)`. Tutte puntano a `/api/sviluppo-bambino/strumenti/*`.

### 7.2 Route

| Route | Componente | Auth |
|---|---|---|
| `/sviluppo-bambino/strumenti` | `StrumentiIndexPage` | pubblica |
| `/sviluppo-bambino/strumenti/:slug` | `SchedaStrumentoPage` | pubblica |
| `/sviluppo-bambino/strumenti/admin` | `StrumentiEditorialePage` | `useIsAdmin()` — redirect se non admin |

Le route pubbliche non montano alcun check di ruolo. La route admin è gated come il Laboratorio (`D5b`).

---

## 8. Frontend — collocazione nella navigazione

**Requisito esplicito** (`D11` §6.0): l'area pubblica appartiene al progetto **Sviluppo Bambino → Produzioni**, e questo deve essere visibile nella navigazione, non solo nelle URL.

- La voce **"Strumenti"** va inserita **dentro il raggruppamento di navigazione "Sviluppo Bambino"**, accanto a "Produzioni" — non come voce di primo livello del sito.
- La voce è **sempre visibile** (è pubblica), a differenza della voce admin "Laboratorio" (`D5b` §2.2) che resta condizionata a `useIsAdmin()`.
- Dalle pagine del progetto "Sviluppo Bambino" / "Produzioni" deve esistere un collegamento diretto all'area "Strumenti", così che il pubblico arrivi agli strumenti finali senza passare dalle pagine tecniche (ora riservate, §10).

> Il componente di navigazione esatto non è coperto dai documenti `D`. Claude Code deve **individuare** il componente che renderizza la navigazione del progetto "Sviluppo Bambino" (cercare i componenti `SviluppoBambino*` citati in `D5` §1.1, es. `SviluppoBambinoPipelineMap`, e il menu/nav che li raggruppa) e collocarvi la voce "Strumenti". Se il raggruppamento "Produzioni" è un sotto-menu, la voce "Strumenti" gli sta accanto allo stesso livello.

---

## 9. Frontend — componenti dell'area pubblica

File sotto `client/src/components/strumenti/` e `client/src/pages/`.

### 9.1 `StrumentiIndexPage`

Intestazione divulgativa dell'area; schede pubblicate raggruppate per **ambito** (`clinico`, `educativo`, `formazione`, `politiche`, con etichette divulgative); filtro per **destinatario** (genitori / operatori / formatori) applicato lato client. Ogni scheda è una `SchedaCard` (titolo del fenomeno, sottotitolo di contesto, badge destinatari, una riga da `a_cosa_serve`). Mostra solo le schede restituite dall'endpoint pubblico (già filtrate per tier lato server).

### 9.2 `SchedaStrumentoPage`

Renderizza `content_snapshot`. Struttura (`D11` §6.3):

```
┌─ CORNICE ──────────────────────────────────────────────┐
│  titolo · sottotitolo                                  │
│  introduzione  (introduzione)                          │
│  riquadro "A cosa serve"  (a_cosa_serve)               │
│  riquadro "Come funziona, in breve"  (come_funziona)   │
│  5 Aree di lettura  (aree_di_lettura[])                │
│     · testo · esempi · "Domande da tenere aperte"      │
├─ CORPO ────────────────────────────────────────────────┤
│  per ciascuna famiglia: intestazione + MaterialeCard[] │
├─ CHIUSURA ─────────────────────────────────────────────┤
│  cornice_non_prescrittiva                              │
└────────────────────────────────────────────────────────┘
```

Componenti: `CornicePanel`, `AreaDiLetturaCard`, `CorpoRepertorio`, `MaterialeCard`, `CorniceNonPrescrittivaBanner`. Nessun viewer JSON, nessun campo di metodo, nessuna lista numerata di passi (`D11` §10.1 punto 6).

### 9.3 `MaterialeCard` — requisiti anti-prescrittivi vincolanti

Per ogni materiale (`D11` §10.1): `non_e_una_ricetta` sempre reso in un riquadro evidenziato e non comprimibile; `cosa_evitare` sempre reso; `formulazioni` sotto un'etichetta esplicita ("Una formulazione possibile, non un copione"); nessuna numerazione di passi. Se `non_e_una_ricetta` è vuoto, il materiale non va renderizzato (coerente con §3.3 punto 5).

---

## 10. Frontend — riservare le pagine read-only ad admin

Le pagine che oggi renderizzano artefatti di pipeline a chiunque (`D5` §0; route `/produzioni/...` e le pagine `SviluppoBambino*` che mostrano output di pipeline) vanno gated dietro `useIsAdmin()`:

- Avvolgere quelle route/pagine in un guard `useIsAdmin()`: se non admin → redirect a `/sviluppo-bambino/strumenti` (l'area pubblica è la loro nuova controparte pubblica).
- Poiché gli endpoint `GET /api/pipeline/*` diventano `admin` (§5.3), un utente non admin non deve mai chiamarli: il guard di route lo garantisce. Verificare che nessun componente pubblico residuo invochi `pipelineService.*`.
- Il Laboratorio (`D5b`) è già gated: nessuna modifica.

Non vanno riservate, ovviamente, le route pubbliche del progetto che non mostrano artefatti di pipeline (pagine editoriali/divulgative pre-esistenti): toccare **solo** le viste che espongono output della pipeline.

---

## 11. Frontend — pannello editoriale admin (`StrumentiEditorialePage`)

Route `/sviluppo-bambino/strumenti/admin`, gated `useIsAdmin()`. Supporta il workflow del doppio gate (`D11` §7).

- **Lista candidati** — da `GET .../admin/candidati`: i `context_id` con output finali, con badge dell'esito gate-dati (passa / non passa, con motivi).
- **Dettaglio scheda** — da `GET .../admin/:contextId`: anteprima della proiezione leggibile + record `published_tools`. Azione `build` (ri-genera proiezione e ricalcola gate). Editor dello `slug`.
- **Transizioni di stato** — `bozza → in_revisione → pubblicato → ritirato` (un admin può tornare indietro). Selettore di `visibility` (`pubblico` / `abbonato` / `riservato`); proposta iniziale dalla mappa `D11` §8.3. La transizione a `pubblicato` con `visibility=pubblico` è **bloccata** dalla UI se il gate-dati non passa (e comunque rifiutata dal server con 422).
- **Checklist non-prescrittiva** (§12): prima di confermare `pubblicato`, l'admin deve spuntare la checklist; le note vanno in `editorial_notes`.

---

## 12. Vincolo non-prescrittivo — implementazione

Il vincolo metodologico (`D11` §10) ha due punti di implementazione concreti.

**Testo di cornice standard.** Definire una costante server-side (es. `STRUMENTI_CORNICE_NON_PRESCRITTIVA`) usata da `buildPublicSchedaProjection` per popolare `cornice_non_prescrittiva`. Contenuto: lo strumento descrive configurazioni e atteggiamenti possibili, non istruzioni; non è un protocollo; non sostituisce il giudizio del professionista né la relazione con il bambino. Testo unico per tutte le schede; revisione del testo a cura del ricercatore.

**Checklist editoriale nel pannello admin.** Nello step di transizione a `pubblicato`, `StrumentiEditorialePage` mostra la checklist di `D11` §10.2 come elenco di spunte obbligatorie (nessun campo di metodo trapelato; ogni materiale ha nota non-prescrittiva e "cosa evitare"; formulazioni etichettate come esempi; snodi decisionali resi come domande; niente forma-checklist; niente etichettatura del bambino / colpevolizzazione del genitore; cornice presente; linguaggio divulgativo). La transizione a `pubblicato` è abilitata solo a checklist completa.

---

## 13. Sequenza di rilascio consigliata

**Tappa 1 — Backend dati e gating**
1. Modello `PublishedTool.ts` + collezione e indici (§2).
2. `strumentiService.ts`: `buildPublicSchedaProjection` (§3) e `evaluatePublicationDataGate` (§4).

**Tappa 2 — Backend API**
3. `routes/strumenti.ts` + `strumentiController.ts`: endpoint pubblici ed editoriali (§5.1, §5.2); registrazione in `index.ts`.
4. Migrazione: `requireAdmin` su tutti i `GET /api/pipeline/*` (§5.3).

**Tappa 3 — Frontend pubblico**
5. `useUserTier` (§6.2); `strumentiService.ts` client (§7.1); route (§7.2).
6. `StrumentiIndexPage`, `SchedaStrumentoPage` e componenti (§9).
7. Collocazione della voce "Strumenti" nella navigazione "Sviluppo Bambino" (§8).

**Tappa 4 — Riservare l'area di lavoro**
8. Guard `useIsAdmin()` sulle pagine read-only di pipeline (§10).

**Tappa 5 — Pannello editoriale**
9. `StrumentiEditorialePage` con workflow del doppio gate e checklist non-prescrittiva (§11, §12).

**Tappa 6 — Verifica end-to-end**
10. Su un `context_id` con output finali, eseguire `build`, verificare la proiezione, percorrere `bozza → in_revisione → pubblicato`, controllare la visibilità per tier.

---

## 14. Criteri di accettazione

### 14.1 Backend
- [ ] Collezione `published_tools` con indici univoci su `context_id` e `slug`.
- [ ] `buildPublicSchedaProjection` non emette mai i campi nascosti di §3.3 punto 1.
- [ ] La proiezione include solo item con `item_verdict = validato`; esclude la famiglia F3-SIT-9.
- [ ] Ogni `MaterialeProiettato` ha `non_e_una_ricetta` valorizzato; gli item senza nota sono esclusi e loggati.
- [ ] `evaluatePublicationDataGate` restituisce `passes=false` per il pilota `gioco-libero × clinico` (`public_site=false`, `f3_coherence_status=null`).
- [ ] `transition` a `pubblicato`+`pubblico` con gate-dati fallito risponde 422 `TOOL_DATA_GATE_FAILED`.
- [ ] La transizione a `pubblicato` congela `content_snapshot`.
- [ ] Tutti i `GET /api/pipeline/*` rispondono 401/403 a un utente non admin.
- [ ] Gli endpoint pubblici `GET /api/sviluppo-bambino/strumenti*` non leggono mai `pipeline_step_executions`.

### 14.2 Frontend
- [ ] `/sviluppo-bambino/strumenti` e `/sviluppo-bambino/strumenti/:slug` sono pubbliche e funzionano da non autenticati.
- [ ] La voce "Strumenti" compare nella navigazione dentro il raggruppamento "Sviluppo Bambino", accanto a "Produzioni".
- [ ] La `SchedaStrumentoPage` non mostra alcun campo di metodo né JSON; mostra sempre la cornice non-prescrittiva e, per ogni materiale, "non è una ricetta" e "cosa evitare".
- [ ] Le pagine read-only di pipeline reindirizzano un non admin a `/sviluppo-bambino/strumenti`.
- [ ] `/sviluppo-bambino/strumenti/admin` è raggiungibile solo da admin.
- [ ] Il pannello editoriale blocca `pubblicato`+`pubblico` se il gate-dati non passa e richiede la checklist non-prescrittiva completa.

### 14.3 No-regressioni
- [ ] La pipeline F2/F3/F3-SIT esegue identicamente; nessuna modifica a step, schemi, output.
- [ ] Il Laboratorio (`D5b`) funziona invariato.
- [ ] Nessuna modifica al protocollo Redis né alle collezioni di pipeline.

---

## 15. Documenti da aggiornare e pendenze

**Annotazioni di revisione da aggiungere** (in testa ai documenti, sul modello delle note di revisione già presenti in `D1`):
- `D4` — §1.1 e §11: i `GET /api/pipeline/*` non sono più `public` ma `admin`; aggiunto il namespace `/api/sviluppo-bambino/strumenti/*`. Rinvio a `D11`/`D12`.
- `D5` — §0 e §1.1: l'interfaccia read-only di pipeline non è più visibile a tutti ma riservata ad admin; aggiunto `useUserTier`. Rinvio a `D11`/`D12`.

**Pendenze** (da `D11` §12, ricordate qui perché impattano l'implementazione):
1. `coerenza-v1.json` mancante a valle di `f3_step_4` impedisce a qualsiasi scheda di superare il gate-dati per il livello `pubblico`. Pendenza della pipeline F3, non di D12, ma in pratica nessuna scheda è pubblicabile `pubblico` finché non è risolta.
2. Livello `abbonato` non attivato: i tema × dominio con sola cornice (senza F3-SIT) restano `riservato`.
3. Derivazione automatica dello `slug` da `theme_id` + `ambito_id` (collisioni, leggibilità): definirla in fase di implementazione dell'endpoint `build`.

---

## 16. Riferimenti

- `D11-area-pubblica-strumenti.md` — **specifica autoritativa di progettazione** (D12 la presuppone).
- `D4-api-spec-express.md` — API e auth (modificato, §5.3, §15).
- `D5-frontend-spec-orchestrazione.md` — frontend, `useIsAdmin` (modificato, §15).
- `D5b-laboratorio-workbench.md` — area riservata (Laboratorio), invariata.
- `D9-pipeline-f3-sit.md` — modulo F3-SIT; `f3-sit-famiglie.json` — tassonomia e `typical_target_user`.
- `f3-step-5-output-tipo-contestualizzato/output-tipo-schema.json`, `f3-sit-step-4-repertorio/sit-repertorio-schema.json` — strutture sorgente della proiezione.
- `Storage dati e schemi pipeline.md` — persistenza, `output_data` mirrorato.
- Pilota: `output/produzioni/temi/gioco-libero-…--clinico-pediatrico/` — fixture di verifica.

---

*Fine documento — D12, implementazione webapp dell'area pubblica strumenti, 2026-05-24.*
