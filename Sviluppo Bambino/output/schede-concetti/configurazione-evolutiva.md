---
id: configurazione-evolutiva
titolo: Configurazione evolutiva
alias: ["Configurazione", "CE"]
area: configurazione
fase_principale: F2
stato: bozza
related:
  - id: operatore-di-lettura
    rel: PRODUCE
    dir: source
    obbligatoria: true
    nota: "la CE è l'output dell'operatore di lettura applicato alle osservazioni"
  - id: nodo-dominante
    rel: PRECEDE_IN_CICLO
    dir: source
    obbligatoria: true
    nota: "dalla CE si identifica il nodo dominante: punto di snodo del sistema"
  - id: nodo-trasversale
    rel: COMPONE
    dir: source
    obbligatoria: true
    nota: "la CE è la forma stabile assunta dalla dinamica tra nodi trasversali"
  - id: campo-relazionale
    rel: ORIENTA
    dir: source
    obbligatoria: true
    nota: "la CE descrive il campo relazionale, non attribuisce proprietà al bambino"
  - id: grammatica-delle-configurazioni
    rel: RENDE_OPERATIVO
    dir: target
    obbligatoria: false
    nota: "la grammatica delle configurazioni fornisce il linguaggio formale per descrivere la CE"
  - id: abitabilita-dell-esperienza
    rel: PRODUCE
    dir: source
    obbligatoria: true
    nota: "la dimensione A della CE misura l'abitabilità dell'esperienza"
  - id: transizione-configurazionale
    rel: COMPONE
    dir: source
    obbligatoria: false
    nota: "la transizione tra due CE è l'unità di misura della valutazione"
---

# Configurazione evolutiva

La forma temporaneamente stabile assunta dalla dinamica tra Nodi Trasversali in un determinato campo relazionale. È l