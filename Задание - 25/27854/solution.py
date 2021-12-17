# https://inf-ege.sdamgia.ru/problem?id=27854

"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [110203;110245], числа,
имеющие ровно четыре различных чётных натуральных делителя. Для каждого найденного числа запишите эти четыре делителя
в четыре соседних столбца на экране с новой строки.
Делители в строке должны следовать в порядке возрастания.
"""

import time

start_time = time.time()

for i in range(110203, 110245 + 1):
    k = 0
    a = []
    for j in range(2, i + 1, 2):
        if i % j == 0 and j % 2 == 0:
            k += 1
            if k > 4:
                break
            a.append(j)

    if k == 4:
        for r in range(len(a)):
            print(a[r], end=' ')
        print()

print("--- %s seconds ---" % (time.time() - start_time))


# 2 4 55102 110204
# 2 14 15746 110222
# 2 6 36742 110226
# 2 22 10022 110242
