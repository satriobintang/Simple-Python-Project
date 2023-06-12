#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import mmh3

class MurmurHash64Encryptor:
    def encrypt(self, text):
        hash_value = mmh3.hash64(text.encode())
        return str(hash_value)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = MurmurHash64Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)