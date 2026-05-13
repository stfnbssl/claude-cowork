---
id: nodo-dominante
titolo: Nodo dominante
alias: ["Nodo limitante"]
area: configurazione
fase_principale: F3
stato: bozza
related:
  - id: configurazione-evolutiva
    rel: PRECEDE_IN_CICLO
    dir: target
    obbligatoria: true
    nota: "la CE viene letta per identificare il nodo dominante"
  - id: tipologia-universale-di-dispositivo
    rel: PRECEDE_IN_CICLO
    dir: source
    obbligatoria: true
    nota: "il nodo dominante orienta la selezione del tipo universale U1–U6"
  - id: nodo-trasversale
    rel: ISTANZA_DI
    dir: target
    obbligatoria: true
    nota: "il nodo dominante è sempre uno degli N1–N7 nella configurazione attuale"
  - id: abitabilita-dell-esperienza
    rel: ORIENTA
    dir: source
    obbligatoria: true
    nota: "è il nodo che limita maggiormente l'abitabilità complessiva"
  - id: nodo-trasversale
    rel: DISTINGUE_DA
    dir: source
    obbligatoria: false
    nota: "il nodo dominante non è il nodo 'più basso': è il più limitante nel