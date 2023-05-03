from scapy.all import *

# Define the host IP
host_ip = "192.168.88.1"

# Define the port range or specific set of ports to scan
ports = range(1, 1025)

# Test each port in the specified range using a for loop
for port in ports:
    packet = IP(dst=host_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
        send(IP(dst=host_ip)/TCP(dport=port, flags="R"), verbose=0)
        print("Port {} is open".format(port))
    elif response and response.haslayer(TCP) and response[TCP].flags == 0x14:
        print("Port {} is closed".format(port))
    else:
        print("Port {} is filtered".format(port))