"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [198577; 198888], числа, имеющие
ровно 6 различных делителя. В ответе для каждого найденного числа запишите два его наибольших
делителя в порядке возрастания.
"""


for i in range(198577, 198888 + 1):
    k = 0
    a = []
    for j in range(1, i+1):
        if i % j == 0:
            k = k + 1
            if k > 6:
                break
            a.append(j)

    if k == 6:
        print(a[4], a[5], end=' ')

