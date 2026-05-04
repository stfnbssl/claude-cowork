"""
Genera tutti i documenti preparatori per Azione 011.
Eseguire una volta sola per creare:
  - azione-011-piano.md
  - azione-011-giorno-1.md  ... giorno-5.md
  - aggiungi_rilevanza.py
"""
import json
from pathlib import Path

ROOT    = Path("/sessions/trusting-peaceful-wozniak/mnt/Sviluppo Bambino")
OUT     = ROOT / "output/assi-strutturali"

with open(OUT / "autori.json", encoding="utf-8") as f:
    autori = json.load(f)
with open(OUT / "bibliografia.json", encoding="utf-8") as f:
    biblio = json.load(f)

autori_by_id = {a["id"]: a for a in autori}
biblio_by_id = {b["id"]: b for b in biblio}

# ── Assegnazione autori ai giorni ────────────────────────────────────────
AUTORI_GIORNI = {
    1: [  # Asse 1 — Fenomenologia, corpo, biologia
        "edmund-husserl", "maurice-merleau-ponty", "martin-heidegger",
        "hans-georg-gadamer", "kurt-goldstein", "georges-canguilhem",
        "john-bowlby", "donald-winnicott", "michel-foucault",
    ],
    2: [  # Asse 2 — Psicoanalisi, genesi morale
        "melanie-klein", "sigmund-freud", "wilfred-bion", "paul-ricoeur",
        "emmanuel-levinas", "jean-piaget", "lawrence-kohlberg",
        "colwyn-trevarthen", "daniel-stern",
    ],
    3: [  # Asse 3 — Normatività, educazione, giudizio
        "hannah-arendt", "alasdair-macintyre", "charles-taylor",
        "bernard-stiegler", "agostino-d-ippona", "tommaso-d-aquino",
        "helmuth-plessner", "george-herbert-mead",
    ],
    4: [  # Asse 4 + Asse 5 — Limite, perdita, desiderio
        "franco-basaglia", "byung-chul-han", "axel-honneth",
        "platone", "aristotele", "immanuel-kant",
        "amartya-sen", "pierre-bourdieu", "edward-tronick",
    ],
    5: [  # Asse 6 — Storico-culturale + autori rimasti
        "lev-vygotskij", "jerome-bruner", "arnold-gehlen",
        "alfred-schutz", "wilhelm-dilthey", "wilhelm-von-humboldt",
        "hartmut-rosa", "ivan-illich", "hans-jonas",
        "axel-honneth",  # rimosso duplicato sotto
    ],
}
# Correggi duplicati
AUTORI_GIORNI[5] = [
    "lev-vygotskij", "jerome-bruner", "arnold-gehlen",
    "alfred-schutz", "wilhelm-dilthey", "wilhelm-von-humboldt",
    "hartmut-rosa", "ivan-illich", "hans-jonas",
]

# ── Assegnazione libri ai giorni ─────────────────────────────────────────
LIBRI_GIORNI = {
    1: [  # Asse 1
        "merleau-ponty-fenomenologia-della-percezione",
        "husserl-lezioni-sulla-coscienza-interna-del-tempo",
        "heidegger-essere-e-tempo",
        "bowlby-attaccamento-e-perdita",
        "canguilhem-normale-e-patologico",
        "goldstein-struttura-dellorganismo",
        "foucault-sorvegliare-e-punire",
        "winnicott-gioco-e-realta",
    ],
    2: [  # Asse 2
        "winnicott-maturational-processes",
        "winnicott-capacity-for-concern",
        "winnicott-use-of-an-object",
        "klein-envy-and-gratitude",
        "freud-io-e-es",
        "bion-learning-from-experience",
        "merleau-ponty-il-visibile-e-linvisibile",
        "levinas-totalita-e-infinito",
        "levinas-altrimenti-che-essere",
        "trevarthen-communication-cooperation",
        "stern-mondo-interpersonale-del-bambino",
        "tronick-neurobehavioral-development",
    ],
    3: [  # Asse 3
        "ricoeur-se-come-un-altro",
        "taylor-fonti-del-se",
        "macintyre-dopo-la-virtu",
        "stiegler-prendersi-cura",
        "arendt-crisi-dell-educazione",
        "arendt-sulla-violenza",
        "arendt-responsabilita-e-giudizio",
        "agostino-confessiones",
        "agostino-de-magistro",
        "tommaso-summa-theologiae",
        "kohlberg-essays-on-moral-development",
        "piaget-giudizio-morale-nel-bambino",
        "gadamer-verita-e-metodo",
        "plessner-gradi-dellorganico",
        "mead-mind-self-and-society",
    ],
    4: [  # Assi 4 e 5
        "freud-lutto-e-melanconia",
        "basaglia-l-istituzione-negata",
        "han-societa-della-stanchezza",
        "platone-simposio",
        "platone-repubblica",
        "aristotele-etica-nicomachea",
        "kant-critica-della-ragion-pratica",
        "kant-fondazione-metafisica-costumi",
        "husserl-ideen-ii",
        "sen-lo-sviluppo-e-liberta",
        "bourdieu-il-senso-pratico",
        "bourdieu-ragioni-pratiche",
        "jonas-il-principio-responsabilita",
    ],
    5: [  # Asse 6
        "vygotskij-pensiero-e-linguaggio",
        "vygotskij-sviluppo-funzioni-psichiche",
        "bruner-acts-of-meaning",
        "bruner-cultura-dell-educazione",
        "schutz-sinnhafte-aufbau",
        "honneth-lotta-per-il-riconoscimento",
        "dilthey-introduzione-scienze-spirito",
        "dilthey-costruzione-mondo-storico",
        "rosa-accelerazione-e-alienazione",
        "illich-deschooling-society",
        "gehlen-l-uomo",
        "humboldt-diversita-delle-lingue",
        "ricoeur-tempo-e-racconto",
        "merleau-ponty-la-prosa-del-mondo",
        "merleau-ponty-institution-et-passivite",
    ],
}

