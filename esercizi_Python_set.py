# Esercizio 1
# Creare un set vuoto e assegnarlo a una variabile.

s = set([])
print(s)

# oppure

s = {}
print(s) 

# Esercizio 2
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".

frutta = set(['mela', 'banana', 'kiwi', 'mela'])
print(frutta)

# oppure 

frutta = {'mela', 'banana', 'kiwi', 'mela'}
print(frutta)

# Esercizio 3
# Aggiungere l'elemento "pesca" al set precedente.

frutta.add('pesca')
print(frutta)

# Esercizio 4
# Rimuovere l'elemento "mela" dal set precedente.

frutta.remove('mela')
print(frutta)

# Esercizio 5
# Verificare se l'elemento "ananas" è presente nel set precedente.

'ananas' in frutta

# Esercizio 6
# Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".

frutti = {'banana', 'kiwi', 'arancia'}
print(frutti)

# Esercizio 7
# Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().

set(range(1,6))

# Esercizio 8 (difficile)
# Creare un nuovo set contenente i numeri pari del set precedente.

# ancora non in grado di eseguirlo