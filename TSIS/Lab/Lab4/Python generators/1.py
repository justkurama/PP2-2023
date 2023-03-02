x = int(input())
def gen(n):
    for i in range(1, n+1):
        yield i*i
g = gen(x)
for i in g: 
    print(i, end=" ")