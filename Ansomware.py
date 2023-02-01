import os
import hashlib
import sys

# A list of file extensions commonly targeted by ransomware
EXTENSIONS = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".jpg", ".png", ".csv", ".sql", ".mdb", ".sln", ".php", ".asp", ".aspx", ".html", ".xml", ".psd"]

def check_file(file_path):
    # Calculate the SHA-256 hash of the file
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    file_hash = hasher.hexdigest()

    # Compare the hash against a known good hash for the file
    # Replace this with your own code to fetch known good hashes for each file
    if file_hash == known_good_hash:
        return True
    else:
        return False

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not check_file(file_path):
                print("Possible ransomware detected:", file_path)
                # Add your own code here to take action, such as deleting the file or restoring it from a backup

if __name__ == "__main__":
    # Scan the current directory and all subdirectories
    scan_directory(os.getcwd())
