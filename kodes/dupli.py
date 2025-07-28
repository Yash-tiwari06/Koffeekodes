l1 = [1, 2, 3, 3, 4, 4, 5]
l2 = [2, 3, 3, 4, 4, 5, 6]
l3=[]
for i in l1:
    if i in l2 and i in l1:
        l3.append(i)
print(l3)