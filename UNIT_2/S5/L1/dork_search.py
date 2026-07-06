
import argparse
import json
import os
import sys
import time

import requests

DEFAULT_DORKS = [
    'filetype:pdf',
    'filetype:xlsx OR filetype:docx',
    'filetype:sql',
    'ext:env OR ext:log OR ext:bak',
    'intitle:"index of"',
    'inurl:admin',
    'inurl:login',
]

API_URL = "https://www.googleapis.com/customsearch/v1"


def run_dork(query, site, api_key, cx, num=10):
    """Esegue una singola query dork tramite Custom Search API."""
    full_query = f"site:{site} {query}"
    params = {
        "key": api_key,
        "cx": cx,
        "q": full_query,
        "num": min(num, 10),  # l'API limita a 10 risultati per richiesta
    }

    try:
        r = requests.get(API_URL, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        return {"query": full_query, "errore": str(e), "results": []}

    items = data.get("items", [])
    results = [
        {"title": i.get("title"), "link": i.get("link"), "snippet": i.get("snippet")}
        for i in items
    ]

    return {"query": full_query, "results": results, "total_found": len(results)}


def run_all_dorks(site, dorks, api_key, cx, delay=1.0):
    """Esegue una lista di dork con un piccolo delay per non saturare le quote."""
    all_results = []
    for dork in dorks:
        print(f"Eseguo: site:{site} {dork}")
        res = run_dork(dork, site, api_key, cx)
        all_results.append(res)
        time.sleep(delay)  # rispetta le rate limit dell'API (100 query/giorno gratis)
    return all_results


def print_summary(all_results):
    print(f"\n{'=' * 60}")
    print("RISULTATI GOOGLE DORKING")
    print(f"{'=' * 60}")

    for res in all_results:
        print(f"\nQuery: {res['query']}")
        if "errore" in res:
            print(f"  Errore: {res['errore']}")
            continue
        if not res["results"]:
            print("  Nessun risultato pubblico trovato.")
        for item in res["results"]:
            print(f"  - {item['title']}")
            print(f"    {item['link']}")


def main():
    parser = argparse.ArgumentParser(
        description="Google Dorking tramite Custom Search API (OSINT passivo)."
    )
    parser.add_argument("site", help="Dominio target (es. example.com)")
    parser.add_argument(
        "--dorks", nargs="+", default=None,
        help="Lista di dork personalizzati (default: set predefinito)"
    )
    parser.add_argument(
        "--output", default=None,
        help="File JSON di output (default: dork_results_<site>.json)"
    )

    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_API_KEY")
    cx = os.environ.get("GOOGLE_CX")

    if not api_key or not cx:
        print("Errore: imposta le variabili d'ambiente GOOGLE_API_KEY e GOOGLE_CX.")
        print("Vedi le istruzioni di setup nel docstring dello script.")
        sys.exit(1)

    dorks = args.dorks or DEFAULT_DORKS
    all_results = run_all_dorks(args.site, dorks, api_key, cx)
    print_summary(all_results)

    output_path = args.output or f"dork_results_{args.site}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\n✔ Risultati salvati in: {output_path}")


if __name__ == "__main__":
    main()
