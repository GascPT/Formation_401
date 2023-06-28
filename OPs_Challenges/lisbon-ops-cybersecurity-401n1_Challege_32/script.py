
import os
import hashlib
from datetime import datetime

def search_files(directory):
    count_files = 0
    count_hits = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            count_files += 1
            file_path = os.path.join(root, file)

            # Generate MD5 hash
            md5_hash = generate_md5(file_path)

            # Get file information
            file_size = os.path.getsize(file_path)
            timestamp = get_timestamp()

            # Print file details
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file}")
            print(f"File Size: {file_size} bytes")
            print(f"File Path: {file_path}")
            print(f"MD5 Hash: {md5_hash}")
            print("-----------------------------------")

            count_hits += 1

    print(f"\nSearch complete. Scanned {count_files} files and found {count_hits} hits.")

def generate_md5(file_path):
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_user_input(prompt):
    if os.name == 'posix':  # Unix-based systems (Linux)
        return input(prompt)
    else:  # Windows
        return input(prompt).decode('utf-8')

directory = get_user_input("Enter the directory to search in: ")
search_files(directory)
