"""
enrich_chapters.py  —  inserisce <img> nel CORPO del testo, dopo [^N],
in corrispondenza della prima citazione di autori e libri.

Le note a piè di pagina rimangono invariate.

Uso:
  python enrich_chapters.py            # tutti gli assi
  python enrich_chapters.py "Asse 1"   # solo quell'asse
"""
import json, re, sys
from pathlib import Path

ROOT       = Path("/sessions/trusting-peaceful-wozniak/mnt/Sviluppo Bambino")
INPUT      = ROOT / "input/assi strutturali/normalized"
ASSETS     = ROOT / "output/assi-strutturali/assets"
OUT_DIR    = ROOT / "output/assi-strutturali/enriched"
ASSETS_URL = "/assets"

ASSE_FILTER = sys.argv[1] if len(sys.argv) > 1 else None

with open(ROOT / "output/assi-strutturali/autori.json", encoding="utf-8") as f:
    autori = json.load(f)
with open(ROOT / "output/assi-strutturali/bibliografia.json", encoding="utf-8") as f:
    biblio = json.load(f)

# ── Asset disponibili ────────────────────────────────────────────────────
def find_img(folder, slug):
    for ext in ("jpg", "jpeg", "png", "gif", "svg", "webp"):
        p = folder / (slug + "." + ext)
        if p.exists() and p.stat().st_size > 2500:
            return ext
    return None

autori_avail = {a["id"]: find_img(ASSETS / "autori", a["id"])
                for a in autori if find_img(ASSETS / "autori", a["id"])}
libri_avail  = {b["id"]: find_img(ASSETS / "libri",  b["id"])
                for b in biblio if find_img(ASSETS / "libri",  b["id"])}

# ── Lookup nomi -> slug ──────────────────────────────────────────────────
name_to_slug = {}
for a in autori:
    if a["id"] not in autori_avail:
        continue
    name_to_slug[a["nome_completo"]] = a["id"]
    cog = a.get("cognome", "").strip()
    if cog and len(cog) >= 4 and cog not in name_to_slug:
        name_to_slug[cog] = a["id"]

ALIASES = {
    "Merleau-Ponty": "maurice-merleau-ponty",
    "Husserl":       "edmund-husserl",
    "Heidegger":     "martin-heidegger",
    "Gadamer":       "hans-georg-gadamer",
    "Winnicott":     "donald-winnicott",
    "Klein":         "melanie-klein",
    "Freud":         "sigmund-freud",
    "Bion":          "wilfred-bion",
    "Ricoeur":       "paul-ricoeur",
    "Levinas":       "emmanuel-levinas",
    "Foucault":      "michel-foucault",
    "Arendt":        "hannah-arendt",
    "Taylor":        "charles-taylor",
    "Vygotskij":     "lev-vygotskij",
    "Bruner":        "jerome-bruner",
    "Piaget":        "jean-piaget",
    "Kohlberg":      "lawrence-kohlberg",
    "Bourdieu":      "pierre-bourdieu",
    "Honneth":       "axel-honneth",
    "Stiegler":      "bernard-stiegler",
    "Basaglia":      "franco-basaglia",
    "Canguilhem":    "georges-canguilhem",
    "Goldstein":     "kurt-goldstein",
    "Plessner":      "helmuth-plessner",
    "Dilthey":       "wilhelm-dilthey",
    "Humboldt":      "wilhelm-von-humboldt",
    "Rosa":          "hartmut-rosa",
    "Jonas":         "hans-jonas",
    "Illich":        "ivan-illich",
    "Bowlby":        "john-bowlby",
}
for alias, slug in ALIASES.items():
    if slug in autori_avail:
        name_to_slug[alias] = slug

title_to_slug = {}
for b in biblio:
    if b["id"] not in libri_avail:
        continue
    title_to_slug[b["titolo"]] = b["id"]
    orig = b.get("titolo_originale", "")
    if orig and orig != b["titolo"]:
        short = orig.split(",")[0].split(":")[0].strip()
        if len(short) >= 6 and short not in title_to_slug:
            title_to_slug[short] = b["id"]

# ── HTML immagini ────────────────────────────────────────────────────────
def author_img(slug, nome):
    ext = autori_avail[slug]
    src = ASSETS_URL + "/autori/" + slug + "." + ext
    return ('<img src="' + src + '" alt="' + nome + '" title="' + nome +
            '" class="ref-portrait" style="height:52px;vertical-align:middle;'
            'border-radius:5%;margin:0 4px 0 2px;'
            'box-shadow:0 1px 3px rgba(0,0,0,.25)">')

def book_img(slug, titolo):
    ext = libri_avail[slug]
    src = ASSETS_URL + "/libri/" + slug + "." + ext
    return ('<img src="' + src + '" alt="' + titolo + '" title="' + titolo +
            '" class="ref-cover" style="height:60px;vertical-align:middle;'
            'margin:0 4px 0 2px;box-shadow:0 1px 4px rgba(0,0,0,.3)">')

