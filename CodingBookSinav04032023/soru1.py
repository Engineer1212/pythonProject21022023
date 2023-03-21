class Sirket:
    def __init__(self, companyNo, name, city, service):
        self.companyNo =companyNo
        self.name = name
        self.city = city
        self.service = service
        self.sirket_listesi = []

    def __str__(self):
        return (f"Sirket No: {self.companyNo} Sirket Adi: {self.name} Sirket ili: {self.city} Servis : {self.service}")

    def listele(self):
        return self.sirket_listesi
    def sirket_ekle(self, sirket):
        self.sirket_listesi.append(sirket)
    def sirket_sil(self, companyNo):
        for i, sirket in enumerate(self.sirket_listesi):
            if sirket.companyNo == companyNo:
                del self.sirket_listesi[i]
                print("Belirtmiş olduğunuz sirket kayıtlarından silindi..")
                return
            else:
                print("Girmiş olduğunuz Sirket No kayıtlarda bulunamadı..")
                break
"""srk1 =Sirket("1111", "Humanity Bank", "Newyork", "Banking" )
print(srk1)"""


def main():
    while True:
        user_input = input("Seçim Yapınız (l: Sirketleri listele, a: Sirket Ekle, r: Sirket sil, q: Çıkış): ")
        if user_input == "l":
            sirketler = Sirket.listele()
            if len(sirketler) == 0:
                print("Sirket kayıtlarda bulunamadı..")
            else:
                for sirket in sirketler:
                    print(
                        f"Sirket No: {sirket.companyNo}, Sirket Adı: {sirket.name}, Sirket Sehri: {sirket.city}, Servis: {sirket.service}")
        elif user_input == "a":
            companyNo = input("Sirket No giriniz")
            name = input("Sirket adı giriniz... ")
            city = input("Sirketin faaliyette bulundugu sehri giriniz.. ")
            service = input("Sirketin faaliyet alanini giriniz ... ")
            sirket = Sirket(companyNo, name, city, service)
            sirket.sirket_ekle(sirket)
            print("Girdiğiniz sirket kayitlara başarı ile eklendi.")
        elif user_input == "r":
            companyNo = input("Silmek istediğiniz sirketin kodunu giriniz... ")
            sirket.sirket_sil(companyNo)

        elif user_input == "q":
            break
        else:
            print("Hatalı seçim yaptınız. Lütfen belirtilen harflerden birini seçiniz..")


if __name__ == "__main__":
    main()