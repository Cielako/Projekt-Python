from ipstack import GeoLookup
geo_lookup = GeoLookup("8b1261f4d109cc1673a33da38adf9d28") # Klucz do api
location = geo_lookup.get_own_location() # Test własnego adresu ip
print(location)