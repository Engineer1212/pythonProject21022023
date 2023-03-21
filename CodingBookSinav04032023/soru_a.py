class Sirket():
    def __init__(self, companyNo, name, city, service):
        self.companyNo = companyNo
        self.name = name
        self.city = city
        self.service = service
        self.holding_liste = []

    def __str__(self):
        return (f"Sirket Kodu; {self.companyNo}, Sirket Adi: {self.name} Sirket ili: {self.city} Sirket Alani: {self.service}")



srk1 = Sirket (1111, "Humanity Bank", "Newyork", "Banking")
srk2 = Sirket (2222, "Humanity Justice", "Newyork", "Advocacy")
print(srk1)
print(srk2)