"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [568023;569230], число, имеющее
максимальное количество различных натуральных делителей, если таких чисел несколько — найдите минимальное из них.
Выведите на экран количество делителей такого числа и само число.
"""

# python залупа

import time

def main():
    start_time = time.time()

    number = 0
    kolvodelit = 0

    for i in range(568023, 569230 + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1

        if k > kolvodelit:
            kolvodelit = k
            number = i

    print(kolvodelit, number)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()

# 144 568260
