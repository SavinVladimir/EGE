# https://inf-ege.sdamgia.ru/problem?id=27699

"""
Текстовый файл состоит не более чем из 106 символов L, D и R. Определите максимальную длину цепочки вида LDRLDRLDR...
(составленной из фрагментов LDR, последний фрагмент может быть неполным).
"""

import re

f = open('24_27699.txt',  'r')
s = f.readline()


def find(a: str):
    b = str(max(re.findall('((LDR)+(L|LD)?)', a))).split()
    return str(b[0])


def processing(x: str):
    x = re.sub("[(),' ]", '', x)
    return x

k = processing(find(s))
print(len(k))




