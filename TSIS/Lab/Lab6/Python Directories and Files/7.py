#Write a Python program to copy the contents of a file to another file
with open('c:/pp2/TSIS/Lab/Lab6/Python Directories and Files/text.txt', 'r') as f:
    content = f.read()

with open('c:/pp2/TSIS/Lab/Lab6/Python Directories and Files/output.txt', 'w') as k:
    k.write(content)