TITOLI_GIORNI = {
    1: "Asse 1 — Fenomenologia, corpo, conoscenza biologica (9 autori, 8 libri)",
    2: "Asse 2 — Psicoanalisi e genesi della vita morale (9 autori, 12 libri)",
    3: "Asse 3 — Normatività, educazione, giudizio (8 autori, 15 libri)",
    4: "Assi 4 e 5 — Limite, perdita, desiderio (9 autori, 13 libri)",
    5: "Asse 6 — Storico-culturale, linguaggio, istituzioni (9 autori, 15 libri)",
}

FOCUS_GIORNI = {
    1: ("Asse 1 — Ontologico-fenomenologico",
        "I pensatori che fondano la comprensione del soggetto come corpo vissuto, "
        "intenzionalità, temporalità. Merleau-Ponty e Husserl sono il cuore dell'asse; "
        "Heidegger e Gadamer aprono verso l'essere-nel-mondo e l'ermeneutica; "
        "Goldstein e Canguilhem forniscono il fondamento biologico-normativo; "
        "Bowlby e Winnicott portano la prospettiva dello sviluppo relazionale precoce."),
    2: ("Asse 2 — Affettivo-morale",
        "I pensatori della psicoanalisi e della genesi morale. Klein, Freud e Bion "
        "costruiscono la teoria dell'interiorizzazione dell'altro; Levinas fornisce "
        "il fondamento etico del volto; Trevarthen e Stern portano la ricerca "
        "empirica sull'intersoggettività precoce; Piaget e Kohlberg aprono sul "
        "versante dello sviluppo morale."),
    3: ("Asse 3 — Normativo-educativo",
        "I pensatori della norma, dell'educazione e del giudizio. Arendt è centrale "
        "per la distinzione tra autorità e potere; MacIntyre e Taylor fondano "
        "l'etica delle virtù e del sé narrativo; Stiegler porta la critica della "
        "tecnica come dispositivo educativo; Agostino e Tommaso rappresentano la "
        "tradizione della normatività orientata al bene."),
    4: ("Assi 4 e 5 — Separazione/Limite e Desiderio",
        "Asse 4: pensatori dell'incontro con il reale, la perdita, la separazione — "
        "Basaglia sulla crisi dell'istituzione, Han sulla società performativa, "
        "Plessner e Mead sull'eccentricità del soggetto. "
        "Asse 5: i filosofi del desiderio — Platone e Aristotele fondano la "
        "tradizione; Kant introduce il dovere; Sen, Bourdieu e Jonas completano "
        "il quadro della soggettività orientata."),
    5: ("Asse 6 — Storico-culturale",
        "I pensatori della mediazione culturale, del linguaggio, delle istituzioni. "
        "Vygotskij e Bruner forniscono il fondamento psico-culturale; Dilthey e "
        "Humboldt apportano la tradizione delle scienze dello spirito e del linguaggio; "
        "Rosa, Han e Illich portano la critica della modernità; Schutz e Honneth "
        "completano il quadro sociologico-fenomenologico."),
}

