# Analisi Statica di un Campione Malevolo Mascherato da Applicazione di Sistema

## Relazione di Laboratorio — Attività di Ethical Hacking e Malware Analysis

**Corso:** Cybersecurity / Penetration Testing
**Ambiente di lavoro:** Macchina virtuale FlareVM (ambiente isolato e controllato)
**Campione analizzato:** `notepad-classico.exe`
**Tipologia di attività:** Analisi statica di malware a scopo didattico

---

## 1. Introduzione

Nell'ambito delle attività didattiche relative alla disciplina della sicurezza informatica, è stata condotta un'esercitazione pratica di *malware analysis* avente ad oggetto un file eseguibile denominato `notepad-classico.exe`, reperito all'interno della cartella "Malware" della macchina virtuale FlareVM. FlareVM costituisce una distribuzione Windows specificamente configurata per l'analisi di codice malevolo, dotata di un insieme completo di strumenti di reverse engineering, analisi statica e dinamica, ed è stata impiegata in qualità di ambiente isolato, privo di connessione a reti di produzione, al fine di prevenire qualsiasi rischio di propagazione accidentale del campione in esame.

Si precisa, in via preliminare e con carattere di assoluta rilevanza, che l'intera attività descritta nella presente relazione è stata svolta esclusivamente a fini didattici e di formazione accademica, nel rispetto dei principi dell'*ethical hacking*, in un contesto di laboratorio pienamente controllato e segregato dalla rete istituzionale. In nessuna fase dell'esercitazione il campione è stato eseguito al di fuori dell'ambiente sandbox, né si è proceduto ad alcuna azione riconducibile a un attacco reale contro sistemi terzi.

## 2. Obiettivi dell'Attività

Coerentemente con quanto stabilito dalla consegna dell'esercizio, l'attività si è posta i seguenti obiettivi specifici:

- Identificare, mediante analisi statica, le librerie (DLL) importate dinamicamente dal campione `notepad-classico.exe`, fornendo per ciascuna di esse una descrizione tecnica elaborata con il supporto di strumenti di intelligenza artificiale;
- Individuare le sezioni che compongono la struttura del file eseguibile (formato PE — *Portable Executable*), fornendo per ciascuna una descrizione tecnica delle relative funzioni e proprietà;
- Formulare, quale approfondimento facoltativo, una considerazione conclusiva sulla natura e sulla pericolosità del campione, sulla base delle evidenze raccolte ed elaborate.

## 3. Metodologia e Ambiente di Analisi

La metodologia adottata ha seguito un approccio incrementale, tipico delle attività di *triage* iniziale di un campione sospetto, articolato secondo le seguenti fasi:

1. **Isolamento dell'ambiente di lavoro**, mediante l'impiego di una macchina virtuale dedicata (FlareVM) priva di accesso a reti locali o aziendali;
2. **Raccolta di metadati e valori di hash** del file, propedeutica a qualunque ulteriore fase di indagine;
3. **Analisi statica automatizzata** tramite lo strumento *Detect It Easy*, finalizzata all'identificazione del tipo di file, del compilatore e di eventuali tecniche di offuscamento;
4. **Verifica di reputazione** tramite la piattaforma collaborativa *VirusTotal*, per la raccolta di riscontri incrociati da parte di molteplici motori antivirus e regole di rilevamento comportamentale (YARA);
5. **Analisi statica approfondita** tramite lo strumento *PEStudio*, per l'esame dettagliato delle librerie importate e delle sezioni del file;
6. **Interpretazione e sintesi dei risultati** con il supporto di un modello linguistico di intelligenza artificiale, impiegato quale strumento di ausilio alla comprensione tecnica dei dati raccolti.

Si evidenzia come, coerentemente con le indicazioni della consegna, il campione non sia mai stato eseguito in nessuna fase dell'attività: l'intera analisi ha carattere esclusivamente statico, ovvero condotta sul file "a riposo", senza attivazione del codice in esso contenuto.

