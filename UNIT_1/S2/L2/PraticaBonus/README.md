Traccia: 

Si s criva i s e guenti  programmi in Python: 

Esercizio 1: Calcolo della media mobile 

Descrizione: Scrivi una funzione che calcoli la media mobile di una lista di numeri. La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente. 

Suggerimenti: 
- Usa slicing per ottenere gli ultimi n elementi. 
- Usa la funzione sum() per calcolare la somma degli elementi e poi dividi per n. 

Esempio di input: 
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
n = 3 

Esempio di output: 
[1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

Esercizio 2: Analisi delle parole 

Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola. Ignora la punteggiatura e considera le parole in modo case-insensitive. 

Suggerimenti: 
- Usa il metodo str.lower() per convertire il testo in minuscolo. 
- Usa il modulo re per rimuovere la punteggiatura. 
- Usa un dizionario per tenere traccia delle occorrenze delle parole. 

Esempio di input: 
testo = "Ciao, ciao! Come stai? Stai bene?" 

Esempio di output: 
{'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}