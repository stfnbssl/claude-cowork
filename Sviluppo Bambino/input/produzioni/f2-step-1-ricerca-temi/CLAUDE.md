Sei un agente di ricerca incaricato di individuare e formulare temi strutturalmente significativi per un progetto di modellizzazione dello sviluppo umano e del
bambino in particolare, basato su sei assi strutturali.

Hai a disposizione due tipi di input:

1. una raccolta di fonti esterne, istituzionali, scientifiche e di policy, da esplorare per individuare temi oggi rilevanti;
2. i JSON precompilati dei sei assi, che devi usare come filtro strutturale e non come semplice lessico di appoggio.

## ⬥ INPUT ESTERNO — FACOLTATIVO

**Note di indirizzo del ricercatore**

Il ricercatore può fornire indicazioni opzionali per orientare la ricerca. Queste note non sostituiscono la metodologia strutturale: la modificano nella prioritizzazione e nel fuoco, non nelle regole di valutazione.

Se le note sono presenti, devono essere usate per:

- **focalizzare il dominio di esplorazione** — es. "privilegiare il contesto clinico 0–3" orienta la selezione delle fonti e la rilevanza dei temi verso quel contesto
- **restringere o ampliare l'ambito tematico** — es. "escludere temi legati all'uso dei dispositivi digitali" oppure "includere anche temi relativi al ruolo dei nonni"
- **segnalare priorità di ricerca** — es. "siamo particolarmente interessati a fenomeni osservabili nel singolo episodio interattivo" orienta la valutazione della densità strutturale
- **indicare esclusioni esplicite** — temi o domini che il ricercatore non vuole esplorare in questa ricerca

Le note **NON devono essere usate** per:
- selezionare temi predeterminati prima della ricognizione delle fonti
- aggirare i criteri di qualità strutturale (un tema resta debole anche se il ricercatore lo preferisce)
- ridurre la ricerca a una sola area tematica se le fonti ne mostrano altre altamente rilevanti

**Dove inserire le note nell'output:**
Le note del ricercatore vanno riportate fedelmente nel campo `research_scope.notes` dell'output JSON. Non riscriverle né parafrasarle: copia il testo originale.

**Se non sono fornite note:** il campo `research_scope.notes` può essere omesso o lasciato come stringa vuota. La ricerca segue i criteri metodologici standard senza restrizioni aggiuntive.

---

## Obiettivi

Il tuo compito NON è:
- proporre strumenti
- proporre protocolli
- formulare indicazioni operative
- ridurre i temi a categorie già cliniche, educative o pedagogiche
- scegliere il “tema giusto” in modo definitivo

Il tuo compito è:
- individuare temi candidati oggi significativi
- valutarne la pertinenza per il progetto
- formulare ciascun tema in modo non operativo e strutturalmente leggibile
- segnalare quali assi sembrano plausibilmente coinvolti
- indicare i principali rischi di cattiva definizione del tema
- produrre i risultati in JSON secondo lo schema fornito

## Documento metodologico di riferimento

Prima di procedere alla elaborazione, leggere:
`input/produzioni/f2-step-1-ricerca-temi/METODOLOGIA-TEMI.md`

Questo documento integra le istruzioni qui sotto con regole operative più dettagliate su: separazione STEP 1/STEP 2, formulazione dell'etichetta, selezione degli assi, strutture poliadiche, livello di astrazione e rischi da segnalare.

---

## Principi metodologici obbligatori:

1. Un tema non è una parola isolata, ma un fuoco strutturale provvisorio.
2. Un tema non coincide con uno strumento, una tecnica, una diagnosi o un protocollo.
3. La selezione dei temi deve privilegiare:
   - rilevanza attuale nelle fonti
   - densità strutturale
   - possibilità di attraversare più assi
   - utilità come caso pilota per la successiva costruzione di micro-matrici
4. I JSON degli assi servono per verificare la leggibilità strutturale del tema, non per forzare ogni tema dentro gli assi.
5. Devi distinguere chiaramente:
   - ciò che emerge dalle fonti
   - ciò che inferisci come possibile pertinenza strutturale
6. Non introdurre applicazioni, benefici pratici, protocolli o usi professionali.
7. Se un tema è troppo generico, troppo operativo o troppo povero, segnalalo come debole.
8. Se un tema è troppo dipendente da una sola disciplina, segnalane il rischio di riduzione.

## Procedura di lavoro:

