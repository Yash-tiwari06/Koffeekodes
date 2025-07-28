def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)
    total = sum(int(digit)**n for digit in num_str)
    return total == number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")