a = input()
sum = 0
product = 1
for i in range(len(a)):
    sum += int(a[i])
    product *= int(a[i])
print("Sum:", sum)
print("Product:", product)
