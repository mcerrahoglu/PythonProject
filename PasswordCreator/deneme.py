from random import randint

class Password():
    tr = "abcçdefgğhıijklmnoöprsştuüvyz"
    numeric = "0123456789"
    sembols = "!'^+%&/()=?_-<>#${}[]*@.,:|~"
    sifre = ""
    listoftr = list(tr)
    numerica = list(numeric)
    sembola = list(sembols)

    def __init__(self):
        pass


    def randomcome(self):
        self.ran = randint(0, 2)
        self.rantr = randint(0, len(self.listoftr) - 1)
        self.rannum = randint(0, len(self.numerica) - 1)
        self.ransem = randint(0, len(self.sembola) - 1)

    def harfkontrol(self, uppercase):

        if uppercase == 1:
            rancase = randint(0, 1)

            if rancase == 0:
                a = str(self.listoftr[self.rantr])
                self.sifre = self.sifre + a
            elif rancase == 1:

                a = str(self.listoftr[self.rantr])
                a = a.upper()
                self.sifre = self.sifre + a

        else:

            a = str(self.listoftr[self.rantr])
            self.sifre = self.sifre + a


    def numaracontrol(self):

        b = str(self.numerica[self.rannum])
        self.sifre = self.sifre + b


    def sembolkontrol(self):

        c = str(self.sembola[self.ransem])
        self.sifre = self.sifre + c


    def passwordcreate(self, numara, sembol, uppervaryok, uzunluk):
        controlofnumeric = 0
        controlofsembol = 0

        if numara != 0:
            controlofnumeric = 1

        if sembol != 0:
            controlofsembol = 1

        for sayac in range(0, int(uzunluk)):
            self.randomcome()

            if self.ran == 0:
                self.harfkontrol(uppervaryok)

            elif self.ran == 1:
                if controlofnumeric == 1:
                    self.numaracontrol()
                else:
                    sayi = randint(0, 1)
                    if sayi == 1:
                        self.harfkontrol(uppervaryok)
                    else:
                        if controlofsembol == 1:
                            self.sembolkontrol()
                        else:
                            self.harfkontrol(uppervaryok)
            elif self.ran == 2:
                if controlofsembol == 1:
                    self.sembolkontrol()
                else:
                    sayi = randint(0, 1)
                    if sayi == 1:
                        self.harfkontrol(uppervaryok)
                    else:
                        if controlofnumeric == 1:
                            self.numaracontrol()
                        else:
                            self.harfkontrol(uppervaryok)

        print(f"şifre..:{self.sifre}")





