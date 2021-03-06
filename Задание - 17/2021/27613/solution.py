# https://inf-ege.sdamgia.ru/problem?id=27613

"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [7525; 13486],
которые делятся на 7 и не делятся на 6, 9, 14, 21. Найдите количество таких чисел и минимальное из них.
В ответе запишите два целых числа без пробелов и других дополнительных символов:
сначала количество, затем минимальное число.
"""

minn = 20000
k = 0

for i in range(7525, 13486 + 1):
    if i % 7 == 0 and i % 6 != 0 and i % 9 != 0 and i % 14 != 0 and i % 21 != 0:
        k = k + 1
        if i < minn:
            minn = i

print(k, minn, sep='')

# 2847525
