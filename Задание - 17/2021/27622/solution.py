# https://inf-ege.sdamgia.ru/problem?id=27622

"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [8812; 12285], которые делятся на 8 или 19 и
не делятся на 4, 9, 14, 16. Найдите количество таких чисел и максимальное из них.
В ответе запишите два целых числа без пробелов и других дополнительных символов:
сначала количество, затем максимальное число.
"""

k = 0
maxx = 0

for i in range(8812, 12285 + 1):
    if (i % 8 == 0 or i % 19 == 0) and (i % 4 != 0 and i % 9 != 0 and i % 14 != 0 and i % 16 != 0):
        k += 1
        if i > maxx:
            maxx = i

print(k, maxx, sep='')

# 11712274
