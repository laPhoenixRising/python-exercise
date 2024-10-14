file = open("Poesia", "w")
file.write("Ciao mondo")
file.close()

file = open("Poesia", "a")
file.write(" Come stai?")
file.close()

file = open("Poesia")
print(file.read())
file.close()