def autore_block(aid):
    a = autori_by_id.get(aid, {})
    if not a:
        return "### " + aid + "\n*Dati non trovati*\n"
    lines = [
        "### " + a["nome_completo"],
        "- **ID**: `" + a["id"] + "`",
        "- **Disciplina**: " + a.get("disciplina", "—"),
        "- **Periodo**: " + a.get("periodo", "—"),
        "- **Nazionalità**: " + a.get("nazionalita", "—"),
        "- **Assi**: " + ", ".join(a.get("citato_in_assi", [])),
    ]
    note = a.get("note", "")
    if note:
        lines.append("- **Note**: " + note)
    lines.append("")
    return "\n".join(lines)

def libro_block(bid):
    b = biblio_by_id.get(bid, {})
    if not b:
        return "### " + bid + "\n*Dati non trovati*\n"
    autore_nome = autori_by_id.get(b.get("autore_id", ""), {}).get("nome_completo", b.get("autore_id", "—"))
    lines = [
        "### " + b["titolo"],
        "- **ID**: `" + b["id"] + "`",
        "- **Autore**: " + autore_nome,
        "- **Anno**: " + str(b.get("anno_prima_edizione", "—")),
        "- **Genere**: " + b.get("genere", "—"),
        "- **Assi**: " + ", ".join(b.get("citato_in_assi", [])),
    ]
    orig = b.get("titolo_originale", "")
    if orig and orig != b["titolo"]:
        lines.append("- **Titolo originale**: " + orig)
    ctx = b.get("contesto_citazione", "")
    if ctx:
        lines.append("- **Contesto citazione**: " + ctx)
    inferred = b.get("aggiunto_per_completezza", False)
    if inferred:
        lines.append("- **Nota**: Aggiunto per completezza (non citato direttamente nei capitoli)")
    lines.append("")
    return "\n".join(lines)

# ── Genera documento per ogni giorno ────────────────────────────────────
LINEE_GUIDA = """## Linee guida per la scrittura

**Obiettivo di ogni testo**: spiegare perché questo autore / questo libro è importante *per il progetto Sviluppo Bambino*, non fornire una biografia o una recensione generale.

**Prospettiva**: il lettore del sito HCAIRE (educatore, clinico, ricercatore) vuole capire il legame specifico tra questo pensatore e il modello degli assi strutturali.

**Per gli autori** (150–200 parole):
1. Chi è, in una frase (disciplina, epoca, tradizione)
2. Qual è il contributo specifico al modello degli assi strutturali
3. In quali assi il suo pensiero è presente e come
4. Una frase finale sul perché vale la pena conoscerlo per questo progetto

**Per i libri** (100–150 parole):
1. Di cosa tratta il libro, in una frase
2. Quale problema del modello aiuta a rispondere
3. In quali assi viene usato e come

**Tono**: accessibile ma non divulgativo, preciso ma non accademico. Evitare riassunti enciclopedici.

**Output JSON** (al termine del giorno di lavoro, aggiungere al file `rilevanza-GIORNO-N.json`):
```json
{
  "autori": [
    { "id": "edmund-husserl", "rilevanza": "..." },
    ...
  ],
  "libri": [
    { "id": "husserl-lezioni-sulla-coscienza-interna-del-tempo", "rilevanza": "..." },
    ...
  ]
}
```

"""

