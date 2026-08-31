# Esercizio: Creazione di Gruppi e Condivisioni in Windows Server 2022 (Active Directory)

## Obiettivo
Familiarizzare con la gestione dei gruppi di utenti e delle condivisioni di rete in Windows Server 2022. Imparerai a creare gruppi di dominio, condividere cartelle tramite interfaccia grafica e consentire l'accesso remoto alle risorse di rete.

---

## Scenario dell'Esercizio
Simuleremo un'azienda con due reparti distinti. Creeremo due **Gruppi Globali** di dominio e condivideremo le cartelle per l'accesso via rete:
1. **`Team_Finanza`**: Richiede accesso remoto alla cartella condivisa con dati finanziari.
2. **`HelpDesk_Livello1`**: Richiede accesso remoto alla cartella strumenti di diagnostica.

---

## Fase 1: Preparazione e Apertura di Active Directory

1. Accedi al Domain Controller con un account membro del gruppo **Domain Admins**.
2. Apri lo strumento **Active Directory Users and Computers**:
   - Premi `Win + R`, digita `dsa.msc` e premi Invio.
   - *Oppure:* Apri **Server Manager** → **Tools** → **Active Directory Users and Computers**.
3. Nell'albero a sinistra, espandi il tuo dominio (es. `Epicode.local`) e clicca sulla **OU (Organizational Unit)** dove vuoi creare i gruppi.

---

## Fase 2: Creazione dei Gruppi

### Creazione del gruppo `Team_Finanza`
1. Clicca col tasto destro nello spazio vuoto della OU selezionata → **New** → **Group**.
2. Compila i campi:
   - **Group name:** `Team_Finanza`
   - **Group name (pre-Windows 2000):** `Team_Finanza`
   - **Group scope:** Seleziona **Global**
   - **Group type:** Seleziona **Security**
3. Nel campo **Description** scrivi: *"Gruppo per i membri del dipartimento finanziario. Accesso ai report contabili."*
4. Clicca **OK**.

### Creazione del gruppo `HelpDesk_Livello1`
1. Tasto destro → **New** → **Group**.
2. Compila i campi:
   - **Group name:** `HelpDesk_Livello1`
   - **Group scope:** **Global**
   - **Group type:** **Security**
3. **Description:** *"Gruppo per il supporto tecnico di primo livello. Accesso remoto e diagnostica."*
4. Clicca **OK**.

---

## Fase 3: Creazione Utenti e Aggiunta ai Gruppi

### Creazione utente `mario.rossi` (Team_Finanza)
1. In ADUC, tasto destro sulla OU → **New** → **User**.
2. Compila:
   - **First name:** Mario
   - **Last name:** Rossi
   - **User logon name:** `mario.rossi`
   - Clicca **Next**
   - Password: `Password123!`
   - **Deseleziona**: *User must change password at next logon*
   - Clicca **Next** → **Finish**

### Creazione utente `luca.bianchi` (HelpDesk_Livello1)
Ripeti la procedura creando `luca.bianchi`.

### Aggiungi utenti ai gruppi
1. Doppio clic su `mario.rossi` → scheda **Member Of** → **Add...**
2. Digita `Team_Finanza` → **Check Names** → **OK** → **OK**
3. Doppio clic su `luca.bianchi` → scheda **Member Of** → **Add...**
4. Digita `HelpDesk_Livello1` → **Check Names** → **OK** → **OK**

---

## Fase 4: Configurazione delle Condivisioni (Sharing)

### 1. Condivisione cartella Finanza (Per `Team_Finanza`)

#### Passo A: Crea la cartella
1. Apri **File Explorer**
2. Vai su `C:\` e crea la cartella `Dati_Aziendali`
3. Dentro crea la sottocartella `Finanza`

#### Passo B: Condividi la cartella
1. Tasto destro su `C:\Dati_Aziendali\Finanza` → **Properties**
2. Vai alla scheda **Sharing**
3. Clicca **Advanced Sharing...**
4. ✅ Spunta **Share this folder**
5. **Share name:** `Finanza` (questo sarà il nome visibile in rete)
6. Clicca **Permissions**

#### Passo C: Configura i permessi di condivisione
1. Seleziona **Everyone** → clicca **Remove**
2. Clicca **Add...**
3. Digita `Team_Finanza` → **Check Names** → **OK**
4. Seleziona `Team_Finanza` nella lista
5. Nella colonna **Allow**, spunta:
   - ✅ **Full Control**
   - ✅ **Change**
   - ✅ **Read**
6. Clicca **OK** → **OK** → **Close**

#### Passo D: Configura Security (NTFS) - Necessario!
⚠️ **Importante:** Anche se usi lo Sharing, devi configurare anche la scheda Security altrimenti l'accesso verrà negato.

1. Sempre in **Properties** della cartella, vai alla scheda **Security**
2. Clicca **Edit...** → **Add...**
3. Digita `Team_Finanza` → **Check Names** → **OK**
4. Seleziona `Team_Finanza` e spunta **Allow**:
   - ✅ **Modify**
   - ✅ **Read & execute**
   - ✅ **List folder contents**
   - ✅ **Read**
   - ✅ **Write**
5. Clicca **OK** → **OK**

---

### 2. Condivisione cartella Diagnostica (Per `HelpDesk_Livello1`)

#### Passo A: Crea la cartella
1. Crea la cartella `C:\Tools\Diagnostica`
2. Dentro crea un file di testo e rinominalo `check_system.bat`

#### Passo B: Condividi la cartella
1. Tasto destro su `C:\Tools\Diagnostica` → **Properties** → **Sharing**
2. **Advanced Sharing...**
3. ✅ Spunta **Share this folder**
4. **Share name:** `Diagnostica`
5. Clicca **Permissions**

#### Passo C: Configura i permessi
1. **Remove** → **Everyone**
2. **Add...** → digita `HelpDesk_Livello1` → **Check Names** → **OK**
3. Seleziona `HelpDesk_Livello1` e spunta:
   - ✅ **Full Control**
4. **OK** → **OK** → **Close**

---

## Fase 5: Abilita Accesso Remoto (RDP)

Per permettere agli utenti di accedere al server da remoto:

1. Apri **Server Manager** → **Local Server**
2. Clicca su **Remote Desktop** (probabilmente è *Disabled*)
3. Seleziona: **Allow remote connections to this computer**
4. **Deseleziona**: *Allow connections only from computers running Remote Desktop with Network Level Authentication*
5. Clicca **Select Users...**
6. **Add...** → digita `HelpDesk_Livello1` → **Check Names** → **OK**
7. **OK** → **OK**

---

## Fase 6: Documentazione delle Scelte

| Gruppo | Risorsa Condivisa | Share Name | Permesso Sharing |
| :--- | :--- | :--- | :--- |
| **Team_Finanza** | `C:\Dati_Aziendali\Finanza` | `Finanza` | Full Control |
| **HelpDesk_Livello1** | `C:\Tools\Diagnostica` | `Diagnostica` | Read |


---
