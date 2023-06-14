#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class AreaConverter:
    def __init__(self, area_value, area_unit):
        self.area_value = area_value
        self.area_unit = area_unit
    
    def convert(self, target_unit):
        area_in_square_meters = self.area_value

        # Convert to square meters
        if self.area_unit == 'square meters':
            pass
        elif self.area_unit == 'square kilometers':
            area_in_square_meters *= 1000000
        elif self.area_unit == 'acres':
            area_in_square_meters *= 4046.86
        elif self.area_unit == 'hectares':
            area_in_square_meters *= 10000
        elif self.area_unit == 'square miles':
            area_in_square_meters *= 2589988.11
        elif self.area_unit == 'square yards':
            area_in_square_meters *= 0.836127
        elif self.area_unit == 'square feet':
            area_in_square_meters *= 0.092903
        else:
            raise ValueError('Invalid area unit')

        # Convert to target unit
        if target_unit == 'square meters':
            return area_in_square_meters
        elif target_unit == 'square kilometers':
            return area_in_square_meters / 1000000
        elif target_unit == 'acres':
            return area_in_square_meters / 4046.86
        elif target_unit == 'hectares':
            return area_in_square_meters / 10000
        elif target_unit == 'square miles':
            return area_in_square_meters / 2589988.11
        elif target_unit == 'square yards':
            return area_in_square_meters / 0.836127
        elif target_unit == 'square feet':
            return area_in_square_meters / 0.092903
        else:
            raise ValueError('Invalid target area unit')

while True:
    try:
        area_value = float(input('Enter the area value: '))
        area_unit = input('Enter the original area unit (square meters, square kilometers, acres, hectares, square miles, square yards, square feet): ')
        target_unit = input('Enter the target area unit (square meters, square kilometers, acres, hectares, square miles, square yards, square feet): ')
        
        area_converter = AreaConverter(area_value, area_unit)
        converted_area = area_converter.convert(target_unit)
        print(f'The converted area is {converted_area:.2f} {target_unit}')
        break
    except ValueError as e:
        print(e)
