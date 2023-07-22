import numpy as np


def ikiye_bolme(denklem, aralik1, aralik2, durma_kosul, iterasyon=0):

    aralik1_denklem = denklem.replace('x', str(aralik1))
    aralik1_sonuc = eval(aralik1_denklem)
    print(aralik1, "Kapalı Aralığına Göre Denklem Sonucu..:", aralik1_sonuc)

    aralik2_denklem = denklem.replace('x', str(aralik2))
    aralik2_sonuc = eval(aralik2_denklem)
    print(aralik2, "Kapalı Aralığına Göre Denklem Sonucu..:", aralik2_sonuc)

    print("-------------------------------------------------------")
    if aralik1_sonuc*aralik2_sonuc < 0:
        yeni_aralik = float((aralik1+aralik2)/2)
        yeni_aralik_denklem = denklem.replace('x', str(yeni_aralik))
        yeni_aralik_sonuc = eval(yeni_aralik_denklem)
        print("Yeni Kapalı Aralık..:", yeni_aralik)
        print("Yeni Kapalı Aralık Değerine Göre Denklem Sonucu..:", yeni_aralik_sonuc)
        iterasyon = iterasyon + 1
        if (aralik2_sonuc-aralik1_sonuc)/2**iterasyon < durma_kosul:
            print("Durma Koşulu Çalıştı..:", yeni_aralik)

        else:
            if yeni_aralik_sonuc * aralik1_sonuc < 0:
                if yeni_aralik > aralik1:
                    ikiye_bolme(denklem, aralik1, yeni_aralik, durma_kosul, iterasyon)

                else:
                    ikiye_bolme(denklem, yeni_aralik, aralik1, durma_kosul, iterasyon)

            elif yeni_aralik_sonuc * aralik2_sonuc < 0:
                if yeni_aralik > aralik2:
                    ikiye_bolme(denklem, aralik2, yeni_aralik, durma_kosul, iterasyon)

                else:
                    ikiye_bolme(denklem, yeni_aralik, aralik2, durma_kosul, iterasyon)
    else:
        print("Denklemin Kökü Yoktur.")

####################################################################################################################


def ikiye_bolme_iterasyon(denklem, aralik1, aralik2, iterasyon, sayac=0):
    aralik1_denklem = denklem.replace('x', str(aralik1))
    aralik1_sonuc = eval(aralik1_denklem)
    print(aralik1, "Kapalı Aralığına Göre Denklem Sonucu..:", aralik1_sonuc)

    aralik2_denklem = denklem.replace('x', str(aralik2))
    aralik2_sonuc = eval(aralik2_denklem)
    print(aralik2, "Kapalı Aralığına Göre Denklem Sonucu..:", aralik2_sonuc)
    if aralik1_sonuc * aralik2_sonuc < 0:
        yeni_aralik = float((aralik1+aralik2)/2)
        yeni_aralik_denklem = denklem.replace('x', str(yeni_aralik))
        yeni_aralik_sonuc = eval(yeni_aralik_denklem)
        print("Yeni Kapalı Aralık..:", yeni_aralik)
        print("Yeni Kapalı Aralık Değerine Göre Denklem Sonucu..:", yeni_aralik_sonuc)
        sayac = sayac+1
        print("--------------------------------------------------------------")
        print("iterasyon Sayısı...:", sayac)
        print("1. Aralık..:", aralik1, "\n2. Aralık..:", aralik2, "\nYeni Aralık..:", yeni_aralik,
              "\n1. Aralık Sonucu..:", aralik1_sonuc, "\n2. Aralık Sonucu..:", aralik2_sonuc, "\nYeni Aralık Sonucu..:",
              yeni_aralik_sonuc)
        print("--------------------------------------------------------------")
        if sayac == iterasyon:
            print("Durma Koşulu Çalıştı..:", yeni_aralik)
        else:
            if yeni_aralik_sonuc * aralik1_sonuc < 0:
                if yeni_aralik > aralik1:
                    ikiye_bolme_iterasyon(denklem, aralik1, yeni_aralik, iterasyon, sayac)

                else:
                    ikiye_bolme_iterasyon(denklem, yeni_aralik, aralik1, iterasyon, sayac)

            elif yeni_aralik_sonuc * aralik2_sonuc < 0:
                if yeni_aralik > aralik2:
                    ikiye_bolme_iterasyon(denklem, aralik2, yeni_aralik, iterasyon, sayac)

                else:
                    ikiye_bolme_iterasyon(denklem, yeni_aralik, aralik2, iterasyon, sayac)

    else:
        print("Denklemin Kökü Yoktur.")

####################################################################################################################


