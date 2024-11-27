from scapy.all import *


gatewayIP = "192.168.1.1"
DnsServer = "8.8.8.8"



def flipSender(pkt):


    if pkt.haslayer(DNS):
        dns_layer = pkt[DNS]
    
        if dns_layer.qr == 0:
            QueryName  = dns_layer.qd.qname.decode()
            id = dns_layer.id
            print("packet id:"+str(id))
            #print("flipSender report:")
            #print("Query Name:", QueryName)

    #print(pkt.summary())
    core = pkt.payload
    #print(core.summary())
    
    



    dns_request = IP(dst=gatewayIP) / UDP(dport=53) / DNS(rd=1, id=id, qd=DNSQR(qname=QueryName))
    

    return dns_request




def flipReciver(DNS_Response, pkt):
    
    if DNS_Response.haslayer(DNS):
        resolved_ip = DNS_Response[DNS].an.rdata
        #print("resolvedip: "+str(resolved_ip))

        #print(pkt.summary())
        #print(DNS_Response.summary())
        macSrc = pkt[Ether].src
        ipSrc = pkt[IP].src
        #print(macSrc)
        #print(ipSrc)

        modifyed_DNS_Response = Ether(dst=macSrc) / IP(dst=ipSrc) /DNS_Response.payload
        
        #print("modifaed response:")
        #print(final_DNS_Response.show())

        return modifyed_DNS_Response