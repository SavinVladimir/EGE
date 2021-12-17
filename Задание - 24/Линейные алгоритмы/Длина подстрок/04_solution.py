with open('k7a-4.txt', 'r') as f:
    s = f.readline()

k = 0
m = 0

for i in range(0, len(s)):
    if s[i] != 'D':
        k += 1
        if k > m:
            m = k
    else:
        k = 0

print(m)
