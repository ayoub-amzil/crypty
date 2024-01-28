import os
import random
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Set up the AES cipher
BLOCK_SIZE = 16
key = b"m0tE9aijap7IuowSu1Mpbw=="
iv = b"o7ZTXFOgsJVx3cFv"
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

# Set up the folder path
folder_path = "crypt"

# Define a function to generate a random password
def generate_password():
    chars = string.ascii_letters + string.digits + "@_-#"
    return "".join(random.choice(chars) for i in range(20))

# Define a function to encrypt a file
def encrypt_file(file_path):
    # Generate a random password and show it to the user
    password = generate_password()
    print("Generated Password: {}".format(password))
    
    # Read the file data
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Encrypt the file data
    encrypted_data = cipher.encrypt(pad(file_data, BLOCK_SIZE))
    
    # Securely delete the original file
    os.remove(file_path)
    
    # Write the encrypted data to a new file with the ".enc" extension
    file_name = os.path.basename(file_path)
    new_file_path = os.path.join(folder_path, file_name + ".enc")
    with open(new_file_path, "wb") as file:
        file.write(encrypted_data)
    
    print("File encrypted successfully!")
    

# Define a function to decrypt a file
def decrypt_file(file_path):
    # Read the file data
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Decrypt the file data
    decrypted_data = unpad(cipher.decrypt(file_data), BLOCK_SIZE)
    
    # Securely delete the encrypted file
    os.remove(file_path)
    
    # Write the decrypted data to a new file without the ".enc" extension
    file_name, _ = os.path.splitext(os.path.basename(file_path))
    new_file_path = os.path.join(folder_path, file_name)
    with open(new_file_path, "wb") as file:
        file.write(decrypted_data)
    
    print("File decrypted successfully!")

# Prompt the user for the action they want to perform
while True:
    action = input("Enter 1 to encrypt a file or 2 to decrypt a file: ")
    if action not in ["1", "2"]:
        print("Invalid action. Please try again.")
    else:
        break

# Perform the selected action
if action == "1":
    # List the files in the "crypt" folder that don't have the ".enc" extension
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.endswith(".enc")]
    if not files:
        print("No files available to encrypt!")
    else:
        # Show an index with each file
        for i, file_name in enumerate(files):
            print("{}) {}".format(i+1, file_name))
        
        # Ask the user which file they want to encrypt
        while True:
            file_index = input("Enter the index of the file you want to encrypt: ")
            try:
                file_index = int(file_index)
                if file_index < 1 or file_index > len(files):
                    raise ValueError
                break
            except ValueError:
                print("Invalid index. Please try again.")
        
