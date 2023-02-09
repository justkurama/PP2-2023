#Второй максимум
fmax = int(input())
smax = int(input())
if fmax < smax:
    fmax, smax = smax, fmax
i = int(input())
while i != 0:
    if i > fmax:
        smax, fmax = fmax, i
    elif i > smax:
        smax = i
    i = int(input())
print(smax)