def lineer_regriresion_dogrusal(deger_sayisi, sayac=0):
    x_list = []
    y_list = []
    x_kare_list = []
    x_y_carpim_list = []

    for x in range(deger_sayisi):
        x_list.append(float(input(f"{sayac+1}.x Değerini Giriniz..:")))
        sayac = sayac+1

    sayac = 0

    for y in range(deger_sayisi):
        y_list.append(float(input(f"{sayac+1}.y Değerini Giriniz..:")))
        sayac = sayac + 1

    for x_kare in range(deger_sayisi):
        x_kare_list.append(float(x_list[x_kare]**2))

    for x_y_carpim in range(deger_sayisi):
        x_y_carpim_list.append(float(x_list[x_y_carpim]*y_list[x_y_carpim]))

    x_deger_toplam = sum(x_list)
    y_deger_toplam = sum(y_list)
    x_kare_toplam = sum(x_kare_list)
    x_y_carpim_toplam = sum(x_y_carpim_list)

    a = np.array([[deger_sayisi, x_deger_toplam], [x_deger_toplam, x_kare_toplam]])

    b = np.array([y_deger_toplam, x_y_carpim_toplam])

    a_b_deger_ciktisi = np.linalg.solve(a, b)
    a_b_deger_ciktisi_list = list(a_b_deger_ciktisi)

    print("-----------------------------------------------------")
    print("x'in Değer Listesi..:", x_list)
    print("x'in Değerler Toplamı..:", x_deger_toplam)
    print("-----------------------------------------------------")
    print("y'nin Değer Listesi..:", y_list)
    print("y'nin Değerler Toplamı..:", y_deger_toplam)
    print("-----------------------------------------------------")
    print("x^2'nin Değer Listesi..:", x_kare_list)
    print("x^2'nin Değerler Toplamı..:", x_kare_toplam)
    print("-----------------------------------------------------")
    print("x*y'nin Değer Listesi..:", x_y_carpim_list)
    print("x*y'nin Değerler Toplamı..:", x_y_carpim_toplam)
    print("-----------------------------------------------------")
    print(deger_sayisi, "* a + ", x_deger_toplam, "* b = ", y_deger_toplam)
    print(x_deger_toplam, "* a + ", x_kare_toplam, "* b = ", x_y_carpim_toplam)
    print(f"{a_b_deger_ciktisi_list[0]} + {a_b_deger_ciktisi_list[1]}X")

####################################################################################################################


def lineer_regriresion_egrisel(deger_sayisi, sayac=0):

    x_list = []
    y_list = []
    x_kare_list = []
    x_kup_list = []
    x_ussu_dort_list = []
    x_y_carpim_list = []
    x_kare_y_carpim_list = []

    for x in range(deger_sayisi):
        x_list.append(float(input(f"{sayac+1}.x Değerini Giriniz..:")))
        sayac = sayac+1

    sayac = 0

    for y in range(deger_sayisi):
        y_list.append(float(input(f"{sayac+1}.y Değerini Giriniz..:")))
        sayac = sayac + 1

    for x_kare in range(deger_sayisi):
        x_kare_list.append(float(x_list[x_kare]**2))

    for x_kup in range(deger_sayisi):
        x_kup_list.append(float(x_list[x_kup]**3))

    for x_dort in range(deger_sayisi):
        x_ussu_dort_list.append(float(x_list[x_dort]**4))

    for x_y_carpim in range(deger_sayisi):
        x_y_carpim_list.append(float(x_list[x_y_carpim] * y_list[x_y_carpim]))

    for x_kare_y in range(deger_sayisi):
        x_kare_y_carpim_list.append(float((x_list[x_kare_y]**2)*y_list[x_kare_y]))

    x_deger_toplam = sum(x_list)
    y_deger_toplam = sum(y_list)
    x_kare_toplam = sum(x_kare_list)
    x_kup_toplam = sum(x_kup_list)
    x_dort_toplam = sum(x_ussu_dort_list)
    x_y_carpim_toplam = sum(x_y_carpim_list)
    x_kare_y_toplam = sum(x_kare_y_carpim_list)

    a = np.array([[deger_sayisi, x_deger_toplam, x_kare_toplam], [x_deger_toplam, x_kare_toplam, x_kup_toplam],
                  [x_kare_toplam, x_kup_toplam, x_dort_toplam]])

    b = np.array([y_deger_toplam, x_y_carpim_toplam, x_kare_y_toplam])

    a_b_deger_ciktisi = np.linalg.solve(a, b)

    a_b_deger_ciktisi_list = list(a_b_deger_ciktisi)

    print("-----------------------------------------------------")
    print("x'in Değer Listesi..:", x_list)
    print("x'in Değerler Toplamı..:", x_deger_toplam)
    print("-----------------------------------------------------")
    print("y'nin Değer Listesi..:", y_list)
    print("y'nin Değerler Toplamı..:", y_deger_toplam)
    print("-----------------------------------------------------")
    print("x^2'nin Değer Listesi..:", x_kare_list)
    print("x^2'nin Değerler Toplamı..:", x_kare_toplam)
    print("-----------------------------------------------------")
    print("x^3'ün Değer Listesi..:", x_kup_list)
    print("x^3'ün Değerler Toplamı..:", x_kup_toplam)
    print("-----------------------------------------------------")
    print("x^4'ün Değer Listesi..:", x_ussu_dort_list)
    print("x^4'ün Değerler Toplamı..:", x_dort_toplam)
    print("-----------------------------------------------------")
    print("x*y'nin Değer Listesi..:", x_y_carpim_list)
    print("x*y'nin Değerler Toplamı..:", x_y_carpim_toplam)
    print("-----------------------------------------------------")
    print("x^2*y'nin Değer Listesi..:", x_kare_y_carpim_list)
    print("x^2*y'nin Değerler Toplamı..:", x_kare_y_toplam)
    print("-----------------------------------------------------")

    print(f"{a_b_deger_ciktisi_list[0]} + ({a_b_deger_ciktisi_list[1]})X + ({a_b_deger_ciktisi_list[2]})X^2 \n")
