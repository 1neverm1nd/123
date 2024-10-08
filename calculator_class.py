
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Usage example
calculator = Calculator()

print(calculator.add(10, 5))        # 15
print(calculator.subtract(10, 5))   # 5
print(calculator.multiply(10, 5))   # 50
print(calculator.divide(10, 5))     # 2.0
print(calculator.divide(10, 0))     # "Error: Division by zero"
