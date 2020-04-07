# PWJS - O programie  IPSI (Internet Protocol Simple Information)
(?) Oznacza dodatkowe założenia, które na ten czas są w planach, lecz mogą ulec zmianie
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
- Dodatkowe informacje, które mogą być trakotwane jakkolwiek jako przydatne 
# 3. Technologia 
- W głównej mierze wykorzystanie Pythona w połączeniu z bibliotekami(PyQt5/Tkinter,IplookUp, etc.).
- Ewentualnie inne technologie, mogące przyspieszyć tworzenie projektu. (?)
# 4. Lista Zadań
- [x] Nazwa aplikacji
- [x] Główne założenie działania aplikacji
- [ ] Tester osiąglaności witryny
- [x] Trasa adresów pomiędzy hostem a witryną (moduł)
- [x] Tester portów (moduł)
- [ ] Czas jaki upłynął do połączenia się z witryną
- [ ] Tester pingu (moduł)
- [ ] info o systemie operacyjnym witryny (moduł)
- [ ] Przybliżona lokalizacja adresu witryny (moduł)
- [ ] Generowanie raportu (z informacjami na temat konkretnej witryny)
- [ ] Możliwość zapisu raportu do pliku tekstowego
- [ ] Pomysł na wygląd interfejsu graficznego
- [ ] Implementacja systemu graficznego w aplikacji





