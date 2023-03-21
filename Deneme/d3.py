class ogrenci:
    isim = "-"
    devamsizlik = 0

    def devamsizlikEkle():
        ogrenci.devamsizlik += 1

print(ogrenci.devamsizlik)    # 0

ogrenci.devamsizlikEkle()     # Merhaba

print(ogrenci.devamsizlik)     # 1
ogrenci.devamsizlikEkle()     # Merhaba
print(ogrenci.devamsizlik)     # 1