from scapy.all import *
import logger

gatewayIP = "192.168.1.1"
iface = "enp0s31f6"

def getDnsQUERY(DNS_Question):
    print("-----------------------")

    print("DNS Question:")
    print(DNS_Question.show())
    print(DNS_Question.summary())

    DNS_Question = DNS_Question.payload


    if DNS_Question.haslayer(Ether):

        dstMac = getmacbyip(gatewayIP)
        srcmac = get_if_hwaddr(iface)
        DNS_Question[Ether].dst = dstMac
        DNS_Question[Ether].src = srcmac

        Ether_layer = DNS_Question[Ether]

        Ether_layer_dst = Ether_layer.dst
        Ether_layer_src = Ether_layer.src
        Ether_layer_type = Ether_layer.type
        
        print("Ether_layer_dst: "+str(Ether_layer_dst))
        print("Ether_layer_src: "+str(Ether_layer_src))
        print("Ether_layer_type: "+str(Ether_layer_type))


    if DNS_Question.haslayer(IP):
        IP_layer = DNS_Question[IP]

        dstIp = gatewayIP
        srcIp = get_if_addr(iface)

        DNS_Question[IP].dst = dstIp
        DNS_Question[IP].src = srcIp



        IP_layer_version = IP_layer.version
        IP_layer_ihl = IP_layer.ihl
        IP_layer_tos = IP_layer.tos
        IP_layer_len = IP_layer.len
        IP_layer_id = IP_layer.id
        IP_layer_flags = IP_layer.flags
        IP_layer_frag = IP_layer.frag
        IP_layer_ttl = IP_layer.ttl
        IP_layer_proto = IP_layer.proto
        IP_layer_chksum = IP_layer.chksum
        IP_layer_src = IP_layer.src
        IP_layer_dst = IP_layer.dst

        print("IP_layer_version: "+str(IP_layer_version))
        print("IP_layer_ihl: "+str(IP_layer_ihl))
        print("IP_layer_tos: "+str(IP_layer_tos))
        print("IP_layer_len: "+str(IP_layer_len))
        print("IP_layer_id: "+str(IP_layer_id))
        print("IP_layer_flags: "+str(IP_layer_flags))
        print("IP_layer_frag: "+str(IP_layer_frag))
        print("IP_layer_ttl: "+str(IP_layer_ttl))
        print("IP_layer_proto: "+str(IP_layer_proto))
        print("IP_layer_chksum: "+str(IP_layer_chksum))
        print("IP_layer_src: "+str(IP_layer_src))
        print("IP_layer_dst: "+str(IP_layer_dst))


    if DNS_Question.haslayer(UDP):
        pass


    if DNS_Question.haslayer(DNS):
        dns_layer = DNS_Question[DNS]
    
        if dns_layer.qr == 0:
            QueryName  = dns_layer.qd.qname.decode()
            print("Query Name:", QueryName)
            print("Query Type:", dns_layer.qd.qtype)




    DNS_Question = Ether(type="IPv4") / DNS_Question
    print(DNS_Question.show())
    DNS_Response = sr1(DNS_Question, verbose=0, iface=iface,timeout=5)
    print("Response: "+str(DNS_Response))
    #print(DNS_Response.show())




