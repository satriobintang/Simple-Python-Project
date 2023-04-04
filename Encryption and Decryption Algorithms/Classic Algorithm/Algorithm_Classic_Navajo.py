#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import string

# Creating Navajo dictionary
navajo_dict = {
    'A': 'WOL-LA-CHEE',
    'B': 'SHUSH',
    'C': 'MOASI',
    'D': 'BE',
    'E': 'DZEH',
    'F': 'MA-E',
    'G': 'KLIZZIE',
    'H': 'LIN',
    'I': 'TKIN',
    'J': 'TKELE-CHO-G',
    'K': 'KLAGO',
    'L': 'LESH-NI',
    'M': 'DIBEH-YAZZIE',
    'N': 'NA-AS-TSO-SI',
    'O': 'NESH-CHEE',
    'P': 'BI-SO-DIH',
    'Q': 'CA-YEILTH',
    'R': 'GAH',
    'S': 'DIBEH',
    'T': 'A-WOH',
    'U': 'CHUO',
    'V': 'TSAS',
    'W': 'NEAHS-JAH',
    'X': 'SHI-DIN',
    'Y': 'TAH',
    'Z': 'A-CHI'
}

# Function to encrypt message using Navajo dictionary
def encrypt(message):
    encrypted_message = []
    for char in message.upper():
        if char in navajo_dict:
            encrypted_message.append(navajo_dict[char])
    return ' '.join(encrypted_message)

# Function to decrypt Navajo code
def decrypt(message):
    decrypted_message = ''
    words = message.split()
    for word in words:
        for char, navajo in navajo_dict.items():
            if navajo == word:
                decrypted_message += char
    return decrypted_message

while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        message = input("Enter message to encrypt: ")
        encrypted_message = encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        message = input("Enter message to decrypt: ")
        decrypted_message = decrypt(message)
        print("Decrypted message:", decrypted_message)
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")