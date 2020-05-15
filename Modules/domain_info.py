import whois
import re

def domain_info(target):
    domain_info = {"Nazwa domeny":"","Rejestrator":"","Serwer whois":"","Referencyjny adres url":"","Data aktualizacji":"","Data utworzenia":"","Data wygaśnięcia":"", "Nazwy serwerów": "","e-maile":""}
    w = whois.whois(target)
    del w["status"]
    for d_key,key,value in zip(domain_info.keys(),w.keys(),w.values()):
        if w[key] == None:
            domain_info[d_key] = "Brak informacji"
        else:
            domain_info[d_key] = value
    return domain_info
    #return w
#print(domain_info("ikea.com"))

#test    
#for x,y in zip(domain_info("yahoo.com").keys(),domain_info("yahoo.com").values()):
    #print(str(f"{x} : {y}"))