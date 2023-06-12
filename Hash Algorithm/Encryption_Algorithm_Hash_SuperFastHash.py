#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import superfasthash

class SuperFastHashEncryptor:
    def encrypt(self, text):
        hash_value = superfasthash.hash(text.encode())
        return hash_value

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = SuperFastHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
