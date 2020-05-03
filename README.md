# PWJS - O programie  IPSI (Internet Protocol Simple Information)
(?) - Oznacza dodatkowe założenia, które na ten czas są w planach, lecz mogą ulec zmianie <br>
(Test) - Moduł niedokończony
# 1. Pomysł 
- Stworzenie aplikacji mającej za zadanie zbieranie informacji o poszczególnym adresie strony internetowej.
- Wdrożenie do aplikacji modułu wysyłającego raport na podany adres e-mail(?)
- Zaprojektowanie intuicyjnego gui dla potencjalnego użytkownika. 
- Ewentualne rozbudowanie programu o dodatkowe funkcje, w miarę rozwoju projektu 
# 2. Plan działania aplikacji
Zbieranie informacji takich jak:
- Czas jaki upłynął (do momentu prawidłowego połączenia się z witryną internetową)
- Trasa przepływu sygnału pomiędzy hostem a witryną (adresów sieciowych prowadzących do adresu docelowego)
- Sprawdzanie portów dla standardowych usług internetowych (Otwarty/Zamknięty)
- Przyblibiżona lokalizacja docelowego adresu internetowego
- Dodatkowe, które mogą być trakotwane jakkolwiek jako przydatne 
# 3. Technologia 
- W głównej mierze wykorzystanie Pythona w połączeniu z bibliotekami:
  - iplookup (ver. 1.0.5) [click](https://pypi.org/project/iplookup/) 
  - ipstack  (ver. 0.1.4) [click](https://pypi.org/project/ipstack/)
  - PyQt5    (ver. 5.13.0)[click](https://pypi.org/project/PyQt5/)
  - whois    (ver. 0.7.2) [click](https://pypi.org/project/python-whois/0.7.2/)
- Ewentualnie inne technologie, mogące przyspieszyć tworzenie projektu. (?)
# 4. Lista Zadań
  ### Moduły:
- [x] Tester osiąglaności witryny + Czas trwania łączenia się z witryną
- [x] Trasa adresów pomiędzy hostem a witryną 
- [x] Tester portów
- [x] Site info mailer (Test) (?)
- [ ] Tester pingu 
- [x] Geolokalizacja adresu witryny (Test) 
- [x] Whois (informacje teleadresowe o domenie) (Test)
- [ ] Generowanie raportu o witrynie + dodatkowe opcje (np. zapis lub wysłanie raportu)
  
  ### Główne:
- [x] Nazwa aplikacji
- [x] Założenia dotyczące działania aplikacji
- [ ] Utworzenie wszystkich modułów aplikacji
- [x] Pomysł na wygląd GUI
- [x] Utworzenie Szablonu GUI
- [ ] Implementacja GUI w aplikacji
  
  ### Poboczne:
- [ ] Lokalizacja i korekta błędów w aplikacji
- [ ] Poprawa GUI (?)

  ### Raporty:
 - [x] Propozycja projektu (13.03.20)
 - [x] Raport I (03.04.20)
 - [x] Raport II (24.04.20)
 - [ ] Raport III (15.05.20)
 - [ ] Raport IV/Prototyp (29.05.20)
 - [ ] Prezentacje/oddanie projektu (19.06.20)



