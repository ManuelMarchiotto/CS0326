# Contare le vocali in una stringa

stringa = input("Inserisci una stringa: ")

# Vocali sia minuscole che maiuscole
vocali = "aeiouAEIOU"
conteggio = 0

for carattere in stringa:
    if carattere in vocali:
        conteggio += 1

print(f"Nella stringa inserita ci sono {conteggio} vocali.")