#Индекс максимума последовательности
max = 0
max_index = -1
i = -1
n = 0
while i != 0:
    i = int(input())
    if i > max:
        max = i
        max_index = n
    n += 1
print(max_index)