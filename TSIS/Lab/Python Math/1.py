#Write a Python program to convert degree to radian.
from math import pi, radians
g = int(input("Input degree: "))
rad = (g * pi)/180 
rad = radians(g)
rad = round(rad, 6)
print("Output radian:", rad)