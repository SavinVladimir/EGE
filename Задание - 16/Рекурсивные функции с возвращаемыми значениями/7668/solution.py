# https://inf-ege.sdamgia.ru/problem?id=7668

"""
Чему будет равно значение, вычисленное алгоритмом при выполнении вызова F(5)?
"""


def F(n):
    if n > 2:
        return F(n-1) + F(n-2)
    else:
        return 1

print(F(5))

# 5
