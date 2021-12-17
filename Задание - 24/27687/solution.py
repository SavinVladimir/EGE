# https://inf-ege.sdamgia.ru/problem?id=27687

"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, состоящей из символов Y.
Хотя бы один символ Y находится в последовательности.
"""


with open('24.txt', 'r') as f:
    s = f.readline()
    k = 1
    kmax = 1

    for i in range(len(s) - 1):
        if s[i] == 'Y' and s[i+1] == 'Y':
            k += 1

            if k > kmax:
                kmax = k

        else:
            k = 1

print(kmax)

# 10

