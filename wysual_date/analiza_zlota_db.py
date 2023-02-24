import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

waluta_usd='USD/uncja'
waluta_pl='PL/uncja'
title="kurs złota"

def pokaz(sql):
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  kursy=[]
  for x in myresult:
    kurs=[x[0],x[1],x[2],x[3]]
    kursy.append(kurs)
    print(str(x[0])+" USD, ",str(x[1])+" PL, -> ",x[2],x[3])
  print(myresult)
  return kursy

mydb = mysql.connector.connect(user='root', password='adminadmin', host='127.0.0.1', database='my_project')
mycursor = mydb.cursor()
query="SELECT * FROM kursy"
result_dataFrame = pd.read_sql(query, mydb)
df = pd.DataFrame(result_dataFrame)
print(df)

df.plot(figsize=(13,5), title=title, subplots=True, linestyle='-.' ,xticks=(df["data"]), rot=45)  # figsize - rozmiar wykresu w calach (szer, wys),
plt.grid()
plt.title(title)
plt.xlabel("data")
plt.ylabel("wartość")
plt.legend()
plt.show()