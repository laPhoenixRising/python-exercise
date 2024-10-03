# Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e 
# stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".

numero = int(input('Inserisci un numero:'))

if (numero > 0):
   print('Il numero è positivo')
else:
   print('Il numero è negativo') 

# Esercizio 2
# Scrivere un programma che chiede all'utente di inserire due numeri e 
# stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, 
# "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, 
# altrimenti stampa "I numeri sono uguali".

n1 = int(input('inserisci un numero:'))
n2 = int(input('inserisci un altro numero:'))

if (n1 > n2):
    print('Il primo numero è maggiore')
elif (n2 > n1):
    print('Il secondo numero è maggiore')
else:
    print('I numeri sono uguali')    

# Esercizio 3
# Scrivere un programma che chiede all'utente di inserire una stringa e 
# stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".

s = input('Inserisci una stringa:')

if (s == ''):
    print('La stringa è vuota')
else:
    print('La stringa non è vuota')    

# Esercizio 4
# Scrivere un programma che chiede all'utente di inserire un numero e 
# stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".

n = int(input('Inserisci un numero:'))

if ((n % 2) == 0):
    print('Il numero è pari')
else:
    print('Il numero è dispari')    

# Esercizio 5
# Scrivere un programma che chiede all'utente di inserire una lettera e 
# stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), 
# altrimenti stampa "La lettera non è una vocale".

lettera = input('Inserisci una lettera:')

if (lettera in ['a', 'i', 'e', 'o', 'u']):
    print('La lettera è una vocale')
else:
    print('La lettera non è una vocale')    

# Esercizio 6
# Scrivere un programma che chiede all'utente di inserire un numero e 
# stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, 
# altrimenti stampa "Il numero non è compreso tra 1 e 10".

numero = int(input('Inserisci un numero:'))

if (numero >= 1 and numero <= 10):
    print('Il numero è compreso tra 1 e 10')
else:
    print('Il numero non è compreso tra 1 e 10')     

# Esercizio 7
# Scrivere un programma che chieda all'utente di inserire un numero intero. 
# Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". 
# Se il numero è uguale a 10, stampare "Il numero è uguale a 10". 
# Se il numero è minore di 10, stampare "Il numero è minore di 10".

numero = int(input('Inserire un numero:'))

if (numero > 10):
    print('Il numero è maggiore di 10')
else:
    if (numero == 10):
        print('Il numero è uguale a 10')
    else:
        print('il numero è minore di 10')        

# Esercizio 8
# Scrivere un programma che chieda all'utente di inserire un carattere. 
# Se il carattere è una vocale (a, e, i, o, u) con isalpha(), 
# stampare "Il carattere inserito è una vocale". 
# Se il carattere è una consonante, stampare "Il carattere inserito è una consonante". 
# Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".


# Esercizio 9 (difficile)
# Scrivi un programma che chieda all'utente di inserire tre numeri interi che rappresentano i lati di un triangolo. 
# Il programma deve verificare se questi tre numeri formano un triangolo rettangolo. 
# Se i tre numeri soddisfano la condizione per essere un triangolo rettangolo 
# (cioè rispettano il teorema di Pitagora), allora stampa "I tre numeri formano un triangolo rettangolo". 
# Altrimenti, stampa "I tre numeri non formano un triangolo rettangolo".