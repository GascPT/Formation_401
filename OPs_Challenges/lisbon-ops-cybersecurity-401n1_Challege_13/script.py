from scapy.all import *
import ipaddress

def tcp_port_scan(host_ip):
    ports = range(1, 1025)
    open_ports = []
    closed_ports = []
    filtered_ports = []

    for port in ports:
        packet = IP(dst=host_ip)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            send(IP(dst=host_ip)/TCP(dport=port, flags="R"), verbose=0)
            open_ports.append(port)
        elif response and response.haslayer(TCP) and response[TCP].flags == 0x14:
            closed_ports.append(port)
        else:
            filtered_ports.append(port)

    return (open_ports, closed_ports, filtered_ports)

def scan_host(ip):
    packet = IP(dst=ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    if not response:
        print("Host is down or unresponsive")
    elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        print("Host is actively blocking ICMP traffic")
    else:
        print("Host is up")
        open_ports, closed_ports, filtered_ports = tcp_port_scan(ip)
        print("Open ports: {}".format(open_ports))
        print("Closed ports: {}".format(closed_ports))
        print("Filtered ports: {}".format(filtered_ports))

# Prompt the user for the host IP address
ip = input("Enter the IP address to scan: ")
scan_host(ip)
