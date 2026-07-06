#!/usr/bin/env python3


import argparse
import json
import os
import sys
import datetime

try:
    import dns.resolver
except ImportError:
    print("Errore: installa dnspython -> pip install dnspython --break-system-packages")
    sys.exit(1)

try:
    import google.generativeai as genai
except ImportError:
    print("Errore: installa google-generativeai -> pip install google-generativeai --break-system-packages")
    sys.exit(1)


DEFAULT_RECORD_TYPES = ["A", "AAAA", "MX", "TXT", "NS", "SOA", "CNAME"]


def collect_dns_logs(domain, record_types=None):
    """Raccoglie i record DNS e li struttura come log con timestamp."""
    if record_types is None:
        record_types = DEFAULT_RECORD_TYPES

    logs = {
        "domain": domain,
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "records": {},
    }

    resolver = dns.resolver.Resolver()
    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            logs["records"][rtype] = [r.to_text() for r in answers]
        except dns.resolver.NoAnswer:
            logs["records"][rtype] = []
        except dns.resolver.NXDOMAIN:
            logs["records"][rtype] = "DOMINIO NON ESISTENTE"
        except Exception as e:
            logs["records"][rtype] = f"errore: {str(e)}"

    return logs


def summarize_with_gemini(logs, api_key, model_name="gemini-2.0-flash"):
    """Invia i log a Gemini e restituisce una sintesi testuale."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    prompt = f"""Sei un analista OSINT. Analizza i seguenti dati DNS raccolti
        in modalità passiva e fornisci una risposta strutturata in italiano con queste sezioni:
        1. RIEPILOGO INFRASTRUTTURA — cosa rivelano i record sulla configurazione del dominio
        2. ANOMALIE O PUNTI DI INTERESSE — es. record TXT insoliti (SPF/DKIM/verifiche),
            numero di MX, eventuali CNAME sospetti, wildcard, ecc.
        3. PROSSIMI PASSI OSINT PASSIVI SUGGERITI — solo tecniche non intrusive
            (es. subdomain enumeration passiva, certificate transparency logs, ecc.)
        Dati DNS raccolti:
        {json.dumps(logs, indent=2, ensure_ascii=False)}
    """

    response = model.generate_content(prompt)
    return response.text


def main():
    parser = argparse.ArgumentParser(
        description="Raccolta log DNS + sintesi automatica tramite Gemini API."
    )
    parser.add_argument("domain", help="Dominio target (es. example.com)")
    parser.add_argument(
        "--types", nargs="+", default=None,
        help=f"Tipi di record DNS (default: {' '.join(DEFAULT_RECORD_TYPES)})"
    )
    parser.add_argument(
        "--model", default="gemini-2.0-flash",
        help="Nome del modello Gemini da usare (default: gemini-2.0-flash)"
    )
    parser.add_argument(
        "--log-output", default=None,
        help="File JSON per i log grezzi (default: dns_log_<domain>.json)"
    )
    parser.add_argument(
        "--summary-output", default=None,
        help="File TXT per la sintesi AI (default: dns_summary_<domain>.txt)"
    )

    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Errore: imposta la variabile d'ambiente GEMINI_API_KEY.")
        sys.exit(1)

    print(f"Raccolgo log DNS per {args.domain}...")
    logs = collect_dns_logs(args.domain, args.types)

    log_path = args.log_output or f"dns_log_{args.domain}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)
    print(f"✔ Log grezzi salvati in: {log_path}")

    print("Invio i dati a Gemini per la sintesi...")
    summary = summarize_with_gemini(logs, api_key, args.model)

    summary_path = args.summary_output or f"dns_summary_{args.domain}.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"\n{'=' * 60}")
    print("SINTESI AI")
    print(f"{'=' * 60}\n")
    print(summary)
    print(f"\n✔ Sintesi salvata in: {summary_path}")


if __name__ == "__main__":
    main()
