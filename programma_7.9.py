frase = "Quel ramo del lago di Como, che volge a mezzogiorno"
lettera = input("Che lettera dell'alfabeto devo trovare? ")
esito = 0
for carattere in range(len(frase)):
    if frase[carattere] == lettera and lettera != " ":
        print(f"Trovata {lettera} in posizione {carattere}")
        esito = 1
    elif lettera == " " and frase[carattere] == lettera:
        print(f"Trovato spazio in posizione {carattere}")
        esito = 1
if not esito:
    if lettera != " ":
        print(f"Non ho trovato {lettera} nella frase")
    elif lettera == " ":
        print("Non ho trovato alcun spazio nella frase")
                    



