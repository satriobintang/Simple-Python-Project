#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class FrequencyConverter:
    def __init__(self, frequency_type, frequency):
        self.frequency_type = frequency_type
        self.frequency = frequency
    
    def convert(self, target_type):
        if self.frequency_type == 'Hertz':
            if target_type == 'Kilohertz':
                return self.frequency / 1000
            elif target_type == 'Megahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Gigahertz':
                return self.frequency / 1_000_000_000
            elif target_type == 'Terahertz':
                return self.frequency / 1_000_000_000_000
            elif target_type == 'Petahertz':
                return self.frequency / 1_000_000_000_000_000
            elif target_type == 'Exahertz':
                return self.frequency / 1_000_000_000_000_000_000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000_000_000_000_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000_000_000_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Kilohertz':
            if target_type == 'Hertz':
                return self.frequency * 1000
            elif target_type == 'Megahertz':
                return self.frequency / 1000
            elif target_type == 'Gigahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Terahertz':
                return self.frequency / 1_000_000_000
            elif target_type == 'Petahertz':
                return self.frequency / 1_000_000_000_000
            elif target_type == 'Exahertz':
                return self.frequency / 1_000_000_000_000_000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000_000_000_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000_000_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Megahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1000
            elif target_type == 'Gigahertz':
                return self.frequency / 1000
            elif target_type == 'Terahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Petahertz':
                return self.frequency / 1_000_000_000
            elif target_type == 'Exahertz':
                return self.frequency / 1_000_000_000_000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000_000_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Gigahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1000
            elif target_type == 'Terahertz':
                return self.frequency / 1000
            elif target_type == 'Petahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Exahertz':
                return self.frequency / 1_000_000_000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Terahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1_000_000
            elif target_type == 'Gigahertz':
                return self.frequency * 1000
            elif target_type == 'Petahertz':
                return self.frequency / 1000
            elif target_type == 'Exahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Petahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Gigahertz':
                return self.frequency * 1_000_000
            elif target_type == 'Terahertz':
                return self.frequency * 1000
            elif target_type == 'Exahertz':
                return self.frequency / 1000
            elif target_type == 'Zettahertz':
                return self.frequency / 1_000_000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Exahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000_000_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1_000_000_000_000
            elif target_type == 'Gigahertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Terahertz':
                return self.frequency * 1_000_000
            elif target_type == 'Petahertz':
                return self.frequency * 1000
            elif target_type == 'Zettahertz':
                return self.frequency / 1000
            elif target_type == 'Yottahertz':
                return self.frequency / 1_000_000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Zettahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000_000_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000_000_000_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1_000_000_000_000_000
            elif target_type == 'Gigahertz':
                return self.frequency * 1_000_000_000_000
            elif target_type == 'Terahertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Petahertz':
                return self.frequency * 1_000_000
            elif target_type == 'Exahertz':
                return self.frequency * 1000
            elif target_type == 'Yottahertz':
                return self.frequency / 1000
            else:
                raise ValueError('Invalid frequency type')
        elif self.frequency_type == 'Yottahertz':
            if target_type == 'Hertz':
                return self.frequency * 1_000_000_000_000_000_000_000_000
            elif target_type == 'Kilohertz':
                return self.frequency * 1_000_000_000_000_000_000_000
            elif target_type == 'Megahertz':
                return self.frequency * 1_000_000_000_000_000_000
            elif target_type == 'Gigahertz':
                return self.frequency * 1_000_000_000_000_000
            elif target_type == 'Terahertz':
                return self.frequency * 1_000_000_000_000
            elif target_type == 'Petahertz':
                return self.frequency * 1_000_000_000
            elif target_type == 'Exahertz':
                return self.frequency * 1_000_000
            elif target_type == 'Zettahertz':
                return self.frequency * 1000
            else:
                raise ValueError('Invalid frequency type')
        else:
            raise ValueError('Invalid frequency type')

while True:
    try:
        frequency_type = input('Enter the original frequency type (Hertz, Kilohertz, Megahertz, Gigahertz, Terahertz, Petahertz, Exahertz, Zettahertz, Yottahertz): ')
        frequency = float(input('Enter the frequency: '))
        target_type = input('Enter the target frequency type (Hertz, Kilohertz, Megahertz, Gigahertz, Terahertz, Petahertz, Exahertz, Zettahertz, Yottahertz): ')
        
        frequency_converter = FrequencyConverter(frequency_type, frequency)
        converted_frequency = frequency_converter.convert(target_type)
        print(f'The converted frequency is {converted_frequency:.2f} {target_type}')
        break
    except ValueError as e:
        print(e)
