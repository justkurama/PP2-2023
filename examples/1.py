mylist = []
run = True
while run:
    x = input("\"end\" to quit")
    if x.isdigit():
        mylist.append(x)
    if x == ("end"):
        run = False
        break
mylist.sort()
print(mylist)