password = "yash1234"
while True:
    user = input("enter correct password-->")
    if user != password:
        print("Try Again !!")
    else:
        print("Congrats, Your password is correct")
        break
