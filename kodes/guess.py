'''
import random
secret_number = random.randint(1, 100)
while True:
    guess = int(input("enter your number: "))
    if guess < secret_number:
        print("too low, Try Again!")
    elif guess > secret_number:
        print("Too high, Try Again!")
    elif guess == secret_number:
        print("Hurrayy!, you guessed it right!")
        break
'''
# find largest
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

second_largest = None
for num in numbers:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num
print(second_largest)
