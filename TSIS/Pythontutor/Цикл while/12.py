#Количество элементов, которые больше предыдущего
prev = int(input())
cnt = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        cnt += 1
    prev = next
print(cnt)