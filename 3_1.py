transleter = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
#print(transleter)

def num_translate(number):
    """Translate english numeral into russian"""
    if number in transleter:
         return (transleter[number])
    else:
        return None

print(num_translate('one'))
print(num_translate('two'))
print(num_translate('один'))

