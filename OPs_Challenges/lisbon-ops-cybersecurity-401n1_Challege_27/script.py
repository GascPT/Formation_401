import subprocess
import datetime
import time
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with log rotation
log_filename = 'network.log'
max_file_size = 1024 * 1024  # 1 MB
backup_count = 3
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

# Create a RotatingFileHandler
file_handler = RotatingFileHandler(filename=log_filename, maxBytes=max_file_size,
                                   backupCount=backup_count)
file_handler.setFormatter(log_formatter)

# Create a logger and add the file handler
logger = logging.getLogger('network_logger')
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

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
        print(log_message)

    except Exception as e:
        # Handle any exceptions and log the error
        logger.error(f"An error occurred: {str(e)}")

    # Wait for two seconds before testing again
    time.sleep(2)
