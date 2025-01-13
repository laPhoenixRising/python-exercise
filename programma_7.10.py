frase = "Quel ramo del lago di Como, che volge a mezzogiorno"
lettera = input("Che lettera dell'alfabeto devo trovare? ")
esito = 0
pos = 0
for carattere in frase:
    pos += 1
    if carattere == lettera and lettera != " ":
        print(f"Trovata {lettera} in posizione {pos}")
        esito = 1
    elif lettera == " " and carattere == lettera:
        esito = 1
        print(f"Trovato spazio in posizione {pos}")
if not esito:
    if lettera != " ":
        print(f"Non ho trovato {lettera} nella frase")
    elif lettera == " ":
        print("Non ho trovato alcun spazio nella frase")
