from scapy.all import *



def getdns(quName):
    dns_request = IP(dst="192.168.1.1") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=quName))
    #print("Request: ")
    #print(dns_request.show())

    DNS_Response = sr1(dns_request, verbose=0,timeout=5, iface="enp0s31f6")
    #print("Response: ")
    #print(type(DNS_Response))
    #print(DNS_Response.show())

    resolved_ip = DNS_Response[DNS].an.rdata
    #print(resolved_ip)
    return resolved_ip



if __name__ == "__main__":
    #quName = "www.google.com"
    #print("domaneName: "+quName)
    quName = input("domaneName: ")
    
    print("ip: "+getdns(quName))