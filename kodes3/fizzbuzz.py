n = int(input("Enter the number: "))
#if n <= 0:
 #   print("insert only positive numbers")
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("fizz")
elif n % 5 == 0:
    print("buzz")
        z