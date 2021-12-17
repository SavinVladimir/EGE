# https://inf-ege.sdamgia.ru/problem?id=27686

"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, состоящей из символов X.
Хотя бы один символ X находится в последовательности.
"""

with open('24_27686.txt', 'r') as f:
    s = f.readline()
    k = 1
    maxx = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1] and s[i] == 'X':
            k += 1
            if k > maxx:
                maxx = k
        else:
            k = 1

    print(maxx)

# 19
