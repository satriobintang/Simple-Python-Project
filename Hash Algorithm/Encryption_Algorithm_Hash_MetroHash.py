#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import metrohash

class MetroHashEncryptor:
    def encrypt(self, text):
        hash_value = metrohash.MetroHash64(text.encode())
        return hex(hash_value)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = MetroHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)