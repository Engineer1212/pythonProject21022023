class Isci:
    def maas(self):
        maas = 100
        zam_orani = 1.2
        print(maas * zam_orani)
isci1 = Isci ()
isci1.maas()

class Temizlik(Isci):
    def maas(self):
        maas = 100
        zam_orani = 1.5
        print(maas * zam_orani)

temiz1 = Temizlik()
temiz1.maas()
