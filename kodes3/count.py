l1 = [1, 2, 3, 4, 5, 6]
count = 0
for i in l1:
    count += 1
print(count)
# que2
l1 = [1, 2, 3, 4, 5, 6]
def count(n):
    if n == []:
        return 0
    else:
        return 1 + count(n[1:])

print(count(l1))
