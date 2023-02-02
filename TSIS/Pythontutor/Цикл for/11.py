#Потерянная карточка
n = int(input())
sum1 = sum2 = 0
for i in range(n-1):
    a = int(input())
    sum1 += a
for i in range(1, n+1):
    sum2 += i
print(sum2 - sum1)