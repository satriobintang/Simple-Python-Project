#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class Encryption:
    def __init__(self):
        self.dictionary = {
            '03.00': 'A',
            '03.05': 'B',
            '03.10': 'C',
            '03.15': 'D',
            '03.20': 'E',
            '03.25': 'F',
            '03.30': 'G',
            '03.35': 'H',
            '03.40': 'I',
            '03.45': 'J',
            '03.50': 'K',
            '03.55': 'L',
            '04.00': 'M',
            '04.05': 'N',
            '04.10': 'O',
            '04.15': 'P',
            '04.20': 'W',
            '04.25': 'R',
            '04.30': 'S',
            '04.35': 'T',
            '04.40': 'U',
            '04.45': 'V',
            '04.50': 'W',
            '04.55': 'X',
            '05.00': 'Y',
            '05.05': 'Z'
        }
    
    def encrypt(self, text):
        result = ''
        for char in text:
            if char == ' ':
                result += ' '
            else:
                for key, value in self.dictionary.items():
                    if char == value:
                        result += key + ' '
                        break
                else:
                    result += char
        return result
    
    def decrypt(self, text):
        result = ''
        chars = text.split(' ')
        for char in chars:
            if char == '':
                result += ' '
            elif char in self.dictionary:
                result += self.dictionary[char]
            else:
                result += char
        return result

OOP_Algoritm = Encryption()

while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        message = input("Enter message to encrypt: ").upper()
        encrypted_message = OOP_Algoritm.encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        message = input("Enter message to decrypt: ").upper()
        decrypted_message = OOP_Algoritm.decrypt(message)
        print("Decrypted message:", decrypted_message)
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")
