import pandas as pd
import matplotlib.pyplot as plt

waluta_usd='USD/uncja'
waluta_pl='PL/uncja'
title="kurs złota"

gold_rate= pd.read_csv('zloto.csv', sep=';', index_col=['data', 'godzina'], header=0) # index_col - co ma być indeksem
print(gold_rate)
df = pd.DataFrame(gold_rate)

# plt.yticks(range(0,5000))
# filter = df['kolumna'] &gt; 5  || czyli >5
# print(df)
# df[['kurs_usd', 'kurs_pl']].plot(colormap='magma')
# print(df)
# print(df["kurs_usd","kurs_pl"])
#  df.plot(figsize=(13,5), subplots=True, title=title, logy=True)

df.plot(figsize=(13,5), title=title, subplots=True, linestyle='-.' ,xticks=(range(14)), rot=45, yticks=(range(0,1000,1000)))  # figsize - rozmiar wykresu w calach (szer, wys),
                                                                                 # xticks - wartości na osi,
                                                                                 # subplots=True - by nie wszytkie wartości na jednym wykresia a na kilku wykresach
                                                                                 # rot - kąt o jaki obróci się napis na osi x
                                                                                 # gdy nie chcemy legendy na wykresie to legend = False

# plt.bar(df['data'],600, color='purple')
plt.grid()
plt.title(title)
plt.xlabel("data")
plt.ylabel("wartość")
plt.legend()
plt.show()

#etykiety pionowe






#  kursySeries=pd.Series(kursy_zlota)
#  print('ilość wpisów: ', kursySeries.size)
#  print('najniższy kurs:', kursySeries.min()[0],waluta,'zanotowany dnia: ',kursySeries.min()[1])
#  print('najwyższy kurs:',kursySeries.max()[0],waluta, 'zanotowany dnia: ',kursySeries.max()[1])

# kursySlownik=dict(kursySeries)
# print(kursySlownik)

#  x_points=[]
#  y_points=[]
#  for elem in kursySeries:
#      x_points.append(kursySeries[0])
#      y_points.append(kursySeries[1])

# dodajemy wykres i umieszczamy punkt startu i spadku
#  title = "Wykres kursów złota"
# x=max(x_points)
# plt.scatter(0, 0, label="Zloto")
# plt.scatter(0, 0, "oś x")
# plt.plot(x_points, y_points, marker="+", color="red", label="Kolejne punkty rzutu.")

# plt.plot()
#  plt.grid()
#  plt.title(title)
#  plt.xlabel("data")
#  plt.ylabel(waluta)
#  plt.legend()
# plt.show()