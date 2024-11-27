from scapy.all import *
import logger

iface = "enp0s31f6"
dst="192.168.1.1"

def getResponse(dns_request):

    DNS_Response = sr1(dns_request, verbose=0,timeout=5, iface="enp0s31f6")
        
    return DNS_Response


def sendResponse(DNS_Response,pkt):
    iface="wlx00c0cab26f0a"

    if DNS_Response.haslayer(DNS):
        resolved_ip = DNS_Response[DNS].an.rdata
        #print("resolvedip: "+str(resolved_ip))

    #print(pkt.summary())
    #print(DNS_Response.summary())
    macSrc = pkt[Ether].src
    ipSrc = pkt[IP].src
    #print(macSrc)
    #print(ipSrc)

    final_DNS_Response = Ether(dst=macSrc) / IP(dst=ipSrc) /DNS_Response.payload
    
    #print("modifaed response:")
    #print(final_DNS_Response.show())
    
    sendp(final_DNS_Response, iface=iface)
    
    

