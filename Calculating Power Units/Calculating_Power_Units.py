#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class PowerConverter:
    def __init__(self, power_type, power):
        self.power_type = power_type
        self.power = power
    
    def convert(self, target_type):
        if self.power_type == 'Watt':
            if target_type == 'Kilowatt':
                return self.power / 1000
            elif target_type == 'Megawatt':
                return self.power / 1e6
            elif target_type == 'Gigawatt':
                return self.power / 1e9
            elif target_type == 'Terawatt':
                return self.power / 1e12
            elif target_type == 'Petawatt':
                return self.power / 1e15
            elif target_type == 'Exawatt':
                return self.power / 1e18
            elif target_type == 'Zettawatt':
                return self.power / 1e21
            elif target_type == 'Yottawatt':
                return self.power / 1e24
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Kilowatt':
            if target_type == 'Watt':
                return self.power * 1000
            elif target_type == 'Megawatt':
                return self.power / 1000
            elif target_type == 'Gigawatt':
                return self.power / 1e6
            elif target_type == 'Terawatt':
                return self.power / 1e9
            elif target_type == 'Petawatt':
                return self.power / 1e12
            elif target_type == 'Exawatt':
                return self.power / 1e15
            elif target_type == 'Zettawatt':
                return self.power / 1e18
            elif target_type == 'Yottawatt':
                return self.power / 1e21
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Megawatt':
            if target_type == 'Watt':
                return self.power * 1e6
            elif target_type == 'Kilowatt':
                return self.power * 1000
            elif target_type == 'Gigawatt':
                return self.power / 1000
            elif target_type == 'Terawatt':
                return self.power / 1e6
            elif target_type == 'Petawatt':
                return self.power / 1e9
            elif target_type == 'Exawatt':
                return self.power / 1e12
            elif target_type == 'Zettawatt':
                return self.power / 1e15
            elif target_type == 'Yottawatt':
                return self.power / 1e18
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Gigawatt':
            if target_type == 'Watt':
                return self.power * 1e9
            elif target_type == 'Kilowatt':
                return self.power * 1e6
            elif target_type == 'Megawatt':
                return self.power * 1000
            elif target_type == 'Terawatt':
                return self.power / 1000
            elif target_type == 'Petawatt':
                return self.power / 1e6
            elif target_type == 'Exawatt':
                return self.power / 1e9
            elif target_type == 'Zettawatt':
                return self.power / 1e12
            elif target_type == 'Yottawatt':
                return self.power / 1e15
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Terawatt':
            if target_type == 'Watt':
                return self.power * 1e12
            elif target_type == 'Kilowatt':
                return self.power * 1e9
            elif target_type == 'Megawatt':
                return self.power * 1e6
            elif target_type == 'Gigawatt':
                return self.power * 1000
            elif target_type == 'Petawatt':
                return self.power / 1000
            elif target_type == 'Exawatt':
                return self.power / 1e6
            elif target_type == 'Zettawatt':
                return self.power / 1e9
            elif target_type == 'Yottawatt':
                return self.power / 1e12
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Petawatt':
            if target_type == 'Watt':
                return self.power * 1e15
            elif target_type == 'Kilowatt':
                return self.power * 1e12
            elif target_type == 'Megawatt':
                return self.power * 1e9
            elif target_type == 'Gigawatt':
                return self.power * 1e6
            elif target_type == 'Terawatt':
                return self.power * 1000
            elif target_type == 'Exawatt':
                return self.power / 1000
            elif target_type == 'Zettawatt':
                return self.power / 1e6
            elif target_type == 'Yottawatt':
                return self.power / 1e9
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Exawatt':
            if target_type == 'Watt':
                return self.power * 1e18
            elif target_type == 'Kilowatt':
                return self.power * 1e15
            elif target_type == 'Megawatt':
                return self.power * 1e12
            elif target_type == 'Gigawatt':
                return self.power * 1e9
            elif target_type == 'Terawatt':
                return self.power * 1e6
            elif target_type == 'Petawatt':
                return self.power * 1000
            elif target_type == 'Zettawatt':
                return self.power / 1000
            elif target_type == 'Yottawatt':
                return self.power / 1e6
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Zettawatt':
            if target_type == 'Watt':
                return self.power * 1e21
            elif target_type == 'Kilowatt':
                return self.power * 1e18
            elif target_type == 'Megawatt':
                return self.power * 1e15
            elif target_type == 'Gigawatt':
                return self.power * 1e12
            elif target_type == 'Terawatt':
                return self.power * 1e9
            elif target_type == 'Petawatt':
                return self.power * 1e6
            elif target_type == 'Exawatt':
                return self.power * 1000
            elif target_type == 'Yottawatt':
                return self.power / 1000
            else:
                raise ValueError('Invalid power type')
        elif self.power_type == 'Yottawatt':
            if target_type == 'Watt':
                return self.power * 1e24
            elif target_type == 'Kilowatt':
                return self.power * 1e21
            elif target_type == 'Megawatt':
                return self.power * 1e18
            elif target_type == 'Gigawatt':
                return self.power * 1e15
            elif target_type == 'Terawatt':
                return self.power * 1e12
            elif target_type == 'Petawatt':
                return self.power * 1e9
            elif target_type == 'Exawatt':
                return self.power * 1e6
            elif target_type == 'Zettawatt':
                return self.power * 1000
            else:
                raise ValueError('Invalid power type')
        else:
            raise ValueError('Invalid power type')

while True:
    try:
        power_type = input('Enter the original power type (Watt, Kilowatt, Megawatt, Gigawatt, Terawatt, Petawatt, Exawatt, Zettawatt, Yottawatt): ')
        power = float(input('Enter the power: '))
        target_type = input('Enter the target power type (Watt, Kilowatt, Megawatt, Gigawatt, Terawatt, Petawatt, Exawatt, Zettawatt, Yottawatt): ')
        
        power_converter = PowerConverter(power_type, power)
        converted_power = power_converter.convert(target_type)
        print(f'The converted power is {converted_power:.2f} {target_type}')
        break
    except ValueError as e:
        print(e)
