#Created by Paweł Smyl

import random

wynik = []
ile = int(input("Podaj liczbe, ile losowan chcesz skreslic?\n"))
ilosc_rzutow = 1
while ilosc_rzutow <= ile:
    lotto = sorted(random.sample(range(1,41),5))
    wynik.append(lotto)
    ilosc_rzutow += 1
print("Wynik to:",wynik)
