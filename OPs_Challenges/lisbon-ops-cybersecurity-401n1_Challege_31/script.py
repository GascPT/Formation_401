

import os

def search_files(file_name, directory):
    count_files = 0
    count_hits = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                count_hits += 1
                file_path = os.path.join(root, file)
                print(f"Found: {file_path}")
            count_files += 1

    print(f"\nSearch complete. Searched {count_files} files and found {count_hits} hits.")

def get_user_input(prompt):
    if os.name == 'posix':  # Unix-based systems (Linux)
        return input(prompt)
    else:
        return input(prompt).encode('utf-8')

file_name = get_user_input("Enter the file name to search for: ")
directory = get_user_input("Enter the directory to search in: ")

search_files(file_name, directory)
