#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import binascii

class CRC16Encryptor:
    def encrypt(self, text):
        crc = binascii.crc_hqx(text.encode(), 0)
        return hex(crc)[2:].zfill(4)

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = CRC16Encryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)