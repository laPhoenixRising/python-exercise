formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('uno', 'due', 'tre', 'quattro'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    'Prova a inserire',
    'Qui il tuo testo',
    'Magari una poesia',
    'O una canzone sulla paura'
))
