from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time

def is_online(target):
    start = time.time()
    target = 'http://' + str(target) # adres
    
    try:
        response = urlopen(Request(target))
    except URLError as exception:
        return ('Nie udało się połączyć z serwerem :( \n\nPowód: '+ str(exception.reason))
    except HTTPError as exception:
        return('Serwer nie mógł zrealizować żądania :( \n\n Kod błędu: ' + str(exception.code))
    else:
        end = time.time() - start
        return ('Strona '+ str(target) +' działa poprawnie, połączenie nastąpiło po: ' + str(round(end,2)) + ' s')

