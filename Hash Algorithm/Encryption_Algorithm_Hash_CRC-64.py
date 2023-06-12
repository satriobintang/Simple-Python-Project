#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import crcmod

class CRC64Encryptor:
    def encrypt(self, text):
        crc_func = crcmod.predefined.mkPredefinedCrcFun('crc-64')
        crc = crc_func(text.encode())
        return hex(crc)[2:].zfill(16)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = CRC64Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)