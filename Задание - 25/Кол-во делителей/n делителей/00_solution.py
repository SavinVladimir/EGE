"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [198877; 198888], числа, имеющие
ровно 4 различных делителя. В ответе для каждого найденного числа запишите два его
наибольших делителя в порядке возрастания.
"""


def find_div(x):
    divs = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            divs.append(j)
            if j != x // j:
                divs.append(x // j)
    divs.sort()
    divs.reverse()
    return divs


for i in range(198877, 198889):
    a = find_div(i)
    if len(a) == 4:
        print(sorted(a[:2]))