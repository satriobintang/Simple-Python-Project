#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class NumberChecker:
    def __init__(self, number):
        self.number = number
    
    def is_even(self):
        return self.number % 2 == 0

while True:
    try:
        number = int(input('Enter a number: '))
        number_checker = NumberChecker(number)
        if number_checker.is_even():
            print('The number is even.')
        else:
            print('The number is odd.')
        break
    except ValueError as e:
        print(e)
