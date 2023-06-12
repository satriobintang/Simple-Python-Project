#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import siphash

class HalfSipHashEncryptor:
    def encrypt(self, text):
        key = b'\x00' * 16  # Kunci yang digunakan untuk enkripsi
        hash_value = siphash.SipHash_2_4(key, text.encode()).hexdigest()
        return hash_value

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = HalfSipHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
