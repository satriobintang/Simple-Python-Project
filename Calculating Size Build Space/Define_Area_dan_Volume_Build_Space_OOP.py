#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass
    
    def volume(self):
        pass

class Cube(Shape):
    def __init__(self, s):
        super().__init__("Cube")
        self.s = s
    
    def area(self):
        return 6 * self.s ** 2
    
    def volume(self):
        return self.s ** 3

class RectangularPrism(Shape):
    def __init__(self, l, w, h):
        super().__init__("Rectangular prism")
        self.l = l
        self.w = w
        self.h = h
    
    def area(self):
        return 2 * (self.l * self.w + self.w * self.h + self.h * self.l)
    
    def volume(self):
        return self.l * self.w * self.h

class TriangularPyramid(Shape):
    def __init__(self, b, h):
        super().__init__("Triangular pyramid")
        self.b = b
        self.h = h
    
    def area(self):
        return (self.b * self.h) / 2
    
    def volume(self):
        return (self.b * self.h) / (3 * ((4 * (self.b / 2) ** 2 - 3 * (self.b / 2) ** 2) ** 0.5))

class QuadrilateralPyramid(Shape):
    def __init__(self, b, h):
        super().__init__("Quadrilateral pyramid")
        self.b = b
        self.h = h
    
    def area(self):
        return self.b ** 2 + 2 * (self.b * ((self.b ** 2 - (self.b / 2) ** 2) ** 0.5))
    
    def volume(self):
        return (self.b ** 2 * self.h) / 3

class Pyramid(Shape):
    def __init__(self, b, h, s):
        super().__init__("Pyramid")
        self.b = b
        self.h = h
        self.s = s
    
    def area(self):
        return self.b ** 2 + 2 * ((self.b / 2) ** 2) ** 0.5 * self.s
    
    def volume(self):
        return (self.b ** 2 * self.h) / 3

class TriangularPrism(Shape):
    def __init__(self, b, h, s):
        super().__init__("Triangular prism")
        self.b = b
        self.h = h
        self.s = s
    
    def area(self):
        return (self.b * self.h) / 2 + self.s * (self.b + (self.b ** 2 - (self.b / 2) ** 2) ** 0.5)
    
    def volume(self):
        return (self.b * self.h * self.s) / 2

class QuadrilateralPrism(Shape):
    def __init__(self, b, h, s):
        super().__init__("Quadrilateral prism")
        self.b = b
        self.h = h
        self.s = s
    
    def area(self):
        return self.b ** 2 + 2 * (self.b * ((self.b ** 2 - (self.b / 2) ** 2) ** 0.5)) + 2 * self.s * (self.b + self.h)
    
    def volume(self):
        return self.b * self.h * self.s

class PentagonalPrism(Shape):
    def __init__(self, b, h, s):
        super().__init__("Pentagonal prism")
        self.b = b
        self.h = h
        self.s = s
    
    def area(self):
        return self.b ** 2 + 2 * (self.b * ((self.b ** 2 - (self.b / 2) ** 2) ** 0.5)) + 2 * self.s * (self.b + self.h)
    
    def volume(self):
        return self.b * self.h * self.s

class Cylinder(Shape):
    def __init__(self, r, h):
        super().__init__("Cylinder")
        self.r = r
        self.h = h
    
    def area(self):
        return 2 * 3.14 * self.r * (self.r + self.h)
    
    def volume(self):
        return 3.14 * self.r ** 2 * self.h

class Cone(Shape):
    def __init__(self, r, h):
        super().__init__("Cone")
        self.r = r
        self.h = h
    
    def area(self):
        return 3.14 * self.r * (self.r + ((self.h ** 2 + self.r ** 2) ** 0.5))
    
    def volume(self):
        return (3.14 * self.r ** 2 * self.h) / 3

class Sphere(Shape):
    def __init__(self, r):
        super().__init__("Sphere")
        self.r = r
    
    def area(self):
        return 4 * 3.14 * self.r ** 2
    
    def volume(self):
        return (4 * 3.14 * self.r ** 3) / 3


while True:
    try:
        # Ask the user to select a shape
        print("List of shapes:")
        print("1. Cube")
        print("2. Rectangular prism")
        print("3. Triangular pyramid")
        print("4. Quadrilateral pyramid")
        print("5. Pyramid")
        print("6. Triangular prism")
        print("7. Quadrilateral prism")
        print("8. Pentagonal prism")
        print("9. Cylinder")
        print("10. Cone")
        print("11. Sphere")
    
        shape_num = int(input("Enter the number of the shape you want to calculate the area and volume for: "))

        # Ask the user to input the required dimensions for the selected shape
        if shape_num == 1:  # Cube
            s = float(input("Enter the value of s: "))
            shape = Cube(s)
        elif shape_num == 2:  # Rectangular prism
            l = float(input("Enter the value of l: "))
            w = float(input("Enter the value of w: "))
            h = float(input("Enter the value of h: "))
            shape = RectangularPrism(l, w, h)

        if shape_num == 3:  # Triangular pyramid
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            shape = TriangularPyramid(b, h)
        elif shape_num == 4:  # Quadrilateral pyramid
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            shape = QuadrilateralPyramid(b, h)

        elif shape_num == 5:  # Pyramid
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            s = float(input("Enter the value of s: "))
            shape = Pyramid(b, h, s)

        elif shape_num == 6:  # Triangular prism
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            s = float(input("Enter the value of s: "))
            shape = TriangularPrism(b, h, s)

        elif shape_num == 7:  # Quadrilateral prism
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            s = float(input("Enter the value of s: "))
            shape = QuadrilateralPrism(b, h, s)

        elif shape_num == 8:  # Pentagonal prism
            b = float(input("Enter the value of b: "))
            h = float(input("Enter the value of h: "))
            s = float(input("Enter the value of s: "))
            shape = PentagonalPrism(b, h, s)

        elif shape_num == 9:  # cylinder
            r = float(input("Enter the value of the radius: "))
            h = float(input("Enter the value of the height: "))
            shape = Cylinder(r, h)

        elif shape_num == 10:  # cone
            r = float(input("Enter the value of the radius: "))
            h = float(input("Enter the value of the height: "))
            shape = Cone(r, h)

        elif shape_num == 11:  # sphere
            r = float(input("Enter the value of the radius: "))
            shape = Sphere(r)

        # Display the results
        print(f"Area of {shape.name}: {shape.area()}")
        print(f"Volume of {shape.name}: {shape.volume()}")
        break
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
