# Modulo 4 — La Matrice Nodo × Contesto
**Numero slide**: 6
**Colore accent**: `#2980b9`
**Tipo prevalente**: interactive + standard

---

## Dati globali del modulo

Definire in `m04.js` le seguenti costanti.

```javascript
const QUATTRO_CONTESTI = [
  {
    id: 'C',
    lettera: 'C',
    nome: 'Clinico',
    colore: '#2980b9',
    icona: '🩺',
    attori: 'Pediatra, NPI, psicologo, medico',
    prospettiva: 'Osservazione clinica situata: come si presenta il bambino in questo setting? Quali configurazioni sono leggibili durante la visita o il colloquio?',
    errore_tipico: 'Trasformare ogni configurazione in sospetto diagnostico.',
    correzione: 'Descrivere prima la forma della configurazione, poi eventualmente distinguere se servono approfondimenti.'
  },
  {
    id: 'P',
    lettera: 'P',
    nome: 'Pedagogico-educativo',
    colore: '#27ae60',
    icona: '📚',
    attori: 'Educatore al nido, insegnante, pedagogista',
    prospettiva: 'Il contesto di apprendimento e cura: come l\'ambiente, le routine e la relazione educativa sostengono o ostacolano lo sviluppo?',
    errore_tipico: 'Trasformare ogni lettura in tecnica educativa.',
    correzione: 'Mantenere uno spazio riflessivo tra osservazione, interpretazione e progettazione.'
  },
  {
    id: 'G',
    lettera: 'G',
    nome: 'Genitoriale',
    colore: '#e67e22',
    icona: '👨‍👩‍👧',
    attori: 'Genitori, famiglia, caregiver primari',
    prospettiva: 'La relazione quotidiana: cosa vede il genitore? Come può riconoscere le configurazioni senza sentirsi valutato?',
    errore_tipico: 'Trasformare la lettura in colpa o prestazione genitoriale.',
    correzione: 'Usare un linguaggio che aumenti la capacità di vedere, non il senso di inadeguatezza.'
  },
  {
    id: 'I',
    lettera: 'I',
    nome: 'Istituzionale / Servizi',
    colore: '#8e44ad',
    icona: '🏛',
    attori: 'Coordinatori, responsabili di servizio, équipe multiprofessionali, rete dei servizi',
    prospettiva: 'L\'organizzazione dei servizi: le strutture, le routine e le procedure facilitano o ostacolano le condizioni per lo sviluppo?',
    errore_tipico: 'Trasformare la metodologia in procedura standardizzata.',
    correzione: 'Usare i Nodi come criteri di leggibilità e progettazione, non come adempimenti.'
  }
];

// Matrice completa Nodo × Contesto
// Fonte: f2-traduzione-interdisciplinare.md §5 + esempi §5.8
const MATRICE = {
  n1: {
    C: {
      domanda: 'Il bambino recupera dopo sovraccarico? L\'esperienza si mantiene o collassa?',
      lettura: 'Il bambino si disorganizza durante la visita ma il campo relazionale permette una ripresa. La regolazione non è autonoma, ma è sostenuta dalla presenza adulta.',
      errore: 'È poco collaborativo.',
      output: 'Traccia osservativa per bilancio; formazione per pediatri sul clima ambulatoriale'
    },
    P: {
      domanda: 'Il contesto sostiene o sovraccarica l\'esperienza del bambino?',
      lettura: 'Le routine di gruppo amplificano o attenuano la disorganizzazione? C\'è spazio per il recupero?',
      errore: 'È iperattivo / non sta fermo.',
      output: 'Scheda riflessiva sull\'ambiente; formazione su regolazione e setting educativo'
    },
    G: {
      domanda: 'Come aiuto mio figlio a ritrovare calma senza sostituirmi completamente?',
      lettura: 'Non si tratta solo di "calmarlo": si tratta di sostenere una ripresa dall\'interno, senza togliergli la possibilità di regolarsi.',
      errore: 'Piange sempre per niente.',
      output: 'Linguaggio restitutivo; domande-guida per il genitore'
    },
    I: {
      domanda: 'Le routine del servizio riducono o aumentano la frammentazione esperienziale?',
      lettura: 'I passaggi tra attività, gli spazi, i tempi: quanto sovraccaricano o sostengono la continuità esperienziale dei bambini?',
      errore: 'Servirebbe più disciplina / struttura.',
      output: 'Criteri di progettazione delle routine; formazione d\'équipe'
    }
  },
  n2: {
    C: {
      domanda: 'Lo scambio adulto-bambino regola o amplifica la difficoltà?',
      lettura: 'Il genitore in ambulatorio sostiene la sequenza oppure si sostituisce o si ritira? Il campo relazionale presente rende la visita più o meno abitabile?',
      errore: 'I genitori sono ansiosi.',
      output: 'Traccia osservativa sulla co-regolazione; formazione sulla restituzione ai genitori'
    },
    P: {
      domanda: 'L\'adulto sostiene l\'azione del bambino senza sostituirsi?',
      lettura: 'L\'educatrice riconosce la difficoltà, non si sostituisce, permette al bambino di restare soggetto. Il campo relazionale continua.',
      errore: 'L\'educatrice è brava / sbagliata.',
      output: 'Formazione sulla differenza tra sostegno e sostituzione; scheda neutra di co-regolazione'
    },
    G: {
      domanda: 'Mi sento in sintonia con mio figlio o spesso in lotta?',
      lettura: 'Non è una questione di bravo/cattivo genitore: è la qualità del campo relazionale che sostiene o no l\'esperienza del bambino.',
      errore: 'Non mi obbedisce mai.',
      output: 'Restituzione narrativa; traccia per il colloquio con i genitori'
    },
    I: {
      domanda: 'Il servizio protegge la relazione adulto-bambino o la burocratizza?',
      lettura: 'Le procedure, i passaggi di consegna, i tempi dell\'équipe: favoriscono o interrompono le relazioni di co-regolazione tra adulti e bambini?',
      errore: 'Basta seguire il protocollo.',
      output: 'Criteri organizzativi per équipe; formazione sulla relazione nei servizi'
    }
  },
  n3: {
    C: {
      domanda: 'Il gesto, lo sguardo o la vocalizzazione aprono una situazione di condivisione con l\'adulto?',
      lettura: 'Il bambino non si limita a manipolare il libro: indica, cerca lo sguardo dell\'adulto, sembra attendere risposta. Accesso al mondo condiviso presente, mediato da gesto, sguardo e parola.',
      errore: '"Buona attenzione condivisa" come etichetta competenziale.',
      output: 'Traccia osservativa per bilancio di salute; micro-formazione per pediatri'
    },
    P: {
      domanda: 'L\'attività genera partecipazione condivisa o resta esecuzione guidata dall\'adulto?',
      lettura: 'Il bambino partecipa quando può scegliere, indicare, ricevere risposta. La lettura non funziona solo come trasmissione di parole: costruisce un campo comune.',
      errore: '"Il bambino segue bene l\'attività."',
      output: 'Traccia per osservare letture in piccolo gruppo; formazione educatori'
    },
    G: {
      domanda: 'In quali momenti mio figlio cerca di condividere qualcosa con me?',
      lettura: 'Quando il bambino indica e guarda il genitore, non sta solo "riconoscendo": sta invitando l\'adulto a entrare nello stesso piccolo mondo.',
      errore: '"Devo insegnargli più parole."',
      output: 'Scheda restitutiva breve; domande-guida per il genitore; materiali Dialogic Book Sharing'
    },
    I: {
      domanda: 'Le routine del servizio creano occasioni di partecipazione simbolica o riducono l\'interazione a prestazione?',
      lettura: 'Ambulatorio, nido, servizio territoriale: predisporre oggetti, tempi e setting rende più probabile l\'emergere di piccoli campi condivisi adulto-bambino.',
      errore: '"Bisogna introdurre un protocollo obbligatorio di lettura."',
      output: 'Criteri per setting più leggibili; tracce organizzative per libro, gioco, relazione nei servizi'
    }
  },
  n4: {
    C: {
      domanda: 'Curiosità presente, evitamento o ritiro?',
      lettura: 'Il bambino esplora l\'ambulatorio o si chiude? Usa il genitore come base sicura o è incollato/distaccato?',
      errore: '"È timido / è iperattivo."',
      output: 'Osservazione dello stile esplorativo; note per il bilancio'
    },
    P: {
      domanda: 'L\'ambiente è esplorabile o produce ansia?',
      lettura: 'Lo spazio, i materiali, le routine permettono cicli di avvicinamento e ritorno? O il contesto satura / inibisce l\'esplorazione?',
      errore: '"Non sta mai fermo / non esplora."',
      output: 'Scheda riflessiva sull\'ambiente educativo; criteri di progettazione degli spazi'
    },
    G: {
      domanda: 'Proteggo troppo o lascio spazio sufficiente per esplorare?',
      lettura: 'L\'esplorazione non è pericolosità: è la modalità con cui il bambino abita il mondo. Il riferimento relazionale non la blocca — la rende possibile.',
      errore: '"Non vuole allontanarsi da me" (letto come problema anziché come configurazione).',
      output: 'Linguaggio restitutivo sull\'esplorazione; domande per il genitore'
    },
    I: {
      domanda: 'Gli spazi del servizio consentono sperimentazione sicura?',
      lettura: 'I setting sono progettati per l\'esplorazione o per il controllo? Quanto permettono cicli di iniziativa e ritorno relazionale?',
      errore: '"I bambini devono stare nei loro spazi."',
      output: 'Criteri architettonici e organizzativi; formazione d\'équipe sull\'esplorazione'
    }
  },
  n5: {
    C: {
      domanda: 'Il limite rompe o riorganizza il campo relazionale?',
      lettura: 'La frustrazione della visita (attesa, spogliazione, esame) è tollerabile? Il bambino può protestare e riprendere? Il campo non si distrugge al primo ostacolo.',
      errore: '"Non tollera la frustrazione / fa i capricci."',
      output: 'Scheda osservativa sulle sequenze di rottura-ripresa; formazione sul limite in ambulatorio'
    },
    P: {
      domanda: 'La regola organizza l\'esperienza o la schiaccia?',
      lettura: 'La norma introdotta dall\'adulto aiuta a strutturare il campo? O produce solo obbedienza-disobbedienza senza apprendimento?',
      errore: '"Non rispetta le regole."',
      output: 'Formazione su limite organizzante vs. distruttivo; scheda riflessiva'
    },
    G: {
      domanda: 'Posso dire no a mio figlio senza che il rapporto si rompa?',
      lettura: 'Il "no" non riguarda l\'obbedienza: riguarda se il campo relazionale può reggere la resistenza del reale e riorganizzarsi. La protesta breve che si risolve non è un problema.',
      errore: '"Devo essere più duro / devo cedere di più."',
      output: 'Linguaggio restitutivo sul limite; domande-guida per il colloquio con genitori'
    },
    I: {
      domanda: 'Le procedure del servizio sono limiti abitabili o pura interdizione?',
      lettura: 'Regole, vincoli organizzativi, protocolli: possono essere limiti che strutturano il campo, non solo obblighi che lo frammentano.',
      errore: '"Il protocollo non si discute."',
      output: 'Criteri per procedure flessibili; formazione sul limite istituzionale'
    }
  },
  n6: {
    C: {
      domanda: 'Dopo la frattura, il bambino riprende?',
      lettura: 'Regressioni, crisi, momenti di interruzione: sono recuperabili? Il bambino torna a una continuità esperienziale sufficiente dopo l\'evento stressante?',
      errore: '"Non tollera le interruzioni / è instabile."',
      output: 'Traccia sulle sequenze interruzione-ripresa; formazione sulla continuità in ambito clinico'
    },
    P: {
      domanda: 'L\'apprendimento è cumulativo o si azzera ogni volta?',
      lettura: 'Il bambino porta con sé qualcosa da una esperienza all\'altra? O ogni sessione di gioco/apprendimento ricomincia da zero?',
      errore: '"Non ricorda / non apprende."',
      output: 'Scheda riflessiva sulla continuità educativa; formazione su memoria esperienziale'
    },
    G: {
      domanda: 'Dopo una crisi, riusciamo a ritrovare il filo del rapporto?',
      lettura: 'Non si tratta di "superare" le difficoltà: si tratta di riprendere una direzione comune. La continuità non è assenza di conflitto, ma possibilità di riprendere.',
      errore: '"Non dimentica mai / porta rancore."',
      output: 'Linguaggio restitutivo sulla ripresa dopo frattura; domande-guida per genitori'
    },
    I: {
      domanda: 'I percorsi del servizio sono longitudinali o episodici?',
      lettura: 'Il servizio mantiene una continuità nel tempo con il bambino e la famiglia? O ogni accesso è una prestazione senza memoria del precedente?',
      errore: '"Ogni visita/accesso è indipendente."',
      output: 'Criteri per la continuità dei percorsi; formazione sull\'integrazione longitudinale'
    }
  },
  n7: {
    C: {
      domanda: 'L\'azione del bambino mostra una direzione propria?',
      lettura: 'Durante la visita, il bambino manifesta iniziative spontanee, interessi, orientamenti? Oppure si adatta solo alle proposte dell\'adulto?',
      errore: '"Ha buona motivazione."',
      output: 'Traccia sull\'iniziativa; note per il bilancio'
    },
    P: {
      domanda: 'Il contesto sostiene le direzioni emergenti del bambino?',
      lettura: 'L\'educazione non solo trasmette: riconosce e amplifica le direzioni che il bambino sta già costruendo. C\'è spazio per l\'iniziativa?',
      errore: '"Bisogna aumentare la motivazione."',
      output: 'Formazione su desiderio, interesse e progettazione educativa'
    },
    G: {
      domanda: 'Dove vedo mio figlio andare verso qualcosa con intensità?',
      lettura: 'Non è solo una preferenza: è la direzione che l\'esperienza prende quando qualcosa acquista valore. Il genitore può imparare a riconoscerla e amplificarla senza impadronirsene.',
      errore: '"Gli piace quel gioco" (troppo povero).',
      output: 'Guida per genitori sull\'iniziativa; scheda restitutiva'
    },
    I: {
      domanda: 'Il servizio alimenta l\'agency del bambino o produce conformità?',
      lettura: 'Un servizio orientato allo sviluppo non propone solo attività: predispone condizioni in cui l\'iniziativa del bambino possa essere riconosciuta, sostenuta e tradotta in esperienza condivisa.',
      errore: '"Serve un catalogo di attività motivanti."',
      output: 'Criteri di progettazione degli ambienti; revisione delle routine; formazione su agency'
    }
  }
};
```

