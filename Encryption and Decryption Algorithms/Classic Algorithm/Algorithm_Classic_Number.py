#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import string

# Makes a dictionary of the alphabet and the corresponding numbers
alphabet = string.ascii_lowercase
numbers = '0123456789'
char_to_num = {char: str(num) for num, char in enumerate(alphabet)}
num_to_char = {str(num): char for num, char in enumerate(alphabet)}

# Function to encrypt messages
def encrypt(message):
    encrypted_message = ''
    for char in message.lower():
        if char in char_to_num:
            encrypted_message += char_to_num[char]
        elif char in numbers:
            encrypted_message += char
        else:
            encrypted_message += ' '
    return encrypted_message

# Function to decrypt messages
def decrypt(message):
    decrypted_message = ''
    i = 0
    while i < len(message):
        if message[i] in num_to_char:
            decrypted_message += num_to_char[message[i]]
        elif message[i] in numbers:
            decrypted_message += message[i]
        else:
            decrypted_message += ' '
        i += 1
    return decrypted_message

# Main program
while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        message = input("Enter message to encrypt: ")
        print("Encrypted message:", encrypt(message))
    elif choice == 'd':
        message = input("Enter message to decrypt: ")
        print("Decrypted message:", decrypt(message))
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")