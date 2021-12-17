# https://inf-ege.sdamgia.ru/problem?id=27694

"""
Определите максимальную длину цепочки вида ABABAB...
(составленной из фрагментов AB, последний фрагмент может быть неполным).
"""

import re

with open('24_27694.txt', 'r') as f:
    print(max([len(i[0]) for i in re.findall('((AB)+(A)?)', f.read())]))