---

## SLIDE 4.1 — Il principio: invariante e prospettiva

**Tipo**: `standard`
**Titolo**: La stessa struttura, quattro sguardi
**Sottotitolo**: Nodo invariante · Contesto come prospettiva

**Contenuto principale**:

Layout a due sezioni verticali.

**Sezione superiore — il principio enunciato**:

Grande blockquote centrato, bordo sinistro --color-accent:

> *"I Nodi Trasversali sono invarianti strutturali: non cambiano passando tra contesti professionali. Cambia solo il tipo di domanda, il livello di osservazione, il tipo di output."*

Sotto, in testo normale:

La Matrice Nodo × Contesto formalizza questa relazione. La si legge così:
- **Riga** = un Nodo (invariante strutturale: sempre lo stesso, in qualsiasi contesto)
- **Colonna** = un contesto (prospettiva di interrogazione: cambia chi guarda, come guarda, perché guarda)
- **Cella** = la domanda professionale che nasce dall'incrocio

**Sezione inferiore — schema visivo 2 × 2**:

Quattro quadranti con un cerchio centrale:

```
          N O D O
          (invariante)
              │
    ──────────┼──────────
              │
  Clinico  Pedagogico  Genitoriale  Istituzionale
  (prospettive di interrogazione)
```

Schema più visivo: un cerchio centrale grande con l'etichetta "N3 — Accesso al mondo condiviso" e quattro frecce che portano a quattro box, ognuno con colore-contesto e la domanda corrispondente per N3:

