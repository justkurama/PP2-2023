a = input()
b = a[::-1]
sum1 = 0
sum2 = 0
for i in range(len(a) // 2):
    sum1 += int(a[i])
for i in range(len(b) // 2):
    sum2 += int(b[i])

if sum1 == sum2:
    print("Счастливый билет!")
else:
    print("Простой билет!")