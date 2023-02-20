# ARPattack

The goal of the project is to analyze and understand the mechanism of the ARP protocol and its potential for use in ***Man-in-the-Middle***.

## Intro

### Address Resolution Protocol

ARP - _(Address resolution protocol)_ is a network protocol used to map IP addresses to MAC addresses on local area networks _(LAN)_. This is necessary because many devices on a LAN, such as routers, computers communicate using MAC addresses, while communication protocols such as TCP and UDP, use IP addresses.

The ARP protocol is a protocol found in the Data Link Layer of the ISO/OSI model. This layer is responsible for the transmission of data between devices on a LAN.

### Atak ARP spoofing

**This attack consists of two stages:**
1. In the first stage, the attacker sends a fake ARP response to the victim, stating that the attacker's MAC address is mapped to the router's IP address. This allows the attacker to fool the victim into thinking that the attacker's computer is a router.

2. During the second stage, the victim accepts the fake ARP packet sent by the attacker and updates the mapping in its ARP table to reflect that the attacker's MAC address is now mapped to the router's IP address. This means that Internet traffic will be routed to the attacker's machine instead of the router. 

If the attacker also wants to intercept Internet traffic destined for the victim, he must also trick the router into sending the victim's traffic to him. Therefore, the attacker must create a fake ARP packet indicating that the victim's IP address is mapped to the attacker's MAC address. This allows the attacker to intercept and examine incoming Internet traffic and then forward that traffic to the victim.

## Description 

`arpSpoof.py` - a tool that has been developed, enables the generation and sending of forged ARP packets to various devices on the network, such as the victim, router or server. The goal of the attack is to manipulate the ARP table in order to gain control over network traffic. Once the attack is complete, the tool automatically restores the ARP table to its original state to avoid detection and also further network-related problems.

## Requirements:

- Python 3.x
- Wireshark
- nmap

## Installation and Usage

- Clone this repository.
- Using pip:
```shell
  pip3 install --pre scapy[basic] 
```
- Run the Python 3 code in the terminal (or command prompt):
```shell
  sudo python3 arpSpoof.py <IP_VICTIM> <ROUTER_IP>
```

## Execution of an ARP spoofing attack 

### General information
![my_ip_attack](https://user-images.githubusercontent.com/70896562/218270119-2954c4b8-1471-4f6d-81ee-842b36dad3a2.png)
|:--:| 
| *IP address of the attacker* |

<br/><br/>
![image](https://user-images.githubusercontent.com/70896562/218267731-61aaec0b-a68a-44b0-895f-dc982a063309.png)
|:--:| 
| *Network topology* |

### Description of the attack carried out:
#### STAGE 1
- At the beginning of the attack, a network scan is carried out to identify hosts on the network. The scan allows gathering information about the IP and MAC addresses of devices that are part of the network, which is necessary for the attack to proceed.

![scan_network](https://user-images.githubusercontent.com/70896562/218269914-ca036fc2-403e-43b2-a830-89039b023e1e.png)
|:--:| 
| *The result of the nmap program* |

#### STAGE 2 
- After obtaining the IP addresses of the hosts on the network, we run the `arpspoof.py` script, the purpose of which is to transmit false responses and manipulate the ARP table. By using this script, we are able to change the contents of the ARP table to reroute network traffic through our device, allowing us to monitor and possibly modify the data transmitted on the network. In this way, we gain control over the network traffic and can perform an attack of the type _Man-in-the-Middle_.

![command_attack](https://user-images.githubusercontent.com/70896562/218269945-ae367823-e8bb-4602-81d5-862d3247776b.png)
|:--:| 
| *Running a script in python* |


![Network (1)](https://user-images.githubusercontent.com/70896562/218269863-6abe5aa2-4602-4094-860c-b2aa6d57c255.svg)
|:--:| 
| *Network topology after script execution* |


- By sending fake ARP responses, we intentionally mislead the victim by suggesting that our MAC address is the IP address of the Metasploitable server. By doing so, the victim believes that our device is the endpoint to which all data sent over the network should be directed.

![mac_router_spoof](https://user-images.githubusercontent.com/70896562/218271191-ac55da1e-04ac-429d-88e2-9ae61ce92b36.png)
|:--:| 
| *Mapping the attacker's MAC address with the server's IP* |

- As in the case of the victim, the server also has to be deliberately manipulated by sending fake ARP responses to enable it to intercept the victim's traffic. By doing this, the server believes that our device is the endpoint to which all data sent by the victim should be directed.

![mac_spoof](https://user-images.githubusercontent.com/70896562/218271229-ef3dd155-4843-4ea0-9e87-2a5043146aba.png)
|:--:| 
| *Mapping the attacker's MAC address with the victim's IP.* |


![tabela_arp](https://user-images.githubusercontent.com/70896562/218271320-9c0c5ef5-8c35-41e9-8aff-7ad3bcdfb443.png)
|:--:| 
| *Victim ARP table* |

#### STAGE 3
- Accessing credentials information when a user (victim) logs into the administration server _PHPAdmin_

![cerficication_ubuntu](https://user-images.githubusercontent.com/70896562/218271365-ce27654a-81c9-458d-9c84-94dbf8c4f47e.png)
|:--:| 
| *Input of credential information by the victim on the phpAdmin server* |


- Movement received by the attacker _(serwer phpAdmin)_:

![get_password](https://user-images.githubusercontent.com/70896562/218271419-f0479c28-752b-4d22-8630-f62363088133.png)
|:--:| 
| *Obtaining credentials by attacker from phpAdmin server* |

- Obtaining credentials while logging in to the _FTP_ server by the victim

![logowanie_ftp](https://user-images.githubusercontent.com/70896562/218271500-52cc8b7a-c70f-46e1-8ebb-714fbff11761.png)
|:--:| 
| *Logging in to the FTP server by the victim* |

- Obtaining credentials by an attacker _(FTP server)_: 

![ftp_cert](https://user-images.githubusercontent.com/70896562/218271543-ef59e9a0-bef6-42c3-affb-0053aea1d200.png)
|:--:| 
| *Obtaining credentials by attacker from ftp server* |

- ARP table after the script has finished running 

![restore_arp](https://user-images.githubusercontent.com/70896562/218271603-f68db1bd-2141-4fe4-b07e-ce6f4d236a9f.png)
|:--:| 
| *Update the victim's ARP table* |

### Summary

- The danger level of an ARP Spoofing attack these days is considered high. An ARP Spoofing attack is a form of man-in-the-middle attack in which an attacker can eavesdrop on and modify network traffic. As a result, the attacker can gain access to sensitive information such as passwords, personal data and other sensitive information.

- ARP Spoofing attacks are particularly dangerous because they are difficult to detect and protect against. Many devices and networks are not sufficiently protected against this form of attack, allowing attackers to easily exploit this security vulnerability.

- For this reason, it is important to take proper precautions, such as using anti-virus software, using network connection encryption and applying network filters to protect against ARP Spoofing attacks.
