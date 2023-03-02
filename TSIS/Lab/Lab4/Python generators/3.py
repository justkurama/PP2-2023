x = int(input())
def gen(n):
    for i in range(n):
        if i % 12 == 0:
            yield i
g = gen(x)
for i in g: 
    print(i, end=" ")