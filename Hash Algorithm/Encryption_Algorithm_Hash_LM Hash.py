#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

from impacket import smbhash

class LMHashEncryptor:
    def encrypt(self, text):
        lm_hash = smbhash.LMOWFv1(text)
        return lm_hash.hex()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = LMHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)