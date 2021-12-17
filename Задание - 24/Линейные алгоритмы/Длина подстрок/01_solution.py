with open('k7a-1.txt', 'r') as f:
    s = f.readline()

k = 0
maximum = 0

for sym in s:
    if sym == 'A' or sym == 'B' or sym == 'C':
        k += 1
        if k > maximum:
            maximum = k
    else:
        k = 0
print(maximum)
