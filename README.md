# KSR

# Komponenty

## Prawo Conway'a
* Struktura kodu odzwierciedla strukturę organizacji
* Komponent != serwis - to nie to samo

## Współdzielenia Binarki vs Kodu

### Binarki
* Spory nakład pracy na releasy/wersje itd
* Trochę zamieszanie z CI/CD, dystrybucją

### Kod
* trudno zarzadzać cyklem zmian
* trudno wersjonować np. zbudowanie GUI moze wymagać różnych wersji różnych plików
* trudno ograniczyć wyciek abstrakcji np. klasa car/person/engine będzie miała zupełnie inne odpowiedzialności po stronie GUI i serwerowej

## 3 Zasady Wujka boba
* **REP** (The Reuse/Release Equivalency Principle) - **Jednostką (re)użycia jest release**
	* **Nie można mieć dużej liczby releasów**
	* Oprogramowanie (re)używane jest udostępniane na zewnątrz firmy/zespołu
	* Ktoś musi zarzadzać jego wydaniami
	* Dostęp do wybranych wersji + dokumentacja wersji
	* Informacja o kompatybilności (semantyczne wersjonowanie)
* **CRP** (Common Reuse Principle) - **Klasy w pakiecie są (re)używane razem**
	* **Używa się zawsze całego pakietu**
	* Klasy w pakiecie są dostarczane razem
	* Ponieważ (re)użytkownik musi wziąść cały pakiet - komponenty/klasy powinny być zgrupowane tak by nie trzebabyło używać wielu pakietów.
	* Kontrola wpływu na inne moduły
	* Specyfikacja wymagań/zależności swojego modułu
* **CCP** (Common Closure Principle) - **Zasada wspólnego domknięcia**
	* **Nie możemy wydać pół pakietu, pakiet trzeba wydać w całości**
	* Wydajemy zawsze cały pakiet.
	* Zmiana pakietu implikuje testowanie u jego usera
	* Zmiana wielu pakietów = dużo testowania
	* Zmiana kawałka pakietu = testowanie całego klienta
	* Najlepiej by pakiet był jednorodny: tj. poszczególne składowe pakietu powinny mieć podobne powody do zmian
	* Najlepiej jeśli poszczególne zmiany funkcjonalności implikują wydanie jak najmniejszej liczby pakietów

#### Branche nie powinny żyć zbyt długo!!!

