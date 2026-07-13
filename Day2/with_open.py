with open("day2.txt", "w") as file:
    file.write("Python is fun\n")
    file.write("I am learning AI")

with open("day2.txt", "r") as file:
    content = file.read()

print(content)