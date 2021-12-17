with open('s1 (1).txt', 'r') as f:
    s = f.readlines()

k = 0

for i in s:
    if i.count('A') == i.count('B'):
        k += 1

print(k)
