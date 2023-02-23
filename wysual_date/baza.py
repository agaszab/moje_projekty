import mysql.connector

def wstaw(kurs_pl, kurs_usd, data, godzina, mydb):
  sql="INSERT INTO kursy(kursy_pl, kursy_usd, data, godzina) VALUES (kurs_pl, kurs_usd, data, godzina)"
  try:
    cursor.execute(sql)
    mydb.commit()
  except:
    mydb.rollback()
#  mydb.close()

def pokaz(sql):
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print(myresult)

mydb = mysql.connector.connect(user='root', password='adminadmin', host='127.0.0.1', database='my_project')
mycursor = mydb.cursor()

wstaw(1833.75,8230.67,'2023-02-23','10:59:11',mydb)
pokaz("SELECT * FROM kursy")


