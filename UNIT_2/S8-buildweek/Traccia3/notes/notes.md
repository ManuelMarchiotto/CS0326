Normale:


# Bonus:

## Descrizione del funzionamento:

Questo programma C esegue le seguenti operazioni:

Dichiarazione variabili:
    vector[10]: array di 10 interi
    i, j, k: contatori per cicli
    swap_var: variabile di appoggio per lo scambio

Input utente:
    Chiede all'utente di inserire 10 interi
    Usa un ciclo for con scanf per leggere i valori
    Mostra un prompt con l'indice corrente [1], [2], ..., [10]

Stampa vettore inserito:
    Mostra tutti i 10 valori inseriti con i relativi indici

Ordinamento (Bubble Sort):
    Implementa l'algoritmo di ordinamento a bolle
    Confronta elementi adiacenti e li scambia se sono in ordine decrescente
    Ordina il vettore in modo crescente

Stampa vettore ordinato:
    Mostra i 10 valori ordinati con i relativi indici


## SPIEGAZIONE DELLA VULNERABILITA'
Buffer Overflow:

Il problema è in questa riga:
c

scanf("%d", &vector[10 + counter]);

Cosa succede:
    vector ha dimensione 10 (indici da 0 a 9)
    Quando counter è 0, si scrive in vector[10] → fuori dai limiti!
    Si sta scrivendo nella memoria adiacente, sovrascrivendo:
        Altre variabili (swap_var, i, j, k)
        Il frame dello stack
        L'indirizzo di ritorno della funzione

Perché causa Segmentation Fault:

    Scrivendo oltre i limiti, si corrompe la memoria dello stack

    Quando si sovrascrive l'indirizzo di ritorno, il programma salta a un indirizzo invalido

    Il sistema operativo termina il processo con "Segmentation fault"

## CONTROLLI DI INPUT AGGIUNTIVI

Per rendere il programma più robusto, aggiungi questi controlli:
c

// Controllo che l'input sia un numero intero valido
int val;
while (scanf("%d", &val) != 1) {
    printf("Input non valido! Inserisci un numero intero: ");
    while (getchar() != '\n');  // Pulisce il buffer
}
vector[i] = val;

// Controllo del range (es. solo numeri positivi)
if (val < 0) {
    printf("Inserisci un numero positivo!\n");
    i--;  // Ripeti l'inserimento
    continue;
}