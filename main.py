class kot:
    name = None
    age = None
    happiness = None
    def set_data(self, name, age, happiness):
        self.name = name
        self.age = age
        self.happiness = happiness
    def get_data(self):
        print('Name:', self.name, "Age:", self.age, "Happiness:", self.happiness)

cat1 = kot()
cat1.name = "Vasya"
cat1.age = 2
cat1.happiness = True

cat2 = kot()
cat2.set_data('Murka', 5, True)
print(cat1.name)
cat2.get_data()