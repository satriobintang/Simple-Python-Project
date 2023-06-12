#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import zlib

class CRC32Encryptor:
    def encrypt(self, text):
        crc32_value = zlib.crc32(text.encode())
        return format(crc32_value & 0xFFFFFFFF, '08x')

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = CRC32Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)