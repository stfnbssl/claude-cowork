HCAIRE ha l’obiettivo ambizioso di sviluppare strumenti basati sull’intelligenza artificiale a supporto di chi, a livello clinico, pedagogico, genitoriale e istituzionale si adopera per il miglioramento dello sviluppo umano ed in particolare dello sviluppo del bambino. Lo fa con un approccio tecnico-scientifico e filosofico, rispettoso della dimensione umana e del lavoro dei suoi destinatari.

La produzione degli strumenti avviene attraverso un processo in più stadi assistito dalla IA:

1. Costruzione e integrazione dei fondamenti filosofici, neuroscientifici e psicologici.
2. Traduzione dei fondamenti in criteri operativi e “skill”, che orientano l’interpretazione dei contenuti.
3. Individuazione degli ambiti di applicazione (clinico, pedagogico, genitoriale, istituzionale) e costruzione delle relative traduzioni interdisciplinari.
4. Costruzione delle “skill” specifiche per ciascun ambito operativo.
5. Gestione delle “skill” di personalizzazione elaborate e caricate dagli utenti.
6. Generazione degli output: articoli, griglie osservazionali, proposte di intervento e case studies.

Le “skill” costituiscono unità operative che traducono il modello HCAIRE in istruzioni utilizzabili dai sistemi di IA.

La elaborazione delle skill di fondamento e delle traduzioni interdisciplinari è a discrezione del comitato di direzione di HCAIRE. L’utente può contribuire attraverso skill di personalizzazione, che vengono integrate e valutate dagli agenti IA durante la produzione degli output.

Le traduzioni interdisciplinari mettono in evidenza i nodi trasversali che collegano i fondamenti ai diversi ambiti operativi.

La generazione degli output avviene a partire da tracce fornite dagli utenti. Le tracce vengono interpretate dal sistema e ricondotte ai nodi trasversali e agli ambiti rilevanti.

Il compito del progetto è:

1. costruire e mantenere la rete di documenti che costituisce l’architettura di base di HCAIRE;
2. sviluppare e gestire le skill derivate da tali documenti;
3. produrre e validare un insieme significativo di tracce di riferimento per testare e dimostrare il funzionamento del sistema.

## Trigger automatico                                                                                   
Quando ricevi un prompt che contiene "Leggi la traccia in input_bartleby.md", esegui il flusso descritto   sotto.                                                                                                                                                                                                           
  ---                                                                                                                                                                                                    
  ## Flusso di elaborazione

  ### 1. Leggi input_bartleby.md

  Leggi il file `input_bartleby.md` nella directory corrente.
  Se il file è vuoto o non esiste, rispondi solo: `{"error": "nessuna traccia da elaborare"}` e fermati.  

  ### 2. Elabora la traccia — Motore di Traducibilità HCAIRE (Moduli A-F)

  Applica i sei moduli in sequenza. Non devi scrivere i moduli nell'output — sono il tuo processo interno.

  **Modulo A — Riformulazione della traccia**
  Identifica il problema reale implicito nella traccia. Chi sono i soggetti? Quali presupposizioni        
  contiene? Che livello di output richiede (genitore, clinico, istituzionale)?

  **Modulo B — Analisi multidimensionale**
  Mappa quali dimensioni sono presenti e quali assenti nella traccia:
  - Relazione (bambino ↔ adulto, tra adulti)
  - Corpo e regolazione (segnali corporei, ritmi, autoregolazione)
  - Affettività (vita emotiva, riconoscimento, contenimento)
  - Mondo storico-culturale (contesto, valori, pressioni sociali)
  - Desiderio e campo intenzionale (motivazioni, orientamenti, spinte)

  **Modulo C — Nodi critici**
  Identifica i rischi di riduzionismo attivi nella traccia:
  - Riduzionismo normativo (confronto con medie)
  - Riduzionismo diagnostico (etichettatura precoce)
  - Frammentazione relazionale (isolare il bambino dal sistema)
  - Biologismo (riduzione a cause neurofisiologiche)
  - Cognitivismo disincarnato (mente senza corpo)

  **Modulo D — Integrazione con il modello**
  Attiva i ConceptNode e le AreaSheet pertinenti dalla KB HCAIRE. Usa i bartlebyId esatti (es. N1,    
  da-002, sk-003). Produci una lettura integrata che colleghi la traccia al modello.

  **Modulo E — Traduzione verso l'output**
  Scegli il tipo di output appropriato (guida-genitoriale, policy-brief, nota-clinico-riflessiva,
  risposta-istituzionale, report-educativo). Determina il tono e il livello linguistico. Scrivi il testo  
  finale in Markdown.

  **Modulo F — Verifica qualità**
  Verifica: l'output evita diagnosi, rassicurazioni vuote e prescrizioni rigide? È coerente con il modello
   HCAIRE? Assegna un punteggio indicativo (0-10).

  ---

  ### 3. Produci l'output

  Rispondi con un **singolo oggetto JSON valido**, senza testo aggiuntivo prima o dopo, con questa        
  struttura:

  ```json
  {
    "title": "Titolo dell'output",
    "output_type": "guida-genitoriale",
    "audience": "genitore",
    "area_id": "da-001",
    "body": "# Titolo\n\nTesto completo in Markdown (800-2000 parole)...",
    "body_summary": "Riassunto in 2-3 frasi, max 300 caratteri.",
    "activated_nodes": ["N1", "N3"],
    "skills_used": ["sk-001", "sk-004"],
    "evaluation": {
      "score": 8,
      "notes": "Output coerente con il modello. Punto di forza: lettura multidimensionale. Limite: ambito 
  relazionale solo accennato.",
      "status": "aperta a revisione"
    }
  }

  Valori ammessi per output_type: guida-genitoriale, policy-brief, nota-clinico-riflessiva,
  risposta-istituzionale, report-educativo
  Valori ammessi per audience: genitore, clinico, decisore-istituzionale, educatore
  I campi activated_nodes e skills_used devono contenere solo bartlebyId validi dalla KB. I nodi trasversali sono i 7 canonici N1–N7 (vedi `Documenti fondativi/Atlante nodi trasversali.md` v2.0); gli ambiti sono i 4 contesti canonici (da-001 genitoriale, da-002 clinico, da-003 pedagogico, da-004 istituzionale/servizi).

  ---
  4. Svuota input_bartleby.md

  Dopo aver prodotto il JSON con successo, sovrascrivi input_bartleby.md con una stringa vuota:

  (file vuoto)

  Usa il tool Write (o Edit) per azzerare il file. Questo segnala al sistema che la traccia è stata       
  elaborata.

  ---
  Principi da rispettare sempre

  - Non diagnosticare, non rassicurare in modo vuoto, non prescrivere in modo rigido
  - Il bambino è sempre soggetto incarnato in relazione — non oggetto di valutazione
  - Profondità teorica anche negli output per genitori
  - Il body deve essere testo leggibile e fluente, non un elenco di moduli
