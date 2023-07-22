import datetime
import pywhatkit as kit

girdi = int(input("Yeni Kişi Eklemek İçin 1, Var Olan Kişilerin Doğum Günü Kontrolü İçin 2 yi Tuşlayınız..:"))

if girdi == 1:
    ad = input("İsim Giriniz..:")
    soyad = input("Soyisim Giriniz..:")
    lakap = input("Arkadaşınıza Özel Bir İsimle Hitap Etmek için özel isim giriniz (İstemiyor iseniz 2'yi tuşlayın)..:")
    tel_no = input("Telefon Numarası..:")
    dog_tar = input("Doğum Günü Tarihini Giriniz(Gün/ay olarak giriniz)..:")

    if lakap in "2":
        with open("messages.txt", mode="a") as newMessages:
            newMessages.write(f"İsim..:{ad}\nSoyisim..:{soyad}\nTelefon..:+90{tel_no}\nDoğum Tarihi..:{dog_tar}\n")
    else:
        with open("messages.txt", mode="a") as newMessages:
            newMessages.write(f"İsim..:{ad}\nSoyisim..:{soyad}\nLakap..:{lakap}\nTelefon..:+90{tel_no}\nDoğum Tarihi..:{dog_tar}\n")

elif girdi == 2:
    with open("messages.txt", mode="r") as newMessages:
        #dataRead = newMessages.read()
        data_count = newMessages.read().count("\n")
        newMessages.seek(0)
        date = datetime.datetime.now()
        gun = str(date.day)
        ay = str(date.month)

        hour = date.hour
        minute = date.minute + 1

        for i in range(data_count):
            data = str(newMessages.readline())
            if "İsim" in data:
                isim = data
            elif "Soyisim" in data:
                soyisim = data
            elif "Lakap" in data:
                lakap = data
            elif "Telefon" in data:
                telefon = data


            if "Doğum Tarihi" in data:
                if gun and ay in data:
                    try:
                        #kit.sendwhatmsg(f"{telefon}", f"Merhaba {isim} Doğum günün kutlu olsun.",hour,minute)
                        #kit.playonyt("https://www.youtube.com/watch?v=wDh9lOwp9QM")
                        print(f"{isim}{soyisim}{lakap}{telefon}")


                    except:
                        print("hata oluştu")
