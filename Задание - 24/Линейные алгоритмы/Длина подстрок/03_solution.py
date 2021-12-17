with open('j2.txt', 'r') as f:
    s = f.readline()

k = 1
m = 1

for i in range(0, len(s) - 1):
    if s[i] != s[i+1]:
        k += 1
        if k > m:
            m = k
    else:
        k = 1

print(m)
