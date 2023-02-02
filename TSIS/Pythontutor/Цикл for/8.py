#Сумма факториалов
a =int(input())
f, sum = 1, 0
for i in range(1, a+1):
    f *= i
    sum += f
print(sum)