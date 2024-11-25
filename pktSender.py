from scapy.all import *
import logger

iface = "enp0s31f6"
dst="192.168.1.1"

def getResponse(pkt):


    if pkt.haslayer(DNS):
        dns_layer = pkt[DNS]
    
        if dns_layer.qr == 0:
            QueryName  = dns_layer.qd.qname.decode()
            print("Query Name:", QueryName)



    dns_request = IP(dst=dst) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=QueryName))
    print("Request: ")
    print(dns_request.show())
    DNS_Response = sr1(dns_request, verbose=0,timeout=5, iface=iface)
    print("Response: ")
    print(type(DNS_Response))
    print(DNS_Response.show())

    if DNS_Response.haslayer(DNS):
        resolved_ip = DNS_Response[DNS].an.rdata
        print("resolvedip: "+str(resolved_ip))
    return DNS_Response


def sendResponse(DNS_Response,pkt):
    iface="wlx00c0cab26f0a"

    if DNS_Response.haslayer(DNS):
        resolved_ip = DNS_Response[DNS].an.rdata
        print("resolvedip: "+str(resolved_ip))

    print(pkt.summary())
    print(DNS_Response.summary())
    macSrc = pkt[Ether].src
    ipSrc = pkt[IP].src
    print(macSrc)
    print(ipSrc)

    final_DNS_Response = Ether(dst=macSrc) / IP(dst=ipSrc) /DNS_Response.payload
    
    print(final_DNS_Response.show())
    
    sendp(final_DNS_Response, iface=iface)
    
    

