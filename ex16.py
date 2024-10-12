from sys import argv

script, filename = argv

print(f"Sto per cancellare {filename}.")
print("Se non desideri procedere, premi CRTL-C (^C).")
print("Se desideri procedere, premi RETURN.")

input("?")

print("Sto aprendo il file...")
target = open(filename, "w")

print("Sto svuotando il file. Addio!")
target.truncate()

print("Ora ti chiederò di inserire tre righe di testo.")

line1 = input("Riga 1: ")
line2 = input("Riga 2: ")
line3 = input("Riga 3: ")

print("Scriverò queste righe nel file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("E alla fine, lo chiudo.")
target.close()