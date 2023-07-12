
import subprocess


target = input("Enter the URL or IP address: ")
port = input("Enter the port number: ")

# Perform banner grabbing using netcat
netcat_command = f'nc -v {target} {port}'
netcat_output = subprocess.run(netcat_command, shell=True, capture_output=True, text=True)
print("\nNetcat Output:")
print(netcat_output.stdout)

# Perform banner grabbing using telnet
telnet_command = f'telnet {target} {port}'
telnet_output = subprocess.run(telnet_command, shell=True, capture_output=True, text=True)
print("\nTelnet Output:")
print(telnet_output.stdout)

# Perform banner grabbing using Nmap on well-known ports
nmap_command = f'nmap -p 1-1024 -sV {target}'
nmap_output = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
print("\nNmap Output:")
print(nmap_output.stdout)
