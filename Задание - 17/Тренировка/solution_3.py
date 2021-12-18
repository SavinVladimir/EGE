p = 1
maxx = 0


def s(n: int) -> int:
    return n % 10 + n // 10 % 10

for i in range(1985, 8528 + 1):
    if s(i) == 6 and i % 2 != 0 and i % 7 != 0 and i % 47 != 0:
        p = p * i
        if i > maxx:
            maxx = i

print(maxx, p % 1000)
