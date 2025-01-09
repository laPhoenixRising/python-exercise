frase = "Quel ramo del lago di Como, che volge a mezzogiorno"
lettera = input("Che lettera dell'alfabeto devo trovare? ")
for carattere in range(len(frase)):
    if frase[carattere] == lettera:
        print(f"Ho trovato una {lettera} in posizione {carattere}")