import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Enter the number: "))
    if guess < secret_number:
        print("you are too high to reach the number")
    elif guess > secret_number:
        print("you are too low to guess the number")
    else:
         print("hurrayyy, you guess right!!")
         break
