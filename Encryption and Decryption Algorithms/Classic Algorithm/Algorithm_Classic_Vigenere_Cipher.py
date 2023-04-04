#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        ciphertext = ''
        i = 0
        for char in plaintext:
            if char == ' ':
                ciphertext += ' '
                continue
            shift = ord(self.key[i % len(self.key)]) - 65
            ciphertext += chr(((ord(char) + shift - 65) % 26) + 65)
            i += 1
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        plaintext = ''
        i = 0
        for char in ciphertext:
            if char == ' ':
                plaintext += ' '
                continue
            shift = ord(self.key[i % len(self.key)]) - 65
            plaintext += chr(((ord(char) - shift - 65) % 26) + 65)
            i += 1
        return plaintext


while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        message = input("Enter message to encrypt: ")
        key = input("Enter key: ")
        cipher = VigenereCipher(key)
        ciphertext = cipher.encrypt(message)
        print(f'Ciphertext: {ciphertext}')
    elif choice == 'd':
        message = input("Enter message to decrypt: ")
        key = input("Enter key: ")
        cipher = VigenereCipher(key)
        plaintext = cipher.decrypt(message)
        print(f'Decrypted plaintext: {plaintext}')
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")
