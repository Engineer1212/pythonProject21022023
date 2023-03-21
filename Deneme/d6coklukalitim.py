class Ogrenci:
    def dersCalis(self):
        print("Ogrenci ders calisiyor")

class Calisan():
    def calis(self):
        print("personel su an da calisiyor")

class Yazilimci(Ogrenci, Calisan):
    pass

yaz1 = Yazilimci()
yaz1.dersCalis()
yaz1.calis()