#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import hashlib

class Shake256Encryptor:
    def encrypt(self, text):
        hash_object = hashlib.shake_256()
        hash_object.update(text.encode())
        return hash_object.hexdigest(64)  # Specify the desired digest size in bytes

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = Shake256Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
