class Parrot:

    #class atrribute
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot("Blu", 10)
print("Blu is a {}".format(blu.species))
print("Blu is {} years old".format(blu.age))