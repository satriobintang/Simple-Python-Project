#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
    
    def generate(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(alphabet) for i in range(self.length))

while True:
    try:
        length = int(input('Enter the desired length of the password: '))
        num_passwords = int(input('Enter the number of passwords to generate: '))
        
        password_generator = PasswordGenerator(length)
        for i in range(num_passwords):
            password = password_generator.generate()
            print(f'Password {i+1}: {password}')
        break
    except ValueError as e:
        print(e)
