# https://inf-ege.sdamgia.ru/problem?id=8099

"""
Сколько символов «звёздочка» будет напечатано на экране при выполнении вызова F(11)?
"""


def F(n):
    if n > 0:
        G(n - 1)


def G(n):
    print("*")

    if n > 1:
        F(n - 2)

print(F(11))

# 4
