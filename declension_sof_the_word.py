"""
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""
numbers = [0, 1, 3, 5, 11, 12, 21, 23, 26, 30, 55, 61, 79, 92, 97]

for num in numbers:
    if 4 < num < 21:
        print(num, 'процентов')
    else:
        remainder_of_division = num % 10
        if remainder_of_division == 1:
            print(num, 'процент')
        elif 1 < remainder_of_division < 5:
            print(num, 'процента')
        else:
            print(num, 'процентов')
