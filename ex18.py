# questa assomiglia ai programmi che usano argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok. quell'*args in realtà è inutile, possiamo fare cosi
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# questa riceve solo un argomento
def print_one(arg1):
    print(f"arg1: {arg1}")

# questa non riceve nessuna argomento
def print_none():
    print("Non ho niente.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
first_name = "Zed"
last_name = "Shaw"
print_two_again(first_name, first_name)
print_one("Primo!")
print_none()
