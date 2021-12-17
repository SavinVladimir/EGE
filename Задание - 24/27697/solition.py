# https://inf-ege.sdamgia.ru/problem?id=27697

"""
Текстовый файл состоит не более чем из 106 символов L, D и R. Определите длину самой длинной последовательности,
состоящей из символов D. Хотя бы один символ D находится в последовательности.
"""

with open('24_27697.txt', 'r') as f:
    s = f.readline()

    k = 1
    maxx = 1

    for i in range(1, len(s)):
        if s[i] == 'D' and s[i - 1] == 'D':
            k += 1
            if k > maxx:
                maxx = k
        else:
            k = 1

print(maxx)

# 11


