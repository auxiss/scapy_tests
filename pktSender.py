from scapy.all import *
import logger

iface = "enp0s31f6"

def gekjtResponse(pkt):
    send(pkt, iface=iface)
    pass