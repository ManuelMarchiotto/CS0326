# Esplorazione del Traffico DNS con Wireshark - Domande e Risposte

---

## Parte 2: Esplorare il Traffico delle Query DNS

### Domanda (Punto d)
* **Domanda:** Quali sono gli indirizzi MAC di origine e destinazione? A quali interfacce di rete sono associati questi indirizzi MAC?
* **Risposta:** 
  * **MAC di origine:** Corrisponde all'indirizzo fisico dell'interfaccia di rete (scheda Wi-Fi o Ethernet) del **PC locale** su cui si sta eseguendo il laboratorio.
  * **MAC di destinazione:** Corrisponde all'indirizzo fisico dell'interfaccia del **Default Gateway** (il router di rete locale), poiché il traffico è destinato a uscire dalla rete locale verso internet.

---

### Domanda (Punto e)
* **Domanda:** Quali sono gli indirizzi IP di origine e destinazione? A quali interfacce di rete sono associati questi indirizzi IP?
* **Risposta:** 
  * **IP di origine:** È l'indirizzo IPv4 privato assegnato al **PC locale** (`10.0.2.15`).
  * **IP di destinazione:** È l'indirizzo IPv4 del **Server DNS** utilizzato dalla macchina per la risoluzione dei nomi (può essere l'IP del router locale, del provider ISP o un resolver pubblico come `8.8.8.8` o `1.1.1.1`).

---

### Domanda (Punto f)
* **Domanda:** Quali sono le porte di origine e destinazione? Qual è il numero di porta DNS predefinito?
* **Risposta:** 
  * **Porta di origine:** È una porta dinamica/ephemerale casuale generata dal client (`44536`).
  * **Porta di destinazione:** È la porta `53`.
  * **Porta DNS predefinita:** Il numero di porta predefinito per il servizio DNS è **53** (utilizza sia UDP che TCP, anche se le query standard usano **UDP/53**).

---

### Domanda (Punto g)
* **Domanda:** Confrontare gli indirizzi MAC e IP nei risultati di Wireshark con gli indirizzi IP e MAC registrati dai comandi (`ipconfig` / `arp` / `ifconfig`). Qual è la tua osservazione?
* **Risposta:** 
  * L'**IP e il MAC di origine** presenti nel pacchetto catturato da Wireshark coincidono perfettamente con gli indirizzi IP e MAC dell'interfaccia attiva registrati sul PC tramite riga di comando.
  * L'**IP di destinazione** corrisponde all'indirizzo IP del Server DNS configurato nella scheda di rete.
  * Il **MAC di destinazione** corrisponde al MAC del Gateway Predefinito mostrato nella tabella ARP per l'IP del router.

---

## Parte 3: Esplorare il Traffico delle Risposte DNS

### Domanda (Punto a)
* **Domanda:** Quali sono gli indirizzi MAC e IP e i numeri di porta di origine e destinazione? Come si confrontano con gli indirizzi nei pacchetti di query DNS?
* **Risposta:** 
  In un pacchetto di risposta, **origine e destinazione sono invertite** rispetto alla query:
  * **IP e MAC di origine:** Indicano ora il Server DNS / Router (destinazione precedente).
  * **IP e MAC di destinazione:** Indicano ora il PC locale (origine precedente).
  * **Porta di origine:** È la porta `53` (Server DNS).
  * **Porta di destinazione:** È la porta dinamica aperta dal PC per la richiesta iniziale.

---

### Domanda (Punto c)
* **Domanda:** Il server DNS può fare query ricorsive?
* **Risposta:** **Sì.** Nel campo *Flags* della risposta DNS, il bit **"Recursion Available: Server can do recursive queries"** è impostato su `1` (true). Questo conferma che il server DNS supporta ed ha eseguito la ricerca ricorsiva per conto del client.

---

### Domanda (Punto d)
* **Domanda:** Come si confrontano i risultati con quelli di `nslookup`?
* **Risposta:** I risultati sono identici. Sia la risposta in Wireshark sia l'output del comando `nslookup` mostrano lo stesso nome di dominio cercato, l'eventuale alias (**CNAME**) e gli stessi indirizzi IPv4/IPv6 (**A/AAAA records**) associati al sito web richiesto (es. `www.cisco.com`).

---

## Domande di Riflessione

### Domanda 1
* **Domanda:** Dai risultati di Wireshark, cos'altro puoi imparare sulla rete quando rimuovi il filtro?
* **Risposta:** Rimuovendo il filtro si può visualizzare tutto il traffico che passa attraverso la scheda di rete. È possibile scoprire:
  * Tutti i protocolli attivi in rete (ARP, DHCP, ICMP, HTTP/HTTPS, TCP/UDP).
  * Gli indirizzi IP e MAC di tutti gli altri dispositivi della sottorete locale con cui il PC comunica.
  * Le applicazioni in esecuzione sul PC che tentano di connettersi ad Internet in background.
  * Eventuali trasmissioni in broadcast o multicast presenti sul segmento di rete.

---

### Domanda 2
* **Domanda:** Come può un attaccante usare Wireshark per compromettere la sicurezza della tua rete?
* **Risposta:** Un attaccante che riesce ad eseguire Wireshark all'interno della stessa rete (o tramite tecniche come l'ARP Spoofing/Poisoning) può:
  * **Intercettare credenziali e dati sensibili:** Leggere password, messaggi, cookie di sessione o dati trasmessi in chiaro (usando protocolli non crittografati come HTTP, Telnet, FTP, POP3).
  * **Eseguire Ricognizione (Eavesdropping):** Mappare la topologia di rete, scoprire quali sistemi operativi, indirizzi IP, servizi e porte sono attivi per pianificare un attacco mirato.
  * **Analizzare le abitudini degli utenti:** Tracciare i siti web visitati tramite l'ispezione delle query DNS in chiaro.