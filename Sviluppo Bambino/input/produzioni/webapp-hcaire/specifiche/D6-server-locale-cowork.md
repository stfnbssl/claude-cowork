# D6 — Server locale Cowork — Spec implementazione

> **Scopo del documento**: istruzioni operative per implementare il `PipelineCommandHandler` nel server locale che interfaccia Cowork. Specifica come leggere i CLAUDE.md degli step, costruire il prompt composito, lanciare Cowork, catturare l'output, e pubblicare eventi su Redis.
>
> **Destinatario**: Claude Code — da leggere dopo D3 (che definisce il protocollo Redis) e insieme al codice del server locale esistente. Il server locale già gestisce altri flussi Telegram/Redis/Cowork: questo documento descrive come aggiungere il handler pipeline senza toccare quelli esistenti.
>
> **Prerequisito**: leggere D3 §12 prima di questo documento — descrive la logica di composizione del prompt che qui viene implementata in codice.

---

## 1. Posizione nel server locale

Il server locale ha già una struttura per gestire comandi Redis. Il `PipelineCommandHandler` si aggiunge come modulo indipendente:

```
server-locale/
├── index.js (o index.ts)          ← esistente: avvia i listener
├── handlers/
│   ├── [altri handler esistenti]  ← non toccare
│   └── pipeline/                  ← nuovo
│       ├── PipelineCommandHandler.js
│       ├── PromptComposer.js
│       ├── CoworkRunner.js
│       └── pipeline-constants.js
└── utils/
    └── redisClient.js             ← esistente o da creare se non c'è
```

Il modulo pipeline viene registrato in `index.js` con una singola riga:

```javascript
const { PipelineCommandHandler } = require('./handlers/pipeline/PipelineCommandHandler');
const pipelineHandler = new PipelineCommandHandler(redisClient);
pipelineHandler.start();   // avvia il BRPOP loop in background
```

---

## 2. `pipeline-constants.js`

Costanti condivise tra i moduli pipeline.

```javascript
// handlers/pipeline/pipeline-constants.js

const PIPELINE_CONSTANTS = {
  // Canali Redis
  COMMANDS_KEY: process.env.REDIS_PIPELINE_COMMANDS_KEY || 'hcaire:pipeline:commands',
  EVENTS_CHANNEL: process.env.REDIS_PIPELINE_EVENTS_CHANNEL || 'hcaire:pipeline:events',

  // Filesystem
  // Cartella radice dove stanno i CLAUDE.md degli step
  STEPS_ROOT: process.env.PIPELINE_STEPS_ROOT ||
    'C:\\my\\claude\\claude-cowork\\Sviluppo Bambino\\input\\produzioni',

  // Cartella radice degli output della pipeline
  OUTPUT_ROOT: process.env.PIPELINE_OUTPUT_ROOT ||
    'C:\\my\\claude\\claude-cowork\\Sviluppo Bambino\\output\\produzioni',

  // Cartella degli input esterni forniti dal ricercatore
  INPUTS_ROOT: process.env.PIPELINE_INPUTS_ROOT ||
    'C:\\my\\claude\\claude-cowork\\Sviluppo Bambino\\input\\produzioni',

  // Timeout default per un'esecuzione Cowork (ms)
  DEFAULT_TIMEOUT_MS: parseInt(process.env.PIPELINE_DEFAULT_TIMEOUT_MS || '300000'),

  // Soglia per inline del contenuto JSON nel prompt (bytes)
  INLINE_FILE_THRESHOLD_BYTES: 50 * 1024,

  // Mapping step_id → cartella CLAUDE.md
  STEP_FOLDER_MAP: {
    'f2_step_1': 'f2-step-1-ricerca-temi',
    'f2_step_2': 'f2-step-2-rilevanza-strutturale',
    'f2_step_3': 'f2-step-3-verifica-strutturale',
    'f2_step_4': 'f2-step-4-micro-matrice',
    'f2_step_5': 'f2-step-5-output-family',
    'f3_step_1': 'f3-step-1-dispositivo-lettura',
    'f3_step_2': 'f3-step-2-stress-test',
    'f3_step_3': 'f3-step-3-correzione-strutturale',
    'f3_step_4': 'f3-step-4-indistinguibilità',
    'f3_step_5': 'f3-step-5-audit',
    'f3_step_6': 'f3-step-6-stabilizzazione-proxy',
    'f3_step_6b': 'f3-step-6-stabilizzazione-proxy',   // stesso folder, variante B
    'f3_step_6c': 'f3-step-6-stabilizzazione-proxy',   // stesso folder, variante C
    'f3_step_7': 'f3-step-7-trasferibilità-dispositivo',
    'f3_step_8': 'f3-step-8-adattamento-strutturale',
    'f3_step_9': 'f3-step-9-dispositivo-completo',
    'f3_step_10': 'f3-step-10-stress-test-dispositivo',
  },

  // Per step con varianti (6b, 6c): nome del file CLAUDE.md alternativo
  STEP_CLAUDE_FILE_MAP: {
    'f3_step_6':  'CLAUDE.md',
    'f3_step_6b': 'CLAUDE-B.md',
    'f3_step_6c': 'CLAUDE-C.md',   // se esiste, altrimenti fallback a CLAUDE.md
  },
};

module.exports = PIPELINE_CONSTANTS;
```

