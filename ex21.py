def add(a, b):
    print(f"Somma {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Sottrazione {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Moltiplicazione {a} * {b}")
    return a * b 

def divide(a, b):
    print(f"Divisione {a} / {b}")
    return a / b


print("Facciamo due conti con le funzioni!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Età: {age}, Altezza: {height}, Peso: {weight}, QI: {iq}")


# Un rompicapo per il credito extra, scrivetelo comunque.
print("Ecco un rompicapo.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Che diventa: ", what, "Riuscite a farlo a mano?")