→ `🩺 Clinico`: *Il gesto apre condivisione?*
→ `📚 Pedagogico`: *L'attività genera partecipazione?*
→ `👨‍👩‍👧 Genitoriale`: *Mio figlio cerca di condividere qualcosa?*
→ `🏛 Istituzionale`: *Il servizio crea partecipazione o prestazione?*

**Regola conclusiva** in grassetto, centrata:

*Il contesto cambia la domanda, non il Nodo.*
*Clinico, pedagogico, genitoriale e istituzionale non vedono cose diverse: vedono lo stesso processo da responsabilità diverse.*

---

## SLIDE 4.2 — I quattro contesti

**Tipo**: `standard`
**Titolo**: I quattro contesti stabili
**Sottotitolo**: Chi interroga · da dove · con quali responsabilità

**Contenuto principale**:

Quattro card orizzontali (una per riga), ognuna con colore-contesto. Usa i dati da `QUATTRO_CONTESTI`.

Ogni card ha struttura fissa:
- Badge lettera (C / P / G / I) + icona + nome contesto, sfondo colorato
- **Attori**: chi è coinvolto
- **Prospettiva**: da dove e perché interroga il Nodo
- **Errore tipico** (in rosso tenue): cosa tende a produrre questo contesto se non usa la F2
- **Correzione metodologica** (in verde tenue): come la F2 orienta correttamente