---

## 3. `PipelineCommandHandler.js`

Il loop principale che legge comandi da Redis e li dispatcha.

```javascript
// handlers/pipeline/PipelineCommandHandler.js

const { COMMANDS_KEY, EVENTS_CHANNEL } = require('./pipeline-constants');
const { PromptComposer } = require('./PromptComposer');
const { CoworkRunner } = require('./CoworkRunner');

class PipelineCommandHandler {
  constructor(redisClient) {
    // Due client Redis separati: uno per BRPOP (blocking), uno per PUBLISH
    this.redisReader = redisClient.duplicate();
    this.redisPublisher = redisClient.duplicate();
    this.activeExecutions = new Map();  // execution_id → { runner, command }
    this.composer = new PromptComposer();
    this.isRunning = false;
  }

  async start() {
    this.isRunning = true;
    console.log('[PipelineHandler] In ascolto su', COMMANDS_KEY);

    // Recupero di esecuzioni interrotte al riavvio (vedi §7)
    await this._recoverInterruptedExecutions();

    // Loop principale BRPOP
    while (this.isRunning) {
      try {
        // BRPOP blocca finché non arriva un messaggio (timeout 0 = infinito)
        const result = await this.redisReader.brpop(COMMANDS_KEY, 0);
        if (!result) continue;

        const [, rawMessage] = result;
        const command = JSON.parse(rawMessage);

        // Dispatch asincrono — non blocca il loop
        this._handleCommand(command).catch(err => {
          console.error('[PipelineHandler] Errore non gestito nel command handler:', err);
        });

      } catch (err) {
        if (!this.isRunning) break;
        console.error('[PipelineHandler] Errore nel BRPOP loop:', err);
        await this._sleep(1000);  // breve pausa prima di riprovare
      }
    }
  }

  stop() {
    this.isRunning = false;
    this.redisReader.disconnect();
    this.redisPublisher.disconnect();
  }

  async _handleCommand(command) {
    const { type, execution_id, step_id, context_id, run_number, payload } = command;

    switch (type) {
      case 'pipeline.step.run':
        await this._handleStepRun(command);
        break;

      case 'pipeline.step.cancel':
        await this._handleStepCancel(command);
        break;

      case 'pipeline.step.ping':
        await this._handlePing(command);
        break;

      default:
        console.warn('[PipelineHandler] Tipo comando non riconosciuto:', type);
    }
  }

  // ─── STEP RUN ───────────────────────────────────────────────────────────────

  async _handleStepRun(command) {
    const { execution_id, step_id, context_id, run_number, payload } = command;

    // Deduplicazione: se questa execution è già in corso, ignorare
    if (this.activeExecutions.has(execution_id)) {
      console.log(`[PipelineHandler] Execution ${execution_id} già in corso — BRPOP duplicato ignorato`);
      await this._publish({ ...command, type: 'pipeline.step.started', payload: { cowork_session_id: null } });
      return;
    }

    console.log(`[PipelineHandler] Avvio step ${step_id} (exec: ${execution_id}, run: #${run_number})`);

    // 1. Componi il prompt
    let composedPrompt;
    try {
      composedPrompt = await this.composer.compose(step_id, payload);
    } catch (err) {
      await this._publishFailed(command, 'sistema', `Errore composizione prompt: ${err.message}`, null);
      return;
    }

    // 2. Crea il runner Cowork
    const runner = new CoworkRunner({
      execution_id,
      step_id,
      prompt: composedPrompt,
      output_dir: payload.output_dir,
      output_filename: payload.output_filename,
      timeout_ms: payload.timeout_ms || require('./pipeline-constants').DEFAULT_TIMEOUT_MS,
      onLog: (text, level) => this._publishLog(command, text, level),
    });

    this.activeExecutions.set(execution_id, { runner, command });

    // 3. Pubblica started
    await this._publish({
      ...command,
      type: 'pipeline.step.started',
      payload: { cowork_session_id: null },
    });

    // 4. Lancia Cowork e attendi il risultato
    try {
      const result = await runner.run();

      this.activeExecutions.delete(execution_id);

      await this._publish({
        ...command,
        type: 'pipeline.step.completed',
        payload: {
          output_file: result.output_file,
          output_file_relative: result.output_file_relative,
          verifica_required: payload.verifica_required ?? false,
          summary: result.summary ?? null,
        },
      });

    } catch (err) {
      this.activeExecutions.delete(execution_id);

      const isTimeout = err.message?.includes('timeout');
      await this._publishFailed(
        command,
        isTimeout ? 'timeout' : 'cowork',
        err.message,
        err.partial_output ?? null
      );
    }
  }

  // ─── STEP CANCEL ────────────────────────────────────────────────────────────

  async _handleStepCancel(command) {
    const { execution_id, payload } = command;
    const active = this.activeExecutions.get(execution_id);

    if (!active) {
      console.log(`[PipelineHandler] Nessuna execution attiva con id ${execution_id} — cancel ignorato`);
      return;
    }

    console.log(`[PipelineHandler] Cancellazione execution ${execution_id}: ${payload.reason}`);
    await active.runner.cancel();
    this.activeExecutions.delete(execution_id);

    await this._publish({
      ...command,
      type: 'pipeline.step.cancelled',
      payload: { reason: payload.reason },
    });
  }

  // ─── PING ───────────────────────────────────────────────────────────────────

  async _handlePing(command) {
    await this._publish({
      ...command,
      type: 'pipeline.step.pong',
      payload: {
        server_version: '1.0.0',
        active_executions: this.activeExecutions.size,
        uptime_seconds: Math.floor(process.uptime()),
      },
    });
  }

  // ─── HELPERS ────────────────────────────────────────────────────────────────

  async _publish(event) {
    const message = JSON.stringify({
      ...event,
      timestamp: new Date().toISOString(),
      message_id: event.message_id || require('crypto').randomUUID(),
    });
    await this.redisPublisher.publish(EVENTS_CHANNEL, message);
  }

  async _publishLog(command, text, level = 'info') {
    await this._publish({
      ...command,
      type: 'pipeline.step.log',
      payload: { text, level },
    });
  }

  async _publishFailed(command, errorSource, errorMessage, partialOutput) {
    console.error(`[PipelineHandler] Step ${command.step_id} fallito (${errorSource}): ${errorMessage}`);
    await this._publish({
      ...command,
      type: 'pipeline.step.failed',
      payload: {
        error_source: errorSource,
        error_message: errorMessage,
        error_detail: null,
        partial_output_file: partialOutput,
      },
    });
  }

  async _recoverInterruptedExecutions() {
    // Al riavvio del server: notifica il backend delle execution rimaste in stato 'in_esecuzione'
    // Il backend aggiornerà il loro stato a 'fallito' tramite il watchdog (D3 §6)
    // Qui non facciamo nulla di attivo — il watchdog del backend se ne occupa.
    console.log('[PipelineHandler] Recovery check completato (watchdog backend gestisce le execution orfane)');
  }

  _sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

