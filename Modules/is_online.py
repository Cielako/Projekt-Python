from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time

def is_online(target):
    start = time.time()
    target = 'http://' + str(target) # adres
    
    try: # próba 
        response = urlopen(Request(target))
    except URLError as exception:# wyjątki
        return ('Nie udało się połączyć z serwerem :( \n\n Powód: '+ str(exception.reason))
    except HTTPError as exception:
        return('Serwer nie mógł zrealizować żądania :( \n\n Kod błędu: ' + str(exception.code))
    else:
        end = time.time() - start
        return ('Strona '+ str(target) +' działa poprawnie, połączono w : ' + str(round(end,2)) + ' s')
# Przykładowy test skanera portów
# print(is_online("www.facebook.com"))
