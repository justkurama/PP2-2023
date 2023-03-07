#Write a Python program to insert spaces between words starting with capital letters.
import re
txt = input()
x = re.findall('[A-Z][^A-Z]*', txt)
text = ' '.join(x)
print(text)