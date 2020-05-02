# Kod został zaczerpnięty ze strony https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
# Głównie zależało mi na szybkości (Skaner którego chciałem użyć wcześniej był strasznie wolny)

import threading
import socket # interfejs sieciowy niskiego poziomu

def portscanner(target):
    open_ports = {}
    def portscan(port):    
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#(Adresacja IPV4 , Przesyłanie danych strumieniowo)
        s.settimeout(0.5)# Ustwiamy standardowe opóźnienie
        try: # sprawdzenie czy port jest otwarty
            con = s.connect((target,port))#połączenie na porcie
            open_ports[port] = "Otwarty"
            # print(f'Port : {port} Otwarty.') # Test otwartych portów
            con.close()#zakończenie połączenia
        except:# jeśli port jest zamknięty wykonuj dalej
            pass
    port_number = 1
    for p in range(1,33434):
        t = threading.Thread(target = portscan, kwargs = {"port" : port_number})# (target - wywoływalny obiekt za pomocą metody run(), kwargs - słownik argumentów do wywołania celu)
        port_number += 1
        t.start() # rozpoczyna działanie wątku
        
    if len(open_ports) == 0: # Jeśli żaden port nie jest otwarty zwróć komunikat
        return "Brak otwartych portów :("
    else:
        return open_ports
    
    # Przykładowy test skanera portów
    # a = portscanner("wp.pl")
    # print(a)

    
