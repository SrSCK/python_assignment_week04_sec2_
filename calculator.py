def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide b zero")
    return a / b

a = int(9)
b = int(3)
print("Calculator")
print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))
