import requests
import bs4
import time

localtime = time.localtime(time.time())
today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # formatowanie daty do postaci 2023-02-02 14:32:32


url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ZLOTO'

try:
    page = requests.get(url)
#   type(page)
    page.raise_for_status()

# poniższe polecenie wyświetli nam całą stronę w jednej linii
#    print(page.content)

except Exception as exc:
    print("wystąpił błąd: %s" % (exc))
    print(f"sprawdź czy adres strony {url} został wpisany poprawnie")








# tworzymy obiekt bs4 by móc przeszukiwać po tagach html
soup = bs4.BeautifulSoup(page.content, 'html.parser')


# ładniejszy sposób wyświetlenia strony, nie w jednym wierszu wszystko
#     print(soup.prettify())


# przeszukiwanie po tagach
# find_all_a = soup.find_all('a')                               # znajdzie wszystkie tagi '<a>' i zapisze w liście
# print(f"na stronie jest {len(find_all_a)} linków")            # ilość elementów listy
# print(find_all_a[50].getText())                               # wypisze tylko to, co między <a></a> z 51 linku z tablicy
# print(find_all_a[50])                                         # wypisze całość od <a> do zakończenia </a> włącznie

find_kurs = soup.find('div', {'class': "profilLast"})         # znajdzie tag '<div>' mający jako atrybut class=profilLast
gold = find_kurs.getText()  # zapisze zawartość tagu w zmiennej 'gold'
print('obecny kurs złota: ',gold)
kurs=gold[:1]+ gold[2:5]+'.'+gold[6:8]



# zapiszemy sobie kurs złota do pliku 'zloto.txt' wraz z datą i godziną
plik = open('zloto.txt', 'a', encoding="utf-8")     # open z argumentem 'a' dopisuje do poprzedniego, gdyby było 'w' to usunełoby poprzednią zawartość i wpisało to co teraz itp
plik.write(kurs+";"+today)                          # zampsuje w pliku
plik.write('\n')
plik.close()

# print(find_kurs.getText())

