import re
from collections import Counter

def conteggio_parole(testo: str) -> dict:
    """
    Analizza il testo e restituisce un dizionario con il conteggio delle parole
    (case-insensitive, ignorando la punteggiatura).
    """
    if not testo:
        return {}
    
    # Converti in minuscolo
    testo = testo.lower()
    
    # Rimuovi punteggiatura con regex e sostituisci con spazio
    testo_pulito = re.sub(r'[^\w\s]', ' ', testo)
    
    # Dividi in parole (gestisce anche spazi multipli)
    parole = testo_pulito.split()
    
    # Usa Counter per contare le occorrenze
    return dict(Counter(parole))


# Test
testo = "Ciao, ciao! Come stai? Stai bene?"
print(conteggio_parole(testo))
# Output atteso: {'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}