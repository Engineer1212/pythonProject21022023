class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def aracBilgi (self):
        return (f"Araciniz {self.marka} marka , {self.model} model olup {self.yil} yilinda uretilmistir.")


araba1 = Araba("BMW","I5", 2016)

print(araba1.yil)
print(araba1.aracBilgi())

class Otobus(Araba):
    def __init__(self, marka, model, yil, koltukSayisi):
        super().__init__(marka, model, yil)
        self.koltukSayisi = koltukSayisi

    def aracBilgi (self):
        return (f"Otobusunuz {self.marka} marka , {self.model} model  {self.yil} yilinda uretilmis ve {self.koltukSayisi} yolcu kapasitesine sahiptir.")

bus1 = Otobus("Mercedes", "Travego", 2023, 45)
print(bus1.aracBilgi())