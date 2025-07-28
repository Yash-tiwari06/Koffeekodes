
'''
#que 1:
def fun(name, age, city):
    return (name, age, city)
person_info = fun("yash", 21, "noida")
name, age, city = person_info

print("Name:", name)
print("Age:", age)
print("City:", city)

#que 2:

def combine_unique(t1, t2):
    combined = t1 + t2
    result = []
    for item in combined:
        if item not in result:
            result.append(item)
    return tuple(result)
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
print("Combined (order preserved):", combine_unique(tuple1, tuple2))

#que 3:
t1 = ("apple", "banana", "cherry", "date", "elderberry")
print(t1[0:2:])
print(t1[-2::])

#que 4:
tup1=(1,2)
tup2=(3, 4)
tup3=(5,6)

combined_tup = tup1 + tup2 + tup3
print(combined_tup)

#que 5:
name=(input("Enter your name: "))
Age = int(input("Enter your age: "))
City = (input("Enter your city: "))
def tuple(name, Age, City):
    return (name, Age, City)
person_info = tuple(name, Age, City)
print("Name:", person_info[0])
print("Age:", person_info[1]) 
print("City:", person_info[2])  
print(type(person_info))'''

#que 6:
name = ('yash', 'sankalp', 'vishnu', 'mahesh')
Age = (21, 22, 23, 24)

paired_list = list(zip(name, Age))
print(paired_list)

