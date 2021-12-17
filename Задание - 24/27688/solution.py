# https://inf-ege.sdamgia.ru/problem?id=27688

"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, состоящей из символов Z.
Хотя бы один символ Z находится в последовательности.
"""

with open('24.txt', 'r') as f:
    s = f.readline()
    k = 1
    kmax = 1

    for i in range(len(s) - 1):
        if s[i] == 'Z' and s[i+1] == 'Z':
            k += 1
            if k > kmax:
                kmax = k

        else:
            k = 1

print(kmax)

# 7
