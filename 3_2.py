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

def num_translate_adv(number):
    """Translate english numeral into russian"""
    if number in transleter:
         return transleter[number]
    else:
        number = number.lower()
        if number in transleter:
         return transleter[number].capitalize()
        else:
            return None

print(num_translate_adv('Two'))
print(num_translate_adv('One'))
print(num_translate_adv('nine'))
print(num_translate_adv('восемь'))