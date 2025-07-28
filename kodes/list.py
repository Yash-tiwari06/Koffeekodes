'''
#que 1:
def get_even_list(lst):
    even_num = []
    for num in lst:
        if num%2 ==0:
            even_num.append(num)
    return even_num
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_list(list))

#que 2:

names = ['arpit', 'bobby', 'chiku', 'dolly']
names.sort(reverse=False)
print(names)

#que 3:

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqred_list=[]
for i in l1:
    sqred_list.append(i**2)
print(sqred_list)

#que 4:
l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
l4 = []
for i in l2:
    if i in l3:
        l4.append(i)
    print(l4)

#que 5:
def rev_list(lst):
    reversed = []
    for i in range((len)(lst) -1, -1, -1):
        reversed.append(i)
    return reversed
list = [1, 2, 3, 4, 5]
print(rev_list(list))

#que 6:

l5 = [1, 2, 3, 4, 5]
l6 = [4, 5, 6, 7, 8]
l7 = []
for i in l5:
    if i not in l6:
        l7.append(i)
    print(l7)
'''
