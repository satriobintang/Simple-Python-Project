#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class Calculator:
    def __init__(self):
        self.numbers = []

    def get_operation(self):
        while True:
            operation = input("Enter the mathematical operation to perform (+, -, *, /): ")
            if operation in ['+', '-', '*', '/']:
                return operation
            else:
                print("Invalid operation. Please try again.")

    def get_number_count(self):
        while True:
            try:
                count = int(input("How many numbers would you like to input? "))
                if count > 0:
                    return count
                else:
                    print("Invalid count. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_numbers(self, count):
        for i in range(count):
            while True:
                try:
                    number = float(input(f"Enter number {i+1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def calculate(self, operation):
        result = None
        if operation == '+':
            result = sum(self.numbers)
        elif operation == '-':
            result = self.numbers[0] - sum(self.numbers[1:])
        elif operation == '*':
            result = 1
            for number in self.numbers:
                result *= number
        elif operation == '/':
            result = self.numbers[0]
            for number in self.numbers[1:]:
                result /= number
        return result

    def run(self):
        while True:
            try:
                operation = self.get_operation()
                count = self.get_number_count()
                self.get_numbers(count)
                result = self.calculate(operation)
                print(f"Operation result: {result}")
                break
            except Exception as e:
                print(f"Error occurred: {e}")


# Example usage of the program
calc = Calculator()
calc.run()
