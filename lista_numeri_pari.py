lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = []
for n in lista:
    if n % 2 == 0:
        pari.append(n)
        
for el in pari:
    print(f"{el}")    