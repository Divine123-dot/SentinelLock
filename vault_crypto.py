#os lets python check if evedence exist on user's device file and manage their path

import os

#base64 convers the 32 bytes key into clean base64 text characters which the encryption hide requres

import base64

#hashlib pick the user's secret passowrd (no matter how long it is ) and uses hash256 math to expand it into 32 byte key

import hashlib

#fernet encryption lock that hides the photos into unedible bytes and open them only with the user's password

from cryptography.fernet import Fernet


#the derive_key function turn the password into byte key for encryption 

def derive_key(password: str) -> bytes:

    #it converst the password string into bytes

    password_bytes = password.encode("utf-8")

    #it uses SHA-256 to create bytes hash digest

    sha256_digest = hashlib.sha256(password_bytes).digest()

    #it encoded into URL safe base64 and return it

    return base64.urlsafe_b64encode(sha256_digest)

#encrypt-file is the file the incident evidence are and they are encrypted and no one can access them expect the person with a password. even the creator or hacker has no access to this file

def encrypt_file(file_path: str, password: str):

    #first verify if the file exist before encryption

    try:
        if not os.path.exists(file_path):
            return None

        #fernet cipher the system pass the user's password into byte for encryption 

        cipher = Fernet(derive_key(password))

        #rb (read binary) read the orginal photo bytes in rb

        with open(file_path, "rb") as file:
            original_data = file.read()

            #the system encrypts the bytes, save the .enc file in wb mode and delete the unlocked original. the image viewer can open them because the system locks the image in AES encryption

        encrypted_data = cipher.encrypt(original_data)
        encrypted_path = file_path + ".enc"

        with open (encrypted_path, "wb") as enc_file:
            enc_file.write(encrypted_data)

        os.remove(file_path)
        return encrypted_path

    except Exception as e:
        return None

#decrypt_file function unlock the file that are encrypted so the user can access them once they log in their account

def decrypt_file(encrypted_path: str, password: str):

    #the system checks if the .enc file exists

    try:
        if not os.path.exists(encrypted_path):
            return None

        #Fernet cipher from the user's password

        cipher = Fernet(derive_key(password))

        #the system decrypts the bytes and restore the original filename that is saved in wb mode and remove the .enc file
        

        #read the scrambled bytes from the .enc file

        with open(encrypted_path, "rb") as enc_file:
            encrypted_data = enc_file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        if encrypted_path.endswith(".enc"):
            restored_path = encrypted_path[:-4]

        else:
            restored_path = encrypted_path +".decrypted"

        with open (restored_path, "wb") as dec_file:
            dec_file.write(decrypted_data)

        os.remove(encrypted_path)
        return restored_path

    except Exception as e:
        return None


# we are testing zero-knowledge encryption and decryption

if __name__ == "__main__":

    test_file = "incidents/test_secret.txt"
    os.makedirs("incidents", exist_ok=True)
    with open(test_file, "w") as f:
        f.write("Top secret thief location and photo evidence!")

        locked_file = encrypt_file(test_file, "MyStrongPin2026")
        print(f"1. File locked at: {locked_file}")

        hacker_attempt = decrypt_file(locked_file, "WrongHackerPin")
        print(f"2. Hacker attemps with a wrong password returned: {hacker_attempt}")

        unlocked_file = decrypt_file(locked_file, "MyStrongPin2026")
        print(f"3. Owner unlocked file at: {unlocked_file}")