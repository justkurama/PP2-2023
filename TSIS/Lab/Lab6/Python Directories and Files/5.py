#Write a Python program to write a list to a file.
mylist = ['AVENGERS,', 'ASSEMBLE', "!"]

with open("c:/pp2/TSIS/Lab/Lab6/Python Directories and Files/text.txt", "w") as f:
    for i in range(len(mylist)):
        f.write(mylist[i] + ' ')