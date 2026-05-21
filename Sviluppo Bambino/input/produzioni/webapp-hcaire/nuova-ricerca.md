# Istruzioni per Claude Code — Pagina "Nuova Ricerca"

Questo documento descrive le modifiche da apportare all'applicazione web HCAIRE per implementare la pagina di avvio di una nuova ricerca, integrando la pipeline F2 Step 1.

---

## Contesto

La pipeline di ricerca parte da uno **Step 1** che esplora fonti e produce un elenco di temi strutturali candidati. Questo step è guidato da un agente Cowork (Claude) che legge il file:

```
input/produzioni/f2-step-1-ricerca-temi/CLAUDE.md
```

Per avviare correttamente questo step, l'agente ha bisogno di due informazioni fornite dal ricercatore:

1. **ID della ricerca** — identifica la cartella di output dove verranno salvati tutti i file della ricerca
2. **Note di indirizzo** (opzionale) — testo libero che orienta la ricerca su contesti, temi o esclusioni di interesse del ricercatore

---

## Pagina da implementare

### Percorso suggerito
`/ricerche/nuova` o `/nuova-ricerca`

### Struttura della pagina

La pagina deve presentare:

**1. Testo esplicativo**
Visualizzare il contenuto del file:
```
output/metodologia/nuova-ricerca-testo-webapp.md
```
Renderizzato come Markdown. Questo testo spiega al ricercatore cosa sta per fare, come scegliere l'ID e come scrivere note efficaci.

**2. Form di input** con due campi:

```
Campo 1: ID Ricerca
  - label: "ID ricerca"
  - tipo: text input
  - placeholder: "es. lettura-condivisa-0-3"
  - validazione: obbligatorio, pattern kebab-case (solo minuscole, cifre, trattini)
  - descrizione sotto il campo: "Identifica questa ricerca in modo univoco. Usato come nome della cartella di output."

Campo 2: Note di indirizzo
  - label: "Note di indirizzo (opzionale)"
  - tipo: textarea
  - placeholder: "Es. Privilegiare temi osservabili in episodi brevi in contesti clinici 0–3. Sono interessato a fenomeni di regolazione corporea nella diade..."
  - descrizione sotto il campo: "Orientano il fuoco della ricerca senza vincolarla. L'agente le userà per prioritizzare fonti e temi, non per predeterminare i risultati."
```

**3. Pulsante di avvio**
- Label: "Avvia la ricerca"
- Azione: costruisce il prompt Cowork e lo invia alla pipeline

---

## Costruzione del prompt per la pipeline

Quando il ricercatore clicca "Avvia la ricerca", il sistema deve:

**1. Verificare che l'ID non sia già in uso**

Controllare se esiste già la cartella:
```
output/produzioni/ricerche/{ricerca_id}/
```
Se esiste, mostrare un errore: *"Una ricerca con questo ID esiste già. Scegli un ID diverso."*

**2. Creare la cartella di output**

```
output/produzioni/ricerche/{ricerca_id}/
```

**3. Costruire il prompt Cowork** (tre blocchi, come da architettura D3 §12)

```
[Blocco 1 — istruzioni agente]
Contenuto di: input/produzioni/f2-step-1-ricerca-temi/CLAUDE.md

[Blocco 2 — input dati]
{
  "ricerca_id": "{ricerca_id}",
  "research_scope": {
    "notes": "{note_ricercatore}"   ← omettere il campo se le note sono vuote
  }
}

[Blocco 3 — istruzione di output]
Salva i risultati con il nome: theme-discovery-v2.json
nella cartella: C:/my/claude/claude-cowork\Sviluppo Bambino\output\produzioni\ricerche\{ricerca_id}\
```

**Nota**: se il campo note è vuoto, omettere la chiave `research_scope.notes` (o inviare `null`). L'agente tratterà l'assenza come "nessuna restrizione".

**4. Avviare la pipeline**

Inviare il prompt costruito a Cowork tramite il meccanismo di orchestrazione esistente (Redis, canale pipeline), specificando:
- `step`: `f2_step_1`
- `ricerca_id`: `{ricerca_id}`
- `stato_atteso_dopo`: `attende_revisione_step1`

---

## Stato della ricerca dopo l'avvio

Al termine dello step 1, il file `theme-discovery-v2.json` viene salvato nella cartella della ricerca. La ricerca entra nello stato `attende_revisione_step1`.

La pagina di dettaglio della ricerca (da implementare separatamente) dovrà permettere al ricercatore di:
- leggere i temi candidati prodotti dallo step 1
- selezionare quale/i temi portare allo step 2
- approvare o rigettare l'output prima di procedere

---

## File di riferimento

| File | Ruolo |
|---|---|
| `input/produzioni/f2-step-1-ricerca-temi/CLAUDE.md` | Istruzioni per l'agente (include sezione INPUT ESTERNO aggiornata) |
| `input/produzioni/f2-step-1-ricerca-temi/theme-discovery-schema.json` | Schema JSON dell'output atteso |
| `output/metodologia/nuova-ricerca-testo-webapp.md` | Testo esplicativo da mostrare nella pagina |
| `output/produzioni/ricerche/` | Cartella radice di tutte le ricerche |

---

## Nota sulla sezione INPUT ESTERNO nel CLAUDE.md

Il file `f2-step-1-ricerca-temi/CLAUDE.md` è già stato aggiornato con una sezione **"⬥ INPUT ESTERNO — FACOLTATIVO"** che spiega all'agente come:
- recepire le note del ricercatore
- usarle per orientare fonte e temi
- riportarle nel campo `research_scope.notes` dell'output JSON

Non è necessario modificare ulteriormente questo file. La sezione è già operativa.