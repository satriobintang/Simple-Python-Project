MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

class MorseCodeTranslator:
    def __init__(self):
        pass
    
    def text_to_morse(self, text):
        morse_code = ''
        for char in text.upper():
            if char == ' ':
                morse_code += ' '
            else:
                morse_code += MORSE_CODE_DICT[char] + ' '
        return morse_code
    
    def morse_to_text(self, morse_code):
        morse_code += ' '
        text = ''
        morse_char = ''
        for char in morse_code:
            if char != ' ':
                morse_char += char
            else:
                if morse_char in MORSE_CODE_DICT.values():
                    text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
                else:
                    text += ' '
                morse_char = ''
        return text


translator = MorseCodeTranslator()

text = input("Please enter a message: ")
morse_code = translator.text_to_morse(text)
print(f'Text: {text} \nMorse Code: {morse_code}')