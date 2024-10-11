from sys import argv

script, filename = argv

txt = open(filename)

print(f"Ecco il tuo file {filename}:")
print(txt.read())

print("Scrivi un'altra volta il nome del file:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())