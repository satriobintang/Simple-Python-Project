#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import string

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet_lower = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase
        self.alphabet = self.alphabet_lower + self.alphabet_upper
    
    def encrypt(self, text):
        encrypted_text = ''
        for char in text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                encrypted_index = (char_index + self.shift) % 26
                encrypted_char = self.alphabet[encrypted_index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    
    def decrypt(self, text):
        decrypted_text = ''
        for char in text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                decrypted_index = (char_index - self.shift) % 26
                decrypted_char = self.alphabet[decrypted_index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

while True:
    try:
        shift = int(input('Enter the shift value (1-25): '))
        if not 1 <= shift <= 25:
            raise ValueError('Shift value must be between 1 and 25.')
        
        text = input('Enter the text to encrypt/decrypt: ')
        cipher = CaesarCipher(shift)
        encrypted_text = cipher.encrypt(text)
        decrypted_text = cipher.decrypt(encrypted_text)
        
        print(f'Original text: {text}')
        print(f'Encrypted text: {encrypted_text}')
        print(f'Decrypted text: {decrypted_text}')
        break
    except ValueError as e:
        print(e)
