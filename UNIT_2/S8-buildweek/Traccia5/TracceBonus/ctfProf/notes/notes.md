nmap -sV 192.168.1.14  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-30 14:10 +0200
Nmap scan report for 192.168.1.14
Host is up (0.00010s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE        VERSION
21/tcp   open  ftp            Synology DiskStation NAS ftpd
42/tcp   open  tcpwrapped
80/tcp   open  http           Apache httpd 2.4.52 ((Ubuntu))
135/tcp  open  msrpc?
1433/tcp open  ms-sql-s?
1723/tcp open  pptp?
2222/tcp open  ssh            OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
5060/tcp open  sip?           (SIP end point; Status: 200 OK)
5061/tcp open  ssl/sip-tls?
8080/tcp open  http           nginx
8443/tcp open  ssl/https-alt?
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1723-TCP:V=7.99%I=7%D=7/30%Time=6A6B3F58%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,9C,"\0\x9c\0\x01\x1a\+<M\0\x02\0\0\x01\0\x01\0\0\0\0\0\0\0\0
SF:\0\0\x01\0\x01\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\
SF:0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0
SF:\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\
SF:0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5060-TCP:V=7.99%I=7%D=7/30%Time=6A6B3F58%P=x86_64-pc-linux-gnu%r(SI
SF:POptions,10A,"SIP/2\.0\x20200\x20OK\r\nCSeq:\x2042\x20OPTIONS\r\nCall-I
SF:D:\x2050000\r\nVia:\x20SIP/2\.0/TCP\x20nm;branch=foo\r\nFrom:\x20sip:nm
SF:@nm;tag=root\r\nTo:\x20sip:nm2@nm2\r\nContact:\x20sip:nm2@nm2\r\nAllow:
SF:\x20REGISTER,\x20OPTIONS,\x20INVITE,\x20CANCEL,\x20BYE,\x20ACK\r\nConte
SF:nt-Length:\x200\r\nAccept:\x20application/sdp\r\nAccept-Language:\x20en
SF:\r\n\r\n");
MAC Address: 08:00:27:02:CF:A8 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; Device: storage-misc; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.96 seconds

ftp 192.168.1.14
Connected to 192.168.1.14.
220 DiskStation FTP server ready.
Name (192.168.1.14:kali): anonymous
331 Guest login ok, type your email address as password.
Password: 
500 Syntax error: PASS requires an argument
ftp: Login failed
ftp> 
ftp> exit
ftp: lostpeer due to signal 13

nmap -p 80 --script=http-enum 192.168.1.14
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-30 14:13 +0200
Nmap scan report for 192.168.1.14
Host is up (0.0016s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-enum: 
|_  /login.php: Possible admin folder
MAC Address: 08:00:27:02:CF:A8 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.28 seconds

gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html,backup -t 50
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.14
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              html,backup,php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta.html            (Status: 403) [Size: 277]
.htaccess.backup     (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
.htaccess.txt        (Status: 403) [Size: 277]
.htpasswd.php        (Status: 403) [Size: 277]
.htpasswd.html       (Status: 403) [Size: 277]
.htpasswd.txt        (Status: 403) [Size: 277]
.htpasswd.backup     (Status: 403) [Size: 277]
.htaccess.html       (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
.hta.txt             (Status: 403) [Size: 277]
.hta                 (Status: 403) [Size: 277]
.hta.php             (Status: 403) [Size: 277]
.hta.backup          (Status: 403) [Size: 277]
.htaccess.php        (Status: 403) [Size: 277]
css                  (Status: 301) [Size: 310] [--> http://192.168.1.14/css/]
images               (Status: 301) [Size: 313] [--> http://192.168.1.14/images/]
index.php            (Status: 302) [Size: 0] [--> login.php]
index.php            (Status: 302) [Size: 0] [--> login.php]
javascript           (Status: 301) [Size: 317] [--> http://192.168.1.14/javascript/]
login.php            (Status: 200) [Size: 773]
oldsite              (Status: 301) [Size: 314] [--> http://192.168.1.14/oldsite/]
server-status        (Status: 403) [Size: 277]
tmp                  (Status: 200) [Size: 18]
Progress: 23045 / 23065 (99.91%)[ERROR] error on word usuarios.backup: timeout occurred during the request
[ERROR] error on word V.backup: timeout occurred during the request
[ERROR] error on word vector: timeout occurred during the request
[ERROR] error on word vehiclemakeoffer.html: timeout occurred during the request
[ERROR] error on word version.html: timeout occurred during the request
[ERROR] error on word view-source.html: timeout occurred during the request
[ERROR] error on word web-beans.backup: timeout occurred during the request
[ERROR] error on word webfm_send.txt: timeout occurred during the request
[ERROR] error on word webinar.php: timeout occurred during the request
[ERROR] error on word webresource: timeout occurred during the request
[ERROR] error on word webstats.html: timeout occurred during the request
[ERROR] error on word welcome.php: timeout occurred during the request
[ERROR] error on word windows.html: timeout occurred during the request
[ERROR] error on word wstat.backup: timeout occurred during the request
[ERROR] error on word wt.html: timeout occurred during the request
[ERROR] error on word xajax.php: timeout occurred during the request
[ERROR] error on word xalan.backup: timeout occurred during the request
[ERROR] error on word xmlimporter.txt: timeout occurred during the request
[ERROR] error on word xn: timeout occurred during the request
[ERROR] error on word zh-cn.backup: timeout occurred during the request
Progress: 23065 / 23065 (100.00%)
===============================================================
Finished
===============================================================

curl -v http://192.168.1.14/login.php
*   Trying 192.168.1.14:80...
* Established connection to 192.168.1.14 (192.168.1.14 port 80) from 192.168.1.10 port 42752 
* using HTTP/1.x
> GET /login.php HTTP/1.1
> Host: 192.168.1.14
> User-Agent: curl/8.20.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Thu, 30 Jul 2026 12:28:52 GMT
< Server: Apache/2.4.52 (Ubuntu)
< Set-Cookie: PHPSESSID=hpo9n0nj7fd2nvcaphuoegc4sf; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Set-Cookie: wand=c2MqVDFsOVN5ezVi; expires=Thu, 06-Aug-2026 12:28:52 GMT; Max-Age=604800; path=/
< Vary: Accept-Encoding
< Content-Length: 773
< Content-Type: text/html; charset=UTF-8
< 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Login</title>
</head>
<body>
<!-- 
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-------------...--------.<++.>++++++++++++.+.<.>>.+++++.
-->

    <!--<img src="images/theta-logo.jpg" pass="accio" alt="Theta Logo">-->
    <img src="images/theta-logo.png" alt="Theta Logo">
    <hr>
    <form method="POST">
        <h1>Login</h1>
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
            </form>
    
</body>
</html>
* Connection #0 to host 192.168.1.14:80 left intact

Cookie wand: c2MqVDFsOVN5ezVi - Sembra essere base64

<!--<img src="images/theta-logo.jpg" pass="accio" alt="Theta Logo">--> - C'è un attributo pass="accio"

Il commento ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-------------...--------.<++.>++++++++++++.+.<.>>.+++++. è Brainfuck. e si traduce con HELLO

## SCAN Completo

echo "=== SCAN COMPLETO ==="
echo "1. Directory comuni"
gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100 -x php,html,txt

echo -e "\n2. File di configurazione"
gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/seclists/Discovery/Web-Content/config.txt -x php,ini,conf

echo -e "\n3. Backup e database"
for file in "backup" "db" "dump" "sql" "database"; do
    gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x $file,bak,old
done

echo -e "\n4. Directory admin"
gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,html | grep -E "(admin|dashboard|panel|control)"

echo -e "\n5. File con extensioni alternative"
for ext in bak old swp tmp ~ php3 php4 php5 phtml; do
    gobuster dir -u http://192.168.1.14 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x $ext -t 50 -l
done | head -50

 curl -v http://192.168.1.14/welcome.php
*   Trying 192.168.1.14:80...
* Established connection to 192.168.1.14 (192.168.1.14 port 80) from 192.168.1.10 port 41984 
* using HTTP/1.x
> GET /welcome.php HTTP/1.1
> Host: 192.168.1.14
> User-Agent: curl/8.20.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Thu, 30 Jul 2026 13:18:06 GMT
< Server: Apache/2.4.52 (Ubuntu)
< Content-Length: 29
< Content-Type: text/html; charset=UTF-8
< 
<h1>
    65511 => fatto
* Connection #0 to host 192.168.1.14:80 left intact
</h1>                                                                                                               
┌──(kali㉿kali)-[~]
└─$ curl -v http://192.168.1.14/welcome.php \
    -H "Cookie: PHPSESSID=hpo9n0nj7fd2nvcaphuoegc4sf; wand=c2MqVDFsOVN5ezVi"
*   Trying 192.168.1.14:80...
* Established connection to 192.168.1.14 (192.168.1.14 port 80) from 192.168.1.10 port 35152 
* using HTTP/1.x
> GET /welcome.php HTTP/1.1
> Host: 192.168.1.14
> User-Agent: curl/8.20.0
> Accept: */*
> Cookie: PHPSESSID=hpo9n0nj7fd2nvcaphuoegc4sf; wand=c2MqVDFsOVN5ezVi
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Thu, 30 Jul 2026 13:18:34 GMT
< Server: Apache/2.4.52 (Ubuntu)
< Content-Length: 29
< Content-Type: text/html; charset=UTF-8
< 
<h1>
    65511 => fatto
* Connection #0 to host 192.168.1.14:80 left intact
</h1>                                                                                                               
┌──(kali㉿kali)-[~]
└─$ curl http://192.168.1.14/tmp/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at 192.168.1.14 Port 80</address>
</body></html>

┌──(kali㉿kali)-[~]
└─$ curl -v http://192.168.1.14/oldsite/
*   Trying 192.168.1.14:80...
* Established connection to 192.168.1.14 (192.168.1.14 port 80) from 192.168.1.10 port 38162 
* using HTTP/1.x
> GET /oldsite/ HTTP/1.1
> Host: 192.168.1.14
> User-Agent: curl/8.20.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 302 Found
< Date: Thu, 30 Jul 2026 13:20:05 GMT
< Server: Apache/2.4.52 (Ubuntu)
< Set-Cookie: PHPSESSID=e12jk931s0vd9fbbnjf7q8ob8b; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Location: login.php
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
< 
* Connection #0 to host 192.168.1.14:80 left intact

┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.1.14/oldsite/ \
    -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
    -x php,html,txt,bak,old \
    -t 50
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.14/oldsite/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              txt,bak,old,php,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
images               (Status: 301) [Size: 321] [--> http://192.168.1.14/oldsite/images/]
index.php            (Status: 302) [Size: 0] [--> login.php]
login.php            (Status: 200) [Size: 661]
css                  (Status: 301) [Size: 318] [--> http://192.168.1.14/oldsite/css/]
tmp                  (Status: 200) [Size: 17]
Progress: 1323348 / 1323348 (100.00%)
===============================================================
Finished
===============================================================

┌──(kali㉿kali)-[~]
└─$ curl http://192.168.1.14/javascript/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at 192.168.1.14 Port 80</address>
</body></html>

┌──(kali㉿kali)-[~]
└─$ curl http://192.168.1.14/welcome.php.bak
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at 192.168.1.14 Port 80</address>
</body></html>
