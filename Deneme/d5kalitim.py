class Calisan:
    def __init__(self, isim, maas, departman):
        print("Calisan sinifi yapici fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Calisan bilgileri gosteriliyor")
        print("Isim : ", self.isim, "Maas : ", self.maas, "Departman : ", self.departman)

    def maasa_zam_yap(self, zam_miktari):
        print("Maasa zam yapildi")
        self.maas += zam_miktari

    def departman_degistir(self, yeni_departman):
        print("Departman degisiyor")
        self.departman = yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        print("Yonetici sinifi calisiyor")
        super().__init__(isim, maas, departman)
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self):
        print("Yonetici bilgileri gosteriliyor")
        print("Isim : ", self.isim, "Maas : ", self.maas, "Departman : ", self.departman, "Sorumlu Kisi Sayisi", self.kisi_sayisi)

yonetici = Yonetici("Adem", 2500, "Arge", 25)
yonetici.maasa_zam_yap(500)
yonetici.bilgileri_goster()
yonetici.departman_degistir("Insan Kaynaklari")
yonetici.bilgileri_goster()
