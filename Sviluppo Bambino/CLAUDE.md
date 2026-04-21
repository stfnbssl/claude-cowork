# Progetto: Sviluppo Bambino (laboratorio HCAIRE)

## Contesto
Il progetto elabora i documenti prodotti nel laboratorio HCAIRE riguardanti
**obiettivi e metodologia** del progetto "Sviluppo Bambino". Lo scopo è
trasformare i documenti Word originali (scaricati da Google Documents) in
**dati strutturati** che alimenteranno il sito HCAIRE per:

- presentare il progetto "Sviluppo Bambino" al pubblico,
- fornire strumenti operativi utili alla sua realizzazione.

Il lavoro è organizzato in due step successivi: prima Markdown editabile,
poi JSON consumabile dall'applicazione web.

---

## Struttura delle cartelle

| Percorso | Ruolo |
|---|---|
| `input/obiettivi e metodologia/` | Documenti Word di partenza (sorgenti Google Docs). **Non modificare.** |
| `input/pre elaborazioni/` | Documenti in cui l'utente ha iniziato manualmente lo step 1 e chiede di proseguire. |
| `output/step 1/` | Output dello step 1 — file Markdown con metadati di classificazione. |
| `output/step 2/` | Output dello step 2 — file JSON finali per il sito. |
| `agenda.md` | Elenco aggiornato dei task da svolgere. **Leggere all'inizio di ogni sessione.** |
| `claude.md` | Questo file — istruzioni permanenti di progetto. |

---

## Flusso di lavoro

### Step 1 — Estrazione in Markdown con metadati

Partendo dai file Word in `input/obiettivi e metodologia/`, produrre in
`output/step 1/` un documento Markdown per ciascun documento sorgente,
composto da:

1. **Front matter YAML** con i metadati di classificazione.
2. **Corpo in Markdown** con il contenuto estratto e formattato in modo pulito
   (titoli coerenti, liste, rimozione di artefatti di conversione da Word).

Schema di front matter (**essenziale per design**):

> **Principio guida:** il front matter dello step 1 è intenzionalmente minimale.
> I documenti di input non verranno trasformati in JSON conservando la loro
> fisionomia originale: i JSON finali saranno tutti frutto di rielaborazioni.
> È al momento della rielaborazione (step 2) che vanno definite esaustivamente
> le proprietà semantiche. Il front matter qui serve solo a identificare e
> tracciare il documento sorgente.

```yaml
---
id:               # slug univoco in kebab-case, es. f6-1-abstract-istituzionale
titolo:           # titolo leggibile del documento
fase:             # numero della fase di appartenenza, es. "6"
fonte:            # nome del file Word originale
data_estrazione:  # YYYY-MM-DD
stato: bozza      # bozza | in-revisione | finale
---
```

> L'utente può intervenire manualmente sui file in `output/step 1/` per
> correzioni e aggiustamenti prima di passare allo step 2.

### Step 2 — Conversione in JSON

Partendo dai Markdown in `output/step 1/` (eventualmente revisionati a mano),
produrre in `output/step 2/` un file JSON per documento, dove:

- i metadati del front matter diventano **proprietà dell'oggetto JSON**,
- il corpo Markdown viene **preservato integralmente come stringa** in una
  proprietà dedicata, pronta per essere renderizzata dal sito.

Schema JSON proposto (**da confermare**):

```json
{
  "id": "obiettivi-generali-v1",
  "titolo": "…",
  "tipo": "obiettivo",
  "progetto": "sviluppo-bambino",
  "laboratorio": "HCAIRE",
  "fonte": "…docx",
  "data_estrazione": "2026-04-21",
  "stato": "finale",
  "tag": [],
  "contenuto_md": "# … \n\n…"
}
```

### Caso speciale: documenti pre-elaborati

Per i file in `input/pre elaborazioni/`:

- **Rispettare** struttura, metadati e scelte editoriali già impostate dall'utente.
- Completare solo le parti mancanti, senza riscrivere ciò che è stato curato a mano.
- Allineare il risultato finale allo stesso formato atteso in `output/step 1/`.

---

## Regole operative

1. All'avvio di ogni sessione, **leggere `agenda.md`** per sapere cosa fare.
2. **Non modificare mai** i file in `input/obiettivi e metodologia/`.
3. Mantenere **uno schema di metadati coerente** tra tutti i documenti.
4. Lingua dei contenuti e dei metadati: **italiano**.
5. Nomi dei file di output: slug in kebab-case, stessa radice per step 1 e step 2
   (es. `obiettivi-generali.md` → `obiettivi-generali.json`). **Da confermare.**

---

## Punti aperti da definire insieme

- [ ] Schema definitivo del front matter YAML (quali campi sono obbligatori? vocabolari controllati per `tipo` e `tag`?)
- [ ] Schema JSON definitivo dello step 2 (nome della proprietà che contiene il Markdown, eventuali campi aggiuntivi richiesti dal sito)
- [ ] Granularità: **un file di output per ogni file di input**, oppure è previsto split (un Word → più documenti logici) o merge?
- [ ] Convenzione di nomenclatura dei file di output
- [ ] Gestione delle immagini eventualmente contenute nei Word (estrazione? link? cartella `assets/`?)