Cos'è Nmap?

Nmap (Network Mapper) è uno strumento open source gratuito utilizzato per la scansione delle reti, la scoperta di host e l'analisi della sicurezza informatica.

Per cosa viene usato nmap?

Nmap viene impiegato da amministratori di rete, etical hacker e professionisti della sicurezza per diverse finalità:

- Discovery di Host: Rileva quali dispositivi (computer, server, stampanti, router) sono accesi e connessi a una rete.
- Scansione delle Porte: Individua le porte di rete aperte (TCP e UDP) su un target per capire quali servizi sono raggiungibili.
- Identificazione dei Servizi e delle Versioni: Determina quali applicazioni (es. Apache, OpenSSH, MySQL) e relative versioni sono in esecuzione sulle porte aperte.
- Fingerprinting del Sistema Operativo: Analizza la risposta ai pacchetti di rete per indovinare il sistema operativo (es. Windows, Linux, macOS) e il tipo di hardware del target.
- Audit di Sicurezza e Vulnerabilità: Attraverso l'Nmap Scripting Engine (NSE), permette di automatizzare controlli per rilevare vulnerabilità note, errate configurazioni o malware.
- Mappatura e Inventario della Rete: Aiuta gli amministratori a tenere traccia dei dispositivi attivi e a verificare la rispondenza alle policy di sicurezza.

Qual è il comando nmap usato?

nmap -A -T4 scanme.nmap.org

Cosa fa l'opzione -A? Cosa fa l'opzione -T4?

- nmap: Il programma di scansione.
- -A: Attiva il rilevamento del sistema operativo (OS detection), il rilevamento della versione dei servizi, lo script scanning e il traceroute.
- -T4: Imposta la velocità di scansione su un livello più rapido (Aggressive timing).
- scanme.nmap.org: L'host/dominio target della scansione.

Quali porte e servizi sono aperti?