module.exports = { PipelineCommandHandler };
```

---

## 4. `PromptComposer.js`

Costruisce il prompt composito da passare a Cowork (D3 §12).

```javascript
// handlers/pipeline/PromptComposer.js

const fs = require('fs').promises;
const path = require('path');
const {
  STEPS_ROOT,
  STEP_FOLDER_MAP,
  STEP_CLAUDE_FILE_MAP,
  INLINE_FILE_THRESHOLD_BYTES,
} = require('./pipeline-constants');

class PromptComposer {

  /**
   * Costruisce il prompt composito per uno step.
   * @param {string} stepId  - es. "f3_step_3"
   * @param {object} payload - payload del comando step.run (D3 §3.1)
   * @returns {string} prompt completo da passare a Cowork
   */
  async compose(stepId, payload) {
    const block1 = await this._buildInputBlock(stepId, payload);
    const block2 = await this._loadAndCleanClaudeMd(stepId);
    const block3 = this._buildOutputBlock(payload);

    return [block1, block2, block3].join('\n\n');
  }

  // ─── BLOCCO 1: CONTESTO INPUT ─────────────────────────────────────────────

  async _buildInputBlock(stepId, payload) {
    const lines = [
      '---',
      'CONTESTO DI ESECUZIONE AUTOMATICA',
      `Step: ${stepId}  |  Run: #${payload.run_number ?? 1}`,
      '',
      'FILE DI INPUT DISPONIBILI',
    ];

    for (const inputFile of (payload.input_files || [])) {
      lines.push(`• [${inputFile.role}]  ${inputFile.path}`);

      try {
        const stats = await fs.stat(inputFile.path);
        if (stats.size <= INLINE_FILE_THRESHOLD_BYTES) {
          const content = await fs.readFile(inputFile.path, 'utf8');
          // Valida che sia JSON prima di includerlo inline
          JSON.parse(content);
          lines.push('  Contenuto:');
          lines.push('  ```json');
          lines.push(content.split('\n').map(l => '  ' + l).join('\n'));
          lines.push('  ```');
        } else {
          lines.push(`  (file > ${INLINE_FILE_THRESHOLD_BYTES / 1024}KB — leggi direttamente dal path)`);
        }
      } catch (err) {
        lines.push(`  (file non leggibile: ${err.message})`);
      }
    }

    // Input esterni forniti dal ricercatore
    const externalInputs = payload.external_inputs || [];
    if (externalInputs.length > 0) {
      lines.push('');
      lines.push('INPUT FORNITI DAL RICERCATORE');
      for (const ext of externalInputs) {
        lines.push(`${ext.input_id}:`);
        lines.push('```json');
        lines.push(JSON.stringify(ext.data, null, 2));
        lines.push('```');
      }
    }

    // Dispositivo sorgente (per step 7, 8, 9 di temi derivati)
    if (payload.dispositivo_sorgente) {
      lines.push('');
      lines.push('DISPOSITIVO SORGENTE (tema di origine)');
      lines.push(`• Tema: ${payload.dispositivo_sorgente.tema_id}`);
      lines.push(`• File: ${payload.dispositivo_sorgente.file}`);

      try {
        const content = await fs.readFile(payload.dispositivo_sorgente.file, 'utf8');
        lines.push('  Contenuto:');
        lines.push('  ```json');
        lines.push(content.split('\n').map(l => '  ' + l).join('\n'));
        lines.push('  ```');
      } catch {
        lines.push('  (file non leggibile — verifica il path)');
      }
    }

    lines.push('---');
    return lines.join('\n');
  }

