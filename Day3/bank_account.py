class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount    
        
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance -= amount
        
    def show_balance(self):
        print(f"{self.owner}'s balance is {self.balance}")
        
account = BankAccount("Zuhra", 100)

account.deposit(50)
account.withdraw(30)
account.show_balance()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


student = Student("Zuhra", 25)
student.introduce()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def describe(self):
        print(f"Book title is {self.title}, author is {self.author}, and it has {self.pages} pages.")
        
book1 = Book("Python Basics", "Ali", 200)
book1.describe()