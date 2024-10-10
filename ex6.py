types_of_people = 10
x = f"Esistono {types_of_people} tipi di persone."

binary = "il codice binario"
do_not = "non lo conosco"
y = f"Quelle che conoscono {binary} e quelle che {do_not}."

print(x)
print(y)

print(f"Ho detto: {x}")
print(f"Ho anche detto: '{y}'")

hilarious = False
joke_evaluation = "Questa battuta è divertente?! {}"

print(joke_evaluation.format(hilarious))

w = "Questa è la parte sinistra di..."
e = "una stringa che ha una parte destra"

print(w + e)
