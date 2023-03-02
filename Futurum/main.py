from random import randint
a = randint(1, 100)
b = int(input())
x = 6
win = 1
i = 0
while a != b and i < x:
    if a > b:
        b = int(input("Больше чем это:"))
    else:
        b = int(input("Меньше чем это:"))
    i += 1
    win +=1
else:
    if a == b:
        print("Вы угадали за ", win, "попыток.")
    else:
        print("Вы не угадали, верный ответ:", a)
