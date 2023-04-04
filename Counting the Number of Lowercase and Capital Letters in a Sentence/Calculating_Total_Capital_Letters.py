#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

sentence = input("Please enter a sentence: ")
uppercase_count = 0
for letter in sentence:
    if letter.isupper():
        uppercase_count += 1
print("The number of uppercase letters in the sentence is:", uppercase_count)