def area_cerchio(raggio):
    import math
    return math.pi*raggio**2

raggio = int(input("Inserisci il raggio "))
print(f"L'area del cerchio è uguale a {area_cerchio(raggio)}")
    