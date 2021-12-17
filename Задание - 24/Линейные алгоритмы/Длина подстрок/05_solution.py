with open('k7a-6.txt', 'r') as f:
    s = f.readline()

k = 0
m = 0

for i in range(0, len(s)):
    if s[i] != 'A' and s[i] != 'E':
        k += 1
        if k > m:
            m = k
    else:
        k = 0

print(m)
