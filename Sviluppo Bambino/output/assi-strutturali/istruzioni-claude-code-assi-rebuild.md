# Istruzioni per Claude Code — Nuovo caso d'uso: Rebuild Assi Strutturali via Cowork

> **Destinatario:** Claude Code che gestisce il monorepo `hcaire-blog`
> **Riferimento architetturale:** `hcaire-docs/docs/10-architecture/local-cowork-bridge.md` §4
> **Ultima revisione:** 2026-05-11

---

## Contesto

I sei file JSON degli assi strutturali (uno per asse, schema `assi-fase-1.json`) devono
diventare l'**unica sorgente di verità** per il progetto Sviluppo Bambino su MongoDB Atlas.
Sono referenziati da più parti della webapp e oggi vivono solo sul filesystem locale in
`precompiled/`.

L'obiettivo è implementare un quarto verticale nel bridge `local/`, chiamato **"assi"**,
che permetta all'admin del sito di triggherare la rigenerazione dei JSON a partire dai
capitoli Markdown in `normalized/`, con Cowork che fa il lavoro concettuale e il server
che poi fa l'upsert su MongoDB.

---

## Che cosa fa Cowork in questo caso

Cowork legge tutti i capitoli Markdown in:

```
C:\my\projects\hcaire-blog\server\content\progetti\sviluppo bambino\assi strutturali\normalized\
```

Ogni sottocartella corrisponde a un asse e contiene i capitoli in `.md`. Cowork costruisce
una scheda asse per ciascuno dei 6 assi e scrive 6 file JSON in:

```
C:\my\projects\hcaire-blog\server\content\progetti\sviluppo bambino\assi strutturali\precompiled\
```

I file prodotti si chiamano `asse_1.json` … `asse_6.json` e devono essere conformi allo
schema in:

```
C:\my\claude\claude-cowork\Sviluppo Bambino\input\assi strutturali\preprocessing\assi-fase-1.json
```

Il CLAUDE.md che guida Cowork si trova in:

```
C:\my\claude\claude-cowork\Sviluppo Bambino\input\assi strutturali\preprocessing\CLAUDE.md
```

Non ci sono step intermedi: è un'operazione singola (non una pipeline F2/F3) che produce
6 file in un'unica esecuzione di Cowork.

---

## Differenze rispetto ai casi d'uso esistenti

| Aspetto | Pipeline F2/F3 | Letture | **Assi (nuovo)** |
|---|---|---|---|
| Step multipli | Sì, 7+5 step | Sì, 10 step | **No — operazione unica** |
| Path resolver locale | Sì (`_resolveLocalPath`) | No (path assoluti) | **No — path assoluti** |
| Espansione assi precompilati | Sì | No | **N/A — li produce lui** |
| Output → MongoDB | No (file locali + `client/public/`) | No | **Sì — upsert dopo completamento** |
| Modello di riferimento | `PipelineCommandHandler` | `LettureCommandHandler` | **`LettureCommandHandler`** (più semplice) |

---

## Implementazione — Checklist §4

### 1. Variabili d'ambiente

Aggiungi a `local/.env` (e al template `local/.env.example`):

```bash
# Assi strutturali rebuild
COWORK_ASSI_PATH=C:\my\claude\claude-cowork\Sviluppo Bambino
NORMALIZED_AXES_DIR=C:\my\projects\hcaire-blog\server\content\progetti\sviluppo bambino\assi strutturali\normalized
PRECOMPILED_AXES_DIR=C:\my\projects\hcaire-blog\server\content\progetti\sviluppo bambino\assi strutturali\precompiled
AXES_SCHEMA_PATH=C:\my\claude\claude-cowork\Sviluppo Bambino\input\assi strutturali\preprocessing\assi-fase-1.json
AXES_CLAUDE_MD_PATH=C:\my\claude\claude-cowork\Sviluppo Bambino\input\assi strutturali\preprocessing\CLAUDE.md
```

> Nota: `PRECOMPILED_AXES_DIR` è già usata dal `PipelineCommandHandler` esistente per
> l'espansione degli assi in input alle produzioni. Verifica che puntino entrambe alla
> stessa cartella (`precompiled/`, non `precompiled-ver-2/`).

---

### 2. Sul server (`server/src/`)

#### 2a. Canali Redis — `services/assiMessageBus.ts`

Clona `services/lettureMessageBus.ts` e adatta:

```typescript
export const REDIS_ASSI_COMMANDS_KEY = 'hcaire:assi:commands';
export const REDIS_ASSI_EVENTS_CHANNEL = 'hcaire:assi:events';
```

Implementa:
- `publishAssiRebuildCommand(redis, payload)` → `LPUSH hcaire:assi:commands`
- `subscribeAssiEvents(redis, handlers)` → `SUBSCRIBE hcaire:assi:events`

#### 2b. Modello MongoDB — `models/AssiRebuild.ts`

