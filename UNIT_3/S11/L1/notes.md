
## Parte 1: Esplorazione dei Processi

### Passo 1: Scaricare e preparare Sysinternals Suite
- Nel tuo browser, vai a questo link: [Sysinternals Suite](https://learn.microsoft.com/sysinternals/downloads/sysinternals-suite)
- Clicca sul link di download (di solito "Download Sysinternals Suite").
- Una volta scaricato il file `.zip`, fai clic destro su di esso e seleziona **Estrai tutto...** (o usa un programma come 7-Zip).
- Estrai i file in una cartella facile da trovare (es. `Desktop\SysinternalsSuite`).
- Apri la cartella `SysinternalsSuite`.

### Passo 2: Esplorare e terminare un processo
- Nella cartella, cerca il file `procexp.exe` e fai doppio clic per aprirlo.
- Se compare una finestra, leggi e clicca su **Accept** (Accetta) per l'accordo di licenza (EULA).
- Vedrai un elenco di processi in esecuzione. Nella barra degli strumenti in alto, cerca un'icona che sembra un mirino (o un bersaglio) chiamata **"Find Window's Process"**.
- Clicca su quell'icona del mirino, tieni premuto il pulsante del mouse e trascina il mirino sopra la finestra del tuo browser web aperto, poi rilascia il mouse.
- Process Explorer evidenzierà automaticamente il processo del tuo browser (es. `msedge.exe` o `chrome.exe`).
- Fai clic destro sul processo evidenziato e seleziona **Kill Process** (Termina processo). Conferma con **OK**. *(Il tuo browser si chiuderà improvvisamente).*

### Passo 3: Avviare e osservare un nuovo processo
- Premi il tasto `Windows` sulla tastiera, scrivi `cmd` e premi **Invio** per aprire il Prompt dei comandi.
- Torna su Process Explorer. Clicca di nuovo sull'icona del mirino e trascinala sulla finestra del Prompt dei comandi. Process Explorer evidenzierà `cmd.exe`.
- Osserva la struttura ad albero a sinistra: vedrai che `cmd.exe` è sotto `explorer.exe` (il padre) e ha sotto di sé `conhost.exe` (il figlio).
- Nella finestra del Prompt dei comandi, scrivi: `ping google.com` e premi **Invio**.
- Guarda immediatamente Process Explorer: vedrai apparire temporaneamente un nuovo processo figlio chiamato `ping.exe` sotto `cmd.exe` mentre il ping è in esecuzione.
- Fai clic destro su `conhost.exe` e seleziona **Check VirusTotal**. 
- Clicca su **Yes** per accettare i termini di servizio di VirusTotal, poi su **OK** alla richiesta successiva.
- Se non la vedi, abilita la colonna VirusTotal: vai nel menu in alto su **View** (Visualizza) > **Select Columns...** > scheda **VirusTotal** > spunta "VirusTotal Ratio" e clicca **OK**. Vedrai un punteggio (es. `0/70`, che significa che è sicuro).
- Fai clic destro su `cmd.exe` e seleziona **Kill Process**. Conferma con **OK**.

> **Osservazione:** Nota che anche `conhost.exe` (e `ping.exe` se era ancora attivo) è scomparso, perché i processi figli vengono terminati automaticamente quando il processo padre (`cmd.exe`) viene ucciso.

---

## Parte 2: Esplorazione di Thread e Handle

### Passo 1: Esplorare i Thread
- Apri di nuovo il Prompt dei comandi (`cmd` dal menu Start).
- In Process Explorer, usa il mirino per selezionare di nuovo il nuovo `conhost.exe` associato al prompt.
- Fai clic destro su `conhost.exe` e scegli **Properties...** (Proprietà).
- Vai alla scheda **Threads**. Qui vedrai un elenco di thread con dettagli come:
  - **TID**: L'ID univoco del thread.
  - **Start Address**: Dove inizia l'esecuzione (es. nomi di file `.dll`).
  - **Context Switches**: Quante volte la CPU ha cambiato contesto per questo thread.
- Clicca su **OK** per chiudere la finestra.

### Passo 2: Esplorare gli Handle
- In Process Explorer, vai nel menu in alto e clicca su **View** (Visualizza).
- Vai su **Lower Pane View** (Vista riquadro inferiore) e seleziona **Handles**.
- Ora la parte inferiore della finestra mostrerà tutti gli "handle" (riferimenti) che `conhost.exe` sta utilizzando.

> **Osservazione:** Vedrai che puntano a oggetti di sistema come chiavi del Registro di sistema (`\Registry`), file, sezioni di memoria (`\Section`), o altri processi/thread.

- Chiudi Process Explorer (**File** > **Exit**).

---

## Parte 3: Esplorazione del Registro di Windows

### Passo 1: Aprire l'Editor del Registro
- Premi il tasto `Windows`, scrivi `regedit` e premi **Invio**.
- Se Windows te lo chiede (Controllo dell'account utente), clicca su **Sì** per consentire le modifiche.

### Passo 2: Trovare la chiave dell'EULA di Process Explorer
- Nella colonna di sinistra, usa le freccette per espandere le cartelle in questo ordine esatto:
  1. `HKEY_CURRENT_USER`
  2. `Software`
  3. `Sysinternals`
  4. `Process Explorer`
- Clicca sulla cartella `Process Explorer`. Nella parte destra della finestra, vedrai una voce chiamata `EulaAccepted`.
- Osserva la colonna "Dati": il valore dovrebbe essere `1` (o `0x00000001 (1)`), che significa che hai già accettato la licenza in precedenza.

### Passo 3: Modificare il valore
- Fai doppio clic su `EulaAccepted`.
- Nella casella "Dati valore" (Value data), cancella `1` e scrivi `0`.
- Clicca su **OK**. Ora la colonna "Dati" mostrerà `0`.

### Passo 4: Verificare la modifica
- Vai nella cartella `SysinternalsSuite` che hai estratto all'inizio.
- Fai doppio clic su `procexp.exe` per aprirlo.

> **Risultato finale:** Vedrai apparire di nuovo la finestra dell'Accordo di Licenza (EULA) di Process Explorer, esattamente come la prima volta che lo hai aperto. Questo dimostra che il Registro di sistema controlla questa impostazione e, avendola resettata a `0`, il programma ti chiede nuovamente di accettarla prima di avviarsi.