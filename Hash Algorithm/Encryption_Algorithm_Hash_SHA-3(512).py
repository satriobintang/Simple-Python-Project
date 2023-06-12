#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import hashlib

class SHA3_512Encryptor:
    def encrypt(self, text):
        hash_object = hashlib.sha3_512()
        hash_object.update(text.encode())
        return hash_object.hexdigest()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = SHA3_512Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)