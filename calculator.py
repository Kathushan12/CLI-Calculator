import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Cannot divide by 0" if y == 0 else x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(int(x))

def sine(x):
    return math.sin(math.radians(x))  # convert to degrees

def cosine(x):
    return math.cos(math.radians(x))

def logarithm(x):
    return math.log(x)

def absolute(x):
    return abs(x)

while True:
    print("\n--- Enhanced CLI Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    print("5. Modulus\n6. Power\n7. Square Root\n8. Factorial")
    print("9. Sine\n10. Cosine\n11. Logarithm\n12. Absolute Value")
    print("13. Exit")

    choice = input("Enter choice (1-13): ")

    if choice == '13':
        print("Exiting calculator.")
        break

    if choice in ['7', '8', '9', '10', '11', '12']:
        num = float(input("Enter number: "))
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    elif choice == '6':
        print("Result:", power(num1, num2)) 
    elif choice == '7':
        print("Result:", square_root(num))
    elif choice == '8':
        print("Result:", factorial(num))
    elif choice == '9':
        print("Result:", sine(num))
    elif choice == '10':
        print("Result:", cosine(num))
    elif choice == '11':
        print("Result:", logarithm(num))
    elif choice == '12':
        print("Result:", absolute(num))
    else:
        print("Invalid input")