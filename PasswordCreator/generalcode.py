from random import randint


tr = "abcçdefgğhıijklmnoöprsştuüvyz"
numeric = "0123456789"
sembols = "!'^+%&/()=?_-<>#${}[]*@.,:|~"


def numericControl(value):
    if value == "1":
        listofnumeric=list(numeric)
        return listofnumeric
    else:
        return 0


def sembolsControl(value):
    if value == "1":
        listsofsembol=list(sembols)
        return listsofsembol
    else:
        return 0


def passwordCreator(valueofnumeric, valueofsembols, valueofuppercase, uzunluk, numerica, sembola):
    sifre = ""
    controlofnumeric = 0
    controlofsembol = 0
    listoftr = list(tr)

    if valueofnumeric != 0:
        controlofnumeric = 1

    if valueofsembols != 0:
        controlofsembol = 1
    print("numeric", controlofnumeric)
    print("sembol", controlofsembol)
    print("uppercase", valueofuppercase)
    print("uzunluk", uzunluk)
    print("numerica", numerica)
    print("sembola", sembola)
    print("listtr", listoftr)
    for sayac in range(0, int(uzunluk)):
        print("sayac=", sayac)
        ran = randint(0, 2)
        print("ran=", ran)
        rantr = randint(0, len(listoftr)-1)
        rannum = randint(0, len(numerica)-1)
        ransem = randint(0, len(sembola)-1)

        if ran == 0:
            print("ran == 0")
            if valueofuppercase == "1":
                print("valueofuppercase == 1")
                rancase = randint(0, 1)
                print("rancase=", rancase)

                if rancase == 0:
                    print("rancase == 0")
                    a = str(listoftr[rantr])
                    sifre = sifre+a
                    print("a=", a)
                    print("sifre=", sifre)

                elif rancase == 1:
                    print("rancase == 1")
                    a1 = str(listoftr[rantr])
                    a1 = a1.upper()
                    sifre = sifre + a1
                    print("a1=", a1)
                    print("sifre=", sifre)
            else:
                print("else")
                a2 = str(listoftr[rantr])
                sifre = sifre + a2
                print("a2=", a2)
                print("sifre=", sifre)

        elif ran == 1 and controlofnumeric == 1:
            print("ran == 1 and controlofnumeric == 1")
            b = str(numerica[rannum])
            sifre = sifre+b
            print("b=", b)
            print("sifre=", sifre)

        elif ran == 2 and controlofsembol == 1:
            print("ran == 2 and controlofsembol == 1")
            c = str(sembola[ransem])
            sifre = sifre+c
            print("c=", c)
            print("sifre=", sifre)

    print(sifre)







