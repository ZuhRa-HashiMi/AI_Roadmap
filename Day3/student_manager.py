import json


class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["grade"]
        )


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def save_students(self):
        students_data = []

        for student in self.students:
            students_data.append(student.to_dict())

        with open("students.json", "w") as file:
            json.dump(students_data, file, indent=4)

        print("Students saved successfully!")

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                students_data = json.load(file)

            self.students = []

            for student_data in students_data:
                student = Student.from_dict(student_data)
                self.students.append(student)

            print("Students loaded successfully!")

        except FileNotFoundError:
            self.students = []
            print("No saved students found.")


manager = StudentManager()
manager.load_students()

while True:
    print("\nStudent Manager Menu")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Save and exit")

    choice = input("Choose an option: ")

    if choice == "1":
        student_id = int(input("Enter student ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        student = Student(student_id, name, age, grade)
        manager.add_student(student)

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        student_id = int(input("Enter student ID to search: "))
        found_student = manager.search_student(student_id)

        if found_student is not None:
            print(found_student)
        else:
            print("Student not found.")

    elif choice == "4":
        manager.save_students()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")