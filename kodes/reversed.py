def reversed_str(s):
    reversed_list = []
    for i in range(len(s) - 1, -1, -1):
        reversed_list.append(s[i])
    reversed_string = ''.join(reversed_list)
    print("reversed string is:", reversed_string)
    return reversed_string

print(reversed_str("hello"))