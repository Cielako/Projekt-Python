import whois
import re
def domain_info(target):
    domain_info = {"Nazwa domeny":"", "Nazwy serwerów": "", "Rejestrator":"", "Adres url rejestratora":"", "Status":"", "Nazwa rejestratora":"", "Data utworzenia":0, "Data wygaśnięcia":0, "Data aktualizacji":0}
    w = whois.whois(target)
    for key,value in zip(domain_info.keys(),w.values()):
        str(value).split()
        domain_info[key] = str(value)
    return domain_info
#test    
#for x,y in zip(domain_info("wp.pl").keys(),domain_info("wp.pl").values()):
    #print(f"{x} : {y}")