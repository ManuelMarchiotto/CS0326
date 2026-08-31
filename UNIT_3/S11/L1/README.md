Esplorazione di Processi, Thread, Handle e Registro di Windows 

VM
CyberOps Security Onion
CyberOps Workstation

Obiettivi

In questo laboratorio, esplorerai i processi, i thread e gli handle utilizzando Process Explorer della Suite SysInternals. 
Utilizzerai anche il Registro di Windows per modificare un'impostazione.

● Parte 1: Esplorazione dei Processi 
● Parte 2: Esplorazione di Thread e Handle 
● Parte 3: Esplorazione del Registro di Windows

Risorse Richieste

● 1 PC Windows con accesso a internet

Parte 1: Esplorazione dei Processi

In questa parte, esplorerai i processi. I processi sono programmi o applicazioni in esecuzione. Esplorerai i processi 
utilizzando Process Explorer nella Suite SysInternals di Windows. Avvierai e osserverai anche un nuovo processo.

Passo 1: Scaricare Windows SysInternals Suite.

● Navigare al seguente link per scaricare Windows SysInternals Suite: https://learn.microsoft.com/sysinternals/downloads/sysinternals-suite 
● Una volta completato il download, estrarre i file dalla cartella. 
● Lasciare aperto il browser web per i passaggi successivi.

Passo 2: Esplorare un processo attivo.

a. Navigare alla cartella SysinternalsSuite con tutti i file estratti. 
b. Aprire procexp.exe. Accettare l'Accordo di Licenza di Process Explorer quando richiesto. 
c. Process Explorer mostra un elenco dei processi attualmente attivi. 
d. Per localizzare il processo del browser web, trascinare l'icona Find Windowʼs Process (Trova Processo della Finestra) sulla finestra aperta del browser web. In questo esempio è stato utilizzato Microsoft Edge

e. Il processo di Microsoft Edge può essere terminato in Process Explorer. Fare clic con il pulsante destro del mouse sul processo selezionato e selezionare Kill Process (Termina Processo). Fare clic su OK per continuare.

Passo 3: Avviare un altro processo. 

a. Aprire un Prompt dei Comandi. (Start > cercare Prompt dei Comandi > selezionare Prompt dei Comandi) 

b. Trascinare l'icona Find Windowʼs Process sulla finestra del Prompt dei Comandi e localizzare il processo evidenziato del Prompt dei Comandi in Process Explorer. 

c. Il processo per il Prompt dei Comandi è cmd.exe. Il suo processo genitore (parent process) è explorer.exe. Il cmd.exe ha un processo figlio (child process), conhost.exe. 

d. Navigare alla finestra del Prompt dei Comandi. Avviare un ping al prompt e osservare i cambiamenti sotto il processo cmd.exe. Cosa è successo durante il processo ping?

e. Mentre si esamina l'elenco dei processi attivi, si scopre che il processo figlio conhost.exe potrebbe essere sospetto. Per verificare la presenza di contenuti malevoli, fare clic con il pulsante destro su conhost.exe e selezionare Check VirusTotal. Quando richiesto, fare clic su Yes per accettare i Termini di Servizio di VirusTotal. Quindi fare clic su OK per la richiesta successiva. 

f. Espandere la finestra di Process Explorer o scorrere verso destra finché non si vede la colonna VirusTotal. Fare clic sul link sotto la colonna VirusTotal. Il browser web predefinito si apre con i risultati relativi al contenuto malevolo di conhost.exe. 

g. Fare clic con il pulsante destro sul processo cmd.exe e selezionare Kill Process. Cosa è successo al processo figlio conhost.exe?

Parte 2: Esplorazione di Thread e Handle

In questa parte, esplorerai i thread e gli handle. I processi hanno uno o più thread. Un thread è un'unità di esecuzione all'interno di un processo. Un handle è un riferimento astratto a blocchi di memoria o oggetti gestiti da un sistema operativo. Utilizzerai Process Explorer (procexp.exe) nella Suite SysInternals di Windows per esplorare i thread e gli handle

