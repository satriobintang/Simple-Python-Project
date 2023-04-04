#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class BMI:
    def __init__(self, gender, weight, height, age):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.bmi = 0

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def classify_bmi(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_recommendation(self):
        if self.bmi < 18.5:
            return "You should eat more to gain weight."
        elif self.bmi < 25:
            return "You are at a healthy weight. Keep up the good work!"
        elif self.bmi < 30:
            return "You should try to lose some weight to lower your BMI."
        else:
            return "You should try to lose some weight to lower your BMI and improve your health."

def main():
    gender = input("Enter your gender (M/F): ")
    weight = 0
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    height = 0
    while True:
        try:
            height = float(input("Enter your height (m): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    age = 0
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    bmi = BMI(gender, weight, height, age)
    bmi.calculate_bmi()
    classification = bmi.classify_bmi()
    recommendation = bmi.get_recommendation()

    print("Your BMI is:", bmi.bmi)
    print("You are classified as:", classification)
    print(recommendation)

if __name__ == "__main__":
    main()
