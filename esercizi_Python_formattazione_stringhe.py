# Esercizio 1
# Creare due variabili "nome" e "cognome" e concatenarle a schermo.

nome = 'Francesca'
cognome = 'Colombo'
s = nome + " " + cognome
print(s)

# Esercizio 2
# Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".

numero = 42
s = 'Il numero è:' + " " + str(numero)
print(s)

# Esercizio 3
# Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". 
# Per il binario utilizzare bin(numero)

numero = 42
s = 'il numero binario di' + " " + str(numero)+ ' è ' + str(bin(numero))
print(s)

# Esercizio 4
# Partendo dalla variabile "numero" uguale a 5, utilizzare le f-strings (interpolazione) 
# per ottenere "Il quadrato di 5 è 25".

numero = 5
s = f'Il quadrato di {numero} è {numero*5}'
print(s)

# Esercizio 5
# Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere 
# "Il mio nome è {nome} ed il cognome è {cognome}". 
# Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.

nome = 'Francesca'
cognome = 'Colombo'
s = f'Il mio nome è {nome} ed il mio cognome è {cognome}'
print(s)

# Esercizio 6
# Facendo riferimento all'esercizio precedente ottenere il seguente risultato modificando 
# i valori nel format(): "Il mio nome è LUCA ed il cognome è RoKKi"

s = f'Il mio nome è {nome.replace('Francesca', 'LUCA')} ed il mio cognome è {cognome.replace('Colombo', 'RoKKi')}'
print(s)