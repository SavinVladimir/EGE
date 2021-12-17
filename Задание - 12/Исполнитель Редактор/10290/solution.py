# https://inf-ege.sdamgia.ru/problem?id=10290

"""
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из цифры 1, за которой
следуют 80 идущих подряд цифр 8? В ответе запишите полученную строку.

НАЧАЛО
  ПОКА нашлось (18) ИЛИ нашлось (288) ИЛИ нашлось (3888)
    ЕСЛИ нашлось (18)
      ТО заменить (18, 2)
      ИНАЧЕ ЕСЛИ нашлось (288)
        ТО заменить (288, 3)
        ИНАЧЕ заменить (3888, 1)
      КОНЕЦ ЕСЛИ
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ
"""


s = '1' + '8' * 80

while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    elif '288' in s:
        s = s.replace('288', '3', 1)
    else:
        s = s.replace('3888', '1', 1)

print(s)




