"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
 num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""


def num_translate(word):
    """
    the function translates English numbers into Russian
    :param word: type: string:
    """
    dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                  'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь',
                  'eight': 'восемь', 'nine': 'девять'}
    print(dictionary.get(word))


def num_translate_adv(word):
    """
    the function translates English numbers into Russian, taking into account the case of the first letter
    :param word: type: string:
    """
    dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                  'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь',
                  'eight': 'восемь', 'nine': 'девять'}
    if word.istitle():
        print(dictionary.get(word.lower()).title())
    else:
        print(dictionary.get(word))
    # print(dictionary.get(word))


num_translate('seven')
num_translate('two')
num_translate('twooo')
num_translate('nine')
print('-------')
num_translate_adv('ooo')
num_translate_adv('Nine')
num_translate_adv('five')
num_translate_adv('Six')
