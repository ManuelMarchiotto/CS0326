def media_mobile(numeri: list, n: int) -> list:
    """
    Calcola la media mobile di una lista di numeri.
    Per ogni posizione i, la media è calcolata sugli ultimi min(i+1, n) elementi.
    """
    if not numeri or n <= 0:
        return []
    
    risultato = []
    for i in range(len(numeri)):
        # Prendi gli ultimi n elementi (o tutti gli elementi disponibili fino a i)
        finestra = numeri[max(0, i - n + 1): i + 1]
        media = sum(finestra) / len(finestra)
        risultato.append(media)
    
    return risultato


# Test
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(media_mobile(numeri, n))
# Output atteso: [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]