for giorno in range(1, 6):
    n_a = len(AUTORI_GIORNI[giorno])
    n_b = len(LIBRI_GIORNI[giorno])
    titolo = TITOLI_GIORNI[giorno]
    asse_focus, asse_desc = FOCUS_GIORNI[giorno]

    lines = [
        "---",
        "id: azione-011-giorno-" + str(giorno),
        "azione: 011",
        "giorno: " + str(giorno) + " di 5",
        "stato: da_fare",
        "autori_da_trattare: " + str(n_a),
        "libri_da_trattare: " + str(n_b),
        "---",
        "",
        "# Azione 011 — Giorno " + str(giorno) + ": " + titolo,
        "",
        "## Contesto dell'azione",
        "",
        "Questo documento fa parte del piano in 5 sessioni per completare l'**Azione 011** "
        "del progetto Sviluppo Bambino (HCAIRE).",
        "",
        "**Obiettivo dell'azione**: per ogni autore e ogni libro presenti nella sezione "
        "degli assi strutturali, produrre un testo che spiega perché quel pensatore / "
        "quel testo è rilevante per il progetto Sviluppo Bambino.",
        "",
        "**Output atteso**: i testi prodotti vanno salvati in `output/assi-strutturali/rilevanza-giorno-" + str(giorno) + ".json` "
        "nel formato descritto nelle linee guida sotto. "
        "Al termine di tutte le sessioni, lo script `aggiungi_rilevanza.py` integrerà "
        "i file JSON giornalieri in `autori.json` e `bibliografia.json`.",
        "",
        "---",
        "",
        "## Focus di oggi",
        "",
        "**" + asse_focus + "**",
        "",
        asse_desc,
        "",
        "---",
        "",
    ]
    lines.append(LINEE_GUIDA)
    lines.append("---")
    lines.append("")
    lines.append("## Autori da trattare oggi (" + str(n_a) + ")")
    lines.append("")
    for aid in AUTORI_GIORNI[giorno]:
        lines.append(autore_block(aid))

    lines.append("---")
    lines.append("")
    lines.append("## Libri da trattare oggi (" + str(n_b) + ")")
    lines.append("")
    for bid in LIBRI_GIORNI[giorno]:
        lines.append(libro_block(bid))

    lines.append("---")
    lines.append("")
    lines.append("## Output del giorno — da compilare")
    lines.append("")
    lines.append("Al termine, salvare il file `rilevanza-giorno-" + str(giorno) + ".json` in `output/assi-strutturali/` con questa struttura:")
    lines.append("")
    lines.append("```json")
    lines.append("{")
    lines.append('  "giorno": ' + str(giorno) + ',')
    lines.append('  "autori": [')
    for aid in AUTORI_GIORNI[giorno]:
        a = autori_by_id.get(aid, {})
        nome = a.get("nome_completo", aid)
        lines.append('    { "id": "' + aid + '", "nome": "' + nome + '", "rilevanza": "..." },')
    lines.append('  ],')
    lines.append('  "libri": [')
    for bid in LIBRI_GIORNI[giorno]:
        b = biblio_by_id.get(bid, {})
        titolo_b = b.get("titolo", bid)[:50]
        lines.append('    { "id": "' + bid + '", "titolo": "' + titolo_b + '", "rilevanza": "..." },')
    lines.append('  ]')
    lines.append('}')
    lines.append("```")
    lines.append("")

    doc_path = OUT / ("azione-011-giorno-" + str(giorno) + ".md")
    doc_path.write_text("\n".join(lines), encoding="utf-8")
    print("Creato: " + doc_path.name)

# ── Piano master ─────────────────────────────────────────────────────────
piano_lines = [
    "---",
    "id: azione-011-piano",
    "azione: 011",
    "stato: in_lavorazione",
    "sessioni_totali: 5",
    "autori_totali: 44",
    "libri_totali: 63",
    "---",
    "",
    "# Azione 011 — Piano di lavoro",
    "## Testi di rilevanza per autori e libri degli assi strutturali",
    "",
    "### Obiettivo",
    "",
    "Per ogni autore (44) e ogni libro (63) presenti nei JSON degli assi strutturali, "
    "produrre un testo che spiega perché quel pensatore / quel testo è importante "
    "per il progetto Sviluppo Bambino, scritto nella prospettiva del modello degli "
    "assi strutturali.",
    "",
    "### Output",
    "",
    "I testi vengono prima prodotti come file JSON giornalieri (`rilevanza-giorno-N.json`), "
    "poi integrati nei file master tramite `aggiungi_rilevanza.py`:",
    "- `output/assi-strutturali/autori.json` → aggiunto campo `rilevanza`",
    "- `output/assi-strutturali/bibliografia.json` → aggiunto campo `rilevanza`",
    "",
    "### Piano per sessione",
    "",
]

for giorno in range(1, 6):
    n_a = len(AUTORI_GIORNI[giorno])
    n_b = len(LIBRI_GIORNI[giorno])
    piano_lines.append("#### Giorno " + str(giorno) + " — " + TITOLI_GIORNI[giorno])
    piano_lines.append("")
    piano_lines.append("File di sessione: `azione-011-giorno-" + str(giorno) + ".md`")
    piano_lines.append("")
    piano_lines.append("Autori (" + str(n_a) + "):")
    for aid in AUTORI_GIORNI[giorno]:
        a = autori_by_id.get(aid, {})
        piano_lines.append("- " + a.get("nome_completo", aid) + " (`" + aid + "`)")
    piano_lines.append("")
    piano_lines.append("Libri (" + str(n_b) + "):")
    for bid in LIBRI_GIORNI[giorno]:
        b = biblio_by_id.get(bid, {})
        piano_lines.append("- " + b.get("titolo", bid)[:55] + " (`" + bid + "`)")
    piano_lines.append("")

