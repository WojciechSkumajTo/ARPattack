# ARPattack

The goal of the project is to analyze and understand the mechanism of the ARP protocol and its potential for use in Man-in-the-Middle attacks.

## Intro

### Address Resolution Protocol

ARP – (ang. Address resolution protocol) jest protokołoem sieciowym używanym do mapowania adresów IP na adresy MAC w sieciach lokalnych (LAN). Jest to niezbędne ponieważ wiele urządzeń w sieci LAN, takich jak routery, komputery komunikują się za pomocą adresów MAC, podczas gdy protokoły komunikacji takie jak TCP i UDP, używają adresów IP.
Protokół ARP jest protokołem znajdującym się w warstawie łącza danych (ang. Data Link Layer) w modelu ISO/OSI. Warstwa ta odpowiada za transmisję danych pomiędzy urządzeniami w sieci LAN. 

### Atak ARP spoofing

Atak ARP spoofing składa się z dwóch faz. W pierwszej fazie atakujący wysyła ofierze fałszywą odpowiedź ARP, stwierdzając, że adres MAC atakującego jest mapowany na adres IP routera. Pozwala to napastnikowi oszukać ofiarę, że komputer atakującego jest routerem. Podczas drugiej fazy ofiara akceptuje fałszywy pakiet ARP wysłany przez atakującego i aktualizuje mapowanie w swojej tabeli ARP, aby odzwierciedlić, że adres MAC atakującego jest teraz mapowany na adres IP routera. Oznacza to, że ruch internetowy będzię kierowany to maszyny atakującego zamiast do routera. 
Jeśli atakujący też chce przechwycić ruch internetowy przeznaczony dla ofiary, musi również oszukać router, aby przesłał mu ruch ofiary. Dlatego atakujący musi stworzyć fałszywy pakiet ARP wskazujący, że adres IP ofiary jest mapowany na adres MAC atakującego. Dzięki temu atakujący może przechwycić i zbadać przychodzący ruch internetowy, a następnie przekazać ten ruch ofierze. 

## Descritpion 
arpSpoof.py - Narzędzie, które zostało opracowywane, umożliwia generowanie i wysyłanie sfałszowanych pakietów ARP do różnych urządzeń znajdujących się w sieci, takich jak ofiara i router. Celem ataku jest manipulowanie tabelą ARP w celu uzyskania kontroli nad ruchem sieciowym. Po zakończeniu ataku, narzędzie automatycznie przywraca tabelę ARP do stanu pierwotnego, aby uniknąć wykrycia a także dalszych problemów związanych siecią.

Requirements:

Python 3.x

## Installation and Usage
Clone this repository.
Using pip:
pip3 install --pre scapy[basic] 
Run the Python 3 code in the terminal (or command prompt).
sudo python3 arpSpoof.py <IP_VICTIM> <ROUTER_IP> 
