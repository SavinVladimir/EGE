"""
Вася составляет 5-буквенные слова, в которых есть только буквы С, Л, О, Н, причём буква С используется в каждом слове
ровно 1 раз. Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
"""

import itertools

s = 'СЛОН'
k = 0
for x in itertools.product(s, repeat=5):
    a = ''.join(x)
    if a.count('С') == 1:
        k += 1

print(k)
