#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

from collections import Counter

class WordParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        try:
            words = self.text.split()
            word_count = Counter(words)
            return word_count
        except Exception as e:
            print(e)

while True:
    try:
        text = input('Enter the text: ')
        parser = WordParser(text)
        word_count = parser.parse()
        print('\nWord count:')
        for word, count in word_count.items():
            print(f'{word}: {count}')
        break
    except Exception as e:
        print(e)
