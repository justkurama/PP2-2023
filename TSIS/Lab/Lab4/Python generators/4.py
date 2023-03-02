n = int(input())
squares = (i*i for i in range(n))

for x in squares:
  print(x, end=" ")
print()

for i in range(1, n+1):
    print(i*i, end=" ")