  // ─── BLOCCO 2: CLAUDE.MD PULITO ──────────────────────────────────────────

  async _loadAndCleanClaudeMd(stepId) {
    const folder = STEP_FOLDER_MAP[stepId];
    if (!folder) throw new Error(`Step non mappato: ${stepId}`);

    // Determina il nome del file (CLAUDE.md, CLAUDE-B.md, CLAUDE-C.md)
    const filename = STEP_CLAUDE_FILE_MAP[stepId] || 'CLAUDE.md';
    const claudePath = path.join(STEPS_ROOT, folder, filename);

    let raw;
    try {
      raw = await fs.readFile(claudePath, 'utf8');
    } catch (err) {
      throw new Error(`CLAUDE.md non trovato in ${claudePath}: ${err.message}`);
    }

    return this._cleanClaudeMd(raw, stepId);
  }

  _cleanClaudeMd(raw, stepId) {
    let cleaned = raw;

    // 1. Rimuovi la sezione "### Salvataggio" (con varianti tipografiche)
    cleaned = cleaned.replace(
      /###\s*(Salvataggio|SALVATAGGIO|Output path|OUTPUT PATH)[\s\S]*?(?=\n###|\n---|\n##|$)/gi,
      ''
    );

    // 2. Rimuovi path hardcoded che iniziano con la lettera di drive Windows
    // (es. "C:\my\clauded\..." che potrebbero comparire in altri punti del testo)
    cleaned = cleaned.replace(
      /`[A-Z]:\\[^`\n]+`/g,
      '[path gestito automaticamente dal sistema]'
    );

    // 3. Per f3_step_10: sostituisci il template MICRO CASI con riferimento al Blocco 1
    if (stepId === 'f3_step_10') {
      cleaned = cleaned.replace(
        /```json\s*[\r\n]+"cases":\s*\[[\s\S]*?\]\s*```/g,
        '> I casi reali da usare per questo stress test sono specificati nel blocco "INPUT FORNITI DAL RICERCATORE" sopra (campo `cases`).'
      );
    }

    // 4. Aggiungi header che chiarisce a Cowork il contesto
    const header = [
      '---',
      'ISTRUZIONI STEP (esecuzione automatica — i file di input sono già elencati sopra)',
      '---',
      '',
    ].join('\n');

    return header + cleaned.trim();
  }

  // ─── BLOCCO 3: DIRETTIVA OUTPUT ──────────────────────────────────────────

  _buildOutputBlock(payload) {
    return [
      '---',
      'DIRETTIVA OUTPUT (ha priorità su qualsiasi percorso menzionato sopra)',
      '',
      `Salva il risultato con queste specifiche esatte:`,
      `• Nome file:  ${payload.output_filename}`,
      `• Cartella:   ${payload.output_dir}`,
      `• Formato:    JSON valido, nessun testo prima o dopo il JSON`,
      `• Encoding:   UTF-8`,
      '',
      'Non creare sottocartelle aggiuntive.',
      'Quando hai scritto il file, termina la risposta.',
      '---',
    ].join('\n');
  }
}

module.exports = { PromptComposer };
```

---

## 5. `CoworkRunner.js`

Lancia Cowork con il prompt composito, cattura l'output riga per riga, gestisce timeout e cancellazione.

```javascript
// handlers/pipeline/CoworkRunner.js

const { spawn } = require('child_process');
const fs = require('fs').promises;
const path = require('path');
const os = require('os');

class CoworkRunner {
  constructor({ execution_id, step_id, prompt, output_dir, output_filename, timeout_ms, onLog }) {
    this.execution_id = execution_id;
    this.step_id = step_id;
    this.prompt = prompt;
    this.output_dir = output_dir;
    this.output_filename = output_filename;
    this.timeout_ms = timeout_ms;
    this.onLog = onLog;
    this.process = null;
    this.isCancelled = false;
  }

  /**
   * Esegue Cowork con il prompt composito.
   * @returns {{ output_file: string, output_file_relative: string, summary: string|null }}
   */
  async run() {
    // 1. Scrivi il prompt su un file temporaneo
    const promptFile = path.join(os.tmpdir(), `pipeline-${this.execution_id}.md`);
    await fs.writeFile(promptFile, this.prompt, 'utf8');

    // 2. Assicurati che la cartella di output esista
    await fs.mkdir(this.output_dir, { recursive: true });

    const expectedOutputPath = path.join(this.output_dir, this.output_filename);

    try {
      await this._runCowork(promptFile);
    } finally {
      // Pulisci il file temporaneo
      await fs.unlink(promptFile).catch(() => {});
    }

    if (this.isCancelled) {
      throw new Error('Esecuzione cancellata');
    }

    // 3. Verifica che il file di output sia stato creato
    try {
      await fs.access(expectedOutputPath);
    } catch {
      throw new Error(`Cowork non ha prodotto il file atteso: ${expectedOutputPath}`);
    }

    // 4. Verifica che il file sia JSON valido
    const content = await fs.readFile(expectedOutputPath, 'utf8');
    try {
      JSON.parse(content);
    } catch {
      throw new Error(`Il file prodotto da Cowork non è JSON valido: ${expectedOutputPath}`);
    }

    // 5. Calcola il path relativo (relativo a PIPELINE_OUTPUT_ROOT)
    const outputRoot = require('./pipeline-constants').OUTPUT_ROOT;
    const relPath = path.relative(outputRoot, expectedOutputPath).replace(/\\/g, '/');

    return {
      output_file: expectedOutputPath,
      output_file_relative: relPath,
      summary: null,   // potrebbe essere estratto dal log in futuro
    };
  }

  async _runCowork(promptFile) {
    return new Promise((resolve, reject) => {
      // ── Adattare questa sezione all'API Cowork esistente nel server locale ──
      //
      // L'invocazione esatta dipende da come il server locale già lancia Cowork
      // negli altri flussi. Le opzioni tipiche sono:
      //
      // Opzione A: Claude Code CLI (se il server usa claude-code come CLI)
      //   this.process = spawn('claude', ['--print', '--file', promptFile], { ... })
      //
      // Opzione B: Cowork SDK (se usa l'SDK direttamente)
      //   this.process = spawn('node', ['-e', `require('cowork').run('${promptFile}')`], { ... })
      //
      // Opzione C: Script dedicato già presente nel server locale
      //   this.process = spawn('node', ['./scripts/run-cowork.js', promptFile], { ... })
      //
      // Usare il pattern già in uso negli altri handler del server locale.
      // ─────────────────────────────────────────────────────────────────────

      const args = this._buildCoworkArgs(promptFile);
      this.process = spawn(args.command, args.params, {
        cwd: args.cwd || process.cwd(),
        env: { ...process.env, ...args.env },
      });

      let stderrBuffer = '';

      // Cattura stdout riga per riga → pubblica come log
      const readline = require('readline');
      const rl = readline.createInterface({ input: this.process.stdout });
      rl.on('line', (line) => {
        if (line.trim()) {
          this.onLog(line, 'info');
        }
      });

      // Cattura stderr per diagnostica
      this.process.stderr.on('data', (data) => {
        const text = data.toString();
        stderrBuffer += text;
        if (text.trim()) {
          this.onLog(text.trim(), 'warn');
        }
      });

      // Timeout
      const timer = setTimeout(() => {
        this.onLog(`Timeout dopo ${this.timeout_ms}ms — processo terminato`, 'error');
        this._killProcess();
        reject(Object.assign(new Error(`timeout`), { message: `Timeout: nessuna risposta dopo ${this.timeout_ms / 1000}s` }));
      }, this.timeout_ms);

      this.process.on('close', (code) => {
        clearTimeout(timer);
        if (this.isCancelled) {
          resolve();  // la cancellazione è gestita da cancel()
          return;
        }
        if (code === 0) {
          resolve();
        } else {
          reject(new Error(`Cowork terminato con exit code ${code}. Stderr: ${stderrBuffer.slice(-500)}`));
        }
      });

      this.process.on('error', (err) => {
        clearTimeout(timer);
        reject(new Error(`Impossibile avviare Cowork: ${err.message}`));
      });
    });
  }

  /**
   * Costruisce i parametri di spawn per Cowork.
   * DA ADATTARE al pattern già in uso nel server locale.
   */
  _buildCoworkArgs(promptFile) {
    // Placeholder — sostituire con l'invocazione effettiva usata negli altri handler
    return {
      command: 'claude',
      params: ['--print', '--file', promptFile],
      cwd: undefined,
      env: {},
    };
  }

  async cancel() {
    this.isCancelled = true;
    this._killProcess();
  }

  _killProcess() {
    if (this.process && !this.process.killed) {
      try {
        process.kill(this.process.pid, 'SIGTERM');
        setTimeout(() => {
          if (this.process && !this.process.killed) {
            process.kill(this.process.pid, 'SIGKILL');
          }
        }, 3000);
      } catch (err) {
        // processo già terminato
      }
    }
  }
}

module.exports = { CoworkRunner };
```

---

## 6. Integrazione con il comando Redis del backend

Il backend (D3 §3.1) invia nel payload del comando `pipeline.step.run` il campo `input_files` come array di oggetti `{ role, path }` con path **assoluti sul filesystem del server locale**.

Questo funziona perché backend e server locale condividono lo stesso filesystem (server locale gira sulla stessa macchina del backend, o su una macchina con accesso agli stessi path).

Se in futuro backend e server locale dovessero girare su macchine diverse, i path assoluti andrebbero sostituiti con URL di download. Per ora il design a filesystem condiviso è corretto e sufficiente.

---

## 7. Gestione del riavvio

Quando il server locale si riavvia mentre un'esecuzione è in corso:

1. `activeExecutions` è in memoria → viene perso.
2. Il watchdog del backend (D3 §6) rileva le execution bloccate in `in_esecuzione` su MongoDB e le porta a `fallito` dopo il grace period.
3. **Non è necessario** che il server locale faccia nulla di attivo al riavvio — il backend gestisce il recovery.

L'unica azione al riavvio è svuotare eventuali file temporanei `.md` lasciati in `os.tmpdir()` da sessioni interrotte:

```javascript
// In PipelineCommandHandler.start(), prima del loop
async _recoverInterruptedExecutions() {
  const tmpDir = require('os').tmpdir();
  const files = await fs.readdir(tmpDir);
  const orphaned = files.filter(f => f.startsWith('pipeline-') && f.endsWith('.md'));
  for (const f of orphaned) {
    await fs.unlink(path.join(tmpDir, f)).catch(() => {});
  }
  console.log(`[PipelineHandler] Cleanup: rimossi ${orphaned.length} file temporanei orfani`);
}
```

---

## 8. Checklist prima di avviare

Prima di attivare il `PipelineCommandHandler` in produzione, verificare:

- [ ] `PIPELINE_STEPS_ROOT` punta alla cartella `input/produzioni/` dove stanno i CLAUDE.md degli step.
- [ ] `PIPELINE_OUTPUT_ROOT` punta alla cartella `output/produzioni/` dove devono andare i file prodotti.
- [ ] Tutti i CLAUDE.md degli step esistono nella cartella mappata da `STEP_FOLDER_MAP`.
- [ ] Per step 6b e 6c: esistono `CLAUDE-B.md` e `CLAUDE-C.md` nelle rispettive cartelle.
- [ ] `_buildCoworkArgs()` in `CoworkRunner.js` è adattato all'API Cowork effettivamente in uso nel server locale.
- [ ] Il Redis client condiviso supporta `.duplicate()` (ioredis lo supporta nativamente).
- [ ] La cartella di output esiste e il processo ha permessi di scrittura.
- [ ] Testare con un `pipeline.step.ping` prima di tentare un `pipeline.step.run` reale.

---

## 9. Test isolato del PromptComposer

Prima di collegare tutto al Redis, testare il `PromptComposer` in isolamento:

```javascript
// test-composer.js — eseguire con: node test-composer.js

const { PromptComposer } = require('./handlers/pipeline/PromptComposer');

async function test() {
  const composer = new PromptComposer();

  const prompt = await composer.compose('f3_step_3', {
    run_number: 1,
    input_files: [
      { role: 'lettura-configurazionale', path: 'C:\\...\\lettura-configurazionale-v1.json' },
      { role: 'stress-test', path: 'C:\\...\\stress-test-v1.json' },
    ],
    external_inputs: [],
    dispositivo_sorgente: null,
    output_dir: 'C:\\...\\output\\produzioni\\temi\\pointing\\',
    output_filename: 'correzione-strutturale-v1.json',
  });

  console.log('=== PROMPT COMPOSITO ===');
  console.log(prompt);
  console.log('=== FINE ===');
  console.log(`Lunghezza: ${prompt.length} caratteri`);
}

test().catch(console.error);
```

Verificare che:
1. Il Blocco 1 contenga i file di input con il loro contenuto JSON.
2. Il Blocco 2 contenga le istruzioni del CLAUDE.md senza path hardcoded e senza la sezione Salvataggio.
3. Il Blocco 3 contenga il path di output corretto.
