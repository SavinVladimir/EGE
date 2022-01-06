print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not x and y) or (y and z):
                print(x, y, z)

"""
x y z
0 1 0
0 1 1
1 1 1
"""

# Ответ xyz
