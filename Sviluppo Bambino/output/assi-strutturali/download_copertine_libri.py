"""
Script: download_copertine_libri.py
Progetto: HCAIRE — Sviluppo Bambino

Scarica le copertine dei libri da Open Library e Google Books.
Le salva in: output/assi-strutturali/assets/libri/
Aggiorna bibliografia.json con il percorso locale di ogni copertina.

FONTI:
  1. Open Library (archive.org) — ricerca per titolo + autore
  2. Google Books API  — fallback gratuito, nessuna API key necessaria

REQUISITI:
  pip install requests

UTILIZZO:
  python download_copertine_libri.py
"""

import json
import os
import re
import time
import requests
from urllib.parse import urlparse, parse_qs, unquote, quote

# --- Configurazione ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIBLIO_JSON = os.path.join(BASE_DIR, "bibliografia.json")
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "libri")
HEADERS = {"User-Agent": "HCAIRE-SviluppoBambino/1.0 (research; stfn.bssl@gmail.com)"}

os.makedirs(ASSETS_DIR, exist_ok=True)


# ── Helper ─────────────────────────────────────────────────────────────────

def is_placeholder(data: bytes) -> bool:
    """Open Library restituisce ~807 byte per immagini mancanti."""
    return len(data) < 2000


def save(data: bytes, dest: str):
    with open(dest, "wb") as f:
        f.write(data)


def get(url: str, **kwargs) -> requests.Response:
    return requests.get(url, headers=HEADERS, timeout=20, **kwargs)


def author_slug(autore_id: str) -> str:
    """Converte un autore_id kebab-case in nome leggibile per la query."""
    return autore_id.replace("-", " ").title()


# ── Open Library ────────────────────────────────────────────────────────────

def search_open_library(titolo: str, autore: str) -> dict:
    """
    Cerca su Open Library per titolo + autore.
    Restituisce il primo risultato con copertina.
    """
    query = f"{titolo} {autore}"
    r = get("https://openlibrary.org/search.json",
            params={"q": query, "fields": "key,cover_i,title,author_name", "limit": 5})
    r.raise_for_status()
    for doc in r.json().get("docs", []):
        cover_i = doc.get("cover_i")
        key = doc.get("key", "")
        olid = re.search(r"OL\d+W", key)
        if cover_i:
            return {"cover_url": f"https://covers.openlibrary.org/b/id/{cover_i}-L.jpg",
                    "fonte": "open_library",
                    "olid": olid.group(0) if olid else None}
        if olid:
            url = f"https://covers.openlibrary.org/b/olid/{olid.group(0)}-L.jpg"
            return {"cover_url": url, "fonte": "open_library", "olid": olid.group(0)}
    return {}


# ── Google Books ─────────────────────────────────────────────────────────────

def search_google_books(titolo: str, autore: str) -> dict:
    """
    Cerca su Google Books API (endpoint pubblico, no API key).
    Restituisce URL copertina se trovato.
    """
    # Prova prima con titolo esatto, poi con titolo originale se diverso
    query = f'intitle:"{titolo}" inauthor:"{autore}"'
    r = get("https://www.googleapis.com/books/v1/volumes",
            params={"q": query, "maxResults": 3, "printType": "books",
                    "orderBy": "relevance"})
    r.raise_for_status()
    items = r.json().get("items", [])

    # Se non trova nulla con ricerca stretta, prova più larga
    if not items:
        query = f"{titolo} {autore}"
        r = get("https://www.googleapis.com/books/v1/volumes",
                params={"q": query, "maxResults": 3, "printType": "books"})
        r.raise_for_status()
        items = r.json().get("items", [])

    for item in items:
        links = item.get("volumeInfo", {}).get("imageLinks", {})
        # Preferisce la risoluzione più alta disponibile
        for size in ("large", "medium", "small", "thumbnail"):
            url = links.get(size)
            if url:
                # Forza HTTPS e richiede zoom più alto per qualità maggiore
                url = url.replace("http://", "https://").replace("zoom=1", "zoom=2")
                return {"cover_url": url, "fonte": "google_books",
                        "gb_id": item.get("id", "")}
    return {}


# ── Titolo originale come query alternativa ─────────────────────────────────

def try_original_title(voce: dict) -> dict:
    """
    Se il titolo italiano non dà risultati,
    prova con il titolo originale (spesso più trovabile su GB).
    """
    orig = voce.get("titolo_originale", "")
    autore = author_slug(voce.get("autore_id", ""))
    if not orig or orig == voce["titolo"]:
        return {}
    result = search_google_books(orig, autore)
    if not result:
        result = search_open_library(orig, autore)
    return result


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    with open(BIBLIO_JSON, encoding="utf-8") as f:
        biblio = json.load(f)

    ok, non_trovate, errori = [], [], []

    for voce in biblio:
        bid = voce["id"]
        titolo = voce["titolo"]
        autore = author_slug(voce.get("autore_id", ""))
        dest = os.path.join(ASSETS_DIR, f"{bid}.jpg")

        print(f"  {titolo[:52]:<52}", end=" ", flush=True)

        # Salta se già scaricata con successo
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            print("già presente ✓")
            voce["img_copertina"] = f"assets/libri/{bid}.jpg"
            ok.append(bid)
            continue

        result = {}
        try:
            # 1. Open Library (titolo italiano + autore)
            result = search_open_library(titolo, autore)
            time.sleep(0.3)

            # 2. Google Books (titolo italiano + autore)
            if not result:
                result = search_google_books(titolo, autore)
                time.sleep(0.3)

            # 3. Titolo originale su entrambe le fonti
            if not result:
                result = try_original_title(voce)
                time.sleep(0.3)

            if not result:
                print("non trovata")
                non_trovate.append(bid)
                continue

            # Scarica
            r = get(result["cover_url"], stream=True)
            r.raise_for_status()
            data = r.content

            if is_placeholder(data):
                # Prova con Google Books anche se OL aveva dato un URL
                if result.get("fonte") != "google_books":
                    result2 = search_google_books(titolo, autore)
                    if not result2:
                        result2 = try_original_title(voce)
                    if result2:
                        r2 = get(result2["cover_url"], stream=True)
                        r2.raise_for_status()
                        if not is_placeholder(r2.content):
                            data = r2.content
                            result = result2

            if is_placeholder(data):
                print("non trovata (solo placeholder)")
                non_trovate.append(bid)
                continue

            save(data, dest)
            voce["img_copertina"] = f"assets/libri/{bid}.jpg"
            voce["img_copertina_fonte"] = result.get("fonte", "")
            if result.get("olid"):
                voce["ol_work_id"] = result["olid"]

            print(f"OK ({result.get('fonte', '?')})")
            ok.append(bid)

        except Exception as e:
            print(f"ERRORE: {e}")
            errori.append({"id": bid, "errore": str(e)})

        time.sleep(0.4)

    # Salva JSON aggiornato
    with open(BIBLIO_JSON, "w", encoding="utf-8") as f:
        json.dump(biblio, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"  Copertine scaricate : {len(ok)}")
    print(f"  Non disponibili     : {len(non_trovate)}")
    print(f"  Errori              : {len(errori)}")
    print("=" * 60)

    if non_trovate:
        print("\nSenza copertina:")
        for bid in non_trovate:
            v = next((x for x in biblio if x["id"] == bid), {})
            print(f"  - {v.get('titolo', bid)}")

    if errori:
        print("\nErrori:")
        for e in errori:
            print(f"  - {e['id']}: {e['errore']}")

    print(f"\nbibliografia.json aggiornato. Copertine in: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
