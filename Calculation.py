# Calculations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("A) Add")
print("B) Subtract")
print("C) Multiply")
print("D) Divide")

while True:

    choice = input("Enter choice(A/B/C/D): ")

    if choice in ('A', 'B', 'C', 'D'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))

