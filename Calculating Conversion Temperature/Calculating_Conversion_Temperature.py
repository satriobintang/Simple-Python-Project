#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class TemperatureConverter:
    def __init__(self, temperature_type, temperature):
        self.temperature_type = temperature_type
        self.temperature = temperature
    
    def convert(self, target_type):
        if self.temperature_type == 'Celcius':
            if target_type == 'Fahrenheit':
                return self.temperature * 9 / 5 + 32
            elif target_type == 'Kelvin':
                return self.temperature + 273.15
            elif target_type == 'Reaumur':
                return self.temperature * 0.8
            else:
                raise ValueError('Invalid temperature type')
        elif self.temperature_type == 'Fahrenheit':
            if target_type == 'Celcius':
                return (self.temperature - 32) * 5 / 9
            elif target_type == 'Kelvin':
                return (self.temperature + 459.67) * 5 / 9
            elif target_type == 'Reaumur':
                return (self.temperature - 32) * 4 / 9
            else:
                raise ValueError('Invalid temperature type')
        elif self.temperature_type == 'Kelvin':
            if target_type == 'Celcius':
                return self.temperature - 273.15
            elif target_type == 'Fahrenheit':
                return self.temperature * 9 / 5 - 459.67
            elif target_type == 'Reaumur':
                return (self.temperature - 273.15) * 0.8
            else:
                raise ValueError('Invalid temperature type')
        elif self.temperature_type == 'Reaumur':
            if target_type == 'Celcius':
                return self.temperature / 0.8
            elif target_type == 'Fahrenheit':
                return self.temperature * 9 / 4 + 32
            elif target_type == 'Kelvin':
                return (self.temperature / 0.8) + 273.15
            else:
                raise ValueError('Invalid temperature type')
        else:
            raise ValueError('Invalid temperature type')

while True:
    try:
        temperature_type = input('Enter the original temperature type (Celcius, Fahrenheit, Kelvin, Reaumur): ')
        temperature = float(input('Enter the temperature: '))
        target_type = input('Enter the target temperature type (Celcius, Fahrenheit, Kelvin, Reaumur): ')
        
        temperature_converter = TemperatureConverter(temperature_type, temperature)
        converted_temperature = temperature_converter.convert(target_type)
        print(f'The converted temperature is {converted_temperature:.2f} {target_type}')
        break
    except ValueError as e:
        print(e)
