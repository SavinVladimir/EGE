print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) and (y <= w)) or (z == (x or y))) == False:
                    print(x, y, z, w)

"""
x y z w
0 1 0 0
1 0 0 0
1 0 0 1
1 1 0 0
"""

# Ответ ywzx
