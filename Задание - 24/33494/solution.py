# https://inf-ege.sdamgia.ru/problem?id=33494

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите
символ, который чаще всего встречается в файле сразу после буквы E.
"""

f = open('24_33494.txt', 'r')
s = f.readline()

d = dict()

for i in range(0, len(s)-1):
    if s[i] == 'E' and s[i+1] != 'E':
        if s[i+1] not in d:
            d[s[i+1]] = 1
        else:
            d[s[i+1]] += 1


sorted_values = sorted(d.values())
sorted_dict = {}

for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
            sorted_dict[k] = d[k]
            break

print(sorted_dict)

a = max(d, key=d.get)
print(a)

# Y
