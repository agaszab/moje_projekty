import pandas as pd

waluta='USD/uncja'

f = open("..\zloto.txt", "r")
kursy_zlota= []
kurs_one= {}
for line in f:
    elem=line.split('|')
    print(elem)
    kursy_zlota.append(elem)

kursySeries=pd.Series(kursy_zlota)
print('ilość wpisów: ', kursySeries.size)
print('najniższy kurs:', kursySeries.min()[0],waluta,'zanotowany dnia: ',kursySeries.min()[1])
print('najwyższy kurs:',kursySeries.max()[0],waluta, 'zanotowany dnia: ',kursySeries.max()[1])

kursySlownik=dict(kursySeries)
print(kursySlownik)

