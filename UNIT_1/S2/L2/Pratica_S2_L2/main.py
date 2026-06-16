# Generatore di Nomi per Band Musicali

print("=== Generatore di Nomi per Band Musicali ===\n")

# Richiesta degli input
città = input("Inserisci il nome della tua città di origine: ").strip()
animale = input("Inserisci il nome del tuo animale domestico: ").strip()

# Generazione del nome della band
nome_band = f"{città} {animale}"

# Output
print("\n" + "="*50)
print(f"Il nome della tua band potrebbe essere: {nome_band}")
print("="*50)