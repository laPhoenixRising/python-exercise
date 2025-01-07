import random
numero = random.randint(1,10)
numeroUtente = 0
tentativi = 1
print("Ho pensato a un numero da 1 a 10.\nHai a disposizione 5 tentativi per indovinarlo.")
while numeroUtente != numero:
    numeroUtente = int(input("Prova a indovinarlo "))
    tentativi += 1
    if tentativi > 5:
        print("Mi spiace, non hai indovinato!")
        break
    if numeroUtente == numero:
        print(f"Bravo! Indovinato! Era proprio {numero}")
        break
    elif numeroUtente > numero:
        print("Troppo grande, mi spiace non hai indovinato.")
    elif numeroUtente < numero:
        print("Troppo piccolo, mi spiace non hai indovinato.")         
