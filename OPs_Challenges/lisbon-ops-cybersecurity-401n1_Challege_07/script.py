from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_FILE, "rb") as f:
        key = f.read()
    return key

def encrypt_file(filepath, key):
    with open(filepath, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    encrypted_filepath = filepath + ".encrypted"

    with open(encrypted_filepath, "wb") as f:
        f.write(encrypted)

    os.remove(filepath)


def decrypt_file(filepath, key):
    with open(filepath, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    decrypted_filepath = filepath[:-10]

    with open(decrypted_filepath, "wb") as f:
        f.write(decrypted)

    os.remove(filepath)


def encrypt_directory(directory):
    key = generate_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            encrypt_file(filepath, key)

    with open(os.path.join(directory, "key.txt"), "wb") as f:
        f.write(key)


def decrypt_directory(directory):
    with open(os.path.join(directory, "key.txt"), "rb") as f:
        key = f.read()

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".encrypted"):
                filepath = os.path.join(root, filename)
                decrypt_file(filepath, key)


def encrypt_string(plaintext):
    key = generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    print(encrypted)


def decrypt_string(ciphertext):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(ciphertext.encode())
    print(decrypted.decode())


def main():
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a directory\n6. Decrypt a directory\n")

    if mode == "1":
        filepath = input("Enter filepath to target file: ")
        key = generate_key()
        encrypt_file(filepath, key)

    elif mode == "2":
        filepath = input("Enter filepath to target file: ")
        key = load_key()
        decrypt_file(filepath, key)

    elif mode == "3":
        plaintext = input("Enter cleartext string: ")
        encrypt_string(plaintext)

    elif mode == "4":
        ciphertext = input("Enter ciphertext string: ")
        decrypt_string(ciphertext)

    elif mode == "5":
        directory = input("Enter directory to target: ")
        encrypt_directory(directory)

    elif mode == "6":
        directory = input("Enter directory to target: ")
        decrypt_directory(directory)

    else:
        print("Invalid mode selected.")


if __name__ == "__main__":
    main()