#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import string

class FrequencyAnalyzer:
    def __init__(self, text):
        self.text = text.lower()
        self.frequency = {}
        self.total_chars = 0

    def analyze(self):
        for char in self.text:
            if char in string.ascii_lowercase:
                if char in self.frequency:
                    self.frequency[char] += 1
                else:
                    self.frequency[char] = 1
                self.total_chars += 1

    def display(self):
        sorted_frequency = sorted(self.frequency.items(), key=lambda x: x[1], reverse=True)
        print("Character Frequency Analysis:")
        for char, count in sorted_frequency:
            percentage = count / self.total_chars * 100
            print(f"{char}: {percentage:.2f}% ({count})")


def main():
    text = input("Enter the text to analyze: ")
    analyzer = FrequencyAnalyzer(text)
    analyzer.analyze()
    analyzer.display()

if __name__ == "__main__":
    main()