Passo 1: Esplorare i thread.

a. Aprire un prompt dei comandi.

b. Nella finestra di Process Explorer, fare clic con il pulsante destro su conhost.exe e selezionare Properties… (Proprietà). Fare clic sulla scheda Threads per visualizzare i thread attivi per il processo conhost.exe. Fare clic su OK per continuare se viene visualizzata una finestra di dialogo di avviso. 

c. Esaminare i dettagli del thread. 

Che tipo di informazioni sono disponibili nella finestra Proprietà?

d. Fare clic su OK per continuare. 

Passo 2: Esplorare gli handle. 

a. In Process Explorer, fare clic su View (Visualizza) > selezionare Lower Pane View (Vista Riquadro Inferiore) > Handles per visualizzare gli handle associati al processo conhost.exe. 

Esaminare gli handle. A cosa puntano gli handle? 

b. Chiudere Process Explorer al termine.

Parte 3: Esplorazione del Registro di Windows

Il Registro di Windows è un database gerarchico che memorizza la maggior parte delle impostazioni di configurazione del sistema operativo e dell'ambiente desktop.

a. Per accedere al Registro di Windows, fare clic su Start > Cercare regedit e selezionare Editor del Registro di sistema. Fare clic su Sì quando viene chiesto di consentire a questa app di apportare modifiche

L'Editor del Registro di sistema ha cinque "hive" (rami principali). Questi hive si trovano al livello più alto del registro.

● HKEY_CLASSES_ROOT è in realtà la sottochiave Classes di HKEY_LOCAL_MACHINE\Software\. Memorizza informazioni utilizzate dalle applicazioni registrate come l'associazione delle estensioni dei file, nonché dati relativi a identificatori programmatici (ProgID), Class ID (CLSID) e Interface ID (IID). 
● HKEY_CURRENT_USER contiene le impostazioni e le configurazioni per gli utenti attualmente connessi. 
● HKEY_LOCAL_MACHINE memorizza informazioni di configurazione specifiche del computer locale. 
● HKEY_USERS contiene le impostazioni e le configurazioni per tutti gli utenti sul computer locale. HKEY_CURRENT_USER è una sottochiave di HKEY_USERS. 
● HKEY_CURRENT_CONFIG memorizza le informazioni hardware utilizzate all'avvio dal computer locale.

b. In un passaggio precedente, avevi accettato l'EULA (End User License Agreement - Accordo di Licenza con l'Utente Finale) per Process Explorer.

Navigare alla chiave di registro EulaAccepted per Process Explorer. Fare clic per selezionare Process Explorer in HKEY_CURRENT_USER  Software > Sysinternals > Process Explorer. Scorrere verso il basso per individuare la chiave EulaAccepted. Attualmente, il valore per la chiave di registro EulaAccepted è 0x00000001(1). 

b. In un passaggio precedente, avevi accettato l'EULA (End User License Agreement - Accordo di Licenza con l'Utente Finale) per Process Explorer. Navigare alla chiave di registro EulaAccepted per Process Explorer.

Fare clic per selezionare Process Explorer in HKEY_CURRENT_USER  Software > Sysinternals > Process Explorer. Scorrere verso il basso per individuare la chiave EulaAccepted. Attualmente, il valore per la chiave di registro EulaAccepted è 0x00000001(1).

c. Fare doppio clic sulla chiave di registro EulaAccepted. Attualmente il dato del valore è impostato su 1. Il valore 1 indica che l'EULA è stato accettato dall'utente.

d. Cambiare il valore 1 in 0 per il dato Valore (Value data). Il valore 0 indica che l'EULA non è stato accettato. Fare clic su OK per continuare.

Qual è il valore per questa chiave di registro nella colonna Dati (Data)?

e. Aprire Process Explorer. Navigare alla cartella in cui è stato scaricato SysInternals. Aprire la cartella SysInternalsSuite > Aprire procexp.exe.

Quando apri Process Explorer, cosa vedi?