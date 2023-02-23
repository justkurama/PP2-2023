class Parent1:
    word1 = ''
    def __init__(self, color, number):
        self.color1 = color
        self.number1 = number
    def printInfo1(self):
        print(self.color1, self.number1)
    def setWord1(self, word):
        self.word1 = word
    def getWord1(self):
        print(self.word1)
class Parent2:
    word2 = ''
    def __init__(self, color, number):
        self.color2 = color
        self.number2 = number
    def printInfo1(self):
        print(self.color2, self.number2)
    def setWord2(self, word):
        self.word2 = word
    def getWord2(self):
        print(self.word2)
class Baby(Parent1, Parent2):
    def __init__(self, color1, color2, number1, number2):
        Parent1.__init__(self, color1, number1)
        Parent2.__init__(self, color2, number2)
        self.color3 = self.color1 + " " + self.color2
        self.number3 = self.number1 + self.number2
    def printColar3(self):
        print(self.color3)
    def printWord3(self):        
        b.setWord1("abc") 
        b.setWord2("def")
        print(self.word1 + self.word2)
    def printNumber3(self):
        print(self.number3)
b = Baby("green", "blue", 4, 5)
b.printWord3()
b.printColar3()
b.printNumber3()