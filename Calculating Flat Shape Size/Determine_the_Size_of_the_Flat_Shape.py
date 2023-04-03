#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

#Asking user to input the type of shape
print("List of shapes:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Trapezoid")
print("5. Rhombus")
print("6. Circle")
print("7. Kite")
print("8. Pentagon")
print("9. Hexagon")
print("10. Parallelogram")

while True:
    try:
        shape = int(input("\nEnter the number of the shape you want to calculate the area and perimeter: "))

        # Calculate area and perimeter based on the selected shape
        if shape == 1:  # Square
            s = int(input("Enter the length of the side: "))
            area = s ** 2
            perimeter = 4 * s
            print(f"The area of the square is {area} and its perimeter is {perimeter}.")
        elif shape == 2:  # Rectangle
            p = int(input("Enter the length: "))
            l = int(input("Enter the width: "))
            area = p * l
            perimeter = 2 * (p + l)
            print(f"The area of the rectangle is {area} and its perimeter is {perimeter}.")
        elif shape == 3:  # Triangle
            a = int(input("Enter the length of the base: "))
            t = int(input("Enter the height: "))
            area = (a * t) / 2
            s = (a + t + (a ** 2 + t ** 2) ** 0.5) / 2
            perimeter = a + t + (a ** 2 + t ** 2) ** 0.5
            print(f"The area of the triangle is {area} and its perimeter is {perimeter}.")
        elif shape == 4:  # Trapezoid
            a = int(input("Enter the length of the first base: "))
            b = int(input("Enter the length of the second base: "))
            t = int(input("Enter the height: "))
            area = ((a + b) * t) / 2
            s = (a + b + (((a - b) ** 2 + t ** 2) ** 0.5)) / 2
            perimeter = a + b + 2 * (((a - b) ** 2 + t ** 2) ** 0.5)
            print(f"The area of the trapezoid is {area} and its perimeter is {perimeter}.")
        elif shape == 5:  # Rhombus
            d1 = int(input("Enter the length of the first diagonal: "))
            d2 = int(input("Enter the length of the second diagonal: "))
            area = (d1 * d2) / 2
            s = (d1 + d2) / 2
            perimeter = 2 * (s ** 2 + (d1 * d2 / s) ** 0.5) ** 0.5
            print(f"The area of the rhombus is {area} and its perimeter is {perimeter}.")
        elif shape == 6:  # Circle
            r = int(input("Enter the radius: "))
            area = 3.14 * r ** 2
            perimeter = 2 * 3.14 * r
            print(f"The area of the circle is {area} and its circumference is {perimeter}.")
        if shape == 7:  # Rhombus
            d1 = int(input("Enter the length of the first diagonal: "))
            d2 = int(input("Enter the length of the second diagonal: "))
            area = (d1 * d2) / 2
            s1 = (d1 ** 2 - d2 ** 2) ** 0.5 / 2
            s2 = (d2 ** 2 - d1 ** 2) ** 0.5 / 2
            perimeter = 2 * (s1 + s2)
            print(f"The area of the rhombus is {area} and the perimeter is {perimeter}.")
        elif shape == 8:  # Pentagon
            s = int(input("Enter the length of the side: "))
            area = (5 * s ** 2) / (4 * ((5 ** 0.5 + 1) / 2) ** 2)
            perimeter = 5 * s
            print(f"The area of the pentagon is {area} and the perimeter is {perimeter}.")
        elif shape == 9:  # Hexagon
            s = int(input("Enter the length of the side: "))
            area = (3 * (3 ** 0.5) * s ** 2) / 2
            perimeter = 6 * s
            print(f"The area of the hexagon is {area} and the perimeter is {perimeter}.")
        elif shape == 10:  # Parallelogram
            a = int(input("Enter the length of the base: "))
            t = int(input("Enter the height: "))
            area = a * t
            perimeter = 2 * (a + t)
            print(f"The area of the parallelogram is {area} and the perimeter is {perimeter}.")
    except ValueError:
        print("The input must be a number!")

    