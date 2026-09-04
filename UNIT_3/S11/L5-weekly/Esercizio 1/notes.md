Quali sono gli output del comando dir?(screen 1)

- CMD: (prompt dei comandi) mi da 15 directory trovate
- PowerShell mi da lo stesso risultato del cmd
- PowerShell Amministratore da moltissimmi risultati, molte anche dll

Comandi:

Risultato comando ping (screen 2)

tutti e 3 danno lo stesso identico risutlato 

Risultato ipconfig (screen 3)

il cmd nn riconosce il comando mentre la powershell si e mi da come output la configurazione della scheda di rete visto che la vm ne ha una sola dandomi un po tutte le sue specifiche come:
- suffisso DNS
- Indirizzo IPv6
- Indirizzo IPv6 temporaneo
- Indirizzo IPv6 locale
- Indirizzo IPv4
- Subnet mask
- Gsateway predefinito


Qual è il comando PowerShell per dir? (screen 4)

Get-ChildItem

Qual è il gateway IPv4? (screen 5)

10.0.2.2

Quali informazioni puoi ottenere dalla scheda Dettagli e dalla finestra propieta per il PID selezionato? (screen 6 - 7)

nella pagina dettagli posso vedere il nome del processo, il numero di PID, lo stato , il nome dell'utente, la memoria che utilizza, la CPU e se è virtualizzabile il processo

mentre per i dettagli possiamo vedere nelle varie pagine le info generale come il dove si trova le dimansioni la data di creazione di 
modifica e di ultimo accesso, poi posso vedere la firma digitale le sicurezze che ha e le sue regole, poi qualche dettaglio in piu e c'è 
il controllo di versione.

Cosa succede ai file nel Cestino? (screen 8-9)

vengono cancellati in maniera definitiva