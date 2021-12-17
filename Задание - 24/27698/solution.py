# https://inf-ege.sdamgia.ru/problem?id=27698

"""
Текстовый файл состоит не более чем из 106 символов L, D и R. Определите длину самой длинной последовательности,
состоящей из символов R. Хотя бы один символ R находится в последовательности.
"""

f = open('24_27698.txt', 'r')
s = f.readline()

k = 1
maxx = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1] and s[i] == 'R':
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 1

print(maxx)

# 1
