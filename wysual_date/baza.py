import mysql.connector
import requests
import bs4

def wstaw(kurs_pl, kurs_usd, data, godzina, mydb):
  sql=f"INSERT INTO kursy(kursy_pl, kursy_usd, data, godzina) VALUES ({str(kurs_pl)}, {str(kurs_usd)}, CURDATE(), CURTIME())"
  cursor = mydb.cursor()
  cursor.execute(sql)
  mydb.commit()

def pokaz(sql):
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print(myresult)

def pobiez():
  url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ZLOTO'
  try:
    page = requests.get(url)
    page.raise_for_status()
  except Exception as exc:
    print("wystąpił błąd: %s" % (exc))
    print(f"sprawdź czy adres strony {url} został wpisany poprawnie")

  soup = bs4.BeautifulSoup(page.content, 'html.parser')
  find_gold_rate = soup.find('div',
                             {'class': "profilLast"})  # znajdzie tag '<div>' mający jako atrybut class=profilLast
  gold = find_gold_rate.getText()  # zapisze zawartość tagu w zmiennej 'gold'
  gold_rate = gold[:1] + gold[2:5] + '.' + gold[6:8]

  find_pl = soup.find_all('span', {'class': 'value'})
  gold_rate_pl = find_pl[4].getText().strip()
  gold_rate_pl = gold_rate_pl[0] + gold_rate_pl[2:]
  gold_rate_pl = gold_rate_pl[:4] + '.' + gold_rate_pl[5:]
  return gold_rate, gold_rate_pl


mydb = mysql.connector.connect(user='root', password='adminadmin', host='127.0.0.1', database='my_project')
mycursor = mydb.cursor()

kurs=pobiez()
# print(kurs)
wstaw(kurs[1],kurs[0],'2023-02-23','10:59:11',mydb)
pokaz("SELECT * FROM kursy")


