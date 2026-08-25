Creeremo una directory chiamata archivio_riservato che conterrà dati sensibili. L'obiettivo è configurare i permessi in modo che solo il proprietario possa 
accedere, leggere, modificare ed eseguire operazioni al suo interno, bloccando qualsiasi accesso a gruppi e altri utenti.

1. Screenshot della Creazione del File o della Directory
Comandi eseguiti:

kali@linux:~$ mkdir archivio_riservato
kali@linux:~$ cd archivio_riservato
kali@linux:~/archivio_riservato$ touch documento_aziendale.txt
kali@linux:~/archivio_riservato$ cd ..

2. Screenshot della Verifica dei Permessi Attuali
Comando eseguito:

kali@linux:~$ ls -ld archivio_riservato
drwxr-xr-x 2 kali kali 4096 ago 25 10:00 archivio_riservato

3. Screenshot della Modifica dei Permessi
Comandi eseguiti:

kali@linux:~$ chmod 700 archivio_riservato
kali@linux:~$ ls -ld archivio_riservato
drwx------ 2 kali kali 4096 ago 25 10:05 archivio_riservato

4. Screenshot del Test dei Permessi
Per dimostrare il funzionamento, testeremo prima il successo con i permessi corretti, poi modificheremo i permessi per dimostrare il blocco in scrittura.
Comandi eseguiti:

# TEST 1: Accesso e scrittura come proprietario (Con permessi 700)
kali@linux:~$ cd archivio_riservato
kali@linux:~/archivio_riservato$ echo "Dati sensibili" > dati.txt
kali@linux:~/archivio_riservato$ ls -l
totale 4
-rw-r--r-- 1 kali kali 15 ago 25 10:10 dati.txt
kali@linux:~/archivio_riservato$ cd ..

# TEST 2: Tentativo di scrittura con permessi limitati (Cambio a 500)
kali@linux:~$ chmod 500 archivio_riservato
kali@linux:~$ ls -ld archivio_riservato
dr-x------ 2 kali kali 4096 ago 25 10:15 archivio_riservato

kali@linux:~$ cd archivio_riservato
kali@linux:~/archivio_riservato$ touch nuovo_file.txt
touch: impossibile fare touch di 'nuovo_file.txt': Permesso negato
kali@linux:~/archivio_riservato$ cd ..

5. Relazione
Titolo: Gestione e Analisi dei Permessi su Directory in Linux
Data: 25 Agosto 2026
Motivazione delle scelte fatte per i permessi
Per questo esercizio ho scelto di configurare i permessi di una directory (archivio_riservato) destinata a contenere file sensibili. 
In Linux, i permessi sulle directory hanno un significato leggermente diverso rispetto ai file:

    Lettura (r): Permette di elencare il contenuto della directory (comando ls).
    Scrittura (w): Permette di creare, cancellare o rinominare file all'interno della directory (comandi touch, rm, mv).
    Esecuzione (x): Permette di "entrare" nella directory (comando cd) e di accedere ai metadati dei file in essa contenuti.

La mia scelta è stata quella di impostare i permessi a 700 (rwx------). 
Ho scelto questa configurazione per garantire la massima riservatezza: il proprietario (utente) ha il controllo totale (può entrare, leggere e creare file), mentre il gruppo e gli "altri" (others) hanno permessi nulli (---). Questo impedisce a qualsiasi altro utente presente nel sistema di anche solo sapere quali file sono contenuti nella cartella.
Analisi dei risultati ottenuti durante i test
Durante la fase di test, ho verificato il comportamento del sistema in due scenari distinti:

    Test con permessi 700 (rwx------): 
    Mi sono spostato all'interno della directory (cd) e ho creato un nuovo file (echo ... > dati.txt). Il sistema ha permesso l'operazione. Questo conferma che il bit di esecuzione (x) permette l'accesso alla cartella e il bit di scrittura (w) consente la creazione di nuovi file al suo interno.
    Test con permessi 500 (r-x------):
    Per testare la restrizione, ho rimosso il permesso di scrittura utilizzando chmod 500. Ho tentato di creare un nuovo file (touch nuovo_file.txt). Il sistema ha restituito l'errore "Permesso negato".

Conclusione:
L'esercizio ha dimostrato con successo come il permesso di scrittura (w) su una directory sia strettamente legato alla capacità di modificarne il contenuto (creare/eliminare file), indipendentemente dai permessi di scrittura del singolo file al suo interno. Inoltre, è stato confermato che l'uso della notazione numerica (es. 700 o 500) tramite chmod è un metodo rapido ed efficace per garantire la sicurezza e l'isolamento dei dati in un ambiente multi-utente Linux.