#Write a Python program to calculate the area of regular polygon.
import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
#Area=1/2(ap), where a denotes the length of an apothem, and p denotes the perimeter.
p = n * l
a = (l/(2*math.tan(math.radians(180/n))))
s = (p*a)/2
s = int(s)
print("The area of the polygon is:", s)