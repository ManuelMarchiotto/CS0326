Traccia: 

Esercizio Threat Intelligence & IOC Durante la lezione teorica, abbiamo visto la Threat Intelligence e gli indicatori di compromissione. 
Abbiamo visto che gli IOC sono evidenze o eventi di un attacco in corso, oppure già avvenuto. 

Per lʼesercizio pratico di oggi, trovate in allegato una cattura di rete effettuata con Wireshark. Analizzate la cattura attentamente e rispondere ai seguenti quesiti: 

- Identificare ed analizzare eventuali IOC, ovvero evidenze di attacchi in corso ● In base agli IOC trovati, fate delle ipotesi sui potenziali vettori di attacco utilizzati 
- Consigliate unʼazione per ridurre gli impatti dellʼattacco attuale ed eventualmente un simile attacco futuro

Traccia: 

Per analizzare la cattura, spostate il file sulla vostra Kali Linux, e fate doppio-click, vi aprirà la cattura direttamente con Wireshark, dopo aver configurato i permessi per lʼutente Kali.

Potete spostare il file sulla vostra Kali creando una cartella condivisa tra il vostro host e la Kali come la figura a destra. 

Vi basterà creare la cartella sul vostro sistema operativo, e configurare la cartella sulla macchina virtuale, specificando il percorso della cartella sul vostro Host ed il nome della cartella. Configurate la cartella con le opzioni in figura.

Da Kali potete accedere alla cartella (ed ai file in essa contenuti) navigando il file system alla directory /media come da figura seguente. Come vedete il nostro file è nella cartella condivisa. Da qui possiamo spostare il file sul desktop con il comando «mv» specificando il nome del file ed il path di destinazione, come visto nelle lezioni sul file system di Linux (il comando che abbiamo usato noi è nella figura a destra). Successivamente assicuratevi che lʼutente Kali possa aprire il file assegnando i permessi necessari - riferimento figura in a destra. A questo punto fate doppio click per analizzare la cattura.

Qualora doveste avere problemi per spostare il file su Kali, trovate una prima parte della cattura negli screenshot di seguito, sufficienti per completare lʼesercizio.