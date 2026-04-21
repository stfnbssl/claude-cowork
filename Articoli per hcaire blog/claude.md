# Workflow Automatico Articoli - Cowork

## Istruzioni Generali

Questo file contiene indicazioni per la produzione di uno o più articoli. Segui le seguenti fasi per ogni articolo.

---

## STRUTTURA DEL FILE DI INPUT

Il file contiene **uno o più tracce di articoli** separati dal seguente marcatore:

```
===== NUOVO ARTICOLO =====
articleRequestId xxxxxxxxxx
```

La traccia di un articolo può essere sia di una o poche parole
che articolata o complessa a piacere. Quando molto semplice usa la fantasia per svilupparla
a sufficenza come input per la produzione di un buon articolo. 

---

## WORKFLOW PER OGNI ARTICOLO

### FASE 1: Ricerca Fonti

1. **Analizza** i contenuti richiesti e identifica 3-4 query di ricerca principali
2. **Ricerca** online per trovare:
   - Almeno 5 fonti diverse (articoli, pagine web, post social, ricerche)
   - Prediligi: siti autorevoli, studi recenti, expert opinion
   - Almeno 2 fonti devono essere primarie (ricerche originali, dati, testimonianze dirette)

3. **Crea la cartella** di lavoro:
   ```
   work/
   ├── [nome_articolo]/
   │   ├── fonti.md
   │   ├── articolo.md
   │   └── metadata.json
   ```

4. **Salva le fonti** in `fonti.md` con questo formato:
   ```markdown
   # Fonti - [Nome Articolo]

   ## Fonte 1
   - **Titolo**: [titolo completo]
   - **URL**: [link]
   - **Tipo**: [articolo/ricerca/post/pagina]
   - **Autore/Fonte**: [chi ha scritto]
   - **Data**: [quando pubblicato]
   - **Rilevanza**: [2-3 righe su perché è importante per questo articolo]

   ## Fonte 2
   [stesso formato]
   ...
   ```

---

### FASE 2: Scrittura Articolo

1. **Usa le fonti** per supportare ogni claim principale
2. **Rispetta rigorosamente**:
   - Il tono e lo stile indicati
   - La lunghezza approssimativa
   - I punti di contenuto richiesti
   - Citazioni e attribuzioni corrette

3. **Struttura consigliata**:
   ```
   # [Titolo Articolo]

   **Introduzione** (50-100 parole)
   
   ## Sezione 1
   [contenuto]
   
   ## Sezione 2
   [contenuto]
   
   ## Conclusione
   [sintesi e call-to-action se appropriato]
   ```

4. **Salva** l'articolo in `articolo.md`

---

### FASE 3: Generazione Metadata JSON

Crea un file `metadata.json` per ogni articolo con questa struttura:

```json
{
  "slug": "nome-articolo-in-kebab-case",
  "titolo": "Titolo Completo dell'Articolo",
  "descrizione": "Una descrizione accattivante di 120-160 caratteri per SEO/preview",
  "categoria": "Categoria principale",
  "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
  "data_creazione": "YYYY-MM-DD",
  "lunghezza_parole": 1500,
  "autore": "Cowork",
  "fonti_usate": [
    "URL fonte 1",
    "URL fonte 2",
    "URL fonte 3",
    "URL fonte 4",
    "URL fonte 5"
  ]
}
```

**Linee guida per i campi**:
- `slug`: minuscolo, solo lettere numeri e trattini (es: "come-scrivere-meglio")
- `descrizione`: accattivante, con parole chiave SEO
- `tags`: max 5, rilevanti e SEO-friendly
- `categoria`: scegli tra quelle esistenti o crea nuova se necessario

---

## ORGANIZZAZIONE CARTELLE

```
work/
├── articolo-1/
│   ├── fonti.md
│   ├── articolo.md
│   └── metadata.json
├── articolo-2/
│   ├── fonti.md
│   ├── articolo.md
│   └── metadata.json
├── articolo-3/
│   ├── fonti.md
│   ├── articolo.md
│   └── metadata.json
└── README.md (elenco articoli completati)
```

---

## QUALCHECKLIST FINALE PER OGNI ARTICOLO

- [ ] Almeno 5 fonti diverse trovate e documentate
- [ ] Articolo scritto nel tono/stile richiesto
- [ ] Lunghezza rispettata (±10%)
- [ ] Tutti i punti di contenuto copertati
- [ ] Citazioni attribuite correttamente
- [ ] Slug in kebab-case
- [ ] Descrizione SEO ottimizzata
- [ ] Tags rilevanti e coerenti
- [ ] File JSON ben formattato
- [ ] Cartella organizzata con i 3 file richiesti

---

## PROCESSO DI SOSTITUZIONE FILE INPUT

1. **Primo ciclo**: Crei il file `input_articoli.md` con i tuoi articoli
2. **Cowork processa** e crea tutti i file in `work/`
3. **Secondo ciclo**: Sostituisci il contenuto di `input_articoli.md` con i NUOVI articoli
4. **Cowork ricomincia** il ciclo con nuovi articoli (le cartelle vecchie rimangono intatte in `work/`)

---

## NOTE IMPORTANTI

- **Ricerca**: Usa SEMPRE strumenti di ricerca web contemporanei per garantire informazioni aggiornate
- **Validazione fonti**: Verifica l'autorevolezza dei siti prima di usarli
- **Coerenza tono**: Controlla che l'articolo finale sia coerente nel tono dall'inizio alla fine
- **SEO**: Inserisci parole chiave naturalmente, non forzatamente
- **Link**: Se possibile, includici link alle fonti nel testo dove rilevante (senza esagerare)

---

## Post-generazione

  Al termine dell'elaborazione di tutti gli articoli in `input_articoli.md`:

  1. Crea la cartella `trace articoli creati/` nella directory del progetto se non      
  esiste
  2. Salva una copia di `input_articoli.md` in `trace articoli creati/` con nome        
  `YYYY-MM-DD_HH-MM-SS_input.md` (timestamp del momento)
  3. Svuota completamente `input_articoli.md` (lascialo vuoto, non eliminarlo)

  Esegui questi passi solo se la generazione è completata senza errori critici.

## Pubblicazione articoli sul blog

Quando il prompt contiene "pubblicali sul blog", dopo aver generato ogni articolo
esegui una richiesta HTTP per pubblicarlo:

- **Endpoint**: POST https://hcaire-blog-server-production.up.railway.app/api/contents/import
- **Header**: Authorization: Bearer 12969c64bd0742fad24913b1e7190255509c4b4dd3de31937fbd4de9563e0a36
- **Header aggiuntivo**: Content-Type: application/json
- **Body**:
   -- isPublished: true
   -- isPinned: false
   -- autore: "stfnbssl"
   -- articleRequestId: fornito nel file di input
   -- contenuto: il contenuto di articolo.md
   ... tutte le proprietà in metadata.json

Usa `curl` per la richiesta:
```bash
curl -s -X POST https://hcaire-blog-server-production.up.railway.app/api/contents/import \
  -H "Authorization: Bearer 12969c64bd0742fad24913b1e7190255509c4b4dd3de31937fbd4de9563e0a36" \
  -H "Content-Type: application/json" \
  -d '{ ...body descritto in precedenza... }'
```

Se la risposta è HTTP 201, la pubblicazione è avvenuta con successo.
Se la risposta è HTTP 400 con "Slug già esistente", l'articolo è già pubblicato — prosegui.
Per altri errori, segnalali nel report finale.
