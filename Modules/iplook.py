from iplookup import iplookup

def iplook(target):
    ip = iplookup.iplookup
    return ip(target)
 
# Przykładowy test modułu 
#for r in range(len(iplook("yahoo.com"))):
    #print(f"{r+1}: " + iplook("yahoo.com")[r])