#Exception
def bolme(a,b):
    sonuc ="Veri giris hatasi..a ve b yi sayi olarak giriniz"
    try:
        sonuc = a / b
    except ZeroDivisionError:
        print("Sifira bolume hatasi")
    except TypeError:
        print("Sayisal deger giriniz")
    return sonuc



print(bolme(10,2))
print(bolme(10,0))
print(bolme("Ahmet",3))


