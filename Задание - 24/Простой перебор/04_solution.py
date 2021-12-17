with open('s1.txt', 'r') as f:
    s = f.readlines()

k = 0

for i in s:
    if i.count('C') > i.count('O'):
        k += 1

print(k)

# 436
