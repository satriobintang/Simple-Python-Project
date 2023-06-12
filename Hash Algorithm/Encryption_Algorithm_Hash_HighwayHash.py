#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import highwayhash

class HighwayHashEncryptor:
    def encrypt(self, text):
        key = b'\x00' * 32  # Kunci yang digunakan untuk enkripsi
        hash_value = highwayhash.hash64(text.encode(), key)
        return hex(hash_value)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = HighwayHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
