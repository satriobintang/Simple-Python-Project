#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class SpaceCounter:
    def __init__(self, text):
        self.text = text

    def count_spaces(self):
        try:
            space_count = self.text.count(" ")
            return space_count
        except Exception as e:
            print(e)

while True:
    try:
        text = input('Enter the text: ')
        counter = SpaceCounter(text)
        space_count = counter.count_spaces()
        print(f"\nNumber of spaces: {space_count}")
        break
    except Exception as e:
        print(e)
