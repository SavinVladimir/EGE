# https://inf-ege.sdamgia.ru/problem?id=36880

"""
Найдите все натуральные числа N, принадлежащие отрезку [400000000;600000000], которые можно представить в виде
N = 2^m · 3^n, где m — чётное число, n — нечётное число. В ответе запишите все найденные числа в порядке возрастания.
"""


for i in range(400000000, 600000000 + 1):
    k = i
    m = 0
    n = 0

    while k % 2 == 0:
        m += 1
        k = k // 2

    if m % 2 == 0 and m > 0:
        while k % 3 == 0:
            n += 1
            k = k // 3

    if n % 2 != 0 and k == 1:
        print(i)

# 408146688
# 452984832
# 516560652
# 573308928
