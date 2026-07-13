import json

student = {
    "name": "zuhra",
    "age": 30
}

json_text = json.dumps(student)
print(json_text)
with open("student.csv", "w") as file:
    json.dump(student, file)

json_text = '{"name": "Zuhra", "age": 25, "city": "Kabul"}'
student = json.loads(json_text)
print(student)
print(student["name"])


profile = {
    "name": "Zuhra",
    "age": 25,
    "skill": "Python"
}

with open("profile.json", "w") as file:
    json.dump(profile, file)
    
with open("profile.json", "r") as file:
    reader = json.load(file)
    print(reader)