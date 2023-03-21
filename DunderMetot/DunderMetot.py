class Sinif():
    def __init__(self, dersAdi):
        self.adi = dersAdi
        self.ogrenciler = []

    def __str__(self):
        return \
                self.adi + ' ' \
                + str(len(self.ogrenciler))

    def __add__(self, ogrenciAdi):
        self.ogrenciler.append(ogrenciAdi)

    def __sub__(self, ogrenciAdi):
        self.ogrenciler.remove(ogrenciAdi)

    def __len__(self):
        return len(self.ogrenciler)


class UniversiteSinifi(Sinif):
    def __init__(self, dersAdi):
        super().__init__(dersAdi)


class LiseSinifi(Sinif):
    def __init__(self, dersAdi):
        super().__init__(dersAdi)


mathClass = Sinif("Matematik")
mathClass + "Aysegul Hanim"
mathClass + "Yilmaz Bey"
mathClass + "Yunus"
print(mathClass)

mathClass - "Yunus"
print(mathClass)

print(len(mathClass))

# phyClass = UniversiteSinifi("Fizik")
# print(phyClass)
#
# litClass = LiseSinifi("Edebiyat")
# print(litClass)