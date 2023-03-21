class Insan:
    def __init__(self, isim, telefon, dogum_tarihi):
        self.isim = isim
        self.telefon = telefon
        self.dogum_tarihi = dogum_tarihi

    def bilgiYazdir(self):
        print(f"{self.isim} isimli kisinin telefon nosu  {self.telefon}, dogum tarihi {self.dogum_tarihi} dur.")



    def yas_hesapla(self):
        self.yas = 2023 - self.dogum_tarihi
        return self.yas

class Ogrenci(Insan):
    def __init__(self, isim, telefon, dogum_tarihi, ogrno):
        super().__init__(isim, telefon, dogum_tarihi)
        self.ogrno = ogrno
        self.transkript = "Mevcut"
        self.notlar = []


    def ortalama(self):
        note1 = int(input("Not1 giriniz."))
        note2 = int(input("Not2 giriniz."))
        note3 = int(input("Not3 giriniz."))

        print("Ortalamaniz", (note1+note2+note3)/3)

    def bilgiYazdir(self):
        print(f"{self.isim} isimli ogrencinin telefon nosu  {self.telefon}, dogum tarihi {self.dogum_tarihi} ve ogrenci nosu {self.ogrno} dur.")


class Prof(Insan):
    def __init__(self, isim, telefon, dogum_tarihi, maas):
        super().__init__( isim, telefon, dogum_tarihi)
        self.maas = maas
    def __str__(self):
        return (f"Ad:{self.isim} Tlf: {self.telefon} Dogum Tarihi: {self.dogum_tarihi} Maas: {self.maas}")

ogr1 = Ogrenci ("Adem", 532, 1982, 162)

ogr1.ortalama()
"""prof1 =Prof("Ali", 532555, 1955, 5897)
print(prof1)
print(ogr1.yas_hesapla())
print(ogr1.bilgiYazdir())
print(prof1.maas)
print(prof1.yas_hesapla())"""
