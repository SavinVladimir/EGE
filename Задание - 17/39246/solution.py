# https://inf-ege.sdamgia.ru/problem?id=39246

"""
Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой два идущих подряд
элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их
сумма делится на 7.
В ответе запишите два числа: сначала количество найденных пар, а затем— максимальную сумму элементов таких пар.
"""

with open('17.txt', 'r') as f:
    n = f.readlines()

k = 0
maxx = 0

for i in range(0, len(n) - 1):
    if ((int(n[i]) + int(n[i+1])) % 7 == 0) and (int(n[i]) % 5 == 0 or int(n[i+1]) % 5 == 0):
        k += 1
        if int(n[i]) + int(n[i+1]) > maxx:
            maxx = int(n[i]) + int(n[i+1])

print(k, maxx)

