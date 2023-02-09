#Количество четных элементов последовательности
evens = -1
i = -1
while i != 0:
    i = int(input())
    if i % 2 == 0:
        evens += 1
print(evens)