#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class SpeedConverter:
    def __init__(self, speed_value, speed_unit):
        self.speed_value = speed_value
        self.speed_unit = speed_unit
    
    def convert(self, target_unit):
        speed_in_meters_per_second = self.speed_value

        # Convert to meters per second
        if self.speed_unit == 'meters/second':
            pass
        elif self.speed_unit == 'km/hour':
            speed_in_meters_per_second *= 0.277778
        elif self.speed_unit == 'miles/hour':
            speed_in_meters_per_second *= 0.44704
        elif self.speed_unit == 'knots':
            speed_in_meters_per_second *= 0.514444
        elif self.speed_unit == 'mach':
            speed_in_meters_per_second *= 343.2
        else:
            raise ValueError('Invalid speed unit')

        # Convert to target unit
        if target_unit == 'meters/second':
            return speed_in_meters_per_second
        elif target_unit == 'km/hour':
            return speed_in_meters_per_second / 0.277778
        elif target_unit == 'miles/hour':
            return speed_in_meters_per_second / 0.44704
        elif target_unit == 'knots':
            return speed_in_meters_per_second / 0.514444
        elif target_unit == 'mach':
            return speed_in_meters_per_second / 343.2
        else:
            raise ValueError('Invalid target speed unit')

while True:
    try:
        speed_value = float(input('Enter the speed value: '))
        speed_unit = input('Enter the original speed unit (meters/second, km/hour, miles/hour, knots, mach): ')
        target_unit = input('Enter the target speed unit (meters/second, km/hour, miles/hour, knots, mach): ')
        
        speed_converter = SpeedConverter(speed_value, speed_unit)
        converted_speed = speed_converter.convert(target_unit)
        print(f'The converted speed is {converted_speed:.2f} {target_unit}')
        break
    except ValueError as e:
        print(e)
