# https://inf-ege.sdamgia.ru/problem?id=37152

"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [12972;89322], которые при делении на 13 дают
остаток 7, при этом не делятся ни на 7, ни на 11. Найдите наибольшее из таких чисел и их количество.
В ответе укажите два числа друг за другом без разделительных знаков — сначала количество найденных чисел, затем
наибольшее найденное число.
"""

k = 0
maxx = 0

for i in range(12972, 89322 + 1):
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        k += 1
        if i > maxx:
            maxx = i

print(k, maxx, sep='')

# 457689317
