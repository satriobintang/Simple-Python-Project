#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import base64

text = input("Enter Text to Encrypt: ").encode('utf-8')

print("===========================================")
print("MESSAGE ENCRYPTION PROCESS")
print("===========================================")

base32_encryption = base64.b32encode(text)
print("Encrypted Text        : ", base32_encryption)
print("Encrypted Text utf-8  : ", base32_encryption.decode('utf-8'))


print("===========================================")
print("MESSAGE DECRYPTION PROCESS")
print("===========================================")

base32_decryption = base64.b32decode(base32_encryption)
print("Decrypted Text        : ", base32_decryption)
print("Decrypted Text utf-8  : ", base32_decryption.decode('utf-8'))