"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def odd_nums(num):
    for odd_num in range(1, num + 1, 2):
        yield odd_num


odd_to_15 = odd_nums(15)
for i in range(9):
    print(next(odd_to_15))
