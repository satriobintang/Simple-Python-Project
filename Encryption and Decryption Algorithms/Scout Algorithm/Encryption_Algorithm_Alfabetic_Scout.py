#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class Cipher:
    # encryption dictionary
    encrypt_dict = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
        'Z': 'Zulu', '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
        ' ': 'Space'
    }

    # decryption dictionary
    decrypt_dict = {
        'Alfa': 'A', 'Bravo': 'B', 'Charlie': 'C', 'Delta': 'D', 'Echo': 'E',
        'Foxtrot': 'F', 'Golf': 'G', 'Hotel': 'H', 'India': 'I', 'Juliet': 'J',
        'Kilo': 'K', 'Lima': 'L', 'Mike': 'M', 'November': 'N', 'Oscar': 'O',
        'Papa': 'P', 'Quebec': 'Q', 'Romeo': 'R', 'Sierra': 'S', 'Tango': 'T',
        'Uniform': 'U', 'Victor': 'V', 'Whiskey': 'W', 'Xray': 'X', 'Yankee': 'Y',
        'Zulu': 'Z', 'Zero': '0', 'One': '1', 'Two': '2', 'Three': '3', 'Four': '4',
        'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9',
        'Space': ' '
    }

    def __init__(self):
        pass

    def encrypt(self, message):
        result = [self.encrypt_dict.get(c.upper(), c) for c in message]
        return " ".join(result)

    def decrypt(self, message):
        result = [self.decrypt_dict.get(w, w) for w in message.split()]
        return " ".join(result)


if __name__ == '__main__':
    cipher = Cipher()
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if choice == 'e':
            message = input("Enter message to encrypt: ")
            print("Encrypted message:", cipher.encrypt(message))
        elif choice == 'd':
            message = input("Enter message to decrypt: ")
            print("Decrypted message:", cipher.decrypt(message))
        elif choice == 'q':
            break
        else:
            print("Invalid choice.")
