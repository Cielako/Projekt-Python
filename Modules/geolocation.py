from ipstack import GeoLookup
def geolocation(target):
    try: 
        geo_lookup = GeoLookup("8b1261f4d109cc1673a33da38adf9d28") # Klucz do api
        location = geo_lookup.get_location(target) # zebranie informacji dla ip
        if location is None:
            return "Nie udało się znaleźć lokalizacji" # jesli nie uda się znaleźć lokalizacji  
        else:
            geo_info = {"kod kontynentu":"","nazwa kontynentu":"","kod kraju":"","nazwa kraju":"","kod regionu":"","nazwa regionu":"","miasto":"","kod pocztowy":"","szerokość geograficzna":"","długość geograficzna":""}
            del location['location'],location['ip'],location['type']
            for key,value in zip(geo_info.keys(),location.values()):
               geo_info[key] = value
            return(geo_info)
    except Exception as e:
        print(e)
        
# Przykładowy test
# for x,y in zip(geolocation("wp.pl").keys(),geolocation("wp.pl").values()):
    # print(f"{x} : {y}")
