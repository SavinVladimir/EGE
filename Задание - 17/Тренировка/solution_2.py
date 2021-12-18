k = 0
minn = 15000

for i in range(1098, 13765+1):
    if i % 2 == 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 23 != 0:
        k += 1
        if i < minn:
            minn = i

print(k, minn, sep='')
