from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Sto copiando da {from_file} a {to_file}")

# Queste due operazioni potrebbero essere eseguite su una sola riga, come?
in_file = open(from_file)
indata = in_file.read()

print(f"Il file di input è grande {len(indata)} byte")

print(f"Il file di output esiste? {exists(to_file)}")
print("Sono pronto; premi INVIO per continuare oppure CTRL-C per annullare.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Bene, tutto fatto.")

out_file.close()
in_file.close()