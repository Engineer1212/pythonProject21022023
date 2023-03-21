def bolme(a,b):
    try:
        sonuc = a / b
    except ZeroDivisionError:
        print("Sifira bolume hatasi")
    except TypeError:
        print("Sayisal deger giriniz")
    else:
        print(sonuc)
    finally:
        print("Islem Tamam")



bolme("Ahmet",3)
bolme(9,3)