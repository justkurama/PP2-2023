#Write a Python program to print yesterday, today, tomorrow.
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print(yesterday)
print(date.today())
print(tomorrow)