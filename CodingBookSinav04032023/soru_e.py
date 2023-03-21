class Sirket():
    def __init__(self, companyNo, name, city, service):
        self.companyNo = companyNo
        self.name = name
        self.city = city
        self.service = service
        self.vergiOrani = 0.20

class EgitimSirketi(Sirket):
    def __init__(self,companyNo, name, city, service):
        super().__init__(companyNo, name, city, service)
        self.vergiOrani = 0.05

sirk1= EgitimSirketi(44444,"Education","Ankara","Egitim")
print(sirk1.vergiOrani)