# https://inf-ege.sdamgia.ru/problem?id=33769

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще
всего встречается в файле после двух одинаковых символов.
Например, в тексте CCCBBABAABCC есть комбинации CCC, CCB, BBA и AAB. Чаще всего — 2 раза — после двух
одинаковых символов стоит B, в ответе для этого случая надо написать B.
"""

f = open('24_33769.txt', 'r')
s = f.readline()

d = dict()

for i in range(2, len(s) - 2):
    if s[i-2] == s[i-1] and s[i] != s[i-1]:
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1

print(d)

a = max(d, key=d.get)
print(a)

# K
