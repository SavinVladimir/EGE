# https://inf-ege.sdamgia.ru/problem?id=7695

"""
Чему будет равно значение, вычисленное алгоритмом при выполнении вызова F(6)?
"""


def F(n):
    if n > 2:
        return F(n-1) + F(n-2)
    else:
        return 1

print(F(6))

# 8
