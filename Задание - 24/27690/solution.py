# https://inf-ege.sdamgia.ru/problem?id=27690

"""
Текстовый файл состоит не более чем из 106 символов A, B и C.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
"""

f = open("zadanie24_1.txt")
s = f.read()
m = 1
k = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        k = k + 1
    else:
        if k > m:
            m = k
        k = 1
print(m)
