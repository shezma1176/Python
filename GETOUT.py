class Cat():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.energy = 100
        self.mood = "calm"

    def meow(self):
        print(f"{self.name} says: Meow!")

    def eat(self, food):
        self.energy += 20
        self.mood = "happy"
        print(f"{self.name} eats {food} and is very pleased")

my_cat = Cat("Piku", "Orange", 3)
my_cat.meow()
my_cat.eat("Treat")