A ulteriore garanzia della sicurezza dell'ambiente di laboratorio, si segnala come la macchina virtuale fosse dotata di uno script di segmentazione di rete (`start_router.sh`), riportato in Figura 1, predisposto per impedire, tramite regole del firewall `iptables`, qualsiasi comunicazione in uscita verso intervalli di indirizzi IP privati (`192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`), con conseguente registrazione (*logging*) di ogni tentativo di connessione verso tali reti. Tale accorgimento, sebbene non direttamente richiesto dalla consegna, rappresenta una buona prassi metodologica nell'analisi di codice potenzialmente malevolo, in quanto riduce ulteriormente la superficie di rischio in caso di esecuzione accidentale del campione.

**Figura 1** — *Script di isolamento di rete (`start_router.sh`) impiegato per la segmentazione del laboratorio di analisi, con regole `iptables` di blocco e registrazione del traffico diretto verso reti private.*

## 4. Fase 1 — Raccolta delle Informazioni Preliminari

Come primo passo dell'indagine, si è proceduto al calcolo dei valori di hash crittografico del campione, operazione indispensabile ai fini dell'identificazione univoca del file e della successiva interrogazione delle banche dati di intelligence sulle minacce.

**Tabella 1 — Valori identificativi del campione**

| Proprietà | Valore |
|---|---|
| Nome file | `notepad-classico.exe` |
| MD5 | `8a00a5c59ac157754ca575d721bcf960` |
| SHA-1 | `c31e260630d6553e2000f8e5f8dc270c751780d9` |
| SHA-256 | `d2e6c9f9273663f3218bcd7cbfb3b6f599fbce7a4ba986f9bbff77e3603988f2` |
| Dimensione | 289.280 byte (282,50 KiB) |
| Percorso completo | `C:\Users\FlareVM\Downloads\notepad-classico.exe` |
| Data di modifica | 24/07/2025 06:26:46 |
| Data di creazione (nel sistema di analisi) | 04/08/2026 05:09:20 |
| Versione file dichiarata | 5.1.2600.5512 [xpsp.080413-2105] |
| Versione prodotto dichiarata | 5.1.2600.5512 |

**Figura 2** — *Elenco del file oggetto di analisi con relativi valori di hash MD5 e SHA-256, dimensione e marche temporali.*

**Figura 3** — *Finestra delle proprietà estese del file, riportante l'insieme completo dei valori di hash (MD5, SHA-1, CRC32, SHA-256, SHA-384, SHA-512) e i metadati di versione.*

