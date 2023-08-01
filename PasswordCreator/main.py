import generalcode


obje = generalcode.Password()
obje.passwordcreate(1, 1, 1, 12)
"""
while True:
    try:
        numeric = int(input("Şifrenizde Numara Olsun mu? (Evet=1 , Hayır=0)..:"))
        sembol = int(input("Şifrenizde sembol Olsun mu? (Evet=1 , Hayır=0)..:"))
        harf = int(input("Şifrenizde büyük harf Olsun mu? (Evet=1 , Hayır=0)..:"))
        karakter = int(input("Şifreniz kaç karakterden oluşsun? (Önerilen Uzunluk 12 karakterdir)..:"))

        if numeric == 1 or 0 and sembol == 1 or 0 and harf == 1 or 0:
            break
        else:
            print("Lütfen istenilen değerleri giriniz")
    except:
        print("Lütfen istenilen değerleri giriniz")

obje.passwordcreate(numeric, sembol, harf, karakter)
"""