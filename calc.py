#Collins Omollo, SCT211-0021/2022
# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    else:
        return a / b

# Main program loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        else:
            print(f"Result: {divide(num1, num2)}")

        break
    else:
        print("Invalid choice. Please try again.")
