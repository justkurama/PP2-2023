import random
a = random.randint(1, 100)
b = int(input("Угадайте число: "))
cnt = 1
maxi = 6
i = 0
while a != b and i < maxi: 
    if a > b:
        b = int(input("Больше, Попытайтесь снова: "))
    else: 
        b = int(input("Меньше, Попытайтесь снова: "))
    cnt += 1
    i += 1
else :
    if a == b:
        print("Верно! Отгодали за", cnt, "попытык.")
    else:
        print("Попытки закончились. Верный ответ:", a)