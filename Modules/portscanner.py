# Kod został zaczerpnięty ze strony https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
# Głównie zależało mi na szybkości (Skaner którego chciałem użyć wcześniej był strasznie wolny)

import threading
import socket #interfejs sieciowy niskiego poziomu

def portscanner(target):
    def portscan(port):    
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#(Adresacja IPV4 , Przesyłanie danych strumieniowo )
        s.settimeout(0.5)# Ustwiamy standardowe opóźnienie
         
        try: #sprawdzenie czy port jest otwarty
            con = s.connect((target,port))#połączenie na porcie
            print(f'Port : {port} Otwarty.')
            con.close()#zakończenie połączenia
        except:#jeśli port jest zamknięty wykonuj dalej
            pass

        
    port_number = 1
    for p in range(1,1024):
        t = threading.Thread(target = portscan, kwargs = {"port" : port_number})
        port_number += 1
        t.start()
