class Animal:
    def __init__(self):
        self.name = "A"

    def printName(self):
        print(self.name)

class Tirnaklilar:
    def __init__(self):
        self.tirnaksayisi = 4

class Cat(Animal, Tirnaklilar):
    def __init__(self):
        Tirnaklilar.__init__(self)
        Animal.__init__(self)

pamuk = Cat()
print(pamuk.tirnaksayisi)
pamuk.printName()