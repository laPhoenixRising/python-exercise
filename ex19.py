def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Tu hai {cheese_count} formaggini!")
    print(f"Tu hai {boxes_of_crackers} scatole di cracker!")
    print("Fantastico, è quanto basta per fare un party!")
    print("Prendi una coperta.\n")


print("Possiamo passare i numeri direttamente alla funzione:")
cheese_and_crackers(20, 30)


print("Oppure, possiamo usare le variabili del nostro programma:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Possiamo anche fare dei calcoli matematici all'interno:")
cheese_and_crackers(10 + 20, 5 + 6)


print("E possiamo combinare le due cose, variabili e calcoli:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)