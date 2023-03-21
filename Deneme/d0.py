class İnsan:
    def __init__(self,isim,tel,dogumt):
        self.isim = isim
        self. tel = tel
        self.dogumt = dogumt
    def yas_soyle(self):
        return "Yaş: " , (2023 - self.dogumt)

class Ogrenci(İnsan):
    def __init__(self,isim,tel,dogumt,ogr_no):
        super().__init__(isim,tel,dogumt)
        self.ogr_no = ogr_no
        self.transkript = "mevcut"
        self.notlar = []
    def not_ekle(self):
        for i in range(3):
            note = int(input("3 not giriniz:"))
            self.notlar.append(note)
        print(self.notlar)
    def ort(self):
        return sum(self.notlar) / len(self.notlar)
    def __str__(self):
        return(f"AD:{self.isim} Tel:{self.tel} DogumTarihi:{self.dogumt} Ogrneci Numarası:{self.ogr_no} Transkript:{self.transkript}")
ogr1 = Ogrenci("yunus",521,1999,1378)
# print(ogr1)
class Prof(İnsan):
    def __init__(self,isim,tel,dogumt,maas):
        super().__init__(isim,tel,dogumt)
        self.maas = maas
ogr1.not_ekle()
print(ogr1.ort())