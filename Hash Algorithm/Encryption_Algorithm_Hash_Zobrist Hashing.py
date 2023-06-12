#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import random

class ZobristHashEncryptor:
    def __init__(self):
        self.hash = 0
        self.seed = self.generate_seed()

    def encrypt(self, text):
        self.hash = self.calculate_hash(text)
        return hex(self.hash)[2:]  # Mengkonversi hash menjadi representasi heksadesimal

    def calculate_hash(self, text):
        hash_value = 0
        for char in text:
            random.seed(ord(char))  # Menginisialisasi generator bilangan acak berdasarkan nilai karakter
            hash_value ^= random.getrandbits(64)  # Melakukan operasi XOR antara hash_value dan bilangan acak 64-bit
        return hash_value

    def generate_seed(self):
        return random.getrandbits(64)  # Menghasilkan seed acak 64-bit saat inisialisasi

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = ZobristHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