![](https://i.imgur.com/O8NnWjX.png)

## Zależności między pakietami / modułami / komponentami
* **Acyclic Dependencies Principle** - nie powinno być wzajemnych ani cyklicznych zależności
	* prowadzą do niedostabilności
* **Stable Dependancies Principle** - często zmienne rzeczy powinny zależeć od rzadko zmiennych
	* Stabilność - Pakiety stabilne (trudne do zmiany) nie powinny zależeć od niestabilnych (łatwych do zmiany)
* **Stable Abstractions Principle** - packages pakiety stabilne są abstrakcyjne. Pakiety konkretne są zwykle niestabilne. Abtrakcyjność pakietu powinna być proporcjonalna do stabilnosci
	* Byty abstrakcyjne są niezmienne. 
	* Zmieniają się rzeczy konkretne np. przepisy, reguły biznesowe, warunki wyboru strategii

## Zależności
* (Afferent) - kto zależy
* (Efferent) – od kogo zależy

## Miara zależności
* **Niestabilność** - (liczba funkcji/klas/modułów do których odwołuje się X) / ((liczba funkcji/klas/modułów, które zależą od (odwołują sie do) X) + (liczba funkcji/klas/modułów do których odwołuje się X))
* **Abstakcyjność** - (liczba typów abstrakcyjnych) / (liczba typów)

![](https://i.imgur.com/QZh0nsC.png)

# Rozpraszanie

## Po co?
* skalowalność
* dostępność i niezawodność
* ułatwienie utrzymania i rozwoju

## Problemy połączeń
* Sieć nie jest niezawodna
* Opóźnienia
* Słabe pasmo
* Sieć nie jest bezpieczna
* Topologia się zmienia
* Sieć nie jest jednorodna

## Założenia
* System nie jest atomowy/monolityczny
* System nie jest skończony
* Logika biznesowa nie powinna być scentralizowana

## System != Aplikacja
Aplikacja: jeden proces, jeden system, jeden komputer
System: wiele procesów, wiele komputerów, wiele systemów operacyjnych
**System = N*aplikacja + połączenia**

## SOA - Service Oriented Architecture
### Atrybuty Jakościowe które może zapewnić
* **Reusability**
* **Adaptability**
* **Maintainability**

#### SOA to nie jest zbiorem technologii jest ideą, architekturą
**Architektura** Podstawowe koncepcje lub własności systemu ujęte w jego elementach, relacjach, zasadach projektowania i ewolucji

### DEFINICJA
* Service-oriented architecture (SOA) jest stylem architektonicznym pozwalającym na budowę systemów opartych na interakcjach luźno powiązanych, zgrubnych, autonomicznych komponentów nazywanych serwisami
* Każdy serwis udostepnia procesy i zachowania ujete w formie kontraktów i wyrażone w formie komunikatów
* Komunikaty dostępne są pod odkrywalnymi adresmi - punktami dostępowymi (endpoint). Zachowanie serwisu jest określane przez zewnętrzne (w stosunku do niego) polityki. Kontrakt i komunikaty są używane przez inne komponenty systemu nazywane konsumentami serwisu

### Ważne wyrazy
* Autonomiczne usługi - jeden z drugim ma niewiele wspólnego
* Jawne granice - gdzie jest sieć, gdzie się kończy który serwis
* Wspoóldzielenie kontraktu a nie klas/typów
* Kontrakt jest dostępny poprzez komunikaty wysyłane na adres endpoint-ów przez konsumentów serwisu
* Polityka pozwala określić takie atrybuty jak bezpieczeństwo, audyty, SLA i ew. kompatybilność wsteczną
* Polityka vs kontakt (interfejs): Polityka może zmieniać sie w trakcie rune-time-u

### Serwis ws. moduł
* Serwis ma tożsamość (adres), moduł (dll) niekoniecznie
* koszt utrzymania serwisu jest niezerowy, koszt istnienia
* koszt komunikacji z serwisem może być, znaczący moduł może istnieć w przestrznie adresowej
* nie można udawać, że komunikacja nie wpływa na działanie!!! Wołanie zdalne może się nie powieść na różne sposoby

### Problemy
* Utrzymywanie wersji (serwisu!!!) nie jest darmowe
* Sztywność architektury + trudne zmiany kontraktu – ale w sumie chodzi o to aby kontakt zmieniać jak najrzadziej
* Co z kompatybilnością ? jeśli zmiany są konieczne – wersjonowanie
* Diagnostyka, Deploymenty, Dokumentacja
* **Stabilność systemu opartego na synchronicznych wołaniach zależy (czy powinna?) od stabilności sieci/komunikacji**

## Czasami opłaca się zacząć od monolitu aby określić co dzielić w serwisy

# Serwis jako komponent systemu
* Odseparowane (web) serwisy odpowiadające za poszczególne obszary domenowe
* Serwis może mieć własne GUI pozwalające na pracę osobom z odpowiedniego działu
* Synchroniczne wołania usług dostarczanych przez inne oddziały/serwisy/podsystemy

## Działanie
* Dużo zapytań od jednej akcji między serwisami
* Dane są w Bazie Danych i każdy serwis strzela do tej samej bazy
* Usługa może powodować wiele zapytań pośrednich i to jeszcze mnożymy przez Liczbę użytkowników

## Podejście synchroniczne
* Procesy głównie czekają na wyniki/zasoby/potwierdzenie
* Lepszy sprzęt często oznacza, że poświęcamy więcej cykli (szybszego) procesora na czekanie
* Timeout – powoduje ponowienie żądania
* System działa w developmencie a w produkcji

### Czasem nie działa
* Maintenance/awaria/deadlock w jednym podsystemie/serwerze może spowodować degradację/zatrzymanie całego systemu
	* Upadek bazy = utrata danych+ downtime
	* Deadlock = rollback transakcji
	* Upadek serwisu = blad przy wywołaniu
* Zmiana kontraktu serwisu
	* konieczność wersjonowania lub jednoczesne wdrażanie wielu serwisów

## Zależności
* Utrudniają development
* Utrudniają wdrażanie
* Ograniczają stabilność
* Utrudniają zarządzanie i utrzymanie
* Nie można ich wyeliminować ... ale trzeba je ograniczać

## Jak efektywnie redukować zależności
* Zależności w kodzie/danych
	* Na poziomie modułu serwisu Ca, Ce, poprawne użycie abstrakcji, DIC
	* m. serwisami – opieramy się na kontraktach (SOA), nie współdzielimy kodu (biblioteki?)
* Przestrzenne (identyfikacja serwisu) – wirtualne endpoint-y, routowanie
* Czasowe – asynchroniczne komunikaty, zdarzenia

![](https://i.imgur.com/225wRp3.png)

# Async wołania kolejkowe
Na sync wysyłamy i czekamy na odpowiedz

## Problemy WWW
* Czasochłonnym przetwarzaniu
* Dużym obciązeniu (WWW lub bazy)
* Zrównolegleniu WWW
* Rollback (gdy padło WWW)
* Wyjątek i zapis do logu (gdy padła baza)
* Zakleszczenie
* Ponowienia gdy nie działa

## Wołania jednokierunkowe
* Kolejki – możliwa gwarancja dostawy
* Ekspozycja interfejsu przez klienta
* Pooling w oczekiwaniu na odpowiedź

## Wołania async
* Typowa implementacja tworzy nowy wątek, który czeka synchronicznie i wykonuje callback
* Bez zmiany logiki/podejścia klient i tak czeka na wyniki - aby klient miał co robić jak się przetwarza

## Wykorzystanie kolejek
* Można spokojnie założyć, że kolejka jest dostępna
* Kolejki pozwalają odizolować serwer WWW od przetwarzania bazodanowego - klien może chodzić sobie po serwisie
* Serwer WWW wykonuje b. krótkie (“lekkie”) operacje – czyli nie powinien być mocno obciążany przez przetważanie pojedynczego żądania
* Po zapisie zlecenia do kolejki można założyć, że zostanie ono przetworzone
* Nawet upadek serwera bazy lub aplikacji przetwarzajacej spowodują w najgorszym razie zwrócenie komunikatu do kolejki i ponowne przetworzenie po podniesieniu się serwera/aplikacji
* W MSMQ kolejki mogą być na dowolnym komputerze
* Przy zapisie do kolejek zdalnych komunikat trafia to tzw. “outgoing queue” (kolejki tymczasowej) na serwerze lokalnym
* Aplikacja pyta (AJAX/WebSockets) czy pojawiło się potwierdzenie wykonania transakcji

### Można też potokowo przetwarzać rządania, równoważy obciążenia

### Przetwarazania transakcyjne są na całym zadaniu, gdy coś nie pujdzie wymaga wycofania zmian we wszytkich serwisach

## Interakcja z innymi serwisami
* (Nie zawsze) możliwe jest zamknięcie w jednej transakcji cyklu operacji na kilku mediach, web serwsach itd
* W przypadku błędu mozna próbować operacji kompensujących ale jeśli w trakcie takiej próby padnie sama aplikacja – stan system jest niespójny
* Dwa podejścia
	* Próba realizacji operacji jako indempotentne (taki który może być powtarzalny (taki zapis istnieje to fajnie - bez rollbacku)) i zgoda na ew. przetworzenie ponowne
	* Wykorzystanie podzadań – dodatkowych komunikatów zapisanych w transakcji do kolejek
* Tak zwane Koordynatory Tranakcji Rozproszonych (DTS) są zwykle powolne i niewydajne

### Podzadania w kolejkach mogą być np. odpowiedzialne  za operacje na różnych serwisach

### Można robić częściowe uzupełnienia (zapisać niepełne dane)

### Problem i transakcja jest łatwa jeśli jest lokalna
kompensacja - odwrócenie operacji, odczyty spoko ale zapis przypał

## **Wzorzec Adres Zwrotny**
![](https://i.imgur.com/Gleamle.png)

## **Wzorzec: Skorelowane Request/Response**
![](https://i.imgur.com/iR2wpdJ.png)


# Publish Subscribe
* Zdarzenia na poziomie systemowym
	* Wystąpienie zdarzenia oznacza wysłanie komunikatu
	* Obsługa zdarzenia odpowiada obsłużeniu komunikatu
* Zdarzenia powinny być rozpatrywane na poziomie biznesowym (zmienił sie stan, zamówienia, ktoś ma inny adres, rabt)
* Publikując zdarzenie nie czekam na odpowiedź
* Autonomia usługi: do wykonania własnej pracy nie potrzebuje reakcji innych usług.
* Notyfikuję inne usługi o zdarzeniach biznesowych w “ich interesie”
* Jak to się ma do tradycyjnych WS
	* Request/response jest dopuszczalne, ale wołający nie powinien polegać na odpowiedzi – Np. wyświetlenie reklamy, prognozy pogody
	* Na upartego można zrealizować pub/sub na WS – komplikując odpowiednio logike wołającego, tak by był w stanie powtarzać wołania, obsługiwać listę subskrybentów
* jak odbiorca nie działa to nie działa i nie dostaje wiadomości, za odbiór odpowiada odbierający
* publikujący jest właścicielem formatu, rozszerzenie formatu idzie poprzez dziedziczenie interfejsu (nowy interfejs), dziedziczy się po starym interfejsie

## Kolejność zdarzeń
* Nie należy zakładać konkretnej kolejności nadchodzenia komunikatów
	* Możliwe rozwiązanie zapis niekompletnej informacji np. opłacono nieznana fakturę – dane nt. szczegółów przyjdą w przyszłosci
	* W ostateczności można założyć próbę ponownego przetworzenia komunikatu w przyszłości
* Zyski to m. in.
	* Lepsza skalowalność
	* Większa odporność na błędy

## Publish / Subscribe vs kolejki
* Wykorzystanie kolejek do publikacji informacji o zdarzeniach pozwala
	* nadawcy nie czekać na przetworzenie komunikatów przez odbiorcę
	* odbiorcy przetworzyć otrzymane komunikaty w dogodnym momencie
* Niebezpieczeństwo: przepełnienie kolejek
* ServiceBus-y często używają kolejek jako warstwy transportowej

## Subscribe
* Dla redukcji powiazań przestrzennych (spatial coupling) możliwe jest mapowanie między typem komunikatu i adresem sewisu odbiorcy (nadawca nie musi więc wiedzieć kto jest odbiorcą)
* Subskrypcja oznacza gotowość do obsługi danego typu komunikatów
	* rejestracja handlera (-> Bus) oznacza właśnie subskrypcje
	* może przekładać się na wysłanie wewnętrznych komunikatów w obrębie infrastruktury
	* Zwykle założenie subskrypcji oznacza zapamietanie adresu handlera/kolejki, której używa

## Styl architektoniczny Broker
![](https://i.imgur.com/6EK9M6J.png)

### Cechy Broker-a
* Broker jest fizycznie odseparowany
* Cała komunikacja odbywa się przez niego
* Broker musi obsłużyć upadki serwisów i przekazywanie wiadomości
* Broker stanowi “single point of failure” – musi być wydajny i niezwykle stabilny
* **Zalety**
	* Dzieki skoncentrowaniu komunikacji w jednym miejscu łatwo zarządzać centralnie konfiguracją
	* Łatwe jest uzyskanie inteligentnego przekazywania danych, transformacje, orkiestracje
	* Nie wymaga wielu zmian w serwisach
* **Wady**
	* Narusza autonomię serwisów
	* Stanowi “single point of failure” i b. często jest wąskim gardłem


## Styl architektoniczny Szyna
![](https://i.imgur.com/UBSzSnQ.png)

### Cechy Szyny
* Szyna niekoniecznie jest fizycznie odseparowana
	* Kanały mogą być zarówno fizyczne jak logiczne
* Komunikacja jest rozproszona pomiedzy wieloma kanalami
* Szyna jest koncepcyjnie prostsza
* Brak ”single point of failure” (dla niektorych/wszystkich operacji/implementacji)

### Zalety Szyny
* Brak “single point of failure”
* Nie narusza autonomii serwisu
* The “anti-broker”

### Wady szyny
* Trudniejsza do zaprojektowania niż Broker
* Czasem trudno rozróżnić

![](https://i.imgur.com/TST1ada.png)

# Serwisy - skalowalność
* Serwis jest techniczną realizacją pewnych biznesowych możliwości
* Serwis powinien być niezależny
* Granice serwisu - za co ja odpowiadam
* Baza Danychnie jest serwisem tylko CRUD

### Żaden serwis nie jest właścicielem strony

## Posadowienie serwisów
* Jeden komputer może gościć wiele serwisów
* Jedna aplikacja może obejmować wiele serwisów
* Pojedynczy workflow może angażować wiele serwisów
* Pojedyncza strona może łączyć dane z wielu serwisów

## Trzeba przygotować się że dane w systemie mogą być nieaktualne

## CAP theorem

### Nie można zbudować systemu, który spełni jednoczesnie 3 postulaty
* Spójność (Consistency)
* Dostępnośc (Availiability)
* Odporność na podziały (Partition tolerance)

### Można wybrać dwa
* CA (SD) – Brak podziałów oznacza monolit
* CP (SO) – Spójny, ale pot. niedostępny w przypadku problemu z wewn. transmisjami
* **AP** (DO) – Dostępny, ale potencjalnie lokalnie niespójny – Eventual Consistency - stabilizuje się po czasie

#### AP – przykład 1: Request/Response
#### AP – przykład 2: Pub/Sub

## Cache = efektywność działania + problemy spójności
* Dane zmieniają się często
* Zapytania powinny być proste
	* Normalizacja implikuje zapytania oparte na wielu tabelach
	* Widoki kosztują

![](https://i.imgur.com/sQivGHc.png)

## CQRS - Common Query Responsibility Segregation - używa rozspojenia
* Oddzielne dane do zapisu i odczytu (rozdzielić update i write oraz komędy i zapytania)
* Komendy są przetwarzane oddzielnie od zapytań
* Wynik aktualizacji danych jest replikowany dowidoku zapytań (cache)
* Możliwe jest w przechowywanie tylko listy komend i bieżącego stanu w cache – (wzorzec Event Sourcing)
* CQRS – to nie jest wzorzec wysokopoziomowy tj. Nie pnadaje się do oparcia na nim architektury całego systemu – to rozwiązanie taktyczne (lokalne)
* Nieaktualne dane -> no trudno odświeży sobie
* Co jakiś czas trzeba zainicjalzować/aktualizowć cache
* Jak się coś zmieniło to powinno się poinformować usera i poczekać na jego decyzję (kolizja updatów)

## Nowoczesny interfejs
* Może wcale nie trzeba korzystać z nieaktualnych danych lub nie trzeba ich pokazywać
* Ważne jest uchwycenie intencji
* Można troche “oszukać”
	* Wysyłka może pójść na adres, który był aktualny kilka minut wcześniej
	* Nie można oczekiwać, że zawsze uda sie rezygnacja z wysyłki w ciagu kilku sekund
	* Właściwy zakup udbywa sie przy potwierdzeniu a nie kliknieciu "kup teraz"

## Drobne optymalizacje i oszustwa
* Walidacja przed wysłaniem
* Odgadywanie zmian
* Bezpośrednia aktualizacja widoku na podstawiwie komendy przed wprowadzeniem i przetworzeniem zmian przez BackEnd

## Komenda vs. encja
* Łatwiej walidować komendę
	* z mała iloscią danych
	* bardziej konkretną
	* Chodzi o potencjalną poprawność (wynik walidacji nie jest ostateczny)
* Walidacja dużych encji jest trudna


# Mikro Serwisy uSOA
Dobry monolit nie jest zły, łatwiej startować od monolitu, ale przejście na serwisy kosztuje lecz pieniądze oszczędza się na monolicie
![](https://i.imgur.com/ODQmqTJ.png)
logika i dopinanie providerów
![](https://i.imgur.com/wJzZTgE.png)
![](https://i.imgur.com/D7N1vwY.png)

## uUsługa
* Mały, niezależny
* Rozmiar – różne miary => do przepisania przez tydzien ?
* Niezależny (autonomiczny?) możliwy do niezależnego
	* rozwoju
	* wdrażania
	* działania

### Zalety
* Mały = Łatwy do zrozumienia, analizy
* Niezależny (to wymaganie raczej niż zaleta)
* Pot. krótkie wydania, szybkie wdrożenia
* Możliwość łatwego zastąpienia (przepisania) pojedynczej usługi
* Podatność na eksperymenty, rozwój
* Można skalować usługi zamiast całego systemu, równoważenie obciążenia, cache-owania (REST)

### Wady
* B. duże znaczenie infrastruktury – problem techniczne – na nast. slajdzie - **Dużo komunikacji, ja tego kodu nie pisałem, nie wiem co się skopało**
* Monitoring, monitoring, monitoring!
* Łatwo przesadzić z rozdrobnieniem – gdzie powinna być granica m. serwisami
	* Antywzorzec – nanoserwisy
* Integracja przez bazę to zły pomysł

### Zagadnienia
* lekkie hostowanie serwisów
* (auto)rejestracja + (auto)discovery
* wersjonowanie
* Równoważenie obciążenia
* caching
* kontola dostępu
* pomiar wydajności API i monitorowanie
* testowanie (jednostkowe, kontakty, integracyjne, systemowe)

![](https://i.imgur.com/p44wigI.png)
![](https://i.imgur.com/hxQnfdj.png)

## Ekosystem uUsług
* W1 **Sprzęt**: fizyczne serwery, bazy danych, system operacyjny, zarządzanie konfiguracją, monitorowanie i logowanie na poziomie hosta
* W2 **Komnikacja**: sieć, DNS, RPC, endpointy, messaging, service discovery, service rejestry, równoważenie obciążenia
* W3 **Platforma Aplikacyjna**: środowisko wytwórcze, testy, pakiety, budowanie, potok wdrożeniowy, monitorowanie i logowanie na poziomie serwisu
* W4 **Mikroserwis**: logika uUsługi, konfiguracja na poziomie uUsługi

## Organizacja - wyzwania
* Odwrotne prawo Conwaya
* Technologiczna gorączka
* Więcej sposobów by upaść
* Wyścig po zasoby

## Gotowość „produkcyjna”
* Cykl wytwórczy
* Cykl wdrożeniowy
* Wprowadzanie/likwidowanie usług
* Planowanie, adresowanie i ochrona przed problemami z zależnościami
* Niezawodny routing i discovery
* Skalowalność i wydajność
* Monitoring
* Dokumentacja

![](https://i.imgur.com/NI81VlQ.png)

![](https://i.imgur.com/N8VkekX.png)
pełny stage (całe środowisko odwzorowane) vs częściowy stage (część środowiska odwzorowane)

## Pomysły na procedurę wdrażania
* Rolling deployment - potok
* Canary release - wdrażanie systemu, przepuszcza się część ruchu i sprawdza się czy działa
* Blue/green release - dwa środowiska, działają równolegle, zamiany -> trzeba utrzymywać dwie
* Wyzwania
	* routing/discovery
	* patching vs. budowa od początku
	* rollback vs. „ucieczka do przodu” - spr czy zadziała, poprawka to nie rollback ale kolejne wydanie
	* zarządzanie zależnościami (rejestracja/usuwanie)

## Tolerowanie błedów/przygotowanie
* Przygotowanie na błędy/problemy z zależnościami
* Netflix: Chaos monkey


# Patenty
### Klient chce Funckjonalności!!!
### O czym się nie myśli
* Reakcja na sytuacje wyjątkowe
* Problemy z siecią/serwisami
* Instalacja
* Diagnostyka
* Przywracanie systemu do życia
* Monitoring

## 12 factor apps
1. Codebase
	* Jedno źródło kodu śledzone systemem kontroli wersji, wiele wdrożeń
2. Zależności
	* Jawnie zadeklaruj i wydziel zależności
3. Konfiguracja
	* Przechowuj konfigurację w środowisku
4. Usługi wspierające
	* Traktuj usługi wspierające jako przydzielone zasoby
5. Buduj, publikuj, uruchamiaj
	* Oddzielaj etap budowania od uruchamiania
6. Procesy
	* Uruchamiaj aplikację jako jeden lub więcej bezstanowych procesów
7. Przydzielanie portów
	* Udostępniaj usługi przez przydzielanie portów
8. Współbieżność
	* Skaluj przez odpowiednio dobrane procesy
9. Zbywalność
	* Zwiększ elastyczność pozwalając na szybkie uruchamianie i zatrzymywanie aplikacji
10. Jednolitość środowisk
	* Utrzymuj konfigurację środowisk jak najbardziej zbliżoną do siebie
11. Logi
	* Traktuj logi jako strumień zdarzeń
12. Zarządzanie aplikacją
	* Uruchamiaj zadania administracyjne jako jednorazowe procesy


### Jak są błędy to najlepiej lokalne

### Punkt integracji, ważne aby błąd w jednym serwisie nie rozsypał całego systemu

### Punkt upadku
Każdy punk integracji może zrobić bum, nie wiadomo gdzie, jak często i czy można go przewidzieć oraz jakie straty spowoduje

## Najgorszy błąd to brak odpowiedzi

## Fail Fast - jeśli upaść to szybko
* Seceariusz
	* baza serwisu obsługa klientów ledwo żyje (właśnie liczony jest roczny raport).
	* próbujemy kupić coś w sklepie (jak wielu innych)
* Dużo lepiej szybko zasygnalizować błąd niż próbować obsłużyć go na niskim poziomie np. przez powtórzenia
* Dla bazy danych czasami powtórzenie może mieć sens (np. w przypadku deadlock-ów)
* Lepiej zwalidować dane przed a nie na końcu transakcji
* Lepiej upewnić się, że mamy potrzebne wszystkie zasoby zanim rozpoczniemy czasochlonne przetwarzanie (np. zawołamy zewnętrzne serwisy)
* Przy problemach dobrym pomysłem jest „recykling” usługi
* Odpowiedzialność usługi: wyłącz się
* Odpowiedzialność infrastruktury podnieś/zrestartuj usługę

## Shed Load
* Przy przeciążeniu niezłe może być zachowanie zbliżone do protokołu TCP – jawne odrzucanie zleceń

## Time Out
* Zawsze gdy tylko można powinien być ustawiany
* Zwykle warto dać możliwość konfiguracji

## Circuit Breaker
* Jeśli serwis np. marketingu stwierdza, że ma problem z baza (np długi czas odpowiedzi) od razu raportuje błąd np. przez 1 min żeby dać czas bazie na podniesienie się.

## Hand Shaking - pytania o status przed wysłaniem zadania, tani sposób sprawdzenia czy app działa
* Zamiast od razu pytać serwis o pot. duże dane (zwłasza na starcie lub po jakimś czasie bezczynności) można najpierw zapitać go o status
* Może odpowiadać, że jest mocno zajęty, że jest gotowy, albo nie odpowiadać -> to też odpowiedz

## Slow responses
* Ulubione zajęcie znudzonego klienta: “Odśwież”
* Długi czas odpowiedzi:
	* Blokuje łańcuch pytających - wątki, pamięć
* Ew. timeout i ponowienie nie anulują poprzedniego żądania, czyli jest jeszcze gorzej
* Co z pomysłem by nie obsługiwać kolejnyć żadań z tego samego IP

## SLA


## User to zło konieczne
* Mało kupujący - jedna grupa serwisów
* Kupujący - druga lepsza grupa serwisów
* Super Klienci - specjalna grupa serwisów

## Sesje - lekkie a najlepiej wcale
* Użytkownik nie wie co to zamykanie sesji – ulubiony sposób wyjścia to przejście gdzie indziej, a nie wyloguj
* Bot nie obsługuje ciastek – co oznacza … domyślnie nową sesję dla każdego żądania
* Można wynieść dane z pamięci serwera WWW

## Przy upadaniu instancji obciążenie na inne wzrasta, należy o tym pamiętać

## System Powinien znieść wszystko
* dobrze działać w typowych warunkach
* przetrwać (niekoniecznie super wydajnie) ektremalne warunki – promocje, święta

## Bulkheads
* Warto rozważyć oddzielne QoS dla różnych typów klientów, usług itd np. przez wydzielenie oddzielnych podsystemów
* Kompromis: skalowanie vs. stabilność

## Wycieki
* Pamięć
* Połączenia do bazy,
* Wątki
* Duży problem dla długo działających aplikacji

## Diagnostyka
* Monitorowanie: pamięć, dysk, zasoby, sieciowe wołania, wolumen danych, stan punktów integracji
* Logowanie: wyjątki, błędne wołania, problemy sieciowe (+ kontekst), ale bez ujawniania szczegłów użytkownikom

## Fiddling
* Aplikacja wymaga restartów
* Aplikacja wymaga czyszczenia dysku (rolowanie logów)
* Skomplikowany start/restart
* Trudna konfiguracja

## Health Check
* Strona z syntetyczną prezentacją stanu systemu
* Self testy

## Test Harnes
* Testy automatyczne nie zastąpią testerów
* Przy wysokopoziomowym testowaniu (manualnym) testujemy nie tylko “heapy path”
* Staramy się być dociekliwi, nieprzewidywalni, po prostu wredni
* TH = oznacza pot. wykorzystanie symulatora klienta
	* Wyjmowanie kabelkow sieciowych to wcale nie taki zły pomysł.
	* złośliwe generowanie dużych zwrotów czy psucie danych może być trudne do uzyskania w normalnym trybie testowania



