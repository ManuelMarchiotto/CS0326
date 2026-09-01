
---

# Domande Esercizio

---

## Pacchetto 1

- Qual è il numero di porta TCP di origine? 

    47912

- Come classificheresti la porta di origine?

    La porta di origine 47912 è una Porte Registrate (Registered Ports): 1024 – 49151

- Qual è il numero di porta TCP di destinazione?

    80

- Come classificheresti la porta di destinazione? 

    la porta 80 è una porta nota o Well-Known Ports (0-1023)

- Quale flag è impostato? 

    Flags: 0x002(SYN)

- A quale valore è impostato il numero di sequenza relativo?

    Sequence Number: 4248719285 - fd 3e 4f b5

---

## Pacchetto 2

- Quali sono i valori delle porte di origine e destinazione?

    Source 80
    Destination 47912

- Quali flag sono impostati? 

    Flag: 0x0012 (SYN, ACK)

- A quali valori sono impostati i numeri relativi di sequenza e acknowledgment?

    Acknwledgment Number 4134163049 f6 6a 52 69

---

## Pacchetto 3

- Quale flag è impostato?

    Flags: 0x010 (ACK)

---

## Visualizzare i pacchetti usando tcpdump

- Cosa fa l'opzione -r?

    In tcpdump, l'opzione -r serve a leggere i pacchetti da un file pcap salvato in precedenza, anziché catturare il traffico in tempo reale dalle schede di rete.

---

## Domande di Riflessione

- Ci sono centinaia di filtri disponibili in Wireshark. Una rete di grandi dimensioni potrebbe avere numerosi filtri e molti tipi diversi di traffico. Elenca tre filtri che potrebbero essere utili a un amministratore di rete. 

    http.request.method == "POST" (oppure http.response.code >= 400) Isola il traffico HTTP specifico per individuare l'invio di dati/form web o intercettare errori del server (come i codici 404 o 500).

    dns.flags.response == 0 (o semplicemente dns) Filtra le richieste DNS inviate dai client per diagnosticare problemi di risoluzione dei nomi o rilevare traffico anomalo verso domini sospetti.

    tcp.analysis.flags (oppure ip.addr == X.X.X.X) Mostra problemi di rete come pacchetti ritrasmessi (tcp.analysis.retransmission) o pacchetti persi, utilissimo per individuare colli di bottiglia e degrado della connessione.

- In quali altri modi Wireshark potrebbe essere utilizzato in una rete di produzione?

    Risoluzione di problemi di prestazioni (Troubleshooting): Analisi di latenza, perdita di pacchetti, ritrasmissioni TCP e lentezza nell'apertura delle applicazioni.

    Network Forensics e Incident Response: Analisi post-incidente per capire come un attaccante è entrato, quali dati sono stati esfiltrati o quali malware stanno comunicando verso l'esterno (C2 - Command & Control).

    Audit di Sicurezza e Conformità: Verificare che il traffico sensibile (come credenziali, dati bancari o personali) viaggi cifrato (es. HTTPS, SSH) e non in chiaro (es. HTTP, Telnet, FTP).

    Analisi dei Protocolli di Applicazione: Verificare il comportamento di nuovi software o aggiornamenti in fase di rilascio per assicurarsi che facciano un uso efficiente della banda di rete.

---