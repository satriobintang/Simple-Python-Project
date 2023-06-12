#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import zlib

class Adler32Encryptor:
    def encrypt(self, text):
        adler32_value = zlib.adler32(text.encode())
        return format(adler32_value & 0xFFFFFFFF, '08x')

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = Adler32Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)