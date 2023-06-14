#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#March 2023

class EnergyConverter:
    def __init__(self, energy_type, energy):
        self.energy_type = energy_type
        self.energy = energy
    
    def convert(self, target_type):
        if self.energy_type == 'Joule':
            if target_type == 'Joule':
                return self.energy
            elif target_type == 'Kilojoule':
                return self.energy / 1000
            elif target_type == 'Calorie':
                return self.energy / 4.184
            elif target_type == 'Kilocalorie':
                return self.energy / 4184
            elif target_type == 'Electronvolt':
                return self.energy * 6.242e+18
            elif target_type == 'British Thermal Unit':
                return self.energy / 1055
            elif target_type == 'Foot-pound':
                return self.energy / 1.356
            elif target_type == 'Erg':
                return self.energy * 10**7
            elif target_type == 'Watt-hour':
                return self.energy / 3600
            elif target_type == 'Kilowatt-hour':
                return self.energy / 3.6e+6
            elif target_type == 'Megawatt-hour':
                return self.energy / 3.6e+9
            elif target_type == 'Gigawatt-hour':
                return self.energy / 3.6e+12
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Kilojoule':
            if target_type == 'Joule':
                return self.energy * 1000
            elif target_type == 'Kilojoule':
                return self.energy
            elif target_type == 'Calorie':
                return self.energy * 239.006
            elif target_type == 'Kilocalorie':
                return self.energy * 0.239006
            elif target_type == 'Electronvolt':
                return self.energy * 6.242e+21
            elif target_type == 'British Thermal Unit':
                return self.energy * 947.817
            elif target_type == 'Foot-pound':
                return self.energy * 737.562
            elif target_type == 'Erg':
                return self.energy * 10**10
            elif target_type == 'Watt-hour':
                return self.energy / 3.6
            elif target_type == 'Kilowatt-hour':
                return self.energy / 3600
            elif target_type == 'Megawatt-hour':
                return self.energy / 3.6e+6
            elif target_type == 'Gigawatt-hour':
                return self.energy / 3.6e+9
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Calorie':
            if target_type == 'Joule':
                return self.energy * 4.184
            elif target_type == 'Kilojoule':
                return self.energy * 0.004184
            elif target_type == 'Calorie':
                return self.energy
            elif target_type == 'Kilocalorie':
                return self.energy * 0.001
            elif target_type == 'Electronvolt':
                return self.energy * 2.611e+19
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.966
            elif target_type == 'Foot-pound':
                return self.energy * 3.086
            elif target_type == 'Erg':
                return self.energy * 4.184e+7
            elif target_type == 'Watt-hour':
                return self.energy / 860.421
            elif target_type == 'Kilowatt-hour':
                return self.energy / 860.421e+3
            elif target_type == 'Megawatt-hour':
                return self.energy / 860.421e+6
            elif target_type == 'Gigawatt-hour':
                return self.energy / 860.421e+9
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Kilocalorie':
            if target_type == 'Joule':
                return self.energy * 4184
            elif target_type == 'Kilojoule':
                return self.energy * 4.184
            elif target_type == 'Calorie':
                return self.energy * 1000
            elif target_type == 'Kilocalorie':
                return self.energy
            elif target_type == 'Electronvolt':
                return self.energy * 2.611e+22
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.966e+3
            elif target_type == 'Foot-pound':
                return self.energy * 3.086e+3
            elif target_type == 'Erg':
                return self.energy * 4.184e+10
            elif target_type == 'Watt-hour':
                return self.energy / 0.860421
            elif target_type == 'Kilowatt-hour':
                return self.energy / 860.421
            elif target_type == 'Megawatt-hour':
                return self.energy / 860.421e+3
            elif target_type == 'Gigawatt-hour':
                return self.energy / 860.421e+6
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Electronvolt':
            if target_type == 'Joule':
                return self.energy * 1.602e-19
            elif target_type == 'Kilojoule':
                return self.energy * 1.602e-22
            elif target_type == 'Calorie':
                return self.energy * 3.829e-20
            elif target_type == 'Kilocalorie':
                return self.energy * 3.829e-23
            elif target_type == 'Electronvolt':
                return self.energy
            elif target_type == 'British Thermal Unit':
                return self.energy * 6.242e-21
            elif target_type == 'Foot-pound':
                return self.energy * 4.869e-21
            elif target_type == 'Erg':
                return self.energy * 1.602e-12
            elif target_type == 'Watt-hour':
                return self.energy * 4.45e-23
            elif target_type == 'Kilowatt-hour':
                return self.energy * 4.45e-26
            elif target_type == 'Megawatt-hour':
                return self.energy * 4.45e-29
            elif target_type == 'Gigawatt-hour':
                return self.energy * 4.45e-32
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'British Thermal Unit':
            if target_type == 'Joule':
                return self.energy * 1055
            elif target_type == 'Kilojoule':
                return self.energy * 1.055
            elif target_type == 'Calorie':
                return self.energy * 252
            elif target_type == 'Kilocalorie':
                return self.energy * 0.252
            elif target_type == 'Electronvolt':
                return self.energy * 1.055e+21
            elif target_type == 'British Thermal Unit':
                return self.energy
            elif target_type == 'Foot-pound':
                return self.energy * 778
            elif target_type == 'Erg':
                return self.energy * 1.055e+10
            elif target_type == 'Watt-hour':
                return self.energy / 3.412
            elif target_type == 'Kilowatt-hour':
                return self.energy / 3412
            elif target_type == 'Megawatt-hour':
                return self.energy / 3.412e+6
            elif target_type == 'Gigawatt-hour':
                return self.energy / 3.412e+9
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Foot-pound':
            if target_type == 'Joule':
                return self.energy * 1.356
            elif target_type == 'Kilojoule':
                return self.energy * 0.001356
            elif target_type == 'Calorie':
                return self.energy * 0.324048
            elif target_type == 'Kilocalorie':
                return self.energy * 0.000324048
            elif target_type == 'Electronvolt':
                return self.energy * 8.462e+18
            elif target_type == 'British Thermal Unit':
                return self.energy * 0.00128507
            elif target_type == 'Foot-pound':
                return self.energy
            elif target_type == 'Erg':
                return self.energy * 1.356e+7
            elif target_type == 'Watt-hour':
                return self.energy / 2655.22
            elif target_type == 'Kilowatt-hour':
                return self.energy / 2.65522e+6
            elif target_type == 'Megawatt-hour':
                return self.energy / 2.65522e+9
            elif target_type == 'Gigawatt-hour':
                return self.energy / 2.65522e+12
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Erg':
            if target_type == 'Joule':
                return self.energy * 1e-7
            elif target_type == 'Kilojoule':
                return self.energy * 1e-10
            elif target_type == 'Calorie':
                return self.energy * 2.389e-8
            elif target_type == 'Kilocalorie':
                return self.energy * 2.389e-11
            elif target_type == 'Electronvolt':
                return self.energy * 6.242e+11
            elif target_type == 'British Thermal Unit':
                return self.energy * 9.478e-11
            elif target_type == 'Foot-pound':
                return self.energy * 7.376e-8
            elif target_type == 'Erg':
                return self.energy
            elif target_type == 'Watt-hour':
                return self.energy * 2.778e-14
            elif target_type == 'Kilowatt-hour':
                return self.energy * 2.778e-17
            elif target_type == 'Megawatt-hour':
                return self.energy * 2.778e-20
            elif target_type == 'Gigawatt-hour':
                return self.energy * 2.778e-23
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Watt-hour':
            if target_type == 'Joule':
                return self.energy * 3600
            elif target_type == 'Kilojoule':
                return self.energy * 3.6
            elif target_type == 'Calorie':
                return self.energy * 859.845
            elif target_type == 'Kilocalorie':
                return self.energy * 0.859845
            elif target_type == 'Electronvolt':
                return self.energy * 2.247e+22
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.412
            elif target_type == 'Foot-pound':
                return self.energy * 2655.22
            elif target_type == 'Erg':
                return self.energy * 3.6e+10
            elif target_type == 'Watt-hour':
                return self.energy
            elif target_type == 'Kilowatt-hour':
                return self.energy / 1000
            elif target_type == 'Megawatt-hour':
                return self.energy / 1e+6
            elif target_type == 'Gigawatt-hour':
                return self.energy / 1e+9
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Kilowatt-hour':
            if target_type == 'Joule':
                return self.energy * 3.6e+6
            elif target_type == 'Kilojoule':
                return self.energy * 3600
            elif target_type == 'Calorie':
                return self.energy * 859845
            elif target_type == 'Kilocalorie':
                return self.energy * 859.845
            elif target_type == 'Electronvolt':
                return self.energy * 2.247e+25
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.412e+3
            elif target_type == 'Foot-pound':
                return self.energy * 2.655e+6
            elif target_type == 'Erg':
                return self.energy * 3.6e+13
            elif target_type == 'Watt-hour':
                return self.energy * 1000
            elif target_type == 'Kilowatt-hour':
                return self.energy
            elif target_type == 'Megawatt-hour':
                return self.energy / 1000
            elif target_type == 'Gigawatt-hour':
                return self.energy / 1e+6
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Megawatt-hour':
            if target_type == 'Joule':
                return self.energy * 3.6e+9
            elif target_type == 'Kilojoule':
                return self.energy * 3.6e+6
            elif target_type == 'Calorie':
                return self.energy * 8.598e+8
            elif target_type == 'Kilocalorie':
                return self.energy * 859845
            elif target_type == 'Electronvolt':
                return self.energy * 2.247e+28
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.412e+6
            elif target_type == 'Foot-pound':
                return self.energy * 2.655e+9
            elif target_type == 'Erg':
                return self.energy * 3.6e+16
            elif target_type == 'Watt-hour':
                return self.energy * 1e+6
            elif target_type == 'Kilowatt-hour':
                return self.energy * 1000
            elif target_type == 'Megawatt-hour':
                return self.energy
            elif target_type == 'Gigawatt-hour':
                return self.energy / 1000
            else:
                raise ValueError('Invalid energy type')
        elif self.energy_type == 'Gigawatt-hour':
            if target_type == 'Joule':
                return self.energy * 3.6e+12
            elif target_type == 'Kilojoule':
                return self.energy * 3.6e+9
            elif target_type == 'Calorie':
                return self.energy * 8.598e+11
            elif target_type == 'Kilocalorie':
                return self.energy * 8.598e+8
            elif target_type == 'Electronvolt':
                return self.energy * 2.247e+31
            elif target_type == 'British Thermal Unit':
                return self.energy * 3.412e+9
            elif target_type == 'Foot-pound':
                return self.energy * 2.655e+12
            elif target_type == 'Erg':
                return self.energy * 3.6e+19
            elif target_type == 'Watt-hour':
                return self.energy * 1e+9
            elif target_type == 'Kilowatt-hour':
                return self.energy * 1e+6
            elif target_type == 'Megawatt-hour':
                return self.energy * 1000
            elif target_type == 'Gigawatt-hour':
                return self.energy
            else:
                raise ValueError('Invalid energy type')
        else:
            raise ValueError('Invalid energy type')

while True:
    try:
        energy_type = input('Enter the original energy type (Joule, Kilojoule, Calorie, Kilocalorie, Electronvolt, British Thermal Unit, Foot-pound, Erg, Watt-hour, Kilowatt-hour, Megawatt-hour, Gigawatt-hour): ')
        energy = float(input('Enter the energy: '))
        target_type = input('Enter the target energy type (Joule, Kilojoule, Calorie, Kilocalorie, Electronvolt, British Thermal Unit, Foot-pound, Erg, Watt-hour, Kilowatt-hour, Megawatt-hour, Gigawatt-hour): ')
        
        energy_converter = EnergyConverter(energy_type, energy)
        converted_energy = energy_converter.convert(target_type)
        print(f'The converted energy is {converted_energy:.2f} {target_type}')
        break
    except ValueError as e:
        print(e)
