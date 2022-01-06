print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not z and x) or (x and y and z):
                print(x, y, z)

"""
x y z
1 0 0
1 1 0
1 1 1
"""

# Ответ yzx
