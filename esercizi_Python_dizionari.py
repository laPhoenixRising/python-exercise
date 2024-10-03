# Esercizio 1
# Creare un dizionario vuoto e assegnarlo a una variabile.

dizionario = {}
print(dizionario)

# oppure

dizionario = DICT()
print(dizionario)

# Esercizio 2
# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.

dizionario = {'nome': 'Mario', 'cognome': 'Rossi', 'età': 30}
print(dizionario)

#oppure

dizionario = {}
dizionario['nome'] = 'Mario'
dizionario['cognome'] = 'Rossi'
dizionario['età'] = 30
print(dizionario)

# Esercizio 3
# Accedere al valore dell'elemento con chiave "età" del dizionario precedente.

print(dizionario['età'])

# Esercizio 4
# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.

dizionario['email'] = 'mario.rossi@email.com'
print(dizionario)

# Esercizio 5
# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.

del dizionario['cognome']
print(dizionario)

# Esercizio 6
# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.

chiavi = list(dizionario.keys())
print(chiavi)

# Esercizio 7
# Creare una nuova lista che contenga solo i valori del dizionario precedente.

valori = list(dizionario.values())
print(valori)

# Esercizio 8
# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.

dizionario.update({'età': 35})
print(dizionario)

# Esercizio 9
# Contare il numero di elementi nel dizionario precedente.

print(len(dizionario)