#Номер числа Фибоначчи
a = int(input())
if a == 0:
    print(0)
else:
    n1, n2 = 0, 1
    n = 1
    while n2 <= a:
        if n2 == a:
            print(n)
            break
        n1, n2 = n2, n1 + n2
        n += 1
    else:
        print(-1)