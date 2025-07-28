def sum_positive(n):
    summ = 0
    for i in n:
        if i % 2 == 0:
            summ += i
    print(summ)
n=[1,2,3,4,5,6]
sum_positive(n)