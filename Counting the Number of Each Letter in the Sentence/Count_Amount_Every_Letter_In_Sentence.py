#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class LetterCounter:
    def __init__(self, text):
        self.text = text.lower()
        self.counts = {}

    def count_letters(self):
        for letter in self.text:
            if letter.isalpha():
                if letter in self.counts:
                    self.counts[letter] += 1
                else:
                    self.counts[letter] = 1

    def display_counts(self):
        self.count_letters()
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter in self.counts:
                print(f"{letter}: {self.counts[letter]}")
            else:
                print(f"{letter}: 0")

def main():
    text = input("Enter a text: ")
    letter_counter = LetterCounter(text)
    letter_counter.display_counts()

if __name__ == "__main__":
    main()