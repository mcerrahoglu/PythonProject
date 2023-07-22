import NumericalLibrary
islem = int(input("Yapmak İstediğiniz İşlemi Giriniz..:\n1-Durma Koşuluna Göre 2'ye Bölme Hesaplama"
                  "\n2-İterasyon Sayısına Göre 2'ye Bölme Hesaplama"
                  "\n3-Dogrusal için hesaplama\n4-Eğrisel İçin Hesaplama"))

if islem == 1:
    denklem = input("denklem gir..:")

    aralik_1 = float(input("Kapalı Aralıktaki İlk Değeri Giriniz...:"))

    aralik_2 = float(input("Kapalı Aralıktaki İkinci Değeri Giriniz...:"))

    durma_kosul = float(input("Durma Koşulunu Giriniz...:"))

    NumericalLibrary.ikiye_bolme(denklem, aralik_1, aralik_2, durma_kosul)

elif islem == 2:
    denklem = input("denklem gir..:")

    aralik_1 = float(input("Kapalı Aralıktaki İlk Değeri Giriniz...:"))

    aralik_2 = float(input("Kapalı Aralıktaki İkinci Değeri Giriniz...:"))

    iterasyon = float(input("İterasyon Giriniz...:"))

    NumericalLibrary.ikiye_bolme_iterasyon(denklem, aralik_1, aralik_2, iterasyon)

elif islem == 3:
    deger_sayisi = int(input("Kaç Adet Değer Girileceğini Belirtiniz..:"))

    NumericalLibrary.lineer_regriresion_dogrusal(deger_sayisi)
elif islem == 4:
    deger_sayisi = int(input("Kaç Adet Değer Girileceğini Belirtiniz..:"))

    NumericalLibrary.lineer_regriresion_egrisel(deger_sayisi)
