import subprocess          
import datetime            
import time                
import smtplib             
import getpass             

ip_address = "8.8.8.8"      

# Get the email address and password for sending notifications
email_address = input("Enter your email address: ")
email_password = getpass.getpass(prompt="Enter your email password: ")

# Set up the email server and login to send notifications
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(email_address, email_password)

prev_status = "Network Active"  

while True:
    # Run the ping command and capture the output
    ping_output = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE).communicate()[0]

    # Check if the ping was successful
    if "1 received" in str(ping_output):
        curr_status = "Network Active"
    else:
        curr_status = "Network Error"

    # If the status has changed, send a notification email
    if prev_status != curr_status:
        if curr_status == "Network Active":
            subject = "Host is up"
        else:
            subject = "Host is down"
        body = f"The host status changed from {prev_status} to {curr_status} at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}"
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        smtp_connection.sendmail(email_address, email_address, message)

      
        prev_status = curr_status

    # Print the timestamp, status, and IP address
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), curr_status, "to", ip_address)

    time.sleep(2)