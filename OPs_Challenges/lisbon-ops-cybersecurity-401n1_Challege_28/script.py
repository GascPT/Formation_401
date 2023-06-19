
import subprocess
import datetime
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Create a FileHandler to write log messages to a file
file_handler = logging.FileHandler('network.log')
file_handler.setLevel(logging.INFO)

# Create a StreamHandler to output log messages to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Set the log message format for both handlers
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(log_formatter)
stream_handler.setFormatter(log_formatter)

# Get the root logger and add the handlers
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Define the IP address to test
ip_address = "8.8.8.8"

while True:
    try:
        # Run the ping command and capture the output
        ping_output = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE).communicate()[0]

        # Check if the ping was successful
        if "1 received" in str(ping_output):
            status = "Network Active"
        else:
            status = "Network Error"

        # Print the timestamp, status, and IP address
        log_message = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} {status} to {ip_address}"
        logger.info(log_message)

    except Exception as e:
        # Handle any exceptions and log the error
        logger.error(f"An error occurred: {str(e)}")

    # Wait for two seconds before testing again
    time.sleep(2)
