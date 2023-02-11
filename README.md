# ARPattack

The goal of the project is to analyze and understand the mechanism of the ARP protocol and its potential for use in Man-in-the-Middle attacks.

## Intro

### Address Resolution Protocol

ARP – (ang. Address resolution protocol) jest protokołoem sieciowym używanym do mapowania adresów IP na adresy MAC w sieciach lokalnych (LAN). Jest to niezbędne ponieważ wiele urządzeń w sieci LAN, takich jak routery, komputery komunikują się za pomocą adresów MAC, podczas gdy protokoły komunikacji takie jak TCP i UDP, używają adresów IP.
Protokół ARP jest protokołem znajdującym się w warstawie łącza danych (ang. Data Link Layer) w modelu ISO/OSI. Warstwa ta odpowiada za transmisję danych pomiędzy urządzeniami w sieci LAN. 

### Atak ARP spoofing

Atak ARP spoofing składa się z dwóch faz. W pierwszej fazie atakujący wysyła ofierze fałszywą odpowiedź ARP, stwierdzając, że adres MAC atakującego jest mapowany na adres IP routera. Pozwala to napastnikowi oszukać ofiarę, że komputer atakującego jest routerem. Podczas drugiej fazy ofiara akceptuje fałszywy pakiet ARP wysłany przez atakującego i aktualizuje mapowanie w swojej tabeli ARP, aby odzwierciedlić, że adres MAC atakującego jest teraz mapowany na adres IP routera. Oznacza to, że ruch internetowy będzię kierowany do maszyny atakującego zamiast do routera. 
Jeśli atakujący też chce przechwycić ruch internetowy przeznaczony dla ofiary, musi również oszukać router, aby przesłał mu ruch ofiary. Dlatego atakujący musi stworzyć fałszywy pakiet ARP wskazujący, że adres IP ofiary jest mapowany na adres MAC atakującego. Dzięki temu atakujący może przechwycić i zbadać przychodzący ruch internetowy, a następnie przekazać ten ruch ofierze. 

## Descritpion 
arpSpoof.py - Narzędzie, które zostało opracowywane, umożliwia generowanie i wysyłanie sfałszowanych pakietów ARP do różnych urządzeń znajdujących się w sieci, takich jak ofiara i router. Celem ataku jest manipulowanie tabelą ARP w celu uzyskania kontroli nad ruchem sieciowym. Po zakończeniu ataku, narzędzie automatycznie przywraca tabelę ARP do stanu pierwotnego, aby uniknąć wykrycia a także dalszych problemów związanych siecią.

Requirements:

Python 3.x
Wireshark

## Installation and Usage
Clone this repository.
Using pip:
pip3 install --pre scapy[basic] 
Run the Python 3 code in the terminal (or command prompt).
sudo python3 arpSpoof.py <IP_VICTIM> <ROUTER_IP> 

## Wykonywanie ataku ARP spoofing 

Adres IP atakującego:

![my_ip_attack](https://user-images.githubusercontent.com/70896562/218270119-2954c4b8-1471-4f6d-81ee-842b36dad3a2.png)



Topologia sieci
![image](https://user-images.githubusercontent.com/70896562/218267731-61aaec0b-a68a-44b0-895f-dc982a063309.png)

1. Na początku ataku, przeprowadzane jest skanowanie sieci, którego celem jest identyfikacja hostów znajdujących się w sieci. Skanowanie pozwala na zgromadzenie informacji o adresach IP i MAC urządzeń, które są częścią sieci, co jest niezbędne do dalszego działania ataku.

![scan_network](https://user-images.githubusercontent.com/70896562/218269914-ca036fc2-403e-43b2-a830-89039b023e1e.png)


2. Po uzyskaniu adresów IP hostów w sieci, uruchamiamy skrypt "arpspoof.py", którego celem jest przekazywanie fałszywych odpowiedzi i manipulowanie tabelą ARP. Dzięki wykorzystaniu tego skryptu, jesteśmy w stanie zmienić zawartość tabeli ARP w celu przekierowania ruchu sieciowego przez nasze urządzenie, co pozwala na monitorowanie i ewentualne zmodyfikowanie danych przesyłanych w sieci. W ten sposób, uzyskujemy kontrolę nad ruchem sieciowym i możemy wykonać atak typu Man-in-the-Middle.

![command_attack](https://user-images.githubusercontent.com/70896562/218269945-ae367823-e8bb-4602-81d5-862d3247776b.png)

Topologia po wykonaniu skryptu
![Network (1)](https://user-images.githubusercontent.com/70896562/218269863-6abe5aa2-4602-4094-860c-b2aa6d57c255.svg)

3. Poprzez wysyłanie fałszywych odpowiedzi ARP, celowo wprowadzamy ofiarę w błąd, sugerując, że nasz adres MAC jest adresem IP serwera Metaploitable. Dzięki takiemu działaniu, ofiara uważa, że nasze urządzenie jest punktem końcowym, do którego powinny być skierowane wszystkie dane przesyłane w sieci.

![mac_router_spoof](https://user-images.githubusercontent.com/70896562/218271191-ac55da1e-04ac-429d-88e2-9ae61ce92b36.png)


Podobnie jak w przypadku ofiary, serwer również musi być celowo zmanipulowany poprzez wysłanie fałszywych odpowiedzi ARP, aby umożliwić przechwytywanie ruchu ofiary. Dzięki takiemu działaniu, serwer uważa, że nasze urządzenie jest punktem końcowym, do którego powinny być skierowane wszystkie dane przesyłane przez ofiarę.

![mac_spoof](https://user-images.githubusercontent.com/70896562/218271229-ef3dd155-4843-4ea0-9e87-2a5043146aba.png)

Tabela ARP

![tabela_arp](https://user-images.githubusercontent.com/70896562/218271320-9c0c5ef5-8c35-41e9-8aff-7ad3bcdfb443.png)

Uzyskanie poświadczen podczas gdy ofaira loguje sie na serwer phpadmin:

Wpisywanie poświadczen przez ofiare:

![cerficication_ubuntu](https://user-images.githubusercontent.com/70896562/218271365-ce27654a-81c9-458d-9c84-94dbf8c4f47e.png)

Otrzymany ruch przez atakujacego:

![get_password](https://user-images.githubusercontent.com/70896562/218271419-f0479c28-752b-4d22-8630-f62363088133.png)

Uzyskanie podświdcze podczas logowanie na serwer FTP przez ofiare 

![logowanie_ftp](https://user-images.githubusercontent.com/70896562/218271500-52cc8b7a-c70f-46e1-8ebb-714fbff11761.png)

Uzyskanie poświadczen przez atakujacego: 

![ftp_cert](https://user-images.githubusercontent.com/70896562/218271543-ef59e9a0-bef6-42c3-affb-0053aea1d200.png)


Tablea ARP po zakończeniu skryptu: 

![restore_arp](https://user-images.githubusercontent.com/70896562/218271603-f68db1bd-2141-4fe4-b07e-ce6f4d236a9f.png)





