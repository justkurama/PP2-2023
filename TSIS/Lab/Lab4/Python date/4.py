#Write a Python program to calculate two date difference in seconds.
from datetime import datetime
day1 = input("YYYY/MM/DD HH:MM:SS ")
day2 = input("YYYY/MM/DD HH:MM:SS ")


d1 = datetime.strptime(day1, "%Y/%m/%d %H:%M:%S")
d2 = datetime.strptime(day2, "%Y/%m/%d %H:%M:%S")


delta = d2 - d1
print(f'Difference is {delta.seconds} seconds')