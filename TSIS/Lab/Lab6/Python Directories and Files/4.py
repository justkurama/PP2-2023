#Write a Python program to count the number of lines in a text file.
import os

path = 'c:/pp2/TSIS/Lab/Lab5/row.txt'
with open( path , 'r', encoding='UTF8') as f:
    lines = f.readlines()
    print(len(lines))