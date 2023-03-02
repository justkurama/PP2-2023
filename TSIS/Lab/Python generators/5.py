n = int(input())
gen = (i for i in range(n))
x = reversed(gen)
for i in x:
  print(i)