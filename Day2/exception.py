def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b
print(divide_numbers(10, 2))    
    