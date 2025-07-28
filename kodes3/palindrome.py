
def is_palindrome(s1):
    if len(s1) <= 1:
        return True
    if s1[0] != s1[-1]:
        return False
    return is_palindrome(s1[1:-1])
s1 = (input("Enter the String: "))
if is_palindrome(s1):
    print("given String is palindrome")
else:
    print("given string is not palindrome")