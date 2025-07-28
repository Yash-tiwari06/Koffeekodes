from collections import Counter
def first_non_repeating_char(s):
    count = Counter(s)

    for char in s:
        if count[char] == 1:
            return char

my_string = "stress"
result = first_non_repeating_char(my_string)
print(result)