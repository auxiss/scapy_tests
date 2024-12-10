from scapy.all import *



def TraceRoute(target_ip,iface):
	ttl = 1
	while True:

		print("\n\nhop "+str(ttl)+".")

		# Build the packet: IP layer + ICMP (ping)
		packet = IP(dst=target_ip, ttl=ttl)/ICMP()
		print("request pkt: "+str(packet.summary()))

		# Send the packet and receive the response
		response = sr1(packet, timeout=2, iface=iface)

		# Check if a response was received
		if response:
			print("Received response from:", response[IP].src)
			print("response pkt: "+str(response.summary()))


			# Check if target has ben reched
			if target_ip == response[IP].src:
				print("target reched!")
				return 0
			
		
		else:
			print("No response received. The request may have timed out.")

		ttl=ttl+1


if __name__ == "__main__":
	iface = "enp0s31f6"
	# Define the target IP address
	target_ip = "8.8.8.8"  # Example: Google Public DNS


	TraceRoute(target_ip ,iface)