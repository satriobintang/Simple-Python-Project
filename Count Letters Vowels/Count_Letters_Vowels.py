#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class VowelCounter:
    def __init__(self):
        self.vowels = {'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0}
    
    def count(self, word):
        for char in word:
            if char in self.vowels:
                self.vowels[char] += 1
    
    def get_count(self):
        return self.vowels

while True:
    try:
        word = input('Enter a word: ')
        word = word.lower()
        vowel_counter = VowelCounter()
        vowel_counter.count(word)
        counts = vowel_counter.get_count()
        print(f'Number of vowels in the word:')
        print(f'a: {counts["a"]}')
        print(f'i: {counts["i"]}')
        print(f'u: {counts["u"]}')
        print(f'e: {counts["e"]}')
        print(f'o: {counts["o"]}')
        break
    except ValueError as e:
        print(e)
