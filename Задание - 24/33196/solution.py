# https://inf-ege.sdamgia.ru/problem?id=33196

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего
встречается в файле сразу после буквы A.Например, в тексте ABCAABADDD после буквы A два раза стоит B,
по одному разу — A и D. Для этого текста ответом будет B.
"""

f = open('24_33196.txt', 'r')
s = f.readline()

d = dict()

for i in range(len(s)-1):
    if s[i] == 'A' and s[i+1] != 'A':
        if s[i+1] not in d:
            d[s[i+1]] = 1
        else:
            d[s[i+1]] += 1

max_key = max(d, key=d.get)

print(max_key)

# G
