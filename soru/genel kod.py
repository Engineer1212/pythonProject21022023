class Holding:
    def __init__(self, companyNo, name, city, service):
        self.companyNo = companyNo
        self.name = name
        self.city = city
        self.service = service
        self.vergiOrani = 0.20

    def __str__(self):
        return (f"Sirket No: {self.companyNo} Sirket Adi: {self.name} Sirket ili: {self.city} Servis : {self.service}")


class Karamaciolmayan(Holding):
    def __init__(self, companyNo, name, city, service):
        super().__init__(companyNo, name, city, service)
        self.vergiOrani = 0.05


srk1 = Holding(1111, "Humanity Bank", "NewYork", "Banking")
srk2 = Holding(2222, "Humanity Justice", "Newyork", "Advocacy")
srk3 = Karamaciolmayan(5555, "Humanity Education", "Newyork", "Education")
print(srk1.companyNo)
print(srk1.name)
print(srk1.city)
print(srk1.service)
print(srk3.vergiOrani)
print(srk1)
