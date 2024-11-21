# Esercizio 1
# Creare una tupla vuota e assegnarla a una variabile.

tupla = ()
print(tupla)

# Esercizio 2
# Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".

t = ('mela', 'banana', 'kiwi')
print(t)

# Esercizio 3
# Accedere all'elemento "banana" della tupla precedente.

print(t[1])

# Esercizio 4
# Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.

t2 = t[0:2]
print(t2)

# Esercizio 5
# Verificare se l'elemento "ananas" è presente nella tupla precedente.

'ananas' in t2

# Esercizio 6
# Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").

t3 = ('pesca', 'arancia')
t4 = t2 + t3
print(t4)

# Esercizio 7
# Verificare la lunghezza della tupla precedente.

print(len(t4))

# Esercizio 8
# Creare una tupla contenente i numeri interi da 1 a 5.

tupla_numeri = (1, 2, 3, 4, 5)
print(tupla_numeri)

# Esercizio 9 (difficile)
# Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.

# argomento non ancora studiato

# Esercizio 10
# Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

t4.count('mela')
