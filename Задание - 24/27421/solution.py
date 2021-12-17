# https://inf-ege.sdamgia.ru/problem?id=27421

"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
"""

with open('24_27421.txt', 'r') as f:
    s = f.readline()
    k = 1
    kmax = 1

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            k += 1

            if k > kmax:
                kmax = k

        else:
            k = 1

print(kmax)

# 35

