La tua prima scansione con YARA

L'obiettivo è creare una regola YARA capace di scovare un file di testo segreto nascosto sul desktop. 

1. Crea il bersaglio 

Apri il Blocco Note (Notepad), scrivi all'interno la frase Connessione_C2_Rilevata e salva il file sul tuo Desktop con il nome config.txt. 

2. Scrivi la regola 

Apri un nuovo file nel Blocco Note e incolla questa regola YARA: 

Snippet di codice 

rule Rileva_Finto_Malware { 
    strings: 
        $stringa_segreta = "Connessione_C2_Rilevata" ascii wide nocase 
    condition: $stringa_segreta 
} 

Salva questo file sul Desktop con il nome mia_regola.yar (assicurati che l'estensione sia .yar e non .yar.txt). 

3. Lancia la caccia 

Apri il Prompt dei comandi (CMD) di Windows e spostati sul Desktop usando il comando: 

cd Desktop 

Ora esegui YARA lanciando la tua regola contro il file config.txt: 

yara64.exe mia_regola.yar config.txt 

Verifica del successo: Se la regola è scritta bene, YARA risponderà sul terminale stampando: Rileva_Finto_Malware config.txt Se il terminale rimane vuoto, 
significa che c'è un errore nella stringa o nel nome del file! 

La Caccia al File (Uso obbligatorio di YARA) 

Il malware è furbo: ha cambiato il suo hash e ha preso il nome di un file di sistema legittimo di Windows (es. si è rinominato taskhost.exe o svchost.exe ed è 
nascosto in mezzo a migliaia di file). Cercarlo a mano o per nome è impossibile.

Tuttavia, un report di Threat Intelligence internazionale ci dice che questo specifico gruppo di hacker (APT) usa sempre: 

- Una stringa di testo specifica offuscata nel codice: AntiAV_Bypass_2026 
- Una sequenza di byte esadecimali specifica usata per fare memory injection: { E2 9A 12 FF } 

La vostra missione: 

1. Create una regola YARA chiamata caccia_malware.yar. 
2. Impostate la regola in modo che faccia scattare l'allarme se trova la stringa di testo (ricordatevi i modificatori ascii wide nocase!) OPPURE la sequenza di byte. 
3. Lanciate la scansione sulla cartella dei file di sistema https://drive.google.com/file/d/1FRizdbYgUpGD0jRNRRgAoVE62RajMg_b/view?usp=sh aring 
4. yara64.exe -r caccia_malware.yar C:\Directory_Sospetta 
5. Segnatevi il nome esatto del file maligno che YARA vi restituirà in output.