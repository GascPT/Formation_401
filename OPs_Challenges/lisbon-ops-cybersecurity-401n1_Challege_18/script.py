import zipfile

def zip_brute_force(zip_file, word_list):
    with open(word_list, 'r', encoding='latin-1') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        try:
            with zipfile.ZipFile(zip_file, 'r') as zf:
                zf.extractall(pwd=password.encode('utf-8'))
            print("SUCCESS: Password found!")
            print("Password:", password)
            return
        except Exception as e:
            if 'Bad password' in str(e):
                print("Failed attempt:", password)
            else:
                print("Error:", str(e))
                return

    print("Password not found in the word list.")

def main():
    print("Select a mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. Defensive; Password Complexity")
    print("4. Brute Force; SSH Authentication")
    print("5. Brute Force; ZIP File Password")

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
    elif mode == "5":
        zip_file = input("Enter the path of the password-locked ZIP file: ")
        word_list = "RockYou.txt"
        zip_brute_force(zip_file, word_list)
    else:
        print("Invalid mode number. Please try again.")

if __name__ == "__main__":
    main()
