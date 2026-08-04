Esercizio di oggi: Setup Laboratorio di Analisi Malware e Identificazione IOC 

Obiettivo: Configurare l'ambiente FlareVM e identificare Indicatori di Compromissione (IOC) tramite analisi del Registro di Windows e triage su VirusTotal. 

Attività: 

- Creare uno snapshot "Clean" della VM pronta all'uso 
- Avviare lo script malwareRepo.ps1 della Desktop della FlareVM 

Bonus Extra: 

- Simulare la creazione di una chiave di persistenza manuale in HKCU Run con regedit e verificarne l'effetto al riavvio 
- Scompattate dei malware a scelte nella cartella malware 
- Una volta scompattati calcolare lʼhash dei file premendo il tasto destro su di essi e usando la funzione di hash.
- Cercare su VirusTotal 3 hash e analizzare i report: detection ratio, tab Behavior e Relations ○ Compilare una tabella IOC con hash, domini C2 e chiavi di registro trovate nei report VirusTotal 
- Analizzare con un LLM i risultati della ricerca e valutare la completezza della risposta AI