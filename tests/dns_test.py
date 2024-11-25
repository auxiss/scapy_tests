from scapy.all import *





print("DNS_Response: ")
dns_request = IP(dst="1.1.1.1") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
print("Request: ")
print(dns_request.show())
DNS_Response = sr1(dns_request, verbose=0,timeout=5, iface="enp0s31f6")
print("Response: ")
print(DNS_Response.show())
