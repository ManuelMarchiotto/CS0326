Traccia dell'Esercizio Fase 1 

Scansione del Servizio Telnet Esercizio Traccia Sulla base dellʼesercizio visto in lezione teorica, utilizzare Metasploit per analizzare il servizio Telnet sulla macchina Metasploitable, adoperando il modulo auxiliary/scanner/telnet/telnet_version. 

Extra Fase 2 

Autenticazione e Creazione della Sessione L'obiettivo è ottenere l'accesso a Metasploitable 2 sfruttando le sue credenziali predefinite. Utilizza il modulo auxiliary/scanner/telnet/telnet_login e imposta i seguenti parametri: 

- Il target (RHOSTS). 
- Le credenziali note USERNAME e PASSWORD. 
- L'opzione STOP_ON_SUCCESS su true. Una volta eseguito con successo, il modulo stabilirà una sessione di comando.

Fase 3 

Gestione delle Sessioni Esercizio Traccia Verifica le sessioni attive tramite il comando sessions -l. Per interagire con la sessione appena creata, digita sessions -i <ID_sessione>. Fase 4 Upgrade della Sessione a Meterpreter Metti in background la sessione attiva usando la combinazione di tasti Ctrl+Z e confermando con y alla richiesta. Successivamente, utilizza il modulo post/multi/manage/shell_to_meterpreter per eseguire l'upgrade della sessione a Meterpreter. Controlla le opzioni con il comando show options ed effettua tutte le configurazioni necessarie per completare l'operazione.