piano_lines += [
    "### Stato avanzamento",
    "",
    "| Giorno | Sessione | Autori | Libri | Stato |",
    "|--------|----------|--------|-------|-------|",
    "| 1 | Asse 1 | " + str(len(AUTORI_GIORNI[1])) + " | " + str(len(LIBRI_GIORNI[1])) + " | Da fare |",
    "| 2 | Asse 2 | " + str(len(AUTORI_GIORNI[2])) + " | " + str(len(LIBRI_GIORNI[2])) + " | Da fare |",
    "| 3 | Asse 3 | " + str(len(AUTORI_GIORNI[3])) + " | " + str(len(LIBRI_GIORNI[3])) + " | Da fare |",
    "| 4 | Assi 4-5 | " + str(len(AUTORI_GIORNI[4])) + " | " + str(len(LIBRI_GIORNI[4])) + " | Da fare |",
    "| 5 | Asse 6 | " + str(len(AUTORI_GIORNI[5])) + " | " + str(len(LIBRI_GIORNI[5])) + " | Da fare |",
    "",
    "### Come avviare ogni sessione",
    "",
    "1. Aprire il file di sessione del giorno: `azione-011-giorno-N.md`",
    "2. Leggere la sezione Focus e le Linee guida",
    "3. Scrivere tutti i testi di rilevanza",
    "4. Salvare in `rilevanza-giorno-N.json`",
    "5. Eseguire `aggiungi_rilevanza.py N` per integrare nel JSON master",
    "6. Aggiornare lo stato nel file piano",
    "",
]

(OUT / "azione-011-piano.md").write_text("\n".join(piano_lines), encoding="utf-8")
print("Creato: azione-011-piano.md")

# ── Script aggiungi_rilevanza.py ─────────────────────────────────────────
script = r'''"""
aggiungi_rilevanza.py — integra i testi di rilevanza nei JSON master

Uso:
  python aggiungi_rilevanza.py 1        # integra giorno 1
  python aggiungi_rilevanza.py 1 2 3    # integra giorni 1, 2, 3
  python aggiungi_rilevanza.py all      # integra tutti i giorni disponibili
"""
import json, sys
from pathlib import Path

ROOT = Path("/sessions/trusting-peaceful-wozniak/mnt/Sviluppo Bambino")
OUT  = ROOT / "output/assi-strutturali"

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

autori = load_json(OUT / "autori.json")
biblio = load_json(OUT / "bibliografia.json")

autori_by_id = {a["id"]: a for a in autori}
biblio_by_id = {b["id"]: b for b in biblio}

giorni = sys.argv[1:]
if not giorni:
    print("Specificare giorni: python aggiungi_rilevanza.py 1 2 ...")
    sys.exit(1)

if giorni == ["all"]:
    giorni = [str(i) for i in range(1, 6)]

n_autori = 0
n_libri  = 0

for g in giorni:
    path = OUT / ("rilevanza-giorno-" + g + ".json")
    if not path.exists():
        print("File non trovato: " + path.name + " — salto")
        continue
    data = load_json(path)

    for item in data.get("autori", []):
        aid = item["id"]
        rel = item.get("rilevanza", "").strip()
        if aid in autori_by_id and rel:
            autori_by_id[aid]["rilevanza"] = rel
            n_autori += 1

    for item in data.get("libri", []):
        bid = item["id"]
        rel = item.get("rilevanza", "").strip()
        if bid in biblio_by_id and rel:
            biblio_by_id[bid]["rilevanza"] = rel
            n_libri += 1

    print("Integrato giorno " + g + " — autori: " + str(len(data.get("autori",[]))) +
          ", libri: " + str(len(data.get("libri",[]))))

save_json(OUT / "autori.json", autori)
save_json(OUT / "bibliografia.json", biblio)
print("\nSalvati autori.json e bibliografia.json")
print("Aggiunti: " + str(n_autori) + " rilevanze autori, " + str(n_libri) + " rilevanze libri")
'''

(OUT / "aggiungi_rilevanza.py").write_text(script, encoding="utf-8")
print("Creato: aggiungi_rilevanza.py")
print("\nDone. Tutti i file sono pronti.")
