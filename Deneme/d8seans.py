class Calisan:
    def __init__(self, ad, maas):
        self.ad = ad
        self.maas = maas

    def __str__(self):
        return (f"AD: {self.ad} Maas: {self.maas}")

    def __add__(self, other):
        return self.maas + other.maas


class Guvenlik(Calisan):
    def __init__(self, ad, maas):
        super().__init__(ad, maas)
        self.mesai = 35

    def __str__(self):
        return (f"AD: {self.ad} Maas: {self.maas} Mesai: {self.mesai}")


cal1 = Calisan("Adem", 10000)
guv1 = Guvenlik("Ahmet", 5000)
print(guv1)
print(cal1 + guv1)
