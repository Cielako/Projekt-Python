# PWJS - O programie  IPSI (Internet Protocol Simple Information)
(?) - Oznacza dodatkowe założenia, które na ten czas są w planach, lecz mogą ulec zmianie
(Test) - Moduł niedokończony
# 1. Pomysł 
- Stworzenie aplikacji mającej za zadanie zbieranie informacji o poszczególnym adresie strony internetowej.
- Wdrożenie do aplikacji systemu logowania na pocztę(prawdopodobnie gmail) i przesyłanie danych pobranych z witryny na wybrany adres e-mail (?)
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
  - #iplookup (ver. 1.0.5 [click](https://pypi.org/project/iplookup/ "click") 
  - ipstack  (ver. 0.1.4)
  - PyQt5 / Tkinter
- Ewentualnie inne technologie, mogące przyspieszyć tworzenie projektu. (?)
# 4. Lista Zadań
  ### Moduły:
- [x] Tester osiąglaności witryny + Czas trwania łączenia się z witryną
- [x] Trasa adresów pomiędzy hostem a witryną 
- [x] Tester portów
- [ ] Site info mailer (Test) (?)
- [ ] Tester pingu 
- [ ] Geolokalizacja adresu witryny (Test) 
- [ ] Generowanie raportu o witrynie + dodatkowe opcje (np. zapis lub wysłanie raportu)
  
  ### Główne:
- [x] Nazwa aplikacji
- [x] Założenia działania aplikacji
- [ ] Utworzenie wszystkich modułów aplikacji
- [ ] Pomysł na wygląd interfejsu graficznego
- [ ] Implementacja interfejsu graficznego w aplikacji
  
  ### Poboczne:





