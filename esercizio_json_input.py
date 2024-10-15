file = open("input.json")
a = file.read()
file.close()

import json

b = json.loads(a)

name = input("Inserisci il nome: ")
age = input("Inserisci l'età: ")

dictionary = {"nome": name, "age": age}

b.append(dictionary)

c = json.dumps(b)

file = open("input.json", "w")
file.write(c)
file.close()