# Esercizio 1
# Assegnare una stringa "ciao mondo" ad una variabile "stringa" e 
# utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.

stringa = 'ciao mondo'
print(stringa.upper())


# Esercizio 2
# Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e 
# utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile.

stringa = 'Benvenuti a Roma'
stringa2 = stringa.lower()
print(stringa2)

# Esercizio 3
# Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e 
# utilizzare il metodo split() per dividere la stringa in una lista di parole.

stringa = 'Il meglio deve ancora venire'
print(stringa.split())

# Esercizio 4
# Assegnare una stringa "Hello World" ad una variabile "stringa" e 
# utilizzare il metodo replace() per sostituire "World" con "Python".

stringa = 'Hello World'
print(stringa.replace('World', 'Python'))

# Esercizio 5
# Assegnare una stringa " Ciao " ad una variabile "stringa" e 
# utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..

stringa = ' Ciao '
print(stringa.strip())

# Esercizio 6
# Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.

stringa = 'abcdefg'
print(stringa [0:3])

# Esercizio 7
# Assegnare una stringa "Python" ad una variabile "stringa" e 
utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".

stringa = 'Python'
print(stringa.startswith('Py'))

# Esercizio 8
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e 
# utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.

stringa = 'Ciao mondo'
print(stringa.count('o'))

# Esercizio 9
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa". 
# Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

stringa = 'Ciao mondo'
print(stringa[-5:].replace('o', 'k'))