#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class LeapYear:
    def __init__(self, year):
        self.year = year
        self.is_leap_year = False

    def check_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    self.is_leap_year = True
            else:
                self.is_leap_year = True

def main():
    year = 0
    while True:
        try:
            year = int(input("Enter a year : "))
        except ValueError:
            print("Please enter a valid number.")

        leap_year = LeapYear(year)
        leap_year.check_leap_year()
        if leap_year.is_leap_year:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
        
        action = (input("Press Q to quit, Y to Continue : "))

        if action.lower() == "y":
            continue
        elif action.lower() == "q":
            break

if __name__ == "__main__":
    main()