nmap -A -T4 scanme.nmap.org
Starting Nmap 7.97 ( https://nmap.org ) at 2026-09-04 09:09 -0400
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.18s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE        VERSION
22/tcp    open     ssh            OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open     http           Apache httpd 2.4.7 ((Ubuntu))
|_http-title: Go ahead and ScanMe!
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-favicon: Nmap Project
135/tcp   filtered msrpc
593/tcp   filtered http-rpc-epmap
9929/tcp  open     nping-echo     Nping echo
31337/tcp open     tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Dall'output del comando ip address visibile nell'immagine, la tua macchina virtuale appartiene alla rete:

10.0.2.0/24

A quale rete appartiene la tua VM? 

Dettagli dell'interfaccia principale (enp0s3):
- Indirizzo IP della VM: 10.0.2.15
- Subnet Mask (CIDR): /24 (corrispondente a 255.255.255.0)
- Indirizzo di Network: 10.0.2.0
- Indirizzo di Broadcast: 10.0.2.255

Quanti host sono attivi?

[analyst@secOps ~]$ nmap -A -T4 10.0.2.0/24
Starting Nmap 7.97 ( https://nmap.org ) at 2026-09-04 09:14 -0400
Stats: 0:01:05 elapsed; 254 hosts completed (2 up), 2 undergoing Service Scan
Service scan Timing: About 80.00% done; ETC: 09:15 (0:00:05 remaining)
Nmap scan report for 10.0.2.2
Host is up (0.00027s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
631/tcp  open  ipp           CUPS 2.4
|_http-server-header: CUPS/2.4 IPP/2.1
|_http-title: Bad Request - CUPS v2.4.16
3389/tcp open  tcpwrapped
| rdp-ntlm-info: 
|   Target_Name: MANUEL-KATANA-17-B12VGK
|   NetBIOS_Domain_Name: MANUEL-KATANA-17-B12VGK
|   NetBIOS_Computer_Name: MANUEL-KATANA-17-B12VGK
|   DNS_Domain_Name: MANUEL-KATANA-17-B12VGK
|   DNS_Computer_Name: MANUEL-KATANA-17-B12VGK
|   Product_Version: 10.0.22631
|_  System_Time: 2026-09-04T13:14:52+00:00
3390/tcp open  ms-wbt-server xrdp
| rdp-ntlm-info: 
|   Target_Name: MANUEL-KATANA-17-B12VGK
|   NetBIOS_Domain_Name: MANUEL-KATANA-17-B12VGK
|   NetBIOS_Computer_Name: MANUEL-KATANA-17-B12VGK
|   DNS_Domain_Name: MANUEL-KATANA-17-B12VGK
|   DNS_Computer_Name: MANUEL-KATANA-17-B12VGK
|   Product_Version: 10.0.22631
|_  System_Time: 2026-09-04T13:14:52+00:00

Host script results:
|_clock-skew: mean: -18s, deviation: 0s, median: -18s

Nmap scan report for 10.0.2.15
Host is up (0.00028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.0.2.15
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0               0 Mar 26  2018 ftp_test
22/tcp open  ssh     OpenSSH 10.0 (protocol 2.0)
Service Info: Host: Welcome

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (2 hosts up) scanned in 75.37 seconds


a. Apri un browser web e naviga su scanme.nmap.org. Leggi il messaggio pubblicato. Qual è lo scopo di questo sito?

Lo scopo di scanme.nmap.org è fornire una risorsa autorizzata e sicura messa a disposizione dal progetto Nmap per consentire agli utenti di testare e imparare a usare lo scanner di rete Nmap senza effettuare scansioni non autorizzate su sistemi terzi.

In sintesi, il messaggio pubblicato sul sito specifica che:

- Apprendimento e Test: È stato creato per permettere di provare Nmap, testare le sue opzioni e verificare che l'installazione funzioni correttamente.
- Uso Consentito: Gli utenti sono autorizzati a effettuare scansioni verso questo dominio con Nmap.
- Limiti d'Uso: Richiede di non sovraccaricare il server (evitando attacchi DoS o scansioni troppo aggressive/ripetute a frequenza elevata) e di non tentare di violare la sicurezza del sistema (es. tentativi di exploit, attacchi brute-force o modifiche non autorizzate al sito).


Quali porte e servizi sono aperti? 

    2/tcp: ssh (OpenSSH 6.6.1p1 Ubuntu)
    80/tcp: http (Apache httpd 2.4.7)
    9929/tcp: nping-echo (Nping echo)
    31337/tcp: tcpwrapped

Quali porte e servizi sono filtrati? 

    135/tcp: msrpc
    593/tcp: http-rpc-epmap

Qual è l'indirizzo IP del server? 

    IPv4: 45.33.32.156
    IPv6: 2600:3c01::f03c:91ff:fe18:bb2f

Qual è il sistema operativo? 

    Linux (distribuzione Ubuntu come indicato dai banner di SSH e Apache, con CPE cpe:/o:linux:linux_kernel).

Domanda di Riflessione 
Nmap è uno strumento potente per l'esplorazione e la gestione della rete. Come può Nmap aiutare con la sicurezza della rete? Come può Nmap essere usato da un attore malevolo come strumento nefasto?

Come Nmap aiuta con la sicurezza della rete (Uso Difensivo / Blue Teaming):
- Audit di Sicurezza: Permette di identificare quali porte e servizi sono esposti inutilmente verso l'esterno, aiutando a ridurre la superficie di attacco.
- Gestione delle Vulnerabilità: Consente di scoprire servizi obsoleti o non aggiornati che contengono falle di sicurezza note.
- Verifica delle Regole del Firewall: Aiuta a confermare se le porte filtrate (o bloccate) corrispondono effettivamente alle policy di sicurezza aziendali.
- Inventario della Rete: Permette di rilevare dispositivi non autorizzati (rogue devices) collegati alla rete.

Come Nmap viene usato da un attore malevolo (Uso Offensivo / Red Teaming):
- Ricognizione (Reconnaissance): È la prima fase di un attacco; l'aggressore usa Nmap per mappare la rete target e trovare macchine attive.
- Individuazione dei Vettori di Attacco: Identifica servizi specifici e le relative versioni esatte per cercare exploit pronti all'uso (es. exploit su CVE note).
- Bypass dei Difese: Utilizza tecniche di scansione avanzate (come la frammentazione dei pacchetti o gli script NSE) per eludere la rilevazione dei sistemi IDS/IPS o del firewall.