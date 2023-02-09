#Переставить два слова
a = input()
fw = a[:a.find(' ')]
aw = a[a.find(' ') + 1:]
print(aw + ' ' + fw)