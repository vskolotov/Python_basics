"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков:

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
    get_jokes(2)
    ["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random


def get_jokes(count_jokes):
    """
    the function creates jokes from words taken from three lists: noun, adverb, adjective
    :param count_jokes: type: int
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(count_jokes):
        jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    print(jokes)


get_jokes(8)
