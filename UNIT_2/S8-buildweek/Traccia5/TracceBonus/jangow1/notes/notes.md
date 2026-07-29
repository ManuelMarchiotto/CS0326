

## sudo netdiscover -r 192.168.1.0/24

-> 192.168.1.13 blackbox

## sudo nmap -sV -sC -p- 192.168.1.13 

-p- scansiona tutte le porte (1-65535)

-sV rileva le versioni dei servizi

-sC usa gli script predefiniti di nmap

Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-28 16:43 +0200
Stats: 0:01:17 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 61.64% done; ETC: 16:45 (0:00:48 remaining)
Nmap scan report for 192.168.1.13
Host is up (0.0014s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
80/tcp open  http    Apache httpd 2.4.18
|_http-title: Index of /
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-ls: Volume /
| SIZE  TIME              FILENAME
| -     2021-06-10 18:05  site/
|_
MAC Address: 08:00:27:73:C0:1E (Oracle VirtualBox virtual NIC)
Service Info: Host: 127.0.0.1; OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 122.34 seconds

## curl -v http://192.168.1.13

## gobuster dir -u http://192.168.1.13/ -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.13/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.htaccess            (Status: 403) [Size: 277]
.hta                 (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
server-status        (Status: 403) [Size: 277]
site                 (Status: 301) [Size: 311] [--> http://192.168.1.13/site/]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================


## gobuster dir -u http://192.168.1.13/site/ -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.13/site/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.htpasswd            (Status: 403) [Size: 277]
.hta                 (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
assets               (Status: 301) [Size: 318] [--> http://192.168.1.13/site/assets/]
css                  (Status: 301) [Size: 315] [--> http://192.168.1.13/site/css/]
index.html           (Status: 200) [Size: 10190]
js                   (Status: 301) [Size: 314] [--> http://192.168.1.13/site/js/]
wordpress            (Status: 301) [Size: 321] [--> http://192.168.1.13/site/wordpress/]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================

cve 2021-4043 pawnkill reminder