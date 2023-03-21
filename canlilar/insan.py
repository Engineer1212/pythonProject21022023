from canlilar.Canlı import Canli


class Insan(Canli):
    def __init__(self):
        super().__init__("yemek")

    def solu(self):
        print("Insan solumasi")