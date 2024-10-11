from sys import argv

script, user_name = argv
prompt = '> '

print(f"Ciao {user_name}, io sono il programma {script}.")
print("Mi piacerebbe farti qualche domanda.")
print(f"Ti piaccio, {user_name}?")
likes = input(prompt)

print(f"Dove vivi {user_name}?")
lives = input(prompt)

print("Che tipo di computer hai?")
computer = input(prompt)

print(f"""
Va bene, hai risposto {likes} quando ti ho chiesto se ti piacevo.
Vivi a {lives}. Non sono sicuro di sapere dove si trovi.
E hai un computer {computer}. Ottimo
""")