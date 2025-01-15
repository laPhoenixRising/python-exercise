lista = []
n = input("Quanti numeri?")
n = int(n)
for x in range(n):
    m = input(f"inserire il numero {x+1}: ")
    m = int(m)
    lista.append(m)

print(lista)    