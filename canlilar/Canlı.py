class Canli:
    def __init__(self, gidasi):
        self.gida = ""

    def solu(self):
        print("canli solumasi")


class Hayvan(Canli):
    def __init__(self):
        super().__init__("yemek")
