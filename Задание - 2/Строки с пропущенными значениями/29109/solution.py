print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((z <= w) or (y == w)) and ((x or z) == y):
                    print(x, y, z, w)

"""
x y z w
0 0 0 0
0 0 0 1 - Подходит
0 1 1 1 - Подходит
1 1 0 0 - Подходит
1 1 0 1 - Подходит
1 1 1 1
"""

# Ответ - zyxw

