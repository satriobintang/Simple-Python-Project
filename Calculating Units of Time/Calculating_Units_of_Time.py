#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class TimeConverter:
    def __init__(self, time_value, time_unit):
        self.time_value = time_value
        self.time_unit = time_unit
    
    def convert(self, target_unit):
        time_in_seconds = self.time_value

        # Convert to seconds
        if self.time_unit == 'seconds':
            pass
        elif self.time_unit == 'minutes':
            time_in_seconds *= 60
        elif self.time_unit == 'hours':
            time_in_seconds *= 3600
        elif self.time_unit == 'days':
            time_in_seconds *= 86400
        elif self.time_unit == 'months':
            time_in_seconds *= 2629800
        elif self.time_unit == 'years':
            time_in_seconds *= 31557600
        elif self.time_unit == 'decades':
            time_in_seconds *= 315576000
        elif self.time_unit == 'centuries':
            time_in_seconds *= 3155760000
        elif self.time_unit == 'millennia':
            time_in_seconds *= 31557600000
        else:
            raise ValueError('Invalid time unit')

        # Convert to target unit
        if target_unit == 'seconds':
            return time_in_seconds
        elif target_unit == 'minutes':
            return time_in_seconds / 60
        elif target_unit == 'hours':
            return time_in_seconds / 3600
        elif target_unit == 'days':
            return time_in_seconds / 86400
        elif target_unit == 'months':
            return time_in_seconds / 2629800
        elif target_unit == 'years':
            return time_in_seconds / 31557600
        elif target_unit == 'decades':
            return time_in_seconds / 315576000
        elif target_unit == 'centuries':
            return time_in_seconds / 3155760000
        elif target_unit == 'millennia':
            return time_in_seconds / 31557600000
        else:
            raise ValueError('Invalid target time unit')

while True:
    try:
        time_value = float(input('Enter the time value: '))
        time_unit = input('Enter the original time unit (seconds, minutes, hours, days, months, years, decades, centuries, millennia): ')
        target_unit = input('Enter the target time unit (seconds, minutes, hours, days, months, years, decades, centuries, millennia): ')
        
        time_converter = TimeConverter(time_value, time_unit)
        converted_time = time_converter.convert(target_unit)
        print(f'The converted time is {converted_time:.2f} {target_unit}')
        break
    except ValueError as e:
        print(e)
