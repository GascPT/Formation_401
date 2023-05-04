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

def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    key = generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    encrypted_filepath = filepath + ".encrypted"
    with open(encrypted_filepath, "wb") as f:
        f.write(encrypted)
    os.remove(filepath)

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    decrypted_filepath = filepath[:-10]
    with open(decrypted_filepath, "wb") as f:
        f.write(decrypted)
    os.remove(filepath)

def encrypt_string(plaintext):
    key = generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    print("Encrypted string:", encrypted.decode())
    return encrypted

def decrypt_string(ciphertext):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(ciphertext.encode())
    print("Decrypted string:", decrypted.decode())
    return decrypted

def main():
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")
    if mode == "1":
        filepath = input("Enter filepath to target file: ")
        encrypt_file(filepath)
    elif mode == "2":
        filepath = input("Enter filepath to target file: ")
        decrypt_file(filepath)
    elif mode == "3":
        plaintext = input("Enter cleartext string: ")
        ciphertext = encrypt_string(plaintext)
    elif mode == "4":
        ciphertext = input("Enter ciphertext string: ")
        decrypt_string(ciphertext)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()