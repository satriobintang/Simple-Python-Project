#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

class MagneticFieldConverter:
    def __init__(self, field_type, field_strength):
        self.field_type = field_type
        self.field_strength = field_strength
    
    def convert(self, target_type):
        if self.field_type == 'Tesla':
            if target_type == 'Gauss':
                return self.field_strength * 10**4
            elif target_type == 'Oersted':
                return self.field_strength * 0.79577472
            elif target_type == 'A/m':
                return self.field_strength / (4 * 3.14159265359 * 10**-7)
            elif target_type == 'Wb/m²':
                return self.field_strength
            elif target_type == 'Mx/cm²':
                return self.field_strength * 10**4
            elif target_type == 'kG':
                return self.field_strength * 10**4
            elif target_type == 'mT':
                return self.field_strength * 10**3
            elif target_type == 'µT':
                return self.field_strength
            elif target_type == 'nT':
                return self.field_strength * 10**-3
            elif target_type == 'pT':
                return self.field_strength * 10**-6
            elif target_type == 'fT':
                return self.field_strength * 10**-9
            else:
                raise ValueError('Invalid magnetic field type')
        elif self.field_type == 'Gauss':
            if target_type == 'Tesla':
                return self.field_strength * 10**-4
            elif target_type == 'Oersted':
                return self.field_strength * 0.79577472 * 10**-4
            elif target_type == 'A/m':
                return self.field_strength / (4 * 3.14159265359 * 10**-3)
            elif target_type == 'Wb/m²':
                return self.field_strength * 10**-4
            elif target_type == 'Mx/cm²':
                return self.field_strength
            elif target_type == 'kG':
                return self.field_strength * 0.1
            elif target_type == 'mT':
                return self.field_strength
            elif target_type == 'µT':
                return self.field_strength * 10**-1
            elif target_type == 'nT':
                return self.field_strength * 10**-4
            elif target_type == 'pT':
                return self.field_strength * 10**-7
            elif target_type == 'fT':
                return self.field_strength * 10**-10
            else:
                raise ValueError('Invalid magnetic field type')
        elif self.field_type == 'Oersted':
            if target_type == 'Tesla':
                return self.field_strength * 1.25663706 * 10**-3
            elif target_type == 'Gauss':
                return self.field_strength * 1.25663706 * 10**-1
            elif target_type == 'A/m':
                return self.field_strength * 1.25663706
            elif target_type == 'Wb/m²':
                return self.field_strength * 1.25663706 * 10**-3
            elif target_type == 'Mx/cm²':
                return self.field_strength * 1.25663706
            elif target_type == 'kG':
                return self.field_strength * 1.25663706 * 10**-1
            elif target_type == 'mT':
                return self.field_strength * 1.25663706
            elif target_type == 'µT':
                return self.field_strength * 1.25663706 * 10**3
            elif target_type == 'nT':
                return self.field_strength * 1.25663706 * 10**6
            elif target_type == 'pT':
                return self.field_strength * 1.25663706 * 10**9
            elif target_type == 'fT':
                return self.field_strength * 1.25663706 * 10**12
            else:
                raise ValueError('Invalid magnetic field type')
        elif self.field_type == 'A/m':
            if target_type == 'Tesla':
                return self.field_strength * 4 * 3.14159265359 * 10**-7
            elif target_type == 'Gauss':
                return self.field_strength * 4 * 3.14159265359 * 10**-3
            elif target_type == 'Oersted':
                return self.field_strength * 0.79577472
            elif target_type == 'Wb/m²':
                return self.field_strength * 4 * 3.14159265359 * 10**-7
            elif target_type == 'Mx/cm²':
                return self.field_strength * 4 * 3.14159265359 * 10**-3
            elif target_type == 'kG':
                return self.field_strength * 4 * 3.14159265359 * 10**-3
            elif target_type == 'mT':
                return self.field_strength * 4 * 3.14159265359 * 10**-1
            elif target_type == 'µT':
                return self.field_strength * 4 * 3.14159265359 * 10**2
            elif target_type == 'nT':
                return self.field_strength * 4 * 3.14159265359 * 10**5
            elif target_type == 'pT':
                return self.field_strength * 4 * 3.14159265359 * 10**8
            elif target_type == 'fT':
                return self.field_strength * 4 * 3.14159265359 * 10**11
            else:
                raise ValueError('Invalid magnetic field type')
        elif self.field_type == 'Wb/m²':
            if target_type == 'Tesla':
                return self.field_strength
            elif target_type == 'Gauss':
                return self.field_strength * 10**4
            elif target_type == 'Oersted':
                return self.field_strength * 7957.7472
            elif target_type == 'A/m':
                return self.field_strength / (4 * 3.14159265359 * 10**-7)
            elif target_type == 'Mx/cm²':
                return self.field_strength * 10**4
            elif target_type == 'kG':
                return self.field_strength * 10**4
            elif target_type == 'mT':
                return self.field_strength * 10**3
            elif target_type == 'µT':
                return self.field_strength
            elif target_type == 'nT':
                return self.field_strength * 10**-3
            elif target_type == 'pT':
                return self.field_strength * 10**-6
            elif target_type == 'fT':
                return self.field_strength * 10**-9
            else:
                raise ValueError('Invalid magnetic field type')
        elif self.field_type == 'Mx/cm²':
            if target_type == 'Tesla':
                return self.field_strength * 10**-4
            elif target_type == 'Gauss':
                return self.field_strength * 0.1
            elif target_type == 'Oersted':
                return self.field_strength * 0.79577472 * 10**-4
            elif target_type == 'A/m':
                return self.field_strength / (4 * 3.14159265359 * 10**-3)
            elif target_type == 'Wb/m²':
                return self.field_strength * 10**-4
            elif target_type == 'kG':
                return self.field_strength * 0.1
            elif target_type == 'mT':
                return self.field_strength
            elif target_type == 'µT':
                return self.field_strength * 10**-1
            elif target_type == 'nT':
                return self.field_strength * 10**-4
            elif target_type == 'pT':
                return self.field_strength * 10**-7
            elif target_type == 'fT':
                return self.field_strength * 10**-10
            else:
                raise ValueError('Invalid magnetic field type')
        else:
            raise ValueError('Invalid magnetic field type')

while True:
    try:
        field_type = input('Enter the original magnetic field type (Tesla, Gauss, Oersted, A/m, Wb/m², Mx/cm²): ')
        field_strength = float(input('Enter the magnetic field strength: '))
        target_type = input('Enter the target magnetic field type (Tesla, Gauss, Oersted, A/m, Wb/m², Mx/cm²): ')
        
        field_converter = MagneticFieldConverter(field_type, field_strength)
        converted_field_strength = field_converter.convert(target_type)
        print(f'The converted magnetic field strength is {converted_field_strength:.2e} {target_type}')
        break
    except ValueError as e:
        print(e)