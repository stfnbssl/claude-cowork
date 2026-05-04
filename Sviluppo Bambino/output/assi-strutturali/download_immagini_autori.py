"""
Script: download_immagini_autori.py
Progetto: HCAIRE — Sviluppo Bambino

Scarica le foto degli autori da Wikimedia Commons e le salva in:
  output/assi-strutturali/assets/autori/

Strategia (in ordine di priorità per ogni autore):
  1. Usa il filename hardcodato in autori.json (img_wikimedia_filename)
  2. Se non funziona, interroga l'API Wikipedia per trovare l'immagine
     principale della pagina dell'autore
  3. Se nemmeno questo funziona, segna come "non trovato"

Poi aggiorna autori.json con i metadati della licenza di ogni immagine.

REQUISITI:
  pip install requests

UTILIZZO:
  Eseguire dalla cartella "output/assi-strutturali/" oppure
  adattare BASE_DIR al percorso corretto.

  python download_immagini_autori.py
"""

import json
import os
import re
import time
import requests
from urllib.parse import urlparse

# --- Configurazione ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUTORI_JSON = os.path.join(BASE_DIR, "autori.json")
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "autori")
HEADERS = {
    "User-Agent": "HCAIRE-SviluppoBambino/1.0 (research; stfn.bssl@gmail.com)"
}

os.makedirs(ASSETS_DIR, exist_ok=True)


def get_image_info_from_commons(filename: str) -> dict:
    """Recupera URL e metadati licenza da Wikimedia Commons dato il filename."""
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 400,
        "format": "json",
    }
    r = requests.get(url, params=params, headers=HEADERS, timeout=20)
    r.raise_for_status()
    data = r.json()
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        if page.get("ns") == -1:  # pagina inesistente
            return {}
        ii = page.get("imageinfo", [{}])[0]
        if not ii.get("url"):
            return {}
        meta = ii.get("extmetadata", {})
        return {
            "thumb_url": ii.get("thumburl") or ii.get("url", ""),
            "full_url": ii.get("url", ""),
            "filename": filename,
            "licenza": meta.get("LicenseShortName", {}).get("value", "sconosciuta"),
            "autore_immagine": meta.get("Artist", {}).get("value", ""),
        }
    return {}


def find_image_via_wikipedia(wp_url: str) -> dict:
    """
    Interroga l'API Wikipedia per recuperare l'immagine principale
    della pagina dell'autore, poi risolve il filename su Commons.
    """
    # Estrae il titolo della pagina dall'URL Wikipedia
    # es. https://it.wikipedia.org/wiki/Maurice_Merleau-Ponty -> Maurice_Merleau-Ponty
    match = re.search(r"wikipedia\.org/wiki/(.+)$", wp_url)
    if not match:
        return {}
    page_title = match.group(1).replace("_", " ")

    # Determina la lingua
    lang_match = re.search(r"(https?://)([a-z]+)\.wikipedia", wp_url)
    lang = lang_match.group(2) if lang_match else "en"

    api_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": page_title,
        "prop": "pageimages",
        "piprop": "original|name",
        "pithumbsize": 400,
        "format": "json",
    }
    r = requests.get(api_url, params=params, headers=HEADERS, timeout=20)
    r.raise_for_status()
    data = r.json()
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        filename = page.get("pageimage")
        if filename:
            return get_image_info_from_commons(filename)
    return {}


def download_file(url: str, dest: str):
    """Scarica un file binario."""
    r = requests.get(url, headers=HEADERS, timeout=30, stream=True)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)


def ext_from_url(url: str) -> str:
    """Estrae l'estensione del file dall'URL."""
    path = urlparse(url).path
    ext = path.rsplit(".", 1)[-1].lower().split("?")[0]
    return ext if ext in ("jpg", "jpeg", "png", "gif", "svg", "webp") else "jpg"


def main():
    with open(AUTORI_JSON, encoding="utf-8") as f:
        autori = json.load(f)

    risultati = {"ok": [], "non_trovati": [], "errori": []}

    for autore in autori:
        aid = autore["id"]
        nome = autore["nome_completo"]
        hardcoded_filename = autore.get("img_wikimedia_filename")
        wp_url = autore.get("wikipedia_url", "")

        # Salta autori senza alcuna fonte
        if not hardcoded_filename and not wp_url:
            print(f"  [--] {nome} — nessuna fonte disponibile, salto")
            risultati["non_trovati"].append(aid)
            continue

        print(f"  Cercando: {nome}...", end=" ", flush=True)

        info = {}

        # --- Strategia 1: filename hardcodato ---
        if hardcoded_filename:
            try:
                info = get_image_info_from_commons(hardcoded_filename)
            except Exception as e:
                print(f"\n    [warn] Commons filename fallito: {e}")

        # --- Strategia 2: API Wikipedia ---
        if not info and wp_url:
            try:
                info = find_image_via_wikipedia(wp_url)
            except Exception as e:
                print(f"\n    [warn] Wikipedia API fallita: {e}")

        if not info or not info.get("thumb_url"):
            print("non trovata")
            risultati["non_trovati"].append(aid)
            time.sleep(0.3)
            continue

        # Determina percorso destinazione
        ext = ext_from_url(info["full_url"])
        dest = os.path.join(ASSETS_DIR, f"{aid}.{ext}")

        # Salta se già scaricato (da run precedente)
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            print(f"già presente ✓")
            autore["img_path_locale"] = f"assets/autori/{aid}.{ext}"
            if not autore.get("img_licenza"):
                autore["img_licenza"] = info.get("licenza", "")
                autore["img_autore_foto"] = info.get("autore_immagine", "")
                autore["img_url_wikimedia"] = info.get("full_url", "")
                autore["img_wikimedia_filename"] = info.get("filename", hardcoded_filename or "")
            risultati["ok"].append(aid)
            time.sleep(0.3)
            continue

        try:
            download_file(info["thumb_url"], dest)
        except Exception as e:
            print(f"ERRORE download: {e}")
            risultati["errori"].append({"id": aid, "errore": str(e)})
            time.sleep(0.3)
            continue

        # Aggiorna autore con metadati
        autore["img_path_locale"] = f"assets/autori/{aid}.{ext}"
        autore["img_licenza"] = info.get("licenza", "")
        autore["img_autore_foto"] = info.get("autore_immagine", "")
        autore["img_url_wikimedia"] = info.get("full_url", "")
        autore["img_wikimedia_filename"] = info.get("filename", hardcoded_filename or "")

        lic = info.get("licenza", "?")
        print(f"OK ({lic})")
        risultati["ok"].append(aid)
        time.sleep(0.5)

    # Salva autori.json aggiornato
    with open(AUTORI_JSON, "w", encoding="utf-8") as f:
        json.dump(autori, f, ensure_ascii=False, indent=2)

    # Report finale
    print("\n" + "=" * 50)
    print(f"  Scaricati con successo : {len(risultati['ok'])}")
    print(f"  Non trovati            : {len(risultati['non_trovati'])}")
    print(f"  Errori                 : {len(risultati['errori'])}")
    print("=" * 50)

    if risultati["non_trovati"]:
        print("\nNon trovati (da gestire manualmente):")
        for aid in risultati["non_trovati"]:
            a = next((x for x in autori if x["id"] == aid), {})
            print(f"  - {a.get('nome_completo', aid)}")

    if risultati["errori"]:
        print("\nErrori:")
        for e in risultati["errori"]:
            print(f"  - {e['id']}: {e['errore']}")

    print(f"\nautori.json aggiornato con percorsi e metadati licenza.")
    print(f"Immagini in: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
