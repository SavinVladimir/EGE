# https://inf-ege.sdamgia.ru/problem?id=27695

"""
Текстовый файл состоит не более чем из 106 символов L, D и R. Определите максимальное количество идущих подряд
символов, среди которых каждые два соседних различны.
"""

f = open('24_27695.txt', 'r')
s = f.readline()

k = 1
maxx = 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 1

print(maxx)

# 45
