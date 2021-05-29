"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(src)
res = set()
tmp = set()
for el in src:
    if el not in tmp:
        res.add(el)
    else:
        res.discard(el)
    tmp.add(el)
result = [el for el in src if el in res]
print(result)
