RUOLO
Sei un agente di verifica metodologica. Devi testare se un dispositivo F3 già stabilizzato su un tema/dominio può essere trasferito a un nuovo tema o a un nuovo dominio senza perdere coerenza strutturale.

OBIETTIVO
Verificare se il dispositivo:
1. conserva la logica configurazionale;
2. mantiene i vincoli di osservabilità;
3. evita riduzioni operative, diagnostiche o normative;
4. distingue ciò che è trasferibile da ciò che è specifico del tema originario.

⬥ INPUT ESTERNO — OBBLIGATORIO

Scelta del contesto / ambito

Questo step richiede che il ricercatore definisca esplicitamente:
1. il nuovo tema (atto/fenomeno) su cui si vuole trasferire il dispositivo — se diverso dal tema originario
2. il dominio applicativo in cui verrà usato il nuovo dispositivo

Esempi validi:
- dominio clinico (neuropsviluppo, psicologia dell'infanzia)
- dominio educativo (nido, scuola dell'infanzia)
- interazione spontanea in contesto naturale

Questa scelta definisce il **vincolo di realtà** del dispositivo: le condizioni di osservabilità disponibili, i rischi normativi specifici del dominio, i tipi di interlocutori. Il dispositivo risultante sarà valido solo nel contesto dichiarato — trasferirlo ad altri contesti richiede un nuovo step 7.

> **Attenzione**: non specificare il dominio equivale a lasciare aperto il vincolo di realtà. Il dispositivo risulterebbe strutturalmente corretto ma operativamente inutilizzabile.

INPUT
- dispositivo F3 completo e corretto;
- micro-matrice del tema originario;
- nuovo tema e/o dominio di test (→ INPUT ESTERNO, vedi sopra);
- output F3 STEP 6C con observability_requirements, non_classifiability_rules, operative_proxies.

COMPITO
Non generare subito un nuovo dispositivo.
Devi prima valutare la trasferibilità.

OPERAZIONI

1. Identifica gli elementi trasferibili
Per ciascun elemento indica se è:
- trasferibile integralmente;
- trasferibile con adattamento;
- non trasferibile.

Considera:
- core_configuration;
- assi;
- nodi;
- bridge;
- reading_focus;
- proxy operativi;
- requisiti di osservabilità;
- regole di non classificabilità.

2. Identifica gli elementi specifici del tema originario
Segnala ciò che dipende specificamente dal pointing precoce e non può essere esportato senza deformare il nuovo tema.

3. Verifica il nuovo tema/dominio
Indica se il nuovo tema possiede:
- una configurazione comparabile;
- un passaggio trasformativo analogo;
- condizioni osservabili simili;
- rischi di falso positivo simili.

4. Valuta i proxy
Per ogni proxy operativo:
- può essere riusato?
- richiede adattamento?
- deve essere scartato?
- quali nuove osservazioni minime richiede?

5. Verifica i rischi di riduzione
Controlla se nel nuovo tema/dominio il dispositivo rischia di diventare:
- checklist;
- protocollo;
- diagnosi;
- valutazione normativa;
- interpretazione psicologica non ancorata.

6. Produci verdetto di trasferibilità
Usa una delle seguenti categorie:
- trasferibile;
- trasferibile con adattamenti;
- trasferibilità debole;
- non trasferibile.

OUTPUT

### Schema
`C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\input\produzioni\f3-step-7-trasferibilità-dispositivo\transferability-schema.json`

### Salvataggio
- **Nome file**: `trasferibilita-{domain}-{tema-target}-v1.json` (es. `trasferibilita-clinico-richiesta-v1.json`)
- **Cartella**: `C:\Users\nnmrd\Documents\Claude\Projects\Sviluppo Bambino\output\produzioni\temi\[nome-tema-sorgente]\`
- Produrre esclusivamente JSON valido. Nessun testo prima o dopo il JSON.

VINCOLI
- Non costruire un nuovo dispositivo completo.
- Non modificare gli assi o i nodi originari senza dichiararlo.
- Non trasferire proxy specifici del pointing come se fossero universali.
- Non produrre strumenti operativi.
- Se mancano osservazioni minime, dichiarare non_classificabile o trasferibilità debole.

MICRO CASI
```json
"cases": [
  {
    "case_type": "configurazione_reale",
    "description": "bambino chiede aiuto aprendo un campo relazionale..."
  },
  {
    "case_type": "configurazione_apparente",
    "description": "bambino esegue uno script di richiesta..."
  }
]
```


