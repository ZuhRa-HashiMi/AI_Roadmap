class Vehicle:
    def start(self):
        print("Vehicle started")
        
    
class Car(Vehicle):
    def start(self):
        print("Car started")
        
        
car = Car()
car.start()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Zuhra", 25)
print(student)