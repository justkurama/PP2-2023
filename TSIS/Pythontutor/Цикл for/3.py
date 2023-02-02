#Ряд - 3
a = int(input())
b = int(input())
for i in range(a - a%2, b - b%2, -2):
    print(i, end=" ")