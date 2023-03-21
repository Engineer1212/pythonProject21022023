class Calisan:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.email = isim.lower() + soyisim.lower() + "@sirket.com"
        self.maas = maas


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, uzmanlik):
        super().__init__(isim, soyisim, maas)
        self.uzmanlik = uzmanlik


class Idareci(Calisan):
    def __init__(self, isim, soyisim, maas, yetki):
        super().__init__( isim, soyisim, maas)
        self.yetki = yetki


cal1 = Calisan("Adem", "SAV", 10000)
print(cal1.email)
yaz1 = Yazilimci("Ahmet", "SAV", 10000, "python")
print(yaz1.uzmanlik)
mdr1 = Idareci ("Salih", "Kaya", 7895, "Arge")
print(mdr1.yetki)
print(mdr1.email)
