'''def get_top_student(student_scores):
    top_student = max(student_scores, key=student_scores.get)
    return top_student

student = {
    'arpit': 85,
    'bobby': 92,
    'yash': 78, 
    'dolly': 88
}
top = get_top_student(student)
print(top)

# que 2:
names = ["Alice", "Bob", "Charlie", "David"]
name_lengths = {name: len(name) for name in names}

print("Name lengths dictionary:", name_lengths)

# que 3:

def common_key_value_pairs(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}        

result = common_key_value_pairs(dict1, dict2)
print("Common key-value pairs:", result)'''

#que 4:

products = {
    "burger": 40,
    "pizza": 120,
    "pasta": 60,
    "sandwich": 35,
    "cold Drink": 40
}
print("show all available products-->")
print(products)
product_name = input("Enter the product name to search: ").lower()

if product_name in products:
    print(f" is available at Rs.{products[product_name]}")
else:
    print(f"Sorry, {product_name} is not available.")