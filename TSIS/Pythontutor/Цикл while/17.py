#Максимальное число идущих подряд равных элементов
prev = -1
curr_rep_len = 0
max_rep_len = 0
i = int(input())
while i != 0:
    if prev == i:
        curr_rep_len += 1
    else:
        prev = i
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    i = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)