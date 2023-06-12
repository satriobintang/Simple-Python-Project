#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class APHashEncryptor:
    def encrypt(self, text):
        hash_value = self.ap_hash(text)
        return hash_value

    def ap_hash(self, text):
        hash_value = 0xAAAAAAAA
        for i, char in enumerate(text):
            if i & 1 == 0:
                hash_value ^= ((hash_value << 7) ^ ord(char) ^ (hash_value >> 3))
            else:
                hash_value ^= (~((hash_value << 11) ^ ord(char) ^ (hash_value >> 5)))
        return hash_value

while True:
    try:
        text = input('Enter the text to encrypt: ')
        encryptor = APHashEncryptor()
        encrypted_text = encryptor.encrypt(text)
        print(f'Encrypted text: {encrypted_text}')
        break
    except Exception as e:
        print(e)
