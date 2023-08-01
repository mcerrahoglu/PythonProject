import random
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

    def passwordcheck(self):
        sifre = list(self.sifre)
        if len(sifre) > 1:
            if sifre[-1] == sifre[-2]:
                a = sifre[-1]
                for i in self.listoftr:
                    if a == i:
                        sifre[-1] = random.choice(self.listoftr)
                        break
                for j in self.numerica:
                    if a == j:
                        sifre[-1] = random.choice(self.numerica)
                        break
                for k in self.sembola:
                    if a == k:
                        sifre[-1] = random.choice(self.sembola)
                        break


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
                self.passwordcheck()

            elif self.ran == 1:
                if controlofnumeric == 1:
                    self.numaracontrol()
                    self.passwordcheck()
                else:
                    sayi = randint(0, 1)
                    if sayi == 1:
                        self.harfkontrol(uppervaryok)
                        self.passwordcheck()
                    else:
                        if controlofsembol == 1:
                            self.sembolkontrol()
                            self.passwordcheck()
                        else:
                            self.harfkontrol(uppervaryok)
                            self.passwordcheck()
            elif self.ran == 2:
                if controlofsembol == 1:
                    self.sembolkontrol()
                    self.passwordcheck()
                else:
                    sayi = randint(0, 1)
                    if sayi == 1:
                        self.harfkontrol(uppervaryok)
                        self.passwordcheck()
                    else:
                        if controlofnumeric == 1:
                            self.numaracontrol()
                            self.passwordcheck()
                        else:
                            self.harfkontrol(uppervaryok)
                            self.passwordcheck()

        print(f"şifre..:{self.sifre}")