#Степень двойки
n = int(input())
i = 2
power = 1
while i <= n:
    i *= 2
    power += 1
print(power - 1, i // 2)