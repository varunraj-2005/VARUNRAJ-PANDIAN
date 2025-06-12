pip install cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

with open('file.txt', 'rb') as file:
    encrypted = cipher.encrypt(file.read())

with open('file.encrypted', 'wb') as enc_file:
    enc_file.write(encrypted)
