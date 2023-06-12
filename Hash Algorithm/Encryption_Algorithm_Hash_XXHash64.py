#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import xxhash

class XXHash64Encryptor:
    def encrypt(self, text):
        hash_object = xxhash.xxh64(text)
        return hash_object.hexdigest()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = XXHash64Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)