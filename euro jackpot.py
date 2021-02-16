# Created by Paweł Smyl

import random

wynik = []
ile = int(input("Podaj liczbe, ile losowan chcesz skreslic?\n"))
ilosc_rzutow = 1
while ilosc_rzutow <= ile:
    jack1 = sorted(random.sample(range(1,50),5))
    jack2 = sorted(random.sample(range(1,10),2))
    wynik.append(jack1)
    wynik.append(jack2)
    ilosc_rzutow += 1
print("Wynik to:",wynik)
