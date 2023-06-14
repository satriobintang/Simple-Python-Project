#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import requests

class CurrencyConverter:
    def __init__(self, amount, base_currency):
        self.amount = amount
        self.base_currency = base_currency
    
    def get_conversion_rate(self, target_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        data = response.json()
        
        if 'rates' in data and target_currency in data['rates']:
            return data['rates'][target_currency]
        else:
            raise ValueError('Invalid currency')
    
    def convert(self, target_currency):
        base_rate = self.get_conversion_rate(target_currency)
        target_rate = self.get_conversion_rate(self.base_currency)
        
        converted_amount = self.amount * (base_rate / target_rate)
        return converted_amount
    

# Glossary of currency terms
currency_terms = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'GBP': 'British Pound Sterling',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan',
    'HKD': 'Hong Kong Dollar',
    'NZD': 'New Zealand Dollar',
    'SEK': 'Swedish Krona',
    'KRW': 'South Korean Won',
    'SGD': 'Singapore Dollar',
    'NOK': 'Norwegian Krone',
    'MXN': 'Mexican Peso',
    'INR': 'Indian Rupee',
    'BRL': 'Brazilian Real',
    'RUB': 'Russian Ruble',
    'ZAR': 'South African Rand',
    'TRY': 'Turkish Lira',
    'IDR': 'Indonesian Rupiah',
    # Add other currencies as needed
}

while True:
    try:
        print('Available Currencies:')
        for currency_code, currency_name in currency_terms.items():
            print(f'{currency_code}: {currency_name}')
        
        base_currency = input('Enter the base currency: ').upper()
        amount = float(input('Enter the amount: '))
        target_currency = input('Enter the target currency: ').upper()
        
        if base_currency not in currency_terms or target_currency not in currency_terms:
            raise ValueError('Invalid currency')
        
        currency_converter = CurrencyConverter(amount, base_currency)
        converted_amount = currency_converter.convert(target_currency)
        print(f'The converted amount is {converted_amount:.2f} {target_currency}')
        break
    except ValueError as e:
        print(e)
