class Parent:
    def __init__(self, word, color, number):
        self.word1 = word
        self.color1 = color
        self.number1 = number
    def printInfo1(self):
        print(self.color1, self.number1)
    def printInfo2(self):
        print(self.word1)


p1 = Parent(input("Word1 "), input("Color1 "), int(input("Number1 ")),)
p2 = Parent(input("Word2 "), input("Color2 "), int(input("Number3 ")),)

class Baby(Parent):
    def __init__(self, word, color, number):
        super().__init__(word, color, number)
    def printColar3(self):
        print(p1.color1 + " " + p2.color1)
    def printWord3(self):
        print(p1.word1 + p2.word1)
    def printNumber3(self):
        print(p1.number1 + p2.number1)

#Outputs
p1.printInfo2()
p1.printInfo1()
p2.printInfo2()
p2.printInfo1()
b = Baby(" ", " ", 0)
b.printWord3()
b.printColar3()
b.printNumber3()