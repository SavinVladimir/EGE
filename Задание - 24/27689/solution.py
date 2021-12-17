# https://inf-ege.sdamgia.ru/problem?id=27689

"""
Текстовый файл состоит не более чем из 10^6 символов X, Y и Z.  Определите максимальную длину цепочки вида XYZXYZXYZ...
(составленной из фрагментов XYZ, последний фрагмент может быть неполным).
"""

import re

f = open('24_27689.txt', 'r')
line = f.readline()


def find(s: str):
    k = str(max(re.findall('((XYZ)+(X|XY)?)', s))).split()
    return k[0]


def processing(s: str):
    k = re.sub("[()',]", '', s)
    return k

print(len(processing(find(line))))


