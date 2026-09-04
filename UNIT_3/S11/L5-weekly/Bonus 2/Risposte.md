Quali sono i due indirizzi IP coinvolti in questo attacco di SQL injection in base alle informazioni visualizzate?

10.0.2.4
10.0.2.15

Qual è la versione?

Server: Apache/2.4.18 (Ubuntu)

Quale utente ha l'hash della password di 8d3533d75ae2c3966d7e0d4fcc69216b?

Utente: Pablo

Qual è la password in chiaro?

L'hash MD5 8d3533d75ae2c3966d7e0d4fcc69216b corrisponde alla stringa non cifrata letmein.
Password in chiaro: letmein

Domande di Riflessione 
1. Qual è il rischio che le piattaforme utilizzino il linguaggio SQL? I siti web sono comunemente basati su database e utilizzano il linguaggio SQL. La gravità di un attacco di SQL injection dipende dall'aggressore. 

Il rischio principale legato all'uso del linguaggio SQL non risiede nel linguaggio in sé, ma nel modo in cui la piattaforma gestisce l'input inviato dall'utente. Se un'applicazione web concatena direttamente le stringhe inserite dagli utenti nelle query SQL senza prima pulirle o validarle, si crea una vulnerabilità di SQL Injection (SQLi).

La gravità di un attacco SQLi dipende dagli obiettivi e dalle capacità dell'aggressore, ma può portare a conseguenze critiche:
    Perdita di riservatezza: L'attaccante può leggere dati sensibili memorizzati nel database (credenziali, dati personali, carte di credito, segreti commerciali).
    Compromissione dell'integrità: L'aggressore può modificare, inserire o eliminare dati, fino a cancellare intere tabelle del database.
    Perdita di disponibilità: Possibilità di causare un Denial of Service (DoS) sovraccaricando il database con query complesse o dannose.
    Esecuzione di comandi da remoto (RCE): In determinati contesti (e con privilegi di database elevati), l'attaccante può eseguire comandi sul sistema operativo del server sottostante, compromettendo l'intera infrastruttura.

2. Naviga in internet ed esegui una ricerca per “prevenire attacchi di SQL injectionˮ. Quali sono 2 metodi o passaggi che possono essere adottati per prevenire gli attacchi di SQL injection?

Uso di Query Parametrizzate (Prepared Statements): È la difesa principale e più efficace. Consiste nel separare il codice SQL dai dati inseriti dall'utente. Utilizzando i prepared statements (supportati da quasi tutti i linguaggi di programmazione e ORM), l'interprete SQL tratta l'input dell'utente strettamente come un valore letterale (dato) e mai come codice eseguibile, rendendo impossibile l'alterazione della struttura della query.

Principio del Minimo Privilegio (Least Privilege): Consiste nel configurare l'account di database utilizzato dall'applicazione web limitandone le autorizzazioni allo stretto indispensabile (es. concedere solo permessi di SELECT, INSERT, UPDATE ed evitare account con privilegi di amministratore come root o sa). In questo modo, anche se un attaccante riuscisse a individuare una SQLi, i danni che potrebbe arrecare all'intero sistema verrebbero notevolmente circoscritti.