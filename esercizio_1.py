lista = []
n = input("Quanti numeri?")
n = int(n)
for x in range(n):
    m = input(f"inserire il numero {x+1}: ")
    m = int(m)
    lista.append(m)

input("Grazie.Premere invio per stampare la lista.")
i = 1
for el in lista:
    print(f"{i}: {el}")
    i += 1