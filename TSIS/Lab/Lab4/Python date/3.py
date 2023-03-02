#Write a Python program to drop microseconds from datetime.
from datetime import *
currenttime = datetime.today().replace(microsecond=0)
print(currenttime)