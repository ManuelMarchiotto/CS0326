Esercizio del Giorno

Argomento: Attacchi DoS (Denial of Service) - Simulazione di un UDP Flood 

Introduzione: 

Gli attacchi di tipo DoS (Denial of Service) mirano a saturare le richieste di determinati servizi, rendendoli così indisponibili e causando significativi impatti sul business delle aziende. 

Obiettivo dell'Esercizio: 

Scrivere un programma in Python che simuli un UDP flood, ovvero l'invio massivo di richieste UDP verso una macchina target che è in ascolto su una porta UDP casuale.

Requisiti del Programma: 
1. Input dell'IP Target:
    - Il programma deve richiedere all'utente di inserire l'IP della macchina target. 
2. Input della Porta Target: 
    - Il programma deve richiedere all'utente di inserire la porta UDP della macchina target. 
3. Costruzione del Pacchetto: 
    - La grandezza dei pacchetti da inviare deve essere di 1 KB per pacchetto. 
    - Suggerimento: per costruire il pacchetto da 1 KB, potete utilizzare il modulo random per la generazione di byte casuali. 
4. Numero di Pacchetti da Inviare: 
    - Il programma deve chiedere all'utente quanti pacchetti da 1 KB inviare.