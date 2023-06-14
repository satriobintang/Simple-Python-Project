#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import string
import random

class OneTimePadCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.numbers = '0123456789'
        self.char_to_num = {char: str(num) for num, char in enumerate(self.alphabet)}
        self.num_to_char = {str(num): char for num, char in enumerate(self.alphabet)}

    def generate_key(self, length):
        key = ''
        for _ in range(length):
            key += random.choice(self.alphabet)
        return key

    def encrypt(self, message, key):
        encrypted_message = ''
        for i in range(len(message)):
            if message[i] in self.char_to_num:
                message_num = int(self.char_to_num[message[i]])
                key_num = int(self.char_to_num[key[i]])
                encrypted_num = (message_num + key_num) % len(self.alphabet)
                encrypted_message += self.num_to_char[str(encrypted_num)]
            elif message[i] in self.numbers:
                encrypted_message += message[i]
            else:
                encrypted_message += ' '
        return encrypted_message

    def decrypt(self, message, key):
        decrypted_message = ''
        for i in range(len(message)):
            if message[i] in self.char_to_num:
                message_num = int(self.char_to_num[message[i]])
                key_num = int(self.char_to_num[key[i]])
                decrypted_num = (message_num - key_num) % len(self.alphabet)
                decrypted_message += self.num_to_char[str(decrypted_num)]
            elif message[i] in self.numbers:
                decrypted_message += message[i]
            else:
                decrypted_message += ' '
        return decrypted_message

# Main program
cipher = OneTimePadCipher()

while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        message = input("Enter message to encrypt: ")
        key = cipher.generate_key(len(message))
        print("Key:", key)
        encrypted_message = cipher.encrypt(message.lower(), key)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        message = input("Enter message to decrypt: ")
        key = input("Enter key: ")
        decrypted_message = cipher.decrypt(message.lower(), key)
        print("Decrypted message:", decrypted_message)
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")
