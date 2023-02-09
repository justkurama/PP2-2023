#Среднее значение последовательности
sum = 0
n = 0
i = int(input())
while i != 0:
    sum += i
    n += 1
    i = int(input())
print(sum / n)