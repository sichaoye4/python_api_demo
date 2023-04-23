# utils to use cryptography.fernet to decrypt the encrypted data using the key
from cryptography.fernet import Fernet
import os
from pathlib import Path

def decrypt(encrypted_data: str, key: str) -> str:
    f = Fernet(key)
    return f.decrypt(bytes(encrypted_data, 'utf-8')).decode('utf-8')

def decrypt_db_password(encrypted_data: str) -> str:
    # get home directory from os    
    home_dir = os.path.expanduser('~')

    # get the path to the key file
    key_file_path = Path(home_dir, 'key.txt')

    # read key and convert into byte
    with open(str(key_file_path)) as f:
        refKey = ''.join(f.readlines())
        refKeybyt = bytes(refKey, 'utf-8')
    f.close()
    return decrypt(encrypted_data, refKeybyt)