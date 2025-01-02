import random
numero = random.randint(1,10)
numeroUtente = 0
print("Ho pensato a un numero da 1 a 10.")
while numeroUtente != numero:
    numeroUtente = int(input("Prova a indovinarlo "))
    if numeroUtente == numero:
        print(f"Bravo! Indovinato! Era proprio {numero}")
        break
    elif numeroUtente > numero:
        print("Troppo grande, mi spiace non hai indovinato.")
    elif numeroUtente < numero:
        print("Troppo piccolo, mi spiace non hai indovinato.")         
