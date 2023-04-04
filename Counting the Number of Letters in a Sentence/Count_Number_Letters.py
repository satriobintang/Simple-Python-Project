#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

sentence = input("Please input a sentence: ")
letter_count = 0
for letter in sentence:
    if letter.isalpha():
        letter_count += 1
print("The number of letters in the sentence is:", letter_count)