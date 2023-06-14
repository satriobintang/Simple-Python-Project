#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class LengthConverter:
    def __init__(self, length, original_unit):
        self.length = length
        self.original_unit = original_unit

    def convert(self, target_unit):
        units = {
            'km': 1000,
            'hm': 100,
            'dam': 10,
            'm': 1,
            'dm': 0.1,
            'cm': 0.01,
            'mm': 0.001
        }

        if self.original_unit not in units or target_unit not in units:
            raise ValueError('Invalid length unit')

        conversion_factor = units[self.original_unit] / units[target_unit]
        converted_length = self.length * conversion_factor
        return converted_length

while True:
    try:
        length = float(input('Enter the length: '))
        original_unit = input('Enter the original unit (km, hm, dam, m, dm, cm, mm): ')
        target_unit = input('Enter the target unit (km, hm, dam, m, dm, cm, mm): ')

        length_converter = LengthConverter(length, original_unit)
        converted_length = length_converter.convert(target_unit)
        print(f'The converted length is {converted_length} {target_unit}')
        break
    except ValueError as e:
        print(e)
