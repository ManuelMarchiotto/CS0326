#Progrmma che verifica se il numero è pari o dispari

# chiedo all'utente un numero
num = input("Inserisci un numero:")


# facendo il modulo verifico se per caso il numero è pari o dispari perche 
# se il resto della dicvisione per 2 è sempre un numero pari
if int(num) % 2 ==0:
    print("il numero è pari")
else:
    print("il numero è dispari")

