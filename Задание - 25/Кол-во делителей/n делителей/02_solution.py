"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [190201; 190220], числа, имеющие
ровно 4 различных делителя. В ответе для каждого найденного числа запишите два его наибольших
делителя в порядке убывания.
"""


for i in range(190201, 190221):
    k = 0
    a = []
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
            if k > 4:
                break
            a.append(j)

    if k == 4:
        print(a[3], a[2], end=" ")
