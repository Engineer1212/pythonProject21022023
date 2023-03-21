class Calisan:
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def __str__(self):
        return f"Ad:{self.ad} Soyad: {self.soyad} Maas: {self.maas}"

    def __add__(self, other):
        return ("Calisanlarin maas Toplami:", self.maas + other.maas)


class Yonetici(Calisan):
    def __init__(self, ad, soyad, maas, yetki):
        super().__init__(ad, soyad, maas)
        self.yetki = yetki

    def __str__(self):
        return f"Ad:{self.ad} Soyad: {self.soyad} Maas: {self.maas} Yetki: {self.yetki}"


cal1 = Calisan("Adem", "Sav", 5000)
yon1 = Yonetici("Ali", "Kaya", 6400, "Sinirsiz")

print(cal1)
print(yon1)
print(yon1 + cal1)