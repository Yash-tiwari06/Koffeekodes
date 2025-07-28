'''def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
#
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%1 == 0:
            return False
    return True
print(check_prime(3))'''

year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year. ")
else:
    print(f"{year} is not a leap year. ")