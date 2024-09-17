# Esercizio 1
# Dichiarare due variabili "numero1" e "numero2" e assegnargli due numeri interi. 
# Eseguire l'addizione tra le due variabili e assegnare il risultato ad una nuova variabile "somma", 
# mandandola a schermo.

numero1 = 3
numero2 = 7
somma = numero1 + numero2
print(somma)

# Esercizio 2
# Eseguire la sottrazione tra le due variabili e assegnare il risultato ad una nuova variabile "differenza". 
# Mandare a schermo.

differenza = numero1 - numero2
print(differenza)

# Esercizio 3
# Eseguire la moltiplicazione tra le due variabili e assegnare il risultato ad una nuova variabile "prodotto". 
# Mandare a schermo.

prodotto = numero1 * numero2
print(prodotto)

# Esercizio 4
# Eseguire la divisione tra le due variabili e assegnare il risultato ad una nuova variabile "quoziente". 
# Mandare a schermo.

quoziente = numero1 / numero2
print(quoziente)

# Esercizio 5
# Eseguire l'operazione di modulo tra le due variabili e assegnare il risultato ad una nuova variabile "resto". 
# Mandare a schermo.

modulo = numero1 % numero2
print(modulo)

# Esercizio 6
# Incrementare "numero1" di 1 e decrementare "numero2" di 3. Mandare a schermo i nuovi valori.

numero1 = numero1 + 1
numero2 = numero2 - 3
print(numero1, numero2)

# Esercizio 7
# Moltiplicare "numero1" per se stesso + 5, sommarlo quindi a "numero2" elevato alla seconda. 
# Assegnare l'operazione alla variabile risultato e mandare a schermo.

operazione = ((numero1 * numero1) + 5)+(numero2 ** 2)
print(operazione) 

# Esercizio 8
# Trovare quella operazione per portare "numero1" a valere 1 senza riassegnarlo direttamente ad 1 e 
# sottraendolo a se stesso.

numero1 = (numero1 - numero1) + 1
print(numero1)
