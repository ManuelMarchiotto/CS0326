Lezione del Giorno (potete aiutarvi con ChatGPT 

Argomento: Sfruttamento di una vulnerabilità di File Upload sulla DVWA per l'inserimento di una shell in PHP. Obiettivi: 
1. Configurazione del Laboratorio: 
    - Configurate il vostro ambiente virtuale in modo che la macchina Metasploitable sia raggiungibile dalla macchina Kali Linux. 
    - Assicuratevi che ci sia comunicazione bidirezionale tra le due macchine.
2. Esercizio Pratico: 
    - Sfruttate la vulnerabilità di file upload presente sulla DVWA Damn Vulnerable Web Application) per ottenere il controllo remoto della macchina bersaglio. 
    - Caricate una semplice shell in PHP attraverso l'interfaccia di upload della DVWA. 
    - Utilizzate la shell per eseguire comandi da remoto sulla macchina Metasploitable.
3. Monitoraggio con BurpSuite: 
    - Intercettate e analizzate ogni richiesta HTTP/HTTPS verso la DVWA utilizzando BurpSuite. 
    - Familiarizzate con gli strumenti e le tecniche utilizzate dagli Hacker Etici per monitorare e analizzare il traffico web.

Lezione del Giorno 

Traccia dell'Esercizio:

1. Preparazione dell'Ambiente: Esercizio Traccia 
    - Configurate la macchina virtuale Metasploitable. 
    - Configurate la macchina virtuale Kali Linux.
    - Verificate la connessione tra le due macchine con un semplice ping.
2. Caricamento della Shell PHP: 
    - Accedete alla DVWA sulla macchina Metasploitable tramite il browser della Kali Linux. 
    - Navigare alla sezione File Upload della DVWA. 
    - Create una semplice shell PHP (ad esempio, shell.php) e caricatela attraverso il modulo di upload. 
    - Verificate che il file sia stato caricato con successo.
3. Esecuzione della Shell PHP:
    - Accedete alla shell caricata tramite il browser.
    - Utilizzate la shell per eseguire comandi da remoto sulla macchina Metasploitable.
4. Intercettazione e Analisi con BurpSuite: 
    - Avviate BurpSuite e configurate il browser per utilizzare Burp come proxy. 
    - Intercettate le richieste HTTP/HTTPS effettuate durante il processo di upload e di esecuzione della shell. 
    - Analizzate le richieste e le risposte per comprendere il funzionamento e individuare eventuali vulnerabilità.

Suggerimento 1: 
Esercizio Traccia Accedete alla DVWA dalla macchina Kali via browser, vi consigliamo di mantenere sempre aperta una sessione di BurpSuite per intercettare ogni richiesta e analizzare il contenuto.
Prima di iniziare configurate il «security level» della DVWA a «LOW» dalla scheda DVWA Security. Successivamente spostatevi sulla scheda Upload per mettere in pratica il vostro exploit.

Suggerimento 2: 
A destra un esempio di codice minimale della shell da caricare. Una volta caricata la shell, essa accetta un parametro tramite richiesta GET nel campo cmd
Potete trovare sul web shell molto più sofisticate, con interfaccia grafica e funzioni avanzate. Lo studente che ha completato lʼesercizio (recuperate le evidenze dellʼexploit) può testare il caricamento di una shell avanzata.