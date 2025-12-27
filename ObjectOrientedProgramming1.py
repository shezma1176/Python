# Creating Cat class
class Cat:
    # __init__ method
    def __init__(self, name):
        self.name = name

    # Method inside the class
    def introduce(self):
        print("Hello! I am", self.name)

# Creating objects of the class
Cat1 = Cat("Piku")
Cat2 = Cat("Tom")

# Calling the method using objects
Cat1.introduce()
Cat2.introduce()