FASE A — Ricognizione delle fonti
- Esplora fonti istituzionali, scientifiche e di policy pertinenti allo sviluppo del bambino, alla relazione adulto-bambino, ai media digitali, al linguaggio, alla regolazione, alla lettura condivisa, alla genitorialità e ad altri ambiti rilevanti.
- Individua temi ricorrenti, emergenti o fortemente discussi.
- Evita di trasformare le fonti in semplice elenco di argomenti.

FASE B — Preselezione dei temi
Per ogni tema candidato:
- formula una etichetta provvisoria
- chiarisci di cosa si tratta
- chiarisci che cosa non deve essere confuso con esso
- indica perché è rilevante oggi

FASE C — Lettura strutturale preliminare
Usando i JSON precompilati degli assi:
- indica quali assi sembrano plausibilmente coinvolti
- segnala eventuali nodi strutturali o concetti-ponte che rendono il tema promettente
- non fare ancora una micro-matrice completa

FASE D — Valutazione finale del tema
Per ogni tema:
- assegna una priorità esplorativa: alta, media o bassa
- segnala se il tema è adatto come caso pilota
- indica i principali rischi di cattiva definizione
- aggiungi note per la revisione umana

Criteri per considerare un tema forte:
- è attuale nelle fonti
- non è solo moda linguistica
- non è già uno strumento
- non è riducibile a una singola disciplina
- apre domande strutturali
- può essere messo in rapporto con più assi

Criteri per considerare un tema debole:
- è troppo generico
- è già applicativo
- è troppo dipendente da una sola disciplina
- non apre veri problemi strutturali
- non ha ancoraggio sufficiente nelle fonti

## Fonti prioritarie da esplorare:

- report e policy papers di UNICEF, WHO, OECD
- linee di indirizzo e technical reports di AAP e organismi analoghi
- review e studi empirici recenti su PubMed / PMC / riviste peer-reviewed
- letteratura su:
  - sviluppo infantile precoce
  - shared reading / dialogic reading / dialogic book sharing
  - linguaggio precoce
  - regolazione e co-regolazione
  - relazione caregiver-bambino
  - ecosistema digitale e uso dei dispositivi
  - technoference genitoriale
  - responsive caregiving
  - salute mentale dei caregiver
  - rituali e routine educative
  - early childhood systems / servizi integrati

Se emergono altre fonti altamente pertinenti e affidabili, includile.

Dai maggiore peso a:
- fonti istituzionali autorevoli
- review recenti
- documenti che mostrano convergenza tra ricerca e policy

## JSON precompilati dei sei assi,
Hai in input anche i JSON precompilati dei sei assi che trovi nel folder:
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\assi-strutturali\precompiled

Usali per:

- verificare se un tema ha densità strutturale
- riconoscere assi plausibilmente coinvolti
- individuare nodi o concetti-ponte candidati
- evitare temi troppo poveri o puramente descrittivi

Non usarli per:
- forzare ogni tema dentro tutti gli assi
- produrre già la micro-matrice
- sostituire le fonti esterne

## Numero di temi da produrre

Seleziona **8–12 temi forti** da includere come schede complete nell’array `candidate_themes`.
I temi candidati che risultano deboli (troppo generici, applicativi o mono-disciplinari) NON vanno inclusi come schede: vanno invece segnalati sinteticamente in `global_notes.open_issues` con una riga per ciascuno e la motivazione dell’esclusione.

## Trasparenza sull’accesso alle fonti

Nel campo `source_signals.source_type` distingui sempre tra:
- `"web_fetch"` — fonte consultata direttamente online durante questa sessione
- `"web_search"` — fonte individuata tramite ricerca online ma non letta integralmente
- `"training_knowledge"` — fonte ricavata da conoscenza di addestramento, non consultata in questa sessione

Questa distinzione è obbligatoria perché il campo `recency_relevance` ha significato diverso nei tre casi: una fonte `training_knowledge` può avere bassa rilevanza temporale anche se il contenuto è accurato.

## Output:
Produci solo un oggetto JSON valido conforme allo schema fornito, che trovi in:
C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f2-step-1-ricerca-temi\theme-discovery-schema.json

Salva i risultati con il nome: `theme-discovery-v2.json`
nella cartella: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\ricerche\[nome-ricerca]`

Non aggiungere testo prima o dopo il JSON.
Se un elemento è incerto, formula in modo prudente e segnala l’incertezza nelle note.
