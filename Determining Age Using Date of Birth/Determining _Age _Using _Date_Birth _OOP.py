#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

import datetime

class Age:
    def __init__(self, birthdate):
        self.birthdate = birthdate


    def calculate_age(self):
        # Get current date
        current_date = datetime.datetime.now()
        
        # Calculate the difference between birthdate and current date
        date_difference = current_date - self.birthdate
        
        # Convert the date difference to years
        age = date_difference.days / 365
        
        # Display the result
        print(f"Age: {age:.2f} years")

def get_birthdate_input():
    date = int(input("Enter birthdate (1-31): "))
    month = int(input("Enter birth month (1-12): "))
    year = int(input("Enter birth year: "))
    birthdate = datetime.datetime(year, month, date)
    return birthdate
    
def main():
    while True:
        try:
            # Get birthdate input from user
            birthdate = get_birthdate_input()
        
            # Create an object of the Age class
            age = Age(birthdate)
            
            # Calculate age
            age.calculate_age()
            
            # Stop the loop
            break
    
        except ValueError:
            print("Invalid birthdate input. Please try again.")

if __name__ == "__main__":
    main()