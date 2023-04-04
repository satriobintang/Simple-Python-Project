#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class BoyScoutCipher:
    def __init__(self):
        self.grid = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y']
        ]

    def encrypt(self, message):
        encoded = ''
        for char in message:
            if char == ' ':
                encoded += ' '
            else:
                row, col = self.find_char(char)
                encoded += str(row) + str(col)
        return encoded

    def decrypt(self, message):
        decoded = ''
        i = 0
        while i < len(message):
            if message[i] == ' ':
                decoded += ' '
                i += 1
            else:
                row = int(message[i])
                col = int(message[i+1])
                decoded += self.grid[row][col]
                i += 2
        return decoded

    def find_char(self, char):
        for row in range(5):
            for col in range(5):
                if self.grid[row][col] == char:
                    return row, col
        return -1, -1

if __name__ == '__main__':
    cipher = BoyScoutCipher()
    while True:
        choice = input('Enter E to encrypt or D to decrypt: ').strip().upper()
        if choice in ['E', 'D']:
            break
        print('Invalid choice!')

    message = input('Enter the message to encrypt or decrypt: ').strip().upper()

    if choice == 'E':
        encoded = cipher.encrypt(message)
        print('Encoded message:', encoded)
    else:
        decoded = cipher.decrypt(message)
        print('Decoded message:', decoded)