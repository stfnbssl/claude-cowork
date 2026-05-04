"""
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
