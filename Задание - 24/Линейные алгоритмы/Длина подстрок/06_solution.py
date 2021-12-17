with open('j7.txt', 'r') as f:
    s = f.readline()

k = 0
m = 0

for i in range(0, len(s)):
    if int(s[i]) % 2 == 0:
        k += 1
        if k > m:
            m = k
    else:
        k = 0

print(m)
