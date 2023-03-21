from canlilar.Canlı import Hayvan
from canlilar.bitki import Bitki
from canlilar.insan import Insan

canliListesi = []
i1 = Insan()
i2 = Insan()
b1 = Bitki()
h1 = Hayvan()

canliListesi.append(i1)
canliListesi.append(i2)
canliListesi.append(b1)
canliListesi.append(h1)

for canli in canliListesi:
    canli.solu()
