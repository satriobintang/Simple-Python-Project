#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import farmhash

class FarmHashEncryptor:
    def encrypt(self, text):
        hash_value = farmhash.hash64(text)
        return hex(hash_value)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = FarmHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