# ── Pre-compila pattern (una volta sola) ─────────────────────────────────
names_sorted  = sorted(name_to_slug, key=len, reverse=True)
titles_sorted = sorted(title_to_slug, key=len, reverse=True)

author_patterns = []
for name in names_sorted:
    slug = name_to_slug[name]
    esc  = re.escape(name)
    author_patterns.append({
        "name": name, "slug": slug,
        "bold": re.compile("(\\*\\*" + esc + "[,;:]?\\*\\*)"),
        "kw":   re.compile("(?:Per|Cfr\\.|Vedi|Si veda|veda)\\s+(" + esc + ")(?=[,;\\s\\.])"),
        "par":  re.compile("\\((?:[^()]*?;\\s*)?(" + esc + ")(?:\\s*;[^()]*?)?\\)"),
    })

book_patterns = []
for title in titles_sorted:
    slug = title_to_slug[title]
    esc  = re.escape(title)
    book_patterns.append({
        "title": title, "slug": slug,
        "triple": re.compile("(\\*\\*\\*" + esc + "[^*]*?\\*\\*\\*)"),
        "single": re.compile("(?<![*])(\\*" + esc + "[^*\\n]*?\\*)(?![*])"),
    })

print("Autori: " + str(len(author_patterns)) + " pattern | Libri: " + str(len(book_patterns)) + " pattern")

# ── Arricchimento capitolo ────────────────────────────────────────────────
FN_DEF = re.compile(r'^\[\^(\d+)\]:')   # riga di definizione nota
FN_REF = re.compile(r'\[\^(\d+)\]')     # riferimento nel testo

def enrich(content):
    lines = content.split("\n")

    # ── Fase 1: scansiona le note per capire quale immagine va con quale [^N]
    #    Usa seen globale per garantire che ogni immagine appaia UNA sola volta
    seen_a  = set()
    seen_b  = set()
    fn_imgs = {}   # { fn_num: [img_html, ...] }

    for line in lines:
        m = FN_DEF.match(line)
        if not m:
            continue
        fn_num = int(m.group(1))
        imgs   = []

        for ap in author_patterns:
            slug = ap["slug"]
            if slug in seen_a:
                continue
            for pat in (ap["bold"], ap["kw"], ap["par"]):
                if pat.search(line):
                    imgs.append(author_img(slug, ap["name"]))
                    seen_a.add(slug)
                    break

        for bp in book_patterns:
            slug = bp["slug"]
            if slug in seen_b:
                continue
            for pat in (bp["triple"], bp["single"]):
                if pat.search(line):
                    imgs.append(book_img(slug, bp["title"]))
                    seen_b.add(slug)
                    break

        if imgs:
            fn_imgs[fn_num] = imgs

    # ── Fase 2: nel corpo del testo sostituisce [^N] con [^N]<imgs>
    #    Le note rimangono invariate
    inserted = set()   # numeri già inseriti (ogni [^N] va arricchito solo la prima volta)
    lines_out = []

    for line in lines:
        if FN_DEF.match(line):
            lines_out.append(line)   # note: lasciale intatte
            continue

        def replace_ref(m):
            fn_num = int(m.group(1))
            if fn_num not in fn_imgs or fn_num in inserted:
                return m.group(0)
            inserted.add(fn_num)
            return m.group(0) + " " + " ".join(fn_imgs[fn_num])

        lines_out.append(FN_REF.sub(replace_ref, line))

    return "\n".join(lines_out), len(seen_a), len(seen_b)

# ── Processa tutti gli assi ───────────────────────────────────────────────
total_f = 0
total_a = 0
total_b = 0

for asse_dir in sorted(INPUT.iterdir()):
    if not asse_dir.is_dir():
        continue
    if ASSE_FILTER and ASSE_FILTER not in asse_dir.name:
        continue
    out_asse = OUT_DIR / asse_dir.name
    out_asse.mkdir(parents=True, exist_ok=True)
    print("\n--- " + asse_dir.name, flush=True)

    for cap in sorted(asse_dir.iterdir()):
        if cap.suffix != ".md":
            continue
        content = cap.read_text(encoding="utf-8")
        enriched, n_a, n_b = enrich(content)
        (out_asse / cap.name).write_text(enriched, encoding="utf-8")
        total_f += 1
        total_a += n_a
        total_b += n_b
        name_short = cap.name[:60]
        line_out = "  " + name_short.ljust(60) + "  a:" + str(n_a).rjust(2) + "  b:" + str(n_b).rjust(2)
        print(line_out, flush=True)

print("=" * 60)
print("File: " + str(total_f) + " | Foto autori: " + str(total_a) + " | Copertine: " + str(total_b))
