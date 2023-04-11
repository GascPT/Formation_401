import subprocess
import datetime
import time

# Define the IP address to test
ip_address = "8.8.8.8"

while True:
    # Run the ping command and capture the output
    ping_output = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE).communicate()[0]

    # Check if the ping was successful
    if "1 received" in str(ping_output):
        status = "Network Active"
    else:
        status = "Network Error"

    # Print the timestamp, status, and IP address
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), status, "to", ip_address)

    # Wait for two seconds before testing again
    time.sleep(2)