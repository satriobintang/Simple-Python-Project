#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

from Cryptodome.Hash import Skein

class SkeinEncryptor:
    def encrypt(self, text):
        hash_object = Skein.new(digest_bits=256)  # Menggunakan Skein-256
        hash_object.update(text.encode())
        return hash_object.hexdigest()

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = SkeinEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
