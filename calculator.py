
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("\nEnter your choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
        
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}\n")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}\n")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}\n")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}\n")

    except ValueError as e:
        print(f"\nError: {e}\n")

if __name__ == "__main__":
    calculator()