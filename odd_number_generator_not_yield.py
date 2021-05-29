"""
Написать генератор нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
"""

num = int(input())
odd_to_n = (odd_num for odd_num in range(1, num + 1, 2))

for i in range(num // 2 + 1):
    print(next(odd_to_n))
