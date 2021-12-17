# https://inf-ege.sdamgia.ru/problem?id=33096

"""
Определите количество принадлежащих отрезку [3 · 10^10; 5 · 10^10] натуральных чисел, которые делятся на 11 и на 100 000
и при этом не делятся на 17, 23, 41 и 103, а также наименьшее из таких чисел.
В ответе запишите два целых числа: сначала количество, затем наименьшее число.
"""

k = 0
minn = 600000

for i in range(300000, 500000):
    if i % 11 == 0 and i % 17 != 0 and i % 23 != 0 and i % 41 != 0 and i % 103 !=0:
        k += 1
        if i < minn:
            minn = i

print(k, 100000 * minn, sep='')

# 1581530000300000
