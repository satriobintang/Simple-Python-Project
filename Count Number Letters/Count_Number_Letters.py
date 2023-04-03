#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

# Ask user to input a sentence
sentence = input("Enter a sentence: ")

# Count the number of letters in the sentence
letter_count = 0
for letter in sentence:
    if letter.isalpha():
        letter_count += 1

# Display the total count of letters in the sentence
print("The number of letters in the sentence is:", letter_count)
