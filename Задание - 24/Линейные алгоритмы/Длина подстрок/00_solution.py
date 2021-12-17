with open('k7.txt', 'r') as f:
    s = f.readline()

m = 1
k = 1

for i in range(0, len(s)-1):
    if s[i] == s[i+1] and s[i] == 'B':
        k += 1
        if k > m:
            m = k
    else:
        k = 1

print(m)
