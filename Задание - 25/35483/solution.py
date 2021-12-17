# https://inf-ege.sdamgia.ru/problem?id=35483

"""
Найдите все натуральные числа, принадлежащие отрезку [35000000;40000000], у которых ровно пять различных нечётных
делителей (количество чётных делителей может быть любым). В ответе перечислите найденные числа в порядке возрастания.
"""


def is_prime(n):
    return all(n % i != 0 for i in range(2, n))


def numbers(m, n):
    i = 3
    while True:
        if is_prime(i):
            j = i ** 4
            if n < j:
                break
            while j <= n:
                if m <= j:
                    yield j
                j *= 2
        i += 2


print(*sorted(numbers(35_000_000, 40_000_000)), sep='\n')

