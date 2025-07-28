class Calculator:
    def add(self, *args):
        return  sum(args)
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if a and b == 0:
            raise "Don't enter a zero"
        return print("dont enter 0:", a / b)

calc = Calculator()
print(calc.subtract(10, 5.5))
print(calc.divide(10, 0 ))