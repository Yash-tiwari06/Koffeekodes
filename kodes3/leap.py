def get_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("enter the year: "))
if get_leapyear(year):
    print("this is a leap year")
else:
   print("you entered a invalid year")