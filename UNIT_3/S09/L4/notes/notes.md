# Configurazione del Registro di Sicurezza per Login/Logoff

Ecco i passaggi per abilitare e gestire il registro.
1. Accedere al Visualizzatore Eventi

Il primo passo per iniziare è aprire lo strumento di gestione dei log.
    Premi Win + R per aprire la finestra "Esegui".
    Digita eventvwr e premi Invio.

2. Configurare le Proprietà del Registro di Sicurezza

È utile sapere dove si trovano i file di log e come si comportano quando sono pieni.
    Nel pannello di sinistra, espandi Registri di Windows e seleziona Sicurezza.
    Fai clic con il tasto destro su "Sicurezza" e scegli Proprietà.
    Nella finestra che si apre, puoi vedere e modificare il percorso del file di log (ad esempio, %SystemRoot%\System32\winevt\Logs\Security.evtx) e la dimensione massima del log (il valore predefinito è 20.480 KB).
    Nella sezione "Quando il log è pieno", puoi scegliere se sovrascrivere gli eventi (per impostazione predefinita) o archiviare il log.

3. Abilitare il Controllo degli Accessi (Audit)

Questo è il passaggio cruciale per far sì che Windows registri gli eventi di login e logoff.

Importante: Esistono due modi per farlo, ma non vanno usati insieme, altrimenti si rischiano risultati inaspettati.
Opzione A: Politiche di Controllo Avanzate (Raccomandata)

Questo metodo è più granulare e viene utilizzato nei sistemi moderni.
    Apri il Editor Criteri di gruppo locali (digita gpedit.msc in "Esegui" e premi Invio).
    Naviga fino al percorso: Configurazione computer > Impostazioni di Windows > Impostazioni di Sicurezza > Configurazione criteri di controllo avanzati > Criteri di controllo di sistema > Accesso/Disconnessione.
    Nel riquadro di destra, per registrare gli accessi, abilita i seguenti criteri:
        Controllo accesso (Audit Logon): Seleziona le caselle Operazione riuscita e Operazione non riuscita per registrare sia gli accessi riusciti che quelli falliti.
    Per registrare le disconnessioni, abilita il criterio Controllo disconnessione (Audit Logoff) selezionando almeno Operazione riuscita.

Opzione B: Criteri di Controllo di Base

Questo metodo è più semplice ma meno dettagliato.
    Apri l' Editor Criteri di gruppo locali.
    Naviga fino al percorso: Configurazione computer > Impostazioni di Windows > Impostazioni di Sicurezza > Criteri locali > Criteri di controllo.
    Nel riquadro di destra, fai doppio clic su Controllo eventi di accesso.
    Seleziona le caselle Operazione riuscita e Operazione non riuscita.



Come configurarle:

Per "Controlla Accesso":
    Fai clic con il tasto destro su "Controlla Accesso"
    Seleziona "Proprietà"
    Nella finestra che si apre, spunta:
        Operazione riuscita (per registrare i login riusciti)
        Operazione non riuscita (per registrare i tentativi di login falliti)
    Clicca su OK

Per "Controlla Fine sessione":
    Fai clic con il tasto destro su "Controlla Fine sessione"
    Seleziona "Proprietà"
    Spunta:
        Operazione riuscita (per registrare i logoff)
    Clicca su OK

Risultato finale:

Dopo aver configurato, le due sottocategorie dovrebbero apparire così:
Sottocategoria	Eventi di controllo
Controlla Accesso	Operazione riuscita, Operazione non riuscita
Controlla Fine sessione	Operazione riuscita
Nota importante:

Nell'immagine vedo che tutto è impostato su "Non configurata". Questo significa che al momento non sta registrando nulla. Dopo aver applicato le modifiche come descritto sopra, Windows inizierà a tracciare tutti gli accessi e le disconnessioni.
Verifica finale:
    Chiudi tutte le finestre e clicca su OK/Applica per salvare.
    Apri il Visualizzatore eventi (eventvwr).
    Vai su Registri di Windows → Sicurezza.
    Effettua un login/logoff (o blocca/sblocca il PC con Win + L).
    Aggiorna il registro (tasto destro su "Sicurezza" → "Aggiorna").
    Dovresti vedere eventi con:
        ID 4624 = Accesso riuscito
        ID 4625 = Accesso fallito
        ID 4634 o 4647 = Disconnessione