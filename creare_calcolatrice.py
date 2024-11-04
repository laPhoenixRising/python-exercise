from math import sqrt

hello_message = """
Benvenuti al programma calcolatrice!

Di seguito un elenco delle varie funzioni disponibili:

- Per effettuare un' Addizione, seleziona 1; 
- Per effettuare una Sottrazione, seleziona 2; 
- Per effettuare una Moltiplicazione, seleziona 3; 
- Per effettuare una Divisione, seleziona 4; 
- Per effettuare un Calcolo Esponenziale, seleziona 5; 
- Per effettuare una Radice Quadrata, seleziona 6; 
- Per uscire dal programma puoi digitare ESC; 
"""


while True:
    print(hello_message)

    action = input("Inserisci il numero corrispondente all'operazione da effettuare: ")

    if action == "1":
        print("\nHai scelto: Addizione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("Inserisci il secondo numero -> "))
        print("Il risultato dell'Addizione è: ", str(a + b))

    elif action == "2":
        print("\nHai scelto: Sottrazione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("Inserisci il secondo numero -> "))
        print("Il risultato della Sottrazione è: ", str(a - b))  

    elif action == "3":
        print("\nHai scelto: Moltiplicazione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("Inserisci il secondo numero -> "))
        print("Il risultato della Moltiplicazione è: ", str(a * b))       

    elif action == "4":
        print("\nHai scelto: Divisione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("Inserisci il secondo numero -> "))
        print("Il risultato della Divisione è: ", str(a / b))


    elif action == "5":
        print("\nHai scelto: Calcolo Esponenziale\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("Inserisci il secondo numero -> "))
        print("Il risultato del Calcolo Esponenziale è: ", str(a ** b))  

    
    elif action == "6":
        print("\nHai scelto: Radice Quadrata\n")
        a = float(input("Inserisci il numero -> "))
        print("Il risultato dell'operazione è: ", str(sqrt(a)))

    elif action == "ESC":
        print("\nL'applicazione verrà chiusa!\n")
        break    

    new_action = input("\nDesideri continuare ad utilizzare l'applicazione? S/N ")
    if new_action == "N" or new_action == "n":
        print("A presto!\n")
        break    

    print("Sto tornando al menù principale!\n")    

