#Минимум из трех чисел
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c: 
    print(a)
elif c < b and c < a:
    print(c)
elif b < a and b < c: 
    print(b)