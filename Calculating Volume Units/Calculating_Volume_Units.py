#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class VolumeConverter:
    def __init__(self, volume_value, volume_unit):
        self.volume_value = volume_value
        self.volume_unit = volume_unit
    
    def convert(self, target_unit):
        volume_in_cubic_meters = self.volume_value

        # Convert to cubic meters
        if self.volume_unit == 'cubic meters':
            pass
        elif self.volume_unit == 'liters':
            volume_in_cubic_meters *= 0.001
        elif self.volume_unit == 'gallons':
            volume_in_cubic_meters *= 0.00378541
        elif self.volume_unit == 'pints':
            volume_in_cubic_meters *= 0.000473176
        elif self.volume_unit == 'fluid ounces':
            volume_in_cubic_meters *= 0.0000295735
        elif self.volume_unit == 'cups':
            volume_in_cubic_meters *= 0.000236588
        elif self.volume_unit == 'teaspoons':
            volume_in_cubic_meters *= 0.00000492892
        else:
            raise ValueError('Invalid volume unit')

        # Convert to target unit
        if target_unit == 'cubic meters':
            return volume_in_cubic_meters
        elif target_unit == 'liters':
            return volume_in_cubic_meters / 0.001
        elif target_unit == 'gallons':
            return volume_in_cubic_meters / 0.00378541
        elif target_unit == 'pints':
            return volume_in_cubic_meters / 0.000473176
        elif target_unit == 'fluid ounces':
            return volume_in_cubic_meters / 0.0000295735
        elif target_unit == 'cups':
            return volume_in_cubic_meters / 0.000236588
        elif target_unit == 'teaspoons':
            return volume_in_cubic_meters / 0.00000492892
        else:
            raise ValueError('Invalid target volume unit')

while True:
    try:
        volume_value = float(input('Enter the volume value: '))
        volume_unit = input('Enter the original volume unit (cubic meters, liters, gallons, pints, fluid ounces, cups, teaspoons): ')
        target_unit = input('Enter the target volume unit (cubic meters, liters, gallons, pints, fluid ounces, cups, teaspoons): ')
        
        volume_converter = VolumeConverter(volume_value, volume_unit)
        converted_volume = volume_converter.convert(target_unit)
        print(f'The converted volume is {converted_volume:.2f} {target_unit}')
        break
    except ValueError as e:
        print(e)
