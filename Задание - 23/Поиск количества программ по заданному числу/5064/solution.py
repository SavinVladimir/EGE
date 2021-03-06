# https://inf-ege.sdamgia.ru/problem?id=5064

"""
У исполнителя Удвоитель-Утроитель три команды, которым присвоены номера:
1. прибавь 1
2. умножь на 2
3. умножь на 3.
Первая из них увеличивает на 1 число на экране, вторая увеличивает это число в 2 раза, третья - в 3 раза.
Программа для Удвоителя-Утроителя — это последовательность команд. Сколько существует программ, которые
число 1 преобразуют в число 13?
"""


def k(x: int, y: int) -> int:
    if x == y:
        return 1
    if x > y:
        return 0
    return k(x+1, y) + k(x*2, y) + k(x*3, y)

if __name__ == '__main__':
    print(k(1, 13))

# 38
