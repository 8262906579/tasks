# Simple calculator with basic arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to execute the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Validate input choice
    if choice in ['1', '2', '3', '4']:
        try:
            # Input numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform operation based on user choice
            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid operation.")

# Run the calculator
calculator()



