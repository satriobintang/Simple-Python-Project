#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import base64

text = input("Enter the text to be encrypted: ").encode('utf-8')

print("===========================================")
print("MESSAGE ENCRYPTION PROCESS")
print("===========================================")

base64_encryption = base64.b64encode(text)
print("Encryption Result     : ", base64_encryption)
print("Encryption Result utf-8: ", base64_encryption.decode('utf-8'))

print("===========================================")
print("MESSAGE DECRYPTION PROCESS")
print("===========================================")

base64_decryption = base64.decodebytes(base64_encryption)
print("Decryption Result     : ", base64_decryption)
print("Decryption Result utf-8: ", base64_decryption.decode('utf-8'))