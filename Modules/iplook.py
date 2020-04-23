from iplookup import iplookup

def iplook(adres):
    ip = iplookup.iplookup
    return ip(adres)
 
for r in range(len(iplook("yahoo.com"))):
    print(f"{r+1}: " + iplook("yahoo.com")[r])