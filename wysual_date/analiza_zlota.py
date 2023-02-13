import pandas as pd
import matplotlib.pyplot as plt

waluta='USD/uncja'

# f = open("..\zloto.txt", "r")
# kursy_zlota= []
# kurs_one= {}
# for line in f:
#     elem=line.split(';')
#     print(elem)
#     kursy_zlota.append(elem)

kursy_zlota= pd.read_csv("..\zloto.csv")
df = pd.DataFrame(kursy_zlota)
df.columns = ['kurs', 'data']
print(df)

#  kursySeries=pd.Series(kursy_zlota)
print('ilość wpisów: ', kursySeries.size)
print('najniższy kurs:', kursySeries.min()[0],waluta,'zanotowany dnia: ',kursySeries.min()[1])
print('najwyższy kurs:',kursySeries.max()[0],waluta, 'zanotowany dnia: ',kursySeries.max()[1])

# kursySlownik=dict(kursySeries)
# print(kursySlownik)

x_points=[]
y_points=[]
for elem in kursySeries:
    x_points.append(kursySeries[0])
    y_points.append(kursySeries[1])

# dodajemy wykres i umieszczamy punkt startu i spadku
title = "Wykres kursów złota"
# x=max(x_points)
# plt.scatter(0, 0, label="Zloto")
# plt.scatter(0, 0, "oś x")
# plt.plot(x_points, y_points, marker="+", color="red", label="Kolejne punkty rzutu.")

plt.plot(x_points,y_points)
plt.grid()
plt.title(title)
plt.xlabel("data")
plt.ylabel(waluta)
plt.legend()
plt.show()