#Количество элементов, равных максимуму
max = 0
cnt = 0
i = -1
while i != 0:
    i = int(input())
    if i > max:
        max, cnt = i, 1
    elif i == max:
        cnt += 1        
print(cnt)