class Animal:
    def __init__(self):
        self.name ="A"
        print("animal")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("cat")


pamuk = Cat()
print(pamuk.name)