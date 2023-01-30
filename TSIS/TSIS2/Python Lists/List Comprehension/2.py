fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)