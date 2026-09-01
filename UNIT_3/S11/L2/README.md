Usare Wireshark per Osservare l'Handshake a 3 Vie TCP

Obiettivi

● Parte 1: Preparare gli Host per Catturare il Traffico 
● Parte 2: Analizzare i Pacchetti usando Wireshark 
● Parte 3: Visualizzare i Pacchetti usando tcpdump

Contesto / Scenario

In questo laboratorio, userai Wireshark per catturare ed esaminare i pacchetti generati tra il browser del PC che utilizza il protocollo HTTP (HyperText Transfer Protocol) e un server web, come www.google.com. Quando un'applicazione, come HTTP o FTP (File Transfer Protocol), si avvia per la prima volta su un host, TCP utilizza 
l'handshake a tre vie per stabilire una sessione TCP affidabile tra i due host. Ad esempio, quando un PC utilizza un browser web per navigare in internet, viene 
avviato un handshake a tre vie e viene stabilita una sessione tra l'host del PC e il server web. Un PC può avere più sessioni TCP attive simultaneamente con vari siti web.

Risorse Richieste: Macchina virtuale CyberOps Workstation

ISTRUZIONI

Parte 1: Preparare gli Host per Catturare il Traffico

a. Avviare la VM CyberOps. Accedere con nome utente analyst e password cyberops.

b. Avviare Mininet.

[analyst@secOps ~]$ sudo lab.support.files/scripts/cyberops_topo.py

c. Avviare gli host H1 e H4 in Mininet.

*** Starting CLI:    
    mininet> xterm H1    
    mininet> xterm H4

d. Avviare il server web su H4.

[root@secOps analyst]# /home/analyst/lab.support.files/scripts/reg_server_start.sh

e. Per motivi di sicurezza, non è possibile eseguire Firefox dall'account utente root. Sull'host H1, usare il comando su (switch user) per passare dall'utente root all'account utente analyst:

[root@secOps analyst]# su analyst

f. Avviare il browser web su H1. Ci vorrà qualche momento.

[analyst@secOps ~]$ firefox &

g. Dopo l'apertura della finestra di Firefox, avviare una sessione tcpdump nel terminale Node: H1 e inviare l'output a un file chiamato capture.pcap. Con l'opzione -v, è possibile osservare l'avanzamento. Questa cattura si fermerà dopo aver catturato 50 pacchetti, poiché è configurata con l'opzione -c 50.

[analyst@secOps ~]$ sudo tcpdump -i H1-eth0 -v -c 50 -w /home/analyst/capture.pcap

h. Dopo l'avvio di tcpdump, navigare rapidamente a 172.16.0.40 nel browser web Firefox.

Parte 2: Analizzare i Pacchetti usando Wireshark

Passo 1: Applicare un filtro alla cattura salvata.

a. Premere INVIO per vedere il prompt. Avviare Wireshark su Node: H1. Fare clic su OK quando viene richiesto l'avviso riguardante l'esecuzione di Wireshark come superutente.

[analyst@secOps ~]$ wireshark-gtk &

b. In Wireshark, fare clic su File > Open. Selezionare il file pcap salvato situato in /home/analyst/capture.pcap.

c. Applicare un filtro tcp alla cattura. In questo esempio, i primi 3 frame rappresentano il traffico di interesse.

Passo 2: Esaminare le informazioni all'interno dei pacchetti, inclusi indirizzi IP, numeri di porta TCP e flag di controllo TCP.

a. In questo esempio, il frame 1 è l'inizio dell'handshake a tre vie tra il PC e il server su H4. Nel riquadro dell'elenco dei pacchetti (sezione superiore della finestra principale), selezionare il primo pacchetto, se necessario.

b. Fare clic sulla freccia a sinistra del Transmission Control Protocol nel riquadro dei dettagli del pacchetto per espanderlo ed esaminare le informazioni TCP. Localizzare le informazioni sulla porta di origine e destinazione.

c. Fare clic sulla freccia a sinistra dei Flags. Un valore di 1 significa che il flag è impostato. Localizzare il flag impostato in questo pacchetto.

Nota: Potrebbe essere necessario regolare le dimensioni delle finestre superiore e centrale all'interno di Wireshark per visualizzare le informazioni necessarie.

● Qual è il numero di porta TCP di origine? 
● Come classificheresti la porta di origine?
● Qual è il numero di porta TCP di destinazione? 
● Come classificheresti la porta di destinazione? 
● Quale flag è impostato? 
● A quale valore è impostato il numero di sequenza relativo?

d. Selezionare il pacchetto successivo nell'handshake a tre vie. In questo esempio, è il frame 2. Questa è la risposta del server web alla richiesta iniziale di avviare una sessione.

● Quali sono i valori delle porte di origine e destinazione? 
● Quali flag sono impostati? 
● A quali valori sono impostati i numeri relativi di sequenza e acknowledgment?

e. Infine, selezionare il terzo pacchetto nell'handshake a tre vie.

Esaminare il terzo e ultimo pacchetto dell'handshake.

Quale flag è impostato?

I numeri relativi di sequenza e acknowledgment sono impostati a 1 come punto di partenza. La connessione TCP è stabilita e la comunicazione tra il computer di origine e il server web può iniziare.

Parte 3: Visualizzare i pacchetti usando tcpdump

È anche possibile visualizzare il file pcap e filtrare per le informazioni desiderate.

a. Aprire una nuova finestra di terminale, inserire man tcpdump. Nota: Potrebbe essere necessario premere INVIO per vedere il prompt.

Utilizzando le pagine manuale (man pages) disponibili con il sistema operativo Linux, è possibile leggere o cercare tra le pagine manuale le opzioni per selezionare le informazioni desiderate dal file pcap.

Per cercare nelle pagine man, è possibile usare / (ricerca in avanti) o ? (ricerca indietro) per trovare termini specifici, n per passare alla corrispondenza successiva e q per uscire. Ad esempio, per cercare informazioni sull'opzione -r, digitare /-r. Digitare n per passare alla corrispondenza successiva.

Cosa fa l'opzione -r?

b. Nello stesso terminale, aprire il file di cattura usando il seguente comando per visualizzare i primi 3 pacchetti TCP catturati:

Per visualizzare l'handshake a 3 vie, potrebbe essere necessario aumentare il numero di righe dopo l'opzione -c.

c. Navigare al terminale usato per avviare Mininet. Terminare Mininet inserendo quit nella finestra principale del terminale della VM CyberOps.

d. Dopo aver chiuso Mininet, inserire sudo mn -c per pulire i processi avviati da Mininet. Inserire la password cyberops quando richiesto.   

Domande di Riflessione

1. Ci sono centinaia di filtri disponibili in Wireshark. Una rete di grandi dimensioni potrebbe avere numerosi filtri e molti tipi diversi di traffico. Elenca tre filtri che potrebbero essere utili a un amministratore di rete. 

2. In quali altri modi Wireshark potrebbe essere utilizzato in una rete di produzione?