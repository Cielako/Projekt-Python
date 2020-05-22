import whois

def domain_info(target):
    #domain_info = {"Nazwa domeny":"","Rejestrator":"","Serwer whois":"","Referencyjny adres url":"","Data aktualizacji":"","Data utworzenia":"","Data wygaśnięcia":"", "Nazwy serwerów": "","e-maile":""}
    w = whois.whois(target)
    #del w['status'],w['dnssec'],w['name'],w['org'],w['address'],w['city'],w['state'],w['zipcode'],w['country']
    for key,value in zip(w.keys(),w.values()):
        if w[key] == None:
            w[key] = "Brak informacji"
        else:
            w[key] = value
    return w

#test    
#for x,y in zip(domain_info("yahoo.com").keys(),domain_info("yahoo.com").values()):
    #print(str(f"{x} : {y}"))