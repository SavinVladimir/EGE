# https://inf-ege.sdamgia.ru/problem?id=27692

"""
Текстовый файл состоит не более чем из 106 символов A, B и C.
Определите максимальное количество идущих подряд символов B.
"""

f = open('24.txt', 'r')
s = f.readline()
k = 1
maxx = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1] and s[i] == 'B':
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 1

print(maxx)

