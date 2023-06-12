#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import t1hash

class T1HashEncryptor:
    def encrypt(self, text):
        hash_object = t1hash.T1Hash()
        hash_object.update(text.encode())
        return hash_object.hexdigest()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = T1HashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)