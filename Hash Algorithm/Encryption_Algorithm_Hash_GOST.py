#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

from Cryptodome.Hash import GOST

class GOSTEncryptor:
    def encrypt(self, text):
        hash_object = GOST.new(digest_bits=256)  # Menggunakan GOST-256
        hash_object.update(text.encode())
        return hash_object.hexdigest()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = GOSTEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)