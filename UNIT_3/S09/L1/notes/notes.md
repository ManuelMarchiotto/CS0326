Analisi Malware Wannacry

1. Identificazione del Campione

    Nome File: WannaCry.exe
    Hash SHA-256: be22645c61949ad6a077373a7d6cd85e3fae44315632f161adc4c99d5a8e6844
    Dimensione: 224 KB (229.376 bytes).
    Tipo di File: Eseguibile Windows a 32-bit (PE32) con interfaccia GUI.

2. Le "Red Flags" (Bandiere Rosse) evidenti dagli screenshot

    VirusTotal (60/66): Questo è il dato più importante. Ben 60 motori antivirus su 66 rilevano questo file come dannoso.
    Classificazione Uniforme: Quasi tutti i vendor lo etichettano come "Trojan.Ransom.WannaCryptor", "WannaCry", "Ransomware" o "Win32/Trojan-gen". Non ci sono dubbi sul fatto che sia un ransomware.
    Pestudio (Rilevazioni):
        score: 60/66 (allineato con VirusTotal).
        Flag rosse sulle Import: Pestudio ha marcato con una 'x' rossa funzioni critiche come VirtualAlloc, VirtualProtect, CreateDirectoryA, WriteFile e CryptDecrypt. Queste sono tipiche di malware che devono decifrare file e scriverne di nuovi sul disco.
        Risorsa Sospetta: Nella sezione "resources" (Image 7), viene identificata una risorsa di tipo PKZIP con la firma "PKZIP-Self Extractor". Questo è un fortissimo indicatore che il file eseguibile contiene al suo interno un altro file zip criptato o un payload aggiuntivo che verrà estratto a runtime.

3. Analisi Tecnica (Dai dettagli)
    Packer/Compilatore: Gli screenshot indicano "Microsoft Linker 6.0" e "Visual Studio 6.0". Anche se questo è un vecchio compilatore (usato ancora oggi), combinato con l'entropia alta di alcune sezioni e la risorsa zip, suggerisce che il malware potrebbe essere impaccato o offuscato (c'è un alto tasso di entropia nella sezione .rsrc - 7,993).

    Comportamento (dai tags di VirusTotal): La dashboard di VirusTotal mostra dei tags di comportamento:
        persistence
        long-sleeps (spesso usato per eludere le sandbox)
        calls-wmi, checks-user-input, checks-cpu-name
        direct-cpu-clock-access, detect-debug-environment (tipiche tecniche anti-debug).
    PE Header: subsystem: GUI e entry-point: 0x00006F9A. L'entry point punta alla sezione .text, il che è normale per i file non caricati con loader strani, ma la presenza di "dvdplay placeholder Application" nella descrizione potrebbe essere un falso positivo o un tentativo di camuffamento.

💡 Cosa fare con queste informazioni?

ATTENZIONE: Questo file è un malware estremamente pericoloso (Ransomware WannaCry).

    NON ESECUTARLO MAI su un computer a cui tieni o su una rete aziendale. WannaCry è noto per sfruttare la vulnerabilità EternalBlue (MS17-010) e diffondersi rapidamente in rete.
    Isolamento: Se hai questo file su una macchina virtuale per analisi (come "FlareVM" indicato nel percorso delle immagini), assicurati che la VM non abbia accesso alla rete LAN del tuo computer fisico, altrimenti potrebbe provare a infettare altri pc.
    Conservazione: Conserva una copia del file in un archivio zip con password (es: infected) per eventuali future analisi, ma tieni il file lontano dalla cartella dei download.
    Aggiornamenti: Ricorda che WannaCry ha colpito duramente nel 2017. Se hai intenzione di analizzarlo in una VM (sandbox), assicurati di avere tutte le patch di Windows aggiornate (specialmente quelle per SMBv1), altrimenti il malware potrebbe infettare la VM stessa attraverso la rete virtuale.