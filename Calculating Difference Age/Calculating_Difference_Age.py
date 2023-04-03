#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

from datetime import datetime

class AgeCalculator:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

while True:
    try:
        birth_date_1 = input('Enter the birth date of person 1 (YYYY-MM-DD): ')
        birth_date_2 = input('Enter the birth date of person 2 (YYYY-MM-DD): ')
        birth_date_1 = datetime.strptime(birth_date_1, '%Y-%m-%d')
        birth_date_2 = datetime.strptime(birth_date_2, '%Y-%m-%d')
        age_calculator_1 = AgeCalculator(birth_date_1)
        age_calculator_2 = AgeCalculator(birth_date_2)
        age_1 = age_calculator_1.calculate_age()
        age_2 = age_calculator_2.calculate_age()
        age_difference = abs(age_1 - age_2)
        print(f'The age difference between the two persons is {age_difference} years')
        break
    except Exception as e:
        print(e)
