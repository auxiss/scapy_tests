from scapy.all import *
import logger




def getResponse(dns_request):
    iface = "enp0s31f6"

    DNS_Response = sr1(dns_request, verbose=0,timeout=5, iface=iface)
        
    return DNS_Response


def sendResponse(DNS_Response):
    iface="wlx00c0cab26f0a"

    print(type(DNS_Response))
    print(DNS_Response.summary())
    sendp(DNS_Response, iface=iface)
    
    

