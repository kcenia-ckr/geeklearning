
from random import choice

def get_jokes(n):
    jokes = ""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while n != 0:
        jokes += choice(nouns) + " "
        jokes += choice(adverbs) + " "
        jokes += choice(adjectives) + " " + '\n'
        n -= 1
    print(jokes)


get_jokes(3)