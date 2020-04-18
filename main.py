from Modules.iplook import iplook
from Modules.geolocation import geolocation

print(iplook("wp.pl"))# test skanera portów

for x,y in geolocation("wp.pl").items():# test geolokalizacji
    print(f"{x} : {y}")