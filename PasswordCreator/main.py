import generalcode

numeric = input("numara var mı")
sembol = input("sembol var mı")
harf = input("büyük harf var mı")
karakter = input("kaç karakter")

numerica = generalcode.numericControl(numeric)
sembola = generalcode.sembolsControl(sembol)
generalcode.passwordCreator(numeric, sembol, harf, karakter, numerica, sembola)