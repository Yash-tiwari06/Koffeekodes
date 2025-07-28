def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("kanak"))
print(is_palindrome("lavel"))  # True