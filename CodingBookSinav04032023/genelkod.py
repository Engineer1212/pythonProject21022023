class Sirket():
    def __init__(self, companyNo, name, city, service):
        self.companyNo = companyNo
        self.name = name
        self.city = city
        self.service = service


class Sirketler:
    def __init__(self):
        self.sirket_listesi = []

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
                print("Girmiş olduğunuz sirket kodu bulunamadı..")
                break


def main():
    sirketlerr = Sirketler()
    while True:
        user_input = input("Seçim Yapınız (l: Sirketleri listele, a: Sirket Ekle, r: Sirket sil, q: Çıkış): ")
        if user_input == "l":
            sirketler = sirketlerr.listele()
            if len(sirketler) == 0:
                print("Kayitlarda herhangibir sirket bulunamadı..")
            else:
                for sirket in sirketler:
                    print(
                        f"Sirket No: {sirket.companyNo}, Sirket Adı: {sirket.name}, Sehir: {sirket.city}, Faaliyet Alani: {sirket.city}")
        elif user_input == "a":
            companyNo = input("Sirket Kodu giriniz... ")
            name = input("Sirket adı giriniz... ")
            city = input("Sirket ili giriniz.. ")
            service = input("Faaliyet Alani giriniz ... ")
            sirket = Sirket(companyNo, name, city, service)
            sirketlerr.sirket_ekle(sirket)
            print("Girdiğiniz sirket kayitlara başarı ile eklendi.")
        elif user_input == "r":
            companyNo = input("Silmek istediğiniz sirketin kodunu giriniz... ")
            sirketlerr.sirket_sil(companyNo)

        elif user_input == "q":
            break
        else:
            print("Hatalı seçim yaptınız. Lütfen belirtilen harflerden birini seçiniz..")


if __name__ == "__main__":
    main()
