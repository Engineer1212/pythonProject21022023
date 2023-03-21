#multiple inheritance
class Animal:
    def __init__(self):
        self.name = "Animal"

class Violent:
    def __init__(self):
        self.tirnaksayisi= 4

class Cat(Animal, Violent):
    def __init__(self):
        Animal.__init__(self)
        Violent.__init__(self)
        self.color = "black"


pamuk = Cat()
print(pamuk.name)