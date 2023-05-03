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

    print("Open ports: {}".format(open_ports))
    print("Closed ports: {}".format(closed_ports))
    print("Filtered ports: {}".format(filtered_ports))

def icmp_ping_sweep(network_address):
    network = ipaddress.ip_network(network_address)
    hosts = [str(host) for host in network.hosts()]
    total_hosts = len(hosts)
    online_hosts = 0
    blocked_hosts = 0

    for host in hosts:
        if host == str(network.network_address) or host == str(network.broadcast_address):
            continue
        packet = IP(dst=host)/ICMP()
        response = sr1(packet, timeout=1, verbose=0)
        if not response:
            print("Host {} is down or unresponsive".format(host))
        elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
            print("Host {} is actively blocking ICMP traffic".format(host))
            blocked_hosts += 1
        else:
            print("Host {} is responding".format(host))
            online_hosts += 1

    print("Total hosts: {}".format(total_hosts))
    print("Online hosts: {}".format(online_hosts))
    print("Blocked hosts: {}".format(blocked_hosts))

# Prompt the user for the choice of mode
mode = input("Enter the mode to use (1 for TCP Port Range Scanner, 2 for ICMP Ping Sweep): ")

if mode == "1":
    # Prompt the user for the host IP address
    host_ip = input("Enter the host IP address: ")
    tcp_port_scan(host_ip)
elif mode == "2":
    # Prompt the user for the network address
    network_address = input("Enter the network address including CIDR block (e.g. 10.10.0.0/24): ")
    icmp_ping_sweep(network_address)
else:
    print("Invalid mode choice. Please try again.")
