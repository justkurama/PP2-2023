#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.
import os
path = 'c:/pp2/TSIS/Lab/Lab6/Python Directories and Files/text.txt'
if os.path.exists(path):
    os.remove(path)