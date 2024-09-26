# Esercizio 1
# Creare una lista vuota e assegnarla a una variabile.

vuota = []
print(vuota)

# Esercizio 2
# Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.

numeri = [1, 2, 3, 4, 5]
print(numeri)

# Esercizio 3
# Accedere all'elemento con indice 2 della lista precedente.

print(numeri[2])

# Esercizio 4
# Aggiungere un nuovo elemento "6" alla lista precedente.

numeri.append(6)
print(numeri)

# Esercizio 5
# Rimuovere l'elemento con indice 3 dalla lista precedente.

numeri.pop(3)
print(numeri)

# Esercizio 6
# Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.

nuovi_numeri = list(numeri[0:3])
print(nuovi_numeri)

# Esercizio 7
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.

dispari = numeri[1::2]
print(dispari)

# Esercizio 8
# Ordinare la lista precedente in ordine decrescente.

numeri.reverse()
print(numeri)

# Esercizio 9
# Contare quante volte l'elemento "2" appare nella lista precedente.

print(numeri.count(2))