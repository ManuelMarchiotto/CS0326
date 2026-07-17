Esercizio del Giorno

Si ricordi che la configurazione dei servizi costituisce essa stessa una parte integrante dell'esercizio.

L’esercizio di oggi ha un duplice scopo:

- Fare pratica con Hydra per craccare l’autenticazione dei servizi di rete. 
- Consolidare le conoscenze dei servizi stessi tramite la loro configurazione.

L’esercizio si svilupperà in due fasi:

- Una prima fase dove insieme vedremo l’abilitazione di un servizio SSH e la relativa sessione di cracking dell’autenticazione con Hydra. 
- Una seconda fase dove sarete liberi di configurare e craccare un qualsiasi servizio di rete tra quelli disponibili, ad esempio ftp, rdp, telnet, autenticazione HTTP.

Esercizio guidato: configurazione e cracking SSH

- Creiamo un nuovo utente su Kali Linux, con il comando «adduser». 
- Chiamiamo l’utente test_user, e configuriamo una password iniziale testpass 
- Attiviamo il servizio ssh con il comando sudo service ssh start 
- Il file di configurazione del demone sshd lo troviamo al path /etc/ssh/sshd_config, qui possiamo abilitare l’accesso all’utente root in ssh (di default 
per ragioni di sicurezza è vietato), cambiare la porta e l’indirizzo di binding del servizio e modificare molte altre opzioni. Ricordate che per tutti i servizi c’è un file di configurazione dove potete modificare le impostazioni del servizio stesso. Ai fini dell’esercizio lasciamo il file così e 
procediamo.

Esercizio guidato: configurazione e cracking SSH

- Testiamo la connessione in SSH dell’utente appena creato sul sistema, eseguendo il comando seguente: ssh test_user@ip_kali, 
sostituite Ip_kali con l’ip della vostra macchina. 
- Se le credenziali inserite sono corrette, dovreste ricevere il prompt dei comandi dell’utente test_user sulla nostra Kali.

Esercizio guidato: configurazione e cracking SSH

- A questo punto, avendo verificato l’accesso, non ci resta che configurare Hydra per una sessione di cracking. Ovviamente in questo esercizio conosciamo già l’utente e la password per accedere, ma soffermiamoci sulla sintassi di Hydra per ora, successivamente potete cambiare e scegliere username e password random per testare il sistema in «blackbox».

- Possiamo attaccare l’autenticazione SSH con Hydra con il seguente comando, dove –l, e –p minuscole si usano se vogliamo utilizzare un singolo username ed una singola password. Ipotizziamo di non conoscere username e password ed utilizziamo invece delle liste per l’attacco a dizionario. Useremo gli switch–L, -P (notate che sono entrambe in maiuscolo).

hydra–l username –p password IP–t 4 ssh

Esercizio guidato: configurazione e cracking SSH

- Il nostro comando sarà quindi:

hydra –L username_list –P password_list IP_KALI–t 4 ssh

- Dove sostituiremo username_list e password_list con le wordlist scaricate e IP kali con il nostro IP. Esercizio Traccia 
- Se volete scaricare una collezione di username e password, installate seclists. Seclists contiene elenchi di username e password piuttosto vasti.
Utilizzate il comando «sudo apt install seclists».

Esercizio guidato: configurazione e cracking SSH

Potete aggiungere lo switch–V, in modo tale da controllare «live» i tentativi di cracking di Hydra.

Esercizio fase 2 – suggerimento:

Per la seconda parte dell’esercizio, scegliete un servizio da configurare, e poi provate a craccare l’autenticazione con Hydra. 

- Se optate per il servizio ftp, che consigliamo, potete semplicemente installarlo con il seguente comando: sudo apt install vsftpd 
- E poi avviare il servizio con: sudo service vsftpd start

Opzionale

Sarà evidente che recuperare le credenziali,con seclist, richiederà molto tempo. È necessario trovare una soluzione.