

import argparse
import json
import sys
import datetime

try:
    import dns.resolver
except ImportError:
    print("Errore: installa dnspython -> pip install dnspython --break-system-packages")
    sys.exit(1)

try:
    import whois
except ImportError:
    whois = None
    print("Attenzione: python-whois non installato, il modulo WHOIS sarà saltato.")
    print("Installa con: pip install python-whois --break-system-packages")


DEFAULT_RECORD_TYPES = ["A", "AAAA", "MX", "TXT", "NS", "SOA", "CNAME"]


def collect_dns_records(domain, record_types=None):
    """Interroga il dominio per i tipi di record DNS specificati."""
    if record_types is None:
        record_types = DEFAULT_RECORD_TYPES

    results = {}
    resolver = dns.resolver.Resolver()

    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            results[rtype] = [r.to_text() for r in answers]
        except dns.resolver.NoAnswer:
            results[rtype] = []
        except dns.resolver.NXDOMAIN:
            results[rtype] = "DOMINIO NON ESISTENTE"
        except Exception as e:
            results[rtype] = f"errore: {str(e)}"

    return results


def collect_whois(domain):
    """Recupera i dati WHOIS per il dominio, se il modulo è disponibile."""
    if whois is None:
        return {"errore": "modulo python-whois non disponibile"}

    try:
        w = whois.whois(domain)
        # Converte in dict serializzabile (alcuni campi sono datetime)
        data = {}
        for key, value in w.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                data[key] = value.isoformat()
            elif isinstance(value, list):
                data[key] = [
                    v.isoformat() if isinstance(v, (datetime.datetime, datetime.date)) else v
                    for v in value
                ]
            else:
                data[key] = value
        return data
    except Exception as e:
        return {"errore": str(e)}


def build_report(domain, record_types=None):
    """Costruisce il report completo DNS + WHOIS."""
    report = {
        "domain": domain,
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "dns_records": collect_dns_records(domain, record_types),
        "whois": collect_whois(domain),
    }
    return report


def print_summary(report):
    """Stampa un riepilogo leggibile a video."""
    print(f"\n{'=' * 60}")
    print(f"REPORT OSINT PASSIVO — {report['domain']}")
    print(f"Generato: {report['timestamp_utc']}")
    print(f"{'=' * 60}\n")

    print("--- Record DNS ---")
    for rtype, values in report["dns_records"].items():
        print(f"\n[{rtype}]")
        if isinstance(values, list):
            if values:
                for v in values:
                    print(f"  {v}")
            else:
                print("  (nessun record)")
        else:
            print(f"  {values}")

    print("\n--- WHOIS ---")
    whois_data = report["whois"]
    if "errore" in whois_data:
        print(f"  {whois_data['errore']}")
    else:
        interesting_fields = [
            "domain_name", "registrar", "whois_server", "creation_date",
            "expiration_date", "updated_date", "name_servers", "status",
            "emails", "org", "country",
        ]
        for field in interesting_fields:
            if field in whois_data and whois_data[field]:
                print(f"  {field}: {whois_data[field]}")


def main():
    parser = argparse.ArgumentParser(
        description="Raccolta OSINT passiva: DNS + WHOIS su un dominio."
    )
    parser.add_argument("domain", help="Dominio target (es. example.com)")
    parser.add_argument(
        "--types", nargs="+", default=None,
        help=f"Tipi di record DNS da interrogare (default: {' '.join(DEFAULT_RECORD_TYPES)})"
    )
    parser.add_argument(
        "--output", default=None,
        help="Percorso file JSON di output (default: dns_report_<domain>.json)"
    )

    args = parser.parse_args()

    report = build_report(args.domain, args.types)
    print_summary(report)

    output_path = args.output or f"dns_report_{args.domain}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n✔ Report completo salvato in: {output_path}")


if __name__ == "__main__":
    main()
