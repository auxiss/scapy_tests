from scapy.all import *


# Get the UDP checksum computed by Scapy
packet = IP(dst="10.11.12.13", src="10.11.12.14")/UDP()/DNS()
packet = IP(raw(packet))  # Build packet (automatically done when sending)
checksum_scapy = packet[UDP].chksum

# Set the UDP checksum to 0 and compute the checksum 'manually'
packet = IP(dst="10.11.12.13", src="10.11.12.14")/UDP(chksum=0)/DNS()
packet_raw = raw(packet)
udp_raw = packet_raw[20:]
# in4_chksum is used to automatically build a pseudo-header
chksum = in4_chksum(socket.IPPROTO_UDP, packet[IP], udp_raw)  # For more infos, call "help(in4_chksum)"

assert(checksum_scapy == chksum)


def packetHandler(pkt):
    print("------->>" ,end="")
    print(pkt)
    pinfo.append(pkt.show)

pinfo = []

sniff(iface = "wlan0mon",prn = packetHandler, count=10)   

print(pinfo)

for packet in pinfo:
	print(packet)
