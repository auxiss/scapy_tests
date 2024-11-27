from scapy.all import *
import logger

iface = "enp0s31f6"

# DNS query: Let's query for the A record of 'www.google.com'
target_domain = "www.google.com"
dns_server = "8.8.8.8"  # Google's public DNS server

# Build the DNS query packet

dns_query = IP(dst=dns_server)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=target_domain))

# Send the DNS query and get the response
response = sr1(dns_query, timeout=5, iface=iface)

# Check if a response was received
if response:
    print("Received DNS response:")
    response.show()
else:
    print("No DNS response received.")