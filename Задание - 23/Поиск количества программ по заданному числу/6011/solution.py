# https://inf-ege.sdamgia.ru/problem?id=6011

"""
У исполнителя Удвоитель две команды, которым присвоены номера:
1. прибавь 1,
2. умножь на 2.
Первая из них увеличивает число на экране на 1, вторая удваивает его.
Программа для Удвоителя — это последовательность команд. Сколько есть программ, которые число 2 преобразуют в число 22?
"""


def k(x: int, y: int) -> int:
    if x == y:
        return 1
    if x > y:
        return 0

    return k(x+1, y) + k(x*2, y)

if __name__ == '__main__':
    print(k(2, 22))

# 37

