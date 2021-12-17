# https://inf-ege.sdamgia.ru/problem?id=16898

"""
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Прибавить 3
Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья увеличивает на 3.
Программа для исполнителя РазДваТри — это последовательность команд.
Сколько существует программ, которые преобразуют исходное число 2 в число 14 и
при этом траектория вычислений не содержит чисел 5 и 10?
"""


def k(x: int, y: int, d: int, t: int) -> int:
    if x == y:
        return 1
    if x > y or x == d or x == t:
        return 0

    return k(x + 1, y, d, t) + k(x * 2, y, d, t) + k(x + 3, y, d, t)

if __name__ == '__main__':
    print(k(2, 14, 5, 10))

# 26
