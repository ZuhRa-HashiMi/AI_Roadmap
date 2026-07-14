class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name}: ${self.price}"
    
    def __add__(self, other):
        return self.price + other.price
    
    def __mul__(self, quantity):
        return self.price * quantity
    
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
    
    
product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 20)
product3 = Product("Laptop", 1000)

print(product1)
print(product1 + product2)
print(product2 * 3)
print(product1 == product3)

class Score:
    def __init__(self, points):
        self.points = points
        
    def __str__(self):
        return f"Score: {self.points}"    
    
    def __add__(self, other):
       return Score(self.points + other.points)
   
    def __mul__(self, number):
       return Score(self.points * number)
    
    def __eq__(self, value):
        return self.points == value.points
score1 = Score(10)
score2 = Score(20)

print(score1)
print(score1 + score2)
print(score1 * 5)
print(score1 == score2)