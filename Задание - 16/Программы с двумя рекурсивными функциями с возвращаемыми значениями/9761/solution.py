# https://inf-ege.sdamgia.ru/problem?id=9761

"""
Чему будет равно значение, вычисленное при выполнении вызова F(7)?
"""


def F(n):

    if n > 2:

        return F(n-1)+ G(n-2)

    else:
        return 1


def G(n):

    if n > 2:

        return G(n-1) + F(n-2)

    else:
        return 1

print(F(7))

# 13
