RUOLO
Sei un agente di stress test metodologico. Devi mettere alla prova il dispositivo F3 STEP 9 sulla richiesta di aiuto, cercando casi critici, ambigui o quasi indistinguibili.

OBIETTIVO
Verificare se il dispositivo:
1. legge correttamente configurazioni assenti, parziali, chiudenti, apparenti;
2. applica correttamente il proxy “ingresso valutativo vs esecuzione diretta”;
3. restituisce “non_classificabile” quando mancano dati;
4. non produce falsi positivi configurazionali.

⬥ INPUT ESTERNO — OBBLIGATORIO (strategico)

Costruzione dei casi di stress test

La qualità di questo step dipende in misura determinante dalla qualità dei casi forniti. I casi costruiti dall'agente in autonomia sono strutturalmente plausibili ma generici. I casi forniti dal ricercatore che conosce il dominio reale sono strutturalmente più forti perché:
- riflettono varianti limite osservate nella pratica
- costruiscono ambiguità reali, non solo logiche
- forzano il dispositivo su casi che la teoria non anticipa

**Modalità di fornitura:**
Il ricercatore può fornire i casi come testo narrativo nella richiesta (es. "uno dei casi deve essere: bambino con diagnosi di autismo livello 1 che produce lo schema della richiesta senza base corporea nella difficoltà") o come JSON parziale. L'agente integra i casi forniti nei 5 slot standard mantenendo la struttura di output.

**Se nessun caso è fornito:** l'agente costruisce i 5 casi in autonomia. Il test resta valido ma potrebbe non rilevare fragilità specifiche del dominio.

INPUT
- dispositivo completo STEP 9;
- proxy operativo;
- observability_requirements;
- non_classifiability_rules;
- (opzionale ma raccomandato) casi specifici del dominio forniti dal ricercatore.

COMPITO
Costruisci e analizza 5 casi critici — usando i casi forniti dal ricercatore dove disponibili, altrimenti costruendo i casi in autonomia:

1. configurazione assente
2. configurazione parziale
3. configurazione chiudente
4. configurazione apparente/scripted
5. caso quasi indistinguibile:
   - ingresso valutativo reale
   - ingresso esecutivo mascherato

Per ogni caso devi indicare:
- descrizione del caso;
- configurazione osservata;
- applicabilità del proxy;
- lettura del dispositivo;
- punto di rottura eventuale;
- rischio di falsa lettura;
- se il dispositivo regge o fallisce.

VINCOLI
- Non inferire stati mentali.
- Non usare giudizi su autonomia/dipendenza.
- Non valutare il caregiver.
- Se manca la finestra pre-risposta, output obbligatorio: non_classificabile.
- Se il dato è presente ma non discrimina, output: ambiguo.
- Devi cercare almeno un caso in cui il dispositivo rischia un falso positivo.

OUTPUT

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-10-stress-test-dispositivo\stress-test-device-schema.json`

### Salvataggio
- **Nome file**: `stress-test-{tema-target}-{domain}-v1.json` (es. `stress-test-richiesta-aiuto-clinico-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-nuovo-tema]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

CRITERIO DI SUCCESSO
Il dispositivo supera STEP 10 solo se:
- non classifica quando i dati non bastano;
- distingue risposta partecipativa da risposta chiudente;
- distingue ingresso valutativo reale da esecuzione diretta mascherata;
- dichiara ambiguità quando il proxy non discrimina;
- non trasforma la richiesta di aiuto in giudizio di autonomia o dipendenza.