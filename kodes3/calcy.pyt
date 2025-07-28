
def calc(a, b, c):
    a = int(input("enter the number: "))
    b = int(input("enter the number: "))
    c = input("enter the operator: ")
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        print(a / b)
    elif c == '*':
        print(a * b)
calc(a, b, c)