Si osserva, quale prima anomalia rilevata, una significativa discrepanza tra la versione dichiarata dal file (5.1.2600.5512), corrispondente storicamente al componente Blocco Note distribuito con Windows XP Service Pack 3, e le marche temporali di modifica e creazione, riconducibili rispettivamente agli anni 2025 e 2026. Tale incongruenza cronologica costituisce un primo indicatore, ancorché non conclusivo, di una possibile alterazione del file originale a fini di occultamento (tecnica nota in letteratura come *masquerading*, catalogata all'interno del framework MITRE ATT&CK con identificativo T1036).

## 5. Fase 2 — Analisi Statica Automatizzata (Detect It Easy)

Al fine di ottenere una prima caratterizzazione tecnica del file, si è proceduto all'analisi mediante lo strumento *Detect It Easy* (DiE), utilizzato per la determinazione del formato, del compilatore e di eventuali tecniche di compressione o offuscamento del codice.

**Tabella 2 — Risultati dell'analisi con Detect It Easy**

| Parametro | Valore rilevato |
|---|---|
| Tipo di file | PE32 |
| Architettura | I386 (32-bit) |
| Endianness | Little Endian (LE) |
| Tipo applicazione | GUI |
| Sistema operativo dichiarato | Windows 95 |
| Linker | Microsoft Linker (7.10.4035) |
| Compilatore | Microsoft Visual C/C++ (13.10.4035) |
| Linguaggio | C |
| Ambiente di sviluppo | Visual Studio (2003) |
| Indicatore euristico | *(Heur) Packer: Compressed or packed data* — rilevato tramite ripetizione dei nomi delle sezioni e pattern di istruzioni tipico ("pusha...") in corrispondenza dell'*entry point* |

**Figura 4** — *Interfaccia dello strumento Detect It Easy, con evidenza dell'indicatore euristico di possibile compressione o offuscamento del codice (in rosso).*

Il riscontro più rilevante emerso in questa fase è rappresentato dall'indicatore euristico relativo alla probabile presenza di dati compressi o offuscati (*packed data*), motivato dalla ripetizione dei nomi delle sezioni e dalla presenza, in corrispondenza del punto di ingresso del programma, di un pattern di istruzioni assembly (`pusha`) tipicamente associato a routine di *unpacking* o *stub* di decompressione eseguiti in fase di avvio. Tale evidenza risulta coerente con quanto successivamente confermato dall'analisi dell'entropia condotta con PEStudio (cfr. Sezione 9).

## 6. Fase 3 — Analisi di Intelligence Collettiva (VirusTotal)

Il valore di hash SHA-256 calcolato nella Fase 1 è stato sottoposto alla piattaforma *VirusTotal*, servizio di *threat intelligence* che aggrega i responsi di numerosi motori antivirus commerciali, al fine di verificare la reputazione del campione presso la comunità internazionale di sicurezza.

**Figura 5** — *Sintesi del responso di VirusTotal: 58 motori antivirus su 72 hanno classificato il campione come malevolo, con etichetta di minaccia popolare "trojan.rozena/meterpreter".*

Il campione ha ottenuto un tasso di rilevamento pari a **58 rilevamenti su 72 motori antivirus interrogati**, valore che rappresenta un indicatore di elevatissima attendibilità circa la natura malevola del file. La piattaforma ha attribuito al campione l'etichetta di minaccia popolare **`trojan.rozena/meterpreter`**, riconducendolo alla categoria "trojan" e associandolo alle famiglie **Rozena**, **Meterpreter** e **Swrort**.

Dalla scheda di dettaglio tecnico (Figura 6) sono stati inoltre estratti ulteriori identificativi univoci del campione (*vhash*, *authentihash*, *imphash*, *rich PE header hash*, *ssdeep*, *TLSH*), utili ai fini della correlazione con campioni analoghi presenti in altre campagne malevole, nonché la conferma del tipo di file (Win32 EXE) e degli strumenti di compilazione impiegati.

**Figura 6** — *Scheda dei metadati tecnici estesi del campione su VirusTotal, con hash di similarità (imphash, ssdeep, TLSH) utili alla correlazione con campagne malevole affini.*

Di particolare rilievo risulta il contenuto della sezione *Community* della piattaforma (Figura 7), nella quale un analista terzo ha documentato la corrispondenza del campione con una regola YARA denominata **`SUSP_ShellCode_Indicator_Nov22_2`**, appartenente al set di regole *Suspicious2 Indicators* dello scanner **THOR APT** sviluppato da Florian Roth, la cui descrizione ufficiale indica la rilevazione di *shellcode* riconducibile a semplici *reverse shell*. Tale riscontro conferma la presenza, all'interno del file, di codice binario grezzo predisposto per essere eseguito in memoria, elemento tipico delle tecniche di *post-exploitation* impiegate dal framework Metasploit (da cui il payload Meterpreter trae origine).

**Figura 7** — *Commento della community di VirusTotal relativo alla corrispondenza con la regola YARA "SUSP_ShellCode_Indicator_Nov22_2", indicativa della presenza di shellcode riconducibile a reverse shell.*

## 7. Fase 4 — Analisi Statica Approfondita (PEStudio)

Al fine di completare il quadro informativo raccolto, si è proceduto a un'analisi statica di maggior dettaglio mediante lo strumento *PEStudio*, specificamente concepito per l'esame preliminare di file eseguibili sospetti in ottica di *malware assessment*.

**Figura 8** — *Panoramica generale del file in PEStudio: dimensione, entropia complessiva, punto di ingresso, descrizione del file ("Blocco note") e marca temporale del compilatore.*

Dall'analisi generale del file (Figura 8) sono emersi i seguenti elementi di rilievo:

- **Entropia complessiva del file**: 6,273 (su una scala massima di 8), valore compatibile con la presenza di dati parzialmente compressi o cifrati;
- **Descrizione interna del file**: "Blocco note", coerente con il tentativo di mascheramento come applicazione legittima;
- **Nome originale del modulo** (campo *original-file-name*): `NOTEPAD.EXE`, ulteriore conferma dell'intento di impersonare l'applicazione di sistema Blocco Note;
- **Manifest applicativo**: `Microsoft.Windows.Shell.notepad`, elemento anch'esso coerente con la strategia di *masquerading*;
- **Marca temporale di compilazione**: domenica 13 aprile 2008, ore 18:35:51 UTC — dato palesemente incompatibile con le marche temporali di modifica e creazione del file rilevate nella Fase 1, a ulteriore riprova di una probabile manipolazione dei metadati.

## 8. Analisi delle Librerie Importate

L'esame della tabella degli import (Figura 10), condotto tramite PEStudio, ha rilevato un totale di **201 funzioni importate**, di cui **18 espressamente segnalate dallo strumento come potenzialmente sospette**, distribuite su un insieme di **9 librerie** (*Dynamic Link Library*, DLL) di sistema. Le funzioni contrassegnate come sospette sono state analizzate singolarmente, anche con il supporto di un modello di intelligenza artificiale, al fine di comprenderne la finalità tecnica nel contesto specifico del campione in esame.

**Figura 9** — *Tabella completa degli import del file, con evidenza (in rosso) delle 18 funzioni classificate come potenzialmente sospette e delle rispettive librerie di provenienza.*

**Tabella 3 — Librerie importate e relativa descrizione funzionale**

| Libreria | Funzione tipica | Descrizione tecnica (elaborata con supporto AI) |
|---|---|---|
| **ADVAPI32.dll** | Gestione del registro di sistema e servizi Windows | Libreria avanzata delle API di Windows, deputata alla gestione del registro di sistema, dei servizi e delle politiche di sicurezza. Nel campione in esame espone le funzioni `RegCreateKeyW` e `RegSetValueExW`, tipicamente impiegate per la creazione o modifica di chiavi di registro finalizzate all'ottenimento della **persistenza** del malware a ogni riavvio del sistema operativo. |
| **KERNEL32.dll** | Gestione di processi, memoria e file system | Libreria fondamentale del sistema operativo Windows, responsabile della gestione di processi, thread, memoria e file system. Nel campione risultano importate funzioni quali `GetCurrentThreadId`, `GetCurrentProcess`, `GetCurrentProcessId` (utili per l'identificazione del contesto di esecuzione, spesso impiegate in tecniche anti-debug o di iniezione di codice), `FindFirstFileW`, `WriteFile`, `DeleteFileW` (manipolazione del file system) e, soprattutto, `MapViewOfFile` / `UnmapViewOfFile`, funzioni impiegate per la mappatura di regioni di memoria condivisa, tecnica comunemente sfruttata per l'**iniezione di codice** in processi legittimi (*process injection*). |
| **USER32.dll** | Gestione dell'interfaccia utente e degli eventi di sistema | Libreria responsabile della gestione delle finestre, dei messaggi e dell'interfaccia utente grafica. Il campione importa funzioni quali `GetForegroundWindow` e `GetDesktopWindow` (identificazione della finestra attiva, potenzialmente utilizzabile per finalità di sorveglianza dell'attività utente), nonché `SetWinEventHook` e `UnhookWinEvent`, funzioni che consentono l'installazione di *hook* di sistema per l'intercettazione di eventi, tecnica talvolta impiegata per il monitoraggio non autorizzato delle azioni dell'utente. Sono inoltre presenti funzioni di gestione degli appunti di sistema (`OpenClipboard`, `CloseClipboard`, `IsClipboardFormatAvailable`), potenzialmente riconducibili a finalità di esfiltrazione di dati copiati dall'utente. |
| **COMDLG32.dll** | Finestre di dialogo comuni | Libreria che implementa le finestre di dialogo standard di Windows (apertura/salvataggio file, ricerca testo, impostazione stampa e font: `GetOpenFileNameW`, `GetSaveFileNameW`, `FindTextW`, `ReplaceTextW`, `ChooseFontW`, `PrintDlgExW`). L'importazione di tali funzioni è coerente con la componente "di facciata" del programma, ossia l'interfaccia grafica dell'applicazione Blocco Note utilizzata quale copertura per mascherare la reale natura malevola del file. |
| **SHELL32.dll** | Interazione con la shell di Windows | Libreria che espone funzionalità di interazione con la shell del sistema operativo (gestione di icone, drag-and-drop, associazioni file). La funzione `DragFinish`, rilevata tra gli import, è associata alla gestione delle operazioni di trascinamento file, coerente con l'interfaccia grafica dell'applicazione di copertura. |
| **KERNEL32.dll** *(funzioni di persistenza/evasione)* | Manipolazione avanzata della memoria | *(Vedi sopra)* — si segnala in modo specifico la coppia `MapViewOfFile`/`UnmapViewOfFile`, la cui compresenza con l'elevata entropia della sezione `.text` (cfr. Sezione 9) rafforza l'ipotesi di una routine di decompressione o decifratura del payload eseguita in memoria al momento dell'avvio del processo. |

*Nota metodologica: le librerie COMCTL32.dll e ulteriori DLL di sistema risultano presenti nell'elenco completo degli import (9 librerie totali), pur non essendo state riportate singolarmente in tabella in quanto associate a funzioni standard dell'interfaccia grafica non direttamente classificate come sospette dallo strumento di analisi.*

Dall'esame combinato delle librerie e delle funzioni importate emerge un quadro coerente con quello di un contagocce (*dropper*) o di un impianto (*implant*) di post-exploitation: da un lato, la presenza di funzioni legate alla gestione di finestre di dialogo e all'interfaccia grafica assicura al programma un aspetto verosimile di applicazione legittima; dall'altro, la combinazione di funzioni per la scrittura su registro di sistema, la manipolazione di file e, soprattutto, la mappatura di memoria virtuale, risulta tipica dei meccanismi di **persistenza**, **evasione** e **iniezione di codice** propri dei payload della famiglia Meterpreter.

## 9. Analisi delle Sezioni del File Eseguibile

L'esame della struttura interna del file, condotto tramite la funzione di analisi delle sezioni di PEStudio (Figura 9), ha permesso di individuare **cinque sezioni**, di cui una risultante dalla ripetizione anomala del medesimo nome (`.text`), circostanza di per sé indicativa di una probabile manipolazione della struttura originaria del file mediante strumenti di *packing*.

**Figura 10** — *Tabella delle sezioni del file PE, con relativi valori di entropia, dimensioni e caratteristiche di lettura/scrittura/esecuzione; si segnala in evidenza (riquadro blu) l'indicatore "self-modifying" associato alla seconda sezione ".text".*

**Tabella 4 — Sezioni del file eseguibile e relativa descrizione tecnica**

| Sezione | Entropia | Caratteristiche | Descrizione tecnica (elaborata con supporto AI) |
|---|---|---|---|
| **.text** (sezione 0) | 6,214 | Esecuzione | Sezione che contiene tradizionalmente il codice macchina eseguibile del programma. Il valore di entropia rilevato (6,214 su una scala massima di 8) è sensibilmente superiore a quanto tipicamente atteso per codice compilato non compresso (generalmente compreso tra 5 e 6), suggerendo la presenza di codice sottoposto a tecniche di offuscamento o di compressione parziale. |
| **.data** (sezione 1) | 1,149 | Lettura/Scrittura | Sezione destinata alla memorizzazione delle variabili globali e statiche inizializzate del programma. Il basso valore di entropia rilevato è coerente con la natura ordinariamente non compressa di tale sezione, contenente prevalentemente dati strutturati e non codice eseguibile. |
| **.rsrc** (sezione 2) | 5,421 | Lettura | Sezione delle risorse del programma, contenente elementi quali icone, stringhe, finestre di dialogo e informazioni di versione. Il valore di entropia, pur non anomalo in assoluto per risorse contenenti immagini compresse, risulta comunque significativo e meritevole di approfondimento in sede di analisi dinamica. |
| **.text** (sezione 3, duplicata) | 6,428 | Lettura/Scrittura/Esecuzione, **self-modifying** | Sezione di particolare interesse investigativo: la duplicazione del nome standard `.text`, unitamente alla combinazione di permessi di lettura, scrittura ed esecuzione simultanei e al flag "self-modifying" (codice auto-modificante) esplicitamente segnalato dallo strumento, costituisce un indicatore di elevatissima gravità. Tale configurazione è tipicamente associata a routine di *unpacking* o *stub* di decifratura che scrivono ed eseguono codice all'interno della medesima area di memoria in fase di avvio del processo, tecnica ampiamente documentata nell'ambito dei *packer* malevoli e della generazione di payload tramite framework quali Metasploit. |
| **.idata** (sezione 4) | 5,439 | Lettura | Sezione contenente la tabella degli indirizzi di importazione (*Import Address Table*), utilizzata dal sistema operativo per la risoluzione dinamica degli indirizzi delle funzioni importate dalle librerie esterne documentate nella Sezione 8 della presente relazione. |

L'elemento di maggior rilievo emerso da tale analisi risiede, con evidenza, nella sezione duplicata `.text` (sezione 3), la cui combinazione di attributi — permessi RWX (lettura, scrittura ed esecuzione) contemporanei e flag di auto-modifica del codice — rappresenta uno degli indicatori tecnici più affidabili per la classificazione di un file come *packed* o contenente uno *stub* di caricamento di uno *shellcode*, in piena coerenza con quanto già riscontrato nella Fase 3 mediante la corrispondenza con la regola YARA relativa ai *reverse shell*.

## 10. Analisi dei Rischi e Contromisure

La presente sezione approfondisce, in chiave sistemica, i rischi connessi alla tipologia di minaccia identificata, articolando l'analisi secondo un modello che tiene conto della probabilità di occorrenza, dell'impatto potenziale e delle relative misure di mitigazione, in coerenza con i principi dei framework NIST Cybersecurity Framework e MITRE ATT&CK.

### 10.1 Identificazione dei Rischi

| Rischio | Tecnica MITRE ATT&CK di riferimento | Impatto potenziale |
|---|---|---|
| **Esecuzione accidentale del payload da parte dell'utente**, tratto in inganno dal nome e dall'icona dell'applicazione | T1204 — *User Execution* | Compromissione totale della riservatezza, integrità e disponibilità del sistema (accesso remoto non autorizzato) |
| **Persistenza del malware** tramite modifica del registro di sistema | T1547 — *Boot or Logon Autostart Execution* | Permanenza della compromissione anche a seguito di riavvii successivi del sistema |
| **Iniezione di codice in processi legittimi** tramite le API di mappatura della memoria | T1055 — *Process Injection* | Elusione dei controlli antivirus basati sulla reputazione del processo ed esecuzione di codice con i privilegi del processo ospitante |
| **Comunicazione con infrastruttura di comando e controllo (C2)** tipica dei payload Meterpreter | T1071 — *Application Layer Protocol* | Esfiltrazione di dati sensibili, controllo remoto non autorizzato del sistema, movimento laterale verso altri host della rete |
| **Furto di credenziali** conseguente al controllo remoto del sistema | T1555 — *Credentials from Password Stores* | Compromissione di ulteriori sistemi e servizi (bancari, aziendali, cloud) tramite riutilizzo delle credenziali sottratte |
| **Elusione dei controlli di sicurezza perimetrali** grazie alle tecniche di *masquerading* e *packing* | T1027 — *Obfuscated Files or Information*; T1036 — *Masquerading* | Riduzione dell'efficacia dei sistemi antivirus tradizionali basati su firme statiche |

### 10.2 Contromisure Tecniche

- **Implementazione di soluzioni EDR (*Endpoint Detection and Response*)**: a differenza degli antivirus tradizionali basati su firme, tali soluzioni sono in grado di rilevare comportamenti anomali (quali la scrittura ed esecuzione di codice nella medesima area di memoria) anche in assenza di una firma nota, mitigando efficacemente il rischio descritto in Tabella relativamente alla tecnica T1055;
- **Applicazione del principio del privilegio minimo (*least privilege*)**: la limitazione dei diritti di scrittura sul registro di sistema per gli utenti non amministrativi riduce sensibilmente la capacità del malware di conseguire persistenza (T1547);
- **Adozione di politiche di *application whitelisting*** (ad esempio tramite Windows Defender Application Control o AppLocker), che impediscono l'esecuzione di eseguibili non esplicitamente autorizzati, indipendentemente dal nome o dall'icona con cui si presentano;
- **Segmentazione della rete e monitoraggio del traffico East-West**, secondo il principio Zero Trust, al fine di limitare la capacità del malware di stabilire comunicazioni con infrastrutture di comando e controllo esterne e di contenere eventuali fenomeni di movimento laterale;
- **Analisi comportamentale del traffico di rete** mediante sistemi IDS/IPS dotati di firme aggiornate per il rilevamento del traffico Meterpreter, tipicamente riconoscibile da specifici pattern di comunicazione anche in presenza di cifratura del canale;
- **Verifica dell'integrità dei file tramite firma digitale**: l'assenza di una firma digitale valida (rilevata anche nel campione in esame, ove il campo "certificate" risulta non disponibile) costituisce un ulteriore indicatore da integrare nelle politiche di controllo preventivo dell'esecuzione.

### 10.3 Contromisure Organizzative

- **Formazione e sensibilizzazione del personale** (*security awareness*) in merito ai rischi connessi all'apertura di file eseguibili di provenienza non verificata, anche qualora questi si presentino con nomi e icone apparentemente innocui;
- **Definizione di procedure di *incident response* collaudate**, comprensive di un piano di isolamento immediato degli host potenzialmente compromessi, di analisi forense e di ripristino da backup verificati;
- **Politiche di gestione delle password** che prevedano la rotazione immediata delle credenziali in caso di sospetta compromissione, privilegiando l'utilizzo di dispositivi alternativi e non compromessi per l'operazione;
- **Adozione dell'autenticazione a più fattori resistente al phishing** (chiavi hardware FIDO2 o passkey), quale misura di contenimento del danno anche in caso di avvenuta sottrazione delle credenziali da parte del malware.

### 10.4 Sintesi della Valutazione del Rischio

Sulla base delle evidenze raccolte, il rischio complessivo associato al campione `notepad-classico.exe`, qualora eseguito in un ambiente di produzione privo delle contromisure sopra descritte, deve essere qualificato come **elevato**, in ragione della combinazione tra un'alta probabilità di esecuzione accidentale (dovuta all'efficace tecnica di *masquerading* adottata) e un impatto potenzialmente critico (accesso remoto non autorizzato con capacità di persistenza e furto di credenziali).

## 11. Considerazioni Finali

L'insieme delle evidenze raccolte nel corso della presente attività di laboratorio converge, in maniera coerente e reciprocamente corroborante, verso l'identificazione univoca del campione `notepad-classico.exe` quale **trojan appartenente alla famiglia Rozena/Meterpreter**, dotato di caratteristiche tipiche dei payload generati mediante framework di post-exploitation quali Metasploit.

Si è potuto osservare come il campione impieghi una strategia articolata su tre livelli:

1. **Livello di inganno visivo (masquerading)**: il nome del file, la sua icona, la descrizione interna ("Blocco note") e il nome del modulo originale (`NOTEPAD.EXE`) sono stati deliberatamente predisposti al fine di far percepire il file come l'applicazione di sistema Blocco Note, sfruttando la fiducia implicita dell'utente verso componenti nativi del sistema operativo;
2. **Livello di offuscamento tecnico (packing)**: l'elevata entropia riscontrata nelle sezioni contenenti codice eseguibile, unitamente alla duplicazione anomala della sezione `.text` e alla presenza del flag di auto-modifica del codice, indica con elevata probabilità l'impiego di un *packer* finalizzato a occultare il payload reale agli strumenti di analisi statica tradizionali;
3. **Livello funzionale malevolo**: le funzioni importate dalle librerie di sistema, in particolare quelle relative alla scrittura sul registro (persistenza) e alla mappatura di memoria virtuale (iniezione di codice), unitamente alla corrispondenza con la regola YARA relativa a *shellcode* di tipo *reverse shell*, confermano la presenza di funzionalità di controllo remoto non autorizzato del sistema.

L'esercitazione ha altresì evidenziato l'efficacia di un approccio metodologico incrementale, che combina strumenti di analisi statica automatizzata, piattaforme di *threat intelligence* collaborativa e strumenti di analisi manuale approfondita, quale prassi consolidata nell'ambito della disciplina della *malware analysis*, nonché l'utilità del supporto di sistemi di intelligenza artificiale quale strumento di ausilio all'interpretazione tecnica — e non sostitutivo — del giudizio critico dell'analista.

## 12. Conclusioni

L'attività di laboratorio condotta ha consentito di raggiungere pienamente gli obiettivi didattici prefissati, dimostrando come l'applicazione rigorosa di una metodologia di analisi statica strutturata sia in grado di rivelare, con un elevato grado di confidenza, la reale natura di un file eseguibile anche in assenza della sua esecuzione, riducendo così al minimo l'esposizione al rischio nel corso del processo di indagine.

Il campione `notepad-classico.exe` rappresenta un caso paradigmatico ed esemplificativo delle moderne strategie di *social engineering* tecnico impiegate dal cybercrime, in cui l'inganno visivo si combina con sofisticate tecniche di offuscamento del codice, a conferma di come la sola vigilanza dell'utente finale, per quanto essenziale, non possa costituire l'unica linea di difesa di un'organizzazione. La sicurezza informatica, come emerso anche dall'analisi dei rischi e delle contromisure sviluppata nella presente relazione, deve pertanto essere concepita come un processo continuo e multilivello, fondato sull'integrazione sinergica di misure tecniche (soluzioni EDR, segmentazione di rete, controllo delle applicazioni), misure organizzative (formazione, procedure di incident response) e un costante affinamento delle competenze analitiche del personale addetto alla sicurezza.

L'esperienza maturata nel corso della presente esercitazione costituisce, in tal senso, un contributo formativo di rilievo per lo sviluppo delle competenze professionali richieste nell'ambito della cybersecurity, in piena aderenza ai principi etici e metodologici propri della disciplina dell'*ethical hacking*.

---

*La presente relazione è stata redatta esclusivamente per finalità didattiche e di formazione accademica, nell'ambito di un'attività di laboratorio condotta in ambiente virtualizzato, isolato e controllato. Nessuna delle operazioni descritte è stata eseguita al di fuori di tale ambiente, né ha comportato l'esecuzione del codice malevolo analizzato.*