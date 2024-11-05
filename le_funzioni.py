def say_my_name():
    name = input("Come ti chiami? ")
    print("Il tuo nome è: ", name)

say_my_name()    


def addizione(a, b):
    print("Questa è la funzione addizione.")
    print("Fornisce la somma di due numeri passati come parametri.")
    risultato = a + b
    print("Il risultato dell'addizione è " + str(risultato))

addizione(5, 10)    
    

def laptop_nuovo(ram, cpu, antivirus=False):
    print("Il laptop nuovo avrà le seguenti caratteristiche:")
    print("RAM: " + ram)
    print("CPU: " + cpu)
    if antivirus == True:
        print("Hai comprato anche un antivirus.")

laptop_nuovo("16GB", "i7", antivirus=True)

def addizione(a, b):
    risultato = a + b 

risultato = addizione(3, 3)
print(risultato)
print(type(risultato))