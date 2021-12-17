# https://inf-ege.sdamgia.ru/problem?id=13606

"""
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
Первая команда увеличивает число на экране на 1, вторая – умножает его на 2, третья – умножает на 3.
Программа для исполнителя А17 – это последовательность команд.
Сколько существует программ, для которых при исходном числе 2 результатом является число 28 и при этом траектория
вычислений содержит число 14?
"""


def k(x: int, y: int) -> int:
    if x == y:
        return 1
    if x > y:
        return 0

    return k(x+1, y) + k(x*2, y) + k(x*3, y)

if __name__ == '__main__':
    print(k(2, 14) * k(14, 28))

# 38

