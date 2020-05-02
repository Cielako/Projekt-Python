import whois
def domain_info(target):
    domain_info = {"nazwa domeny":"", "nazwy serwerów": "", "rejestrator":"", "adres url rejestratora":"", "status":"", "nazwa rejestratora":"", "data utworzenia":"", "data wygaśnięcia":"", "data aktualizacji":""}
    w = whois.whois(target)
    for key,value in zip(domain_info.keys(),w.values()):
        domain_info[key] = value
    return domain_info
    
print(domain_info("wp.pl"))