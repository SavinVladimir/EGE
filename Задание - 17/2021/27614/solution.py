# https://inf-ege.sdamgia.ru/problem?id=27614

"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [5883; 15906],
которые делятся на 9 или 23 и не делятся на 13, 18, 19, 22. Найдите количество таких чисел и максимальное из них.
В ответе запишите два целых числа без пробелов и других дополнительных символов:
 сначала количество, затем максимальное число.
"""

maxx = 0
k = 0

for i in range(5883, 15906 + 1):
    if (i % 9 == 0 or i % 23 == 0) and (i % 13 != 0 and i % 18 != 0 and i % 19 != 0 and i % 22 != 0):
        k += 1
        if i > maxx:
            maxx = i

print(k)
print(maxx)

print(k, maxx, sep='')

# 81015893
