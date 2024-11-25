from scapy.all import *

iface = "enp0s31f6"
# Define the target IP address
target_ip = "8.8.8.8"  # Example: Google Public DNS

# Build the packet: IP layer + ICMP (ping)
packet = IP(dst=target_ip)/ICMP()
packet.show()

# Send the packet and receive the response
response = sr1(packet, timeout=2, iface=iface)

# Check if a response was received
if response:
    print("Received response from:", response[IP].src)
    print("Response details:")
    response.show()
else:
    print("No response received. The request may have timed out.")