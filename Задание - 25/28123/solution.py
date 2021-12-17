# https://inf-ege.sdamgia.ru/problem?id=28123

"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [125256;125330], числа,
имеющие ровно шесть различных чётных натуральных делителей. Для каждого найденного числа запишите эти шесть делителей
в шесть соседних столбцов на экране с новой строки.
Делители в строке должны следовать в порядке возрастания.
"""


for i in range(125256, 125330 + 1):
    k = 0
    a = []
    for j in range(2, i + 1, 2):
        if i % j == 0 and j % 2 == 0:
            k += 1
            if k > 6:
                break
            a.append(j)

    if k == 6:
        for r in range(0, 6):
            print(a[r], end=' ')
        print('\n')

# 2 6 18 13918 41754 125262
# 2 4 8 31322 62644 125288
# 2 6 18 13922 41766 125298
