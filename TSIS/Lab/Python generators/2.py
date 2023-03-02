x = int(input())
def gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
g = gen(x)
for i in g: 
    print(i, end=" ")