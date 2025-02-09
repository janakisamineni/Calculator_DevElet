def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    while True:
        print("\nSimple CLI Calculator")
        print("Options: +, -, *, /, exit")
        operation = input("Enter operation: ").strip()

        if operation.lower() == "exit":
            print("Exiting Calculator...")
            break

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please enter +, -, *, /")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
