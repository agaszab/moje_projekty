import requests
res = requests.get('https://www.gutenberg.org/files/27062/27062-0.txt')
res2 = requests.get('https://bibula.com')
type(res)   #pobranie zawartości
type(res2)


# 1 sposob na sprawdzenie czy się poprawnie dane pobraly
res.status_code==requests.codes.ok     # response.status_code == 200 oznacza że wykonało się prawidłowo,  404 - zasob nie zostal znaleziony
                                       # odpowiedź przechowywana jest w zmiennej text obiektu Resonse

# 2 sposob na sprawdzenie czy się poprawnie dane pobraly - jeśli nie, wystąpi wyjątek - by nie przerwał się program najlepiej tą metodę umieścić
#   w bloku try:
#               res.raise_for_status()
#           except Exception as exc:
#                print("wystąpił błąd: %s" %(exc))
#   by samemu obsłużyć błąd bez przerwania programu

res.raise_for_status()

len(res.text)   #pokazuje ile znaków się ściągneło
print(res.text[34:350])
print(res2.text[:350])



# można też zawartość zapisać do pliku

playFile = open('ze_strony_www.txt', 'wb')   # open z argumentem 'wb' oznacza, że tworzymy plik binarny
for elem in res.iter_content(100000):   # 1000000 to ilość bajtów w jednym fragmencie bo zapisujemy porcjami
    playFile.write(elem)     # write(elem) zampsuje zawartość elem w pliku
playFile.close()