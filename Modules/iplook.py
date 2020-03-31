from iplookup import iplookup

def iplook(adres):
    ip = iplookup.iplookup
    print(f"Trasa przebiegu dla adresu: https://{adres} \n--------------------------------------------------")
    for r in range(len(ip(adres))):
        print(f"{r+1}:",ip(adres)[r])