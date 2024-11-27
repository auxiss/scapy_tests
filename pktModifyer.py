from scapy.all import *


gatewayIP = "192.168.1.1"
DnsServer = "8.8.8.8"



def flipSender(pkt):

    if pkt.haslayer(DNS):
        dns_layer = pkt[DNS]
    
        if dns_layer.qr == 0:
            QueryName  = dns_layer.qd.qname.decode()
            print("flipSender report:")
            print("Query Name:", QueryName)

    #print(pkt.summary())
    core = pkt.payload
    #print(core.summary())


    dns_request = IP(dst=gatewayIP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=QueryName))
    

    return dns_request




def flipReciver(pkt):
    pass