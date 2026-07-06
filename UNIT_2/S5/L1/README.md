# OSINT Passivo — Toolkit DNS / WHOIS / Dorking / AI Summary

Toolkit didattico per la raccolta passiva di informazioni da fonti aperte (OSINT)
su un dominio, con supporto per interrogazioni DNS, WHOIS, Google Dorking tramite
API ufficiale e sintesi automatica dei risultati con Gemini.

## ⚠️ Nota etica e legale

Usa questi strumenti **solo** su:
- domini di tua proprietà, oppure
- target per cui hai un'autorizzazione scritta esplicita (es. scope di bug bounty,
  penetration test contrattualizzato, laboratorio didattico).

La raccolta di record DNS e WHOIS pubblici è generalmente lecita in quanto dati
pubblici, ma resta tua responsabilità rispettare leggi locali, ToS delle
piattaforme e policy dell'organizzazione target.

## Struttura del progetto

```
osint_project/
├── dns_recon.py          # Interrogazioni DNS + WHOIS
├── dork_search.py        # Google Dorking via Custom Search API
├── ai_dns_summary.py      # Log DNS + sintesi con Gemini API
├── requirements.txt
└── README.md
```

## Installazione

```bash
pip install -r requirements.txt --break-system-packages
```

## 1. DNS + WHOIS recon

```bash
python dns_recon.py example.com
python dns_recon.py example.com --types A MX TXT
python dns_recon.py example.com --output report.json
```

Produce un report a video e un file JSON con tutti i record DNS e i dati WHOIS.

## 2. Google Dorking

Richiede una API key e un Search Engine ID (cx) di Google Custom Search:

1. Crea un motore su https://programmablesearchengine.google.com/ (attiva
   "Search the entire web")
2. Genera una API key su https://console.cloud.google.com/apis/credentials
   e abilita "Custom Search API"

```bash
export GOOGLE_API_KEY="la_tua_chiave"
export GOOGLE_CX="il_tuo_cx"

python dork_search.py example.com
python dork_search.py example.com --dorks "filetype:pdf" "inurl:admin"
```

Nota: la versione gratuita dell'API ha un limite di 100 query/giorno.

## 3. Log DNS + sintesi AI (Gemini)

```bash
export GEMINI_API_KEY="la_tua_chiave"   # https://aistudio.google.com/apikey

python ai_dns_summary.py example.com
```

Lo script raccoglie i record DNS, li salva come log JSON con timestamp,
e li invia a Gemini per generare un riepilogo con:
- panoramica dell'infrastruttura
- anomalie o punti di interesse
- suggerimenti per ulteriori step OSINT passivi

## Sfida extra: Maltego

Maltego è uno strumento grafico non pensato per l'automazione da riga di comando.
Workflow suggerito:

1. Crea un nuovo grafo, inserisci l'entità **Domain**
2. Applica i Transform standard: `To DNS Name`, `To MX Record`,
   `To IP Address`, `To Netblock`, `To Whois Details`
3. Se disponibili, usa i Transform Hub di **SecurityTrails** o **Shodan**
   per arricchire con sottodomini e host esposti
4. Espandi verso entità **Person/Email** se emergono contatti nei record WHOIS
5. Usa il layout "Block" per raggruppare le entità per tipologia

I file JSON prodotti da `dns_recon.py` possono essere usati come riferimento
per costruire manualmente le entità in Maltego, o come input per un
Transform locale personalizzato (Local Transform in Python).
