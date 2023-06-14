#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class WeightConverter:
    def __init__(self, weight, original_unit):
        self.weight = weight
        self.original_unit = original_unit

    def convert(self, target_unit):
        units = {
            'kg': 1000,
            'hg': 100,
            'dag': 10,
            'g': 1,
            'dg': 0.1,
            'cg': 0.01,
            'mg': 0.001
        }

        if self.original_unit not in units or target_unit not in units:
            raise ValueError('Invalid weight unit')

        conversion_factor = units[self.original_unit] / units[target_unit]
        converted_weight = self.weight * conversion_factor
        return converted_weight

while True:
    try:
        weight = float(input('Enter the weight: '))
        original_unit = input('Enter the original unit (kg, hg, dag, g, dg, cg, mg): ')
        target_unit = input('Enter the target unit (kg, hg, dag, g, dg, cg, mg): ')

        weight_converter = WeightConverter(weight, original_unit)
        converted_weight = weight_converter.convert(target_unit)
        print(f'The converted weight is {converted_weight} {target_unit}')
        break
    except ValueError as e:
        print(e)
