import json

contenuto = {
    "first_name": "Francesca",
    "last_name": "Colombo",
    "age": 36 
    }

file_json = json.dumps(contenuto) 
#print(file_json)
file = open("sample.json", "w")

file.write(file_json)

file.close()

file = open("sample.json")
print(file.read())
file.close()