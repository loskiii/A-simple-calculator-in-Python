class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero is undefined."


# Example usage
calculator = Calculator()

# Addition
print("3 + 4 =", calculator.add(3, 4))

# Subtraction
print("8 - 5 =", calculator.subtract(8, 5))

# Multiplication
print("2 * 6 =", calculator.multiply(2, 6))

# Division
print("10 / 2 =", calculator.divide(10, 2))
print("10 / 0 =", calculator.divide(10, 0))