```typescript
// Traccia le esecuzioni di rebuild
interface IAssiRebuildExecution {
  _id: ObjectId;
  status: 'in_coda' | 'in_esecuzione' | 'completato' | 'fallito';
  triggered_at: Date;
  completed_at?: Date;
  log_lines: string[];
  axes_updated: string[];   // ['asse_1', 'asse_2', ...] se completato
  error?: string;
}
```

#### 2c. Collection MongoDB per i dati — `assi_strutturali`

Ogni documento corrisponde a un asse. Schema derivato da `assi-fase-1.json`:

```typescript
// Indice univoco su axis_id
db.collection('assi_strutturali').createIndex({ axis_id: 1 }, { unique: true });

// Struttura documento (corrisponde al JSON prodotto da Cowork + metadati)
interface IAsseStrutturale {
  axis_id: string;           // 'asse_1' … 'asse_6'
  axis_name: string;
  version: string;
  status: 'bozza' | 'consolidato' | 'in_revisione';
  structural_function: string;
  core_processes: Array<{ name: string; description: string }>;
  bridge_concepts: Array<{ concept: string; definition: string; linked_nodes?: string[] }>;
  structural_nodes: Array<{ node: string; short_definition: string }>;
  internal_articulations: Array<{ section: string; function: string }>;
  reduction_risks: Array<{ type: string; description: string }>;
  structural_questions: string[];
  methodological_constraints: string[];
  compilation_notes: {
    confidence_level: 'bassa' | 'media' | 'alta';
    needs_human_review: boolean;
    notes?: string;
    open_issues?: string[];
  };
  // Metadati aggiunti dal server al momento dell'upsert
  _last_rebuilt: Date;
  _source_version: string;   // hash o timestamp della cartella normalized/
}
```

#### 2d. Event subscriber — `services/assiEventSubscriber.ts`

Clona `services/lettureEventSubscriber.ts`. Handler da implementare:

| Evento | Azione |
|---|---|
| `step.started` | `AssiRebuildExecution.status = 'in_esecuzione'` |
| `step.log` | Append a `log_lines` (con buffer, come le letture) |
| `step.completed` | Leggi i 6 file da `PRECOMPILED_AXES_DIR`, fa upsert su `assi_strutturali`, imposta `status = 'completato'`, popola `axes_updated` |
| `step.failed` | `status = 'fallito'`, salva `error` |
| `step.cancelled` | `status = 'fallito'` con note |

**Logica upsert post-completamento** (dentro l'handler `step.completed`):

```typescript
const fs = require('fs');
const path = require('path');

const precompiledDir = process.env.PRECOMPILED_AXES_DIR!;
const axesUpdated: string[] = [];

for (let i = 1; i <= 6; i++) {
  const filePath = path.join(precompiledDir, `asse_${i}.json`);
  if (!fs.existsSync(filePath)) continue;
  
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  await db.collection('assi_strutturali').updateOne(
    { axis_id: `asse_${i}` },
    { $set: { ...data, _last_rebuilt: new Date() } },
    { upsert: true }
  );
  axesUpdated.push(`asse_${i}`);
}

await AssiRebuildExecution.updateOne(
  { _id: executionId },
  { $set: { status: 'completato', completed_at: new Date(), axes_updated: axesUpdated } }
);
```

#### 2e. Rotta admin — `routes/assi.ts`

```
POST /api/admin/assi/rebuild
```

Comportamento:
1. Crea un `AssiRebuildExecution` con `status: 'in_coda'`.
2. Fa `LPUSH hcaire:assi:commands` con payload `{ execution_id, type: 'assi.rebuild' }`.
3. Ritorna `{ execution_id }` al client.

```
GET /api/admin/assi/rebuild/:execution_id
```

Ritorna lo stato dell'esecuzione (per polling dalla UI o per SSE se preferisci seguire
il pattern delle produzioni).

#### 2f. Avvio servizi in `server/src/index.ts`

```typescript
// Dentro il blocco try/catch indipendente degli altri subscriber
try {
  assiEventSubscriber.start();
  assiWatchdog.start();   // opzionale, timeout dopo N minuti senza eventi
} catch (err) {
  logger.error('AssiEventSubscriber failed to start', err);
}
```

---

### 3. Sul worker `local/src/`

#### 3a. Costanti — `pipeline/assiConstants.ts`

```typescript
export const REDIS_ASSI_COMMANDS_KEY = 'hcaire:assi:commands';
export const REDIS_ASSI_EVENTS_CHANNEL = 'hcaire:assi:events';

export const COWORK_ASSI_PATH = process.env.COWORK_ASSI_PATH!;
export const NORMALIZED_AXES_DIR = process.env.NORMALIZED_AXES_DIR!;
export const PRECOMPILED_AXES_DIR = process.env.PRECOMPILED_AXES_DIR!;
export const AXES_CLAUDE_MD_PATH = process.env.AXES_CLAUDE_MD_PATH!;
```

