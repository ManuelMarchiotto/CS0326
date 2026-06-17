import math


def calcola_quadrato():
    print("\n--- PERIMETRO QUADRATO ---")
    lato = float(input("Inserisci la lunghezza del lato: "))
    if lato < 0:
        print("Errore: Il lato non può essere negativo.")
        return
    perimetro = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro:.2f}")


def calcola_cerchio():
    print("\n--- CIRCONFERENZA CERCHIO ---")
    raggio = float(input("Inserisci la lunghezza del raggio: "))
    if raggio < 0:
        print("Errore: Il raggio non può essere negativo.")
        return
    # Circonferenza = 2 * pi_greco * r
    circonferenza = 2 * math.pi * raggio
    print(f"La circonferenza del cerchio è: {circonferenza:.2f}")


def calcola_rettangolo():
    print("\n--- PERIMETRO RETTANGOLO ---")
    base = float(input("Inserisci la lunghezza della base: "))
    altezza = float(input("Inserisci la lunghezza dell'altezza: "))
    if base < 0 or altezza < 0:
        print("Errore: Base e altezza non possono essere negative.")
        return
    # Perimetro = (base * 2) + (altezza * 2)
    perimetro = (base * 2) + (altezza * 2)
    print(f"Il perimetro del rettangolo è: {perimetro:.2f}")


def menu():
    while True:
        print("\n=============================")
        print("   CALCOLO PERIMETRI GEOMETRICI")
        print("=============================")
        print("1. Quadrato")
        print("2. Cerchio (Circonferenza)")
        print("3. Rettangolo")
        print("4. Esci dal programma")

        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            calcola_quadrato()
        elif scelta == "2":
            calcola_cerchio()
        elif scelta == "3":
            calcola_rettangolo()
        elif scelta == "4":
            print("Grazie per aver usato il programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")


# Avvia il programma
if __name__ == "__main__":
    menu()