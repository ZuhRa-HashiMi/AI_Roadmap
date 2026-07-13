import csv
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["zuhra", 25, "kabul"])
    writer.writerow(["Shakir", 30, "Kabul"])
    
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
        
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
        
        
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(f"{row["name"]} live in {row["city"]}")
        
        
students = [
    {"name": "Nilofer", "age": 25},
    {"name": "Yaseen", "age": 30}
]

with open("student.csv", "w", newline="") as file:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader
    writer.writerows(students)
    

with open("skills.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["skill", "level"])
    writer.writerow(["Python", "Beginner"])
    writer.writerow(["Java", "Intermediate"])
    writer.writerow(["AI", "Beginner"])