#Орёл или Решка? Ваша ставка:
import random
wincnt = 0
cnt = 0
restart =""
def Game():
    global wincnt, cnt, restart
    b = random.randint(0, 1)
    if b == 0 and a == "Орёл":
        wincnt += 1
        print("Верно!")
    elif b ==1 and a == "Решка":
        wincnt += 1
        print("Верно!")
    else:
        print("Не повезло!")
    restart = input('Хотите сыграть еще: ')

run = True
restart = "Да"
while run:
    if restart == "Да":
        cnt += 1
        a = input("Орёл или Решка? Ваша ставка: ")
        Game()
    else:
        run = False
        print("Сыгрыно :", cnt, "раз. Выиграли", wincnt, "раз." ) 