#### 3b. Prompt composer — `pipeline/AssiPromptComposer.ts`

Il prompt per Cowork è già scritto nel `CLAUDE.md` del preprocessing. Il composer si
limita a leggerlo e restituirlo come stringa. Non servono sostituzioni di placeholder.

```typescript
import fs from 'fs';
import { AXES_CLAUDE_MD_PATH } from './assiConstants';

export class AssiPromptComposer {
  compose(): string {
    return fs.readFileSync(AXES_CLAUDE_MD_PATH, 'utf-8');
  }
}
```

> **Importante**: il CLAUDE.md del preprocessing ha i path di input e output hardcoded.
> Prima di usarlo, verifica che il path di output punti a `precompiled/` (non
> `precompiled-ver-2/`). Se necessario aggiorna il CLAUDE.md direttamente — Cowork
> (Stefano) provvede.

#### 3c. Command handler — `pipeline/AssiCommandHandler.ts`

Clona `LettureCommandHandler.ts` (il più semplice, senza path resolver). Differenze:

- Usa `REDIS_ASSI_COMMANDS_KEY` e `REDIS_ASSI_EVENTS_CHANNEL` da `assiConstants.ts`
- `cwd` per lo spawn: `COWORK_ASSI_PATH`
- Prompt: `new AssiPromptComposer().compose()`
- Pre-flight check: leggi `AssiRebuildExecution` da Mongo, salta se `status !== 'in_coda'`
- Non c'è mappa step-id → cartella: c'è un solo "step" (il rebuild completo)
- `output_file` nell'evento `step.completed`: non serve — il server legge direttamente
  dalla cartella `PRECOMPILED_AXES_DIR` (sa già dove sono i file)

Schema del payload del comando in coda:

```typescript
interface AssiRebuildCommand {
  type: 'assi.rebuild';
  execution_id: string;
}
```

#### 3d. Avvio in `local/src/index.ts`

```typescript
import { AssiCommandHandler } from './pipeline/AssiCommandHandler';

// Accanto agli altri handler
const assiHandler = new AssiCommandHandler(redisClient, mongoDb);
await assiHandler.start();
```

---

## Schema MongoDB — riepilogo

| Collection | Chiave | Descrizione |
|---|---|---|
| `assi_strutturali` | `axis_id` (unique) | I 6 JSON degli assi, fonte di verità |
| `assi_rebuild_executions` | `_id` | Log delle esecuzioni di rebuild |

**Indici consigliati su `assi_strutturali`:**

```javascript
db.assi_strutturali.createIndex({ axis_id: 1 }, { unique: true })
db.assi_strutturali.createIndex({ status: 1 })
db.assi_strutturali.createIndex({ _last_rebuilt: -1 })
```

---

## Flusso end-to-end

```
[Admin UI]
  └─ POST /api/admin/assi/rebuild
       └─ crea AssiRebuildExecution { status: 'in_coda' }
       └─ LPUSH hcaire:assi:commands { type: 'assi.rebuild', execution_id }
            │
[local/ worker — AssiCommandHandler]
  └─ BRPOP hcaire:assi:commands
       └─ pre-flight: verifica status === 'in_coda'
       └─ compose prompt da AXES_CLAUDE_MD_PATH
       └─ spawn: claude --print --dangerously-skip-permissions
                 stdin: prompt, cwd: COWORK_ASSI_PATH
            │
[Cowork — Claude]
  └─ legge capitoli da NORMALIZED_AXES_DIR/asse_*/
  └─ costruisce 6 schede asse conformi ad assi-fase-1.json
  └─ scrive asse_1.json … asse_6.json in PRECOMPILED_AXES_DIR/
  └─ exit 0
            │
[local/ worker]
  └─ PUBLISH hcaire:assi:events { type: 'step.completed' }
            │
[server — AssiEventSubscriber]
  └─ legge i 6 file da PRECOMPILED_AXES_DIR/
  └─ upsert su MongoDB collection 'assi_strutturali'
  └─ aggiorna AssiRebuildExecution { status: 'completato', axes_updated: [...] }
```

---

## Note operative

- **Mock mode**: aggiungi `ASSI_MOCK_MODE=true` in `local/.env` per test senza spawn reale
  (il handler scrive file segnaposto in `PRECOMPILED_AXES_DIR/`).
- **Durata attesa**: Cowork impiega tipicamente 3–8 minuti per elaborare tutti e 6 gli
  assi. Imposta il timeout di `CoworkRunner` a 15 minuti.
- **Rigenerazione parziale**: non è prevista nella prima versione. Se serve in futuro,
  si può estendere il payload del comando con `{ axes: [1, 3] }` e modificare il CLAUDE.md
  per accettare un parametro di filtro.
- **Cowork conosce la procedura**: il progetto Cowork (Stefano) possiede e mantiene il
  CLAUDE.md del preprocessing e sa rigenerare i `precompiled/` manualmente se necessario.
  Il bridge è solo l'automazione di quel processo.
