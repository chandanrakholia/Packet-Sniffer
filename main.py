from scapy.all import *

# Craft a packet
packet = IP(dst="www.google.com")/ICMP()

# Send the packet
response = sr1(packet, timeout=5)

# Display the response
response.show()

