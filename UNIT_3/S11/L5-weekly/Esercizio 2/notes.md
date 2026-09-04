# Report di Analisi Malware: Task ANY.RUN `9a158718-43fe-45ce-85b3-66203dbc2281`

**Data Analisi:** 4 Settembre 2026  
**Fonte Dati:** ANY.RUN Interactive Malware Sandbox  
**Valutazione Complessiva:** 🔴 **MINACCIA CRITICA / MALICIOUS**  

---

## 1. Sintesi Esecutiva

Il campione analizzato si riferisce a un'infezione multi-stadio veicolata tramite repository **GitHub** compromessi o creati *ad hoc* (`MELITERRER/frew` e `MELITERRER/kioluu`). 

L'eseguibile principale (**`Muadnrd.exe`** / **`Jvczfhe.exe`**) è scritto in ambiente **.NET**, protetto e offuscato tramite **.NET Reactor**, e mette in atto diverse tecniche di **Evasione Sandbox** (tramite ritardi di esecuzione con `timeout.exe`) ed **Esecuzione tramite Proxy di Sistema** (usando `InstallUtil.exe`). Le comunicazioni con l'infrastruttura di Comando e Controllo (C2) avvengono sfruttando domini **Dynamic DNS (`*.duckdns.org`)**.

---

## 2. Informazioni sul Campione & IOC

### 📄 File e Artefatti
| Proprietà | Dettaglio |
| :--- | :--- |
| **Nomi File Rilevati** | `Jvczfhe.exe`, `Muadnrd.exe` |
| **Formato File** | Executable Windows (PE32, .NET Assembly) |
| **Protezione / Packer** | **.NET Reactor** (`.NET Reactor protector has been detected`) |
| **Origine / URL Download** | `https://github.com/MELITERRER/frew`, `https://github.com/MELITERRER/kioluu` |

### 🌐 Indicatori di Compromissione di Rete (Network IOCs)
| Tipologia | Indicatore | Descrizione / Ruolo |
| :--- | :--- | :--- |
| **C2 Domain** | `*.duckdns.org` | Infrastruttura di Comando & Controllo tramite Dynamic DNS |
| **Download Host** | `github.com`, `raw.githubusercontent.com` | Distribuzione del payload iniziale |
| **TLS/OCSP Checks** | `r10.o.lencr.org`, `r11.o.lencr.org` | Verifica validità certificati Let's Encrypt usati per connessioni HTTPS |
| **TLS/OCSP Checks** | `ocsp.sectigo.com`, `ocsp.digicert.com` | Verifica certificati CA aggiuntivi |
| **Indirizzi IP** | `140.82.114.21`, `140.82.121.6` | Server GitHub CDN / API |
| **Indirizzi IP** | `184.24.77.x` | Server CDN Akamai (revoca/validazione certificati) |

---

## 3. Catena di Esecuzione dei Processi (*Process Tree*)

L'albero dei processi evidenzia la seguente sequenza operativa:

```
[2256] svchost.exe (-k NetworkService -p -s Dnscache)
  └── [6552] firefox.exe (Navigazione verso repository GitHub)
        └── [6596] firefox.exe (Download del file eseguibile)
              └── [7492] Jvczfhe.exe (Primo stadio eseguibile)
                    ├── [7520] cmd.exe /c timeout 21 & exit
                    │     └── [7572] timeout.exe 21 (Anti-Sandbox Delay)
                    ├── [5152] InstallUtil.exe (LOLBIN Proxy Execution)
                    └── [7824] Muadnrd.exe (Secondo stadio / Payload)
                          ├── [7876] cmd.exe /c timeout 21 & exit
                          │     └── [7968] timeout.exe 21
                          ├── [7248] Muadnrd.exe (Istanza attiva)
                          └── [7584] WerFault.exe -u -p 7824 -s 2888 (Crash Handler / Injection Error)
```

### Dettaglio delle Fasi di Esecuzione:
1. **Fase 1: Download & Initial Execution**  
   Il browser `firefox.exe` scarica il binario dal repository GitHub. L'utente o uno script esegue `Jvczfhe.exe`.
2. **Fase 2: Defense Evasion (Time Delay)**  
   Il malware esegue `cmd.exe /c timeout 21 & exit` invocando `timeout.exe 21`. Questa pausa forzata di 21 secondi serve a far scadere il tempo di analisi automatizzata delle sandbox tradizionali.
3. **Fase 3: Process Hollowing / LOLBIN Execution**  
   Viene chiamato `InstallUtil.exe` (tool legittimo di .NET Framework). Il malware lo abusa per caricare ed eseguire codice arbitrario in memoria evitando la firma del file.
4. **Fase 4: Payload Execution & Crash**  
   Viene avviato `Muadnrd.exe` (protetto con .NET Reactor). Un'istanza genera un errore o tentativo di injection intercettato da `WerFault.exe`, mentre l'istanza principale continua l'attività in background.

---

## 4. Mappatura Tattiche e Tecniche MITRE ATT&CK

| ID Tecnica | Nome Tecnica | Descrizione nel Caso Specifico |
| :--- | :--- | :--- |
| **T1204.002** | User Execution: Malicious File | Download ed esecuzione manuale/automatica di eseguibili dannosi da GitHub. |
| **T1497.003** | Time Based Evasion | Utilizzo di `timeout.exe` per ritardare l'esecuzione ed eludere il tempo limite delle sandbox. |
| **T1218** | System Binary Proxy Execution | Abuso del binario di sistema Windows `InstallUtil.exe` per eseguire codice non verificato. |
| **T1027** | Obfuscated Files or Information | Uso del packer/protettore `.NET Reactor` per ostacolare il reversing e il decompiling. |
| **T1568.002** | Dynamic DNS | Sfruttamento dei domini `duckdns.org` per contattare i server C2 nascondendo l'IP reale. |

---

## 5. Regole e Rilevamenti Suricata / Network Threats

* **Severity:** 🟠 `Potentially Bad Traffic`
* **Signature:** `ET INFO DYNAMIC_DNS Query to a *.duckdns.org Domain`
* **Processo Coinvolto:** `svchost.exe` (PID 2256) / `Muadnrd.exe`
* **Impatto:** Le query DNS verso `*.duckdns.org` indicano la presenza di un beaconing o tentativo di connessione ad un server C2 dinamico non autorizzato.

---

## 6. Raccomandazioni e Mitigazione

### 🛡️ Misure Inmediate (Containment)
1. **Blocco DNS / Firewall:**  
   Bloccare la risoluzione DNS e il traffico verso tutti i sottodomini `*.duckdns.org` a livello aziendale/gateway.
2. **Isolamento dell'Endpoint:**  
   Se un host della rete ha eseguito `Jvczfhe.exe` o `Muadnrd.exe`, isolarlo immediatamente dalla rete locale per prevenire lo spostamento laterale.

### 🔍 Monitoraggio ed EDR
1. **Regole di Rilevamento dei Processi:**  
   Configurare l'EDR per creare un alert prioritario quando:
   * `firefox.exe` o altri browser generano processi `.exe` direttamente nelle cartelle `Downloads` o `Temp`.
   * `InstallUtil.exe` viene eseguito da percorsi non amministrativi o da utente standard.
   * `cmd.exe` chiama `timeout.exe` subito dopo il primo avvio di un eseguibile non firmato.
2. **Integrità Software / Blocco Download:**  
   Restringere o monitorare i download di file eseguibili provenienti da domini pubblici come `github.com` se non rientrano nel flusso di lavoro autorizzato.

---
*Report generato da analisi automatizzata di artefatti visivi e telemetry di ANY.RUN.*