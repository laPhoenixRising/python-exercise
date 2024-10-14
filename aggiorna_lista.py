file = open("Esempio.json")
a = file.read()
file.close()

#print(a)

import json

b = json.loads(a)

b.append(78)

c = json.dumps(b)

file = open("Esempio.json", "w")
file.write(c)
file.close()