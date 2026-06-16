# Trova il massimo in una lista di numeri

# Chiediamo i numeri separati da spazio
input_utente = input("Inserisci una lista di numeri separati da spazio: ")

# Convertiamo la stringa in lista di numeri
numeri = [int(x) for x in input_utente.split()]

if numeri:  # controlla che la lista non sia vuota
    massimo = max(numeri)
    print(f"Il numero più grande è: {massimo}")
else:
    print("Non hai inserito nessun numero.")