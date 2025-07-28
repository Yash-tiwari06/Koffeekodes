'''
try:
    a = int(input("enter the number: "))
    b = int(input("enter the number: "))
    result = a / b
    print("Result: ", result)

except ZeroDivisionError:
    print("Error: division by zero is not allowed")'''

try:
    number = int(input("enter the number: "))
    print("you entered: ", number)
except ValueError:
    print("string is not allowed in input as integer")