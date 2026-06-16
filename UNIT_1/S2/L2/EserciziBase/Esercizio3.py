# Programma che chiede un numero e stampa la sua tabellina fino a 10

# Chiedi il numero all'utente
numero = int(input("Inserisci un numero: "))

print(f"\nTabellina del {numero}:")

# Stampa la tabellina
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")