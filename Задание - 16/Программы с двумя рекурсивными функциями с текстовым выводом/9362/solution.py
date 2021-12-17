# https://inf-ege.sdamgia.ru/problem?id=9362

"""
Сколько символов «звёздочка» будет напечатано на экране при выполнении вызова F(11)?
"""


def F(n):
    if n > 0:
        G(n - 1)


def G(n):
    print("*")
    if n > 1:
        F(n - 3)

print(F(11))

# 3
