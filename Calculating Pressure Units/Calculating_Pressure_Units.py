#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class PressureConverter:
    def __init__(self, pressure_type, pressure):
        self.pressure_type = pressure_type
        self.pressure = pressure
    
    def convert(self, target_type):
        if self.pressure_type == 'Pascal':
            if target_type == 'Bar':
                return self.pressure / 100000
            elif target_type == 'Psi':
                return self.pressure * 0.0001450377
            elif target_type == 'Torr':
                return self.pressure * 0.00750062
            elif target_type == 'Atmosphere':
                return self.pressure * 0.00000986923267
            # Tambahkan konversi ke satuan tekanan lainnya di sini
            else:
                raise ValueError('Invalid pressure type')
        elif self.pressure_type == 'Bar':
            if target_type == 'Pascal':
                return self.pressure * 100000
            elif target_type == 'Psi':
                return self.pressure * 14.50377
            elif target_type == 'Torr':
                return self.pressure * 750.062
            elif target_type == 'Atmosphere':
                return self.pressure * 0.986923267
            # Tambahkan konversi ke satuan tekanan lainnya di sini
            else:
                raise ValueError('Invalid pressure type')
        elif self.pressure_type == 'Psi':
            if target_type == 'Pascal':
                return self.pressure * 6894.75729
            elif target_type == 'Bar':
                return self.pressure * 0.0689475729
            elif target_type == 'Torr':
                return self.pressure * 51.7149326
            elif target_type == 'Atmosphere':
                return self.pressure * 0.0680459639
            # Tambahkan konversi ke satuan tekanan lainnya di sini
            else:
                raise ValueError('Invalid pressure type')
        elif self.pressure_type == 'Torr':
            if target_type == 'Pascal':
                return self.pressure * 133.322368
            elif target_type == 'Bar':
                return self.pressure * 0.00133322368
            elif target_type == 'Psi':
                return self.pressure * 0.0193367747
            elif target_type == 'Atmosphere':
                return self.pressure * 0.00131578947
            # Tambahkan konversi ke satuan tekanan lainnya di sini
            else:
                raise ValueError('Invalid pressure type')
        elif self.pressure_type == 'Atmosphere':
            if target_type == 'Pascal':
                return self.pressure * 101325
            elif target_type == 'Bar':
                return self.pressure * 1.01325
            elif target_type == 'Psi':
                return self.pressure * 14.6959494
            elif target_type == 'Torr':
                return self.pressure * 760
            # Tambahkan konversi ke satuan tekanan lainnya di sini
            else:
                raise ValueError('Invalid pressure type')
        else:
            raise ValueError('Invalid pressure type')

while True:
    try:
        pressure_type = input('Enter the original pressure type (Pascal, Bar, Psi, Torr, Atmosphere): ')
        pressure = float(input('Enter the pressure: '))
        target_type = input('Enter the target pressure type (Pascal, Bar, Psi, Torr, Atmosphere): ')
        
        pressure_converter = PressureConverter(pressure_type, pressure)
        converted_pressure = pressure_converter.convert(target_type)
        print(f'The converted pressure is {converted_pressure:.2f} {target_type}')
        break
    except ValueError as e:
        print(e)