**Card C — Clinico** (colore #2980b9):
Attori: *Pediatra, NPI, psicologo, medico*
Prospettiva: *Osservazione situata: come si presenta il bambino in questo setting? Quali configurazioni sono leggibili durante la visita o il colloquio?*
Errore tipico: *Trasformare ogni configurazione in sospetto diagnostico.*
Correzione: *Descrivere prima la forma della configurazione, poi eventualmente distinguere se servono approfondimenti.*

**Card P — Pedagogico-educativo** (colore #27ae60):
Attori: *Educatore, insegnante, pedagogista*
Prospettiva: *Il contesto di apprendimento e cura: l'ambiente, le routine e la relazione educativa sostengono o ostacolano lo sviluppo?*
Errore tipico: *Trasformare ogni lettura in tecnica educativa.*
Correzione: *Mantenere uno spazio riflessivo tra osservazione, interpretazione e progettazione.*

**Card G — Genitoriale** (colore #e67e22):
Attori: *Genitori, famiglia, caregiver primari*
Prospettiva: *La relazione quotidiana: cosa vede il genitore? Come riconosce le configurazioni senza sentirsi valutato?*
Errore tipico: *Trasformare la lettura in colpa o prestazione genitoriale.*
Correzione: *Usare un linguaggio che aumenti la capacità di vedere, non il senso di inadeguatezza.*

**Card I — Istituzionale/Servizi** (colore #8e44ad):
Attori: *Coordinatori, responsabili di servizio, équipe multiprofessionali*
Prospettiva: *L'organizzazione: le strutture, le routine e le procedure facilitano o ostacolano le condizioni per lo sviluppo?*
Errore tipico: *Trasformare la metodologia in procedura standardizzata.*
Correzione: *Usare i Nodi come criteri di leggibilità, non come adempimenti.*

**Nota in footer**:
*Il contesto Genitoriale è speciale: il linguaggio deve essere accessibile e non valutante. Non si chiedono al genitore osservazioni professionali — si offre un frame per riconoscere ciò che già vede.*

---

## SLIDE 4.3 — La matrice 7 × 4

**Tipo**: `interactive`
**Titolo**: La Matrice Nodo × Contesto
**Sottotitolo**: 7 Nodi · 4 contesti · 28 domande professionali

**Contenuto principale**:

Componente `InteractiveMatrix` con i dati completi da `MATRICE`.

**Layout della matrice**:

Griglia con intestazioni di riga (sinistra) e intestazioni di colonna (sopra).

Intestazioni di riga: badge colorato con numero Nodo (N1–N7) + nome abbreviato.
Intestazioni di colonna: badge colorato con lettera contesto (C / P / G / I) + nome.

Ogni cella mostra la **domanda professionale** (dal campo `domanda`) in testo piccolo. La cella ha altezza fissa e il testo è troncato se troppo lungo; l'espansione avviene al click.

**Comportamento interattivo**:

- **Hover su cella**: evidenzia tutta la riga (Nodo) e tutta la colonna (Contesto) con colore tenue
- **Click su cella**: apre un pannello espanso (sotto la matrice o a lato in viewport largo) con:
  - Intestazione: `[Badge Nodo] × [Badge Contesto]`
  - **Domanda**: testo completo
  - **Lettura valida**: testo dal campo `lettura`
  - **Errore da evitare**: testo dal campo `errore`
  - **Output possibile**: testo dal campo `output`
  - Pulsante "Chiudi" per tornare alla matrice
- **Click su intestazione di riga**: evidenzia tutti i contesti per quel Nodo (utile per confrontare le quattro domande di un Nodo)
- **Click su intestazione di colonna**: evidenzia tutti i Nodi per quel contesto (utile per avere il quadro di un contesto professionale)

**Elemento aggiuntivo — filtro rapido**:

Sopra la matrice, quattro pulsanti filtro colorati: `Clinico` | `Pedagogico` | `Genitoriale` | `Istituzionale`.
Cliccando un filtro, si evidenziano solo le celle di quella colonna; le altre sbiadiscono. Cliccando di nuovo si deseleziona.

**Nota implementativa**: su schermi stretti (< 900px), la matrice diventa verticale (Nodi in colonna, un contesto alla volta con switch). Su schermi larghi (> 1200px), mostrare la matrice completa 7 × 4.

---

## SLIDE 4.4 — Focus: N3 per i quattro contesti

**Tipo**: `standard`
**Titolo**: Lo stesso Nodo, quattro sguardi
**Sottotitolo**: N3 — Accesso al mondo condiviso simbolico attraverso i quattro contesti

**Contenuto principale**:

**Sezione superiore — la situazione-base** (la stessa in tutti e quattro i contesti):

Card narrativa, sfondo --color-primary-light, testo in corsivo:

*Un bambino di circa 20 mesi guarda un libro illustrato con un adulto. Indica una figura, vocalizza, guarda l'adulto, attende una risposta. L'adulto nomina l'immagine e il bambino torna a indicarla.*

**Nodo attivo**: badge `N3` blu + *Accesso al mondo condiviso simbolico*

**Sezione centrale — quattro pannelli affiancati** (o due righe da due su schermi medi):

Ogni pannello ha colore-contesto come bordo superiore o header.

**Pannello C — Clinico**:
*Chi osserva*: il pediatra durante il bilancio di salute
*Domanda*: "Il gesto, lo sguardo o la vocalizzazione aprono condivisione con l'adulto?"
*Lettura valida*: "Il bambino indica, cerca lo sguardo, attende risposta. Accesso al mondo condiviso presente, mediato da gesto e parola adulta."
*Errore*: "Buona attenzione condivisa." (trasforma in competenza psicologica)
*Output*: traccia osservativa per bilancio

**Pannello P — Pedagogico**:
*Chi osserva*: l'educatrice durante la lettura al nido
*Domanda*: "Il libro diventa occasione di partecipazione o resta esecuzione guidata dall'adulto?"
*Lettura valida*: "Il bambino partecipa quando può scegliere, indicare, ricevere risposta. Non trasmissione: costruzione di campo comune."
*Errore*: "Il bambino segue bene l'attività." (descrive adesione, non partecipazione)
*Output*: traccia per lettura in piccolo gruppo

**Pannello G — Genitoriale**:
*Chi osserva*: il genitore a casa, durante la lettura o il gioco
*Domanda* (tradotta in linguaggio accessibile): "In quali momenti mio figlio cerca di condividere qualcosa con me?"
*Lettura valida*: "Quando indica e guarda il genitore, non riconosce solo l'immagine: invita l'adulto a entrare nello stesso piccolo mondo."
*Errore*: "Devo insegnargli più parole." (sposta sulla prestazione linguistica)
*Output*: scheda restitutiva breve; materiali Dialogic Book Sharing

**Pannello I — Istituzionale**:
*Chi osserva*: il coordinatore / responsabile del servizio
*Domanda*: "Le routine del servizio creano occasioni di partecipazione simbolica o riducono l'interazione a prestazione?"
*Lettura valida*: "Ambulatorio, nido, servizio: predisporre oggetti, tempi, setting rende più probabile l'emergere di piccoli campi condivisi."
*Errore*: "Bisogna introdurre un protocollo di lettura obbligatorio." (già decisione operativa — F3)
*Output*: criteri per setting; tracce organizzative

**Sezione inferiore — sintesi tabellare**:

| Contesto | Domanda valida | Errore da evitare | Output possibile |
|---------|---------------|------------------|-----------------|
| Clinico | Il gesto apre condivisione? | "Buona attenzione condivisa" come etichetta | Traccia osservativa |
| Pedagogico | L'attività genera partecipazione? | "Segue bene" | Formazione educatori |
| Genitoriale | Quando cerca di condividere? | "Devo insegnargli parole" | Scheda restitutiva |
| Istituzionale | Il servizio crea partecipazione? | Protocollo obbligatorio precoce | Criteri di setting |

---

## SLIDE 4.5 — Cosa non cambia e cosa cambia

**Tipo**: `comparison`
**Titolo**: La regola della matrice
**Sottotitolo**: Invariante vs. variabile

**Contenuto principale**:

**Sezione superiore — formula conclusiva** (grande, centrata):

*"Il contesto cambia la domanda, non il Nodo."*

Sotto: *Clinico, pedagogico, genitoriale e istituzionale non vedono cose diverse: vedono lo stesso processo da responsabilità diverse.*

**Sezione centrale — tabella delle differenze**:

Componente `ComparisonPanel` adattato a tre colonne:

| | **Non cambia mai** | **Cambia sempre** |
|---|---|---|
| **Il Nodo** | Struttura, definizione, assi coinvolti, proprietà, relazione con altri Nodi | — |
| **La grammatica** | Il tipo di domanda (osservativa, non diagnostica, non prescrittiva) | — |
| **Il principio** | F2 produce leggibilità, non azione | — |
| **La domanda** | — | Il linguaggio usato (clinico / educativo / accessibile / organizzativo) |
| **Il livello** | — | Chi osserva e in quale situazione |
| **L'output** | — | Il tipo di artefatto prodotto (scheda / traccia / restituzione / criteri) |
| **La responsabilità** | — | Ciascun professionista decide con la propria responsabilità disciplinare |

**Sezione inferiore — i quattro errori tipici (uno per contesto)**:

Quattro chip ridotti, con colore-contesto e testo breve:

`🩺 Clinico` → Ogni configurazione diventa sospetto diagnostico
`📚 Pedagogico` → Ogni lettura diventa tecnica educativa
`👨‍👩‍👧 Genitoriale` → Ogni osservazione diventa giudizio sul genitore
`🏛 Istituzionale` → Ogni Nodo diventa procedura standardizzata

Sotto: *Questi errori non derivano dalla malafede professionale: derivano dall'assenza di un livello intermedio. La Matrice è quel livello.*

---

## SLIDE 4.6 — Esercizio: N5 in contesto Genitoriale

**Tipo**: `interactive`
**Titolo**: Prova tu
**Sottotitolo**: N5 — Separazione / Limite reale · Contesto Genitoriale

**Contenuto principale**:

Slide-esercizio con rivelazione progressiva. L'obiettivo è che il partecipante formuli autonomamente la domanda professionale corretta prima di vedere la risposta.

**Sezione superiore — la situazione-base** (card narrativa):

*A casa, il bambino vuole prendere un oggetto fragile. Il genitore dice "no" e sposta l'oggetto. Il bambino protesta, piange brevemente, poi guarda il genitore. L'adulto resta presente e propone un altro oggetto manipolabile.*

Badge del Nodo: `N5` rosso + *Separazione / Limite reale*
Badge del contesto: `G` arancio + *Genitoriale*

**Sezione centrale — tre passaggi a rivelazione**:

Ogni passaggio è nascosto e si rivela cliccando un pulsante.

**Passaggio 1** — *"Dalla struttura del Nodo..."*:

Testo visibile subito:
N5 riguarda l'incontro tra l'intenzionalità del bambino e la resistenza del reale. La domanda strutturale è: *il limite organizza o collassa il campo?*

Sotto: *Ora prova a tradurla nel linguaggio del contesto Genitoriale. Come la direbbe un genitore a se stesso?*

Pulsante: "Mostra la domanda professionale valida →"

**Passaggio 2** — *Domanda professionale valida* (si rivela al click):

Card verde:
**Domanda**: *"Posso dire no a mio figlio senza che il rapporto si rompa?"*

*Perché è valida*: è osservabile, è nel linguaggio del genitore, non implica un giudizio ("sono un buon/cattivo genitore"), e apre una riflessione sulla configurazione relazionale — non dà una risposta.

Pulsante: "Mostra lettura valida →"

**Passaggio 3** — *Lettura metodologicamente valida* (si rivela al secondo click):

Card tenue:
**Lettura**: *Il "no" non riguarda l'obbedienza: riguarda se il campo relazionale può reggere la resistenza del reale e riorganizzarsi. La protesta breve che si risolve non è un problema — è il segno che il limite è abitabile.*

**Errore da evitare**:
❌ *"Devo essere più duro."* — moralizza sul genitore
❌ *"Devo cedere di più."* — moralizza in senso opposto
Entrambi spostano l'attenzione dal campo al giudizio.

**Output possibile**: linguaggio restitutivo sul limite; domande-guida per il colloquio con genitori.

**Chiusura del modulo**:

Testo centrato, leggero:

*Hai visto come lo stesso Nodo (N5) genera una domanda completamente diversa se cambia il contesto. Nel Modulo 5 vedremo come i Nodi non sono solo interrogabili singolarmente: si relazionano tra loro, si sostengono, si vincolano — e insieme formano configurazioni.*

Badge modulo successivo: `→ Modulo 5 — La Dinamica tra Nodi`

---

## Note per l'implementazione

### Slide 4.3 — InteractiveMatrix: priorità di sviluppo

Il componente `InteractiveMatrix` è il cuore del modulo. Suggerisco questo ordine di costruzione:

1. Prima: rendering statico della griglia con tutte le celle visibili (testo troncato)
2. Poi: hover con highlight di riga/colonna
3. Poi: click su cella con pannello espanso
4. Infine: filtri per colonna e click su intestazioni

Se il tempo è limitato, fermarsi al punto 3. I filtri (punto 4) sono un miglioramento, non un requisito.

### Slide 4.3 — Dimensioni delle celle

La matrice 7 × 4 su desktop (1280px) ha:
- Colonna intestazione Nodo: 180px
- Quattro colonne contesto: ~220px ciascuna
- Altezza cella: 60px (testo a due righe)

Le domande nella cella sono troncate con `text-overflow: ellipsis` oltre due righe. Il testo completo appare nel pannello espanso.

### Slide 4.4 — Pannelli affiancati

Su desktop, i quattro pannelli sono affiancati in griglia 2 × 2 con scroll interno se il contenuto supera l'altezza disponibile. Su schermi più piccoli, diventano un accordion verticale (uno aperto alla volta).

### Slide 4.6 — Stato dell'esercizio

Tenere traccia dello stato dell'esercizio con una variabile `let revealed = 0` (0 = solo situazione, 1 = domanda visibile, 2 = lettura visibile). Il pulsante cambia testo in base allo stato. Al termine (revealed === 2) il pulsante scompare e appare la chiusura del modulo.

### Dati e il caso-guida

Il caso-guida (lettura condivisa) è esplicitamente integrato in questa slide attraverso N3 — che è esattamente il Nodo della lettura condivisa — nelle quattro versioni contestuali della slide 4.4. Questo mantiene la coerenza col filo rosso del corso senza ripetere la scena narrativa ogni volta.
