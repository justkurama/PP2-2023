mylist = []
run = True
while run:
    x = input()
    try:
        int(x)
        mylist.append(x)
    except: NameError
    if x == ("end"):
        run = False
        break
mylist.sort()
print(mylist)